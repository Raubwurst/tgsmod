# Formations for Warband by Motomataru
# rel. 01/03/11
# EDIT FOR ORDER DISPLAY 11/19/10 by Caba'drin


from header_common import *
from header_operations import *
from module_constants import *
from header_mission_templates import *

# Formations triggers v3 by motomataru, Warband port
# Global variables	*_formation_type holds type of formation: see "Formation modes" in module_constants
#					*_formation_move_order hold the current move order for the formation
#					*_space hold the multiplier of extra space ordered into formation by the player

formations_triggers = [
	(ti_before_mission_start, 0, 0, [], [   #CABA - EDITED TYPE AND SPACE SETTINGS TO SLOTS
		(party_set_slot, "p_main_party", slot_party_gk_order, 0),
		(party_set_slot, 2, slot_party_gk_order_hold_over_there, 0),
		#(assign, "$native_display", 0),
		(assign, "$autorotate_at_player", formation_autorotate_at_player),
		(assign, "$fclock", 1),
		
		# (try_for_range, ":team", 0, 4),
		    # (try_for_range, ":division", 0, 9),
                # (try_begin),
                    # (eq, ":division", grc_cavalry),			
				    # (store_add, ":slot", slot_team_d0_formation, ":division"), 
		            # #(team_set_slot, ":team", ":slot", formation_wedge),
					# (team_set_slot, ":team", ":slot", formation_none),
					# (store_add, ":slot", slot_team_d0_formation_space, ":division"),
					# (team_set_slot, ":team", ":slot", 0),	
		        # (else_try),					
					# (store_add, ":slot", slot_team_d0_formation, ":division"), 
				    # #(team_set_slot, ":team", ":slot", formation_default),
					# (team_set_slot, ":team", ":slot", formation_none),
					# (store_add, ":slot", slot_team_d0_formation_space, ":division"),
					# (team_set_slot, ":team", ":slot", formation_start_spread_out),
		        # (try_end),
		    # (try_end),
		# (try_end),
		#(assign, "$infantry_formation_type", formation_default),	#type set by first call; depends on faction
		#(assign, "$archer_formation_type", formation_default),
		#(assign, "$cavalry_formation_type", formation_wedge),
		#(assign, "$infantry_space", formation_start_spread_out),	#give a little extra space for ease of forming up
		#(assign, "$archer_space", formation_start_spread_out),
		#(assign, "$cavalry_space", 0),

				
		#ensure item slots are loaded whatever save game this is...
		#(neq, "$new_session", 1),
		# # Autoloot improved by rubik begin
		#(call_script, "script_init_item_score"),
		# # Autoloot improved by rubik end
		#(assign, "$new_session", 1),	
	]),

# Start troops in formation
	(0, formation_delay_for_spawn, ti_once, [], [
		(get_player_agent_no, "$fplayer_agent_no"),
		(agent_get_team, "$fplayer_team_no", "$fplayer_agent_no"),
		(call_script, "script_store_battlegroup_data"), #CABA - SCRIPT OK
		
		#get team fixed data
		(try_for_agents, ":cur_agent"),
			(agent_is_human, ":cur_agent"),
			(agent_get_team, ":cur_team", ":cur_agent"),
			(agent_get_troop_id, ":cur_troop", ":cur_agent"),
			(store_troop_faction, ":cur_faction", ":cur_troop"),
			
			(team_get_slot, ":team_avg_faction", ":cur_team", slot_team_faction),
			(val_add, ":team_avg_faction", ":cur_faction"),
			(team_set_slot, ":cur_team", slot_team_faction, ":team_avg_faction"),
		(try_end),
		
		(try_for_range, ":team", 0, 4),
		    (team_slot_ge, ":team", slot_team_size, 1),
			(team_get_leader, ":fleader", ":team"),
			(try_begin),
				(ge, ":fleader", 0),
				(agent_get_troop_id, ":fleader_troop", ":fleader"),
				(store_troop_faction, ":team_faction", ":fleader_troop"),
			(else_try),
			    (team_get_slot, ":team_size", ":team", slot_team_size),
				(team_get_slot, ":team_avg_faction", ":team", slot_team_faction),
				(store_mul, ":team_faction", ":team_avg_faction", 10),
				(val_div, ":team_faction", ":team_size"),
				(val_add, ":team_faction", 5),
				(val_div, ":team_faction", 10),
			(try_end),		
			(team_set_slot, ":team", slot_team_faction, ":team_faction"),
		(try_end),
		
	    #CABA - EDIT FROM HERE ON ONCE EVERYTHING IS COMPLETE. WOULD NEED TO DO MORE DIVISIONS HERE...OR REMOVE DEFAULT FORMATIONS
	]),


	(0, .3, 0, [(game_key_clicked, gk_order_1)], [
		(party_slot_eq, "p_main_party", slot_party_gk_order, gk_order_1),	#next trigger set MOVE menu?
		(game_key_is_down, gk_order_1),	#BUT player is holding down key?
		(party_set_slot, 2, slot_party_gk_order_hold_over_there, 1),
		(party_set_slot, "p_main_party", slot_party_gk_order, 0),
	]),
	
#implement HOLD OVER THERE when player lets go of key  #MODIFIED FOR SLOTS AND MORE DIVISIONS BY CABA'DRIN
	(.5, 0, 0, [(party_slot_eq, 2, slot_party_gk_order_hold_over_there, 1),(neg|game_key_is_down, gk_order_1)], [
		(assign, "$fclock", 1),
		(call_script, "script_team_get_position_of_enemies", pos60, "$fplayer_team_no", grc_everyone),
		(assign, ":num_bgroups", 0),
		(try_for_range, ":battle_group", 0, 9),
			(class_is_listening_order, "$fplayer_team_no", ":battle_group"),
			(store_add, ":slot", slot_team_d0_size, ":battle_group"),
			(team_slot_ge, "$fplayer_team_no", ":slot", 1),
			(val_add, ":num_bgroups", 1),
		(try_end),	
		
		(agent_get_position, pos49, "$fplayer_agent_no"),
		
        (try_for_range, ":battle_group", 0, 9),
		    (class_is_listening_order, "$fplayer_team_no", ":battle_group"),
			(store_add, ":slot", slot_team_d0_size, ":battle_group"),
			(team_slot_ge, "$fplayer_team_no", ":slot", 1),
			(store_add, ":slot", slot_team_d0_formation, ":battle_group"),
			(neg|team_slot_eq, "$fplayer_team_no", ":slot", formation_none),
			
			(team_get_slot, ":fformation", "$fplayer_team_no", ":slot"),
			(store_add, ":slot", slot_team_d0_formation_space, ":battle_group"),
		    (team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			
			(team_get_order_position, pos2, "$fplayer_team_no", ":battle_group"),
			(call_script, "script_point_y_toward_position", pos2, pos60),
			(try_begin),
				(gt, ":num_bgroups", 1),
				(agent_set_position, "$fplayer_agent_no", pos2),	#fake out script_cf_formation
				(try_begin),	#ignore script failure
					(call_script, "script_cf_formation", "$fplayer_team_no", ":battle_group", ":div_spacing", ":fformation"),
				(try_end),
			(else_try),
				(call_script, "script_set_formation_position", "$fplayer_team_no", ":battle_group", pos2),
				(try_begin),
					(store_add, ":slot", slot_team_d0_type, ":battle_group"),
					(team_get_slot, ":sd_type", "$fplayer_team_no", ":slot"),
					(neq, ":sd_type", sdt_cavalry),
					(neq, ":sd_type", sdt_harcher),
				    (store_add, ":slot", slot_team_d0_size, ":battle_group"),
				    (team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
				    (call_script, "script_get_centering_amount", ":fformation", ":troop_count", ":div_spacing"),
					(try_begin),
						(this_or_next|eq, ":sd_type", sdt_archer),
						(eq, ":sd_type", sdt_skirmisher),
						(val_mul, reg0, -1),
						(assign, ":script", "script_form_archers"),
					(else_try),
					    (assign, ":script", "script_form_infantry"),
					(try_end),
				    (position_move_x, pos2, reg0),
				(else_try),
				    (assign, ":script", "script_form_cavalry"),
				(try_end),
				(copy_position, pos1, pos2),
				(call_script, ":script", "$fplayer_team_no", "$fplayer_agent_no", ":battle_group", ":div_spacing", ":fformation"),		
			(try_end),
			(store_add, ":slot", slot_team_d0_move_order, ":battle_group"),
			(team_set_slot, "$fplayer_team_no", ":slot", mordr_hold),		
		(try_end), #Battle Group Loop #2
		(agent_set_position, "$fplayer_agent_no", pos49),
		(party_set_slot, 2, slot_party_gk_order_hold_over_there, 0)
	]),

	(1, 0, 0, [	#attempt to avoid simultaneous formations function calls #MODIFIED FOR SLOTS AND MANY DIVISIONS BY CABA
		#(neg|key_is_down, key_for_ranks),
		#(neg|key_is_down, key_for_shield),
		#(neg|key_is_down, key_for_wedge),
		#(neg|key_is_down, key_for_square),
		#(neg|key_is_down, key_for_undo),
		(neg|key_is_down, key_f7), #ADDED
		(neg|key_is_down, key_f8), #ADDED
		(neg|game_key_is_down, gk_order_1),
		(neg|game_key_is_down, gk_order_2),
		(neg|game_key_is_down, gk_order_3),
		(neg|game_key_is_down, gk_order_4),
		(neg|game_key_is_down, gk_order_5),
		(neg|game_key_is_down, gk_order_6)
	  ], [
		(set_fixed_point_multiplier, 100),
		(store_mod, ":fifth_second", "$fclock", 5),
		(call_script, "script_team_get_position_of_enemies", pos60, "$fplayer_team_no", grc_everyone),
		(try_begin),
			(eq, reg0, 0),	#no more enemies?
			(call_script, "script_formation_end", "$fplayer_team_no", grc_everyone),
		(else_try),
			(assign, "$autorotate_at_player", 0),
			(try_for_range, ":division", 0, 9),
			    (store_add, ":slot", slot_team_d0_size, ":division"),
				(team_slot_ge, "$fplayer_team_no", ":slot", 1),
				(store_add, ":slot", slot_team_d0_formation, ":division"),
				(neg|team_slot_eq, "$fplayer_team_no", ":slot", formation_none),
				
				(team_get_slot, ":fformation", "$fplayer_team_no", ":slot"),
				(store_add, ":slot", slot_team_d0_formation_space, ":division"),
		        (team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
				(try_begin),
				    (store_add, ":slot", slot_team_d0_move_order, ":division"),
				    (team_slot_eq, "$fplayer_team_no", ":slot", mordr_follow),
			        (call_script, "script_cf_formation", "$fplayer_team_no", ":division", ":div_spacing", ":fformation"),
				(else_try),	   #periodically reform
					(eq, ":fifth_second", 0),
					(team_get_movement_order, reg0, "$fplayer_team_no", ":division"),
					(neq, reg0, mordr_stand_ground),
					
					(call_script, "script_get_formation_position", pos1, "$fplayer_team_no", ":division"),
					(try_begin),
					    (store_add, ":slot", slot_team_d0_type, ":division"),
						(team_get_slot, ":sd_type", "$fplayer_team_no", ":slot"),
						(neq, ":sd_type", sdt_cavalry),
						(neq, ":sd_type", sdt_harcher),
					    (position_move_y, pos1, -2000),
					(try_end),
					(call_script, "script_point_y_toward_position", pos1, pos60),
					(try_begin),
						(neq, ":sd_type", sdt_cavalry),
						(neq, ":sd_type", sdt_harcher),
					    (position_move_y, pos1, 2000),
					(try_end),
					(call_script, "script_set_formation_position", "$fplayer_team_no", ":division", pos1),	
                    (try_begin),	
                        (neq, ":sd_type", sdt_cavalry),
						(neq, ":sd_type", sdt_harcher),					
					    (store_add, ":slot", slot_team_d0_size, ":division"),
					    (team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
					    (call_script, "script_get_centering_amount", ":fformation", ":troop_count", ":div_spacing"),
						(try_begin),
						    (this_or_next|eq, ":sd_type", sdt_archer),
							(eq, ":sd_type", sdt_skirmisher),
						    (val_mul, reg0, -1),
						(try_end),
					    (position_move_x, pos1, reg0),	
                    (try_end),
					(try_begin),
					    (this_or_next|eq, ":sd_type", sdt_cavalry),
						(eq, ":sd_type", sdt_harcher),	
						(call_script, "script_form_cavalry", "$fplayer_team_no", "$fplayer_agent_no", ":division", ":div_spacing"),
					(else_try),
					    (this_or_next|eq, ":sd_type", sdt_archer),
						(eq, ":sd_type", sdt_skirmisher),
					    (call_script, "script_form_archers", "$fplayer_team_no", "$fplayer_agent_no", ":division", ":div_spacing", ":fformation"),		
					(else_try),				
					    (call_script, "script_form_infantry", "$fplayer_team_no", "$fplayer_agent_no", ":division", ":div_spacing", ":fformation"),	
					(try_end),
			    (try_end),
			(try_end), #Division Loop
			(assign, "$autorotate_at_player", formation_autorotate_at_player),
		(try_end),
		(val_add, "$fclock", 1),
	]),
]
#end formations triggers

def modmerge(var_set):
	try:
		from modmerger_options import module_sys_info
		version = module_sys_info["version"]
	except:
		version = 1127 # version not specified.  assume latest warband at this time

	try:
		var_name_1 = "mission_templates"
		orig_mission_templates = var_set[var_name_1]

		# START do your own stuff to do merging

		modmerge_formations_mission_templates(orig_mission_templates)

		# END do your own stuff
            
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)


def modmerge_formations_mission_templates(orig_mission_templates):
	# brute force add formation triggers to all mission templates with mtf_battle_mode
	#for i in range (0,len(orig_mission_templates)):
	#	if( orig_mission_templates[i][1] & mtf_battle_mode ):
	#		orig_mission_templates[i][5].extend(formations_triggers)
	find_i = find_object( orig_mission_templates, "lead_charge" )
	orig_mission_templates[find_i][5].extend(formations_triggers)
	find_i = find_object( orig_mission_templates, "quick_battle_battle" )
	orig_mission_templates[find_i][5].extend(formations_triggers)