# Formations AI for Warband by Motomataru
# rel. 12/26/10

from header_common import *
from header_operations import *
from module_constants import *
from header_mission_templates import *
from header_items import *

####################################################################################################################
# scripts is a list of script records.
# Each script record contns the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################


formAI_scripts = [
# # AI with Formations Scripts    #MODIFIED FOR SLOTS BY CABA
  # script_calculate_decision_numbers by motomataru
  # Input: AI team, size relative to battle in %
  # Output: reg0 - battle presence plus level bump, reg1 - level bump (team avg level / 3)
  ("calculate_decision_numbers", [
	(store_script_param, ":team_no", 1),
	(store_script_param, ":battle_presence", 2),
	(try_begin),
		#(call_script, "script_battlegroup_get_level", ":team_no", grc_everyone),
		(team_get_slot, reg0, ":team_no", slot_team_level),
		(store_div, reg1, reg0, 3),
		(store_add, reg0, ":battle_presence", reg1),	#decision w.r.t. all enemy teams
	(try_end)
	]),
	

  # script_team_field_ranged_tactics by motomataru #EDITED FOR SLOTS BY CABA...many divisions changes necessary
  # Input: AI team, size relative to largest team in %, size relative to battle in %
  # Output: none
  ("team_field_ranged_tactics", [
	(store_script_param, ":team_no", 1),
	(store_script_param, ":rel_army_size", 2),
	(store_script_param, ":battle_presence", 3),
	(assign, ":bgroup", grc_archers), #Pre-Many Divisions
	(assign, ":bg_pos", Archers_Pos), #Pre-Many Divisions
	#(call_script, "script_battlegroup_get_size", ":team_no", grc_archers),
	(store_add, ":slot", slot_team_d0_size, ":bgroup"),
	(team_get_slot, reg0, ":team_no", ":slot"),
	(try_begin),
		(gt, reg0, 0),
		(call_script, "script_battlegroup_get_position", ":bg_pos", ":team_no", ":bgroup"), #CABA - OK
		(call_script, "script_team_get_position_of_enemies", Enemy_Team_Pos, ":team_no", grc_everyone), #CABA - OK
		(call_script, "script_point_y_toward_position", ":bg_pos", Enemy_Team_Pos), #CABA - OK
		(call_script, "script_get_nearest_enemy_battlegroup_location", Nearest_Enemy_Battlegroup_Pos, ":team_no", ":bg_pos"), #CABA - OK
		(assign, ":distance_to_enemy", reg0),
			
		(call_script, "script_calculate_decision_numbers", ":team_no", ":battle_presence"),
		(assign, ":decision_index", reg0),
		(assign, ":level_bump", reg1),
		(try_begin),
			(gt, ":decision_index", 86),	#outpower enemies more than 6:1?
			(team_give_order, ":team_no", ":bgroup", mordr_charge),

		(else_try),
			(ge, "$battle_phase", BP_Jockey),
			(team_slot_eq, ":team_no", slot_team_archers_have_ammo, 0), #running out of ammo?
			(team_give_order, ":team_no", ":bgroup", mordr_charge),

		(else_try),
			(gt, "$cur_casualties", 0),
			(eq, "$cur_casualties", "$prev_casualties"),	#no new casualties since last function call?
			(gt, ":decision_index", Advance_More_Point),
			(le, ":distance_to_enemy", AI_long_range),	#closer than reposition?
			(team_give_order, ":team_no", ":bgroup", mordr_advance),

		#hold somewhere
		(else_try),
			(store_add, ":decision_index", ":rel_army_size", ":level_bump"),	#decision w.r.t. largest enemy team
			(assign, ":move_archers", 0),
			(try_begin),
				(eq, "$battle_phase", BP_Setup),
				(assign, ":move_archers", 1),
			(else_try),
				(ge, "$battle_phase", BP_Fight),
				(try_begin),
					(neg|is_between, ":distance_to_enemy", AI_charge_distance, AI_long_range),
					(assign, ":move_archers", 1),
				(else_try),
					(lt, ":decision_index", Hold_Point),	#probably coming from a defensive position (see below)
					(gt, ":distance_to_enemy", AI_firing_distance),
					(assign, ":move_archers", 1),
				(try_end),
			(else_try),
				(ge, ":decision_index", Hold_Point),	#not starting in a defensive position (see below)
				#(call_script, "script_battlegroup_get_size", ":team_no", grc_infantry),
				(store_add, ":slot", slot_team_d0_size, grc_infantry), #CABA - EDIT NEEDED????
				(team_get_slot, reg0, ":team_no", ":slot"),
				(try_begin),
					(this_or_next|eq, reg0, 0),
					(gt, ":distance_to_enemy", AI_long_range),
					(assign, ":move_archers", 1),
				(else_try),	#don't outstrip infantry when closing
					(call_script, "script_battlegroup_get_position", Infantry_Pos, ":team_no", grc_infantry), #CABA - POS EDIT
					(get_distance_between_positions, ":infantry_to_enemy", Infantry_Pos, Nearest_Enemy_Battlegroup_Pos),
					(val_sub, ":infantry_to_enemy", ":distance_to_enemy"),
					(le, ":infantry_to_enemy", 1500),
					(assign, ":move_archers", 1),
				(try_end),
			(try_end),
			
			(try_begin),
				(gt, ":move_archers", 0),
				(try_begin), #CABA - POS EDIT?
					(eq, ":team_no", 0),
					(assign, ":team_start_pos", Team0_Starting_Point),
				(else_try),
					(eq, ":team_no", 1),
					(assign, ":team_start_pos", Team1_Starting_Point),
				(else_try),
					(eq, ":team_no", 2),
					(assign, ":team_start_pos", Team2_Starting_Point),
				(else_try),
					(eq, ":team_no", 3),
					(assign, ":team_start_pos", Team3_Starting_Point),
				(try_end),

				(try_begin),
					(lt, ":decision_index", Hold_Point),	#outnumbered?
					(lt, "$battle_phase", BP_Fight),
					(store_div, ":distance_to_move", ":distance_to_enemy", 6),	#middle of rear third of battlefield
					(assign, ":hill_search_radius", ":distance_to_move"),

				(else_try),
					(assign, ":from_start_pos", 0),					
					(try_begin),
						(ge, "$battle_phase", BP_Fight),
						(assign, ":from_start_pos", 1),
					(else_try),
						(gt, "$battle_phase", BP_Setup),
						(call_script, "script_point_y_toward_position", ":team_start_pos", ":bg_pos"),
						(position_get_rotation_around_z, reg0, ":team_start_pos"),
						(position_get_rotation_around_z, reg1, ":bg_pos"),
						(val_sub, reg0, reg1),
						(neg|is_between, reg0, -45, 45),
						(assign, ":from_start_pos", 1),
					(try_end),
					
					(try_begin),
						(gt, ":from_start_pos", 0),
						(copy_position, ":bg_pos", ":team_start_pos"),
						(call_script, "script_point_y_toward_position", ":bg_pos", Enemy_Team_Pos),
						(call_script, "script_get_nearest_enemy_battlegroup_location", Nearest_Enemy_Battlegroup_Pos, ":team_no", ":bg_pos"),
						(assign, ":distance_to_enemy", reg0),
					(try_end),

					(try_begin),
						(eq, "$battle_phase", BP_Setup),
						(assign, ":shot_distance", AI_long_range),
					(else_try),
						(assign, ":shot_distance", AI_firing_distance),
						(team_get_slot, reg0, ":team_no", slot_team_percent_ranged_throw),
						(store_sub, reg1, AI_firing_distance, AI_charge_distance),
						(val_add, reg1, 200),	#add two meters to prevent automatically provoking melee from forward enemy infantry
						(val_mul, reg1, reg0),
						(val_div, reg1, 100),
						(val_sub, ":shot_distance", reg1),
					(try_end),

					(store_sub, ":distance_to_move", ":distance_to_enemy", ":shot_distance"),
					(store_div, ":hill_search_radius", ":shot_distance", 3),	#limit so as not to run into enemy
					(try_begin),
						(lt, "$battle_phase", BP_Fight),
						(try_begin),
							(this_or_next|eq, "$battle_phase", BP_Setup),
							(lt, ":battle_presence", Advance_More_Point),	#expect to meet halfway?
							(val_div, ":distance_to_move", 2),
						(try_end),
					(try_end),
				(try_end),

				(position_move_y, ":bg_pos", ":distance_to_move", 0),
				(try_begin),
					(lt, "$battle_phase", BP_Fight),
					(copy_position, pos1, ":bg_pos"),
					(store_div, reg0, ":hill_search_radius", 100),
					(call_script, "script_find_high_ground_around_pos1_corrected", ":bg_pos", reg0),
				(try_end),
			(try_end),

			(team_give_order, ":team_no", ":bgroup", mordr_hold),
			(team_set_order_position, ":team_no", ":bgroup", ":bg_pos"),
		(try_end),
	(try_end)
	]),

	  
  # script_team_field_melee_tactics by motomataru #EDITED FOR SLOTS BY CABA...many divisions changes necessary
  # Input: AI team, size relative to largest team in %, size relative to battle in %
  # Output: none
  ("team_field_melee_tactics", [
	(store_script_param, ":team_no", 1),
#	(store_script_param, ":rel_army_size", 2),
	(store_script_param, ":battle_presence", 3),
	(call_script, "script_calculate_decision_numbers", ":team_no", ":battle_presence"),

	#mop up if outnumber enemies more than 6:1
	(try_begin),
		(gt, reg0, 86),
		(try_for_range, ":division", 0, 9),
		    (store_add, ":slot", slot_team_d0_size, ":division"),
			(team_slot_ge, ":team_no", ":slot", 1),
		    (store_add, ":slot", slot_team_d0_type, ":division"),
		    (neg|team_slot_eq, ":team_no", ":slot", sdt_archer),
			(neg|team_slot_eq, ":team_no", ":slot", sdt_skirmisher),
			(neg|team_slot_eq, ":team_no", ":slot", sdt_harcher), #possibly?
			(call_script, "script_formation_end", ":team_no", ":division"),
			(team_give_order, ":team_no", ":division", mordr_charge),
		(try_end),

	(else_try),
		#find closest distance of enemy to infantry, cavalry troops
		(assign, ":inf_closest_dist", Far_Away),
		(assign, ":inf_closest_non_cav_dist", Far_Away),
		(assign, ":cav_closest_dist", Far_Away),
		(assign, ":num_enemies_in_melee", 0),
		(assign, ":num_enemies_supporting_melee", 0),
		(assign, ":num_enemy_infantry", 0),
		(assign, ":num_enemy_cavalry", 0),
		(assign, ":num_enemy_others", 0),
		(assign, ":sum_level_enemy_infantry", 0),
		(assign, ":x_enemy", 0),
		(assign, ":y_enemy", 0),
		(try_for_agents, ":enemy_agent"),
			(agent_is_alive, ":enemy_agent"),
			(agent_is_human, ":enemy_agent"),
			(agent_get_team, ":enemy_team_no", ":enemy_agent"),
			(teams_are_enemies, ":enemy_team_no", ":team_no"),
			(agent_slot_eq, ":enemy_agent", slot_agent_is_running_away, 0),
			(agent_get_class, ":enemy_class_no", ":enemy_agent"),
			(try_begin),
				(eq, ":enemy_class_no", grc_infantry),
				(val_add, ":num_enemy_infantry", 1),
				(agent_get_troop_id, ":enemy_troop", ":enemy_agent"),
				(store_character_level, ":enemy_level", ":enemy_troop"),
				(val_add, ":sum_level_enemy_infantry", ":enemy_level"),
			(else_try),
				(eq, ":enemy_class_no", grc_cavalry),
				(val_add, ":num_enemy_cavalry", 1),
			(else_try),
				(val_add, ":num_enemy_others", 1),
			(try_end),
			(agent_get_position, pos0, ":enemy_agent"),
			(position_get_x, ":value", pos0),
			(val_add, ":x_enemy", ":value"),
			(position_get_y, ":value", pos0),
			(val_add, ":y_enemy", ":value"),
			(assign, ":enemy_in_melee", 0),
			(assign, ":enemy_supporting_melee", 0),
			(try_for_agents, ":cur_agent"),
				(agent_is_alive, ":cur_agent"),
				(agent_is_human, ":cur_agent"),
				(agent_get_team, ":cur_team_no", ":cur_agent"),
				(eq, ":cur_team_no", ":team_no"),
				(agent_slot_eq, ":cur_agent", slot_agent_is_running_away, 0),
				(agent_get_class, ":cur_class_no", ":cur_agent"),
				(try_begin),
					(eq, ":cur_class_no", grc_infantry),
					(agent_get_position, pos1, ":cur_agent"),
					(get_distance_between_positions, ":distance_of_enemy", pos0, pos1),
					(try_begin),
						(gt, ":inf_closest_dist", ":distance_of_enemy"),
						(assign, ":inf_closest_dist", ":distance_of_enemy"),
						(copy_position, Nearest_Enemy_Troop_Pos, pos0),
						(assign, ":enemy_nearest_troop_distance", ":distance_of_enemy"),
						(assign, ":enemy_nearest_agent", ":enemy_agent"),
					(try_end),
					(try_begin),
						(neq, ":enemy_class_no", grc_cavalry),
						(gt, ":inf_closest_non_cav_dist", ":distance_of_enemy"),
						(assign, ":inf_closest_non_cav_dist", ":distance_of_enemy"),
						(copy_position, Nearest_Non_Cav_Enemy_Troop_Pos, pos0),
						(assign, ":enemy_nearest_non_cav_troop_distance", ":distance_of_enemy"),
						(assign, ":enemy_nearest_non_cav_agent", ":enemy_agent"),
					(try_end),
					(try_begin),
						(lt, ":distance_of_enemy", 150),
						(assign, ":enemy_in_melee", 1),
					(try_end),
					(try_begin),
						(lt, ":distance_of_enemy", 350),
						(assign, ":enemy_supporting_melee", 1),
					(try_end),
				(else_try),
					(eq, ":cur_class_no", grc_cavalry),
					(agent_get_position, pos1, ":cur_agent"),
					(get_distance_between_positions, ":distance_of_enemy", pos0, pos1),
					(try_begin),
						(gt, ":cav_closest_dist", ":distance_of_enemy"),
						(assign, ":cav_closest_dist", ":distance_of_enemy"),
					(try_end),
				(try_end),
			(try_end),
			(try_begin),
				(eq, ":enemy_in_melee", 1),
				(val_add, ":num_enemies_in_melee", 1),
			(try_end),
			(try_begin),
				(eq, ":enemy_supporting_melee", 1),
				(val_add, ":num_enemies_supporting_melee", 1),
			(try_end),
		(try_end), #IS THERE A WAY TO SIMPLIFY THESE NESTED AGENT LOOPS?
		
		(store_add, ":num_enemies", ":num_enemy_infantry", ":num_enemy_cavalry"),
		(val_add, ":num_enemies", ":num_enemy_others"),
		(gt, ":num_enemies", 0),
		#WHY NOT USING STORED DATA?
		(init_position, Enemy_Team_Pos),
		(val_div, ":x_enemy", ":num_enemies"),
		(position_set_x, Enemy_Team_Pos, ":x_enemy"),
		(val_div, ":y_enemy", ":num_enemies"),
		(position_set_y, Enemy_Team_Pos, ":y_enemy"),
		(position_set_z_to_ground_level, Enemy_Team_Pos),

		#(call_script, "script_battlegroup_get_size", ":team_no", grc_archers),
		#(assign, ":num_archers", reg0),
		(store_add, ":slot", slot_team_d0_size, grc_archers),
		(team_get_slot, ":num_archers", ":team_no", ":slot"),
		(try_begin),
			(eq, ":num_archers", 0),
			(assign, ":enemy_from_archers", Far_Away),
			(assign, ":archer_order", mordr_charge),
		(else_try),
			(call_script, "script_battlegroup_get_position", Archers_Pos, ":team_no", grc_archers),
			(call_script, "script_point_y_toward_position", Archers_Pos, Enemy_Team_Pos),
			(call_script, "script_get_nearest_enemy_battlegroup_location", pos0, ":team_no", Archers_Pos),
			(assign, ":enemy_from_archers", reg0),
			(team_get_movement_order, ":archer_order", ":team_no", grc_archers),
		(try_end),

		#(call_script, "script_battlegroup_get_size", ":team_no", grc_infantry),
		#(assign, ":num_infantry", reg0),
		(store_add, ":slot", slot_team_d0_size, grc_infantry),
		(team_get_slot, ":num_infantry", ":team_no", ":slot"),
		(try_begin),
			(eq, ":num_infantry", 0),
			(assign, ":enemy_from_infantry", Far_Away),
		(else_try),
			(call_script, "script_battlegroup_get_position", Infantry_Pos, ":team_no", grc_infantry),
			(call_script, "script_get_nearest_enemy_battlegroup_location", pos0, ":team_no", Infantry_Pos),
			(assign, ":enemy_from_infantry", reg0),
		(try_end),

		#(call_script, "script_battlegroup_get_size", ":team_no", grc_cavalry),
		#(assign, ":num_cavalry", reg0),
		(store_add, ":slot", slot_team_d0_size, grc_cavalry),
		(team_get_slot, ":num_cavalry", ":team_no", ":slot"),
		(try_begin),
			(eq, ":num_cavalry", 0),
			(assign, ":enemy_from_cavalry", Far_Away),
		(else_try),
			(call_script, "script_battlegroup_get_position", Cavalry_Pos, ":team_no", grc_cavalry),
			(call_script, "script_get_nearest_enemy_battlegroup_location", pos0, ":team_no", Cavalry_Pos),
			(assign, ":enemy_from_cavalry", reg0),
		(try_end),

		(try_begin),
			(lt, "$battle_phase", BP_Fight),
			(this_or_next|le, ":enemy_from_infantry", AI_charge_distance),
			(this_or_next|le, ":enemy_from_cavalry", AI_charge_distance),
			(le, ":enemy_from_archers", AI_charge_distance),
			(assign, "$battle_phase", BP_Fight),
		(else_try),
			(lt, "$battle_phase", BP_Jockey),
			(this_or_next|le, ":inf_closest_dist", AI_long_range),
			(le, ":cav_closest_dist", AI_long_range),
			(assign, "$battle_phase", BP_Jockey),
		(try_end),
		
		(team_get_leader, ":team_leader", ":team_no"),
		
		#infantry AI
		(assign, ":place_leader_by_infantry", 0),
		(try_begin),
			(le, ":num_infantry", 0),
			(assign, ":infantry_order", ":archer_order"),
			
			#deal with mounted heroes that team_give_order() treats as infantry   #CABA...could change their division?
			(team_give_order, ":team_no", grc_infantry, ":infantry_order"),
			(try_begin),
				(gt, ":num_archers", 0),
				(copy_position, pos1, Archers_Pos),
				(position_move_y, pos1, 1000, 0),
				(team_set_order_position, ":team_no", grc_infantry, pos1),
			(else_try),
				(team_set_order_position, ":team_no", grc_infantry, Cavalry_Pos),
			(try_end),
		(else_try),
			(store_mul, ":percent_level_enemy_infantry", ":sum_level_enemy_infantry", 100),
			(val_div, ":percent_level_enemy_infantry", ":num_enemies"),
			(try_begin),
				(teams_are_enemies, ":team_no", "$fplayer_team_no"),
				(assign, ":combined_level", 0),
				(assign, ":combined_team_size", 0),
				(assign, ":combined_num_infantry", ":num_infantry"),
			(else_try),
				#(call_script, "script_battlegroup_get_level", "$fplayer_team_no", grc_infantry),
				#(assign, ":combined_level", reg0),
				#(call_script, "script_battlegroup_get_size", "$fplayer_team_no", grc_everyone),
				#(assign, ":combined_team_size", reg0),
				#(call_script, "script_battlegroup_get_size", "$fplayer_team_no", grc_infantry),
				#(store_add, ":combined_num_infantry", ":num_infantry", reg0),
				(store_add, ":slot", slot_team_d0_level, grc_infantry),
		        (team_get_slot, ":combined_level", "$fplayer_team_no", ":slot"),
		        (team_get_slot, ":combined_team_size", "$fplayer_team_no", slot_team_size),
				(store_add, ":slot", slot_team_d0_size, grc_infantry),
				(team_get_slot, ":combined_num_infantry", "$fplayer_team_no", ":slot"),
			(try_end),
			(store_mul, ":percent_level_infantry", ":combined_num_infantry", 100),
			#(call_script, "script_battlegroup_get_level", ":team_no", grc_infantry),
			#(assign, ":level_infantry", reg0),
			(store_add, ":slot", slot_team_d0_level, grc_infantry),
			(team_get_slot, ":level_infantry", ":team_no", ":slot"),
			(val_add, ":combined_level", ":level_infantry"),
			(val_mul, ":percent_level_infantry", ":combined_level"),
			#(call_script, "script_battlegroup_get_size", ":team_no", grc_everyone),
			(team_get_slot, reg0, ":team_no", slot_team_size),
			(val_add, ":combined_team_size", reg0),
			(val_div, ":percent_level_infantry", ":combined_team_size"),

			(assign, ":infantry_order", mordr_charge),
			(try_begin),	#enemy far away AND ranged not charging
				(gt, ":enemy_from_archers", AI_charge_distance),
				(gt, ":inf_closest_dist", AI_charge_distance),
				(neq, ":archer_order", mordr_charge),
				(try_begin),	#fighting not started OR not enough infantry
					(this_or_next|le, "$battle_phase", BP_Jockey),
					(lt, ":percent_level_infantry", ":percent_level_enemy_infantry"),
					(assign, ":infantry_order", mordr_hold),
				(try_end),
			(try_end),

			#if low level troops outnumber enemies in melee by 2:1, attempt to whelm
			(try_begin),
				(le, ":level_infantry", 12),
				(gt, ":num_enemies_in_melee", 0),
				(store_mul, reg0, ":num_enemies_supporting_melee", 2),
				(is_between, reg0, 1, ":num_infantry"),
				(get_distance_between_positions, reg0, Infantry_Pos, Nearest_Enemy_Troop_Pos),
				(le, reg0, AI_charge_distance),
				(call_script, "script_formation_end", ":team_no", grc_infantry),
				(team_give_order, ":team_no", grc_infantry, mordr_charge),
				
			#else attempt to form formation somewhere
			(else_try),
			    (team_get_slot, ":infantry_formation", ":team_no", slot_team_default_formation),
				(try_begin),
				    (eq, ":infantry_formation", formation_default),
				    (call_script, "script_get_default_formation", ":team_no"),
				    (assign, ":infantry_formation", reg0),
				    (team_set_slot, ":team_no", slot_team_default_formation, ":infantry_formation"),
				(try_end),
				# (try_begin),
					# (eq, ":team_no", 0),
					# (try_begin),
						# (eq, "$team0_default_formation", formation_default),
						# (call_script, "script_get_default_formation", 0),
						# (assign, "$team0_default_formation", reg0),
					# (try_end),
					# (assign, ":infantry_formation", "$team0_default_formation"),
				# (else_try),
					# (eq, ":team_no", 1),
					# (try_begin),
						# (eq, "$team1_default_formation", formation_default),
						# (call_script, "script_get_default_formation", 1),
						# (assign, "$team1_default_formation", reg0),
					# (try_end),
					# (assign, ":infantry_formation", "$team1_default_formation"),
				# (else_try),
					# (eq, ":team_no", 2),
					# (try_begin),
						# (eq, "$team2_default_formation", formation_default),
						# (call_script, "script_get_default_formation", 2),
						# (assign, "$team2_default_formation", reg0),
					# (try_end),
					# (assign, ":infantry_formation", "$team2_default_formation"),
				# (else_try),
					# (eq, ":team_no", 3),
					# (try_begin),
						# (eq, "$team3_default_formation", formation_default),
						# (call_script, "script_get_default_formation", 3),
						# (assign, "$team3_default_formation", reg0),
					# (try_end),
					# (assign, ":infantry_formation", "$team3_default_formation"),
				# (try_end),
				
				#(call_script, "script_classify_agent", ":enemy_nearest_agent"),
				#(assign, ":enemy_nearest_troop_battlegroup", reg0),
				(agent_get_division, ":enemy_nearest_troop_battlegroup", ":enemy_nearest_agent"),
				(agent_get_class, ":enemy_nearest_troop_class", ":enemy_nearest_agent"), 
				(agent_get_team, ":enemy_nearest_troop_team", ":enemy_nearest_agent"),
				(team_get_leader, ":enemy_leader", ":enemy_nearest_troop_team"),
				(store_mul, ":percent_enemy_cavalry", ":num_enemy_cavalry", 100),
				(val_div, ":percent_enemy_cavalry", ":num_enemies"),
				(try_begin),
					(neq, ":infantry_formation", formation_none),
					(try_begin),
						(gt, ":percent_enemy_cavalry", 66),
						(assign, ":infantry_formation", formation_square),
					(else_try),
						(neq, ":enemy_nearest_troop_class", grc_cavalry),
						(neq, ":enemy_nearest_troop_class", grc_archers),
						(neq, ":enemy_nearest_agent", ":enemy_leader"),
						#(call_script, "script_battlegroup_get_size", ":enemy_nearest_troop_team", ":enemy_nearest_troop_battlegroup"),
						(store_add, ":slot", slot_team_d0_size, ":enemy_nearest_troop_battlegroup"),
						(team_get_slot, reg0, ":enemy_nearest_troop_team", ":slot"),
						(gt, reg0, ":num_infantry"),	#got fewer troops?
						#(call_script, "script_battlegroup_get_level", ":team_no", grc_infantry),
						#(assign, ":average_level", reg0),
						(store_add, ":slot", slot_team_d0_level, grc_infantry),
						(team_get_slot, ":average_level", ":team_no", ":slot"),
						#(call_script, "script_battlegroup_get_level", ":enemy_nearest_troop_team", ":enemy_nearest_troop_battlegroup"),
						(store_add, ":slot", slot_team_d0_level, ":enemy_nearest_troop_battlegroup"),
						(team_get_slot, reg0, ":enemy_nearest_troop_team", ":slot"),
						(gt, ":average_level", reg0),	#got better troops?
						(assign, ":infantry_formation", formation_wedge),
					(try_end),
				(try_end),
				
				#hold near archers?
				(try_begin),
					(eq, ":infantry_order", mordr_hold),
					(gt, ":num_archers", 0),
					(copy_position, pos1, Archers_Pos),
					(position_move_x, pos1, -100, 0),
					(try_begin),
						(this_or_next|eq, ":enemy_nearest_troop_battlegroup", grc_cavalry),
						(gt, ":percent_level_infantry", ":percent_level_enemy_infantry"),
						(position_move_y, pos1, 1000, 0),	#move ahead of archers in anticipation of charges
					(else_try),
						(position_move_y, pos1, -1000, 0),
					(try_end),
					(assign, ":spacing", 1),

				#advance to nearest (preferably unmounted) enemy
				(else_try),
					(assign, ":target_battlegroup", -1),
					(assign, ":target_size", 1),
					(try_begin),
						(eq, ":num_enemies_in_melee", 0),	#not engaged?
						(gt, ":enemy_from_archers", AI_charge_distance),
						(lt, ":percent_enemy_cavalry", 100),
						(assign, ":distance_to_enemy_troop", ":enemy_nearest_non_cav_troop_distance"),
						(copy_position, pos60, Nearest_Non_Cav_Enemy_Troop_Pos),
						(agent_get_team, ":enemy_non_cav_team", ":enemy_nearest_non_cav_agent"),
						(assign, ":target_team", ":enemy_non_cav_team"),
						(team_get_leader, reg0, ":enemy_non_cav_team"),
						(try_begin),
						    (eq, ":enemy_nearest_non_cav_agent", reg0),
							#(eq, reg0, -1),
							(assign, ":distance_to_enemy_group", Far_Away),
						(else_try),
							#(call_script, "script_classify_agent", ":enemy_nearest_non_cav_agent"),
							#(assign, ":target_battlegroup", reg0),
							(agent_get_division, ":target_battlegroup", ":enemy_nearest_non_cav_agent"),
							(call_script, "script_battlegroup_get_position", pos0, ":enemy_non_cav_team", ":target_battlegroup"),
							(get_distance_between_positions, ":distance_to_enemy_group", Infantry_Pos, pos0),
							#(call_script, "script_battlegroup_get_size", ":enemy_non_cav_team", ":target_battlegroup"),
							#(assign, ":target_size", reg0),
							(store_add, ":slot", slot_team_d0_size, ":target_battlegroup"),
							(team_get_slot, ":target_size", ":enemy_non_cav_team", ":slot"),
						(try_end),
					(else_try),
						(assign, ":distance_to_enemy_troop", ":enemy_nearest_troop_distance"),
						(copy_position, pos60, Nearest_Enemy_Troop_Pos),
						(assign, ":target_team", ":enemy_nearest_troop_team"),
						(try_begin),
							(eq, ":enemy_nearest_agent", ":enemy_leader"),
							(assign, ":distance_to_enemy_group", Far_Away),
						(else_try),
							(assign, ":target_battlegroup", ":enemy_nearest_troop_battlegroup"),
							(call_script, "script_battlegroup_get_position", pos0, ":enemy_nearest_troop_team", ":target_battlegroup"),
							(get_distance_between_positions, ":distance_to_enemy_group", Infantry_Pos, pos0),
							#(call_script, "script_battlegroup_get_size", ":enemy_nearest_troop_team", ":target_battlegroup"),
							#(assign, ":target_size", reg0),
							(store_add, ":slot", slot_team_d0_size, ":target_battlegroup"),
							(team_get_slot, ":target_size", ":enemy_nearest_troop_team", ":slot"),
						(try_end),
					(try_end),
					
					(store_sub, reg0, ":distance_to_enemy_group", ":distance_to_enemy_troop"),
					#attack troop if its unit is far off
					(try_begin),
						(gt, reg0, AI_charge_distance),
						(copy_position, pos0, pos60),
						(assign, ":distance_to_move", ":distance_to_enemy_troop"),
						
					#attack unit
					(else_try),
						(assign, ":distance_to_move", ":distance_to_enemy_group"),
						#wedge pushes through to last enemy infantry rank
						(try_begin),
							(eq, ":infantry_formation", formation_wedge),
							(val_sub, ":distance_to_move", formation_minimum_spacing),

						#non-wedge stops before first rank of enemy
						(else_try),
							(store_mul, reg0, formation_minimum_spacing, 1.5),
							(val_sub, ":distance_to_move", reg0),
							
							#back up for enemies in deep formation
							(eq, ":target_battlegroup", grc_infantry),
							(ge, ":target_size", formation_min_foot_troops),
							(try_begin),
								(neq, ":target_team", "$fplayer_team_no"),
								(val_sub, ":distance_to_move", formation_minimum_spacing),
							(else_try),
								#(neq, "$infantry_formation_type", formation_none),
								(neg|team_slot_eq, "$fplayer_team_no", slot_team_d0_formation, formation_none),
								(val_sub, ":distance_to_move", formation_minimum_spacing),
							(try_end),
						(try_end),
					(try_end),

					#slow for formation appearance on approach
					(try_begin),
						(lt, ":num_infantry", formation_min_foot_troops),
						(assign, ":speed_adjust", 0),
					(else_try),
						(eq, ":infantry_formation", formation_square),
						(assign, reg0, ":num_infantry"),
						(convert_to_fixed_point, reg0),
						(store_sqrt, ":speed_adjust", reg0),
						(val_mul, ":speed_adjust", formation_minimum_spacing),
						(val_div, ":speed_adjust", 2),
						(convert_from_fixed_point, ":speed_adjust"),
					(else_try),
						(eq, ":infantry_formation", formation_wedge),
						(assign, reg0, ":num_infantry"),
						(convert_to_fixed_point, reg0),
						(store_sqrt, ":speed_adjust", reg0),
						(val_mul, ":speed_adjust", formation_minimum_spacing),
						(val_mul, ":speed_adjust", 2),
						(val_div, ":speed_adjust", 3),
						(convert_from_fixed_point, ":speed_adjust"),
					(else_try),
						(assign, ":speed_adjust", formation_minimum_spacing),
					(try_end),
					(try_begin),
						(le, ":distance_to_move", AI_charge_distance),
						(val_add, ":speed_adjust", 600),
					(else_try),
						(le, ":distance_to_move", AI_firing_distance),
						(val_add, ":speed_adjust", 1200),
					(else_try),
						(le, ":distance_to_move", AI_long_range),
						(val_add, ":speed_adjust", 1800),
					(try_end),
					(try_begin),
						(le, ":distance_to_move", AI_long_range),
						(val_min, ":distance_to_move", ":speed_adjust"),
					(try_end),

					#adjust position
					(copy_position, pos1, Infantry_Pos),
					(try_begin),
						(eq, ":num_enemies_in_melee", 0),
						(call_script, "script_point_y_toward_position", pos1, pos0),
						(position_move_y, pos1, ":distance_to_move"),
					(else_try),
						(call_script, "script_get_formation_position", pos2, ":team_no", grc_infantry),
						(position_copy_rotation, pos1, pos2),
						(position_move_y, pos1, -2000),
						(call_script, "script_point_y_toward_position", pos1, pos0),
						(position_move_y, pos1, 2000),
						(position_move_y, pos1, ":distance_to_move"),
					(try_end),
					(assign, ":spacing", 0),
				(try_end),

				(copy_position, pos61, pos1),
				(call_script, "script_get_centering_amount", ":infantry_formation", ":num_infantry", 0),
				(assign, ":centering", reg0),
				(try_begin),
					(neq, ":infantry_formation", formation_none),
					(ge, ":num_infantry", formation_min_foot_troops),
					(call_script, "script_set_formation_position", ":team_no", grc_infantry, pos1),
					(position_move_x, pos1, ":centering"),
					(assign, ":division", grc_infantry), #TEMP
					#(store_add, ":slot", slot_team_d0_formation_space, ":division"),
		            #(team_get_slot, ":div_spacing", ":team_no", ":slot"),
					(call_script, "script_form_infantry", ":team_no", ":team_leader", ":division", ":spacing", ":infantry_formation"),		
					(assign, ":place_leader_by_infantry", 1),
				(else_try),
					(call_script, "script_formation_end", ":team_no", grc_infantry),
					(eq, ":infantry_order", mordr_hold),
					(assign, ":place_leader_by_infantry", 1),
				(try_end),
				(team_give_order, ":team_no", grc_infantry, ":infantry_order"),
				(team_set_order_position, ":team_no", grc_infantry, pos61),
				(position_move_x, pos61, ":centering"),	#for possible leader positioning
			(try_end),
		(try_end),	
		
		#cavalry AI
		(try_begin),
			(gt, ":num_cavalry", 0),
			#get distance to nearest enemy battlegroup(s)
			#(call_script, "script_battlegroup_get_level", ":team_no", grc_cavalry),
			#(assign, ":average_level", reg0),
			(store_add, ":slot", slot_team_d0_level, grc_cavalry),
			(team_get_slot, ":average_level", ":team_no", ":slot"),
			(assign, ":nearest_threat_distance", Far_Away),
			(assign, ":nearest_target_distance", Far_Away),
			(assign, ":num_targets", 0),
			(try_for_range, ":enemy_team_no", 0, 4),
				#(call_script, "script_battlegroup_get_size", ":enemy_team_no", grc_everyone),
				#(gt, reg0, 0),
				(team_slot_ge, ":enemy_team_no", slot_team_size, 1),
				(teams_are_enemies, ":enemy_team_no", ":team_no"),
				#(try_begin),
				#	(eq, ":enemy_team_no", "$fplayer_team_no"),
				#	(assign, ":num_groups", 9),
				#(else_try),
				#	(assign, ":num_groups", 3),
				#(try_end),
				(try_for_range, ":enemy_battle_group", 0, 9),
					#(call_script, "script_battlegroup_get_size", ":enemy_team_no", ":enemy_battle_group"),
					#(assign, ":size_enemy_battle_group", reg0),
					(store_add, ":slot", slot_team_d0_size, ":enemy_battle_group"),
					(team_get_slot, ":size_enemy_battle_group", ":enemy_team_no", ":slot"),
					(gt, ":size_enemy_battle_group", 0),
					(call_script, "script_battlegroup_get_position", pos0, ":enemy_team_no", ":enemy_battle_group"),
					(get_distance_between_positions, ":distance_of_enemy", Cavalry_Pos, pos0),
					(try_begin),	#threat or target?
						#(call_script, "script_battlegroup_get_weapon_length", ":enemy_team_no", ":enemy_battle_group"),
						(store_add, ":slot", slot_team_d0_weapon_length, ":enemy_battle_group"),
						(team_get_slot, reg0, ":enemy_team_no", ":slot"),
						(assign, ":decision_index", reg0),
						#(call_script, "script_battlegroup_get_level", ":enemy_team_no", ":enemy_battle_group"),
						(store_add, ":slot", slot_team_d0_level, ":enemy_battle_group"),
						(team_get_slot, reg0, ":enemy_team_no", ":slot"),
						(val_mul, ":decision_index", reg0),
						(val_mul, ":decision_index", ":size_enemy_battle_group"),
						(val_div, ":decision_index", ":average_level"),
						(val_div, ":decision_index", ":num_cavalry"),
						(try_begin),
							(neq, ":enemy_battle_group", grc_cavalry),
							(val_div, ":decision_index", 2),	#double count cavalry vs. foot soldiers
						(try_end),
						(gt, ":decision_index", 100),
						(try_begin),
							(gt, ":nearest_threat_distance", ":distance_of_enemy"),
							(copy_position, Nearest_Threat_Pos, pos0),
							(assign, ":nearest_threat_distance", ":distance_of_enemy"),
						(try_end),
					(else_try),
						(val_add, ":num_targets", 1),
						(gt, ":nearest_target_distance", ":distance_of_enemy"),
						(copy_position, Nearest_Target_Pos, pos0),
						(assign, ":nearest_target_distance", ":distance_of_enemy"),
					(try_end),
				(try_end),
			(try_end),
			(try_begin),
				(eq, ":nearest_threat_distance", Far_Away),
				(assign, ":nearest_target_guarded", 0),
			(else_try),
				(eq, ":nearest_target_distance", Far_Away),
				(assign, ":nearest_target_guarded", 1),
			(else_try),
				(get_distance_between_positions, reg0, Nearest_Target_Pos, Nearest_Threat_Pos),
				(store_div, reg1, AI_charge_distance, 2),
				(try_begin),	#ignore target too close to threat
					(le, reg0, reg1),
					(assign, ":nearest_target_guarded", 1),
				(else_try),
					(assign, ":nearest_target_guarded", 0),
				(try_end),
			(try_end),

			(assign, ":cavalry_order", mordr_charge), ##CABA HERE
			(try_begin),
				(teams_are_enemies, ":team_no", 0),
				(neg|team_slot_ge, 1, slot_team_reinforcement_stage, 2),
				(neg|team_slot_eq, 1, slot_team_reinforcement_stage, "$attacker_reinforcement_stage"),
				#(lt, "$team1_reinforcement_stage", 2),
				#(neq, "$team1_reinforcement_stage", "$attacker_reinforcement_stage"),
				(assign, ":cavalry_order", mordr_hold),
			(else_try),
				(teams_are_enemies, ":team_no", 1),
				(neg|team_slot_ge, 0, slot_team_reinforcement_stage, 2),
				(neg|team_slot_eq, 0, slot_team_reinforcement_stage, "$attacker_reinforcement_stage"),
				#(lt, "$team0_reinforcement_stage", 2),
				#(neq, "$team0_reinforcement_stage", "$defender_reinforcement_stage"),
				(assign, ":cavalry_order", mordr_hold),
			(else_try),
				(neq, ":infantry_order", mordr_charge),
				(try_begin),
					(le, "$battle_phase", BP_Jockey),
					(assign, ":cavalry_order", mordr_hold),
				(else_try),
					(eq, ":nearest_target_distance", Far_Away),
					(try_begin),
						(eq, ":num_archers", 0),
						(assign, ":distance_to_archers", 0),
					(else_try),
						(get_distance_between_positions, ":distance_to_archers", Cavalry_Pos, Archers_Pos),
					(try_end),
					(try_begin),
						(this_or_next|gt, ":cav_closest_dist", AI_charge_distance),
						(gt, ":distance_to_archers", AI_charge_distance),
						(assign, ":cavalry_order", mordr_hold),
					(try_end),
				(try_end),
			(try_end),

			(try_begin),
				(eq, ":team_no", 0),
				(assign, ":cav_destination", Team0_Cavalry_Destination),
				#(assign, reg0, "$team0_percent_cavalry_are_archers"),
			(else_try),
				(eq, ":team_no", 1),
				(assign, ":cav_destination", Team1_Cavalry_Destination),
				#(assign, reg0, "$team1_percent_cavalry_are_archers"),
			(else_try),
				(eq, ":team_no", 2),
				(assign, ":cav_destination", Team2_Cavalry_Destination),
				#(assign, reg0, "$team2_percent_cavalry_are_archers"),
			(else_try),
				(eq, ":team_no", 3),
				(assign, ":cav_destination", Team3_Cavalry_Destination),
				#(assign, reg0, "$team3_percent_cavalry_are_archers"),
			(try_end),
			(team_get_slot, reg0, ":team_no", slot_team_percent_cavalry_are_archers),
			
			#horse archers don't use wedge
			(try_begin),
				(ge, reg0, 50),
				(call_script, "script_formation_end", ":team_no", grc_cavalry),
				(try_begin),
					(eq, ":num_archers", 0),
					(team_give_order, ":team_no", grc_cavalry, mordr_charge),
				(else_try),
					(team_give_order, ":team_no", grc_cavalry, ":cavalry_order"),
					(copy_position, ":cav_destination", Archers_Pos),
					(position_move_y, ":cav_destination", -500, 0),
					(team_set_order_position, ":team_no", grc_cavalry, ":cav_destination"),
				(try_end),
				
			#close in with no unguarded target farther off, free fight
			(else_try),
				(eq, ":cavalry_order", mordr_charge),
				(le, ":cav_closest_dist", AI_charge_distance),
				(try_begin),
					(eq, ":num_targets", 1),
					(eq, ":nearest_target_guarded", 0),
					(gt, ":nearest_target_distance", ":nearest_threat_distance"),
					(assign, reg0, 0),
				(else_try),
					(ge, ":num_targets", 2),
					(eq, ":nearest_target_guarded", 1),
					(assign, reg0, 0),
				(else_try),
					(assign, reg0, 1),
				(try_end),
				(eq, reg0, 1),
				(team_get_movement_order, reg0, ":team_no", grc_cavalry),
				(try_begin),
					(neq, reg0, mordr_charge),
					(call_script, "script_formation_end", ":team_no", grc_cavalry),
					(team_give_order, ":team_no", grc_cavalry, mordr_charge),
				(try_end),

			#grand charge if target closer than threat AND not guarded
			(else_try),
				(lt, ":nearest_target_distance", ":nearest_threat_distance"),
				(eq, ":nearest_target_guarded", 0),
				(call_script, "script_formation_end", ":team_no", grc_cavalry),
				(team_give_order, ":team_no", grc_cavalry, mordr_hold),
				
				#lead archers up to firing point
				(try_begin),
					(gt, ":nearest_target_distance", AI_firing_distance),
					(eq, ":cavalry_order", mordr_hold),
					(try_begin),
						(eq, ":num_archers", 0),
						(copy_position, ":cav_destination", Cavalry_Pos),	#must be reinforcements, so gather at average position
					(else_try),						
						(copy_position, ":cav_destination", Archers_Pos),
						(position_move_y, ":cav_destination", AI_charge_distance, 0),
					(try_end),
					
				#then CHARRRRGE!
				(else_try),
					(copy_position, ":cav_destination", Cavalry_Pos),
					(call_script, "script_point_y_toward_position", ":cav_destination", Nearest_Target_Pos),
					(position_move_y, ":cav_destination", ":nearest_target_distance", 0),
				(try_end),
				(team_set_order_position, ":team_no", grc_cavalry, ":cav_destination"),
				
			#make a wedge somewhere
			(else_try),
				(try_begin),
					(eq, ":cavalry_order", mordr_charge),
					(neq, ":nearest_target_distance", Far_Away),
					(copy_position, ":cav_destination", Cavalry_Pos),
					(call_script, "script_point_y_toward_position", ":cav_destination", Nearest_Target_Pos),
					(position_move_y, ":cav_destination", ":nearest_target_distance", 0),
					(position_move_y, ":cav_destination", AI_charge_distance, 0),	#charge on through to the other side
				(else_try),
					(neq, ":cavalry_order", mordr_charge),
					(eq, ":num_archers", 0),
					(copy_position, ":cav_destination", Cavalry_Pos),	#must be reinforcements, so gather at average position
				(else_try),
					(copy_position, ":cav_destination", Archers_Pos),	#hold near archers
					(position_move_x, ":cav_destination", 500, 0),
					(position_move_y, ":cav_destination", -1000, 0),
				(try_end),
				
				#move around threat in the way to destination
				(try_begin),
					(neq, ":nearest_threat_distance", Far_Away),
					(call_script, "script_point_y_toward_position", Cavalry_Pos, Nearest_Threat_Pos),
					(call_script, "script_point_y_toward_position", Nearest_Threat_Pos, ":cav_destination"),
					(position_get_rotation_around_z, reg0, Cavalry_Pos),
					(position_get_rotation_around_z, reg1, Nearest_Threat_Pos),
					(store_sub, ":rotation_diff", reg0, reg1),
					(try_begin),
						(lt, ":rotation_diff", -180),
						(val_add, ":rotation_diff", 360),
					(else_try),
						(gt, ":rotation_diff", 180),
						(val_sub, ":rotation_diff", 360),
					(try_end),
					
					(try_begin),
						(is_between, ":rotation_diff", -135, 136),
						(copy_position, ":cav_destination", Cavalry_Pos),
						(assign, ":distance_to_move", AI_firing_distance),
						(try_begin),	#target is left of threat
							(is_between, ":rotation_diff", -135, 0),
							(val_mul, ":distance_to_move", -1),
						(try_end),
						(position_move_x, ":cav_destination", ":distance_to_move", 0),
						(store_sub, ":distance_to_move", ":nearest_threat_distance", AI_firing_distance),
						(position_move_y, ":cav_destination", ":distance_to_move", 0),
						(call_script, "script_point_y_toward_position", ":cav_destination", Cavalry_Pos),
						(position_rotate_z, ":cav_destination", 180),
					(try_end),
				(try_end),
				(get_scene_boundaries, pos0, pos1),
				(position_get_x, reg0, ":cav_destination"),
				(position_get_x, reg1, pos0),
				(val_max, reg0, reg1),
				(position_get_x, reg1, pos1),
				(val_min, reg0, reg1),
				(position_set_x, ":cav_destination", reg0),
				(position_get_y, reg0, ":cav_destination"),
				(position_get_y, reg1, pos0),
				(val_max, reg0, reg1),
				(position_get_y, reg1, pos1),
				(val_min, reg0, reg1),
				(position_set_y, ":cav_destination", reg0),
	
				(position_set_z_to_ground_level, ":cav_destination"),
				(call_script, "script_set_formation_position", ":team_no", grc_cavalry, ":cav_destination"),
				(copy_position, pos1, ":cav_destination"),
				(assign, ":division", grc_cavalry), #TEMP
				(call_script, "script_form_cavalry", ":team_no", ":team_leader", ":division", 0),
				(try_begin),
					(ge, reg0, formation_min_cavalry_troops),
					(team_give_order, ":team_no", grc_cavalry, mordr_hold),
				(else_try),
					(call_script, "script_formation_end", ":team_no", grc_cavalry),
					(team_give_order, ":team_no", grc_cavalry, ":cavalry_order"),
					(team_set_order_position, ":team_no", grc_cavalry, ":cav_destination"),
				(try_end),
			(try_end),
		(try_end),

		#place leader
		(try_begin),
			(ge, ":team_leader", 0),
			(agent_is_alive, ":team_leader"),
			(try_begin),
				(le, ":num_infantry", 0),
				(try_begin),
					(eq, ":archer_order", mordr_charge),
					(agent_clear_scripted_mode, ":team_leader"),
				(else_try),
					(copy_position, pos1, Archers_Pos),
					(position_move_y, pos1, -1000, 0),
					(agent_set_scripted_destination, ":team_leader", pos1, 1),
				(try_end),
			(else_try),
				(neq, ":place_leader_by_infantry", 0),
				(agent_slot_eq, ":team_leader", slot_agent_is_running_away, 0),
				(position_move_x, pos61, 100, 0),
				(agent_set_scripted_destination, ":team_leader", pos61, 1),
			(else_try),
				(agent_clear_scripted_mode, ":team_leader"),
			(try_end),
		(try_end),
	(try_end)
	]),

	  
  # script_field_tactics by motomataru  #EDITED FOR SLOTS BY CABA
  # Input: flag 1 to include ranged
  # Output: none
  ("field_tactics", [
	(store_script_param, ":include_ranged", 1),
	
	#(assign, ":largest_team", -1),
	(assign, ":largest_team_size", 0),
	(assign, ":num_teams", 0),
	(assign, ":battle_size", 0),
	(try_for_range, ":team_no", 0, 4),
	    (team_get_slot, ":team_size", ":team_no", slot_team_size),
	    (team_get_slot, ":team_cav_size", ":team_no", slot_team_num_cavalry),
		(store_add, ":team_adj_size", ":team_size", ":team_cav_size"),
		(gt, ":team_adj_size", 0),
		(val_add, ":num_teams", 1),		
		(val_add, ":battle_size", ":team_adj_size"),
		
		(try_begin),
		    (neq, ":team_no", "$fplayer_team_no"),
			(neg|teams_are_enemies, ":team_no", "$fplayer_team_no"),
			(team_get_slot, ":player_team_adj_size", "$fplayer_team_no", slot_team_adj_size),
			(val_add, ":team_adj_size", ":player_team_adj_size"),	#ally team takes player team into account
		(try_end),
		(team_set_slot, ":team_no", slot_team_adj_size, ":team_adj_size"),
		
	    (lt, ":largest_team_size", ":team_adj_size"),
		(assign, ":largest_team_size", ":team_adj_size"),
		#(assign, ":largest_team", ":team_no"),		
	(try_end),
	
	#apply tactics to every AI team
	(try_for_range, ":ai_team", 0, ":num_teams"),
		(neq, ":ai_team", "$fplayer_team_no"),
		(team_get_slot, ":ai_team_size", ":ai_team", slot_team_adj_size),
		(team_get_slot, ":ai_faction", ":ai_team", slot_team_faction),

		(gt, ":ai_team_size", 0),
		(try_begin),
			(this_or_next|eq, AI_for_kingdoms_only, 0),
			(this_or_next|eq, ":ai_faction", fac_deserters),	#deserters have military training
			(is_between, ":ai_faction", fac_kingdom_1, fac_kingdoms_end),
			(val_mul, ":ai_team_size", 100),
			(store_div, ":team_percentage", ":ai_team_size", ":largest_team_size"),
			(store_div, ":team_battle_presence", ":ai_team_size", ":battle_size"),
			(try_begin),
				(eq, ":include_ranged", 1),
				(call_script, "script_team_field_ranged_tactics", ":ai_team", ":team_percentage", ":team_battle_presence"),
			(try_end),
			(call_script, "script_team_field_melee_tactics", ":ai_team", ":team_percentage", ":team_battle_presence"),
		(try_end),
	(try_end),

	(try_begin),
		(eq, ":include_ranged", 1), 	  
		(assign, "$prev_casualties", "$cur_casualties"),
	(try_end)
	]),

	
# # Utilities used by AI by motomataru 

  # script_find_high_ground_around_pos1_corrected by motomataru  #CABA - OK
  # Input:	arg1: destination position
  #			arg2: search_radius (in meters)
  #			pos1 should hold center_position_no
  # Output:	destination contains highest ground within a <search_radius> meter square around pos1
  # Also uses position registers: pos0
  ("find_high_ground_around_pos1_corrected", [
	(store_script_param, ":destination_pos", 1),
	(store_script_param, ":search_radius", 2),
	(assign, ":fixed_point_multiplier", 1),
	(convert_to_fixed_point, ":fixed_point_multiplier"),
	(set_fixed_point_multiplier, 1),
	
	(position_get_x, ":o_x", pos1),
	(position_get_y, ":o_y", pos1),
	(store_sub, ":min_x", ":o_x", ":search_radius"),
	(store_sub, ":min_y", ":o_y", ":search_radius"),
	(store_add, ":max_x", ":o_x", ":search_radius"),
	(store_add, ":max_y", ":o_y", ":search_radius"),
	
	(get_scene_boundaries, ":destination_pos", pos0),
	(position_get_x, ":scene_min_x", ":destination_pos"),
	(position_get_x, ":scene_max_x", pos0),
	(position_get_y, ":scene_min_y", ":destination_pos"),
	(position_get_y, ":scene_max_y", pos0),
	(val_max, ":min_x", ":scene_min_x"),
	(val_max, ":min_y", ":scene_min_y"),
	(val_min, ":max_x", ":scene_max_x"),
	(val_min, ":max_y", ":scene_max_y"),

	(assign, ":highest_pos_z", -100),
	(copy_position, ":destination_pos", pos1),
	(init_position, pos0),

	(try_for_range, ":i_x", ":min_x", ":max_x"),
		(try_for_range, ":i_y", ":min_y", ":max_y"),
			(position_set_x, pos0, ":i_x"),
			(position_set_y, pos0, ":i_y"),
			(position_set_z_to_ground_level, pos0),
			(position_get_z, ":cur_pos_z", pos0),
			(try_begin),
				(gt, ":cur_pos_z", ":highest_pos_z"),
				(copy_position, ":destination_pos", pos0),
				(assign, ":highest_pos_z", ":cur_pos_z"),
			(try_end),
		(try_end),
	(try_end),
	
	(set_fixed_point_multiplier, ":fixed_point_multiplier"),
  ]),
  
  
  # script_cf_count_casualties by motomataru  #CABA - OK
  # Input: none
  # Output: evalates T/F, reg0 num casualties
  ("cf_count_casualties", [
    (assign, ":num_casualties", 0),
	(try_for_agents,":cur_agent"),
	    (try_begin),
			(this_or_next|agent_is_wounded, ":cur_agent"),
			(this_or_next|agent_slot_eq, ":cur_agent", slot_agent_is_running_away, 1),
			(neg|agent_is_alive, ":cur_agent"),
			(val_add, ":num_casualties", 1),
		(try_end),
	(try_end),
	(assign, reg0, ":num_casualties"),
	(gt, ":num_casualties", 0)
	]),
	
	
  # script_battlegroup_get_position by motomataru #CABA - EDITED TO USE SLOTS, NOT STORED POS NUMBERS
  # Input: destination position, team, battle group (troop class)
  # Output:	battle group position
  #			average team position if "troop class" input NOT set to 0-8
  # NB: Assumes that battle groups beyond 2 are PLAYER team
  # Positions 24-45 reserved (!)  NOW none are reserved...all calculated with slots
  ("battlegroup_get_position", [
	(store_script_param, ":bgposition", 1),
	(store_script_param, ":bgteam", 2),
	(store_script_param, ":bgroup", 3),
	
	(assign, ":x", 0),
	(assign, ":y", 0),
	(init_position, ":bgposition"),
	(try_begin),
	    #(eq, ":bgroup", grc_everyone),
		(neg|is_between, ":bgroup", 0, 9),
		(team_slot_ge, ":bgteam", slot_team_size, 1),
		(team_get_slot, ":x", ":bgteam", slot_team_avg_x),
		(team_get_slot, ":y", ":bgteam", slot_team_avg_y),
		#(store_mul, ":team_shift", ":bgteam", 4),
		#(store_add, ":position_number", Team0_Average_Pos, ":team_shift"),
		# (store_add, ":position_number", Team0_Average_Pos, ":bgteam"),
		# (copy_position, ":bgposition", ":position_number"),	
	(else_try),
		#(neq, ":bgroup", grc_everyone),
		(is_between, ":bgroup", 0, 9),
		(store_add, ":slot", slot_team_d0_size, ":bgroup"),
		(team_slot_ge, ":bgteam", ":slot", 1),
		
		(store_add, ":slot", slot_team_d0_x, ":bgroup"),
		(team_get_slot, ":x", ":bgteam", ":slot"),
		
		(store_add, ":slot", slot_team_d0_y, ":bgroup"),
		(team_get_slot, ":y", ":bgteam", ":slot"),
	(try_end),
	(position_set_x, ":bgposition", ":x"),
	(position_set_y, ":bgposition", ":y"),
	(position_set_z_to_ground_level, ":bgposition"),
  ]),	

  
  # script_get_nearest_enemy_battlegroup_location by motomataru #EDITED FOR SLOTS BY CABA'DRIN
  # Input: destination position, fron team, from position
  # Output:	destination position, reg0 with distance
  # Run script_store_battlegroup_data before calling!
  ("get_nearest_enemy_battlegroup_location", [
	(store_script_param, ":bgposition", 1),
	(store_script_param, ":team_no", 2),
	(store_script_param, ":from_pos", 3),
	(assign, ":distance_to_nearest_enemy_battlegoup", Far_Away),
	(try_for_range, ":enemy_team_no", 0, 4),
		#(call_script, "script_battlegroup_get_size", ":enemy_team_no", grc_everyone),
		#(gt, reg0, 0),
		(team_slot_ge, ":enemy_team_no", slot_team_size, 1),
		(teams_are_enemies, ":enemy_team_no", ":team_no"),
		#(try_begin),
		#	(eq, ":enemy_team_no", "$fplayer_team_no"),
		#	(assign, ":num_groups", 9),
		#(else_try),
		#	(assign, ":num_groups", 3),
		#(try_end),
		(try_for_range, ":enemy_battle_group", 0, 9),
			#(call_script, "script_battlegroup_get_size", ":enemy_team_no", ":enemy_battle_group"),
			#(gt, reg0, 0),
			(store_add, ":slot", slot_team_d0_size, ":enemy_battle_group"),
			(team_slot_ge, ":enemy_team_no", ":slot", 1),
			(call_script, "script_battlegroup_get_position", pos0, ":enemy_team_no", ":enemy_battle_group"),
			(get_distance_between_positions, reg0, pos0, ":from_pos"),
			(try_begin),
				(gt, ":distance_to_nearest_enemy_battlegoup", reg0),
				(assign, ":distance_to_nearest_enemy_battlegoup", reg0),
				(copy_position, ":bgposition", pos0),
			(try_end),
		(try_end),
	(try_end),
	(assign, reg0, ":distance_to_nearest_enemy_battlegoup")
  ]),
]

# Native scripts to replace
formAI_replacement_scripts = [
# # Line added to clear scripted mode right before each (agent_start_running_away, ":cur_agent")
  # script_decide_run_away_or_not #CABA - OK
  # Input: none
  # Output: none
  ("decide_run_away_or_not",
    [
      (store_script_param, ":cur_agent", 1),
      (store_script_param, ":mission_time", 2),
      
      (assign, ":force_retreat", 0),
      (agent_get_team, ":agent_team", ":cur_agent"),
      (agent_get_division, ":agent_division", ":cur_agent"),
      (try_begin),
        (lt, ":agent_division", 9), #static classes
        (team_get_movement_order, ":agent_movement_order", ":agent_team", ":agent_division"),
        (eq, ":agent_movement_order", mordr_retreat),
        (assign, ":force_retreat", 1),
      (try_end),

      (agent_get_slot, ":is_cur_agent_running_away", ":cur_agent", slot_agent_is_running_away),
      (try_begin),
        (eq, ":is_cur_agent_running_away", 0),
        (try_begin),
          (eq, ":force_retreat", 1),
          (agent_clear_scripted_mode, ":cur_agent"),	#handle scripted mode troops - motomataru
          (agent_start_running_away, ":cur_agent"),
          (agent_set_slot, ":cur_agent",  slot_agent_is_running_away, 1),
        (else_try),
          (ge, ":mission_time", 45), #first 45 seconds anyone does not run away whatever happens.
          (agent_get_slot, ":agent_courage_score", ":cur_agent",  slot_agent_courage_score),
          (store_agent_hit_points, ":agent_hit_points", ":cur_agent"),
          (val_mul, ":agent_hit_points", 4),
          (try_begin),
            (agent_is_ally, ":cur_agent"),
            (val_sub, ":agent_hit_points", 100), #ally agents will be more tend to run away, to make game more funnier/harder
          (try_end),
          (val_mul, ":agent_hit_points", 10),
          (store_sub, ":start_running_away_courage_score_limit", 3500, ":agent_hit_points"), 
          (lt, ":agent_courage_score", ":start_running_away_courage_score_limit"), #if (courage score < 3500 - (agent hit points * 40)) and (agent is not running away) then start running away, average hit points : 50, average running away limit = 1500

          (agent_get_troop_id, ":troop_id", ":cur_agent"), #for now do not let heroes to run away from battle
          (neg|troop_is_hero, ":troop_id"),
                                
          (agent_clear_scripted_mode, ":cur_agent"),	#handle scripted mode troops - motomataru
          (agent_start_running_away, ":cur_agent"),
          (agent_set_slot, ":cur_agent",  slot_agent_is_running_away, 1),
        (try_end),
      (else_try),
        (neq, ":force_retreat", 1),
        (agent_get_slot, ":agent_courage_score", ":cur_agent",  slot_agent_courage_score),
        (store_agent_hit_points, ":agent_hit_points", ":cur_agent"),      
        (val_mul, ":agent_hit_points", 4),
        (try_begin),
          (agent_is_ally, ":cur_agent"),
          (val_sub, ":agent_hit_points", 100), #ally agents will be more tend to run away, to make game more funnier/harder
        (try_end),
        (val_mul, ":agent_hit_points", 10),
        (store_sub, ":stop_running_away_courage_score_limit", 3700, ":agent_hit_points"), 
        (ge, ":agent_courage_score", ":stop_running_away_courage_score_limit"), #if (courage score > 3700 - agent hit points) and (agent is running away) then stop running away, average hit points : 50, average running away limit = 1700
        (agent_stop_running_away, ":cur_agent"),
        (agent_set_slot, ":cur_agent",  slot_agent_is_running_away, 0),
      (try_end),      
  ]), #ozan
]

def modmerge(var_set):
	try:
		from modmerger_options import module_sys_info
		version = module_sys_info["version"]
	except:
		version = 1127 # version not specified.  assume latest warband at this time

	try:
		var_name_1 = "scripts"
		orig_scripts = var_set[var_name_1]
		
		modmerge_formAI_scripts(orig_scripts)
		
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)

from util_scripts import *

def modmerge_formAI_scripts(orig_scripts):
	add_scripts(orig_scripts, formAI_replacement_scripts, True)
	add_scripts(orig_scripts, formAI_scripts, True)