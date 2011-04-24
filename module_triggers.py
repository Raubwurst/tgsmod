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
# Tutorial:  #modified for Wheel of Time
  (0.1, 0, ti_once, [(map_free,0)], [
                                      (dialog_box,"str_tutorial_map1"),
                                      (assign,"$g_tutorial_complete",1),
                                      ]),

#  (1.0, 0, ti_once, [(map_free,0)], [(start_map_conversation, "trp_guide", -1)]),

# Refresh Merchants
  (0.0, 0, 24.0, [], [
                      (reset_item_probabilities,100),
                      (set_merchandise_modifier_quality,150),


                      (reset_item_probabilities,100),(set_item_probability_in_merchandise,"itm_salt",700),
                      (troop_add_merchandise,"trp_salt_mine_merchant",itp_type_goods,num_merchandise_goods),

                      # Add trade goods to merchant inventories
#                      (store_sub, ":item_to_production_slot", slot_town_trade_good_productions_begin, trade_goods_begin),
                      (store_sub, ":item_to_price_slot", slot_town_trade_good_prices_begin, trade_goods_begin),

                      (try_for_range,":cur_center",towns_begin,towns_end),
                        (party_get_slot,":cur_merchant",":cur_center",slot_town_merchant),
                        (reset_item_probabilities,100),
                        (try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
#                          (store_add, ":cur_production_slot", ":cur_goods", ":item_to_production_slot"),
                          (store_add, ":cur_price_slot", ":cur_goods", ":item_to_price_slot"),
#                          (party_get_slot, ":cur_production", ":cur_center", ":cur_production_slot"),
                          (party_get_slot, ":cur_price", ":cur_center", ":cur_price_slot"),
                      
#                          (assign, ":cur_probability", 100),
#                          (store_add, ":cur_production", 100, ":cur_production"),
#                          (val_mul, ":cur_probability", ":cur_production"),
#                          (val_div, ":cur_probability", 100),
#                          (try_begin),
#                            (gt, ":cur_probability", 100),
#                            (store_sub, ":temp_dif", ":cur_probability", 100),
#                            (val_mul, ":temp_dif", 4),
#                            (val_add, ":cur_probability", ":temp_dif"),
#                          (try_end),
#                          (store_sub, ":temp_dif", average_price_factor, ":cur_price"),
#                          (val_div, ":temp_dif", 2),
#                          (val_add, ":cur_price", ":temp_dif"),

						  (call_script, "script_center_get_production", ":cur_center", ":cur_goods"),
						  (assign, ":cur_probability", reg0),
						  (call_script, "script_center_get_consumption", ":cur_center", ":cur_goods"),
						  (val_add, ":cur_probability", reg0),
						  
						  (val_mul, ":cur_probability", 4),


                          (val_mul, ":cur_probability", average_price_factor),
                          (val_div, ":cur_probability", ":cur_price"),
                          (val_mul, ":cur_probability", average_price_factor),
                          (val_div, ":cur_probability", ":cur_price"),
                          (val_mul, ":cur_probability", average_price_factor),
                          (val_div, ":cur_probability", ":cur_price"),
#                          (val_mul, ":cur_probability", average_price_factor),
#                          (val_div, ":cur_probability", ":cur_price"),
                          (set_item_probability_in_merchandise,":cur_goods",":cur_probability"),
                        (try_end),
                        (troop_add_merchandise,":cur_merchant",itp_type_goods,num_merchandise_goods),

                        (troop_ensure_inventory_space,":cur_merchant",merchant_inventory_space),
                        (troop_sort_inventory, ":cur_merchant"),
                        (store_troop_gold, ":cur_gold",":cur_merchant"),
                        (lt,":cur_gold",1500),
                        (store_random_in_range,":new_gold",500,1000),
                        (call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),
                      (try_end),
                     ]),

# Refresh Armor sellers
  (0.0, 0, 24.0, [], [
                      (reset_item_probabilities,100),
                      (set_merchandise_modifier_quality,150),
                      (try_for_range,reg(2),armor_merchants_begin,armor_merchants_end),
                        (store_sub, ":cur_town", reg2, armor_merchants_begin),
                        (val_add, ":cur_town", towns_begin),
                        (party_get_slot, ":cur_faction", ":cur_town", slot_center_original_faction),
                        (troop_add_merchandise_with_faction,reg(2), ":cur_faction",itp_type_body_armor,16),
                        (troop_add_merchandise_with_faction,reg(2), ":cur_faction",itp_type_head_armor,16),
                        (troop_add_merchandise_with_faction,reg(2), ":cur_faction",itp_type_foot_armor,8),
                        (troop_add_merchandise_with_faction,reg(2), ":cur_faction",itp_type_hand_armor,4),
                        (troop_ensure_inventory_space,reg(2),merchant_inventory_space),
                        (troop_sort_inventory, reg(2)),
                        (store_troop_gold, reg(6),reg(2)),
                        (lt,reg(6),900),
                        (store_random_in_range,":new_gold",200,400),
                        (call_script, "script_troop_add_gold", reg(2), ":new_gold"),
                      (end_try,0),
                     ]),


# Refresh Weapon sellers
  (0.0, 0, 24.0, [], [
                      (reset_item_probabilities,100),
                      (set_merchandise_modifier_quality,150),
                      (try_for_range,reg(2),weapon_merchants_begin,weapon_merchants_end),
                        (store_sub, ":cur_town", reg2, weapon_merchants_begin),
                        (val_add, ":cur_town", towns_begin),
                        (party_get_slot, ":cur_faction", ":cur_town", slot_center_original_faction),
                        (troop_add_merchandise_with_faction,reg(2), ":cur_faction",itp_type_one_handed_wpn,5),
                        (troop_add_merchandise_with_faction,reg(2), ":cur_faction",itp_type_two_handed_wpn,5),
                        (troop_add_merchandise_with_faction,reg(2), ":cur_faction",itp_type_polearm,5),
                        (troop_add_merchandise_with_faction,reg(2), ":cur_faction",itp_type_shield,6),
                        (troop_add_merchandise_with_faction,reg(2), ":cur_faction",itp_type_bow,4),
                        (troop_add_merchandise_with_faction,reg(2), ":cur_faction",itp_type_crossbow,3),
                        (troop_add_merchandise_with_faction,reg(2), ":cur_faction",itp_type_thrown,5),
                        (troop_add_merchandise_with_faction,reg(2), ":cur_faction",itp_type_arrows,2),
                        (troop_add_merchandise_with_faction,reg(2), ":cur_faction",itp_type_bolts,2),
                        (troop_ensure_inventory_space,reg(2),merchant_inventory_space),
                        (troop_sort_inventory, reg(2)),
                        (store_troop_gold, reg(6),reg(2)),
                        (lt,reg(6),900),
                        (store_random_in_range,":new_gold",200,400),
                      (call_script, "script_troop_add_gold", reg(2), ":new_gold"),
                      (end_try,0),
                     ]),

# Refresh Horse sellers
  (0.0, 0, 24.0, [], [
                      (reset_item_probabilities,100),
                      (set_merchandise_modifier_quality,150),
                      (try_for_range,":cur_merchant",horse_merchants_begin,horse_merchants_end),
                        (store_sub, ":cur_town", ":cur_merchant", horse_merchants_begin),
                        (val_add, ":cur_town", towns_begin),
                        (party_get_slot, ":cur_faction", ":cur_town", slot_center_original_faction),
                        (troop_add_merchandise_with_faction,":cur_merchant", ":cur_faction",itp_type_horse,5),
                        (troop_ensure_inventory_space,":cur_merchant",65),
                        (troop_sort_inventory, ":cur_merchant"),
                        (store_troop_gold, ":cur_gold",":cur_merchant"),
                        (lt,":cur_gold",600),
                        (store_random_in_range,":new_gold",200,400),
                        (call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),
                      (try_end),
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
  (24, 0, ti_once, 
  [
      (store_skill_level, ":inv_skill", "skl_inventory_management", "trp_player"),
      (gt, "$g_player_chamberlain", 0),
      (ge, ":inv_skill", 3),      
  ], 
  [
    (call_script, "script_dplmc_init_item_difficulties"),       
    (call_script, "script_dplmc_init_item_base_score"), 
    (assign, "$g_autoloot", 1),
  ]),
  
  (0.1, 0.5, 0, [(map_free,0),(eq,"$g_move_fast", 1)], [(assign,"$g_move_fast", 0)]),
    
##diplomacy end
  
# moved for wheel of time
#diplomatic indices (was in simple triggers) Begin randomly generating war/peace after game days past 120
  (24, 0, 0, [
              (store_current_hours, ":number_game_hours_passed"),
              (gt, ":number_game_hours_passed", 0, 24*120),],
   [
   (call_script, "script_randomly_start_war_peace_new", 1),

   (try_begin),
		(store_random_in_range, ":acting_village", villages_begin, villages_end),
		(store_random_in_range, ":target_village", villages_begin, villages_end),
		(store_faction_of_party, ":acting_faction", ":acting_village"),
		(store_faction_of_party, ":target_faction", ":target_village"), #target faction receives the provocation
		(neq, ":acting_village", ":target_village"),
		(neq, ":acting_faction", ":target_faction"),

		(call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":target_faction", ":acting_faction"),
		(eq, reg0, 0),

		(try_begin),
			(party_slot_eq, ":acting_village", slot_center_original_faction, ":target_faction"),

			(call_script, "script_add_notification_menu", "mnu_notification_border_incident", ":acting_village", -1),
		(else_try),
			(party_slot_eq, ":acting_village", slot_center_ex_faction, ":target_faction"),

			(call_script, "script_add_notification_menu", "mnu_notification_border_incident", ":acting_village", -1),

		(else_try),
			(set_fixed_point_multiplier, 1),
			(store_distance_to_party_from_party, ":distance", ":acting_village", ":target_village"),
			(lt, ":distance", 25),

			(call_script, "script_add_notification_menu", "mnu_notification_border_incident", ":acting_village", ":target_village"),
		(try_end),
   (try_end),

   (try_for_range, ":faction_1", kingdoms_begin, kingdoms_end),
		(faction_slot_eq, ":faction_1", slot_faction_state, sfs_active),
		(try_for_range, ":faction_2", kingdoms_begin, kingdoms_end),
			(neq, ":faction_1", ":faction_2"),
			(faction_slot_eq, ":faction_2", slot_faction_state, sfs_active),

			#remove provocations
			(store_add, ":slot_truce_days", ":faction_2", slot_faction_truce_days_with_factions_begin),
			(val_sub, ":slot_truce_days", kingdoms_begin),
			(faction_get_slot, ":truce_days", ":faction_1", ":slot_truce_days"),
			(try_begin),
				(ge, ":truce_days", 1),
				(try_begin),
					(eq, ":truce_days", 1),
					(call_script, "script_update_faction_notes", ":faction_1"),
					(lt, ":faction_1", ":faction_2"),
					(call_script, "script_add_notification_menu", "mnu_notification_truce_expired", ":faction_1", ":faction_2"),
				##diplomacy begin
        (else_try),
          (eq, ":truce_days", 61),
          (call_script, "script_update_faction_notes", ":faction_1"),
          (lt, ":faction_1", ":faction_2"),
          (call_script, "script_add_notification_menu", "mnu_dplmc_notification_alliance_expired", ":faction_1", ":faction_2"),
        (else_try),
          (eq, ":truce_days", 41),
          (call_script, "script_update_faction_notes", ":faction_1"),
          (lt, ":faction_1", ":faction_2"),
          (call_script, "script_add_notification_menu", "mnu_dplmc_notification_defensive_expired", ":faction_1", ":faction_2"),
        (else_try),
          (eq, ":truce_days", 21),
          (call_script, "script_update_faction_notes", ":faction_1"),
          (lt, ":faction_1", ":faction_2"),
          (call_script, "script_add_notification_menu", "mnu_dplmc_notification_trade_expired", ":faction_1", ":faction_2"),
        ##diplomacy end
				(try_end),
				(val_sub, ":truce_days", 1),
				(faction_set_slot, ":faction_1", ":slot_truce_days", ":truce_days"),
			(try_end),

			(store_add, ":slot_provocation_days", ":faction_2", slot_faction_provocation_days_with_factions_begin),
			(val_sub, ":slot_provocation_days", kingdoms_begin),
			(faction_get_slot, ":provocation_days", ":faction_1", ":slot_provocation_days"),
			(try_begin),
				(ge, ":provocation_days", 1),
				(try_begin),#factions already at war
					(store_relation, ":relation", ":faction_1", ":faction_2"),
					(lt, ":relation", 0),
					(faction_set_slot, ":faction_1", ":slot_provocation_days", 0),
				(else_try), #Provocation expires
					(eq, ":provocation_days", 1),
					(call_script, "script_add_notification_menu", "mnu_notification_casus_belli_expired", ":faction_1", ":faction_2"),
					(faction_set_slot, ":faction_1", ":slot_provocation_days", 0),
				(else_try),
					(val_sub, ":provocation_days", 1),
					(faction_set_slot, ":faction_1", ":slot_provocation_days", ":provocation_days"),
				(try_end),
			(try_end),

			(try_begin), #at war
				(store_relation, ":relation", ":faction_1", ":faction_2"),
				(lt, ":relation", 0),
				(store_add, ":slot_war_damage", ":faction_2", slot_faction_war_damage_inflicted_on_factions_begin),
				(val_sub, ":slot_war_damage", kingdoms_begin),
				(faction_get_slot, ":war_damage", ":faction_1", ":slot_war_damage"),
				(val_add, ":war_damage", 1),
				(faction_set_slot, ":faction_1", ":slot_war_damage", ":war_damage"),
			(try_end),

		(try_end),
		(call_script, "script_update_faction_notes", ":faction_1"),
	(try_end),
    ]),


### Begin Wheel of time Triggers ###
  
# Initiate $g_tutorial_complete
#  (0.1, 0, ti_once, [], [(assign,"$g_tutorial_complete",0)]),

# Wheel of Time Initialization
  (0.1, 0, ti_once, [(eq, "$g_tutorial_complete", 1)],
    [
        # Diplomacy
#        (call_script,"script_randomly_start_war_peace_new",1),

        # Channeling Proficiency variable
        (assign,"$g_channeling_proficiency_modifier",0),
        (assign,"$g_channeling_proficiency_modifier",0),

    ]),

# Periodically Force Wheel of Time Diplomacy (every 5 days) (don't use for now)
#  (24*5, 0, 0, [(eq, "$g_tutorial_complete", 1)],[(call_script,"script_randomly_start_war_peace_new",1)]),

################## Timeline changes begin ##############

# Faction city and lord changes at 30 days:
  (1, 24*30, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Stone of Tear... King Darlin...to the Legion of the Dragon
        (call_script,"script_change_troop_faction","trp_knight_3_8","fac_kingdom_1"),
        (call_script,"script_give_center_to_faction_aux", "p_castle_4","fac_kingdom_1"),
        #Tear... High Lord Torean... to the Legion of the Dragon, Tear to Rand al'Thor
        (call_script,"script_change_troop_faction","trp_knight_3_6","fac_kingdom_1"),
        (call_script,"script_give_center_to_faction_aux", "p_town_10","fac_kingdom_1"),
        (call_script,"script_give_center_to_lord","p_town_10","trp_kingdom_1_lord",1),
        #Culmarr Castle... High Lord Hearne... to the Legion of the Dragon
        (call_script,"script_change_troop_faction","trp_knight_3_32","fac_kingdom_1"),
        (call_script,"script_give_center_to_faction_aux", "p_castle_1","fac_kingdom_1"),
        #Slezkh Castle... High Lord Tolmeran... to the Legion of the Dragon
        (call_script,"script_change_troop_faction","trp_knight_3_38","fac_kingdom_1"),
        (call_script,"script_give_center_to_faction_aux", "p_castle_22","fac_kingdom_1"),
        
        #Mayene... Berelain sur Paendrag Paeron... to the Legion of the Dragon
        (call_script,"script_change_troop_faction","trp_knight_2_2","fac_kingdom_1"),
        (call_script,"script_give_center_to_faction_aux", "p_town_12","fac_kingdom_1"),

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
        (call_script,"script_give_center_to_lord","p_town_19","trp_knight_5_11",1),

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
        (call_script,"script_change_troop_faction","trp_knight_3_4","fac_kingdom_7"),
        (call_script,"script_give_center_to_faction_aux", "p_town_8","fac_kingdom_7"),
        (call_script,"script_give_center_to_lord","p_town_8","trp_knight_7_2",1),

        (dialog_box, "str_seanchan_invade_tarabon"),

    ]),

# Faction city and lord changes at 55 days:
  (1, 24*55, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Salidar... to the White Tower, to Lelaine Sedai
        (call_script,"script_give_center_to_faction_aux", "p_castle_34","fac_kingdom_5"),
        (call_script,"script_give_center_to_lord","p_castle_34","trp_knight_5_7",1),
        
        (dialog_box, "str_rebel_aes_sedai_to_salidar"),

    ]),

# Faction city and lord changes at 60 days:
  (1, 24*60, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Cairhien... Lord Dobraine Taborwin...to the Legion of the Dragon
        (call_script,"script_change_troop_faction","trp_knight_2_14","fac_kingdom_1"),
        (call_script,"script_give_center_to_faction_aux", "p_town_1","fac_kingdom_1"),
        #Haringoth Castle... Lady Selande Darengil... to the Legion of the Dragon
        (call_script,"script_change_troop_faction","trp_knight_2_21","fac_kingdom_1"),
        (call_script,"script_give_center_to_faction_aux", "p_castle_35","fac_kingdom_1"),
        #Tevarin Castle... Cairhien Lord... to the Legion of the Dragon
        (call_script,"script_change_troop_faction","trp_knight_2_24","fac_kingdom_1"),
        (call_script,"script_give_center_to_faction_aux", "p_castle_23","fac_kingdom_1"),

        (dialog_box, "str_dragon_takes_cairhien"),

    ]),

# Faction city and lord changes at 62 days:
  (1, 24*62, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Caemlyn... to the Legion of the Dragon, to Lord Davram Bashere
        (call_script,"script_give_center_to_faction_aux", "p_town_3","fac_kingdom_1"),
        (call_script,"script_give_center_to_lord","p_town_3","trp_knight_1_5",1),

        (dialog_box, "str_dragon_takes_caemlyn"),

    ]),

# Faction city and lord changes at 65 days:
  (1, 24*65, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Egwene al'Vere raised to rebel Amyrlin Seat... give her leadership of Salidar
        (call_script,"script_give_center_to_lord","p_castle_34","trp_kingdom_5_lord",1),

        (dialog_box, "str_rebel_aes_sedai_raise_egwene_to_amyrlin"),

    ]),

# Faction city and lord changes at 70 days:
  (1, 24*70, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Amador... to the Seanchan Empire... to Banner-General Gamel Loune
        (call_script,"script_give_center_to_faction_aux", "p_town_13","fac_kingdom_7"),
        (call_script,"script_give_center_to_lord","p_town_13","trp_knight_7_4",1),
        #Fortress of the Light... to the Seanchan Empire... to Banner-General Mikhel Najirah
        (call_script,"script_give_center_to_faction_aux", "p_castle_3","fac_kingdom_7"),
        (call_script,"script_give_center_to_lord","p_castle_3","trp_knight_7_5",1),
        #Bellon... High Inquisitor Rhadam Asunawa... to the Seanchan Empire
        (call_script,"script_change_troop_faction","trp_knight_3_29","fac_kingdom_7"),
        (call_script,"script_give_center_to_faction_aux", "p_castle_2","fac_kingdom_7"),
        #Sienda... to the Seanchan Empire... to Banner-General Efraim Yamada
        (call_script,"script_give_center_to_faction_aux", "p_castle_30","fac_kingdom_7"),
        (call_script,"script_give_center_to_lord","p_castle_30","trp_knight_7_7",1),
        #Grunwalder Castle... to the Seanchan Empire... to Lieutenant-General Abaldar Yulan
        (call_script,"script_give_center_to_faction_aux", "p_castle_28","fac_kingdom_7"),
        (call_script,"script_give_center_to_lord","p_castle_28","trp_knight_7_8",1),
        
        (dialog_box, "str_seanchan_invade_amadicia"),

    ]),

# Faction city and lord changes at 72 days:
  (1, 24*72, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Ebou Dar... King Beslan Mitsobar... to the Seanchan Empire... to Empress Fortuona Athaem Kore Paendrag
        (call_script,"script_change_troop_faction","trp_knight_2_7","fac_kingdom_7"),
        (call_script,"script_give_center_to_faction_aux", "p_town_4","fac_kingdom_7"),
        (call_script,"script_give_center_to_lord","p_town_4","trp_kingdom_7_lord",1),
        #Alkindar... Altara Lord... to the Seanchan Empire... to King Beslan Mitsobar
        (call_script,"script_change_troop_faction","trp_knight_2_35","fac_kingdom_7"),
        (call_script,"script_give_center_to_faction_aux", "p_castle_25","fac_kingdom_7"),
        (call_script,"script_give_center_to_lord","p_castle_25","trp_knight_2_7",1),
        #Jurador... Altara Lesser Lady... to the Seanchan Empire... to Altara Lord
        (call_script,"script_change_troop_faction","trp_knight_2_38","fac_kingdom_7"),
        (call_script,"script_give_center_to_faction_aux", "p_castle_36","fac_kingdom_7"),
        (call_script,"script_give_center_to_lord","p_castle_36","trp_knight_2_35",1),
        #Cormaed... Altara Lady... to the Seanchan Empire
        (call_script,"script_change_troop_faction","trp_knight_2_36","fac_kingdom_7"),
        (call_script,"script_give_center_to_faction_aux", "p_castle_32","fac_kingdom_7"),

        (dialog_box, "str_seanchan_invade_altara"),

    ]),

# Faction city and lord changes at 73 days:
  (1, 24*73, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Illian... Lord Ballin Elamri... to the Legion of the Dragon
        (call_script,"script_change_troop_faction","trp_knight_2_11","fac_kingdom_1"),
        (call_script,"script_give_center_to_faction_aux", "p_town_22","fac_kingdom_1"),
        (call_script,"script_give_center_to_lord","p_town_22","trp_knight_2_11",1),
        #Rindyar Castle... Lord Spiron Narettin... to the Legion of the Dragon
        (call_script,"script_change_troop_faction","trp_knight_2_10","fac_kingdom_1"),
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
        (call_script,"script_give_center_to_faction_aux", "p_town_3","fac_kingdom_3"),
        (call_script,"script_give_center_to_lord","p_town_3","trp_kingdom_3_lord",1),

        (dialog_box, "str_elayne_claims_andor_throne"),

    ]),

# Faction city and lord changes at 90 days:
  (1, 24*90, ti_once, [(eq, "$g_tutorial_complete", 1)],
   [
        #Bandar Eban... to the Legion of the Dragon... to Davram Bashere
        (call_script,"script_give_center_to_faction_aux", "p_town_6","fac_kingdom_1"),
        (call_script,"script_give_center_to_lord","p_town_6","trp_knight_1_5",1),
        #Katar... Lord Rodel Ituralde... to the Legion of the Dragon
        (call_script,"script_change_troop_faction","trp_knight_2_5","fac_kingdom_1"),
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
        (call_script,"script_give_center_to_lord","p_town_19","trp_kingdom_5_lord",1),

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
        (call_script,"script_give_center_to_faction_aux", "p_town_17","fac_kingdom_8"),
        (call_script,"script_give_center_to_lord","p_town_17","trp_knight_8_1",1),
        #Shol Arbela... to the Shadowspawn... to Demandred
        (call_script,"script_give_center_to_faction_aux", "p_town_9","fac_kingdom_8"),
        (call_script,"script_give_center_to_lord","p_town_9","trp_knight_8_2",1),
        #Canluum... to the Shadowspawn... to Moghedien
        (call_script,"script_give_center_to_faction_aux", "p_castle_19","fac_kingdom_8"),
        (call_script,"script_give_center_to_lord","p_castle_19","trp_knight_8_3",1),

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

# Basic Game messages for Wheel of Time

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
                      (this_or_next|eq,"$background_answer_2",cb_childhood_ashaman_soldier),
                      (eq,"$background_answer_2",cb_childhood_village_wisdom_assistant),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 1),],[(dialog_box,"str_learn_weave_1")]),
  
  (0, 0.15, ti_once, [(this_or_next|eq,"$background_answer_2",cb_childhood_novice),
                      (this_or_next|eq,"$background_answer_2",cb_childhood_ashaman_soldier),
                      (eq,"$background_answer_2",cb_childhood_village_wisdom_assistant),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 15),], [(dialog_box,"str_learn_weave_2")]),
  
  (0, 0.15, ti_once, [(this_or_next|eq,"$background_answer_2",cb_childhood_novice),
                      (this_or_next|eq,"$background_answer_2",cb_childhood_ashaman_soldier),
                      (eq,"$background_answer_2",cb_childhood_village_wisdom_assistant),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 30),], [(dialog_box,"str_learn_weave_3")]),
  
  (0, 0.15, ti_once, [(this_or_next|eq,"$background_answer_2",cb_childhood_novice),
                      (this_or_next|eq,"$background_answer_2",cb_childhood_ashaman_soldier),
                      (eq,"$background_answer_2",cb_childhood_village_wisdom_assistant),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 50),], [(dialog_box,"str_learn_weave_4")]),
  
  (0, 0.15, ti_once, [(this_or_next|eq,"$background_answer_2",cb_childhood_novice),
                      (this_or_next|eq,"$background_answer_2",cb_childhood_ashaman_soldier),
                      (eq,"$background_answer_2",cb_childhood_village_wisdom_assistant),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 65),], [(dialog_box,"str_learn_weave_5")]),
  
  (0, 0.15, ti_once, [(this_or_next|eq,"$background_answer_2",cb_childhood_novice),
                      (this_or_next|eq,"$background_answer_2",cb_childhood_ashaman_soldier),
                      (eq,"$background_answer_2",cb_childhood_village_wisdom_assistant),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 75),], [(dialog_box,"str_learn_weave_6")]),
  
  (0, 0.15, ti_once, [(this_or_next|eq,"$background_answer_2",cb_childhood_novice),
                      (this_or_next|eq,"$background_answer_2",cb_childhood_ashaman_soldier),
                      (eq,"$background_answer_2",cb_childhood_village_wisdom_assistant),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 85),], [(dialog_box,"str_learn_weave_7")]),
  
  (0, 0.15, ti_once, [(this_or_next|eq,"$background_answer_2",cb_childhood_novice),
                      (this_or_next|eq,"$background_answer_2",cb_childhood_ashaman_soldier),
                      (eq,"$background_answer_2",cb_childhood_village_wisdom_assistant),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 100),], [(dialog_box,"str_learn_weave_8")]),
  
  (0, 0.15, ti_once, [(this_or_next|eq,"$background_answer_2",cb_childhood_novice),
                      (this_or_next|eq,"$background_answer_2",cb_childhood_ashaman_soldier),
                      (eq,"$background_answer_2",cb_childhood_village_wisdom_assistant),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 125),], [(dialog_box,"str_learn_weave_9")]),
  
  (0, 0.15, ti_once, [(this_or_next|eq,"$background_answer_2",cb_childhood_novice),
                      (this_or_next|eq,"$background_answer_2",cb_childhood_ashaman_soldier),
                      (eq,"$background_answer_2",cb_childhood_village_wisdom_assistant),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 150),], [(dialog_box,"str_learn_weave_10")]),
  
  (0, 0.15, ti_once, [(this_or_next|eq,"$background_answer_2",cb_childhood_novice),
                      (this_or_next|eq,"$background_answer_2",cb_childhood_ashaman_soldier),
                      (eq,"$background_answer_2",cb_childhood_village_wisdom_assistant),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 175),], [(dialog_box,"str_learn_weave_11")]),
  
  (0, 0.15, ti_once, [(this_or_next|eq,"$background_answer_2",cb_childhood_novice),
                      (this_or_next|eq,"$background_answer_2",cb_childhood_ashaman_soldier),
                      (eq,"$background_answer_2",cb_childhood_village_wisdom_assistant),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 200),], [(dialog_box,"str_learn_weave_12")]),
  
  (0, 0.15, ti_once, [(this_or_next|eq,"$background_answer_2",cb_childhood_novice),
                      (this_or_next|eq,"$background_answer_2",cb_childhood_ashaman_soldier),
                      (eq,"$background_answer_2",cb_childhood_village_wisdom_assistant),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 225),], [(dialog_box,"str_learn_weave_13")]),
  
  (0, 0.15, ti_once, [(this_or_next|eq,"$background_answer_2",cb_childhood_novice),
                      (this_or_next|eq,"$background_answer_2",cb_childhood_ashaman_soldier),
                      (eq,"$background_answer_2",cb_childhood_village_wisdom_assistant),
                      (store_proficiency_level,":channeling_proficiency","trp_player",wpt_firearm),(ge, ":channeling_proficiency", 250),], [(dialog_box,"str_learn_weave_14")]),

  ## New main map hotkeys
        (0, 0, 0, [(eq, "$g_tutorial_complete", 1)],
         [
            ##Click 'M' to re-add One Power Item to inventory (Now this will only work if player is a channeler)
            (try_begin),
            (key_clicked, key_m),  # start the remainder of the code when 'M' is clicked
            (this_or_next|eq,"$background_answer_2",cb_childhood_novice),
            (this_or_next|eq,"$background_answer_2",cb_childhood_ashaman_soldier),
            (eq,"$background_answer_2",cb_childhood_village_wisdom_assistant),
                (troop_ensure_inventory_space, "trp_player", 1),
                (troop_add_item, "trp_player", "itm_power_player", 0),
            (try_end),

        ]),

  ## New main map testing hotkeys
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

#                            (party_add_members, ":party", "trp_ashaman_soldier", 2),
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



#Don't remove the bracket after this comment  

 
]
