# Formations AI for Warband by Motomataru
# rel. 01/03/11

# This function attaches AI_triggers only to missions "lead_charge" and "quick_battle_battle"
# For other missions, add to end of triggers list like so: " ] + AI_triggers "

# Make sure to comment out competing AI triggers in the mission templates modified
# But NOT morale scripts
# For example, for Warband 1.131 "lead_charge"

      # #AI Triggers
      # (0, 0, ti_once, [
          # (store_mission_timer_a,":mission_time"),(ge,":mission_time",2),
          # ],
       # [(call_script, "script_select_battle_tactic"),
        # (call_script, "script_battle_tactic_init"),
        # #(call_script, "script_battle_calculate_initial_powers"), #deciding run away method changed and that line is erased
        # ]),
      
# DON'T comment out morale/courage scripts that are HERE...

      # (5, 0, 0, [
          # (store_mission_timer_a,":mission_time"),

          # (ge,":mission_time",3),
          
          # (call_script, "script_battle_tactic_apply"),
          # ], []), #applying battle tactic

from header_common import *
from header_operations import *
from module_constants import *
from header_mission_templates import *

#AI triggers v3 for WB by motomataru
AI_triggers = [  
	(ti_before_mission_start, 0, 0, [(party_slot_eq, "p_main_party", slot_party_pref_formations, 1)], [
		(assign, "$cur_casualties", 0),
		(assign, "$prev_casualties", 0),
		(assign, "$ranged_clock", 1),
		(assign, "$battle_phase", BP_Setup),
		(assign, "$clock_reset", 0),
		(try_for_range, ":team_no", 0, 4),
		    (team_set_slot, ":team_no", slot_team_default_formation, formation_default),
			#(team_set_slot, ":team_no", slot_team_reinforcement_stage, 0), #Not needed, team slots begin missions reset
		(try_end),
		# (assign, "$team0_default_formation", formation_default),
		# (assign, "$team1_default_formation", formation_default),
		# (assign, "$team2_default_formation", formation_default),
		# (assign, "$team3_default_formation", formation_default),
		(init_position, Team0_Cavalry_Destination),
		(init_position, Team1_Cavalry_Destination),
		(init_position, Team2_Cavalry_Destination),
		(init_position, Team3_Cavalry_Destination),
		# (assign, "$team0_reinforcement_stage", 0),
		# (assign, "$team1_reinforcement_stage", 0),
	]),

	(0, AI_Delay_For_Spawn, ti_once, [(party_slot_eq, "p_main_party", slot_party_pref_formations, 1)], [
		(try_for_agents, ":cur_agent"),
			(agent_set_slot, ":cur_agent",  slot_agent_is_running_away, 0),
		(try_end),
		(set_fixed_point_multiplier, 100),
		(call_script, "script_battlegroup_get_position", Team0_Starting_Point, 0, grc_everyone),
		(call_script, "script_battlegroup_get_position", Team1_Starting_Point, 1, grc_everyone),
		(call_script, "script_battlegroup_get_position", Team2_Starting_Point, 2, grc_everyone),
		(call_script, "script_battlegroup_get_position", Team3_Starting_Point, 3, grc_everyone),
		(call_script, "script_field_tactics", 1)
	]),

	(1, .5, 0, [(party_slot_eq, "p_main_party", slot_party_pref_formations, 1)], [	#delay to offset half a second from formations trigger
		(try_begin),
			(call_script, "script_cf_count_casualties"),
			(assign, "$cur_casualties", reg0),
			(assign, "$battle_phase", BP_Fight),
		(try_end),
		
		(set_fixed_point_multiplier, 100),
		(call_script, "script_store_battlegroup_data"),
		(try_begin),	#reassess ranged position when fighting starts
			(ge, "$battle_phase", BP_Fight),
			(eq, "$clock_reset", 0),
			(call_script, "script_field_tactics", 1),
			(assign, "$ranged_clock", 0),
			(assign, "$clock_reset", 1),
		(else_try),	#reassess ranged position every five seconds after setup
			(ge, "$battle_phase", BP_Jockey),
			(store_mod, reg0, "$ranged_clock", 5),		
			(eq, reg0, 0),
			(call_script, "script_field_tactics", 1),
			#(assign, "$team0_reinforcement_stage", "$defender_reinforcement_stage"),
			#(assign, "$team1_reinforcement_stage", "$attacker_reinforcement_stage"),
			(team_set_slot, 0, slot_team_reinforcement_stage, "$defender_reinforcement_stage"),
			(team_set_slot, 1, slot_team_reinforcement_stage, "$attacker_reinforcement_stage"),
		(else_try),
			(call_script, "script_field_tactics", 0),
		(try_end),

		(try_begin),
			(eq, "$battle_phase", BP_Setup),
			(assign, ":not_in_setup_position", 0),
			(try_for_range, ":bgteam", 0, 4),
				(neq, ":bgteam", "$fplayer_team_no"),
				(team_slot_ge, ":bgteam", slot_team_size, 1), #battlegroup_get_size phase out
				(call_script, "script_battlegroup_get_position", pos1, ":bgteam", grc_archers),
				(team_get_order_position, pos0, ":bgteam", grc_archers),
				(get_distance_between_positions, reg0, pos0, pos1),
				(gt, reg0, 500),
				(assign, ":not_in_setup_position", 1),
			(try_end),
			(eq, ":not_in_setup_position", 0),	#all AI reached setup position?
			(assign, "$battle_phase", BP_Jockey),
		(try_end),
		
		(val_add, "$ranged_clock", 1),
	]),
]

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

		modmerge_formAI_mission_templates(orig_mission_templates)

		# END do your own stuff
            
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)

def modmerge_formAI_mission_templates(orig_mission_templates):
	find_i = find_object( orig_mission_templates, "lead_charge" )
	orig_mission_templates[find_i][5].extend(AI_triggers)
	find_i = find_object( orig_mission_templates, "quick_battle_battle" )
	orig_mission_templates[find_i][5].extend(AI_triggers)
