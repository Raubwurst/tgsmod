from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *

from module_constants import *

####################################################################################################################
#  Each trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Delay interval: Time to wait before applying the consequences of the trigger
#    After its conditions have been evaluated as true.
# 3) Re-arm interval. How much time must pass after applying the consequences of the trigger for the trigger to become active again.
#    You can put the constant ti_once here to make sure that the trigger never becomes active again after it fires once.
# 4) Conditions block (list). This must be a valid operation block. See header_operations.py for reference.
#    Every time the trigger is checked, the conditions block will be executed.
#    If the conditions block returns true, the consequences block will be executed.
#    If the conditions block is empty, it is assumed that it always evaluates to true.
# 5) Consequences block (list). This must be a valid operation block. See header_operations.py for reference. 
####################################################################################################################

# Some constants for use below
merchant_inventory_space = 30
num_merchandise_goods = 36



triggers = [
# Tutorial:  #modified for TGS
  (0.1, 0, ti_once, [(map_free,0)], [
                                      (dialog_box,"str_tutorial_map1"),
                                      (assign,"$g_tutorial_complete",1),
                                      ]),

#  (1.0, 0, ti_once, [(map_free,0)], [(start_map_conversation, "trp_guide", -1)]),

# Refresh Merchants
  (0.0, 0, 24.0, [],
  [    
    (call_script, "script_refresh_center_inventories"),
  ]),

# Refresh Armor sellers
  (0.0, 0, 24.0, [],
  [    
    (call_script, "script_refresh_center_armories"),
  ]),

# Refresh Weapon sellers
  (0.0, 0, 24.0, [],
  [
    (call_script, "script_refresh_center_weaponsmiths"),
  ]),

# Refresh Horse sellers
  (0.0, 0, 24.0, [],
  [
    (call_script, "script_refresh_center_stables"),
  ]),
  

#############

#Captivity:

#  (1.0, 0, 0.0, [],
#   [
#       (ge,"$captivity_mode",1),
#       (store_current_hours,reg(1)),
#       (val_sub,reg(1),"$captivity_end_time"),
#       (ge,reg(1),0),
#       (display_message,"str_nobleman_reached_destination"),
#       (jump_to_menu,"$captivity_end_menu"),
#    ]),


  (5.7, 0, 0.0, 
  [
    (store_num_parties_of_template, reg2, "pt_manhunters"),    
    (lt, reg2, 4)
  ],
  [
    (set_spawn_radius, 1),
    (store_add, ":p_town_22_plus_one", "p_town_22", 1),
    (store_random_in_range, ":selected_town", "p_town_1", ":p_town_22_plus_one"),
    (spawn_around_party, ":selected_town", "pt_manhunters"),
  ]),



  (1.0, 0.0, 0.0, [
  (check_quest_active, "qst_track_down_bandits"),
  (neg|check_quest_failed, "qst_track_down_bandits"),
  (neg|check_quest_succeeded, "qst_track_down_bandits"),
  
  ],
   [
    (quest_get_slot, ":bandit_party", "qst_track_down_bandits", slot_quest_target_party),
	(try_begin),
		(party_is_active, ":bandit_party"),
		(store_faction_of_party, ":bandit_party_faction", ":bandit_party"),
		(neg|is_between, ":bandit_party_faction", kingdoms_begin, kingdoms_end), #ie, the party has not respawned as a non-bandit
		
		
		(assign, ":spot_range", 8),
		(try_begin),
			(is_currently_night),
			(assign, ":spot_range", 5),
		(try_end),
		
		(try_for_parties, ":party"),
			(gt, ":party", "p_spawn_points_end"),
			
			(store_faction_of_party, ":faction", ":party"),
			(is_between, ":faction", kingdoms_begin, kingdoms_end),
			
			
			(store_distance_to_party_from_party, ":distance", ":party", ":bandit_party"),
			(lt, ":distance", ":spot_range"),
			(try_begin),
				(eq, "$cheat_mode", 1),
				(str_store_party_name, s4, ":party"),
				(display_message, "@{!}DEBUG -- Wanted bandits spotted by {s4}"),
			(try_end),
			
			(call_script, "script_get_closest_center", ":bandit_party"),
			(assign, ":nearest_center", reg0),
#			(try_begin),
#				(get_party_ai_current_behavior, ":behavior", ":party"),
#				(eq, ":behavior", ai_bhvr_attack_party),
#				(call_script, "script_add_log_entry",  logent_party_chases_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
#			(else_try),
#				(eq, ":behavior", ai_bhvr_avoid_party),
#				(call_script, "script_add_log_entry",  logent_party_runs_from_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
#			(else_try),
			(call_script, "script_add_log_entry",  logent_party_spots_wanted_bandits, ":party",  ":nearest_center", ":bandit_party", -1),
#			(try_end),
		(try_end),
	(else_try), #Party not found
		(display_message, "str_bandits_eliminated_by_another"),
        (call_script, "script_abort_quest", "qst_track_down_bandits", 0),
	(try_end),
   ]),


#Tax Collectors
# Prisoner Trains
#  (4.1, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_prisoner_train"),
#                         (assign, "$pin_limit", peak_prisoner_trains),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#                         (party_set_ai_object,"$pout_party","$pout_town"),
#                    ]),
#
#  (4.1, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_prisoner_train"),
#                         (assign, "$pin_limit", peak_prisoner_trains),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#                         (party_set_ai_object,"$pout_party","$pout_town"),
#                    ]),

  (2.0, 0, 0, [(store_random_party_of_template, reg(2), "pt_prisoner_train_party"),
               (party_is_in_any_town,reg(2)),
               ],
              [(store_faction_of_party, ":faction_no", reg(2)),
               (call_script,"script_cf_select_random_walled_center_with_faction", ":faction_no", -1),
               (party_set_ai_behavior,reg(2),ai_bhvr_travel_to_party),
               (party_set_ai_object,reg(2),reg0),
               (party_set_flags, reg(2), pf_default_behavior, 0),
            ]),

##Caravans
#  (4.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_caravan"),
#                         (assign, "$pin_limit", peak_kingdom_caravans),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#                         (party_set_ai_object,"$pout_party","$pout_town"),
#                    ]),

#  (4.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_caravan"),
#                         (assign, "$pin_limit", peak_kingdom_caravans),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                         (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#                         (party_set_ai_object,"$pout_party","$pout_town"),
#                    ]),

##  (2.0, 0, 0, [(store_random_party_of_template, reg(2), "pt_kingdom_caravan_party"),
##               (party_is_in_any_town,reg(2)),
##               ],
##              [(store_faction_of_party, ":faction_no", reg(2)),
##               (call_script,"script_cf_select_random_town_with_faction", ":faction_no"),
##               (party_set_ai_behavior,reg(2),ai_bhvr_travel_to_party),
##               (party_set_ai_object,reg(2),reg0),
##               (party_set_flags, reg(2), pf_default_behavior, 0),
##            ]),
  
  (4.0, 0, 0.0,
   [
     (eq, "$caravan_escort_state", 1), #cancel caravan_escort_state if caravan leaves the destination
     (assign, ":continue", 0),
     (try_begin),
       (neg|party_is_active, "$caravan_escort_party_id"),
       (assign, ":continue", 1),
     (else_try),
       (get_party_ai_object, ":ai_object", "$caravan_escort_party_id"),
       (neq, ":ai_object", "$caravan_escort_destination_town"),
       (assign, ":continue", 1),
     (try_end),
     (eq, ":continue", 1),
     ],
   [
     (assign, "$caravan_escort_state", 0),
     ]),

#Messengers
#  (4.2, 0, 0.0, [],
#   [(assign, "$pin_faction", "fac_swadians"),
#    (assign, "$pin_party_template", "pt_swadian_messenger"),
#    (assign, "$pin_limit", peak_kingdom_messengers),
#    (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#    (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#    (party_set_ai_object,"$pout_party","$pout_town"),
#    ]),

#  (4.2, 0, 0.0, [],
#   [(assign, "$pin_faction", "fac_vaegirs"),
#    (assign, "$pin_party_template", "pt_vaegir_messenger"),
#    (assign, "$pin_limit", peak_kingdom_caravans),
#    (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#    (party_set_ai_behavior,"$pout_party",ai_bhvr_travel_to_party),
#    (party_set_ai_object,"$pout_party","$pout_town"),
#    ]),

  (1.5, 0, 0, [(store_random_party_of_template, reg(2), "pt_messenger_party"),
               (party_is_in_any_town,reg(2)),
               ],
   [(store_faction_of_party, ":faction_no", reg(2)),
    (call_script,"script_cf_select_random_walled_center_with_faction", ":faction_no", -1),
    (party_set_ai_behavior,reg(2),ai_bhvr_travel_to_party),
    (party_set_ai_object,reg(2),reg0),
    (party_set_flags, reg(2), pf_default_behavior, 0),
    ]),
  
  

#Deserters

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_deserters"),
#                         (assign, "$pin_limit", 4),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),
  
#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_deserters"),
#                         (assign, "$pin_limit", 4),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#Kingdom Parties
  (1.0, 0, 0.0, [],
   [(try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
      (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),
##      (neq, ":cur_kingdom", "fac_player_supporters_faction"),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_forager),
##      (try_end),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_scout),
##      (try_end),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_patrol),
##      (try_end),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_messenger),
##      (try_end),
      (try_begin),
        (store_random_in_range, ":random_no", 0, 100),
        (lt, ":random_no", 10),
        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_kingdom_caravan),
      (try_end),
##      (try_begin),
##        (store_random_in_range, ":random_no", 0, 100),
##        (lt, ":random_no", 10),
##        (call_script, "script_create_kingdom_party_if_below_limit", ":cur_kingdom", spt_prisoner_train),
##      (try_end),
    (try_end),
    ]),


#Swadians
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_swadian_foragers",4)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_swadian_scouts",4)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_swadian_harassers",3)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_swadian_war_parties",2)]),


#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_foragers"),
#                         (assign, "$pin_limit", "$peak_swadian_foragers"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_scouts"),
#                         (assign, "$pin_limit", "$peak_swadian_scouts"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_patrol"),
#                         (assign, "$pin_limit", "$peak_swadian_harassers"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_swadians"),
#                         (assign, "$pin_party_template", "pt_swadian_war_party"),
#                         (assign, "$pin_limit", "$peak_swadian_war_parties"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),
#Vaegirs
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_vaegir_foragers",4)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_vaegir_scouts",4)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_vaegir_harassers",3)]),
#  (0.0, 0.0, ti_once, [], [(assign,"$peak_vaegir_war_parties",2)]),
  

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_foragers"),
#                         (assign, "$pin_limit", "$peak_vaegir_foragers"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_scouts"),
#                         (assign, "$pin_limit", "$peak_vaegir_scouts"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_patrol"),
#                         (assign, "$pin_limit", "$peak_vaegir_harassers"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#  (10.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_vaegirs"),
#                         (assign, "$pin_party_template", "pt_vaegir_war_party"),
#                         (assign, "$pin_limit", "$peak_vaegir_war_parties"),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),

#Villains etc.
#  (14.2, 0, 0.0, [],
#                     [
#                         (assign, "$pin_faction", "fac_sea_raiders"),
#                         (assign, "$pin_party_template", "pt_sea_raiders"),
#                         (assign, "$pin_limit", 5),
#                         (call_script,"script_cf_spawn_party_at_faction_town_if_below_limit"),
#                    ]),


#
##  (10.1, 0, 0.0, [],
##                     [
##                         (assign, "$pin_party_template", "pt_refugees"),
##                         (assign, "$pin_limit", 5),
##                         (call_script,"script_cf_spawn_party_at_random_town_if_below_limit"),
##                    ]),
##
##  (10.1, 0, 0.0, [],
##                     [
##                         (assign, "$pin_party_template", "pt_farmers"),
##                         (assign, "$pin_limit", 6),
##                         (call_script,"script_cf_spawn_party_at_random_town_if_below_limit"),
##                    ]),

#  [1.0, 96.0, ti_once, [], [[assign,"$peak_dark_hunters",3]]],
  
##  (10.1, 0, 0.0, [],
##                     [
##                         (assign, "$pin_party_template", "pt_dark_hunters"),
##                         (assign, "$pin_limit", "$peak_dark_hunters"),
##                         (call_script,"script_cf_spawn_party_at_random_town_if_below_limit"),
##                    ]),

#Companion quests

##  (0, 0, ti_once,
##   [
##       (entering_town,"p_town_1"),
##       (main_party_has_troop,"trp_borcha"),
##       (eq,"$borcha_freed",0)
##    ],
##   
##   [
##       (assign,"$borcha_arrive_sargoth_as_prisoner", 1),
##       (start_map_conversation, "trp_borcha", -1)
##    ]
##   ),
##
##  (1, 0, ti_once,
##   [
##      (map_free,0),
##      (eq,"$borcha_asked_for_freedom",0),
##      (main_party_has_troop,"trp_borcha")
##    ],
##   [
##       (start_map_conversation, "trp_borcha", -1)
##    ]
##   ),
##  
##  (2, 0, ti_once,
##   [
##      (map_free, 0),
##      (neq,"$borcha_asked_for_freedom",0),
##      (eq,"$borcha_freed",0),
##      (main_party_has_troop,"trp_borcha")
##    ],
##   [
##       (start_map_conversation, "trp_borcha", -1),
##    ]
##   ),

##### TODO: QUESTS COMMENT OUT BEGIN

###########################################################################
### Random Governer Quest triggers
###########################################################################

# Incriminate Loyal Advisor quest
  (0.2, 0.0, 0.0,
   [
       (check_quest_active, "qst_incriminate_loyal_commander"),
       (neg|check_quest_concluded, "qst_incriminate_loyal_commander"),
       (quest_slot_eq, "qst_incriminate_loyal_commander", slot_quest_current_state, 2),
       (quest_get_slot, ":quest_target_center", "qst_incriminate_loyal_commander", slot_quest_target_center),
       (quest_get_slot, ":quest_target_party", "qst_incriminate_loyal_commander", slot_quest_target_party),
       (try_begin),
         (neg|party_is_active, ":quest_target_party"),
         (quest_set_slot, "qst_incriminate_loyal_commander", slot_quest_current_state, 3),
         (call_script, "script_fail_quest", "qst_incriminate_loyal_commander"),
       (else_try),
         (party_is_in_town, ":quest_target_party", ":quest_target_center"),
         (remove_party, ":quest_target_party"),
         (quest_set_slot, "qst_incriminate_loyal_commander", slot_quest_current_state, 3),
         (quest_get_slot, ":quest_object_troop", "qst_incriminate_loyal_commander", slot_quest_object_troop),
         (assign, ":num_available_factions", 0),
         (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
           (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
           (neq, ":faction_no", "fac_player_supporters_faction"),
           (neg|quest_slot_eq, "qst_incriminate_loyal_commander", slot_quest_target_faction, ":faction_no"),
           (val_add, ":num_available_factions", 1),
         (try_end),
         (try_begin),
           (gt, ":num_available_factions", 0),
           (store_random_in_range, ":random_faction", 0, ":num_available_factions"),
           (assign, ":target_faction", -1),
           (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
             (eq, ":target_faction", -1),
             (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
             (neq, ":faction_no", "fac_player_supporters_faction"),
             (neg|quest_slot_eq, "qst_incriminate_loyal_commander", slot_quest_target_faction, ":faction_no"),
             (val_sub, ":random_faction", 1),
             (lt, ":random_faction", 0),
             (assign, ":target_faction", ":faction_no"),
           (try_end),
         (try_end),
         (try_begin),
           (gt, ":target_faction", 0),
           (call_script, "script_change_troop_faction", ":quest_object_troop", ":target_faction"),
         (else_try),
           (call_script, "script_change_troop_faction", ":quest_object_troop", "fac_robber_knights"),
         (try_end),
         (call_script, "script_succeed_quest", "qst_incriminate_loyal_commander"),
       (try_end),
    ],
   []
   ),
# Runaway Peasants quest
  (0.2, 0.0, 0.0,
   [
       (check_quest_active, "qst_bring_back_runaway_serfs"),
       (neg|check_quest_concluded, "qst_bring_back_runaway_serfs"),
       (quest_get_slot, ":quest_object_center", "qst_bring_back_runaway_serfs", slot_quest_object_center),
       (quest_get_slot, ":quest_target_center", "qst_bring_back_runaway_serfs", slot_quest_target_center),
       (try_begin),
         (party_is_active, "$qst_bring_back_runaway_serfs_party_1"),
         (try_begin),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_1", ":quest_target_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_1"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
         (else_try),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_1", ":quest_object_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_1"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_1"),
           (gt, ":cur_distance", 3),
           (party_set_ai_object, "$qst_bring_back_runaway_serfs_party_1", ":quest_target_center"),
         (try_end),
       (try_end),
       (try_begin),
         (party_is_active, "$qst_bring_back_runaway_serfs_party_2"),
         (try_begin),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_2", ":quest_target_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_2"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
         (else_try),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_2", ":quest_object_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_2"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_2"),
           (gt, ":cur_distance", 3),
           (party_set_ai_object, "$qst_bring_back_runaway_serfs_party_2", ":quest_target_center"),
         (try_end),
       (try_end),
       (try_begin),
         (party_is_active, "$qst_bring_back_runaway_serfs_party_3"),
         (try_begin),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_3", ":quest_target_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_3"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_fleed", 1),
         (else_try),
           (party_is_in_town, "$qst_bring_back_runaway_serfs_party_3", ":quest_object_center"),
           (remove_party, "$qst_bring_back_runaway_serfs_party_3"),
           (val_add, "$qst_bring_back_runaway_serfs_num_parties_returned", 1),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_bring_back_runaway_serfs_party_3"),
           (gt, ":cur_distance", 3),
           (party_set_ai_object, "$qst_bring_back_runaway_serfs_party_3", ":quest_target_center"),
         (try_end),
       (try_end),
       (assign, ":sum_removed", "$qst_bring_back_runaway_serfs_num_parties_returned"),
       (val_add, ":sum_removed", "$qst_bring_back_runaway_serfs_num_parties_fleed"),
       (ge, ":sum_removed", 3),
       (try_begin),
         (ge, "$qst_bring_back_runaway_serfs_num_parties_returned", 3),
         (call_script, "script_succeed_quest", "qst_bring_back_runaway_serfs"),
       (else_try),
         (eq, "$qst_bring_back_runaway_serfs_num_parties_returned", 0),
         (call_script, "script_fail_quest", "qst_bring_back_runaway_serfs"),
       (else_try),
         (call_script, "script_conclude_quest", "qst_bring_back_runaway_serfs"),
       (try_end),
    ],
   []
   ),
### Defend Nobles Against Peasants quest
##  (0.2, 0.0, 0.0,
##   [
##       (check_quest_active, "qst_defend_nobles_against_peasants"),
##       (neg|check_quest_succeeded, "qst_defend_nobles_against_peasants"),
##       (neg|check_quest_failed, "qst_defend_nobles_against_peasants"),
##       (quest_get_slot, ":quest_target_center", "qst_defend_nobles_against_peasants", slot_quest_target_center),
##       (assign, ":num_active_parties", 0),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_1", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_1"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_1", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_1"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_1"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_2", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_2"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_2", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_2"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_2"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_3", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_3"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_3", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_3"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_3"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_4", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_4"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_4", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_4"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_4"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_5", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_5"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_5", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_5"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_5"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_6", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_6"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_6", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_6"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_6"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_7", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_7"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_7", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_7"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_7"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_defend_nobles_against_peasants_noble_party_8", 0),
##         (party_is_active, "$qst_defend_nobles_against_peasants_noble_party_8"),
##         (val_add, ":num_active_parties", 1),
##         (party_is_in_town, "$qst_defend_nobles_against_peasants_noble_party_8", ":quest_target_center"),
##         (remove_party, "$qst_defend_nobles_against_peasants_noble_party_8"),
##         (party_get_num_companions, ":num_companions", "$qst_defend_nobles_against_peasants_noble_party_8"),
##         (val_add, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":num_companions"),
##       (try_end),
##       (eq, ":num_active_parties", 0),
##       (try_begin),
##         (store_div, ":limit", "$qst_defend_nobles_against_peasants_num_nobles_to_save", 2),
##         (ge, "$qst_defend_nobles_against_peasants_num_nobles_saved", ":limit"),
##         (call_script, "script_succeed_quest", "qst_defend_nobles_against_peasants"),
##       (else_try),
##         (call_script, "script_fail_quest", "qst_defend_nobles_against_peasants"),
##       (try_end),
##    ],
##   []
##   ),
### Capture Conspirators quest
##  (0.15, 0.0, 0.0,
##   [
##       (check_quest_active, "qst_capture_conspirators"),
##       (neg|check_quest_succeeded, "qst_capture_conspirators"),
##       (neg|check_quest_failed, "qst_capture_conspirators"),
##       (quest_get_slot, ":quest_target_center", "qst_capture_conspirators", slot_quest_target_center),
##       (quest_get_slot, ":faction_no", "qst_capture_conspirators", slot_quest_target_faction),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_num_parties_to_spawn", "$qst_capture_conspirators_num_parties_spawned"),
##         (store_random_in_range, ":random_no", 0, 100),
##         (lt, ":random_no", 20),
##         (set_spawn_radius, 3),
##         (spawn_around_party,":quest_target_center","pt_conspirator"),
##         (val_add, "$qst_capture_conspirators_num_parties_spawned", 1),
##         (party_get_num_companions, ":num_companions", reg0),
##         (val_add, "$qst_capture_conspirators_num_troops_to_capture", ":num_companions"),
##         (party_set_ai_behavior, reg0, ai_bhvr_travel_to_party),
##         (party_set_ai_object, reg0, "$qst_capture_conspirators_party_1"),
##         (party_set_flags, reg0, pf_default_behavior, 0),
##         (try_begin),
##           (le, "$qst_capture_conspirators_party_2", 0),
##           (assign, "$qst_capture_conspirators_party_2", reg0),
##         (else_try),
##           (le, "$qst_capture_conspirators_party_3", 0),
##           (assign, "$qst_capture_conspirators_party_3", reg0),
##         (else_try),
##           (le, "$qst_capture_conspirators_party_4", 0),
##           (assign, "$qst_capture_conspirators_party_4", reg0),
##         (else_try),
##           (le, "$qst_capture_conspirators_party_5", 0),
##           (assign, "$qst_capture_conspirators_party_5", reg0),
##         (else_try),
##           (le, "$qst_capture_conspirators_party_6", 0),
##           (assign, "$qst_capture_conspirators_party_6", reg0),
##         (else_try),
##           (le, "$qst_capture_conspirators_party_7", 0),
##           (assign, "$qst_capture_conspirators_party_7", reg0),
##         (try_end),
##       (try_end),
##
##       (assign, ":num_active_parties", 0),
##
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_1", 0),
##         (party_is_active, "$qst_capture_conspirators_party_1"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_1"),
##           (remove_party, "$qst_capture_conspirators_party_1"),
##         (else_try),
##           (party_get_num_attached_parties, ":num_attachments", "$qst_capture_conspirators_party_1"),
##           (gt, ":num_attachments", 0),
##           (assign, ":leave_meeting", 0),
##           (try_begin),
##             (store_sub, ":required_attachments", "$qst_capture_conspirators_num_parties_to_spawn", 1),
##             (eq, ":num_attachments", ":required_attachments"),
##             (val_add, "$qst_capture_conspirators_leave_meeting_counter", 1),
##             (ge, "$qst_capture_conspirators_leave_meeting_counter", 15),
##             (assign, ":leave_meeting", 1),
##           (try_end),
##           (try_begin),
##             (eq, "$qst_capture_conspirators_num_parties_to_spawn", "$qst_capture_conspirators_num_parties_spawned"),
##             (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_capture_conspirators_party_1"),
##             (assign, ":min_distance", 3),
##             (try_begin),
##               (is_currently_night),
##               (assign, ":min_distance", 2),
##             (try_end),
##             (lt, ":cur_distance", ":min_distance"),
##             (assign, "$qst_capture_conspirators_leave_meeting_counter", 15),
##             (assign, ":leave_meeting", 1),
##           (try_end),
##           (eq, ":leave_meeting", 1),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_1", ai_bhvr_travel_to_point),
##           (party_set_flags, "$qst_capture_conspirators_party_1", pf_default_behavior, 0),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_1"),
##           (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##           (party_set_ai_target_position, "$qst_capture_conspirators_party_1", pos2),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_2", 0),
##             (party_detach, "$qst_capture_conspirators_party_2"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_2", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_2", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_2", pos2),
##           (try_end),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_3", 0),
##             (party_detach, "$qst_capture_conspirators_party_3"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_3", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_3", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_3", pos2),
##           (try_end),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_4", 0),
##             (party_detach, "$qst_capture_conspirators_party_4"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_4", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_4", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_4", pos2),
##           (try_end),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_5", 0),
##             (party_detach, "$qst_capture_conspirators_party_5"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_5", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_5", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_5", pos2),
##           (try_end),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_6", 0),
##             (party_detach, "$qst_capture_conspirators_party_6"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_6", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_6", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_6", pos2),
##           (try_end),
##           (try_begin),
##             (gt, "$qst_capture_conspirators_party_7", 0),
##             (party_detach, "$qst_capture_conspirators_party_7"),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_7", ai_bhvr_travel_to_point),
##             (party_set_flags, "$qst_capture_conspirators_party_7", pf_default_behavior, 0),
##             (call_script, "script_map_get_random_position_around_position_within_range", 15, 17),
##             (party_set_ai_target_position, "$qst_capture_conspirators_party_7", pos2),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_1"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_1"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_1"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_1", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_1", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_1", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_1", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_2", 0),
##         (party_is_active, "$qst_capture_conspirators_party_2"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_2"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_2", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_2"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_2"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_2", ai_bhvr_hold),
##             (party_attach_to_party, "$qst_capture_conspirators_party_2", "$qst_capture_conspirators_party_1"),
##             (party_set_flags, "$qst_capture_conspirators_party_2", pf_default_behavior, 0),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_2"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_2"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_2"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_2", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_2", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_2", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_2", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_3", 0),
##         (party_is_active, "$qst_capture_conspirators_party_3"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_3"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_3", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_3"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_3"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_3", ai_bhvr_hold),
##             (party_attach_to_party, "$qst_capture_conspirators_party_3", "$qst_capture_conspirators_party_1"),
##             (party_set_flags, "$qst_capture_conspirators_party_3", pf_default_behavior, 0),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_3"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_3"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_3"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_3", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_3", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_3", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_3", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_4", 0),
##         (party_is_active, "$qst_capture_conspirators_party_4"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_4"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_4", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_4"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_4"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_4", ai_bhvr_hold),
##             (party_set_flags, "$qst_capture_conspirators_party_4", pf_default_behavior, 0),
##             (party_attach_to_party, "$qst_capture_conspirators_party_4", "$qst_capture_conspirators_party_1"),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_4"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_4"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_4"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_4", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_4", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_4", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_4", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_5", 0),
##         (party_is_active, "$qst_capture_conspirators_party_5"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_5"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_5", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_5"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_5"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_5", ai_bhvr_hold),
##             (party_set_flags, "$qst_capture_conspirators_party_5", pf_default_behavior, 0),
##             (party_attach_to_party, "$qst_capture_conspirators_party_5", "$qst_capture_conspirators_party_1"),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_5"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_5"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_5"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_5", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_5", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_5", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_5", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_6", 0),
##         (party_is_active, "$qst_capture_conspirators_party_6"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_6"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_6", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_6"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_6"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_6", ai_bhvr_hold),
##             (party_set_flags, "$qst_capture_conspirators_party_6", pf_default_behavior, 0),
##             (party_attach_to_party, "$qst_capture_conspirators_party_6", "$qst_capture_conspirators_party_1"),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_6"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_6"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_6"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_6", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_6", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_6", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_6", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##       (try_begin),
##         (gt, "$qst_capture_conspirators_party_7", 0),
##         (party_is_active, "$qst_capture_conspirators_party_7"),
##         (val_add, ":num_active_parties", 1),
##         (try_begin),
##           (party_is_in_any_town, "$qst_capture_conspirators_party_7"),
##           (try_begin),
##             (neg|party_is_in_town, "$qst_capture_conspirators_party_7", "$qst_capture_conspirators_party_1"),
##             (remove_party, "$qst_capture_conspirators_party_7"),
##           (else_try),
##             (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_7"),
##             (neq, ":ai_behavior", ai_bhvr_hold),
##             (party_set_ai_behavior, "$qst_capture_conspirators_party_7", ai_bhvr_hold),
##             (party_set_flags, "$qst_capture_conspirators_party_7", pf_default_behavior, 0),
##             (party_attach_to_party, "$qst_capture_conspirators_party_7", "$qst_capture_conspirators_party_1"),
##           (try_end),
##         (try_end),
##         (try_begin),
##           (get_party_ai_behavior, ":ai_behavior", "$qst_capture_conspirators_party_7"),
##           (eq, ":ai_behavior", ai_bhvr_travel_to_point),
##           (party_get_ai_target_position, pos2, "$qst_capture_conspirators_party_7"),
##           (party_get_position, pos1, "$qst_capture_conspirators_party_7"),
##           (get_distance_between_positions, ":distance", pos2, pos1),
##           (lt, ":distance", 200),
##           (call_script, "script_get_closest_walled_center_of_faction", "$qst_capture_conspirators_party_7", ":faction_no"),#Can fail
##           (ge, reg0, 0),
##           (party_set_ai_object, "$qst_capture_conspirators_party_7", reg0),
##           (party_set_ai_behavior, "$qst_capture_conspirators_party_7", ai_bhvr_travel_to_party),
##           (party_set_flags, "$qst_capture_conspirators_party_7", pf_default_behavior, 0),
##         (try_end),
##       (try_end),
##
##       (eq, ":num_active_parties", 0),
##       (party_count_prisoners_of_type, ":count_captured_conspirators", "p_main_party", "trp_conspirator"),
##       (party_count_prisoners_of_type, ":count_captured_conspirator_leaders", "p_main_party", "trp_conspirator_leader"),
##       (val_add, ":count_captured_conspirators", ":count_captured_conspirator_leaders"),
##       (try_begin),
##         (store_div, ":limit", "$qst_capture_conspirators_num_troops_to_capture", 2),
##         (gt, ":count_captured_conspirators", ":limit"),
##         (call_script, "script_succeed_quest", "qst_capture_conspirators"),
##       (else_try),
##         (call_script, "script_fail_quest", "qst_capture_conspirators"),
##       (try_end),
##    ],
##   []
##   ),
# Follow Spy quest
  (0.5, 0.0, 0.0,
   [
       (check_quest_active, "qst_follow_spy"),
       (eq, "$qst_follow_spy_no_active_parties", 0),
       (quest_get_slot, ":quest_giver_center", "qst_follow_spy", slot_quest_giver_center),
       (quest_get_slot, ":quest_object_center", "qst_follow_spy", slot_quest_object_center),
       (assign, ":abort_meeting", 0),
       (try_begin),
         (this_or_next|ge, "$qst_follow_spy_run_away", 2),
         (this_or_next|neg|party_is_active, "$qst_follow_spy_spy_party"),
         (neg|party_is_active, "$qst_follow_spy_spy_partners_party"),
       (else_try),
         (eq, "$qst_follow_spy_meeting_state", 0),
         (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_follow_spy_spy_party"),
         (try_begin),
           (assign, ":min_distance", 3),
           (try_begin),
             (is_currently_night),
             (assign, ":min_distance", 1),
           (try_end),
           (le, ":cur_distance", ":min_distance"),
           (store_distance_to_party_from_party, ":player_distance_to_quest_giver_center", "p_main_party", ":quest_giver_center"),
           (gt, ":player_distance_to_quest_giver_center", 1),
           (val_add, "$qst_follow_spy_run_away", 1),
           (try_begin),
             (eq, "$qst_follow_spy_run_away", 2),
             (assign, ":abort_meeting", 1),
             (display_message, "str_qst_follow_spy_noticed_you"),
           (try_end),
         (else_try),
           (store_distance_to_party_from_party, ":cur_distance", "$qst_follow_spy_spy_partners_party", "$qst_follow_spy_spy_party"),
           (le, ":cur_distance", 1),
           (party_attach_to_party, "$qst_follow_spy_spy_party", "$qst_follow_spy_spy_partners_party"),
           (assign, "$qst_follow_spy_meeting_state", 1),
           (assign, "$qst_follow_spy_meeting_counter", 0),
         (try_end),
       (else_try),
         (eq, "$qst_follow_spy_meeting_state", 1),
         (store_distance_to_party_from_party, ":cur_distance", "p_main_party", "$qst_follow_spy_spy_partners_party"),
         (try_begin),
           (le, ":cur_distance", 1),
           (party_detach, "$qst_follow_spy_spy_party"),
           (val_add, "$qst_follow_spy_run_away", 1),
           (try_begin),
             (eq, "$qst_follow_spy_run_away", 2),
             (assign, ":abort_meeting", 1),
             (display_message, "str_qst_follow_spy_noticed_you"),
           (try_end),
         (else_try),
           (val_add, "$qst_follow_spy_meeting_counter", 1),
           (gt, "$qst_follow_spy_meeting_counter", 4),
           (party_detach, "$qst_follow_spy_spy_party"),
           (assign, ":abort_meeting", 1),
           (assign, "$qst_follow_spy_meeting_state", 2),
         (try_end),
       (try_end),
       (try_begin),
         (eq, ":abort_meeting", 1),
         (party_set_ai_object, "$qst_follow_spy_spy_party", ":quest_giver_center"),
         
         (party_set_ai_object, "$qst_follow_spy_spy_partners_party", ":quest_object_center"),
         
         (party_set_ai_behavior, "$qst_follow_spy_spy_party", ai_bhvr_travel_to_party),
         (party_set_ai_behavior, "$qst_follow_spy_spy_partners_party", ai_bhvr_travel_to_party),
         (party_set_flags, "$qst_follow_spy_spy_party", pf_default_behavior, 0),
         (party_set_flags, "$qst_follow_spy_spy_partners_party", pf_default_behavior, 0),
       (try_end),
       (assign, ":num_active", 0),
       (try_begin),
         (party_is_active, "$qst_follow_spy_spy_party"),
         (val_add, ":num_active", 1),
         (party_is_in_town, "$qst_follow_spy_spy_party", ":quest_giver_center"),
         (remove_party, "$qst_follow_spy_spy_party"),
         (assign, "$qst_follow_spy_spy_back_in_town", 1),
         (val_sub, ":num_active", 1),
       (try_end),
       (try_begin),
         (party_is_active, "$qst_follow_spy_spy_partners_party"),
         (val_add, ":num_active", 1),
         (party_is_in_town, "$qst_follow_spy_spy_partners_party", ":quest_object_center"),
         (remove_party, "$qst_follow_spy_spy_partners_party"),
         (assign, "$qst_follow_spy_partner_back_in_town", 1),
         (val_sub, ":num_active", 1),
       (try_end),
       (try_begin),
         (eq, "$qst_follow_spy_partner_back_in_town",1),
         (eq, "$qst_follow_spy_spy_back_in_town",1),
         (call_script, "script_fail_quest", "qst_follow_spy"),
       (try_end),
       (try_begin),
         (eq, ":num_active", 0),
         (assign, "$qst_follow_spy_no_active_parties", 1),
         (party_count_prisoners_of_type, ":num_spies", "p_main_party", "trp_spy"),
         (party_count_prisoners_of_type, ":num_spy_partners", "p_main_party", "trp_spy_partner"),
         (gt, ":num_spies", 0),
         (gt, ":num_spy_partners", 0),
         (call_script, "script_succeed_quest", "qst_follow_spy"),
       (try_end),
    ],
   []
   ),
### Raiders quest
##  (0.95, 0.0, 0.2,
##   [
##       (check_quest_active, "qst_hunt_down_raiders"),
##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
##    ],
##   [
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
##       (party_set_ai_behavior, ":quest_target_party", ai_bhvr_hold),
##       (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
##    ]
##   ),
##
##  (0.7, 0, 0.2,
##   [
##       (check_quest_active, "qst_hunt_down_raiders"),
##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
##    ],
##   [
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
##       (party_set_ai_behavior,":quest_target_party",ai_bhvr_travel_to_party),
##       (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
##    ]
##   ),
##  
##  (0.1, 0.0, 0.0,
##   [
##       (check_quest_active, "qst_hunt_down_raiders"),
##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
##       (neg|party_is_active, ":quest_target_party")
##    ],
##   [
##       (call_script, "script_succeed_quest", "qst_hunt_down_raiders"),
##    ]
##   ),
##  
##  (1.3, 0, 0.0,
##   [
##       (check_quest_active, "qst_hunt_down_raiders"),
##       (neg|check_quest_succeeded, "qst_hunt_down_raiders"),
##       (neg|check_quest_failed, "qst_hunt_down_raiders"),
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
##       (quest_get_slot, ":quest_target_center", "qst_hunt_down_raiders", slot_quest_target_center),
##       (party_is_in_town,":quest_target_party",":quest_target_center")
##    ],
##   [
##       (call_script, "script_fail_quest", "qst_hunt_down_raiders"),
##       (display_message, "str_raiders_reached_base"),
##       (quest_get_slot, ":quest_target_party", "qst_hunt_down_raiders", slot_quest_target_party),
##       (remove_party, ":quest_target_party"),
##    ]
##   ),

##### TODO: QUESTS COMMENT OUT END

#########################################################################
# Random MERCHANT quest triggers
####################################  
 # Apply interest to merchants guild debt  1% per week
  (24.0 * 7, 0.0, 0.0,
   [],
   [
       (val_mul,"$debt_to_merchants_guild",101),
       (val_div,"$debt_to_merchants_guild",100)
    ]
   ),
# Escort merchant caravan:
  (0.1, 0.0, 0.1, [(check_quest_active, "qst_escort_merchant_caravan"),
                   (eq, "$escort_merchant_caravan_mode", 1)
                   ],
                  [(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                   (try_begin),
                     (party_is_active, ":quest_target_party"),
                     (party_set_ai_behavior, ":quest_target_party", ai_bhvr_hold),
                     (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
                   (try_end),
                   ]),
  (0.1, 0.0, 0.1, [(check_quest_active, "qst_escort_merchant_caravan"),
                    (eq, "$escort_merchant_caravan_mode", 0),
                    ],
                   [(quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                    (try_begin),
                      (party_is_active, ":quest_target_party"),
                      (party_set_ai_behavior, ":quest_target_party", ai_bhvr_escort_party),
                      (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
                      (party_set_ai_object, ":quest_target_party", "p_main_party"),
                    (try_end),
                    ]),

  (0.1, 0, 0.0, [(check_quest_active, "qst_escort_merchant_caravan"),
                 (quest_get_slot, ":quest_target_party", "qst_escort_merchant_caravan", slot_quest_target_party),
                 (neg|party_is_active,":quest_target_party"),
                 ],
                [(call_script, "script_abort_quest", "qst_escort_merchant_caravan", 2),
                 ]),

# Troublesome bandits
  (0.3, 0.0, 1.1, [(check_quest_active, "qst_troublesome_bandits"),
                   (neg|check_quest_failed, "qst_troublesome_bandits"),
                   (store_num_parties_destroyed, ":cur_eliminated", "pt_troublesome_bandits"),
                   (lt, "$qst_troublesome_bandits_eliminated", ":cur_eliminated"),
                   (store_num_parties_destroyed_by_player, ":cur_eliminated_by_player", "pt_troublesome_bandits"),
                   (eq, ":cur_eliminated_by_player", "$qst_troublesome_bandits_eliminated_by_player"),
                   ],
                  [(display_message, "str_bandits_eliminated_by_another"),
                   (call_script, "script_abort_quest", "qst_troublesome_bandits", 2),
                   ]),

  (0.3, 0.0, 1.1, [(check_quest_active, "qst_troublesome_bandits"),
                   (neg|check_quest_succeeded, "qst_troublesome_bandits"),
                   (store_num_parties_destroyed, ":cur_eliminated", "pt_troublesome_bandits"),
                   (lt, "$qst_troublesome_bandits_eliminated", ":cur_eliminated"),
                   (store_num_parties_destroyed_by_player, ":cur_eliminated_by_player", "pt_troublesome_bandits"),
                   (neq, ":cur_eliminated_by_player", "$qst_troublesome_bandits_eliminated_by_player"),
                   ],
                  [(call_script, "script_succeed_quest", "qst_troublesome_bandits"),]),
				  
# Kidnapped girl:
   (1, 0, 0,
   [(check_quest_active, "qst_kidnapped_girl"),
    (quest_get_slot, ":quest_target_party", "qst_kidnapped_girl", slot_quest_target_party),
    (party_is_active, ":quest_target_party"),
    (party_is_in_any_town, ":quest_target_party"),
    (remove_party, ":quest_target_party"),
    ],
   []
   ),


#Rebellion changes begin
#move 

  (0, 0, 24 * 14,
   [
        (try_for_range, ":pretender", pretenders_begin, pretenders_end),
          (troop_set_slot, ":pretender", slot_troop_cur_center, 0),
          (neq, ":pretender", "$supported_pretender"),
          (troop_get_slot, ":target_faction", ":pretender", slot_troop_original_faction),
          (faction_slot_eq, ":target_faction", slot_faction_state, sfs_active),
          (faction_slot_eq, ":target_faction", slot_faction_has_rebellion_chance, 1),
          (neg|troop_slot_eq, ":pretender", slot_troop_occupation, slto_kingdom_hero),

          (try_for_range, ":unused", 0, 30),
            (troop_slot_eq, ":pretender", slot_troop_cur_center, 0),
            (store_random_in_range, ":town", towns_begin, towns_end),
            (store_faction_of_party, ":town_faction", ":town"),
            (store_relation, ":relation", ":town_faction", ":target_faction"),
            (le, ":relation", 0), #fail if nothing qualifies
           
            (troop_set_slot, ":pretender", slot_troop_cur_center, ":town"),
            (try_begin),
              (eq, "$cheat_mode", 1),
              (str_store_troop_name, 4, ":pretender"),
              (str_store_party_name, 5, ":town"),
              (display_message, "@{!}{s4} is in {s5}"),
            (try_end),
          (try_end),

#        (try_for_range, ":rebel_faction", rebel_factions_begin, rebel_factions_end),
#            (faction_get_slot, ":rebellion_status", ":rebel_faction", slot_faction_state),
#            (eq, ":rebellion_status", sfs_inactive_rebellion),
#            (faction_get_slot, ":pretender", ":rebel_faction", slot_faction_leader),
#            (faction_get_slot, ":target_faction", ":rebel_faction", slot_faction_rebellion_target),#

#            (store_random_in_range, ":town", towns_begin, towns_end),
#            (store_faction_of_party, ":town_faction", ":town"),
#            (store_relation, ":relation", ":town_faction", ":target_faction"),
#            (le, ":relation", 0), #fail if nothing qualifies

 #           (faction_set_slot, ":rebel_faction", slot_faction_inactive_leader_location, ":town"),
        (try_end), 
       ],
[]
),
#Rebellion changes end

#NPC system changes begin
#Move unemployed NPCs around taverns
   (24 * 15 , 0, 0, 
   [
    (call_script, "script_update_companion_candidates_in_taverns"),
    ],
   []
   ),

#Process morale and determine personality clashes
  (0, 0, 24,
   [],
[

#Count NPCs in party and get the "grievance divisor", which determines how fast grievances go away
#Set their relation to the player
        (assign, ":npcs_in_party", 0),
        (assign, ":grievance_divisor", 100),
        (try_for_range, ":npc1", companions_begin, companions_end),
            (main_party_has_troop, ":npc1"),
            (val_add, ":npcs_in_party", 1),
        (try_end),
        (val_sub, ":grievance_divisor", ":npcs_in_party"),
        (store_skill_level, ":persuasion_level", "skl_persuasion", "trp_player"),
        (val_add, ":grievance_divisor", ":persuasion_level"),
        (assign, reg7, ":grievance_divisor"),

#        (display_message, "@{!}Process NPC changes. GD: {reg7}"),



##Activate personality clash from 24 hours ago
        (try_begin), #scheduled personality clashes require at least 24hrs together
             (gt, "$personality_clash_after_24_hrs", 0),
             (eq, "$disable_npc_complaints", 0),
             (try_begin),
                  (troop_get_slot, ":other_npc", "$personality_clash_after_24_hrs", slot_troop_personalityclash_object),
                  (main_party_has_troop, "$personality_clash_after_24_hrs"),
                  (main_party_has_troop, ":other_npc"),
                  (assign, "$npc_with_personality_clash", "$personality_clash_after_24_hrs"),
             (try_end),
             (assign, "$personality_clash_after_24_hrs", 0),
        (try_end),
#

         
        (try_for_range, ":npc", companions_begin, companions_end),
###Reset meeting variables
            (troop_set_slot, ":npc", slot_troop_turned_down_twice, 0),
            (try_begin),
                (troop_slot_eq, ":npc", slot_troop_met, 1),
                (troop_set_slot, ":npc", slot_troop_met_previously, 1),
            (try_end),

###Check for coming out of retirement
            (troop_get_slot, ":occupation", ":npc", slot_troop_occupation),
            (try_begin),
                (eq, ":occupation", slto_retirement),
                (troop_get_slot, ":renown_min", ":npc", slot_troop_return_renown),

                (str_store_troop_name, s31, ":npc"),
                (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
                (assign, reg4, ":player_renown"),
                (assign, reg5, ":renown_min"),
#                (display_message, "@{!}Test {s31}  for retirement return {reg4}, {reg5}."),

                (gt, ":player_renown", ":renown_min"),
                (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, 0),
                (troop_set_slot, ":npc", slot_troop_morality_penalties, 0),
                (troop_set_slot, ":npc", slot_troop_occupation, 0),
            (try_end),


#Check for political issues
			(try_begin), #does npc's opponent pipe up?
				(troop_slot_ge, ":npc", slot_troop_days_on_mission, 5),
				(troop_slot_eq, ":npc", slot_troop_current_mission, npc_mission_kingsupport),

				(troop_get_slot, ":other_npc", ":npc", slot_troop_kingsupport_opponent),
				(troop_slot_eq, ":other_npc", slot_troop_kingsupport_objection_state, 0),
				
				(troop_set_slot, ":other_npc", slot_troop_kingsupport_objection_state, 1),
				
				(str_store_troop_name, s3, ":npc"),
				(str_store_troop_name, s4, ":other_npc"),

				(try_begin),
					(eq, "$cheat_mode", 1),
					(display_message, "str_s4_ready_to_voice_objection_to_s3s_mission_if_in_party"),
				(try_end),
			(try_end),

			#Check for quitting
            (try_begin),
                (main_party_has_troop, ":npc"),
				
                (call_script, "script_npc_morale", ":npc"),
                (assign, ":npc_morale", reg0),

                (try_begin),
                    (lt, ":npc_morale", 20),
                    (store_random_in_range, ":random", 0, 100),
                    (val_add, ":npc_morale", ":random"),
                    (lt, ":npc_morale", 20),
                    (assign, "$npc_is_quitting", ":npc"),
                (try_end),

				#Reduce grievance over time (or augment, if party is overcrowded
                (troop_get_slot, ":grievance", ":npc", slot_troop_personalityclash_penalties),
                (val_mul, ":grievance", 90),
                (val_div, ":grievance", ":grievance_divisor"),
                (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, ":grievance"),

                (troop_get_slot, ":grievance", ":npc", slot_troop_morality_penalties),
                (val_mul, ":grievance", 90),
                (val_div, ":grievance", ":grievance_divisor"),
                (troop_set_slot, ":npc", slot_troop_morality_penalties, ":grievance"),


				#Change personality grievance levels
                (try_begin),
                    (this_or_next|troop_slot_ge, ":npc", slot_troop_personalityclash_state, 1),
                        (eq, "$disable_npc_complaints", 1),
                    (troop_get_slot, ":object", ":npc", slot_troop_personalityclash_object),
                    (main_party_has_troop, ":object"),
                    (call_script, "script_reduce_companion_morale_for_clash", ":npc", ":object", slot_troop_personalityclash_state),
                (try_end),
                (try_begin),
                    (this_or_next|troop_slot_ge, ":npc", slot_troop_personalityclash2_state, 1),
                        (eq, "$disable_npc_complaints", 1),
                    (troop_get_slot, ":object", ":npc", slot_troop_personalityclash2_object),
                    (main_party_has_troop, ":object"),
                    (call_script, "script_reduce_companion_morale_for_clash", ":npc", ":object", slot_troop_personalityclash2_state),
                (try_end),
                (try_begin),
                    (this_or_next|troop_slot_ge, ":npc", slot_troop_personalitymatch_state, 1),
                        (eq, "$disable_npc_complaints", 1),
                    (troop_get_slot, ":object", ":npc", slot_troop_personalitymatch_object),
                    (main_party_has_troop, ":object"),
                    (troop_get_slot, ":grievance", ":npc", slot_troop_personalityclash_penalties),
                    (val_mul, ":grievance", 9),
                    (val_div, ":grievance", 10),
                    (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, ":grievance"),
                (try_end),


				
#Check for new personality clashes

				#Active personality clash 1 if at least 24 hours have passed
                (try_begin),
                    (eq, "$disable_npc_complaints", 0),
                    (eq, "$npc_with_personality_clash", 0),
                    (eq, "$npc_with_personality_clash_2", 0),
                    (eq, "$personality_clash_after_24_hrs", 0),
                    (troop_slot_eq, ":npc", slot_troop_personalityclash_state, 0),
                    (troop_get_slot, ":other_npc", ":npc", slot_troop_personalityclash_object),
                    (main_party_has_troop, ":other_npc"),
                    (assign, "$personality_clash_after_24_hrs", ":npc"),
                (try_end),

				#Personality clash 2 and personality match is triggered by battles
				(try_begin),
					(eq, "$npc_with_political_grievance", 0),
				
					(troop_slot_eq, ":npc", slot_troop_kingsupport_objection_state, 1),
					(assign, "$npc_with_political_grievance", ":npc"),
				(try_end),

			#main party does not have troop, and the troop is a companion
			(else_try), 
				(neg|main_party_has_troop, ":npc"),
				(eq, ":occupation", slto_player_companion),

				
				(troop_get_slot, ":days_on_mission", ":npc", slot_troop_days_on_mission),
				(try_begin),
					(gt, ":days_on_mission", 0),
					(val_sub, ":days_on_mission", 1),
					(troop_set_slot, ":npc", slot_troop_days_on_mission, ":days_on_mission"),
				##diplomacy begin
        (else_try),
          (troop_slot_eq, ":npc", slot_troop_current_mission, dplmc_npc_mission_spy_request), #spy mission
          (troop_slot_ge, ":npc", dplmc_slot_troop_mission_diplomacy, 1), #caught

          (troop_set_slot, "trp_hired_blade", slot_troop_mission_object, ":npc"),
          (assign, "$npc_to_rejoin_party", "trp_hired_blade"),
        ##diplomacy end
				(else_try), 
					(troop_slot_ge, ":npc", slot_troop_current_mission, 1),
					
					#If the hero can join
					(this_or_next|neg|troop_slot_eq, ":npc", slot_troop_current_mission, npc_mission_rejoin_when_possible),
						(hero_can_join, ":npc"),
						
					(assign, "$npc_to_rejoin_party", ":npc"),
				(try_end),
            (try_end),
        (try_end),
    ]),


#NPC system changes end

# Lady of the lake achievement
   (1, 0, 0,
   [
     (troop_get_type, ":is_female", "trp_player"),
     (eq, ":is_female", 1),       
     (try_for_range, ":companion", companions_begin, companions_end),
       (troop_slot_eq, ":companion", slot_troop_occupation, slto_player_companion),

       (troop_get_inventory_capacity, ":inv_cap", ":companion"),
       (try_for_range, ":i_slot", 0, ":inv_cap"),
         (troop_get_inventory_slot, ":item_id", ":companion", ":i_slot"),

		 (ge, ":item_id", 0),

	 	 (this_or_next|eq, ":item_id", "itm_great_sword"),
	 	 (this_or_next|eq, ":item_id", "itm_sword_two_handed_a"),
		 (eq, ":item_id", "itm_strange_great_sword"),
		 		 
		 (assign, ":inv_cap", 0),
	   (try_end),
	 (try_end),
    ],
   []
   ),




##diplomacy begin
  # Appoint chamberlain
   (24 , 0, 24 * 12, 
   [],
   [
    (assign, ":has_fief", 0),
    (try_for_range, ":center_no", centers_begin, centers_end),
      (party_get_slot,  ":lord_troop_id", ":center_no", slot_town_lord),
      (eq, ":lord_troop_id", "trp_player"),
      (assign, ":has_fief", 1),
    (try_end),
    (eq, ":has_fief", 1),
    
    (try_begin), #debug
      (eq, "$cheat_mode", 1),
      (assign, reg0, "$g_player_chamberlain"),
      (display_message, "@{!}DEBUG : chamberlain: {reg0}"),
    (try_end),

    (assign, ":notification", 0),
    (try_begin),
      (eq, "$g_player_chamberlain", 0),
      (assign, ":notification", 1),
    (else_try),
      (neq, "$g_player_chamberlain", -1),
      (neq, "$g_player_chamberlain", "trp_dplmc_chamberlain"),
      (assign, ":notification", 1),
    (try_end),
    
    (try_begin),
      (eq, ":notification", 1),
      (call_script, "script_add_notification_menu", "mnu_dplmc_notification_appoint_chamberlain", 0, 0),
    (try_end),]
   ),
   
  # Appoint constable
   (24 , 0, 24 * 13, 
   [],
   [
    (assign, ":has_fief", 0),
    (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
      (party_get_slot,  ":lord_troop_id", ":center_no", slot_town_lord),
      (eq, ":lord_troop_id", "trp_player"),
      (assign, ":has_fief", 1),
    (try_end),
    (eq, ":has_fief", 1),
    
    (try_begin), #debug
      (eq, "$cheat_mode", 1),
      (assign, reg0, "$g_player_constable"),
      (display_message, "@{!}DEBUG : constable: {reg0}"),
    (try_end),

    (assign, ":notification", 0),
    (try_begin),
      (eq, "$g_player_constable", 0),
      (assign, ":notification", 1),
    (else_try),
      (neq, "$g_player_constable", -1),
      (neq, "$g_player_constable", "trp_dplmc_constable"),
      (assign, ":notification", 1),
    (try_end),
    
    (try_begin),
      (eq, ":notification", 1),
      (call_script, "script_add_notification_menu", "mnu_dplmc_notification_appoint_constable", 0, 0),
    (try_end),
    ]
   ),
   
  # Appoint chancellor
   (24 , 0, 24 * 14, 
   [],
   [
   (assign, ":has_fief", 0),
    (try_for_range, ":center_no", towns_begin, towns_end),
      (party_get_slot,  ":lord_troop_id", ":center_no", slot_town_lord),
      (eq, ":lord_troop_id", "trp_player"),
      (assign, ":has_fief", 1),
    (try_end),
    (eq, ":has_fief", 1),
    
    (try_begin), #debug
      (eq, "$cheat_mode", 1),
      (assign, reg0, "$g_player_chancellor"),
      (display_message, "@{!}DEBUG : chancellor: {reg0}"),
    (try_end),

    (assign, ":notification", 0),
    (try_begin),
      (eq, "$g_player_chancellor", 0),
      (assign, ":notification", 1),
    (else_try),
      (neq, "$g_player_chancellor", -1),
      (neq, "$g_player_chancellor", "trp_dplmc_chancellor"),
      (assign, ":notification", 1),
    (try_end),
    
    (try_begin),
      (eq, ":notification", 1),
      (call_script, "script_add_notification_menu", "mnu_dplmc_notification_appoint_chancellor", 0, 0),
    (try_end),
    ]),
   
  #initialize autoloot feature if you have a chamberlain
  ##diplomacy start+
  #Disable this: autoloot gets initialized elsewhere.
  (24, 0, ti_once, 
  [
	  ##NEW:
	  (eq, 0, 1),
	  ##OLD:
      #(store_skill_level, ":inv_skill", "skl_inventory_management", "trp_player"),
      #(gt, "$g_player_chamberlain", 0),
      #(ge, ":inv_skill", 3),      
  ], 
  [
	##NEW:
	#This doesn't ever get called, but if it did here's what should happen"
	(call_script, "script_dplmc_initialize_autoloot", 1),#argument "1" forces this to make changes
	##OLD:
    #(call_script, "script_dplmc_init_item_difficulties"),       
    #(call_script, "script_dplmc_init_item_base_score"), 
    #(assign, "$g_autoloot", 1),
  ]),
  
  (0.1, 0.5, 0, [(map_free,0),(eq,"$g_move_fast", 1)], [(assign,"$g_move_fast", 0)]),
    
##diplomacy end

################################################
################################################


## TGS: mat: Compressed attempt at scripted diplomacy
  # TGS scripted diplomacy
  (24, 0, 0,
               [(store_current_hours, ":number_game_hours_passed"),
                (le, ":number_game_hours_passed", 24*170-6),
                ],
   [
        (store_current_hours, ":number_game_hours_passed"),
        
        (try_for_range, ":first_kingdom", "fac_kingdom_1", kingdoms_end),
        
            (store_add, ":first_kingdom_plus_one", ":first_kingdom", 1),
            (try_for_range, ":second_kingdom", ":first_kingdom_plus_one", kingdoms_end),
        
                (store_relation, ":rel", ":first_kingdom", ":second_kingdom"),
                (assign, ":diplo_action_taken", 0),
        
                (try_begin),

      #Set diplomacy for the first 30 days
    
      #Legion is at peace with everyone
      #Southland Coalition is at war with Southland Alliance, Seanchan and at peace with everyone else
      #Southland Alliance is at war with Southland Coalition, Seanchan and at peace with everyone else
      #Borderlands are at war with Shadowspawn, neutral with Aiel Nation, and at peace with everyone else
      #White Tower is at war with Shadowspawn and at peace with everyone else
      #Aiel Nation is at war with Shadowspawn, neutral with Borderlands, and at peace with everyone else
      #Seanchan are at war with Southland Coalition, Southland Alliance and at peace with everyone else
      #Shadowspawn are at war with Aiel Nation, Borderlands, and White Tower and at peace with everyone else        
        
                (is_between, ":number_game_hours_passed", 0, 24*30-6),

        
                    # Nations at War        
                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_6"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_10"), # illian vs tear
                    (eq, ":second_kingdom", "fac_kingdom_16"), # illian vs whitecloaks
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),
        
                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_7"),
                    (eq, ":second_kingdom", "fac_kingdom_11"), # murandy vs andor
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),
        
                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_9"),
                    (eq, ":second_kingdom", "fac_kingdom_14"), # arad doman vs tarabon
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),
        
                    (try_begin), # Original
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_17"), # shienar vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_18"), # arafel vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_19"), # kandor vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_20"), # saldaea vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_21"), # white tower vs shadowspawn
                    (eq, ":first_kingdom", "fac_kingdom_22"), # aiel vs shadowspawn
                    (eq, ":second_kingdom", "fac_kingdom_24"),
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_23"),
                    (eq, ":second_kingdom", "fac_kingdom_28"), # seanchan vs toman head
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),        

        
                    # Nations at Peace
                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_1"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_2"), # legion and band
                    (eq, ":second_kingdom", "fac_kingdom_3"), # legion and two rivers
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_2"),
                    (eq, ":second_kingdom", "fac_kingdom_3"), # band and two rivers
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_3"),
                    (eq, ":second_kingdom", "fac_kingdom_11"), # two rivers and andor
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_11"),
                    (eq, ":second_kingdom", "fac_kingdom_21"), # andor and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_15"),
                    (eq, ":second_kingdom", "fac_kingdom_16"), # amadicia and whitecloaks
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_17"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_18"), # shienar and arafel
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_19"), # shienar and kandor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_20"), # shienar and saldaea
                    (eq, ":second_kingdom", "fac_kingdom_21"), # shienar and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_18"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_19"), # arafel and kandor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_20"), # arafel and saldaea
                    (eq, ":second_kingdom", "fac_kingdom_21"), # arafel and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_19"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_20"), # kandor and saldaea
                    (eq, ":second_kingdom", "fac_kingdom_21"), # kandor and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_20"),
                    (eq, ":second_kingdom", "fac_kingdom_21"), # saldaea and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),                
        

                    # Nations who are Neutral - may squabble, but not actively warring (Default State)
                    (try_begin),
                    (eq, ":diplo_action_taken", 0),
                        (try_begin),
                        (neg|is_between, ":rel", -5, 6),
                            (call_script, "script_diplomacy_start_neutral_between_kingdoms", ":first_kingdom", ":second_kingdom", 1),
                        (try_end),
                    (try_end),

        


      #Set diplomacy for days 30 though 45
    
      #Legion is neutral with Southland Alliance and at peace with everyone else  (High peace with Aiel after 45 days)
      #Southland Coalition is at war with Southland Alliance, Seanchan, and at peace with everyone else
      #Southland Alliance is at war with Southland Coalition, Seanchan, neutral with Legion, Aiel Nation, and at peace with everyone else
      #Borderlands are at war with Shadowspawn, neutral with Aiel Nation, and at peace with everyone else
      #White Tower is at war with Shadowspawn and at peace with everyone else
      #Aiel Nation is at war with Shadowspawn, neutral with Borderlands, Southland Alliance and at peace with everyone else
      #Seanchan are at war with Southland Coalition,Southland Alliance and at peace with everyone else
      #Shadowspawn are at war with Aiel Nation, Borderlands, and White Tower and at peace with everyone else

                (else_try),
                (is_between, ":number_game_hours_passed", 24*30-6, 24*45-6),

        
                    # Nations at War
                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_6"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_10"), # illian vs tear
                    (eq, ":second_kingdom", "fac_kingdom_16"), # illian vs whitecloaks
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),
        
                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_7"),
                    (eq, ":second_kingdom", "fac_kingdom_11"), # murandy vs andor
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),
        
                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_9"),
                    (eq, ":second_kingdom", "fac_kingdom_14"), # arad doman vs tarabon
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),
        
                    (try_begin), # Original
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_17"), # shienar vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_18"), # arafel vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_19"), # kandor vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_20"), # saldaea vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_21"), # white tower vs shadowspawn
                    (eq, ":first_kingdom", "fac_kingdom_22"), # aiel vs shadowspawn
                    (eq, ":second_kingdom", "fac_kingdom_24"),
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 30 - 45
                    (eq, ":first_kingdom", "fac_kingdom_23"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_26"), # seanchan vs sea folk
                    (eq, ":second_kingdom", "fac_kingdom_28"), # seanchan vs toman head
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),            


                    # Nations at Peace
                    (try_begin), # Modified for 30 - 45
                    (eq, ":first_kingdom", "fac_kingdom_1"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_2"), # legion and band
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_3"), # legion and two rivers
                    (eq, ":second_kingdom", "fac_kingdom_4"), # legion and mayene
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Modified for 30 - 45
                    (eq, ":first_kingdom", "fac_kingdom_2"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_3"), # band and two rivers
                    (eq, ":second_kingdom", "fac_kingdom_4"), # band and mayene
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Modified for 30 - 45
                    (eq, ":first_kingdom", "fac_kingdom_3"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_3"), # two rivers and mayene
                    (eq, ":second_kingdom", "fac_kingdom_11"), # two rivers and andor
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_11"),
                    (eq, ":second_kingdom", "fac_kingdom_21"), # andor and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_15"),
                    (eq, ":second_kingdom", "fac_kingdom_16"), # amadicia and whitecloaks
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_17"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_18"), # shienar and arafel
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_19"), # shienar and kandor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_20"), # shienar and saldaea
                    (eq, ":second_kingdom", "fac_kingdom_21"), # shienar and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_18"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_19"), # arafel and kandor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_20"), # arafel and saldaea
                    (eq, ":second_kingdom", "fac_kingdom_21"), # arafel and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_19"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_20"), # kandor and saldaea
                    (eq, ":second_kingdom", "fac_kingdom_21"), # kandor and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_20"),
                    (eq, ":second_kingdom", "fac_kingdom_21"), # saldaea and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),                
        

                    # Nations who are Neutral - may squabble, but not actively warring (Default State)
                    (try_begin),
                    (eq, ":diplo_action_taken", 0),
                        (try_begin),
                        (neg|is_between, ":rel", -5, 6),
                            (call_script, "script_diplomacy_start_neutral_between_kingdoms", ":first_kingdom", ":second_kingdom", 1),
                        (try_end),
                    (try_end),

      #Set diplomacy for days 45 though 60
    
      #Legion is neutral with Southland Alliance and at peace with everyone else  (High peace with Aiel after 45 days)
      #Southland Coalition is at war with Southland Alliance, Seanchan, and at peace with everyone else
      #Southland Alliance is at war with Southland Coalition, Seanchan, neutral with Legion, Aiel Nation, and at peace with everyone else
      #Borderlands are at war with Shadowspawn, neutral with Aiel Nation, and at peace with everyone else
      #White Tower is at war with Shadowspawn and at peace with everyone else
      #Aiel Nation is at war with Shadowspawn, neutral with Borderlands, Southland Alliance and at peace with everyone else
      #Seanchan are at war with Southland Coalition,Southland Alliance and at peace with everyone else
      #Shadowspawn are at war with Aiel Nation, Borderlands, and White Tower and at peace with everyone else

                (else_try),
                (is_between, ":number_game_hours_passed", 24*45-6, 24*60-6),

        
                    # Nations at War
                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_6"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_10"), # illian vs tear
                    (eq, ":second_kingdom", "fac_kingdom_16"), # illian vs whitecloaks
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),
        
                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_7"),
                    (eq, ":second_kingdom", "fac_kingdom_11"), # murandy vs andor
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),
        
                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_9"),
                    (eq, ":second_kingdom", "fac_kingdom_14"), # arad doman vs tarabon
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),
        
                    (try_begin), # Original
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_17"), # shienar vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_18"), # arafel vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_19"), # kandor vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_20"), # saldaea vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_21"), # white tower vs shadowspawn
                    (eq, ":first_kingdom", "fac_kingdom_22"), # aiel vs shadowspawn
                    (eq, ":second_kingdom", "fac_kingdom_24"),
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 45 - 60
                    (eq, ":first_kingdom", "fac_kingdom_14"),
                    (eq, ":second_kingdom", "fac_kingdom_23"), # tarabon vs seanchan
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),        
                    (try_end),

                    (try_begin), # New for 45 - 60
                    (eq, ":first_kingdom", "fac_kingdom_23"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_26"), # seanchan vs sea folk
                    (eq, ":second_kingdom", "fac_kingdom_28"), # seanchan vs toman head
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),            
        

                    # Nations at Peace
                    (try_begin), # Modified for 45 - 60
                    (eq, ":first_kingdom", "fac_kingdom_1"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_2"), # legion and band
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_3"), # legion and two rivers
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_4"), # legion and mayene
                    (eq, ":second_kingdom", "fac_kingdom_22"), # legion and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Modified for 45 - 60
                    (eq, ":first_kingdom", "fac_kingdom_2"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_3"), # band and two rivers
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_4"), # band and mayene
                    (eq, ":second_kingdom", "fac_kingdom_22"), # band and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Modified for 45 - 60
                    (eq, ":first_kingdom", "fac_kingdom_3"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_3"), # two rivers and mayene
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # two rivers and andor
                    (eq, ":second_kingdom", "fac_kingdom_22"), # two rivers and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_11"),
                    (eq, ":second_kingdom", "fac_kingdom_21"), # andor and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_15"),
                    (eq, ":second_kingdom", "fac_kingdom_16"), # amadicia and whitecloaks
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_17"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_18"), # shienar and arafel
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_19"), # shienar and kandor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_20"), # shienar and saldaea
                    (eq, ":second_kingdom", "fac_kingdom_21"), # shienar and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_18"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_19"), # arafel and kandor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_20"), # arafel and saldaea
                    (eq, ":second_kingdom", "fac_kingdom_21"), # arafel and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_19"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_20"), # kandor and saldaea
                    (eq, ":second_kingdom", "fac_kingdom_21"), # kandor and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_20"),
                    (eq, ":second_kingdom", "fac_kingdom_21"), # saldaea and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),                
        

                    # Nations who are Neutral - may squabble, but not actively warring (Default State)
                    (try_begin),
                    (eq, ":diplo_action_taken", 0),
                        (try_begin),
                        (neg|is_between, ":rel", -5, 6),
                            (call_script, "script_diplomacy_start_neutral_between_kingdoms", ":first_kingdom", ":second_kingdom", 1),
                        (try_end),
                    (try_end),

      #Set diplomacy for days 60 though 75
    
      #Legion is neutral with Southland Coalition, Southland Alliance, Seanchan, Shadowspawn and at peace with everyone else  (Super peace with Aiel Nation)
      #Southland Coalition is at war with Southland Alliance, Seanchan, neutral with Legion, Aiel Nation and at peace with everyone else
      #Southland Alliance is at war with Southland Coalition and Seanchan, neutral with Legion, Aiel Nation and at peace with everyone else
      #Borderlands are at war with Shadowspawn, peace with Aiel Nation, and at peace with everyone else
      #White Tower is at war with Shadowspawn and at peace with everyone else
      #Aiel Nation is at war with Shadowspawn, neutral with Southland Coalition, Southland Alliance, Seanchan, and peace with Borderlands and everyone else
      #Seanchan are at war with Southland Coalition and Southland Alliance and at peace with everyone else
      #Shadowspawn are at war with Aiel Nation, Borderlands, and White Tower and at peace with everyone else

                (else_try),
                (is_between, ":number_game_hours_passed", 24*60-6, 24*75-6),

        
                    # Nations at War
                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_6"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_10"), # illian vs tear
                    (eq, ":second_kingdom", "fac_kingdom_16"), # illian vs whitecloaks
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),
        
                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_7"),
                    (eq, ":second_kingdom", "fac_kingdom_11"), # murandy vs andor
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),
        
                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_9"),
                    (eq, ":second_kingdom", "fac_kingdom_14"), # arad doman vs tarabon
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),
        
                    (try_begin), # Modified for 60 - 75
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_1"), # legion vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_2"), # band vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_3"), # two rivers vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_17"), # shienar vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_18"), # arafel vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_19"), # kandor vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_20"), # saldaea vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_21"), # white tower vs shadowspawn
                    (eq, ":first_kingdom", "fac_kingdom_22"), # aiel vs shadowspawn
                    (eq, ":second_kingdom", "fac_kingdom_24"),
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Modified for 60 - 75
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_8"), # altara vs seanchan
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_14"), # tarabon vs seanchan
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_15"), # amadicia vs seanchan
                    (eq, ":first_kingdom", "fac_kingdom_16"), # whitecloaks vs seanchan
                    (eq, ":second_kingdom", "fac_kingdom_23"),
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 45 - 60
                    (eq, ":first_kingdom", "fac_kingdom_23"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_26"), # seanchan vs sea folk
                    (eq, ":second_kingdom", "fac_kingdom_28"), # seanchan vs toman head
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),           
        

                    # Nations at Peace
                    (try_begin), # Modified for 45 - 60
                    (eq, ":first_kingdom", "fac_kingdom_1"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_2"), # legion and band
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_3"), # legion and two rivers
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_4"), # legion and mayene
                    (eq, ":second_kingdom", "fac_kingdom_22"), # legion and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Modified for 45 - 60
                    (eq, ":first_kingdom", "fac_kingdom_2"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_3"), # band and two rivers
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_4"), # band and mayene
                    (eq, ":second_kingdom", "fac_kingdom_22"), # band and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Modified for 45 - 60
                    (eq, ":first_kingdom", "fac_kingdom_3"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_3"), # two rivers and mayene
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # two rivers and andor
                    (eq, ":second_kingdom", "fac_kingdom_22"), # two rivers and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_11"),
                    (eq, ":second_kingdom", "fac_kingdom_21"), # andor and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_15"),
                    (eq, ":second_kingdom", "fac_kingdom_16"), # amadicia and whitecloaks
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_17"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_18"), # shienar and arafel
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_19"), # shienar and kandor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_20"), # shienar and saldaea
                    (eq, ":second_kingdom", "fac_kingdom_21"), # shienar and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_18"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_19"), # arafel and kandor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_20"), # arafel and saldaea
                    (eq, ":second_kingdom", "fac_kingdom_21"), # arafel and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_19"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_20"), # kandor and saldaea
                    (eq, ":second_kingdom", "fac_kingdom_21"), # kandor and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_20"),
                    (eq, ":second_kingdom", "fac_kingdom_21"), # saldaea and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),                
        

                    # Nations who are Neutral - may squabble, but not actively warring (Default State)
                    (try_begin),
                    (eq, ":diplo_action_taken", 0),
                        (try_begin),
                        (neg|is_between, ":rel", -5, 6),
                            (call_script, "script_diplomacy_start_neutral_between_kingdoms", ":first_kingdom", ":second_kingdom", 1),
                        (try_end),
                    (try_end),

      #Set diplomacy for days 75 though 95
    
      #Legion is neutral with Southland Coalition, Shadowspawn, war with Seanchan and at peace with everyone else  (Super peace with Aiel Nation)
      #Southland Coalition is neutral with Southland Alliance, Legion, Aiel Nation at war with Seanchan and at peace with everyone else
      #Southland Alliance is neutral with Southland Coalition, at war with Seanchan, and at peace with everyone else
      #Borderlands are at war with Shadowspawn, peace with Aiel Nation, and at peace with everyone else
      #White Tower is at war with Shadowspawn, neutral with Seanchan, and at peace with everyone else
      #Aiel Nation is at war with Shadowspawn, Seanchan, neutral with Southland Coalition, and peace with Borderlands and everyone else
      #Seanchan are at war with Southland Coalition and Southland Alliance, Legion, Aiel Nation, neutral with Shadowspawn, White Tower, and at peace with everyone else
      #Shadowspawn are at war with Aiel Nation, Borderlands, and White Tower, neutral with Legion, and at peace with everyone else

                (else_try),
                (is_between, ":number_game_hours_passed", 24*75-6, 24*95-6),

        
                    # Nations at War
                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_6"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_10"), # illian vs tear
                    (eq, ":second_kingdom", "fac_kingdom_16"), # illian vs whitecloaks
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),
        
                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_7"),
                    (eq, ":second_kingdom", "fac_kingdom_11"), # murandy vs andor
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),
        
                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_9"),
                    (eq, ":second_kingdom", "fac_kingdom_14"), # arad doman vs tarabon
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Modified for 60 - 75
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_1"), # legion vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_2"), # band vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_3"), # two rivers vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_17"), # shienar vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_18"), # arafel vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_19"), # kandor vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_20"), # saldaea vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_21"), # white tower vs shadowspawn
                    (eq, ":first_kingdom", "fac_kingdom_22"), # aiel vs shadowspawn
                    (eq, ":second_kingdom", "fac_kingdom_24"),
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Modified for 75 - 95
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_1"), # legion vs seanchan
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_2"), # band vs seanchan
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_3"), # two rivers vs seanchan
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_8"), # altara vs seanchan
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_14"), # tarabon vs seanchan
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_15"), # amadicia vs seanchan
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_16"), # whitecloaks vs seanchan
                    (eq, ":first_kingdom", "fac_kingdom_22"), # aiel vs seanchan
                    (eq, ":second_kingdom", "fac_kingdom_23"),
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 45 - 60
                    (eq, ":first_kingdom", "fac_kingdom_23"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_26"), # seanchan vs sea folk
                    (eq, ":second_kingdom", "fac_kingdom_28"), # seanchan vs toman head
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),           


                    # Nations at Peace
                    (try_begin), # Modified for 75 - 95
                    (eq, ":first_kingdom", "fac_kingdom_1"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_2"), # legion and band
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_3"), # legion and two rivers
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_4"), # legion and mayene
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # legion and andor
                    (eq, ":second_kingdom", "fac_kingdom_22"), # legion and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Modified for 75 - 95
                    (eq, ":first_kingdom", "fac_kingdom_2"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_3"), # band and two rivers
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_4"), # band and mayene
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # band and andor
                    (eq, ":second_kingdom", "fac_kingdom_22"), # band and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Modified for 75 - 95
                    (eq, ":first_kingdom", "fac_kingdom_3"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_3"), # two rivers and mayene
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # two rivers and andor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # two rivers and ghealdan
                    (eq, ":second_kingdom", "fac_kingdom_22"), # two rivers and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 75 - 95
                    (eq, ":first_kingdom", "fac_kingdom_8"),
                    (eq, ":second_kingdom", "fac_kingdom_23"), # altara and seanchan
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),        

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_11"),
                    (eq, ":second_kingdom", "fac_kingdom_21"), # andor and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_15"),
                    (eq, ":second_kingdom", "fac_kingdom_16"), # amadicia and whitecloaks
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_17"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_18"), # shienar and arafel
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_19"), # shienar and kandor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_20"), # shienar and saldaea
                    (eq, ":second_kingdom", "fac_kingdom_21"), # shienar and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_18"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_19"), # arafel and kandor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_20"), # arafel and saldaea
                    (eq, ":second_kingdom", "fac_kingdom_21"), # arafel and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_19"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_20"), # kandor and saldaea
                    (eq, ":second_kingdom", "fac_kingdom_21"), # kandor and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_20"),
                    (eq, ":second_kingdom", "fac_kingdom_21"), # saldaea and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),                
        

                    # Nations who are Neutral - may squabble, but not actively warring (Default State)
                    (try_begin),
                    (eq, ":diplo_action_taken", 0),
                        (try_begin),
                        (neg|is_between, ":rel", -5, 6),
                            (call_script, "script_diplomacy_start_neutral_between_kingdoms", ":first_kingdom", ":second_kingdom", 1),
                        (try_end),
                    (try_end),

      #Set diplomacy for days 95 though 118
    
      #Legion is neutral with Southland Coalition, Shadowspawn, war with Seanchan and at peace with everyone else  (Super peace with Aiel Nation)
      #Southland Coalition is neutral with Southland Alliance, Legion, Aiel Nation at war with Seanchan and at peace with everyone else
      #Southland Alliance is neutral with Southland Coalition, at war with Seanchan, and at peace with everyone else
      #Borderlands are at war with Shadowspawn, peace with Aiel Nation, and at peace with everyone else
      #White Tower is at war with Shadowspawn, neutral with Seanchan, and at peace with everyone else
      #Aiel Nation is at war with Shadowspawn, Seanchan, neutral with Southland Coalition, and peace with Borderlands and everyone else
      #Seanchan are at war with Southland Coalition and Southland Alliance, Legion, Aiel Nation, neutral with Shadowspawn, White Tower, and at peace with everyone else
      #Shadowspawn are at war with Aiel Nation, Borderlands, and White Tower, neutral with Legion, and at peace with everyone else

                (else_try),
                (is_between, ":number_game_hours_passed", 24*95-6, 24*118-6),

        
                    # Nations at War
                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_7"),
                    (eq, ":second_kingdom", "fac_kingdom_11"), # murandy vs andor
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),
        
                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_9"),
                    (eq, ":second_kingdom", "fac_kingdom_14"), # arad doman vs tarabon
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Modified for 60 - 75
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_1"), # legion vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_2"), # band vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_3"), # two rivers vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_17"), # shienar vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_18"), # arafel vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_19"), # kandor vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_20"), # saldaea vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_21"), # white tower vs shadowspawn
                    (eq, ":first_kingdom", "fac_kingdom_22"), # aiel vs shadowspawn
                    (eq, ":second_kingdom", "fac_kingdom_24"),
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Modified for 75 - 95
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_1"), # legion vs seanchan
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_2"), # band vs seanchan
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_3"), # two rivers vs seanchan
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_8"), # altara vs seanchan
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_14"), # tarabon vs seanchan
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_15"), # amadicia vs seanchan
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_16"), # whitecloaks vs seanchan
                    (eq, ":first_kingdom", "fac_kingdom_22"), # aiel vs seanchan
                    (eq, ":second_kingdom", "fac_kingdom_23"),
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 95-118
                    (eq, ":first_kingdom", "fac_kingdom_23"),
                    (eq, ":second_kingdom", "fac_kingdom_26"), # seanchan vs sea folk
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),           


                    # Nations at Peace
                    (try_begin), # Modified for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_1"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_2"), # legion and band
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_3"), # legion and two rivers
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_4"), # legion and mayene
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_5"), # legion and cairhien
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_6"), # legion and illian
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_9"), # legion and arad doman
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_10"), # legion and tear
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # legion and andor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # legion and ghealdan
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # legion and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_22"), # legion and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Modified for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_2"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_3"), # band and two rivers
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_4"), # band and mayene
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_5"), # band and cairhien
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_6"), # band and illian
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_9"), # band and arad doman
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_10"), # band and tear
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # band and andor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # band and ghealdan
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # band and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_22"), # band and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Modified for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_3"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_4"), # two rivers and mayene
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_5"), # two rivers and cairhien
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_6"), # two rivers and illian
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_9"), # two rivers and arad doman
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_10"), # two rivers and tear
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # two rivers and andor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # two rivers and ghealdan
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # two rivers and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_22"), # two rivers and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_4"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_5"), # mayene and cairhien
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_6"), # mayene and illian
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_9"), # mayene and arad doman
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_10"), # mayene and tear
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # mayene and andor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # mayene and ghealdan
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # mayene and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_22"), # mayene and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_5"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_6"), # cairhien and illian
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_9"), # cairhien and arad doman
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_10"), # cairhien and tear
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # cairhien and andor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # cairhien and ghealdan
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # cairhien and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_22"), # cairhien and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_6"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_9"), # illian and arad doman
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_10"), # illian and tear
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # illian and andor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # illian and ghealdan
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # illian and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_22"), # illian and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),           

                    (try_begin), # Modified for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_8"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_14"), # altara and tarabon
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_15"), # altara and amadicia
                    (eq, ":second_kingdom", "fac_kingdom_23"), # altara and seanchan
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_9"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_10"), # arad doman and tear
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # arad doman and andor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # arad doman and ghealdan
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # arad doman and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_22"), # arad doman and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_10"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # tear and andor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # tear and ghealdan
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # tear and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_22"), # tear and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_11"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # andor and ghealdan
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # andor and whitecloaks
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_21"), # andor and white tower
                    (eq, ":second_kingdom", "fac_kingdom_22"), # andor and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_12"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # ghealdan and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_22"), # ghealdan and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),            

                    (try_begin), # Modified for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_14"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_15"), # tarabon and amadicia
                    (eq, ":second_kingdom", "fac_kingdom_23"), # tarabon and seanchan
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Modified for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_15"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_23"), # amadicia and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_23"), # amadicia and seanchan
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_16"),
                    (eq, ":second_kingdom", "fac_kingdom_22"), # whitecloaks and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),         

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_17"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_18"), # shienar and arafel
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_19"), # shienar and kandor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_20"), # shienar and saldaea
                    (eq, ":second_kingdom", "fac_kingdom_21"), # shienar and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_18"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_19"), # arafel and kandor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_20"), # arafel and saldaea
                    (eq, ":second_kingdom", "fac_kingdom_21"), # arafel and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_19"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_20"), # kandor and saldaea
                    (eq, ":second_kingdom", "fac_kingdom_21"), # kandor and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_20"),
                    (eq, ":second_kingdom", "fac_kingdom_21"), # saldaea and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),                
        

                    # Nations who are Neutral - may squabble, but not actively warring (Default State)
                    (try_begin),
                    (eq, ":diplo_action_taken", 0),
                        (try_begin),
                        (neg|is_between, ":rel", -5, 6),
                            (call_script, "script_diplomacy_start_neutral_between_kingdoms", ":first_kingdom", ":second_kingdom", 1),
                        (try_end),
                    (try_end),

      #Set diplomacy for days 118 though 120
    
      #Legion is neutral with Southland Coalition, Shadowspawn, war with Seanchan and at peace with everyone else  (Super peace with Aiel Nation)
      #Southland Coalition is neutral with Southland Alliance, Legion, Aiel Nation at war with Seanchan and at peace with everyone else
      #Southland Alliance is neutral with Southland Coalition, at war with Seanchan, and at peace with everyone else
      #Borderlands are at war with Shadowspawn, peace with Aiel Nation, and at peace with everyone else
      #White Tower is at war with Shadowspawn, neutral with Seanchan, and at peace with everyone else
      #Aiel Nation is at war with Shadowspawn, Seanchan, neutral with Southland Coalition, and peace with Borderlands and everyone else
      #Seanchan are at war with Southland Coalition and Southland Alliance, Legion, Aiel Nation, neutral with Shadowspawn, White Tower, and at peace with everyone else
      #Shadowspawn are at war with Aiel Nation, Borderlands, and White Tower, neutral with Legion, and at peace with everyone else

                (else_try),
                (is_between, ":number_game_hours_passed", 24*118-6, 24*120-6),

        
                    # Nations at War
                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_7"),
                    (eq, ":second_kingdom", "fac_kingdom_11"), # murandy vs andor
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),
        
                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_9"),
                    (eq, ":second_kingdom", "fac_kingdom_14"), # arad doman vs tarabon
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Modified for 60 - 75
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_1"), # legion vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_2"), # band vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_3"), # two rivers vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_17"), # shienar vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_18"), # arafel vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_19"), # kandor vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_20"), # saldaea vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_21"), # white tower vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_22"), # aiel vs shadowspawn
                    (eq, ":first_kingdom", "fac_kingdom_23"), # seanchan vs shadowspawn
                    (eq, ":second_kingdom", "fac_kingdom_24"),
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Modified for 118 - 120
                    (eq, ":first_kingdom", "fac_kingdom_21"), # white tower vs seanchan
                    (eq, ":second_kingdom", "fac_kingdom_23"),
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 95-118
                    (eq, ":first_kingdom", "fac_kingdom_23"),
                    (eq, ":second_kingdom", "fac_kingdom_26"), # seanchan vs sea folk
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),         


                    # Nations at Peace
                    (try_begin), # Modified for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_1"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_2"), # legion and band
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_3"), # legion and two rivers
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_4"), # legion and mayene
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_5"), # legion and cairhien
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_6"), # legion and illian
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_9"), # legion and arad doman
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_10"), # legion and tear
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # legion and andor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # legion and ghealdan
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # legion and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_22"), # legion and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Modified for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_2"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_3"), # band and two rivers
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_4"), # band and mayene
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_5"), # band and cairhien
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_6"), # band and illian
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_9"), # band and arad doman
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_10"), # band and tear
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # band and andor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # band and ghealdan
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # band and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_22"), # band and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Modified for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_3"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_4"), # two rivers and mayene
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_5"), # two rivers and cairhien
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_6"), # two rivers and illian
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_9"), # two rivers and arad doman
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_10"), # two rivers and tear
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # two rivers and andor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # two rivers and ghealdan
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # two rivers and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_22"), # two rivers and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_4"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_5"), # mayene and cairhien
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_6"), # mayene and illian
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_9"), # mayene and arad doman
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_10"), # mayene and tear
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # mayene and andor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # mayene and ghealdan
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # mayene and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_22"), # mayene and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_5"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_6"), # cairhien and illian
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_9"), # cairhien and arad doman
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_10"), # cairhien and tear
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # cairhien and andor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # cairhien and ghealdan
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # cairhien and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_22"), # cairhien and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_6"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_9"), # illian and arad doman
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_10"), # illian and tear
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # illian and andor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # illian and ghealdan
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # illian and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_22"), # illian and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),           

                    (try_begin), # Modified for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_8"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_14"), # altara and tarabon
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_15"), # altara and amadicia
                    (eq, ":second_kingdom", "fac_kingdom_23"), # altara and seanchan
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_9"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_10"), # arad doman and tear
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # arad doman and andor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # arad doman and ghealdan
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # arad doman and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_22"), # arad doman and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_10"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # tear and andor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # tear and ghealdan
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # tear and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_22"), # tear and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_11"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # andor and ghealdan
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # andor and whitecloaks
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_21"), # andor and white tower
                    (eq, ":second_kingdom", "fac_kingdom_22"), # andor and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_12"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # ghealdan and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_22"), # ghealdan and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),            

                    (try_begin), # Modified for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_14"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_15"), # tarabon and amadicia
                    (eq, ":second_kingdom", "fac_kingdom_23"), # tarabon and seanchan
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Modified for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_15"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_23"), # amadicia and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_23"), # amadicia and seanchan
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_16"),
                    (eq, ":second_kingdom", "fac_kingdom_22"), # whitecloaks and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),         

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_17"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_18"), # shienar and arafel
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_19"), # shienar and kandor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_20"), # shienar and saldaea
                    (eq, ":second_kingdom", "fac_kingdom_21"), # shienar and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_18"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_19"), # arafel and kandor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_20"), # arafel and saldaea
                    (eq, ":second_kingdom", "fac_kingdom_21"), # arafel and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_19"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_20"), # kandor and saldaea
                    (eq, ":second_kingdom", "fac_kingdom_21"), # kandor and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_20"),
                    (eq, ":second_kingdom", "fac_kingdom_21"), # saldaea and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),                
        

                    # Nations who are Neutral - may squabble, but not actively warring (Default State)
                    (try_begin),
                    (eq, ":diplo_action_taken", 0),
                        (try_begin),
                        (neg|is_between, ":rel", -5, 6),
                            (call_script, "script_diplomacy_start_neutral_between_kingdoms", ":first_kingdom", ":second_kingdom", 1),
                        (try_end),
                    (try_end),

      #Set diplomacy for days 120 though 170

############################################################################################################        
    
      #All at war with the Shadowspawn for at least 50 days (other stuff stays somewhat the same)

                (else_try),
                (is_between, ":number_game_hours_passed", 24*120-6, 24*170-6),

        
                    # Nations at War
                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_7"),
                    (eq, ":second_kingdom", "fac_kingdom_11"), # murandy vs andor
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),
        
                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_9"),
                    (eq, ":second_kingdom", "fac_kingdom_14"), # arad doman vs tarabon
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Modified for 120 - 170
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_1"), # legion vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_2"), # band vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_3"), # two rivers vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_4"), # mayene vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_5"), # cairhien vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_6"), # illian vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_7"), # murandy vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_8"), # altara tower vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_9"), # arad doman vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_10"), # tear vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_11"), # andor vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_12"), # ghealdan vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_13"), # far madding vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_14"), # tarabon vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_15"), # amadicia vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_16"), # whitecloaks vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_17"), # shienar vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_18"), # arafel vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_19"), # kandor vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_20"), # saldaea vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_21"), # white tower vs shadowspawn
                    (this_or_next|eq, ":first_kingdom", "fac_kingdom_22"), # aiel vs shadowspawn
                    (eq, ":first_kingdom", "fac_kingdom_23"), # seanchan vs shadowspawn
                    (eq, ":second_kingdom", "fac_kingdom_24"),
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Modified for 118 - 120
                    (eq, ":first_kingdom", "fac_kingdom_21"), # white tower vs seanchan
                    (eq, ":second_kingdom", "fac_kingdom_23"),
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 95-118
                    (eq, ":first_kingdom", "fac_kingdom_23"),
                    (eq, ":second_kingdom", "fac_kingdom_26"), # seanchan vs sea folk
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 120 - 170
                    (eq, ":first_kingdom", "fac_kingdom_24"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_26"), # shadowspawn vs sea folk
                    (eq, ":second_kingdom", "fac_kingdom_28"), # shadowspawn vs toman head
                        (try_begin),
                        (gt, ":rel", -10),
                            (call_script, "script_diplomacy_start_war_between_kingdoms_silent", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),              


                    # Nations at Peace
                    (try_begin), # Modified for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_1"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_2"), # legion and band
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_3"), # legion and two rivers
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_4"), # legion and mayene
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_5"), # legion and cairhien
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_6"), # legion and illian
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_9"), # legion and arad doman
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_10"), # legion and tear
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # legion and andor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # legion and ghealdan
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # legion and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_22"), # legion and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Modified for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_2"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_3"), # band and two rivers
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_4"), # band and mayene
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_5"), # band and cairhien
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_6"), # band and illian
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_9"), # band and arad doman
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_10"), # band and tear
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # band and andor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # band and ghealdan
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # band and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_22"), # band and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Modified for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_3"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_4"), # two rivers and mayene
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_5"), # two rivers and cairhien
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_6"), # two rivers and illian
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_9"), # two rivers and arad doman
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_10"), # two rivers and tear
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # two rivers and andor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # two rivers and ghealdan
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # two rivers and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_22"), # two rivers and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_4"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_5"), # mayene and cairhien
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_6"), # mayene and illian
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_9"), # mayene and arad doman
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_10"), # mayene and tear
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # mayene and andor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # mayene and ghealdan
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # mayene and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_22"), # mayene and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_5"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_6"), # cairhien and illian
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_9"), # cairhien and arad doman
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_10"), # cairhien and tear
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # cairhien and andor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # cairhien and ghealdan
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # cairhien and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_22"), # cairhien and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_6"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_9"), # illian and arad doman
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_10"), # illian and tear
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # illian and andor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # illian and ghealdan
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # illian and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_22"), # illian and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),           

                    (try_begin), # Modified for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_8"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_14"), # altara and tarabon
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_15"), # altara and amadicia
                    (eq, ":second_kingdom", "fac_kingdom_23"), # altara and seanchan
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_9"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_10"), # arad doman and tear
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # arad doman and andor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # arad doman and ghealdan
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # arad doman and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_22"), # arad doman and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_10"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_11"), # tear and andor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # tear and ghealdan
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # tear and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_22"), # tear and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_11"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_12"), # andor and ghealdan
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # andor and whitecloaks
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_21"), # andor and white tower
                    (eq, ":second_kingdom", "fac_kingdom_22"), # andor and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_12"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_16"), # ghealdan and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_22"), # ghealdan and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),            

                    (try_begin), # Modified for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_14"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_15"), # tarabon and amadicia
                    (eq, ":second_kingdom", "fac_kingdom_23"), # tarabon and seanchan
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Modified for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_15"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_23"), # amadicia and whitecloaks
                    (eq, ":second_kingdom", "fac_kingdom_23"), # amadicia and seanchan
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # New for 95 - 118
                    (eq, ":first_kingdom", "fac_kingdom_16"),
                    (eq, ":second_kingdom", "fac_kingdom_22"), # whitecloaks and aiel
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),         

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_17"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_18"), # shienar and arafel
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_19"), # shienar and kandor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_20"), # shienar and saldaea
                    (eq, ":second_kingdom", "fac_kingdom_21"), # shienar and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_18"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_19"), # arafel and kandor
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_20"), # arafel and saldaea
                    (eq, ":second_kingdom", "fac_kingdom_21"), # arafel and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_19"),
                    (this_or_next|eq, ":second_kingdom", "fac_kingdom_20"), # kandor and saldaea
                    (eq, ":second_kingdom", "fac_kingdom_21"), # kandor and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),

                    (try_begin), # Original
                    (eq, ":first_kingdom", "fac_kingdom_20"),
                    (eq, ":second_kingdom", "fac_kingdom_21"), # saldaea and white tower
                        (try_begin),
                        (lt, ":rel", 10),
                            (call_script, "script_diplomacy_start_peace_between_kingdoms_tweaked", ":first_kingdom", ":second_kingdom", 1),
                            (assign, ":diplo_action_taken", 1),
                        (else_try),
                            (assign, ":diplo_action_taken", 1),
                        (try_end),
                    (try_end),                
        

                    # Nations who are Neutral - may squabble, but not actively warring (Default State)
                    (try_begin),
                    (eq, ":diplo_action_taken", 0),
                        (try_begin),
                        (neg|is_between, ":rel", -5, 6),
                            (call_script, "script_diplomacy_start_neutral_between_kingdoms", ":first_kingdom", ":second_kingdom", 1),
                        (try_end),
                    (try_end),          



                ## days past final bracket
                (try_end),

            ## try_for_range's final brackets
            (try_end),
        (try_end),        
    ]), 
## TGS: mat: End
  
# TGS Initialization
  (0.1, 0, ti_once, [(eq, "$g_tutorial_complete", 1)],
    [
        # Channeling Proficiency variable
        (assign, "$g_channeling_proficiency_modifier",0),
        (assign, "$g_day_number", 1),
    ]),

#display day number
  (24, 0, 0, [],
   [
        (assign, reg0, "$g_day_number"),
        (display_message, "@Day {reg0} ..."),
        (val_add, "$g_day_number", 1),
    ]),  

################## Timeline changes begin ##############

# Events at 10 days:
  (1, 24*10, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        (dialog_box, "str_tarwins_gap"),
    ]),

# Faction city and lord changes at 15 days:
  (1, 24*15, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Falme to Seanchan
        (call_script,"script_give_center_to_faction_aux", "p_town_7","fac_kingdom_23"),

        (dialog_box, "str_falme_falls"),
    ]),

# Faction city and lord changes at 20 days:
  (1, 24*20, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Falme to Toman Head
        (call_script,"script_give_center_to_faction_aux", "p_town_7","fac_kingdom_28"),

        (dialog_box, "str_falme_liberated"),
    ]),

# Faction city and lord changes at 25 days:
  (1, 24*25, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Tremalking Town to Seanchan
        (call_script,"script_give_center_to_faction_aux", "p_town_33","fac_kingdom_23"),

        (dialog_box, "str_seanchan_retreat"),
    ]),    

# Faction city and lord changes at 30 days:
  (1, 24*30, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Stone of Tear... King Darlin...to the Legion of the Dragon
        (call_script,"script_change_troop_faction","trp_kingdom_10_lord","fac_kingdom_1"),
        (call_script,"script_give_center_to_faction_aux", "p_castle_4","fac_kingdom_1"),
        #Tear... High Lord Torean... to the Legion of the Dragon, Tear to Rand al'Thor
        (call_script,"script_change_troop_faction","trp_knight_10_1","fac_kingdom_1"),
        (call_script,"script_give_center_to_faction_aux", "p_town_10","fac_kingdom_1"),
        (call_script,"script_give_center_to_lord","p_town_10","trp_kingdom_1_lord",1),
        #Culmarr Castle... High Lord Hearne... to the Legion of the Dragon
        (call_script,"script_change_troop_faction","trp_knight_10_2","fac_kingdom_1"),
        (call_script,"script_give_center_to_faction_aux", "p_castle_1","fac_kingdom_1"),
        #Slezkh Castle... High Lord Tolmeran... to the Legion of the Dragon
        (call_script,"script_change_troop_faction","trp_knight_10_6","fac_kingdom_1"),
        (call_script,"script_give_center_to_faction_aux", "p_castle_22","fac_kingdom_1"),

## Removed for splitting the factions (just make Mayene allied w/ Legion instead)        
        #Mayene... Berelain sur Paendrag Paeron... to the Legion of the Dragon
#        (call_script,"script_change_troop_faction","trp_knight_2_2","fac_kingdom_1"),
#        (call_script,"script_give_center_to_faction_aux", "p_town_12","fac_kingdom_1"),
        (call_script,"script_change_troop_faction","trp_knight_4_2","fac_kingdom_1"), # Captain Havien Nurelle
## End

        (dialog_box, "str_dragon_is_reborn_1"),
#        (dialog_box, "str_dragon_is_reborn_2"),

    ]),

  (1, 24*30+1, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
#        (dialog_box, "str_dragon_is_reborn_1"),
        (dialog_box, "str_dragon_is_reborn_2"),
    ]),

# Faction city and lord changes at 43 days:
  (1, 24*43, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Siuan Sedai is deposed... give Tar Valon to loyalist Aes Sedai
        (call_script,"script_give_center_to_lord","p_town_19","trp_knight_21_1",1), # Silviana (Mistress of Novices)

        (dialog_box, "str_siuan_deposed"),

    ]),

# Message to play at 45 days:
  (1, 24*45, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Rand al'Thor is recognized as Car'a'carn
        (dialog_box, "str_caracarn"),
    ]),

# Faction city and lord changes at 47 days:
  (1, 24*47, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Tanchico... Panarch Amathera Aelfdene...to the Seanchan Empire, Tanchico to Banner-General Furyk Karede
        (call_script,"script_change_troop_faction","trp_kingdom_14_lord","fac_kingdom_23"),
        (call_script,"script_give_center_to_faction_aux", "p_town_8","fac_kingdom_23"),
        (call_script,"script_give_center_to_lord","p_town_8","trp_knight_23_2",1),

        (dialog_box, "str_seanchan_invade_tarabon"),

    ]),

# Faction city and lord changes at 55 days:
  (1, 24*55, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Salidar... to the White Tower, to Lelaine Sedai
        (call_script,"script_give_center_to_faction_aux", "p_castle_34","fac_kingdom_21"),
        (call_script,"script_give_center_to_lord","p_castle_34","trp_knight_21_9",1),
        
        (dialog_box, "str_rebel_aes_sedai_to_salidar"),

    ]),

# Faction city and lord changes at 60 days:
  (1, 24*60, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Cairhien... Lord Dobraine Taborwin...to the Legion of the Dragon
        (call_script,"script_change_troop_faction","trp_knight_5_3","fac_kingdom_1"),
        (call_script,"script_give_center_to_faction_aux", "p_town_1","fac_kingdom_1"),
        #Haringoth Castle... Lady Selande Darengil... to the Legion of the Dragon
        (call_script,"script_change_troop_faction","trp_knight_5_4","fac_kingdom_1"),
        (call_script,"script_give_center_to_faction_aux", "p_castle_35","fac_kingdom_1"),
        #Tevarin Castle... Bertome Saighan... to the Legion of the Dragon
        (call_script,"script_change_troop_faction","trp_knight_5_7","fac_kingdom_1"),
        (call_script,"script_give_center_to_faction_aux", "p_castle_23","fac_kingdom_1"),

        (dialog_box, "str_dragon_takes_cairhien"),

    ]),

# Faction city and lord changes at 62 days:
  (1, 24*62, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Caemlyn... to the Legion of the Dragon, to Lord Davram Bashere (He joins from Saldaea)
        (call_script,"script_give_center_to_faction_aux", "p_town_3","fac_kingdom_1"),
        (call_script,"script_change_troop_faction","trp_knight_20_1","fac_kingdom_1"),
        (call_script,"script_give_center_to_lord","p_town_3","trp_knight_20_1",1),

        (dialog_box, "str_dragon_takes_caemlyn"),

    ]),

# Faction city and lord changes at 65 days:
  (1, 24*65, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Egwene al'Vere raised to rebel Amyrlin Seat... give her leadership of Salidar
        (call_script,"script_give_center_to_lord","p_castle_34","trp_kingdom_21_lord",1),

        (dialog_box, "str_rebel_aes_sedai_raise_egwene_to_amyrlin"),

    ]),

# Faction city and lord changes at 70 days:
  (1, 24*70, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Amador... to the Seanchan Empire... to Banner-General Gamel Loune
        (call_script,"script_give_center_to_faction_aux", "p_town_13","fac_kingdom_23"),
        (call_script,"script_give_center_to_lord","p_town_13","trp_knight_23_4",1),
        #Fortress of the Light... to the Seanchan Empire... to Banner-General Mikhel Najirah
        (call_script,"script_give_center_to_faction_aux", "p_castle_3","fac_kingdom_23"),
        (call_script,"script_give_center_to_lord","p_castle_3","trp_knight_23_5",1),
        #Bellon... High Inquisitor Rhadam Asunawa... to the Seanchan Empire
        (call_script,"script_change_troop_faction","trp_knight_16_1","fac_kingdom_23"),
        (call_script,"script_give_center_to_faction_aux", "p_castle_2","fac_kingdom_23"),
        #Sienda... to the Seanchan Empire... to Banner-General Efraim Yamada
        (call_script,"script_give_center_to_faction_aux", "p_castle_30","fac_kingdom_23"),
        (call_script,"script_give_center_to_lord","p_castle_30","trp_knight_23_7",1),
        #Grunwalder Castle... to the Seanchan Empire... to Lieutenant-General Abaldar Yulan
        (call_script,"script_give_center_to_faction_aux", "p_castle_28","fac_kingdom_23"),
        (call_script,"script_give_center_to_lord","p_castle_28","trp_knight_23_8",1),
        
        (dialog_box, "str_seanchan_invade_amadicia"),

    ]),

# Faction city and lord changes at 72 days:
  (1, 24*72, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Ebou Dar... King Beslan Mitsobar... to the Seanchan Empire... to Empress Fortuona Athaem Kore Paendrag
        (call_script,"script_change_troop_faction","trp_kingdom_8_lord","fac_kingdom_23"),
        (call_script,"script_give_center_to_faction_aux", "p_town_4","fac_kingdom_23"),
        (call_script,"script_give_center_to_lord","p_town_4","trp_kingdom_23_lord",1),
        #Alkindar... Altara Lord... to the Seanchan Empire... to King Beslan Mitsobar
        (call_script,"script_change_troop_faction","trp_knight_8_6","fac_kingdom_23"),
        (call_script,"script_give_center_to_faction_aux", "p_castle_25","fac_kingdom_23"),
        (call_script,"script_give_center_to_lord","p_castle_25","trp_kingdom_8_lord",1),
        #Jurador... Altara Lesser Lady... to the Seanchan Empire... to Altara Lord
        (call_script,"script_change_troop_faction","trp_knight_8_7","fac_kingdom_23"),
        (call_script,"script_give_center_to_faction_aux", "p_castle_36","fac_kingdom_23"),
        (call_script,"script_give_center_to_lord","p_castle_36","trp_knight_8_6",1),
        #Cormaed... Altara Lady... to the Seanchan Empire
        (call_script,"script_change_troop_faction","trp_knight_8_5","fac_kingdom_23"),
        (call_script,"script_give_center_to_faction_aux", "p_castle_32","fac_kingdom_23"),

        (dialog_box, "str_seanchan_invade_altara"),

    ]),

# Faction city and lord changes at 73 days:
  (1, 24*73, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Illian... Lord Ballin Elamri... to the Legion of the Dragon
        (call_script,"script_change_troop_faction","trp_knight_6_7","fac_kingdom_1"),
        (call_script,"script_give_center_to_faction_aux", "p_town_22","fac_kingdom_1"),
        (call_script,"script_give_center_to_lord","p_town_22","trp_knight_6_7",1),
        #Rindyar Castle... Lord Spiron Narettin... to the Legion of the Dragon
        (call_script,"script_change_troop_faction","trp_knight_6_3","fac_kingdom_1"),
        (call_script,"script_give_center_to_faction_aux", "p_castle_27","fac_kingdom_1"),

        (dialog_box, "str_dragon_takes_illian"),

    ]),

# Faction city and lord changes at 75 days:
  (1, 24*75, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Queen Alliandre of Ghealdan swears fealty
        (dialog_box, "str_queen_alliandra_swears_fealty"),
    ]),

# Faction city and lord changes at 77 days:
  (1, 24*77, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Caemlyn... to the Southlander Alliance... to Queen Elayne Trakand
        (call_script,"script_give_center_to_faction_aux", "p_town_3","fac_kingdom_11"),
        (call_script,"script_give_center_to_lord","p_town_3","trp_kingdom_11_lord",1),

        (dialog_box, "str_elayne_claims_andor_throne"),

    ]),

# Faction city and lord changes at 90 days:
  (1, 24*90, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Bandar Eban... to the Legion of the Dragon... to Davram Bashere
        (call_script,"script_give_center_to_faction_aux", "p_town_6","fac_kingdom_1"),
        (call_script,"script_give_center_to_lord","p_town_6","trp_knight_20_1",1),
        #Katar... Lord Rodel Ituralde... to the Legion of the Dragon
        (call_script,"script_change_troop_faction","trp_knight_9_1","fac_kingdom_1"),
        (call_script,"script_give_center_to_faction_aux", "p_castle_32","fac_kingdom_1"),

        (dialog_box, "str_dragon_takes_arad_doman"),

    ]),

# Faction city and lord changes at 95 days:
  (1, 24*95, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Rand begins preparing for the last battle
        (dialog_box, "str_dragon_prepares_for_last_battle"),
    ]),

# Faction city and lord changes at 100 days:
  (1, 24*100, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Egwene al'Vere unites the White Tower
        (call_script,"script_give_center_to_lord","p_town_19","trp_kingdom_21_lord",1),

        (dialog_box, "str_egwene_unites_white_tower"),

    ]),

# Faction city and lord changes at 115 days:
  (1, 24*115, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Last battle near
        (dialog_box, "str_last_battle_near"),
    ]),

# Faction city and lord changes at 120 days:
  (1, 24*120, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Chachin... to the Shadowspawn... to Moridin
        (call_script,"script_give_center_to_faction_aux", "p_town_17","fac_kingdom_24"),
        (call_script,"script_give_center_to_lord","p_town_17","trp_knight_24_1",1),
        #Shol Arbela... to the Shadowspawn... to Demandred
        (call_script,"script_give_center_to_faction_aux", "p_town_9","fac_kingdom_24"),
        (call_script,"script_give_center_to_lord","p_town_9","trp_knight_24_2",1),
        #Canluum... to the Shadowspawn... to Graendal
        (call_script,"script_give_center_to_faction_aux", "p_castle_19","fac_kingdom_24"),
        (call_script,"script_give_center_to_lord","p_castle_19","trp_knight_24_5",1),

        (dialog_box, "str_last_battle_begins"),

    ]),
################## Timeline changes end ##############

# Determine whether or not Channeling proficiency should rise after a battle:  # Equation 1 (Current channeling proficiency modifier is greater than (channeling level + 1)^3)  ## This is very aggressive at high Channeling levels
  (0.1, 0, 0, [## Effectively commented out the trigger since condition cannot be met
               (eq, "$g_tutorial_complete", 1),
               (eq, "$g_tutorial_complete", 0),],
   [
        #get player channeling proficiency...
        (store_proficiency_level,":proficiency_current","trp_player",wpt_firearm),
        #deterimine whether or not proficiency should rise
        (assign,":pro_cur_1",":proficiency_current"),
        (assign,":pro_cur_2",":proficiency_current"),
        (val_mul,":pro_cur_2",":pro_cur_2"),
        (val_mul,":pro_cur_1",":pro_cur_2"),
        (assign,":proficiency_base_measure",":pro_cur_1"),
        (try_begin),
            (lt,"$g_channeling_proficiency_modifier",":proficiency_base_measure"),
            (assign,"$g_channeling_proficiency_modifier",":proficiency_base_measure"),
        (else_try),
            (assign,":pro_next_1",":proficiency_current"),
            (val_add,":pro_next_1",1),
            (assign,":pro_next_2",":proficiency_current"),  ####this line not compiling for some reason
            (val_add,":pro_next_2",1),
            (val_mul,":pro_next_2",":pro_next_2"),
            (val_mul,":pro_next_1",":pro_next_2"),
            (assign,":proficiency_next_measure",":pro_next_1"),
            (try_begin),
                (gt,"$g_channeling_proficiency_modifier",":proficiency_next_measure"),
                (troop_raise_proficiency, "trp_player",wpt_firearm,1),
                (display_message,"str_channeling_proficiency_increases"),
            (try_end),
        (try_end),
    ]),

  # Give xp if channeling was used in battle
  # Determine whether or not Channeling proficiency should rise after a battle:  # Equation 2 (Current channeling proficiency modifier is greater than 2*(15*(channeling level + 1)^2 + 250*(channeling level + 1)))
  (0.1, 0, 0, [(eq, "$g_tutorial_complete", 1)],
   [
       # add xp check
       (try_begin),
       (gt, "$g_channeling_proficiency_modifier", "$g_channeling_proficiency_modifier_before"),
            (store_sub, ":difference", "$g_channeling_proficiency_modifier", "$g_channeling_proficiency_modifier_before"),
            (store_div, ":xp_gained", ":difference", 2),
            (add_xp_to_troop,":xp_gained","trp_player"),
            (display_message, "@Due to channeling..."),

            (assign, "$g_channeling_proficiency_modifier_before", "$g_channeling_proficiency_modifier"),
       (try_end),
       
        #get player channeling proficiency...
        (store_proficiency_level,":proficiency_current","trp_player",wpt_firearm),
        #deterimine whether or not proficiency should rise
        (store_mul, ":proficiency_current_squared", ":proficiency_current", ":proficiency_current"),
        (store_mul, ":pro_cur_1", 15, ":proficiency_current_squared"),
        (store_mul, ":pro_cur_2", 250, ":proficiency_current"),
        (store_add, ":pro_cur_add", ":pro_cur_1", ":pro_cur_2"),
        (store_mul, ":proficiency_base_measure", 2, ":pro_cur_add"),
        (try_begin),
            (lt,"$g_channeling_proficiency_modifier",":proficiency_base_measure"),
            (assign,"$g_channeling_proficiency_modifier",":proficiency_base_measure"),
            (assign, "$g_channeling_proficiency_modifier_before", "$g_channeling_proficiency_modifier"),
        (else_try),
            (store_add, ":proficiency_next", 1, ":proficiency_current"),
            (store_mul, ":proficiency_next_squared", ":proficiency_next", ":proficiency_next"),
            (store_mul, ":pro_next_1", 15, ":proficiency_next_squared"),
            (store_mul, ":pro_next_2", 250, ":proficiency_next"),
            (store_add, ":pro_next_add", ":pro_next_1", ":pro_next_2"),
            (store_mul, ":proficiency_next_measure", 2, ":pro_next_add"),
            (try_begin),
                (gt,"$g_channeling_proficiency_modifier",":proficiency_next_measure"),
                (troop_raise_proficiency, "trp_player",wpt_firearm,1),
                (display_message,"str_channeling_proficiency_increases"),
            (try_end),
        (try_end),
    ]),

# Basic Game messages for TGS

  # Welcome message
  (0, 0.1, ti_once, [(eq, "$g_tutorial_complete", 1)], [(dialog_box,"str_welcome_to_randland")]),

  # Help Menu
  (0, 0, 0, [(eq, "$g_tutorial_complete", 1)],
    [
        (try_begin),
        (key_clicked, key_h),  # start the remainder of the code when 'H' is clicked
            (dialog_box, "str_channeling_help"),
        (try_end),
   ]),

  # Learn Weave Triggers
  (0, 0.15, ti_once, [(this_or_next|eq,"$background_answer_2",cb_childhood_novice),
                      (eq,"$background_answer_2",cb_childhood_wilder),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 1),],[(dialog_box,"str_learn_weave_1")]),
  
  (0, 0.15, ti_once, [(this_or_next|eq,"$background_answer_2",cb_childhood_novice),
                      (eq,"$background_answer_2",cb_childhood_wilder),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 15),], [(dialog_box,"str_learn_weave_2")]),
  
  (0, 0.15, ti_once, [(this_or_next|eq,"$background_answer_2",cb_childhood_novice),
                      (eq,"$background_answer_2",cb_childhood_wilder),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 30),], [(dialog_box,"str_learn_weave_3")]),
  
  (0, 0.15, ti_once, [(this_or_next|eq,"$background_answer_2",cb_childhood_novice),
                      (eq,"$background_answer_2",cb_childhood_wilder),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 50),], [(dialog_box,"str_learn_weave_4")]),
  
  (0, 0.15, ti_once, [(this_or_next|eq,"$background_answer_2",cb_childhood_novice),
                      (eq,"$background_answer_2",cb_childhood_wilder),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 65),], [(dialog_box,"str_learn_weave_5")]),
  
  (0, 0.15, ti_once, [(this_or_next|eq,"$background_answer_2",cb_childhood_novice),
                      (eq,"$background_answer_2",cb_childhood_wilder),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 75),], [(dialog_box,"str_learn_weave_6")]),
  
  (0, 0.15, ti_once, [(this_or_next|eq,"$background_answer_2",cb_childhood_novice),
                      (eq,"$background_answer_2",cb_childhood_wilder),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 85),], [(dialog_box,"str_learn_weave_7")]),
  
  (0, 0.15, ti_once, [(this_or_next|eq,"$background_answer_2",cb_childhood_novice),
                      (eq,"$background_answer_2",cb_childhood_wilder),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 100),], [(dialog_box,"str_learn_weave_8")]),
  
  (0, 0.15, ti_once, [(this_or_next|eq,"$background_answer_2",cb_childhood_novice),
                      (eq,"$background_answer_2",cb_childhood_wilder),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 125),], [(dialog_box,"str_learn_weave_9")]),
  
  (0, 0.15, ti_once, [(this_or_next|eq,"$background_answer_2",cb_childhood_novice),
                      (eq,"$background_answer_2",cb_childhood_wilder),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 150),], [(dialog_box,"str_learn_weave_10")]),
  
  (0, 0.15, ti_once, [(this_or_next|eq,"$background_answer_2",cb_childhood_novice),
                      (eq,"$background_answer_2",cb_childhood_wilder),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 175),], [(dialog_box,"str_learn_weave_11")]),
  
  (0, 0.15, ti_once, [(this_or_next|eq,"$background_answer_2",cb_childhood_novice),
                      (eq,"$background_answer_2",cb_childhood_wilder),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 200),], [(dialog_box,"str_learn_weave_12")]),
  
  (0, 0.15, ti_once, [(this_or_next|eq,"$background_answer_2",cb_childhood_novice),
                      (eq,"$background_answer_2",cb_childhood_wilder),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 225),], [(dialog_box,"str_learn_weave_13")]),
  
  (0, 0.15, ti_once, [(this_or_next|eq,"$background_answer_2",cb_childhood_novice),
                      (eq,"$background_answer_2",cb_childhood_wilder),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 250),], [(dialog_box,"str_learn_weave_14")]),

  ## New main map hotkeys
        (0, 0, 0, [(eq, "$g_tutorial_complete", 1)],
         [
            ##Click 'M' to re-add One Power Item to inventory (Now this will only work if player is a channeler)
            (try_begin),
            (key_clicked, key_m),  # start the remainder of the code when 'M' is clicked
            (this_or_next|eq,"$background_answer_2",cb_childhood_novice),
            (eq,"$background_answer_2",cb_childhood_wilder),
                (troop_ensure_inventory_space, "trp_player", 1),
                (troop_add_item, "trp_player", "itm_power_player", 0),
            (try_end),

        ]),

  ## Trigger to update channeling proficiency slot for npc companions
        (0, 0.1, 0, [(eq, "$g_tutorial_complete", 1)],
         [
             (try_for_range, ":troop_no", companions_begin, companions_end),
                 (store_proficiency_level,":channeling_proficiency",":troop_no",wpt_firearm),
                 (try_begin),
                    (lt, ":channeling_proficiency", 15),
                        (assign, ":known_weaves", 1),
                    (else_try),
                    (is_between, ":channeling_proficiency", 15, 30),
                        (assign, ":known_weaves", 2),
                    (else_try),
                    (is_between, ":channeling_proficiency", 30, 45),
                        (assign, ":known_weaves", 3),
                    (else_try),
                    (is_between, ":channeling_proficiency", 45, 60),
                        (assign, ":known_weaves", 4),
                    (else_try),
                    (is_between, ":channeling_proficiency", 60, 80),
                        (assign, ":known_weaves", 5),
                    (else_try),
                    (is_between, ":channeling_proficiency", 80, 100),
                        (assign, ":known_weaves", 6),
                    (else_try),
                    (is_between, ":channeling_proficiency", 100, 125),
                        (assign, ":known_weaves", 7),
                    (else_try),
                    (is_between, ":channeling_proficiency", 125, 150),
                        (assign, ":known_weaves", 8),
                    (else_try),
                    (is_between, ":channeling_proficiency", 150, 175),
                        (assign, ":known_weaves", 9),
                    (else_try),
                    (is_between, ":channeling_proficiency", 175, 200),
                        (assign, ":known_weaves", 10),
                    (else_try),
                    (ge, ":channeling_proficiency", 200),
                        (assign, ":known_weaves", 11),
                    (try_end),
                 (troop_set_slot, ":troop_no", slot_troop_npc_companion_known_weaves, ":known_weaves"),
             (try_end),
        ]),  

  ## New main map testing hotkeys HACK: make sure this doesn't work in non-development versions
        (0, 0, 0, [(eq, "$g_tutorial_complete", 1), #  to enable cheats, remove the second line in the condition
                   #(eq, "$g_tutorial_complete", 0),
                   ],
         [
            ##Click 'K' to add troops to hero party
            (try_begin),
            (key_clicked, key_k),  # start the remainder of the code when 'K' is clicked
                (try_for_parties, ":party"),
                    (assign, ":player_check", 0),
                    (party_count_members_of_type, ":player_check", ":party", "trp_player"),
                    (try_begin),
                    (gt, ":player_check", 0),
                        (try_begin),
                        (eq, "$g_cheat_recruit_add", 1),

#                            (party_add_members, ":party", "trp_ashaman_soldier", 10),
                            (party_add_members, ":party", "trp_ashaman_dedicated", 10),
#                            (party_add_members, ":party", "trp_ashaman", 2),
            
#                            (party_add_members, ":party", "trp_legion_recruit_army", 2),
#                            (party_add_members, ":party", "trp_legion_footman", 2),
#                            (party_add_members, ":party", "trp_legion_infantry", 2),
#                            (party_add_members, ":party", "trp_legion_swordsman", 2),
#                            (party_add_members, ":party", "trp_legion_pikeman", 2),
#                            (party_add_members, ":party", "trp_legion_crossbowman", 2),
#                            (party_add_members, ":party", "trp_legion_cavalry", 2),
#                            (party_add_members, ":party", "trp_legion_lancer", 2),
#                            (party_add_members, ":party", "trp_legion_man_at_arms", 2),

#                            (party_add_members, ":party", "trp_ashaman_veteran", 4),
#                            (party_add_members, ":party", "trp_legion_blademaster", 4),
#                            (party_add_members, ":party", "trp_legion_bannerman", 4),
#                            (party_add_members, ":party", "trp_legion_heavy_crossbowman", 4),
#                            (party_add_members, ":party", "trp_legion_heavy_lancer", 4),
#                            (party_add_members, ":party", "trp_legion_captain", 4),

#                            (party_add_members, ":party", "trp_red_hand_recruit", 3),
#                            (party_add_members, ":party", "trp_red_hand_infantry", 3),
#                            (party_add_members, ":party", "trp_red_hand_pikeman", 3),
#                            (party_add_members, ":party", "trp_red_hand_crossbowman", 3),
#                            (party_add_members, ":party", "trp_red_hand_man_at_arms", 3),            
#                            (party_add_members, ":party", "trp_red_hand_light_cavalry", 3),
            
#                            (party_add_members, ":party", "trp_red_hand_bannerman", 4),
#                            (party_add_members, ":party", "trp_red_hand_swordsman", 4),
#                            (party_add_members, ":party", "trp_red_hand_fast_crossbowman", 10),
#                            (party_add_members, ":party", "trp_red_hand_lancer", 4),
#                            (party_add_members, ":party", "trp_red_hand_captain", 4),
#                            (party_add_members, ":party", "trp_red_hand_skirmisher", 4),

#                            (party_add_members, ":party", "trp_two_rivers_farmer", 5),
#                            (party_add_members, ":party", "trp_two_rivers_spearman", 5),
#                            (party_add_members, ":party", "trp_two_rivers_longbowman", 5),
            
#                            (party_add_members, ":party", "trp_two_rivers_halberdier", 10),
#                            (party_add_members, ":party", "trp_two_rivers_scout", 10),
#                            (party_add_members, ":party", "trp_two_rivers_marksman", 10),
            # HACK for npc companions
#            (party_add_members, ":party", "trp_npc1",1),
#            (party_add_members, ":party", "trp_npc2",1),
#            (party_add_members, ":party", "trp_npc3",1),
#            (party_add_members, ":party", "trp_npc4",1),
#            (party_add_members, ":party", "trp_npc5",1),
#            (party_add_members, ":party", "trp_npc6",1),
#            (party_add_members, ":party", "trp_npc7",1),
#            (party_add_members, ":party", "trp_npc8",1),
#            (party_add_members, ":party", "trp_npc9",1),
#            (party_add_members, ":party", "trp_npc10",1),
#            (party_add_members, ":party", "trp_npc11",1),
#            (party_add_members, ":party", "trp_npc12",1),
#            (party_add_members, ":party", "trp_npc13",1),
#            (party_add_members, ":party", "trp_npc14",1),
#            (party_add_members, ":party", "trp_npc15",1),
#            (party_add_members, ":party", "trp_npc16",1),

            
            ## Hack for Shara
#            (party_add_members, ":party", "trp_shara_recruit",2),
#            (party_add_members, ":party", "trp_shara_armsman",2),
#            (party_add_members, ":party", "trp_shara_town_guard",2),
#            (party_add_members, ":party", "trp_shara_border_guard",2),
#            (party_add_members, ":party", "trp_shara_swordsman",2),
#            (party_add_members, ":party", "trp_shara_bowman",2),
#            (party_add_members, ":party", "trp_shara_scout",2),
#            (party_add_members, ":party", "trp_shara_man_at_arms",5),
#            (party_add_members, ":party", "trp_ayyad_villager",2),
#            (party_add_members, ":party", "trp_ayyad_village_leader",2),
#            (party_add_members, ":party", "trp_shara_defender",2),
#            (party_add_members, ":party", "trp_shara_captain",2),
#            (party_add_members, ":party", "trp_shara_marksman",2),
#            (party_add_members, ":party", "trp_shara_crossbowman",2),
#            (party_add_members, ":party", "trp_shara_shbo_guardsman",2),
#            (party_add_members, ":party", "trp_shara_skirmisher",5),
#            (party_add_members, ":party", "trp_ayyad_counsel_member",2),

            ## Hack for Sea Folk
#            (party_add_members, ":party", "trp_sea_folk_recruit",3),
#            (party_add_members, ":party", "trp_sea_folk_bilge_hand",3),
#            (party_add_members, ":party", "trp_sea_folk_deck_hand",3),
#            (party_add_members, ":party", "trp_sea_folk_boatswain",3),
#            (party_add_members, ":party", "trp_sea_folk_dogwatcher",3),
#            (party_add_members, ":party", "trp_sea_folk_weatherly",3),
#            (party_add_members, ":party", "trp_sea_folk_quarterling",3),
#            (party_add_members, ":party", "trp_sea_folk_sailmistress",3),
#            (party_add_members, ":party", "trp_sea_folk_recruit_channeler",3),
#            (party_add_members, ":party", "trp_sea_folk_pupil",3),
#            (party_add_members, ":party", "trp_sea_folk_cargomaster",3),
#            (party_add_members, ":party", "trp_sea_folk_deck_defender",3),
#            (party_add_members, ":party", "trp_sea_folk_wavemistress",3),
#            (party_add_members, ":party", "trp_sea_folk_windfinder",3),

            ## Hack for Land of Madmen
#            (party_add_members, ":party", "trp_madmen_recruit",2),
#            (party_add_members, ":party", "trp_madmen_wanderer",2),
#            (party_add_members, ":party", "trp_madmen_villager",2),
#            (party_add_members, ":party", "trp_madmen_clansman",2),
#            (party_add_members, ":party", "trp_madmen_looter",2),
#            (party_add_members, ":party", "trp_madmen_hunter",2),
#            (party_add_members, ":party", "trp_madmen_ambusher",2),
#            (party_add_members, ":party", "trp_madmen_horse_tamer",2),
#            (party_add_members, ":party", "trp_madmen_slave_catcher",2),
#            (party_add_members, ":party", "trp_madmen_air_shifter",2),
#            (party_add_members, ":party", "trp_madmen_fire_tamer",2),
#            (party_add_members, ":party", "trp_madmen_chieftan",2),
#            (party_add_members, ":party", "trp_madmen_pillager",2),
#            (party_add_members, ":party", "trp_madmen_assassin",2),
#            (party_add_members, ":party", "trp_madmen_thunderhoof",2),
#            (party_add_members, ":party", "trp_madmen_plains_rider",2),
#            (party_add_members, ":party", "trp_madmen_storm_caller",2),
            
            ## Hack for Toman Head
#            (party_add_members, ":party", "trp_toman_head_recruit",8),
#            (party_add_members, ":party", "trp_toman_head_footman",8),
#            (party_add_members, ":party", "trp_toman_head_city_guard",8),
#            (party_add_members, ":party", "trp_toman_head_bowman",8),
#            (party_add_members, ":party", "trp_toman_head_scout",8), 


            

                        (else_try),
                        (eq, "$g_cheat_recruit_add", 2),
            
#                            (party_add_members, ":party", "trp_mayene_recruit", 5),
#                            (party_add_members, ":party", "trp_mayene_militia", 5),
#                            (party_add_members, ":party", "trp_mayene_man_at_arms", 5),
#                            (party_add_members, ":party", "trp_mayene_lancer", 5),
            
#                            (party_add_members, ":party", "trp_mayene_swordsman", 5),
#                            (party_add_members, ":party", "trp_mayene_bowman", 5),
#                            (party_add_members, ":party", "trp_mayene_royal_guard", 5),

#                            (party_add_members, ":party", "trp_cairhien_recruit", 5),
#                            (party_add_members, ":party", "trp_cairhien_militia", 5),
#                            (party_add_members, ":party", "trp_cairhien_pikeman", 5),
#                            (party_add_members, ":party", "trp_cairhien_man_at_arms", 5),
            
#                            (party_add_members, ":party", "trp_cairhien_crossbowman", 5),
#                            (party_add_members, ":party", "trp_cairhien_bannerman", 5),
#                            (party_add_members, ":party", "trp_cairhien_light_cavalry", 5),
#                            (party_add_members, ":party", "trp_cairhien_lancer", 5),

#                            (party_add_members, ":party", "trp_illian_recruit", 5),
#                            (party_add_members, ":party", "trp_illian_militia", 5),
#                            (party_add_members, ":party", "trp_illian_swordsman", 5),
#                            (party_add_members, ":party", "trp_illian_companion", 55),
#                            (party_add_members, ":party", "trp_illian_bowman", 5),
#                            (party_add_members, ":party", "trp_illian_crossbowman", 5),
#                            (party_add_members, ":party", "trp_illian_scout", 5),
            
#                            (party_add_members, ":party", "trp_illian_companion_captain", 5),
#                            (party_add_members, ":party", "trp_illian_marksman", 5),
#                            (party_add_members, ":party", "trp_illian_man_at_arms", 5),

#                            (party_add_members, ":party", "trp_murandy_recruit", 5),
#                            (party_add_members, ":party", "trp_murandy_militia", 5),
#                            (party_add_members, ":party", "trp_murandy_maceman", 5),
#                            (party_add_members, ":party", "trp_murandy_bowman", 5),
#                            (party_add_members, ":party", "trp_murandy_scout", 5),
#                            (party_add_members, ":party", "trp_murandy_lancer", 5),
            
#                            (party_add_members, ":party", "trp_murandy_berserker", 5),
#                            (party_add_members, ":party", "trp_murandy_marksman", 5),
#                            (party_add_members, ":party", "trp_murandy_captain", 5),

#                            (party_add_members, ":party", "trp_altara_recruit", 5),
#                            (party_add_members, ":party", "trp_altara_dueler", 5),
#                            (party_add_members, ":party", "trp_altara_swordsman", 5),
#                            (party_add_members, ":party", "trp_altara_scout53),
            
#                            (party_add_members, ":party", "trp_altara_royal_guard", 5),
#                            (party_add_members, ":party", "trp_altara_knife_thrower", 5),
#                            (party_add_members, ":party", "trp_altara_man_at_arms", 5),
#                            (party_add_members, ":party", "trp_altara_skirmisher", 5),

#                            (party_add_members, ":party", "trp_arad_doman_recruit", 5),
#                            (party_add_members, ":party", "trp_arad_doman_rabble", 5),
#                            (party_add_members, ":party", "trp_arad_doman_swordsman", 5),
#                            (party_add_members, ":party", "trp_arad_doman_scout", 5),
            
#                            (party_add_members, ":party", "trp_arad_doman_long_swordsman", 5),
#                            (party_add_members, ":party", "trp_arad_doman_bowman", 5),
#                            (party_add_members, ":party", "trp_arad_doman_man_at_arms", 5),
                        (else_try),
                        (eq, "$g_cheat_recruit_add", 3),
            
#                            (party_add_members, ":party", "trp_tear_recruit", 5),
#                            (party_add_members, ":party", "trp_tear_town_watch", 5),
#                            (party_add_members, ":party", "trp_tear_swordsman", 5),
#                            (party_add_members, ":party", "trp_tear_defender", 5),
#                            (party_add_members, ":party", "trp_tear_bowman", 5),
#                            (party_add_members, ":party", "trp_tear_scout", 5),
#                            (party_add_members, ":party", "trp_tear_lancer", 5),
            
#                            (party_add_members, ":party", "trp_tear_blademaster", 5),
#                            (party_add_members, ":party", "trp_tear_defender_captain", 5),
#                            (party_add_members, ":party", "trp_tear_crossbowman", 5),
#                            (party_add_members, ":party", "trp_tear_light_cavalry", 5),
#                            (party_add_members, ":party", "trp_tear_heavy_lancer", 5),

#                            (party_add_members, ":party", "trp_andor_recruit", 5),
#                            (party_add_members, ":party", "trp_andor_militia", 5),
#                            (party_add_members, ":party", "trp_andor_swordsman", 5),
#                            (party_add_members, ":party", "trp_andor_bowman", 5),
#                            (party_add_members, ":party", "trp_andor_scout", 5),
#                            (party_add_members, ":party", "trp_andor_lancer", 5),
#                            (party_add_members, ":party", "trp_andor_queens_guard", 5),
            
#                            (party_add_members, ":party", "trp_andor_blademaster", 5),
#                            (party_add_members, ":party", "trp_andor_halberdier", 5),
#                            (party_add_members, ":party", "trp_andor_crossbowman", 5),
#                            (party_add_members, ":party", "trp_andor_man_at_arms", 5),
#                            (party_add_members, ":party", "trp_andor_bannerman", 5),

#                            (party_add_members, ":party", "trp_ghealdan_recruit", 5),
#                            (party_add_members, ":party", "trp_ghealdan_militia", 5),
#                            (party_add_members, ":party", "trp_ghealdan_axeman", 5),
#                            (party_add_members, ":party", "trp_ghealdan_bowman", 5),
#                            (party_add_members, ":party", "trp_ghealdan_scout", 5),
#                            (party_add_members, ":party", "trp_ghealdan_lancer", 5),
            
#                            (party_add_members, ":party", "trp_ghealdan_heavy_axeman", 10),
#                            (party_add_members, ":party", "trp_ghealdan_marksman", 5),
#                            (party_add_members, ":party", "trp_ghealdan_man_at_arms", 5),
#                            (party_add_members, ":party", "trp_ghealdan_royal_guard", 10),

#                            (party_add_members, ":party", "trp_far_madding_recruit", 10),
#                            (party_add_members, ":party", "trp_far_madding_footman", 10),
            
#                            (party_add_members, ":party", "trp_far_madding_city_guard", 20),
#                            (party_add_members, ":party", "trp_far_madding_crossbowman", 20),

#                            (party_add_members, ":party", "trp_tarabon_recruit", 5),
#                            (party_add_members, ":party", "trp_tarabon_rabble", 5),
#                            (party_add_members, ":party", "trp_tarabon_bowman", 5),
#                            (party_add_members, ":party", "trp_tarabon_scout", 5),

#                            (party_add_members, ":party", "trp_tarabon_spearman", 10),
#                            (party_add_members, ":party", "trp_tarabon_marksman", 10),
#                            (party_add_members, ":party", "trp_tarabon_lancer", 10),
#                            (party_add_members, ":party", "trp_tarabon_skirmisher", 10),

#                            (party_add_members, ":party", "trp_amadicia_militia", 3),
#                            (party_add_members, ":party", "trp_amadicia_pikeman", 5),
#                            (party_add_members, ":party", "trp_amadicia_bowman", 5),
            
#                            (party_add_members, ":party", "trp_amadicia_captain", 5),
#                            (party_add_members, ":party", "trp_amadicia_skirmisher", 5),
            
#                            (party_add_members, ":party", "trp_whitecloak_recruit", 2),
#                            (party_add_members, ":party", "trp_whitecloak_footman", 3),
#                            (party_add_members, ":party", "trp_whitecloak_swordsman", 5),
#                            (party_add_members, ":party", "trp_whitecloak_bowman", 5),
#                            (party_add_members, ":party", "trp_whitecloak_man_at_arms", 5),

#                            (party_add_members, ":party", "trp_whitecloak_captain", 5),
#                            (party_add_members, ":party", "trp_whitecloak_crossbowman", 5),
#                            (party_add_members, ":party", "trp_whitecloak_lancer", 5),
                        (else_try),
                        (eq, "$g_cheat_recruit_add", 4),
            
#                            (party_add_members, ":party", "trp_shienar_recruit", 2),
#                            (party_add_members, ":party", "trp_shienar_militia", 3),
#                            (party_add_members, ":party", "trp_shienar_spearman", 5),
#                            (party_add_members, ":party", "trp_shienar_swordsman", 5),
#                            (party_add_members, ":party", "trp_shienar_bowman", 5),
#                            (party_add_members, ":party", "trp_shienar_light_cavalry", 5),
#                            (party_add_members, ":party", "trp_shienar_lancer", 5),
#                            (party_add_members, ":party", "trp_shienar_heavy_lancer", 5),
            
#                            (party_add_members, ":party", "trp_shienar_pikeman", 5),
#                            (party_add_members, ":party", "trp_shienar_blademaster", 5),
#                            (party_add_members, ":party", "trp_shienar_marksman", 5),
#                            (party_add_members, ":party", "trp_shienar_crossbowman", 5),
#                            (party_add_members, ":party", "trp_shienar_captain", 5),

#                            (party_add_members, ":party", "trp_arafel_recruit", 2),
#                            (party_add_members, ":party", "trp_arafel_militia", 3),
#                            (party_add_members, ":party", "trp_arafel_swordsman", 5),
#                            (party_add_members, ":party", "trp_arafel_halberdier", 5),
#                            (party_add_members, ":party", "trp_arafel_bowman", 5),
#                            (party_add_members, ":party", "trp_arafel_man_at_arms", 5),
            
#                            (party_add_members, ":party", "trp_arafel_blademaster", 10),
#                            (party_add_members, ":party", "trp_arafel_bannerman", 10),
#                            (party_add_members, ":party", "trp_arafel_marksman", 5),
#                            (party_add_members, ":party", "trp_arafel_lancer", 5),
#                            (party_add_members, ":party", "trp_arafel_skirmisher", 5),

#                            (party_add_members, ":party", "trp_kandor_recruit", 2),
#                            (party_add_members, ":party", "trp_kandor_militia", 3),
#                            (party_add_members, ":party", "trp_kandor_axeman", 50),
#                            (party_add_members, ":party", "trp_kandor_berserker", 5),
#                            (party_add_members, ":party", "trp_kandor_bowman", 5),
#                            (party_add_members, ":party", "trp_kandor_man_at_arms", 5),
            
#                            (party_add_members, ":party", "trp_kandor_captain", 10),
#                            (party_add_members, ":party", "trp_kandor_maceman", 10),
#                            (party_add_members, ":party", "trp_kandor_crossbowman", 5),
#                            (party_add_members, ":party", "trp_kandor_heavy_horseman", 5),
#                            (party_add_members, ":party", "trp_kandor_skirmisher", 5),

#                            (party_add_members, ":party", "trp_saldaea_recruit", 2),
#                            (party_add_members, ":party", "trp_saldaea_militia", 3),
#                            (party_add_members, ":party", "trp_saldaea_swordsman", 5),
#                            (party_add_members, ":party", "trp_saldaea_bowman", 5),
#                            (party_add_members, ":party", "trp_saldaea_cavalry", 5),
#                            (party_add_members, ":party", "trp_saldaea_light_cavalry", 5),
#                            (party_add_members, ":party", "trp_saldaea_elite_light_cavalry", 5),
#                            (party_add_members, ":party", "trp_saldaea_skirmisher", 5),
            
#                            (party_add_members, ":party", "trp_saldaea_bannerman", 5),
#                            (party_add_members, ":party", "trp_saldaea_halberdier", 5),
#                            (party_add_members, ":party", "trp_saldaea_marksman", 5),
                            (party_add_members, ":party", "trp_saldaea_quartermaster", 100),
#                            (party_add_members, ":party", "trp_saldaea_elite_skirmisher", 5),
                        (else_try),
                        (eq, "$g_cheat_recruit_add", 5),
            
                            (party_add_members, ":party", "trp_aes_sedai_green", 1),
                            (party_add_members, ":party", "trp_aes_sedai_red", 1),#                            (party_add_members, ":party", "trp_aes_sedai_yellow", 1),
                            (party_add_members, ":party", "trp_aes_sedai_blue", 1),
                            (party_add_members, ":party", "trp_aes_sedai_white", 1),
                            (party_add_members, ":party", "trp_aes_sedai_brown", 1),
                            (party_add_members, ":party", "trp_aes_sedai_grey", 1),
            
                            (party_add_members, ":party", "trp_aes_sedai_green_veteran", 1),
                            (party_add_members, ":party", "trp_aes_sedai_red_veteran", 1),
                            (party_add_members, ":party", "trp_aes_sedai_yellow_veteran", 1),
                            (party_add_members, ":party", "trp_aes_sedai_blue_veteran", 1),
                            (party_add_members, ":party", "trp_aes_sedai_white_veteran", 1),
                            (party_add_members, ":party", "trp_aes_sedai_brown_veteran", 1),
                            (party_add_members, ":party", "trp_aes_sedai_grey_veteran", 1),

#                            (party_add_members, ":party", "trp_novice_social", 1),
#                            (party_add_members, ":party", "trp_novice_civil", 1),
#                            (party_add_members, ":party", "trp_accepted_medical", 1),
#                            (party_add_members, ":party", "trp_accepted_academic", 1),
#                            (party_add_members, ":party", "trp_accepted_political", 1),
#                            (party_add_members, ":party", "trp_accepted_military", 1),
            
#                            (party_add_members, ":party", "trp_tar_valon_street_patrol", 2),
#                            (party_add_members, ":party", "trp_tower_guard_infantry", 2),
#                            (party_add_members, ":party", "trp_tower_guard_captain", 2),
#                            (party_add_members, ":party", "trp_tower_guard_crossbowman", 2),
#                            (party_add_members, ":party", "trp_warder_trainee", 2),
#                            (party_add_members, ":party", "trp_youngling_infantry", 2),
#                            (party_add_members, ":party", "trp_youngling_cavalry", 2),
                        (else_try),
                        (eq, "$g_cheat_recruit_add", 6),

                            (party_add_members, ":party", "trp_aiel_recruit_channeler", 2),
                            (party_add_members, ":party", "trp_wise_one_apprentice", 2),
                            (party_add_members, ":party", "trp_wise_one", 2),
                            (party_add_members, ":party", "trp_wise_one_dream_walker", 2),
            
#                            (party_add_members, ":party", "trp_aiel_recruit_soldier", 1),
#                            (party_add_members, ":party", "trp_aiel_recruit_lithe", 2),
#                            (party_add_members, ":party", "trp_aiel_raider", 2),
#                            (party_add_members, ":party", "trp_aiel_recruit_athletic", 2),
#                            (party_add_members, ":party", "trp_aiel_runner", 2),
#                            (party_add_members, ":party", "trp_aiel_scout", 2),
#                            (party_add_members, ":party", "trp_aiel_recruit_bulky", 2),
#                            (party_add_members, ":party", "trp_aiel_enforcer", 2),
#                            (party_add_members, ":party", "trp_aiel_recruit_warrior", 2),
#                            (party_add_members, ":party", "trp_aiel_brute", 2),
#                            (party_add_members, ":party", "trp_aiel_grappler", 2), #30

#                            (party_add_members, ":party", "trp_knife_hand", 2),
#                            (party_add_members, ":party", "trp_night_spear", 2),
#                            (party_add_members, ":party", "trp_dawn_runner", 2),
#                            (party_add_members, ":party", "trp_mountain_dancer", 2),
#                            (party_add_members, ":party", "trp_maiden_of_the_spear", 2),
#                            (party_add_members, ":party", "trp_water_seeker", 2),
#                            (party_add_members, ":party", "trp_stone_dog", 3),
#                            (party_add_members, ":party", "trp_red_shield", 3),
#                            (party_add_members, ":party", "trp_brother_of_the_eagle", 3),
#                            (party_add_members, ":party", "trp_brotherless", 3),
#                            (party_add_members, ":party", "trp_black_eye", 3),
#                            (party_add_members, ":party", "trp_true_blood", 3),
                        (else_try),
                        (eq, "$g_cheat_recruit_add", 7),

#                            (party_add_members, ":party", "trp_seanchan_recruit_channeler", 2),
#                            (party_add_members, ":party", "trp_suldam", 1),
                            (party_add_members, ":party", "trp_der_suldam", 15),
            
#                            (party_add_members, ":party", "trp_seanchan_recruit_soldier", 2),
#                            (party_add_members, ":party", "trp_seanchan_armsman", 2),
#                            (party_add_members, ":party", "trp_seanchan_footman", 2),
#                            (party_add_members, ":party", "trp_seanchan_swordsman", 2),
#                            (party_add_members, ":party", "trp_seanchan_blademaster", 2),
#                            (party_add_members, ":party", "trp_seanchan_pikeman", 2),
#                            (party_add_members, ":party", "trp_seanchan_archer", 2),
#                            (party_add_members, ":party", "trp_seanchan_scout", 2),
#                            (party_add_members, ":party", "trp_seanchan_man_at_arms", 2),
#                            (party_add_members, ":party", "trp_seanchan_lancer", 2),
            
#                            (party_add_members, ":party", "trp_seanchan_deathwatch_guard", 4),
#                            (party_add_members, ":party", "trp_seanchan_halberdier", 4),
#                            (party_add_members, ":party", "trp_seanchan_marksman", 4),
#                            (party_add_members, ":party", "trp_seanchan_crossbowman", 4),
#######                            (party_add_members, ":party", "trp_seanchan_morat_torm", 2),
#                            (party_add_members, ":party", "trp_seanchan_captain", 4),
#                            (party_add_members, ":party", "trp_seanchan_skirmisher", 4),
            
#                            (party_add_members, ":party", "trp_seanchan_tarabon_ally", 1),
#                            (party_add_members, ":party", "trp_seanchan_amadicia_ally", 1),
#                            (party_add_members, ":party", "trp_seanchan_altara_ally", 1),
                        (else_try),
                        (eq, "$g_cheat_recruit_add", 8),
            
#                            (party_add_members, ":party", "trp_shadowspawn_recruit_creature", 2),
#                            (party_add_members, ":party", "trp_trolloc_grunt", 2),
#                            (party_add_members, ":party", "trp_trolloc_hewer", 2),
#                            (party_add_members, ":party", "trp_trolloc_berserker", 2),
                            (party_add_members, ":party", "trp_trolloc_clan_chief", 50),
#                            (party_add_members, ":party", "trp_myrddraal", 30),
#                            (party_add_members, ":party", "trp_trolloc_archer", 2),
#                            (party_add_members, ":party", "trp_trolloc_stalker", 2),
                            (party_add_members, ":party", "trp_draghkar", 50),
            
#                            (party_add_members, ":party", "trp_darkfriend_channeler", 4),
#                            (party_add_members, ":party", "trp_aes_sedai_black", 4),
#                            (party_add_members, ":party", "trp_dreadlord", 4),
#                            (party_add_members, ":party", "trp_darkfriend_initiate", 4),
#                            (party_add_members, ":party", "trp_darkfriend_murderer", 4),
#                            (party_add_members, ":party", "trp_darkfriend_assassin", 4),
#                            (party_add_members, ":party", "trp_darkfriend_ambusher", 4),
#                            (party_add_members, ":party", "trp_darkfriend_leader", 4),
#                            (party_add_members, ":party", "trp_darkfriend_marksman", 4),
                        (try_end),
                    (try_end),
                (try_end),
            (try_end),

            ##Click 'O' to add xp to hero party
            (try_begin),
            (key_clicked, key_o),  # start the remainder of the code when 'O' is clicked
                (try_for_parties, ":party"),
                    (assign, ":player_check", 0),
                    (party_count_members_of_type, ":player_check", ":party", "trp_player"),
                    (try_begin),
                    (gt, ":player_check", 0),
                        (party_add_xp, ":party", 100000),
                    (try_end),
                (try_end),
            (try_end),

            ##Click 'N' to add gold to player
            (try_begin),
            (key_clicked, key_n),  # start the remainder of the code when 'N' is clicked
                (troop_add_gold, "trp_player", 10000),
            (try_end),

            ##Click 'J' to toggle which faction recruits to add
            (try_begin),
            (key_clicked, key_j),  # start the remainder of the code when 'J' is clicked
                (try_begin),
                (eq, "$g_cheat_recruit_add", 1),
                    (assign, "$g_cheat_recruit_add", 2),
                    (display_message, "@Southlander Coalition..."),
                (else_try),
                (eq, "$g_cheat_recruit_add", 2),
                    (assign, "$g_cheat_recruit_add", 3),
                    (display_message, "@Southlander Alliance..."),
                (else_try),
                (eq, "$g_cheat_recruit_add", 3),
                    (assign, "$g_cheat_recruit_add", 4),
                    (display_message, "@Borderlands..."),
                (else_try),
                (eq, "$g_cheat_recruit_add", 4),
                    (assign, "$g_cheat_recruit_add", 5),
                    (display_message, "@White Tower..."),
                (else_try),
                (eq, "$g_cheat_recruit_add", 5),
                    (assign, "$g_cheat_recruit_add", 6),
                    (display_message, "@Aiel..."),
                (else_try),
                (eq, "$g_cheat_recruit_add", 6),
                    (assign, "$g_cheat_recruit_add", 7),
                    (display_message, "@Seanchan..."),
                (else_try),
                (eq, "$g_cheat_recruit_add", 7),
                    (assign, "$g_cheat_recruit_add", 8),
                    (display_message, "@Shadowspawn..."),
                    (else_try),
                (eq, "$g_cheat_recruit_add", 8),
                    (assign, "$g_cheat_recruit_add", 1),
                    (display_message, "@Legion..."),
                (try_end),
            (try_end),

        ]),

## TGS: mat: DEGUG: Add Sea Battles

(0.1, 0, 0, [(party_get_current_terrain,":terrain","p_main_party"),
      (assign, reg1,":terrain"),],
   [#(try_begin),  # it seems like this shouldn't be there so I'll remove for now
     (troop_get_inventory_slot, ":cur_horse", "trp_player", 8), #horse slot
     (assign, ":new_icon", -1),
     (try_begin),
       (eq,reg1,7), # 7 = rt_bridge
       (assign, ":new_icon", "icon_ship"),
      #(display_message,"@water"),
     (else_try),
       (eq, "$g_player_icon_state", pis_normal),
       (try_begin),
         (ge, ":cur_horse", 0),
         (assign, ":new_icon", "icon_player_horseman"),
         #(display_message,"@no water, horse"),
       (else_try),
         (assign, ":new_icon", "icon_player"),
         #(display_message,"@no water, no horse"),
       (try_end),
    (else_try),
      (eq, "$g_player_icon_state", pis_camping), # All of this is thanks to Lumos bein' generous, and not being as much of a lazy arse as I am
      (assign, ":new_icon", "icon_camp"),
    (try_end),
     ## TGS: mat: Edited to keep icons from going crazy
     (party_get_icon, ":current_icon", "p_main_party"),
     (try_begin),
     (neq, ":current_icon", ":new_icon"),
         (party_set_icon,"p_main_party", ":new_icon"),
     (try_end),
     ## TGS: mat: End
]),
  
## TGS: mat: Removed to stop the stuttering
#    (0.1, 0, 0, [(party_get_current_terrain,":terrain","p_main_party"),
#      (neq,":terrain",7),], # 7 = rt_bridge
#   [(party_set_icon,"p_main_party", "icon_player"),]),
## TGS: mat: End
  
 (0.1, 0, 0.0, [],
[(try_for_parties, ":cur_party"),
   (party_get_current_terrain, ":terrain", ":cur_party"),
   (eq, ":terrain", 7), # 7 = rt_bridge
      (party_get_template_id, ":cur_template", ":cur_party"),
      (party_get_slot, ":party_type", ":cur_party", slot_party_type),
      (this_or_next|eq, ":cur_template", "pt_kingdom_hero_party"),
      (this_or_next|eq, ":cur_template", "pt_kingdom_caravan_party"),
      (this_or_next|eq, ":cur_template", "pt_manhunters"),
      (this_or_next|eq, ":cur_template", "pt_village_farmers"),
      (this_or_next|eq, ":cur_template", "pt_deserters"),
      (this_or_next|eq, ":cur_template", "pt_looters"),
      (this_or_next|eq, ":cur_template", "pt_forest_bandits"),
      (this_or_next|eq, ":cur_template", "pt_steppe_bandits"),
      (this_or_next|eq, ":cur_template", "pt_mountain_bandits"),
 # added by mat2rivs
      (this_or_next|eq, ":cur_template", "pt_taiga_bandits"),
      (this_or_next|eq, ":cur_template", "pt_desert_bandits"),#
      (this_or_next|eq, ":cur_template", "pt_trollocs"),#
      (this_or_next|eq, ":cur_template", "pt_merchant_caravan"),#
      (this_or_next|eq, ":cur_template", "pt_dplmc_spouse"),#
      (this_or_next|eq, ":cur_template", "pt_dplmc_gift_caravan"),#
      (this_or_next|eq, ":cur_template", "pt_dplmc_recruiter"),#
      (this_or_next|eq, ":party_type", spt_patrol), # for new town patrols
 # end
      (eq, ":cur_template", "pt_sea_raiders"),
        (party_set_icon, ":cur_party", "icon_ship"),
   (else_try),
   (neq,":terrain",7), # 7 = rt_bridge
     (party_get_template_id, ":cur_template", ":cur_party"),
     (eq, ":cur_template", "pt_kingdom_hero_party"),
       (party_set_icon,":cur_party","icon_flagbearer_a"),
   (else_try),
 # added by mat2rivs
     (this_or_next|eq, ":cur_template", "pt_merchant_caravan"),
     (this_or_next|eq, ":cur_template", "pt_dplmc_gift_caravan"),
 # end
     (eq, ":cur_template", "pt_kingdom_caravan_party"),
       (party_set_icon,":cur_party","icon_mule"),
   (else_try),
     (eq, ":cur_template", "pt_deserters"),
       (party_set_icon,":cur_party","icon_vaegir_knight"),
   (else_try),
 # added by mat2rivs
     (this_or_next|eq, ":cur_template", "pt_dplmc_recruiter"),
 # end
     (this_or_next|eq, ":party_type", spt_patrol), # for new town patrols
     (eq, ":cur_template", "pt_manhunters"),
       (party_set_icon,":cur_party","icon_gray_knight"),
   (else_try),
     (eq, ":cur_template", "pt_village_farmers"),
       (party_set_icon,":cur_party","icon_peasant"),
 # added by mat2rivs
   (else_try),
     (eq, ":cur_template", "pt_dplmc_spouse"),
       (party_set_icon,":cur_party","icon_woman"),
 # end
   (else_try),
     (this_or_next|eq, ":cur_template", "pt_looters"),
     (this_or_next|eq, ":cur_template", "pt_forest_bandits"),
# (this_or_next|eq, ":cur_template", "pt_steppe_bandits"),  # should be kherghit icon
     (this_or_next|eq, ":cur_template", "pt_mountain_bandits"),
 # added by mat2rivs
     (this_or_next|eq, ":cur_template", "pt_desert_bandits"),
     (this_or_next|eq, ":cur_template", "pt_trollocs"),
 # end
     (eq, ":cur_template", "pt_sea_raiders"),
       (party_set_icon,":cur_party","icon_axeman"),
 # added by mat2rivs
   (else_try),
     (this_or_next|eq, ":cur_template", "pt_taiga_bandits"),
     (eq, ":cur_template", "pt_steppe_bandits"),
       (party_set_icon,":cur_party","icon_khergit"),
 # end 
   (else_try),
     (eq, ":cur_template", "pt_cattle_herd"),
        (party_set_icon,":cur_party","icon_cattle"),
   (try_end),
 ]),

## a little extra trigger added by mat2rivs to keep track of the terrain type the character was on last.
    (0.5, 0, 0, [],
   [(party_get_current_terrain, "$g_player_party_previous_terrain_type", "p_main_party")]),  ## If this is non rt_bridge and they are in rt_bridge, then they can fight in the 'Go Ashore' mode

  ## New main map distance measuring trigger (Disabled normally)
        (0, 0, 0, [(eq, "$g_tutorial_complete", 1), #  to enable, remove the second line in the condition
                   (eq, "$g_tutorial_complete", 0),
                   ],
         [
            ##Click 'N' to find main party's distance to bandar eban
            (try_begin),
            (key_clicked, key_n),  # start the remainder of the code when 'N' is clicked
                #(party_get_position, pos1, "p_main_party"),
                #(party_get_position, pos2, "p_town_6"),
                #(get_distance_between_positions, reg1, pos1, pos2),
                #(display_message, "@Main party is {reg1} cm from Bandar Eban..."),
            
                (call_script, "script_tgs_check_terrain_around_party", "p_main_party", 275), # will need to find radius
                (try_begin),
                (eq, reg0, 0),
                    (display_message, "@Too far from land to go ashore..."),
                (else_try),
                (eq, reg0, 1),
                    (display_message, "@Close enough to land to go ashore..."),
                (else_try),
                    (display_message, "@Script is not working correctly..."),
                (try_end),
            ## Other code
                (assign, ":num_parties", 0),
                (try_for_parties, ":party_no"),
                    (val_add, ":num_parties", 1),
                    (assign, ":count", 0),
                    (party_count_members_of_type, ":count", ":party_no", "trp_player"),
                    (try_begin),
                    (gt, ":count", 0),
                        (assign, reg2, ":party_no"),
                        (str_store_party_name, s1, ":party_no"),
                        (display_message, "@Player is in {reg2}: {s1}."),
                    (try_end),
                (try_end),
                (assign, reg2, ":num_parties"),
                (display_message, "@There are currently {reg2} parties."),
            (try_end),

        ]),

## TGS: Sea Battles end  



#Don't remove the bracket after this comment   

 
]
