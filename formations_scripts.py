# Formations for Warband by Motomataru
# rel. 01/03/11

from header_common import *
from header_operations import *
from module_constants import *
from header_parties import *
from header_skills import *
from header_mission_templates import *
from header_items import *
from header_triggers import *
from header_terrain_types import *
from header_music import *
from ID_animations import *

####################################################################################################################
# scripts is a list of script records.
# Each script record contns the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################


scripts = [
# #Formations Scripts	    #EDITED FOR MANY DIVISIONS BY CABA'DRIN - ROUGH, NEED TO MOVE EXTRA DIVS AROUND - REWORKED
  # script_cf_formation v2 by motomataru
  # Input: team, troop class, spacing, formation type
  # Output: reg0 number of troops in formation, pos61 formation position
  # Formation(s) form near team leader (player)
  ("cf_formation", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fclass", 2),
	(store_script_param, ":formation_extra_spacing", 3),
	(store_script_param, ":fformation", 4),
	(team_get_leader, ":fleader", ":fteam"),
	(gt, ":fleader", -1),	#any team members left?
	(agent_get_position, pos1, ":fleader"),
	(try_begin),
		(eq, "$autorotate_at_player", 1),
		(call_script, "script_team_get_position_of_enemies", pos60, ":fteam", grc_everyone),
		(neq, reg0, 0),	#more than 0 enemies still alive?
		(call_script, "script_point_y_toward_position", pos1, pos60),
	(try_end),
	
	(call_script, "script_cf_valid_formation_division", ":fteam", ":fclass", ":fformation"),
	(assign, ":num_troops", reg0),
	(assign, ":sd_type", reg1),
	
	(try_begin),
		#(eq, ":fclass", grc_cavalry),
		(this_or_next|eq, ":sd_type", sdt_cavalry),
		(eq, ":sd_type", sdt_harcher),
		(position_move_x, pos1, 500),		#cavalry set up 5m RIGHT of leader
		(try_begin),
		    (eq, ":sd_type", sdt_harcher),
			(position_move_x, pos1, 500),  #5m further RIGHT
			(position_move_y, pos1, -500), #5m BACK
		(try_end),
		(copy_position, pos61, pos1),
		(call_script, "script_form_cavalry", ":fteam", ":fleader", ":fclass", ":formation_extra_spacing"),
	(else_try),
		#(eq, ":fclass", grc_infantry),
		(this_or_next|eq, ":sd_type", sdt_infantry),
		(eq, ":sd_type", sdt_polearm),
		(position_move_x, pos1, -100),		#infantry set up 1m LEFT of leader
		(try_begin),
		    (eq, ":sd_type", sdt_polearm),
			(position_move_x, pos1, 100), #Re-center
			(position_move_y, pos1, 300), #3m FRONT
		(try_end),
		(copy_position, pos61, pos1),
		(call_script, "script_form_infantry", ":fteam", ":fleader", ":fclass", ":formation_extra_spacing", ":fformation"),
		(call_script, "script_get_centering_amount", ":fformation", ":num_troops", ":formation_extra_spacing"),
		(val_mul, reg0, -1),
		(position_move_x, pos61, reg0, 0),
	(else_try),
		(this_or_next|eq, ":sd_type", sdt_archer),
		(eq, ":sd_type", sdt_skirmisher),
		(position_move_y, pos1, 1000),		#archers set up 10m FRONT of leader
		(try_begin),
			(eq, ":sd_type", sdt_skirmisher),
			(position_move_y, pos1, 200), #2m further forward
		(try_end),
		(copy_position, pos61, pos1),
		(call_script, "script_get_centering_amount", formation_default, ":num_troops", ":formation_extra_spacing"),
		(val_mul, reg0, -1),
		(position_move_x, pos1, reg0, 0),
		(call_script, "script_form_archers", ":fteam", ":fleader", ":fclass", ":formation_extra_spacing", ":fformation"),
	(try_end),

#	(team_set_order_position, ":fteam", ":fclass", pos61),
	(call_script, "script_set_formation_position", ":fteam", ":fclass", pos61),
	(assign, reg0, ":num_troops"),
  ]),
   
  # script_form_cavalry v2 by motomataru #EDITED FOR MANY DIVISIONS BY CABA'DRIN
  # Input: team, agent number of team leader, battle group/troop class, spacing
  # Output: reg0 troop count
  # Form in wedge, (now not) excluding horse archers
  # Creates formation starting at pos1
  ("form_cavalry", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fleader", 2),
	(store_script_param, ":fclass", 3),
	(store_script_param, ":formation_extra_spacing", 4),
	(store_mul, ":extra_space", ":formation_extra_spacing", 50),
	(store_add, ":x_distance", 150, ":extra_space"),
	(store_add, ":y_distance", 250, ":extra_space"),		#larger y minimum distance to accommodate mounts
	(assign, ":max_level", 0),
	(try_for_agents, ":agent"),
		(call_script, "script_cf_valid_formation_member", ":fteam", ":fclass", ":fleader", ":agent"),
		(agent_get_troop_id, ":troop_id", ":agent"),
		(store_character_level, ":troop_level", ":troop_id"),
		(gt, ":troop_level", ":max_level"),
		(assign, ":max_level", ":troop_level"),
	(end_try),
	(assign, ":column", 1),
	(assign, ":rank_dimension", 1),
	(store_mul, ":neg_y_distance", ":y_distance", -1),
	(store_mul, ":neg_x_distance", ":x_distance", -1),
	(store_div, ":wedge_adj", ":x_distance", 2),
	(store_div, ":neg_wedge_adj", ":neg_x_distance", 2),
	(assign, ":troop_count", 0),
	(val_add, ":max_level", 1),
	(assign, ":form_left", 1),
	(assign, ":first_member", -1),
	(try_for_range_backwards, ":rank_level", 0, ":max_level"),	#put troops with highest exp in front
		(try_for_agents, ":agent"),
			(agent_get_troop_id, ":troop_id", ":agent"),
			(store_character_level, ":troop_level", ":troop_id"),
			(eq, ":troop_level", ":rank_level"),				
			(call_script, "script_cf_valid_formation_member", ":fteam", ":fclass", ":fleader", ":agent"),
			(val_add, ":troop_count", 1),
			(try_begin),
			    (eq, ":first_member", -1),
				(assign, ":first_member", ":agent"),
				(store_add, ":slot", slot_team_d0_first_member, ":fclass"),
		        (team_set_slot, ":fteam", ":slot", ":first_member"),
			(try_end),
			(agent_set_scripted_destination, ":agent", pos1, 1),
			(try_begin),
				(eq, ":form_left", 1),
				(position_move_x, pos1, ":neg_x_distance", 0),
			(else_try),
				(position_move_x, pos1, ":x_distance", 0),
			(try_end),
			(val_add, ":column", 1),
			(gt, ":column", ":rank_dimension"),
			(position_move_y, pos1, ":neg_y_distance", 0),
			(try_begin),
				(neq, ":form_left", 1),
				(assign, ":form_left", 1),
				(position_move_x, pos1, ":neg_wedge_adj", 0),
			(else_try),
				(assign, ":form_left", 0),
				(position_move_x, pos1, ":wedge_adj", 0),
			(try_end),			
			(assign, ":column", 1),
			(val_add, ":rank_dimension", 1),
		(end_try),
	(end_try),
	(try_begin),
		(eq, ":first_member", -1), #To preserver the possbility of a -1 result if the above all fails
		(store_add, ":slot", slot_team_d0_first_member, ":fclass"),
		(team_set_slot, ":fteam", ":slot", ":first_member"),
	(try_end),
	(assign, reg0, ":troop_count")
  ]),
	   
  # script_form_archers v2 by motomataru #EDITED FOR MANY DIVISIONS BY CABA'DRIN
  # Input: team, agent number of team leader, battle group/troop class, spacing, formation
  # Output: reg0 troop count
  # Form in staggered line both directions
  # Creates formation starting at pos1
  ("form_archers", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fleader", 2),
	(store_script_param, ":fclass", 3),
	(store_script_param, ":formation_extra_spacing", 4),
	(store_script_param, ":archers_formation", 5),
	(store_mul, ":extra_space", ":formation_extra_spacing", 50),
	(store_add, ":distance", formation_minimum_spacing, ":extra_space"),		#minimum distance between troops
	(assign, ":troop_count", 0),
	(assign, ":total_move_y", 0),	#staggering variable	
	(assign, ":first_member", -1),
	(try_for_agents, ":agent"),
		(call_script, "script_cf_valid_formation_member", ":fteam", ":fclass", ":fleader", ":agent"),
		(try_begin),
			(eq, ":first_member", -1),
			(assign, ":first_member", ":agent"),
			(store_add, ":slot", slot_team_d0_first_member, ":fclass"),
			(team_set_slot, ":fteam", ":slot", ":first_member"),
		(try_end),
		(agent_set_scripted_destination, ":agent", pos1, 1),
		(position_move_x, pos1, ":distance", 0),
		(try_begin),
			(eq, ":archers_formation", formation_ranks),
			(val_add, ":total_move_y", 75),
			(try_begin),
				(le, ":total_move_y", 150),
				(position_move_y, pos1, 75, 0),
			(else_try),
				(position_move_y, pos1, -150, 0),
				(assign, ":total_move_y", 0),
			(try_end),
		(try_end),
		(val_add, ":troop_count", 1),
	(try_end),
	(try_begin),
		(eq, ":first_member", -1), #To preserver the possibility of a -1 result if the above all fails
		(store_add, ":slot", slot_team_d0_first_member, ":fclass"),
		(team_set_slot, ":fteam", ":slot", ":first_member"),
	(try_end),
	(assign, reg0, ":troop_count")
  ]),
	   
  # script_form_infantry v2 by motomataru #EDITED FOR MANY DIVISIONS BY CABA'DRIN
  # Input: (pos1), team, agent number of team leader, battle group/troop class, spacing, formation
  # Output: reg0 troop count
  # If input "formation" is formation_default, will select a formation based on faction
  # Creates formation starting at pos1
  ("form_infantry", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fleader", 2),
	(store_script_param, ":fclass", 3),
	(store_script_param, ":formation_extra_spacing", 4),
	(store_script_param, ":infantry_formation", 5),
	(store_mul, ":extra_space", ":formation_extra_spacing", 50),
	(store_add, ":distance", formation_minimum_spacing, ":extra_space"),		#minimum distance between troops	
	(store_mul, ":neg_distance", ":distance", -1),
	(store_add, ":slot", slot_team_d0_size, ":fclass"), #battlegroup_get_size phase out
	(team_get_slot, ":num_troops", ":fteam", ":slot"),
	(assign, ":troop_count", ":num_troops"),
	(try_begin),
		(eq, ":infantry_formation", formation_default),
		(call_script, "script_get_default_formation", ":fteam"),
		(assign, ":infantry_formation", reg0),
	(try_end),
	(assign, ":form_left", 1),
	(assign, ":column", 1),
	(assign, ":rank", 1),

	(assign, ":first_member", -1),
	(try_begin),
		(eq, ":infantry_formation", formation_square),
		(convert_to_fixed_point, ":num_troops"),
		(store_sqrt, ":square_dimension", ":num_troops"),
		(convert_from_fixed_point, ":square_dimension"),
		(val_add, ":square_dimension", 1),

		(try_for_agents, ":agent"),
			(call_script, "script_cf_valid_formation_member", ":fteam", ":fclass", ":fleader", ":agent"),
			(try_begin),
				(eq, ":first_member", -1),
				(assign, ":first_member", ":agent"),
				(store_add, ":slot", slot_team_d0_first_member, ":fclass"),
				(team_set_slot, ":fteam", ":slot", ":first_member"),
			(try_end),
			(agent_set_scripted_destination, ":agent", pos1, 1),
			(try_begin),
			    (store_add, ":slot", slot_team_d0_order_weapon, ":fclass"), #PBOD
				(team_get_slot, reg0, ":fteam", ":slot"), #PBOD
				(eq, reg0, clear), #PBOD - Weapon Order "Clear"
				(this_or_next|eq, ":rank", 1),
				(this_or_next|ge, ":rank", ":square_dimension"),
				(this_or_next|eq, ":column", 1),
				(ge, ":column", ":square_dimension"),
				(call_script, "script_equip_best_melee_weapon", ":agent", 0, 0),
			(else_try),
			    (eq, reg0, clear), #PBOD - Weapon Order "Clear"
				(call_script, "script_equip_best_melee_weapon", ":agent", 0, 1),
			(try_end),
			(try_begin),
				(eq, ":form_left", 1),
				(position_move_x, pos1, ":neg_distance", 0),
			(else_try),
				(position_move_x, pos1, ":distance", 0),
			(try_end),
			(val_add, ":column", 1),
			(gt, ":column", ":square_dimension"),
			(position_move_y, pos1, ":neg_distance", 0),
			(try_begin),
				(neq, ":form_left", 1),
				(assign, ":form_left", 1),
				(position_move_x, pos1, ":neg_distance", 0),
			(else_try),
				(assign, ":form_left", 0),
				(position_move_x, pos1, ":distance", 0),
			(try_end),			
			(assign, ":column", 1),		
			(val_add, ":rank", 1),
		(end_try),
		
	(else_try),
		(eq, ":infantry_formation", formation_wedge),
		(assign, ":max_level", 0),
		(try_for_agents, ":agent"),
			(call_script, "script_cf_valid_formation_member", ":fteam", ":fclass", ":fleader", ":agent"),
			(agent_get_troop_id, ":troop_id", ":agent"),
			(store_character_level, ":troop_level", ":troop_id"),
			(gt, ":troop_level", ":max_level"),
			(assign, ":max_level", ":troop_level"),
		(end_try),

		(assign, ":rank_dimension", 1),
		(store_div, ":wedge_adj", ":distance", 2),
		(store_div, ":neg_wedge_adj", ":neg_distance", 2),
		(val_add, ":max_level", 1),
		(try_for_range_backwards, ":rank_level", 0, ":max_level"),	#put troops with highest exp in front
			(try_for_agents, ":agent"),
				(agent_get_troop_id, ":troop_id", ":agent"),
				(store_character_level, ":troop_level", ":troop_id"),
				(eq, ":troop_level", ":rank_level"),				
				(call_script, "script_cf_valid_formation_member", ":fteam", ":fclass", ":fleader", ":agent"),
				(try_begin),
					(eq, ":first_member", -1),
					(assign, ":first_member", ":agent"),
					(store_add, ":slot", slot_team_d0_first_member, ":fclass"),
					(team_set_slot, ":fteam", ":slot", ":first_member"),
				(try_end),
				(agent_set_scripted_destination, ":agent", pos1, 1),
				(try_begin),
				    (store_add, ":slot", slot_team_d0_order_weapon, ":fclass"), #PBOD
				    (team_get_slot, reg0, ":fteam", ":slot"), #PBOD
			        (eq, reg0, clear), #PBOD - Weapon Order "Clear"
					(this_or_next|eq, ":column", 1),
					(ge, ":column", ":rank_dimension"),
					(call_script, "script_equip_best_melee_weapon", ":agent", 0, 0),
				(else_try),
			        (eq, reg0, clear), #PBOD - Weapon Order "Clear"
					(call_script, "script_equip_best_melee_weapon", ":agent", 0, 1),
				(try_end),
				(try_begin),
					(eq, ":form_left", 1),
					(position_move_x, pos1, ":neg_distance", 0),
				(else_try),
					(position_move_x, pos1, ":distance", 0),
				(try_end),
				(val_add, ":column", 1),
				(gt, ":column", ":rank_dimension"),
				(position_move_y, pos1, ":neg_distance", 0),
				(try_begin),
					(neq, ":form_left", 1),
					(assign, ":form_left", 1),
					(position_move_x, pos1, ":neg_wedge_adj", 0),
				(else_try),
					(assign, ":form_left", 0),
					(position_move_x, pos1, ":wedge_adj", 0),
				(try_end),			
				(assign, ":column", 1),
				(val_add, ":rank_dimension", 1),
			(end_try),
		(end_try),
		
	(else_try),
		(eq, ":infantry_formation", formation_ranks),
		(store_div, ":rank_dimension", ":num_troops", 3),		#basic three ranks
		(val_add, ":rank_dimension", 1),		
		(assign, ":max_level", 0),
		(try_for_agents, ":agent"),
			(call_script, "script_cf_valid_formation_member", ":fteam", ":fclass", ":fleader", ":agent"),
			(agent_get_troop_id, ":troop_id", ":agent"),
			(store_character_level, ":troop_level", ":troop_id"),
			(gt, ":troop_level", ":max_level"),
			(assign, ":max_level", ":troop_level"),
		(end_try),


		(val_add, ":max_level", 1),
		(try_for_range_backwards, ":rank_level", 0, ":max_level"),	#put troops with highest exp in front
			(try_for_agents, ":agent"),
				(agent_get_troop_id, ":troop_id", ":agent"),
				(store_character_level, ":troop_level", ":troop_id"),
				(eq, ":troop_level", ":rank_level"),				
				(call_script, "script_cf_valid_formation_member", ":fteam", ":fclass", ":fleader", ":agent"),
				(try_begin),
					(eq, ":first_member", -1),
					(assign, ":first_member", ":agent"),
					(store_add, ":slot", slot_team_d0_first_member, ":fclass"),
					(team_set_slot, ":fteam", ":slot", ":first_member"),
				(try_end),
				(agent_set_scripted_destination, ":agent", pos1, 1),
				(try_begin),
				    (store_add, ":slot", slot_team_d0_order_weapon, ":fclass"), #PBOD
				    (team_get_slot, reg0, ":fteam", ":slot"), #PBOD
			        (eq, reg0, clear), #PBOD - Weapon Order "Clear"
					(eq, ":rank", 1),
					(call_script, "script_equip_best_melee_weapon", ":agent", 0, 0),
				(else_try),
			        (eq, reg0, clear), #PBOD - Weapon Order "Clear"
					(call_script, "script_equip_best_melee_weapon", ":agent", 0, 1),
				(try_end),
				(try_begin),
					(eq, ":form_left", 1),
					(position_move_x, pos1, ":neg_distance", 0),
				(else_try),
					(position_move_x, pos1, ":distance", 0),
				(try_end),
				(val_add, ":column", 1),

				(gt, ":column", ":rank_dimension"),	#next rank?
				(position_move_y, pos1, ":neg_distance", 0),
				(try_begin),
					(neq, ":form_left", 1),
					(assign, ":form_left", 1),
					(position_move_x, pos1, ":neg_distance", 0),
				(else_try),
					(assign, ":form_left", 0),
					(position_move_x, pos1, ":distance", 0),
				(try_end),			
				(assign, ":column", 1),
				(val_add, ":rank", 1),
			(end_try),
		(end_try),
		
	(else_try),
		(eq, ":infantry_formation", formation_shield),
		(store_div, ":rank_dimension", ":num_troops", 3),		#basic three ranks
		(val_add, ":rank_dimension", 1),		
		#prep with longest weapons, force shields
		# (try_for_agents, ":agent"),
			# (call_script, "script_cf_valid_formation_member", ":fteam", ":fclass", ":fleader", ":agent"),
			# (call_script, "script_equip_best_melee_weapon", ":agent", 1, 1),
		# (end_try),
		(assign, ":first_second_rank_agent", -1),
		(assign, ":min_len_non_shielded", -1),
		(try_for_range, ":weap_group", 0, 3),
			(store_mul, ":min_len", ":weap_group", Third_Max_Weapon_Length),
			(store_add, ":max_len", ":min_len", Third_Max_Weapon_Length),
			(try_begin),
				(gt, ":min_len_non_shielded", -1),	#looped through agents at least once since rank 2
				(assign, ":min_len_non_shielded", ":min_len"),
			(try_end),
			(try_for_agents, ":agent"),
				(call_script, "script_cf_valid_formation_member", ":fteam", ":fclass", ":fleader", ":agent"),
				(agent_get_wielded_item, ":agent_weapon", ":agent", 0),
				(try_begin),
					(gt, ":agent_weapon", itm_no_item),
					(item_get_slot, ":weapon_length", ":agent_weapon", slot_item_length),
				(else_try),
					(assign, ":weapon_length", 0),
				(try_end),
				(try_begin),
					(gt, ":rank", 1),
					(try_begin),
						(eq, ":first_second_rank_agent", ":agent"),	#looped through agents at least once since rank 2
						(assign, ":min_len_non_shielded", ":min_len"),
					(else_try),
						(eq, ":first_second_rank_agent", -1),
						(assign, ":first_second_rank_agent", ":agent"),
					(try_end),
					(store_add, ":slot", slot_team_d0_order_weapon, ":fclass"), #PBOD
				    (team_get_slot, reg0, ":fteam", ":slot"), #PBOD
			        (eq, reg0, clear), #PBOD - Weapon Order "Clear"
					(ge, ":weapon_length", ":min_len"),	#avoid reequipping agents that are already in formation
					(eq, ":min_len_non_shielded", -1),	#haven't looped through agents at least once since rank 2
					(call_script, "script_equip_best_melee_weapon", ":agent", 0, 1),	#longest weapon, including two-handed
					(agent_get_wielded_item, ":agent_weapon", ":agent", 0),
					(try_begin),
						(gt, ":agent_weapon", itm_no_item),
						(item_get_slot, ":weapon_length", ":agent_weapon", slot_item_length),
					(else_try),
						(assign, ":weapon_length", 0),
					(try_end),
				(try_end),				
				(assign, ":form_up", 0),
				(agent_get_wielded_item, ":agent_shield", ":agent", 1),
				(try_begin),
					(gt, ":agent_shield", itm_no_item),
					(item_get_type, reg0, ":agent_shield"),
					(eq, reg0, itp_type_shield),
					(try_begin),
						(is_between, ":weapon_length", ":min_len", ":max_len"),
						(assign, ":form_up", 1),
					(try_end),
				(else_try),
					(gt, ":rank", 1),
					(is_between, ":weapon_length", ":min_len_non_shielded", ":max_len"),
					(assign, ":form_up", 1),
				(try_end),

				(eq, ":form_up", 1),
				(try_begin),
					(eq, ":first_member", -1),
					(assign, ":first_member", ":agent"),
					(store_add, ":slot", slot_team_d0_first_member, ":fclass"),
					(team_set_slot, ":fteam", ":slot", ":first_member"),
				(try_end),
				(agent_set_scripted_destination, ":agent", pos1, 1),
				(try_begin),
					(store_add, ":slot", slot_team_d0_order_weapon, ":fclass"), #PBOD
				    (team_get_slot, reg0, ":fteam", ":slot"), #PBOD
			        (eq, reg0, clear), #PBOD - Weapon Order "Clear"
					(eq, ":rank", 1),
					(call_script, "script_equip_best_melee_weapon", ":agent", 1, 0),	#best weapon, force shield
				(try_end),
				(try_begin),
					(eq, ":form_left", 1),
					(position_move_x, pos1, ":neg_distance", 0),
				(else_try),
					(position_move_x, pos1, ":distance", 0),
				(try_end),
				(val_add, ":column", 1),
				
				(gt, ":column", ":rank_dimension"),	#next rank?
				(position_move_y, pos1, ":neg_distance", 0),
				(try_begin),
					(neq, ":form_left", 1),
					(assign, ":form_left", 1),
					(position_move_x, pos1, ":neg_distance", 0),
				(else_try),
					(assign, ":form_left", 0),
					(position_move_x, pos1, ":distance", 0),
				(try_end),			
				(assign, ":column", 1),
				(val_add, ":rank", 1),
			(try_end),
		(try_end),
	(try_end),
	(try_begin),
		(eq, ":first_member", -1), #To preserve the possibility of a -1 result if the above all fails
		(store_add, ":slot", slot_team_d0_first_member, ":fclass"),
		(team_set_slot, ":fteam", ":slot", ":first_member"),
	(try_end),
	(assign, reg0, ":troop_count")
  ]),
  
	   
  # script_get_default_formation by motomataru #EDITED TO SLOTS FOR MANY DIVISIONS BY CABA'DRIN
  # Input: team id
  # Output: reg0 default formation
  ("get_default_formation", [
	(store_script_param, ":fteam", 1),
	
	(team_get_slot, ":ffaction", ":fteam", slot_team_faction),
	
	(try_begin),
	    (this_or_next|eq, ":ffaction", fac_player_supporters_faction),
		(eq, ":ffaction", fac_player_faction),
		(is_between, "$players_kingdom", kingdoms_begin, kingdoms_end),
		(neq, "$players_kingdom", fac_player_supporters_faction),
		(assign, ":ffaction", "$players_kingdom"),
	(try_end),

	#assign default formation
	(try_begin),
		(eq, ":ffaction", fac_kingdom_1),	#Swadians
		(assign, reg0, formation_shield),
	(else_try),
		(eq, ":ffaction", fac_kingdom_2),	#Vaegirs
		(assign, reg0, formation_ranks),
	(else_try),
		(eq, ":ffaction", fac_kingdom_3),	#Khergit
		(assign, reg0, formation_none),	#Khergit have underdeveloped infantry
	(else_try),
		(eq, ":ffaction", fac_kingdom_4),	#Nords
		(assign, reg0, formation_shield),
	(else_try),
		(eq, ":ffaction", fac_kingdom_5),	#Rhodoks
		(assign, reg0, formation_shield),
	(else_try),
		(eq, ":ffaction", fac_kingdom_6),	#Sarranid
		(assign, reg0, formation_ranks),
	(else_try),
	    (this_or_next|eq, ":ffaction", fac_player_supporters_faction),
		(eq, ":ffaction", fac_player_faction),	#independent player
		(assign, reg0, formation_ranks),
	(else_try),
		(assign, reg0, formation_none),	#riffraff don't use formations
	(try_end),
  ]),  
  

  # script_equip_best_melee_weapon by motomataru #CABA - OK
  # Input: agent id, flag to force shield, flag to force for length ALONE
  # Output: none
  ("equip_best_melee_weapon", [
	(store_script_param, ":agent", 1),
	(store_script_param, ":force_shield", 2),
	(store_script_param, ":force_length", 3),

	#priority items
	(assign, ":shield", itm_no_item),
	(assign, ":weapon", itm_no_item),
	(try_for_range, ":item_slot", ek_item_0, ek_head),
		(agent_get_item_slot, ":item", ":agent", ":item_slot"),
		(gt, ":item", itm_no_item),
		(item_get_type, ":weapon_type", ":item"),
		(try_begin),
			(eq, ":weapon_type", itp_type_shield),
			(assign, ":shield", ":item"),
		(else_try),
			(eq, ":weapon_type", itp_type_thrown),
			# (agent_get_ammo, ":ammo", ":agent", 0),	#assume infantry would have no other kind of ranged weapon
			# (gt, ":ammo", 0),
			(assign, ":weapon", ":item"),	#use thrown weapons first
		(try_end),
	(try_end),

	#select weapon
	(try_begin),
		(eq, ":weapon", itm_no_item),
		(assign, ":cur_score", 0),
		(try_for_range, ":item_slot", ek_item_0, ek_head),
			(agent_get_item_slot, ":item", ":agent", ":item_slot"),
			(gt, ":item", itm_no_item),
			(item_get_type, ":weapon_type", ":item"),
			(neq, ":weapon_type", itp_type_shield),

			(item_get_slot, reg0, ":item", slot_item_needs_two_hands),
			(this_or_next|eq, reg0, 0),
			(this_or_next|eq, ":force_shield", 0),
			(eq, ":shield", itm_no_item),
			
			(try_begin),
				(neq, ":force_length", 0),
				(item_get_slot, ":item_length", ":item", slot_item_length),
				(try_begin),
					(lt, ":cur_score", ":item_length"),
					(assign, ":cur_score", ":item_length"),
					(assign, ":weapon", ":item"),
				(try_end),
			(else_try),
				(assign, ":imod", imodbit_plain),
				(agent_get_troop_id, ":troop_id", ":agent"),
				(try_begin),    #only heroes have item modifications
					(troop_is_hero, ":troop_id"),
					(try_for_range, ":troop_item_slot",  ek_item_0, ek_head),    # heroes have only 4 possible weapons (equipped)
						(troop_get_inventory_slot, reg0, ":troop_id", ":troop_item_slot"),  #Find Item Slot with same item ID as Equipped Weapon
						(eq, reg0, ":item"),
						(troop_get_inventory_slot_modifier, ":imod", ":troop_id", ":troop_item_slot"),
					(try_end),
				(try_end), 

				(call_script, "script_get_item_score_with_imod", ":item", ":imod"),
				(lt, ":cur_score", reg0),
				(assign, ":cur_score", reg0),
				(assign, ":weapon", ":item"),
			(try_end),
		(try_end),
	(try_end),

	#equip selected items if needed
	(agent_get_wielded_item, reg0, ":agent", 0),
	(try_begin),
		(neq, reg0, ":weapon"),
		(try_begin),
			(gt, ":shield", itm_no_item),
			(agent_get_wielded_item, reg0, ":agent", 1),
			(neq, reg0, ":shield"),	#reequipping secondary will UNequip (from experience)
			(agent_set_wielded_item, ":agent", ":shield"),
		(try_end),
		(gt, ":weapon", itm_no_item),
		(agent_set_wielded_item, ":agent", ":weapon"),
	(try_end),
  ]),


  # script_formation_current_position by motomataru #CABA - OK
  # Input: destination position, team, troop class, formation type, extra spacing
  # Output: in destination position
  ("formation_current_position", [
	(store_script_param, ":fposition", 1),
	(store_script_param, ":fteam", 2),
	(store_script_param, ":fclass", 3),
	(store_script_param, ":fformation", 4),
	(store_script_param, ":formation_extra_spacing", 5),
	#(call_script, "script_get_first_formation_member", ":fteam", ":fclass", ":fformation"),
	#(assign, ":first_agent_in_formation", reg0),
	(store_add, ":slot", slot_team_d0_first_member, ":fclass"),
	(team_get_slot, ":first_agent_in_formation", ":fteam", ":slot"),
	(call_script, "script_get_formation_position", pos0, ":fteam", ":fclass"),
	(try_begin),
		(eq, ":first_agent_in_formation", -1),
		(copy_position, ":fposition", pos0),
	(else_try),
		(agent_get_position, ":fposition", ":first_agent_in_formation"),
		(position_copy_rotation, ":fposition", pos0),
		(store_add, ":slot", slot_team_d0_size, ":fclass"), #battlegroup_get_size phase out
		(team_get_slot, ":num_troops", ":fteam", ":slot"),
		(try_begin),
			#(eq, ":fclass", grc_archers),
			(store_add, ":slot", slot_team_d0_type, ":fclass"),
			(this_or_next|team_slot_eq, ":fteam", ":slot", sdt_archer),
			(team_slot_eq, ":fteam", ":slot", sdt_skirmisher),
			(call_script, "script_get_centering_amount", formation_default, ":num_troops", ":formation_extra_spacing"),
		(else_try),
			(call_script, "script_get_centering_amount", ":fformation", ":num_troops", ":formation_extra_spacing"),
			(val_mul, reg0, -1),
		(try_end),
		(position_move_x, ":fposition", reg0, 0),
	(try_end),
  ]),
  
  
  # script_get_centering_amount by motomataru #CABA - OK
  # Input: formation type, number of infantry, extra spacing
  #        Use formation type formation_default to use script for archer line
  # Output: reg0 number of centimeters to adjust x-position to center formation
  ("get_centering_amount", [
	(store_script_param, ":troop_formation", 1),
	(store_script_param, ":num_troops", 2),
	(store_script_param, ":extra_spacing", 3),
	(store_mul, ":troop_space", ":extra_spacing", 50),
	(val_add, ":troop_space", formation_minimum_spacing),
	(assign, reg0, 0),
	(try_begin),
		(eq, ":troop_formation", formation_square),
		(convert_to_fixed_point, ":num_troops"),
		(store_sqrt, reg0, ":num_troops"),
		(val_mul, reg0, ":troop_space"),
		(convert_from_fixed_point, reg0),
		(val_sub, reg0, ":troop_space"),
	(else_try),
		(this_or_next|eq, ":troop_formation", formation_ranks),
		(eq, ":troop_formation", formation_shield),
		(store_mul, reg0, ":num_troops", ":troop_space"),
		(val_div, reg0, 3),
		(val_sub, reg0, ":troop_space"),
	(else_try),
		(eq, ":troop_formation", formation_default),	#assume these are archers in a line
		(store_mul, reg0, ":num_troops", ":troop_space"),
	(try_end),
	(val_div, reg0, 2),
  ]),

  
  # script_formation_end #CABA - Modified for Classify_agent phase out 
  # Input: team, troop class
  # Output: none
  ("formation_end", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fclass", 2),
	(try_begin),
	    (neq, ":fclass", grc_everyone), 
		(team_get_leader, ":leader", ":fteam"),
	(else_try),
	    (assign, ":leader", -1),
	(try_end),
	(try_for_agents, ":agent"),
		(agent_is_alive, ":agent"),
		(agent_is_human, ":agent"),
		(agent_get_team, ":team", ":agent"),
		(eq, ":team", ":fteam"),
		#(call_script, "script_classify_agent", ":agent"),
		#(this_or_next|eq, reg0, ":fclass"), 
		(neq, ":leader", ":agent"),
		(agent_get_division, ":bgroup", ":agent"),
		(this_or_next|eq, ":bgroup", ":fclass"),
		(eq, ":fclass", grc_everyone), 
		(agent_clear_scripted_mode, ":agent"),
	(try_end),
  ]),


  # script_formation_move_position v2 by motomataru #CABA - EDITED FOR MANY SLOTS AND DIVISIONS
  # Input: team, troop class, formation current position, formation type, extra spacing, (1 to advance or -1 to withdraw or 0 to redirect)
  # Output: pos1 (offset for centering)
  ("formation_move_position", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fclass", 2),
	(store_script_param, ":fcurrentpos", 3),
	(store_script_param, ":fformation", 4),
	(store_script_param, ":formation_extra_spacing", 5),
	(store_script_param, ":direction", 6),
	(copy_position, pos1, ":fcurrentpos"),
	(call_script, "script_team_get_position_of_enemies", pos60, ":fteam", grc_everyone),
	(try_begin),
		(neq, reg0, 0),	#more than 0 enemies still alive?
		(copy_position, pos1, ":fcurrentpos"),	#restore current formation "position"
		(call_script, "script_point_y_toward_position", pos1, pos60),	#record angle from center to enemy
		(assign, ":distance_to_enemy", reg0),
#		(team_get_order_position, pos61, ":fteam", ":fclass"),
		(call_script, "script_get_formation_position", pos61, ":fteam", ":fclass"),
		(get_distance_between_positions, ":move_amount", pos1, pos61),	#distance already moving from previous orders
		(val_add, ":move_amount", 1000),
		(try_begin),
			(gt, ":direction", 0),	#moving forward?
			(gt, ":move_amount", ":distance_to_enemy"),
			(assign, ":move_amount", ":distance_to_enemy"),
		(try_end),
		(val_mul, ":move_amount", ":direction"),
		(position_move_y, pos1, ":move_amount", 0),
		(try_begin),
			(lt, ":distance_to_enemy", 1000),	#less than a move away?
			(position_copy_rotation, pos1, pos61),	#avoid rotating formation
		(try_end),
#		(team_set_order_position, ":fteam", ":fclass", pos1),
		(call_script, "script_set_formation_position", ":fteam", ":fclass", pos1),
		(store_add, ":slot", slot_team_d0_size, ":fclass"),
		(team_get_slot, ":num_troops", ":fteam", ":slot"),
		(try_begin),
			#(neq, ":fclass", grc_archers),
			(store_add, ":slot", slot_team_d0_type, ":fclass"),
			(neg|team_slot_eq, ":fteam", ":slot", sdt_archer),
			(neg|team_slot_eq, ":fteam", ":slot", sdt_skirmisher),
			(call_script, "script_get_centering_amount", ":fformation", ":num_troops", ":formation_extra_spacing"),
		(else_try),
			(call_script, "script_get_centering_amount", formation_default, ":num_troops", ":formation_extra_spacing"),
			(val_mul, reg0, -1),
		(try_end),
		(position_move_x, pos1, reg0, 0),
	(try_end),
  ]),


  # script_set_formation_position by motomataru  #EDITED TO SLOTS FOR MANY DIVISIONS BY CABA'DRIN
  # Input: team, troop class, position
  # Kluge around buggy *_order_position functions for teams 0-3
  ("set_formation_position", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fclass", 2),
	(store_script_param, ":fposition", 3),
	
	(position_get_x, ":x", ":fposition"),
	(position_get_y, ":y", ":fposition"),
	(position_get_rotation_around_z, ":zrot", ":fposition"),
	
	(store_add, ":slot", slot_team_d0_formation_x, ":fclass"),
	(team_set_slot, ":fteam", ":slot", ":x"),	
	(store_add, ":slot", slot_team_d0_formation_y, ":fclass"),
	(team_set_slot, ":fteam", ":slot", ":y"),	
	(store_add, ":slot", slot_team_d0_formation_zrot, ":fclass"),
	(team_set_slot, ":fteam", ":slot", ":zrot"),
	
	(team_set_order_position, ":fteam", ":fclass", ":fposition"),
  ]),	


  # script_get_formation_position by motomataru #EDITED TO SLOTS FOR MANY DIVISIONS BY CABA'DRIN
  # Input: position, team, troop class
  # Output: input position (pos0 used)
  # Kluge around buggy *_order_position functions for teams 0-3
  ("get_formation_position", [
	(store_script_param, ":fposition", 1),
	(store_script_param, ":fteam", 2),
	(store_script_param, ":fclass", 3),
	(init_position, ":fposition"),
	
	(try_begin),
	    (is_between, ":fteam", 0, 4),
		(store_add, ":slot", slot_team_d0_formation_x, ":fclass"),
		(team_get_slot, ":x", ":fteam", ":slot"),
		(store_add, ":slot", slot_team_d0_formation_y, ":fclass"),
		(team_get_slot, ":y", ":fteam", ":slot"),
		(store_add, ":slot", slot_team_d0_formation_zrot, ":fclass"),
		(team_get_slot, ":zrot", ":fteam", ":slot"),
		
		(position_set_x, ":fposition", ":x"),
		(position_set_y, ":fposition", ":y"),
		(position_rotate_z, ":fposition", ":zrot"),
	(else_try), #CABA - When would this ever be called?
		#(call_script, "script_get_first_formation_member", ":fteam", ":fclass", formation_square),
		(store_add, ":slot", slot_team_d0_first_member, ":fclass"),
		(team_get_slot, reg0, ":fteam", ":slot"),
		(try_begin),	  # "launder" team_get_order_position shutting down position_move_x
			(gt, reg0, -1),
			(team_get_order_position, ":fposition", ":fteam", ":fclass"),
			(agent_get_position, pos0, reg0),
			(agent_set_position, reg0, ":fposition"),
			(agent_get_position, ":fposition", reg0),
			(agent_set_position, reg0, pos0),
		(try_end),
	(try_end),
	(position_set_z_to_ground_level, ":fposition"),
  ]),	

  
  # script_cf_valid_formation_division by Caba'drin
  # Input: team, troop class, formation
  # Output: reg0: troop count/1 if too few troops/0 if wrong type, reg1: sdt_*
  # Failure indicates class cannot form this formation
  # Called from within cf_formation
  ("cf_valid_formation_division", [
    (store_script_param, ":fteam", 1),
	(store_script_param, ":fclass", 2),
	(store_script_param, ":fformation", 3),
	
	(assign, ":valid_type", 0),
	(store_add, ":slot", slot_team_d0_type, ":fclass"),
	(team_get_slot, ":sd_type", ":fteam", ":slot"),
	(try_begin), #Eventually make this more complex with the sub-divisions
		(this_or_next|team_slot_eq, ":fteam", ":slot", sdt_infantry),
		(team_slot_eq, ":fteam", ":slot", sdt_polearm),
		(assign, ":size_minimum", formation_min_foot_troops),
		(assign, ":valid_type", 1), #all types valid for infantry	
	(else_try),
		(this_or_next|team_slot_eq, ":fteam", ":slot", sdt_archer),
		(team_slot_eq, ":fteam", ":slot", sdt_skirmisher),
		(assign, ":size_minimum", formation_min_foot_troops),
	    (this_or_next|eq, ":fformation", formation_ranks),
		(eq, ":fformation", formation_default),
		(assign, ":valid_type", 1),	
	(else_try),
		(this_or_next|team_slot_eq, ":fteam", ":slot", sdt_cavalry),
		(team_slot_eq, ":fteam", ":slot", sdt_harcher),
		(assign, ":size_minimum", formation_min_cavalry_troops),
		(eq, ":fformation", formation_wedge),
		(assign, ":valid_type", 1),		
	(try_end),
	
	(try_begin),
	    (eq, ":valid_type", 0),
		(assign, ":num_troops", 0),
	(else_try),
		(store_add, ":slot", slot_team_d0_size, ":fclass"), #battlegroup_get_size phase out
	    (team_get_slot, ":num_troops", ":fteam", ":slot"),
	    (le, ":num_troops", ":size_minimum"),
		(assign, ":num_troops", 1),
	(try_end),
	
	(assign, reg0, ":num_troops"),
	(assign, reg1, ":sd_type"),
	(gt, ":num_troops", 1),    
  ]),
  
	
  # script_cf_valid_formation_member by motomataru #CABA - Modified for Classify_agent phase out
  # Input: team, troop class, agent number of team leader, test agent
  # Output: failure indicates agent is not member of formation
  ("cf_valid_formation_member", [
	(store_script_param, ":fteam", 1),
	(store_script_param, ":fclass", 2),
	(store_script_param, ":fleader", 3),
	(store_script_param, ":agent", 4),
	(neq, ":fleader", ":agent"),
	(agent_get_division, ":bgroup", ":agent"),
	(eq, ":bgroup", ":fclass"),
	#(call_script, "script_classify_agent", ":agent"),
	#(eq, reg0, ":fclass"),
	(agent_get_team, ":team", ":agent"),
	(eq, ":team", ":fteam"),
	(agent_is_alive, ":agent"),
	(agent_is_human, ":agent"),
	(agent_slot_eq, ":agent", slot_agent_is_running_away, 0),
  ]),

	
# #Player team formations functions

  # script_player_attempt_formation    #EDITED TO SLOTS FOR MANY DIVISIONS BY CABA'DRIN
  # Inputs:	arg1: troop class (grc_*)
  #			arg2: formation identifier (formation_*)
  # Output: none
  ("player_attempt_formation", [
	(store_script_param, ":fclass", 1),
	(store_script_param, ":fformation", 2),
	(set_fixed_point_multiplier, 100),

	(try_begin),
		(eq, ":fformation", formation_ranks),
		(str_store_string, s1, "@ranks"),
	(else_try),
		(eq, ":fformation", formation_shield),
		(str_store_string, s1, "@shield wall"),
	(else_try),
		(eq, ":fformation", formation_wedge),
		(str_store_string, s1, "@wedge"),
	(else_try),
		(eq, ":fformation", formation_square),
		(str_store_string, s1, "@square"),
	(else_try),
		(str_store_string, s1, "@up"),
	(try_end),
	(str_store_class_name, s2, ":fclass"),
	(assign, ":new_formation", 0),
	
	(try_begin),
		(store_add, ":slot", slot_team_d0_formation, ":fclass"),
		(neg|team_slot_eq, "$fplayer_team_no", ":slot", ":fformation"),
		(team_set_slot, "$fplayer_team_no", ":slot", ":fformation"),
		(assign, ":new_formation", 1),
		(store_add, ":slot", slot_team_d0_formation_space, ":fclass"),
		(neg|team_slot_ge, "$fplayer_team_no", ":slot", formation_start_spread_out),
		(team_set_slot, "$fplayer_team_no", ":slot", formation_start_spread_out),	#spread out for ease of forming up			
	(try_end),
	(try_begin),
		(store_add, ":slot", slot_team_d0_formation_space, ":fclass"),
		(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
		(call_script, "script_cf_formation", "$fplayer_team_no", ":fclass", ":div_spacing", ":fformation"),
		(try_begin),
			(eq, ":new_formation", 1),
			(display_message, "@{!}{s2} forming {s1}."),
		(try_end),	
	(else_try),
		(store_add, ":slot", slot_team_d0_formation, ":fclass"),
		(team_set_slot, "$fplayer_team_no", ":slot", formation_none),
		(try_begin),
			(gt, reg0, 0),
			(display_message, "@Not enough troops in {s2} to form {s1}, but holding."),
		(else_try),
			(display_message, "@{!}{s2} cannot form {s1}, so is holding."),
		(try_end),
		(call_script, "script_formation_end", "$fplayer_team_no", ":fclass"),
	(try_end),

	(store_add, ":slot", slot_team_d0_move_order, ":fclass"),
	(team_set_slot, "$fplayer_team_no", ":slot", mordr_hold),
	(set_show_messages, 0),
	(team_give_order, "$fplayer_team_no", ":fclass", mordr_hold),
	(team_set_order_position, "$fplayer_team_no", ":fclass", pos61),
	(set_show_messages, 1),
  ]),
  
  
  # script_player_order_formations by motomataru #EDITED TO SLOTS FOR MANY DIVISIONS BY CABA'DRIN
  # Inputs:	arg1: order to formation (mordr_*)
  # Output: none
  ("player_order_formations", [
	(store_script_param, ":forder", 1),
	(set_fixed_point_multiplier, 100),
	
	(try_begin), #On hold, any formations reform in new location		
		(eq, ":forder", mordr_hold),
		(try_for_range, ":division", 0, 9),
		    (class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(neg|team_slot_eq, "$fplayer_team_no", ":slot", formation_none),
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(call_script, "script_player_attempt_formation", ":division", ":formation"),
		(try_end),		
	(else_try),	#Follow is hold	repeated frequently
		(eq, ":forder", mordr_follow),
		(try_for_range, ":division", 0, 9),
		    (class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(neg|team_slot_eq, "$fplayer_team_no", ":slot", formation_none),
			(store_add, ":slot", slot_team_d0_move_order, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", mordr_follow),
		(try_end),		
	(else_try),	#charge or retreat ends formation
		(this_or_next|eq, ":forder", mordr_charge),
		(eq, ":forder", mordr_retreat),
		(try_for_range, ":division", 0, 9),
		    (class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(neg|team_slot_eq, "$fplayer_team_no", ":slot", formation_none),
			(call_script, "script_formation_end", "$fplayer_team_no", ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", formation_none),
			(store_add, ":slot", slot_team_d0_type, ":division"),
			(try_begin),
			    (this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_infantry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_polearm),
				(display_message, "@Infantry formation disassembled."),
			(else_try),
				(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_skirmisher),
				(display_message, "@Archer formation disassembled."),
			(else_try),
				(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
				(display_message, "@Cavalry formation disassembled."),
			(else_try),
				(display_message, "@Formation disassembled."),			
			(try_end),
		(try_end),
				
	(else_try),	#dismount ends formation
		(eq, ":forder", mordr_dismount),
		(try_for_range, ":division", 0, 9),
		    (class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_type, ":division"),
			(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
			(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(neg|team_slot_eq, "$fplayer_team_no", ":slot", formation_none),
			(call_script, "script_formation_end", "$fplayer_team_no", ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", formation_none),
			(display_message, "@Cavalry formation disassembled."),
        (try_end),
			
	(else_try), 
		(eq, ":forder", mordr_advance),
		(try_for_range, ":division", 0, 9),
		    (class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(neg|team_slot_eq, "$fplayer_team_no", ":slot", formation_none),
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(store_add, ":slot", slot_team_d0_formation_space, ":division"),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			(call_script, "script_formation_current_position", pos63, "$fplayer_team_no", ":division", ":formation", ":div_spacing"),
			(try_begin),
			    (store_add, ":slot", slot_team_d0_move_order, ":division"),
				(neg|team_slot_eq, "$fplayer_team_no", ":slot", mordr_advance),
				(call_script, "script_set_formation_position", "$fplayer_team_no", ":division", pos63),
			(try_end),
			(call_script, "script_formation_move_position", "$fplayer_team_no", ":division", pos63, ":formation", ":div_spacing", 1),			
			(try_begin),
			    (this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_infantry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_polearm),
				(call_script, "script_form_infantry", "$fplayer_team_no", "$fplayer_agent_no", ":division", ":div_spacing", ":formation"),
			(else_try),
			    (this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
				(call_script, "script_form_cavalry", "$fplayer_team_no", "$fplayer_agent_no", ":division", ":div_spacing"),
			(else_try),
				(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_skirmisher),	    
				(call_script, "script_form_archers", "$fplayer_team_no", "$fplayer_agent_no", ":division", ":div_spacing", ":formation"),
			(try_end),
			(store_add, ":slot", slot_team_d0_move_order, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", mordr_advance),	
        (try_end),			

	(else_try),
		(eq, ":forder", mordr_fall_back),
		(try_for_range, ":division", 0, 9),
		    (class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(neg|team_slot_eq, "$fplayer_team_no", ":slot", formation_none),
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(store_add, ":slot", slot_team_d0_formation_space, ":division"),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			(call_script, "script_formation_current_position", pos63, "$fplayer_team_no", ":division", ":formation", ":div_spacing"),
			(try_begin),
			    (store_add, ":slot", slot_team_d0_move_order, ":division"),
				(neg|team_slot_eq, "$fplayer_team_no", ":slot", mordr_fall_back),
				(call_script, "script_set_formation_position", "$fplayer_team_no", ":division", pos63),
			(try_end),
			(call_script, "script_formation_move_position", "$fplayer_team_no", ":division", pos63, ":formation", ":div_spacing", -1),			
			(try_begin),
			    (this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_infantry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_polearm),
				(call_script, "script_form_infantry", "$fplayer_team_no", "$fplayer_agent_no", ":division", ":div_spacing", ":formation"),
			(else_try),
			    (this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
				(call_script, "script_form_cavalry", "$fplayer_team_no", "$fplayer_agent_no", ":division", ":div_spacing"),
			(else_try),
				(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_skirmisher),	    
				(call_script, "script_form_archers", "$fplayer_team_no", "$fplayer_agent_no", ":division", ":div_spacing", ":formation"),
			(try_end),
			(store_add, ":slot", slot_team_d0_move_order, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", mordr_fall_back),	
        (try_end),		

	(else_try),
		(eq, ":forder", mordr_stand_closer),		
		(try_for_range, ":division", 0, 9),
		    (class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_formation_space, ":division"),
			(team_slot_ge, "$fplayer_team_no", ":slot", 1),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			(val_sub, ":div_spacing", 1),
			(team_set_slot, "$fplayer_team_no", ":slot", ":div_spacing"),
			(call_script, "script_get_formation_position", pos1, "$fplayer_team_no", ":division"),			
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(try_begin),
			    (this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_infantry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_polearm),
				(store_add, ":slot", slot_team_d0_size, ":division"),
	            (team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
				(call_script, "script_get_centering_amount", ":formation", ":troop_count", ":div_spacing"),
			    (position_move_x, pos1, reg0),
				(call_script, "script_form_infantry", "$fplayer_team_no", "$fplayer_agent_no", ":division", ":div_spacing", ":formation"),
			(else_try),
			    (this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
				(call_script, "script_form_cavalry", "$fplayer_team_no", "$fplayer_agent_no", ":division", ":div_spacing"),
			(else_try),
				(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_skirmisher),
			    (store_add, ":slot", slot_team_d0_size, ":division"),
	            (team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
			    (call_script, "script_get_centering_amount", formation_default, ":troop_count", ":div_spacing"),
			    (val_mul, reg0, -1),
			    (position_move_x, pos1, reg0),				
				(call_script, "script_form_archers", "$fplayer_team_no", "$fplayer_agent_no", ":division", ":div_spacing", ":formation"),
			(try_end),
		(try_end),

	(else_try),
		(eq, ":forder", mordr_spread_out),
		(try_for_range, ":division", 0, 9),
		    (class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_formation_space, ":division"),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			(val_add, ":div_spacing", 1),
			(team_set_slot, "$fplayer_team_no", ":slot", ":div_spacing"),
			(call_script, "script_get_formation_position", pos1, "$fplayer_team_no", ":division"),			
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(try_begin),
			    (this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_infantry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_polearm),
				(store_add, ":slot", slot_team_d0_size, ":division"), 
	            (team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
				(call_script, "script_get_centering_amount", ":formation", ":troop_count", ":div_spacing"),
			    (position_move_x, pos1, reg0),
				(call_script, "script_form_infantry", "$fplayer_team_no", "$fplayer_agent_no", ":division", ":div_spacing", ":formation"), 
			(else_try),
			    (this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
				(call_script, "script_form_cavalry", "$fplayer_team_no", "$fplayer_agent_no", ":division", ":div_spacing"),
			(else_try),
				(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_skirmisher),
			    (store_add, ":slot", slot_team_d0_size, ":division"),
	            (team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
			    (call_script, "script_get_centering_amount", formation_default, ":troop_count", ":div_spacing"),
			    (val_mul, reg0, -1),
			    (position_move_x, pos1, reg0),				
				(call_script, "script_form_archers", "$fplayer_team_no", "$fplayer_agent_no", ":division", ":div_spacing", ":formation"),
			(try_end),
		(try_end),

	(else_try),
		(eq, ":forder", mordr_stand_ground),
		(try_for_range, ":division", 0, 9),
		    (class_is_listening_order, "$fplayer_team_no", ":division"),
			(store_add, ":slot", slot_team_d0_formation, ":division"),
			(neg|team_slot_eq, "$fplayer_team_no", ":slot", formation_none),
			(team_get_slot, ":formation", "$fplayer_team_no", ":slot"),
			(store_add, ":slot", slot_team_d0_formation_space, ":division"),
			(team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			(call_script, "script_formation_current_position", pos63, "$fplayer_team_no", ":division", ":formation", ":div_spacing"),
			(copy_position, pos1, pos63),		
			(try_begin),
			    (this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_infantry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_polearm),
				(store_add, ":slot", slot_team_d0_size, ":division"),
	            (team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),	
				(call_script, "script_get_centering_amount", ":formation", ":troop_count", ":div_spacing"),
			    (position_move_x, pos1, reg0),
				(call_script, "script_form_infantry", "$fplayer_team_no", "$fplayer_agent_no", ":division", ":div_spacing", ":formation"),
			(else_try),
			    (this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
				(call_script, "script_form_cavalry", "$fplayer_team_no", "$fplayer_agent_no", ":division", ":div_spacing"),
			(else_try),
				(this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
				(team_slot_eq, "$fplayer_team_no", ":slot", sdt_skirmisher),
			    (store_add, ":slot", slot_team_d0_size, ":division"),
	            (team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
			    (call_script, "script_get_centering_amount", formation_default, ":troop_count", ":div_spacing"),
			    (val_mul, reg0, -1),
			    (position_move_x, pos1, reg0),				
				(call_script, "script_form_archers", "$fplayer_team_no", "$fplayer_agent_no", ":division", ":div_spacing", ":formation"),
			(try_end),
			(store_add, ":slot", slot_team_d0_move_order, ":division"),
			(team_set_slot, "$fplayer_team_no", ":slot", mordr_stand_ground),
			(call_script, "script_set_formation_position", "$fplayer_team_no", ":division", pos63),
		(try_end),			
	(try_end)
  ]),

  
# #Utilities used by formations   #CABA - OK
  # script_point_y_toward_position by motomataru
  # Input: from position, to position
  # Output: reg0 fixed point distance
  ("point_y_toward_position", [
	(store_script_param, ":from_position", 1),
	(store_script_param, ":to_position", 2),
	(position_get_x, ":dist_x_to_cosine", ":to_position"),
	(position_get_x, ":from_coord", ":from_position"),
	(val_sub, ":dist_x_to_cosine", ":from_coord"),
	(store_mul, ":sum_square", ":dist_x_to_cosine", ":dist_x_to_cosine"),
	(position_get_y, ":dist_y_to_sine", ":to_position"),
	(position_get_y, ":from_coord", ":from_position"),
	(val_sub, ":dist_y_to_sine", ":from_coord"),
	(store_mul, reg0, ":dist_y_to_sine", ":dist_y_to_sine"),
	(val_add, ":sum_square", reg0),
	(convert_from_fixed_point, ":sum_square"),
	(store_sqrt, ":distance_between", ":sum_square"),
	(convert_to_fixed_point, ":dist_x_to_cosine"),
	(val_div, ":dist_x_to_cosine", ":distance_between"),
	(convert_to_fixed_point, ":dist_y_to_sine"),
	(val_div, ":dist_y_to_sine", ":distance_between"),
	(try_begin),
		(lt, ":dist_x_to_cosine", 0),
		(assign, ":bound_a", 90),
		(assign, ":bound_b", 270),
		(assign, ":theta", 180),
	(else_try),
		(assign, ":bound_a", 90),
		(assign, ":bound_b", -90),
		(assign, ":theta", 0),
	(try_end),
	(assign, ":sine_theta", 0),	#avoid error on compile
	(convert_to_fixed_point, ":theta"),
	(convert_to_fixed_point, ":bound_a"),
	(convert_to_fixed_point, ":bound_b"),
	(try_for_range, reg0, 0, 6),	#precision 90/2exp6 (around 2 degrees)
		(store_sin, ":sine_theta", ":theta"),
		(try_begin),
			(gt, ":sine_theta", ":dist_y_to_sine"),
			(assign, ":bound_a", ":theta"),
		(else_try),
			(lt, ":sine_theta", ":dist_y_to_sine"),
			(assign, ":bound_b", ":theta"),
		(try_end),
		(store_add, ":angle_sum", ":bound_b", ":bound_a"),
		(store_div, ":theta", ":angle_sum", 2),
	(try_end),
	(convert_from_fixed_point, ":theta"),
	(position_get_rotation_around_z, reg0, ":from_position"),
	(val_sub, ":theta", reg0),
	(val_sub, ":theta", 90),	#point y-axis at destination
	(position_rotate_z, ":from_position", ":theta"),
	(assign, reg0, ":distance_between"),
  ]),
  

  # script_store_division_type by Caba'drin   ##NEEDS EDIT per PMs with moto
  # Input: team, division
  # Output: reg0 and slot_team_dx_type with sdt_* value
  # Automatically called from store_battlegroup_data; Only during BP_Setup/first 5 seconds to reduce agent loops
  ("store_division_type", [
    (store_script_param_1, ":fteam"),
	(store_script_param_2, ":fclass"),
    
    (assign, ":count_infantry", 0),
    (assign, ":count_archer", 0),
    (assign, ":count_cavalry", 0),
    (assign, ":count_harcher", 0),
    (assign, ":count_polearms", 0),
    (assign, ":count_skirmish", 0),
    (assign, ":count_support", 0),
    (assign, ":count_bodyguard", 0),	

	(try_for_agents, ":cur_agent"),
		(agent_is_alive, ":cur_agent"),      
		(agent_is_human, ":cur_agent"), 
		(agent_slot_eq, ":cur_agent", slot_agent_is_running_away, 0),
		(agent_get_team, ":bgteam", ":cur_agent"),
		(eq, ":bgteam", ":fteam"),
		#(call_script, "script_classify_agent", ":cur_agent"),
		#(assign, ":bgroup", reg0),
		(team_get_leader, ":leader", ":fteam"),
		(neq, ":leader", ":cur_agent"),
		(agent_get_division, ":bgroup", ":cur_agent"),
		(eq, ":bgroup", ":fclass"),
		(agent_get_troop_id, ":cur_troop", ":cur_agent"),
		(agent_get_ammo, ":cur_ammo", ":cur_agent"),
		(agent_get_wielded_item, reg0, ":cur_agent", 0),
		
		(try_begin),
			(lt, reg0, 0),
			(assign, ":cur_weapon_type", 0),
		(else_try),
			(item_get_type, ":cur_weapon_type", reg0), 
		(try_end),
		
		(try_begin),
		    (neg|troop_is_hero, ":cur_troop"),
			(try_begin), #Cavalry	
				(agent_get_horse, reg0, ":cur_agent"),
				(ge, reg0, 0),
				(try_begin),				
					(gt, ":cur_ammo", 0),
					(val_add, ":count_harcher", 1),
				(else_try),
				    (val_add, ":count_cavalry", 1),
				(try_end),
			(else_try), #Archers
				(gt, ":cur_ammo", 0),
				(try_begin),
					(eq, ":cur_weapon_type", itp_type_thrown),
					(val_add, ":count_skirmish", 1),
				(else_try),
				    (val_add, ":count_archer", 1),
				(try_end),
			(else_try), #Infantry
			    (try_begin),
				    (eq, ":cur_weapon_type", itp_type_polearm),
					(val_add, ":count_polearms", 1),
				(else_try),
				    (val_add, ":count_infantry", 1),
				(try_end),			    
			(try_end),
		(else_try), #Heroes
		    (assign, ":support_skills", 0), #OPEN TO SUGGESTIONS HERE    ?skl_trade, skl_spotting, skl_pathfinding, skl_tracking?
		    (store_skill_level, reg0, skl_engineer, ":cur_troop"),
			(val_add, ":support_skills", reg0),
			(store_skill_level, reg0, skl_first_aid, ":cur_troop"),
			(val_add, ":support_skills", reg0),
			(store_skill_level, reg0, skl_surgery, ":cur_troop"),
			(val_add, ":support_skills", reg0),
			(store_skill_level, reg0, skl_wound_treatment, ":cur_troop"),
			(val_add, ":support_skills", reg0),
			(try_begin),
			    (gt, ":support_skills", 5),
				(val_add, ":count_support", 1),
			(else_try),
			    (val_add, ":count_bodyguard", 1),
			(try_end),		
		(try_end), #Regular v Hero		
	(try_end), #Agent Loop	
		
	#Do Comparisons With Counts, set ":div_type"
	(assign, ":slot", slot_team_d0_type),
	(team_set_slot, scratch_team, ":slot", ":count_infantry"),
	(val_add, ":slot", 1),
	(team_set_slot, scratch_team, ":slot", ":count_archer"),
	(val_add, ":slot", 1),
	(team_set_slot, scratch_team, ":slot", ":count_cavalry"),
	(val_add, ":slot", 1),
	(team_set_slot, scratch_team, ":slot", ":count_polearms"),
	(val_add, ":slot", 1),
	(team_set_slot, scratch_team, ":slot", ":count_skirmish"),
	(val_add, ":slot", 1),
	(team_set_slot, scratch_team, ":slot", ":count_harcher"),
	(val_add, ":slot", 1),
	(team_set_slot, scratch_team, ":slot", ":count_support"),
	(val_add, ":slot", 1),
	(team_set_slot, scratch_team, ":slot", ":count_bodyguard"),

	(assign, ":count_to_beat", 0),
	(assign, ":count_total", 0),
	(assign, ":div_type", -1),
	(try_for_range, ":slot", slot_team_d0_type, slot_team_d0_type + 8), #only scratch_team sdt_types at the moment
	    (team_get_slot, ":count", scratch_team, ":slot"),
		(team_set_slot, scratch_team, ":slot", 0), #Reset
		(val_add, ":count_total", ":count"),
		(gt, ":count", ":count_to_beat"),
		(assign, ":count_to_beat", ":count"),
		(val_sub, ":slot", slot_team_d0_type),
		(assign, ":div_type", ":slot"),
	(try_end),
	
	(val_div, ":count_total", 2), #More than Half of this division
	(try_begin),
	    (lt, ":count_to_beat", ":count_total"),
		(try_begin),
		    (is_between, ":div_type", 3, 6),
		    (val_sub, ":div_type", 3),
		(else_try),
		    (ge, ":div_type", 6),
		    (assign, ":div_type", -1), #Or 0
		(try_end),
	(try_end),
	
	(store_add, ":slot", slot_team_d0_type, ":fclass"),
	(team_set_slot, ":fteam", ":slot", ":div_type"),
	(assign, reg0, ":div_type"),  
  ]),
  
  
  # script_store_battlegroup_data by motomataru #EDITED TO SLOTS FOR MANY DIVISIONS BY CABA'DRIN
  # Input: none
  # Output: sets positions and globals to track data on ALL groups in a battle
  # Globals used: pos1, reg0, reg1, #CABA - NO LONGER USED: positions 24-45
  ("store_battlegroup_data", [
	(assign, ":team0_leader", 0),
	(assign, ":team0_x_leader", 0),
	(assign, ":team0_y_leader", 0),
	(assign, ":team0_level_leader", 0),
	(assign, ":team1_leader", 0),
	(assign, ":team1_x_leader", 0),
	(assign, ":team1_y_leader", 0),
	(assign, ":team1_level_leader", 0),
	(assign, ":team2_leader", 0),
	(assign, ":team2_x_leader", 0),
	(assign, ":team2_y_leader", 0),
	(assign, ":team2_level_leader", 0),
	(assign, ":team3_leader", 0),
	(assign, ":team3_x_leader", 0),
	(assign, ":team3_y_leader", 0),
	(assign, ":team3_level_leader", 0),
	
	#Team Slots reset every mission, like agent slots, but just to be sure for when it gets called during the mission
	(try_for_range, ":team", 0, 4),
	    (try_for_range, ":slot", reset_team_stats_begin, reset_team_stats_end), #Those within the "RESET GROUP" in formations_constants
		    (team_set_slot, ":team", ":slot", 0),
		(try_end),
	(try_end),

	(try_for_agents, ":cur_agent"),
		(agent_is_alive, ":cur_agent"),      
		(agent_is_human, ":cur_agent"), 
		(agent_slot_eq, ":cur_agent", slot_agent_is_running_away, 0),
		(agent_get_team, ":bgteam", ":cur_agent"),
		#(call_script, "script_classify_agent", ":cur_agent"),
		#(assign, ":bgroup", reg0),
		(agent_get_division, ":bgroup", ":cur_agent"),
		(try_begin),
			(team_get_leader, ":leader", ":bgteam"),
		    (eq, ":leader", ":cur_agent"),
			(assign, ":bgroup", -1),
		(try_end),
		(agent_get_troop_id, ":cur_troop", ":cur_agent"),
		(store_character_level, ":cur_level", ":cur_troop"),
		(agent_get_ammo, ":cur_ammo", ":cur_agent", 0),
		(assign, ":cur_weapon_type", 0),
		(assign, ":cur_weapon_length", 0),
		(agent_get_wielded_item, reg0, ":cur_agent", 0),
		(try_begin),
			(gt, reg0, itm_no_item),
			(item_get_type, ":cur_weapon_type", reg0),
			(this_or_next|eq, ":cur_weapon_type", itp_type_one_handed_wpn),
			(this_or_next|eq, ":cur_weapon_type", itp_type_two_handed_wpn),
			(this_or_next|eq, ":cur_weapon_type", itp_type_polearm),
			(eq, ":cur_weapon_type", itp_type_thrown),
			(item_get_slot, ":cur_weapon_length", reg0, slot_item_length),
		(try_end),

		(agent_get_position, pos1, ":cur_agent"),
		(position_get_x, ":x_value", pos1),
		(position_get_y, ":y_value", pos1),		
		
		(try_begin),
		    (eq, ":bgroup", -1), #Leaders
			(try_begin),
				(eq, ":bgteam", 0),
				(assign, ":team0_leader", 1),
				(assign, ":team0_x_leader", ":x_value"),
				(assign, ":team0_y_leader", ":y_value"),
				(assign, ":team0_level_leader", ":cur_level"),
			(else_try),
				(eq, ":bgteam", 1),
				(assign, ":team1_leader", 1),
				(assign, ":team1_x_leader", ":x_value"),
				(assign, ":team1_y_leader", ":y_value"),
				(assign, ":team1_level_leader", ":cur_level"),
			(else_try),
				(eq, ":bgteam", 2),
				(assign, ":team2_leader", 1),
				(assign, ":team2_x_leader", ":x_value"),
				(assign, ":team2_y_leader", ":y_value"),
				(assign, ":team2_level_leader", ":cur_level"),
			(else_try),
				(eq, ":bgteam", 3),
				(assign, ":team3_leader", 1),
				(assign, ":team3_x_leader", ":x_value"),
				(assign, ":team3_y_leader", ":y_value"),
				(assign, ":team3_level_leader", ":cur_level"),
			(try_end),
		(else_try),
			(store_add, ":slot", slot_team_d0_size, ":bgroup"), #Division Count
			(team_get_slot, ":value", ":bgteam", ":slot"),
			(val_add, ":value", 1),
			(team_set_slot, ":bgteam", ":slot", ":value"),
			
			(store_add, ":slot", slot_team_d0_level, ":bgroup"), #Division Level
			(team_get_slot, ":value", ":bgteam", ":slot"),
			(val_add, ":value", ":cur_level"),
			(team_set_slot, ":bgteam", ":slot", ":value"),
			
			(store_add, ":slot", slot_team_d0_weapon_length, ":bgroup"), #Division Weapon Length
			(team_get_slot, ":value", ":bgteam", ":slot"),
			(val_add, ":value", ":cur_weapon_length"),
			(team_set_slot, ":bgteam", ":slot", ":value"),
			
			(store_add, ":slot", slot_team_d0_x, ":bgroup"), #Position X
			(team_get_slot, ":value", ":bgteam", ":slot"),
			(val_add, ":value", ":x_value"),
			(team_set_slot, ":bgteam", ":slot", ":value"),
			
			(store_add, ":slot", slot_team_d0_y, ":bgroup"), #Position Y
			(team_get_slot, ":value", ":bgteam", ":slot"),
			(val_add, ":value", ":y_value"),
			(team_set_slot, ":bgteam", ":slot", ":value"),
			
			#Horse-Archer & Throwing Count
			(try_begin),
			    #(troop_is_guarantee_horse, ":cur_troop"),
				(agent_get_horse, reg0, ":cur_agent"),
				(gt, reg0, 0),
				(gt, ":cur_ammo", 0),
				(team_get_slot, ":value", ":bgteam", slot_team_percent_cavalry_are_archers),
				(val_add, ":value", 1),
				(team_set_slot, ":bgteam", slot_team_percent_cavalry_are_archers, ":value"),
			(else_try),
			    (try_begin), #CABA - check for how this is done in moto's code
			        (le, ":cur_ammo", 0),
			        (troop_is_guarantee_ranged, ":cur_troop"),
			        (team_set_slot, ":bgteam", slot_team_archers_have_ammo, 0), #Then this is based on the last agent's ammo state...
			    (try_end),
				(gt, ":cur_ammo", 0),
				(team_set_slot, ":bgteam", slot_team_archers_have_ammo, 1),
				(eq, ":cur_weapon_type", itp_type_thrown),
				(team_get_slot, ":value", ":bgteam", slot_team_percent_ranged_throw),
				(val_add, ":value", 1),
				(team_set_slot, ":bgteam", slot_team_percent_ranged_throw, ":value"),
			(try_end),				
		(try_end), #Leader vs Regular
	(try_end), #Agent Loop

	#calculate team sizes, sum positions; within calculate battle group averages
	(try_for_range, ":team", 0, 4),
	    (assign, ":team_size", 0),
		(assign, ":team_level", 0),
		(assign, ":team_x", 0),
		(assign, ":team_y", 0),
		
		(assign, ":num_infantry", 0),
		(assign, ":num_archers", 0),
		(assign, ":num_cavalry", 0),
		
	    (try_for_range, ":division", 0, 9),
		    #sum for team averages
		    (store_add, ":slot", slot_team_d0_size, ":division"),
		    (team_get_slot, ":division_size", ":team", ":slot"),
			(val_add, ":team_size", ":division_size"),
			
			(store_add, ":slot", slot_team_d0_level, ":division"),
		    (team_get_slot, ":division_level", ":team", ":slot"),
			(val_add, ":team_level", ":division_level"),
			
			(store_add, ":slot", slot_team_d0_x, ":division"),
		    (team_get_slot, ":division_x", ":team", ":slot"),
			(val_add, ":team_x", ":division_x"),
			
			(store_add, ":slot", slot_team_d0_y, ":division"),
		    (team_get_slot, ":division_y", ":team", ":slot"),
			(val_add, ":team_y", ":division_y"),	

            #calculate battle group averages
			(gt, ":division_size", 0),
			(store_add, ":slot", slot_team_d0_level, ":division"),
			(val_div, ":division_level", ":division_size"),			
			(team_set_slot, ":team", ":slot", ":division_level"),
			
			(store_add, ":slot", slot_team_d0_weapon_length, ":division"),
		    (team_get_slot, ":value", ":team", ":slot"),
			(val_div, ":value", ":division_size"),
			(team_set_slot, ":team", ":slot", ":value"),
			
			(store_add, ":slot", slot_team_d0_x, ":division"),
			(val_div, ":division_x", ":division_size"),
		    (team_set_slot, ":team", ":slot", ":division_x"),
			
			(store_add, ":slot", slot_team_d0_y, ":division"),
			(val_div, ":division_y", ":division_size"),
		    (team_set_slot, ":team", ":slot", ":division_y"),
			
			#(try_begin),
			#    (lt, ":division", 3), #CABA - This works right now, as only the player has other divisions enabled...NEED TO RECONSIDER LATER
			#    (store_mul, ":team_shift", ":team", 4),
		    #    (store_add, ":position_number", Team0_Infantry_Pos, ":team_shift"),
			#    (val_add, ":position_number", ":division"),
			#(else_try),
			#    (store_sub, ":team_shift", ":division", 3),
			#	(store_add, ":position_number", Player_Battle_Group3_Pos, ":team_shift"),
			#(try_end),			    
		    #(init_position, ":position_number"), #CABA - REMOVED AUTOMATIC initialization of positions...problem?
			
			#(val_div, ":division_x", ":division_size"),
			#(position_set_x, ":position_number", ":division_x"),
			#(val_div, ":division_y", ":division_size"),
			#(position_set_y, ":position_number", ":division_y"),
			#(position_set_z_to_ground_level, ":position_number"),

			(try_begin),
			    #(eq, "$battle_phase", BP_Setup),
				(store_mission_timer_a, ":time"),
				(le, ":time", 5), #Call within the first 5 seconds, then assume they are set
                (call_script, "script_store_division_type", ":team", ":division"),
			(else_try), #After first 5 seconds, use set types to save on agent_loops
			    (store_add, ":slot", slot_team_d0_type, ":division"),
			    (team_get_slot, reg0, ":team", ":slot"),
			(try_end),
            (try_begin),
                (this_or_next|eq, reg0, sdt_infantry),
				(eq, reg0, sdt_polearm),
				(val_add, ":num_infantry", ":division_size"),
			(else_try),
			    (this_or_next|eq, reg0, sdt_archer),
				(eq, reg0, sdt_skirmisher),
				(val_add, ":num_archers", ":division_size"),
			(else_try),
			    (this_or_next|eq, reg0, sdt_cavalry),
				(eq, reg0, sdt_harcher),
				(val_add, ":num_cavalry", ":division_size"),
			(try_end),
		(try_end), #Division Loop	
		
		(team_set_slot, ":team", slot_team_num_infantry, ":num_infantry"),
		(team_set_slot, ":team", slot_team_num_archers, ":num_archers"),
		(team_set_slot, ":team", slot_team_num_cavalry, ":num_cavalry"),

		#Team Leader Additions
		(try_begin),
		    (eq, ":team", 0),
			(val_add, ":team_size", ":team0_leader"),
			(val_add, ":team_level", ":team0_level_leader"),
			(val_add, ":team_x", ":team0_x_leader"),
			(val_add, ":team_y", ":team0_y_leader"),
		(else_try),
		    (eq, ":team", 1),
			(val_add, ":team_size", ":team1_leader"),
			(val_add, ":team_level", ":team1_level_leader"),
			(val_add, ":team_x", ":team1_x_leader"),
			(val_add, ":team_y", ":team1_y_leader"),
		(else_try),
			(eq, ":team", 2),
			(val_add, ":team_size", ":team2_leader"),
			(val_add, ":team_level", ":team2_level_leader"),
			(val_add, ":team_x", ":team2_x_leader"),
			(val_add, ":team_y", ":team2_y_leader"),
		(else_try),
			(eq, ":team", 3),
			(val_add, ":team_size", ":team3_leader"),
			(val_add, ":team_level", ":team3_level_leader"),
			(val_add, ":team_x", ":team3_x_leader"),
			(val_add, ":team_y", ":team3_y_leader"),		
		(try_end),
		
		#calculate team averages 
		(gt, ":team_size", 0),
		(team_set_slot, ":team", slot_team_size, ":team_size"),
		(val_div, ":team_level", ":team_size"),
		(team_set_slot, ":team", slot_team_level, ":team_level"),	
			
		(team_get_slot, ":value", ":team", slot_team_percent_ranged_throw),
		(val_mul, ":value", 100),
		(try_begin),
		    (gt, ":num_archers", 0),
		    (val_div, ":value", ":num_archers"), 
		(else_try),
		    (assign, ":value", 0),
		(try_end),
		(team_set_slot, ":team", slot_team_percent_ranged_throw, ":value"),	

        (team_get_slot, ":value", ":team", slot_team_percent_cavalry_are_archers),
		(val_mul, ":value", 100),
		(try_begin),
		    (gt, ":num_cavalry", 0),
		    (val_div, ":value", ":num_cavalry"),
		(else_try),
		    (assign, ":value", 0),
		(try_end),
		(team_set_slot, ":team", slot_team_percent_cavalry_are_archers, ":value"),	
		
		(val_div, ":team_x", ":team_size"),
		(team_set_slot, ":team", slot_team_avg_x, ":team_x"),
		(val_div, ":team_y", ":team_size"),
		(team_set_slot, ":team", slot_team_avg_y, ":team_y"),
		
		#(store_mul, ":team_shift", ":team", 4),
		#(store_add, ":position_number", Team0_Average_Pos, ":team_shift"),
		# (store_add, ":position_number", Team0_Average_Pos, ":team"),
		# (init_position, ":position_number"),		
		# (val_div, ":team_x", ":team_size"),
		# (position_set_x, ":position_number", ":team_x"),
		# (val_div, ":team_y", ":team_size"),
		# (position_set_y, ":position_number", ":team_y"),
		# (position_set_z_to_ground_level, ":position_number"),
	(try_end), #Team Loop
	]),

	
  # script_team_get_position_of_enemies by motomataru #CABA - EDITED FOR SLOTS AND MANY DIVISIONS
  # Input: destination position, team, troop class/division
  # Output: destination position: average position if reg0 > 0
  #			reg0: number of enemies
  # Run script_store_battlegroup_data before calling!
  ("team_get_position_of_enemies", [
	(store_script_param, ":enemy_position", 1),
	(store_script_param, ":team_no", 2),
	(store_script_param, ":troop_type", 3),
	(assign, ":pos_x", 0),
	(assign, ":pos_y", 0),
	(assign, ":total_size", 0),
	
	(try_for_range, ":other_team", 0, 4),
		(teams_are_enemies, ":other_team", ":team_no"),
		(try_begin),
			(eq, ":troop_type", grc_everyone),
			(team_get_slot, ":team_size", ":other_team", slot_team_size), #battlegroup_get_size phaseout
			(try_begin),
				(gt, ":team_size", 0),
				(call_script, "script_battlegroup_get_position", ":enemy_position", ":other_team", grc_everyone),
				(position_get_x, reg0, ":enemy_position"),
				(val_mul, reg0, ":team_size"),
				(val_add, ":pos_x", reg0),
				(position_get_y, reg0, ":enemy_position"),
				(val_mul, reg0, ":team_size"),
				(val_add, ":pos_y", reg0),
			(try_end),
		(else_try),
			(assign, ":team_size", 0),
			#(try_begin),
			#	(eq, ":other_team", "$fplayer_team_no"),
			#	(assign, ":num_groups", 9),
			#(else_try),
			#	(assign, ":num_groups", 3),
			#(try_end),
			(try_for_range, ":enemy_battle_group", 0, 9),
				(eq, ":enemy_battle_group", ":troop_type"),
				(store_add, ":slot", slot_team_d0_size, ":troop_type"), #battlegroup_get_size phase out
	            (team_get_slot, ":troop_count", ":other_team", ":slot"),
				(gt, ":troop_count", 0),
				(val_add, ":team_size", ":troop_count"),
				(call_script, "script_battlegroup_get_position", ":enemy_position", ":other_team", ":troop_type"),
				(position_get_x, reg0, ":enemy_position"),
				(val_mul, reg0, ":team_size"),
				(val_add, ":pos_x", reg0),
				(position_get_y, reg0, ":enemy_position"),
				(val_mul, reg0, ":team_size"),
				(val_add, ":pos_y", reg0),
			(try_end),
		(try_end),
		(val_add, ":total_size", ":team_size"),
	(try_end),
	
	(try_begin),
		(eq, ":total_size", 0),
		(init_position, ":enemy_position"),
	(else_try),
		(val_div, ":pos_x", ":total_size"),
		(position_set_x, ":enemy_position", ":pos_x"),
		(val_div, ":pos_y", ":total_size"),
		(position_set_y, ":enemy_position", ":pos_y"),
		(position_set_z_to_ground_level, ":enemy_position"),
	(try_end),

	(assign, reg0, ":total_size"),
  ]),
  
  
  
# # Autoloot improved by rubik begin
  
  ("get_item_score_with_imod", [
    (store_script_param, ":item", 1),
    (store_script_param, ":imod", 2),

    (item_get_type, ":type", ":item"),
    (try_begin),
      (eq, ":type", itp_type_book),
      (item_get_slot, ":i_score", ":item", slot_item_intelligence_requirement),
    (else_try),
      (eq, ":type", itp_type_horse),
      (item_get_slot, ":horse_speed", ":item", slot_item_horse_speed),
      (item_get_slot, ":horse_armor", ":item", slot_item_horse_armor),
      (item_get_slot, ":horse_charge", ":item", slot_item_horse_charge),

      (try_begin),
        (eq, ":imod", imod_swaybacked),
        (val_add, ":horse_speed", -2),
      (else_try),
        (eq, ":imod", imod_lame),
        (val_add, ":horse_speed", -5),
      (else_try),
        (eq, ":imod", imod_heavy),
        (val_add, ":horse_armor", 3),
        (val_add, ":horse_charge", 4),
      (else_try),
        (eq, ":imod", imod_spirited),
        (val_add, ":horse_speed", 1),
        (val_add, ":horse_armor", 1),
        (val_add, ":horse_charge", 1),
      (else_try),
        (eq, ":imod", imod_champion),
        (val_add, ":horse_speed", 2),
        (val_add, ":horse_armor", 2),
        (val_add, ":horse_charge", 2),
      (try_end),

      (store_mul, ":i_score", ":horse_speed", ":horse_armor"),
      (val_mul, ":i_score", ":horse_charge"),
    (else_try),
      (eq, ":type", itp_type_shield),
      (item_get_slot, ":shield_size", ":item", slot_item_length),
      (item_get_slot, ":shield_armor", ":item", slot_item_body_armor),
      (item_get_slot, ":shield_speed", ":item", slot_item_speed),

      (try_begin),
        (eq, ":imod", imod_cracked),
        (val_add, ":shield_armor", -4),
      (else_try),
        (eq, ":imod", imod_battered),
        (val_add, ":shield_armor", -2),
      (else_try),
        (eq, ":imod", imod_thick),
        (val_add, ":shield_armor", 2),
      (else_try),
        (eq, ":imod", imod_reinforced),
        (val_add, ":shield_armor", 4),
      (try_end),

      (val_add, ":shield_armor", 5),
      (store_mul, ":i_score", ":shield_armor", ":shield_size"),
      (val_mul, ":i_score", ":shield_speed"),
    (else_try),
      (this_or_next|eq, ":type", itp_type_head_armor),
      (this_or_next|eq, ":type", itp_type_body_armor),
      (this_or_next|eq, ":type", itp_type_foot_armor),
      (eq, ":type", itp_type_hand_armor),
      (item_get_slot, ":head_armor", ":item", slot_item_head_armor),
      (item_get_slot, ":body_armor", ":item", slot_item_body_armor),
      (item_get_slot, ":leg_armor", ":item", slot_item_leg_armor),
      (store_add, ":i_score", ":head_armor", ":body_armor"),
      (val_add, ":i_score", ":leg_armor"),

      (assign, ":imod_effect_mul", 0),
      (try_begin),
        (gt, ":head_armor", 0),
        (val_add, ":imod_effect_mul", 1),
      (try_end),
      (try_begin),
        (gt, ":body_armor", 0),
        (val_add, ":imod_effect_mul", 1),
      (try_end),
      (try_begin),
        (gt, ":leg_armor", 0),
        (val_add, ":imod_effect_mul", 1),
      (try_end),

      (try_begin),
        (eq, ":imod", imod_plain),
        (assign, ":imod_effect", 0),
      (else_try),
        (eq, ":imod", imod_cracked),
        (assign, ":imod_effect", -4),
      (else_try),
        (eq, ":imod", imod_rusty),
        (assign, ":imod_effect", -3),
      (else_try),
        (eq, ":imod", imod_battered),
        (assign, ":imod_effect", -2),
      (else_try),
        (eq, ":imod", imod_crude),
        (assign, ":imod_effect", -1),
      (else_try),
        (eq, ":imod", imod_tattered),
        (assign, ":imod_effect", -3),
      (else_try),
        (eq, ":imod", imod_ragged),
        (assign, ":imod_effect", -2),
      (else_try),
        (eq, ":imod", imod_sturdy),
        (assign, ":imod_effect", 1),
      (else_try),
        (eq, ":imod", imod_thick),
        (assign, ":imod_effect", 2),
      (else_try),
        (eq, ":imod", imod_hardened),
        (assign, ":imod_effect", 3),
      (else_try),
        (eq, ":imod", imod_reinforced),
        (assign, ":imod_effect", 4),
      (else_try),
        (eq, ":imod", imod_lordly),
        (assign, ":imod_effect", 6),
      (try_end),

      (val_mul, ":imod_effect", ":imod_effect_mul"),
      (val_add, ":i_score", ":imod_effect"),
    (else_try),
      (this_or_next|eq, ":type", itp_type_one_handed_wpn),
      (this_or_next|eq, ":type", itp_type_two_handed_wpn),
      (this_or_next|eq, ":type", itp_type_bow),
      (this_or_next|eq, ":type", itp_type_crossbow),
      (eq, ":type", itp_type_polearm),
      (item_get_slot, ":item_speed", ":item", slot_item_speed),
      (item_get_slot, ":item_length", ":item", slot_item_length),
      (item_get_slot, ":swing_damage", ":item", slot_item_swing_damage),
      (item_get_slot, ":thrust_damage", ":item", slot_item_thrust_damage),
      (val_mod, ":swing_damage", 256),
      (val_mod, ":thrust_damage", 256),
      (assign, ":item_damage", ":swing_damage"),
      (val_max, ":item_damage", ":thrust_damage"),

      (try_begin),
        (eq, ":imod", imod_cracked),
        (val_add, ":item_damage", -5),
      (else_try),
        (eq, ":imod", imod_rusty),
        (val_add, ":item_damage", -3),
      (else_try),
        (eq, ":imod", imod_bent),
        (val_add, ":item_damage", -3),
        (val_add, ":item_speed", -3),
      (else_try),
        (eq, ":imod", imod_chipped),
        (val_add, ":item_damage", -1),
      (else_try),
        (eq, ":imod", imod_balanced),
        (val_add, ":item_damage", 3),
        (val_add, ":item_speed", 3),
      (else_try),
        (eq, ":imod", imod_tempered),
        (val_add, ":item_damage", 4),
      (else_try),
        (eq, ":imod", imod_masterwork),
        (val_add, ":item_damage", 5),
        (val_add, ":item_speed", 1),
      (else_try),
        (eq, ":imod", imod_heavy),
        (val_add, ":item_damage", 2),
        (val_add, ":item_speed", -2),
      (else_try),
        (eq, ":imod", imod_strong),
        (val_add, ":item_damage", 3),
        (val_add, ":item_speed", -3),
      (try_end),

      (try_begin),
        (this_or_next|eq, ":type", itp_type_bow),
        (eq, ":type", itp_type_crossbow),
        (store_mul, ":i_score", ":item_damage", ":item_speed"),
      (else_try),
        (this_or_next|eq, ":type", itp_type_one_handed_wpn),
        (this_or_next|eq, ":type", itp_type_two_handed_wpn),
        (eq, ":type", itp_type_polearm),
        (store_mul, ":i_score", ":item_damage", ":item_speed"),
        (val_mul, ":i_score", ":item_length"),
      (try_end),
    (else_try),
      (this_or_next|eq, ":type", itp_type_arrows),
      (this_or_next|eq, ":type", itp_type_bolts),
      (eq, ":type", itp_type_thrown),
      (item_get_slot, ":thrust_damage", ":item", slot_item_thrust_damage),
      (val_mod, ":thrust_damage", 256),
      (assign, ":i_score", ":thrust_damage"),
      (val_add, ":i_score", 3), # +3 to make sure damage > 0

      (try_begin),
        (eq, ":imod", imod_plain),
        (val_mul, ":i_score", 2),
      (else_try),
        (eq, ":imod", imod_large_bag),
        (val_mul, ":i_score", 2),
        (val_add, ":i_score", 1),
      (else_try),
        (eq, ":imod", imod_bent),
        (val_sub, ":i_score", 3),
        (val_mul, ":i_score", 2),
      (else_try),
        (eq, ":imod", imod_heavy),
        (val_add, ":i_score", 2),
        (val_mul, ":i_score", 2),
      (else_try),
        (eq, ":imod", imod_balanced),
        (val_add, ":i_score", 3),
        (val_mul, ":i_score", 2),
      (try_end),
    (try_end),

    (assign, reg0, ":i_score"),
  ]),
# # Autoloot improved by rubik end



# # M&B Standard AI with changes for formations #CABA - OK; Need expansion when new AI divisions to work with
  # script_formation_battle_tactic_init_aux
  # Input: team_no, battle_tactic
  # Output: none
  ("formation_battle_tactic_init_aux",
    [
      (store_script_param, ":team_no", 1),
      (store_script_param, ":battle_tactic", 2),
      (team_get_leader, ":ai_leader", ":team_no"),
      (try_begin),
        (eq, ":battle_tactic", btactic_hold),
        (agent_get_position, pos1, ":ai_leader"),
        (call_script, "script_find_high_ground_around_pos1", ":team_no", 30),
        (copy_position, pos1, pos52),
        (call_script, "script_find_high_ground_around_pos1", ":team_no", 30), # call again just in case we are not at peak point.
        (copy_position, pos1, pos52),
        (call_script, "script_find_high_ground_around_pos1", ":team_no", 30), # call again just in case we are not at peak point.
        (team_give_order, ":team_no", grc_everyone, mordr_hold),
        (team_set_order_position, ":team_no", grc_everyone, pos52),
        (team_give_order, ":team_no", grc_archers, mordr_advance),
        (team_give_order, ":team_no", grc_archers, mordr_advance),
      (else_try),
        (eq, ":battle_tactic", btactic_follow_leader),
        (team_get_leader, ":ai_leader", ":team_no"),
        (ge, ":ai_leader", 0),
        (agent_set_speed_limit, ":ai_leader", 8),
        (agent_get_position, pos60, ":ai_leader"),
        (team_give_order, ":team_no", grc_everyone, mordr_hold),
        (team_set_order_position, ":team_no", grc_everyone, pos60),
      (try_end),
# formations additions
	  (try_begin),
		(call_script, "script_cf_formation", ":team_no", grc_infantry, 0, formation_default),
	  (try_end),
	  (try_begin),
		(call_script, "script_cf_formation", ":team_no", grc_cavalry, 0, formation_wedge),
	  (try_end),
	  (try_begin),
		(call_script, "script_cf_formation", ":team_no", grc_archers, 2, formation_default),
	  (try_end),
	  (team_give_order, ":team_no", grc_archers, mordr_spread_out),
	  (team_give_order, ":team_no", grc_archers, mordr_spread_out),
# end formations additions
  ]),
  
  # script_formation_battle_tactic_apply_aux #CABA - OK; Need expansion when new AI divisions to work with
  # Input: team_no, battle_tactic
  # Output: battle_tactic
  ("formation_battle_tactic_apply_aux",
    [
      (store_script_param, ":team_no", 1),
      (store_script_param, ":battle_tactic", 2),
      (store_mission_timer_a, ":mission_time"),
      (try_begin),
        (eq, ":battle_tactic", btactic_hold),
        (copy_position, pos1, pos52),
        (call_script, "script_get_closest3_distance_of_enemies_at_pos1", ":team_no", 1),
        (assign, ":avg_dist", reg0),
        (assign, ":min_dist", reg1),
        (try_begin),
          (this_or_next|lt, ":min_dist", 1000),
          (lt, ":avg_dist", 4000),
          (assign, ":battle_tactic", 0),
		  (call_script, "script_formation_end", ":team_no", grc_everyone),	#formations
          (team_give_order, ":team_no", grc_everyone, mordr_charge),
        (try_end),
      (else_try),
        (eq, ":battle_tactic", btactic_follow_leader),
        (team_get_leader, ":ai_leader", ":team_no"),
        (try_begin),
          (agent_is_alive, ":ai_leader"),
          (agent_set_speed_limit, ":ai_leader", 9),
          (call_script, "script_team_get_average_position_of_enemies", ":team_no"),
          (copy_position, pos60, pos0),
          (ge, ":ai_leader", 0),
          (agent_get_position, pos61, ":ai_leader"),
          (position_transform_position_to_local, pos62, pos61, pos60), #pos62 = vector to enemy w.r.t leader
          (position_normalize_origin, ":distance_to_enemy", pos62),
          (convert_from_fixed_point, ":distance_to_enemy"),
          (assign, reg17, ":distance_to_enemy"),
          (position_get_x, ":dir_x", pos62),
          (position_get_y, ":dir_y", pos62),
          (val_mul, ":dir_x", 23),
          (val_mul, ":dir_y", 23), #move 23 meters
          (position_set_x, pos62, ":dir_x"),
          (position_set_y, pos62, ":dir_y"),
        
          (position_transform_position_to_parent, pos63, pos61, pos62), #pos63 is 23m away from leader in the direction of the enemy.
          (position_set_z_to_ground_level, pos63),
        
          (team_give_order, ":team_no", grc_everyone, mordr_hold),
          (team_set_order_position, ":team_no", grc_everyone, pos63),
#formations code
		  (call_script, "script_point_y_toward_position", pos63, pos60),
		  (agent_get_position, pos49, ":ai_leader"),
		  (agent_set_position, ":ai_leader", pos63),	#fake out script_cf_formation
		  (try_begin),
			(call_script, "script_cf_formation", ":team_no", grc_infantry, 0, formation_default),
		  (try_end),
		  (try_begin),
			(call_script, "script_cf_formation", ":team_no", grc_cavalry, 0, formation_wedge),
		  (try_end),
		  (try_begin),
			(call_script, "script_cf_formation", ":team_no", grc_archers, 2, formation_default),
		  (try_end),
		  (agent_set_position, ":ai_leader", pos49),
#end formations code
          (agent_get_position, pos1, ":ai_leader"),
          (try_begin),
            (lt, ":distance_to_enemy", 50),
            (ge, ":mission_time", 30),
            (assign, ":battle_tactic", 0),
			(call_script, "script_formation_end", ":team_no", grc_everyone),	#formations code
            (team_give_order, ":team_no", grc_everyone, mordr_charge),
            (agent_set_speed_limit, ":ai_leader", 60),
          (try_end),
        (else_try),
          (assign, ":battle_tactic", 0),
		  (call_script, "script_formation_end", ":team_no", grc_everyone),	#formations code
          (team_give_order, ":team_no", grc_everyone, mordr_charge),
        (try_end),
      (try_end),
      
      (try_begin), # charge everyone after a while
        (neq, ":battle_tactic", 0),
        (ge, ":mission_time", 300),
        (assign, ":battle_tactic", 0),
		(call_script, "script_formation_end", ":team_no", grc_everyone),	#formations code
        (team_give_order, ":team_no", grc_everyone, mordr_charge),
        (team_get_leader, ":ai_leader", ":team_no"),
        (agent_set_speed_limit, ":ai_leader", 60),
      (try_end),
      (assign, reg0, ":battle_tactic"),
  ]),
  
  # Replacement script for battle_tactic_init_aux to switch between using #CABA - OK
  # M&B Standard AI with changes for formations and original based on
  # NOTE: original script "battle_tactic_init_aux" should be renamed to "orig_battle_tactic_init_aux"
  # constant formation_native_ai_use_formation ( 0: original, 1: use formation )
  # script_battle_tactic_init_aux
  # Input: team_no, battle_tactic
  # Output: none
  ("battle_tactic_init_aux",
    [
      (store_script_param, ":team_no", 1),
      (store_script_param, ":battle_tactic", 2),
	  (try_begin),
		#(eq, formation_native_ai_use_formation, 1),
		(party_slot_eq, "p_main_party", slot_party_pref_formations, 1),
		(call_script, "script_formation_battle_tactic_init_aux", ":team_no", ":battle_tactic"),
	  (else_try),
		(call_script, "script_orig_battle_tactic_init_aux", ":team_no", ":battle_tactic"),
	  (try_end),
    ]),

  # Replacement script for battle_tactic_init_aux to switch between using #CABA - OK
  # M&B Standard AI with changes for formations and original based on
  # NOTE: original script "battle_tactic_apply_aux" should be renamed to "orig_battle_tactic_apply_aux"
  # constant formation_native_ai_use_formation ( 0: original, 1: use formation )
  # script_battle_tactic_apply_aux
  # Input: team_no, battle_tactic
  # Output: battle_tactic
  ("battle_tactic_apply_aux",
    [
      (store_script_param, ":team_no", 1),
      (store_script_param, ":battle_tactic", 2),
	  (try_begin),
		#(eq, formation_native_ai_use_formation, 1),
		(party_slot_eq, "p_main_party", slot_party_pref_formations, 1),
		(call_script, "script_formation_battle_tactic_apply_aux", ":team_no", ":battle_tactic"),
	  (else_try),
		(call_script, "script_orig_battle_tactic_apply_aux", ":team_no", ":battle_tactic"),
	  (try_end),
  ]),

] # scripts


def modmerge(var_set):
	try:
		from modmerger_options import module_sys_info
		version = module_sys_info["version"]
	except:
		version = 1127 # version not specified.  assume latest warband at this time

	try:
		var_name_1 = "scripts"
		orig_scripts = var_set[var_name_1]
		
		modmerge_formations_scripts(orig_scripts)
		
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)

from util_wrappers import *
from util_scripts import *

scripts_directives = [
	#rename scripts to "insert" switch scripts (see end of scripts[])
	[SD_RENAME, "battle_tactic_init_aux" , "orig_battle_tactic_init_aux"],
	[SD_RENAME, "battle_tactic_apply_aux" , "orig_battle_tactic_apply_aux"],
	#insert formations before last call in team_give_order_from_order_panel
	[SD_OP_BLOCK_INSERT, "team_give_order_from_order_panel", D_SEARCH_FROM_BOTTOM | D_SEARCH_LINENUMBER | D_INSERT_BEFORE, 0, 0, [
		(call_script, "script_player_order_formations", ":order"),	#for formations
	]],
] # scripts_rename

def modmerge_formations_scripts(orig_scripts):
	# process script directives first
	process_script_directives(orig_scripts, scripts_directives)
	# add remaining scripts
	add_scripts(orig_scripts, scripts, True)