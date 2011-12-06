from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
  ("none","none",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("rescued_prisoners","Rescued Prisoners",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
  ("enemy","Enemy",icon_gray_knight,0,fac_undeads,merchant_personality,[]),
  ("hero_party","Hero Party",icon_gray_knight,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed. 
####################################################################################################################
##  ("old_garrison","Old Garrison",icon_vaegir_knight,0,fac_neutral,merchant_personality,[]),
  ("village_defenders","Village Defenders",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,10,20),(trp_peasant_woman,0,4)]),

  ("cattle_herd","Cattle Herd",icon_cattle|carries_goods(10),0,fac_neutral,merchant_personality,[(trp_cattle,80,120)]),

##  ("vaegir_nobleman","Vaegir Nobleman",icon_vaegir_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_vaegir_knight,2,6),(trp_vaegir_horseman,4,12)]),
##  ("swadian_nobleman","Swadian Nobleman",icon_gray_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_swadian_knight,2,6),(trp_swadian_man_at_arms,4,12)]),
# Ryan BEGIN
  # edited for TGS
  ("looters","Bandit Rabble",icon_axeman|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_looter,15,125), (trp_arad_doman_rabble, 5, 30), (trp_tarabon_rabble, 5, 50), (trp_forest_bandit, 5, 25)]), #Looters
# Ryan END
  ("manhunters","White Cloaks",icon_gray_knight,0,fac_manhunters,soldier_personality,[(trp_whitecloak_swordsman,10,30), (trp_whitecloak_bowman, 10,30), (trp_whitecloak_lancer, 8,24)]),
##  ("peasant","Peasant",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,1,6),(trp_peasant_woman,0,7)]),

#  ("black_khergit_raiders","Black Khergit Raiders",icon_khergit_horseman_b|carries_goods(2),0,fac_black_khergits,bandit_personality,[(trp_black_khergit_guard,1,10),(trp_black_khergit_horseman,5,5)]),
  ("steppe_bandits","Dragonsworn Bandits",icon_khergit|carries_goods(2),0,fac_outlaws,wot_bandit_personality,[(trp_arad_doman_rabble_bandit, 10, 90), (trp_tarabon_rabble, 10, 90), (trp_forest_bandit, 10, 40), (trp_tarabon_scout, 10, 30), (trp_mountain_bandit, 10, 40), (trp_caravan_guard, 15, 30)]), # Steppe Bandits (trp_steppe_bandit, 4,58)
  ("taiga_bandits","Dragonsworn Bandits",icon_khergit|carries_goods(2),0,fac_outlaws,wot_bandit_personality,[(trp_arad_doman_rabble_bandit, 10, 90), (trp_tarabon_rabble, 10, 90), (trp_forest_bandit, 10, 40), (trp_tarabon_scout, 10, 30), (trp_mountain_bandit, 10, 40), (trp_caravan_guard, 15, 30)]),
  ("desert_bandits","Aiel Renegades",icon_axeman|carries_goods(2),0,fac_outlaws,wot_bandit_personality,[(trp_aiel_raider_bandit,10,45), (trp_aiel_runner, 10,45), (trp_dawn_runner, 5, 10), (trp_maiden_of_the_spear, 5, 10)]),
  ("forest_bandits","Forest Raiders",icon_axeman|carries_goods(2),0,fac_forest_bandits,wot_bandit_personality,[(trp_forest_bandit,10,75), (trp_murandy_bowman, 10, 30), (trp_illian_scout, 5, 20), (trp_shienar_spearman, 5, 15), (trp_ghealdan_militia, 10, 25)]),
  ("mountain_bandits","Bandits",icon_axeman|carries_goods(2),0,fac_mountain_bandits,wot_bandit_personality,[(trp_mountain_bandit,10,75), (trp_saldaea_skirmisher, 10, 25), (trp_sedai_recruit_soldier, 10, 25), (trp_murandy_maceman, 10, 25), (trp_andor_bowman, 10, 25), (trp_cairhien_light_cavalry, 10, 25)]),
  ("sea_raiders","Coastal Raiders",icon_axeman|carries_goods(2),0,fac_outlaws,wot_bandit_personality,[(trp_sea_raider,10,50), (trp_tear_recruit,10,25),(trp_altara_dueler,10,25), (trp_altara_knife_thrower, 10, 25), (trp_tarabon_bowman, 10, 25), (trp_illian_militia, 10, 25)]),
  
  ("trollocs","Marauding Trollocs",icon_axeman|carries_goods(2),0,fac_trollocs,wot_trolloc_personality,[(trp_trolloc_grunt_bandit,20,90), (trp_trolloc_hewer,15,40),(trp_trolloc_stalker,15,40),(trp_myrddraal,1,3)]),
  # end edited for TGS
  
  ("deserters","Deserters",icon_vaegir_knight|carries_goods(3),0,fac_deserters,bandit_personality,[]),
    
  ("merchant_caravan","Merchant Caravan",icon_gray_knight|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25)]),
  ("troublesome_bandits","Troublesome Bandits",icon_axeman|carries_goods(9)|pf_quest_party,0,fac_outlaws,bandit_personality,[(trp_bandit,14,55)]),
  ("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,24,58),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),
  ("kidnapped_girl","Kidnapped Girl",icon_woman|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_kidnapped_girl,1,1)]),

  ("village_farmers","Village Farmers",icon_peasant|pf_civilian,0,fac_innocents,merchant_personality,[(trp_farmer,5,10),(trp_peasant_woman,3,8)]),

  ("spy_partners", "Unremarkable Travellers", icon_gray_knight|carries_goods(10)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_caravan_guard,5,11)]),
  ("runaway_serfs","Runaway Serfs",icon_peasant|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_farmer,6,7), (trp_peasant_woman,3,3)]),
  ("spy", "Ordinary Townsman", icon_gray_knight|carries_goods(4)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
  ("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),
##  ("conspirator", "Conspirators", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator,3,4)]),
##  ("conspirator_leader", "Conspirator Leader", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator_leader,1,1)]),
##  ("peasant_rebels", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,bandit_personality,[(trp_peasant_rebel,33,97)]),
##  ("noble_refugees", "Noble Refugees", icon_gray_knight|carries_goods(12)|pf_quest_party,0,fac_noble_refugees,merchant_personality,[(trp_noble_refugee,3,5),(trp_noble_refugee_woman,5,7)]),

  ("forager_party","Foraging Party",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("scout_party","Scouts",icon_gray_knight|carries_goods(1)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
  ("patrol_party","Patrol",icon_gray_knight|carries_goods(2)|pf_show_faction,0,fac_commoners,soldier_personality,[]),
#  ("war_party", "War Party",icon_gray_knight|carries_goods(3),0,fac_commoners,soldier_personality,[]),
  ("messenger_party","Messenger",icon_gray_knight|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("raider_party","Raiders",icon_gray_knight|carries_goods(16)|pf_quest_party,0,fac_commoners,bandit_personality,[]),
  ("raider_captives","Raider Captives",0,0,fac_commoners,0,[(trp_peasant_woman,6,30,pmf_is_prisoner)]),
  ("kingdom_caravan_party","Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,12,40)]),
  ("prisoner_train_party","Prisoner Train",icon_gray_knight|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("default_prisoners","Default Prisoners",0,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),

  ("routed_warriors","Routed Enemies",icon_vaegir_knight,0,fac_commoners,soldier_personality,[]),


# Caravans
  ("center_reinforcements","Reinforcements",icon_axeman|carries_goods(16),0,fac_commoners,soldier_personality,[(trp_townsman,5,30),(trp_watchman,4,20)]),  

  ("kingdom_hero_party","War Party",icon_flagbearer_a|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
  
# Reinforcements
  # each faction includes three party templates. One is less-modernised, one is med-modernised and one is high-modernised
  # less-modernised templates are generally includes 7-14 troops in total, 
  # med-modernised templates are generally includes 5-10 troops in total, 
  # high-modernised templates are generally includes 3-5 troops in total

  # edited for TGS
  # legion
  ("kingdom_1_reinforcements_a", "{!}kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_ashaman_soldier,3,6),(trp_ashaman_dedicated,2,4),(trp_ashaman,2,3),(trp_ashaman_veteran,1,2)]),
  ("kingdom_1_reinforcements_b", "{!}kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_legion_recruit_army,5,10),(trp_legion_infantry,5,10),(trp_legion_heavy_crossbowman,4,8),(trp_legion_lancer,4,8),(trp_legion_bannerman,2,4),(trp_legion_captain,2,4)]),
  ("kingdom_1_reinforcements_c", "{!}kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_ashaman_soldier,3,6),(trp_ashaman_dedicated,2,4),(trp_ashaman,2,3),(trp_ashaman_veteran,1,2)]),
  ("kingdom_1_reinforcements_d", "{!}kingdom_1_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_legion_recruit_army,5,10),(trp_legion_infantry,5,10),(trp_legion_heavy_crossbowman,4,8),(trp_legion_lancer,4,8),(trp_legion_bannerman,2,4),(trp_legion_captain,2,4)]),
  ("kingdom_1_reinforcements_e", "{!}kingdom_1_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_mayene_man_at_arms,3,6),(trp_mayene_lancer,2,4),(trp_mayene_royal_guard,2,4)]),
  ("kingdom_1_reinforcements_f", "{!}kingdom_1_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_legion_andor_ally,3,6),(trp_andor_swordsman,3,6),(trp_andor_blademaster,2,4),(trp_andor_man_at_arms,2,4)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)
  ("kingdom_1_reinforcements_g", "{!}kingdom_1_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_legion_tear_ally,3,6),(trp_tear_bowman,2,4),(trp_tear_lancer,3,6),(trp_tear_heavy_lancer,2,4),(trp_legion_cairhien_ally,3,6),(trp_cairhien_pikeman,2,4)]),
  ("kingdom_1_reinforcements_h", "{!}kingdom_1_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_legion_illian_ally,3,6),(trp_illian_crossbowman,2,4),(trp_illian_marksman,3,6),(trp_illian_man_at_arms,2,4),(trp_cairhien_lancer,2,4)]),

  # band
  ("kingdom_2_reinforcements_a", "{!}kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_red_hand_recruit,5,10),(trp_red_hand_infantry,3,6),(trp_red_hand_pikeman,4,8),(trp_red_hand_crossbowman,4,8),(trp_red_hand_man_at_arms,2,4),(trp_red_hand_light_cavalry,3,6)]),
  ("kingdom_2_reinforcements_b", "{!}kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_red_hand_bannerman,2,4),(trp_red_hand_swordsman,1,2),(trp_red_hand_fast_crossbowman,3,6),(trp_red_hand_lancer,1,3),(trp_red_hand_captain,1,3),(trp_red_hand_skirmisher,1,3)]),
  ("kingdom_2_reinforcements_c", "{!}kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_red_hand_recruit,5,10),(trp_red_hand_infantry,3,6),(trp_red_hand_pikeman,4,8),(trp_red_hand_crossbowman,4,8),(trp_red_hand_man_at_arms,2,4),(trp_red_hand_light_cavalry,3,6)]),
  ("kingdom_2_reinforcements_d", "{!}kingdom_2_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_red_hand_bannerman,2,4),(trp_red_hand_swordsman,1,2),(trp_red_hand_fast_crossbowman,3,6),(trp_red_hand_lancer,1,3),(trp_red_hand_captain,1,3),(trp_red_hand_skirmisher,1,3)]),
  ("kingdom_2_reinforcements_e", "{!}kingdom_2_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_red_hand_recruit,5,10),(trp_red_hand_infantry,3,6),(trp_red_hand_pikeman,4,8),(trp_red_hand_crossbowman,4,8),(trp_red_hand_man_at_arms,2,4),(trp_red_hand_light_cavalry,3,6)]),
  ("kingdom_2_reinforcements_f", "{!}kingdom_2_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_red_hand_bannerman,2,4),(trp_red_hand_swordsman,1,2),(trp_red_hand_fast_crossbowman,3,6),(trp_red_hand_lancer,1,3),(trp_red_hand_captain,1,3),(trp_red_hand_skirmisher,1,3)]),
  ("kingdom_2_reinforcements_g", "{!}kingdom_2_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_red_hand_recruit,5,10),(trp_red_hand_infantry,3,6),(trp_red_hand_pikeman,4,8),(trp_red_hand_crossbowman,4,8),(trp_red_hand_man_at_arms,2,4),(trp_red_hand_light_cavalry,3,6)]),
  ("kingdom_2_reinforcements_h", "{!}kingdom_2_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_red_hand_bannerman,2,4),(trp_red_hand_swordsman,1,2),(trp_red_hand_fast_crossbowman,3,6),(trp_red_hand_lancer,1,3),(trp_red_hand_captain,1,3),(trp_red_hand_skirmisher,1,3)]),

  # two rivers
  ("kingdom_3_reinforcements_a", "{!}kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_two_rivers_farmer,3,6),(trp_two_rivers_spearman,3,6),(trp_two_rivers_halberdier,2,4),(trp_two_rivers_scout,2,4),(trp_two_rivers_longbowman,4,8),(trp_two_rivers_marksman,3,6)]),
  ("kingdom_3_reinforcements_b", "{!}kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_two_rivers_farmer,3,6),(trp_two_rivers_spearman,3,6),(trp_two_rivers_halberdier,2,4),(trp_two_rivers_scout,2,4),(trp_two_rivers_longbowman,4,8),(trp_two_rivers_marksman,3,6)]),
  ("kingdom_3_reinforcements_c", "{!}kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_two_rivers_farmer,3,6),(trp_two_rivers_spearman,3,6),(trp_two_rivers_halberdier,2,4),(trp_two_rivers_scout,2,4),(trp_two_rivers_longbowman,4,8),(trp_two_rivers_marksman,3,6)]),
  ("kingdom_3_reinforcements_d", "{!}kingdom_3_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_two_rivers_farmer,3,6),(trp_two_rivers_spearman,3,6),(trp_two_rivers_halberdier,2,4),(trp_two_rivers_scout,2,4),(trp_two_rivers_longbowman,4,8),(trp_two_rivers_marksman,3,6)]),
  ("kingdom_3_reinforcements_e", "{!}kingdom_3_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_two_rivers_farmer,3,6),(trp_two_rivers_spearman,3,6),(trp_two_rivers_halberdier,2,4),(trp_two_rivers_scout,2,4),(trp_two_rivers_longbowman,4,8),(trp_two_rivers_marksman,3,6)]),
  ("kingdom_3_reinforcements_f", "{!}kingdom_3_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_two_rivers_farmer,3,6),(trp_two_rivers_spearman,3,6),(trp_two_rivers_halberdier,2,4),(trp_two_rivers_scout,2,4),(trp_two_rivers_longbowman,4,8),(trp_two_rivers_marksman,3,6)]),
  ("kingdom_3_reinforcements_g", "{!}kingdom_3_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_two_rivers_farmer,3,6),(trp_two_rivers_spearman,3,6),(trp_two_rivers_halberdier,2,4),(trp_two_rivers_scout,2,4),(trp_two_rivers_longbowman,4,8),(trp_two_rivers_marksman,3,6)]),
  ("kingdom_3_reinforcements_h", "{!}kingdom_3_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_two_rivers_farmer,3,6),(trp_two_rivers_spearman,3,6),(trp_two_rivers_halberdier,2,4),(trp_two_rivers_scout,2,4),(trp_two_rivers_longbowman,4,8),(trp_two_rivers_marksman,3,6)]),

  # mayene
  ("kingdom_4_reinforcements_a", "{!}kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_mayene_recruit,5,10),(trp_mayene_militia,4,8),(trp_mayene_man_at_arms,3,6),(trp_mayene_lancer,2,4)]),
  ("kingdom_4_reinforcements_b", "{!}kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_mayene_swordsman,3,6),(trp_mayene_bowman,3,6),(trp_mayene_royal_guard,1,2)]),
  ("kingdom_4_reinforcements_c", "{!}kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_mayene_recruit,5,10),(trp_mayene_militia,4,8),(trp_mayene_man_at_arms,3,6),(trp_mayene_lancer,2,4)]),
  ("kingdom_4_reinforcements_d", "{!}kingdom_4_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_mayene_swordsman,3,6),(trp_mayene_bowman,3,6),(trp_mayene_royal_guard,1,2)]),
  ("kingdom_4_reinforcements_e", "{!}kingdom_4_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_mayene_recruit,5,10),(trp_mayene_militia,4,8),(trp_mayene_man_at_arms,3,6),(trp_mayene_lancer,2,4)]),
  ("kingdom_4_reinforcements_f", "{!}kingdom_4_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_mayene_swordsman,3,6),(trp_mayene_bowman,3,6),(trp_mayene_royal_guard,1,2)]),
  ("kingdom_4_reinforcements_g", "{!}kingdom_4_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_mayene_recruit,5,10),(trp_mayene_militia,4,8),(trp_mayene_man_at_arms,3,6),(trp_mayene_lancer,2,4)]),
  ("kingdom_4_reinforcements_h", "{!}kingdom_4_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_mayene_swordsman,3,6),(trp_mayene_bowman,3,6),(trp_mayene_royal_guard,1,2)]),

  # cairhien
  ("kingdom_5_reinforcements_a", "{!}kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_cairhien_recruit,5,10),(trp_cairhien_militia,4,8),(trp_cairhien_pikeman,3,6),(trp_cairhien_man_at_arms,3,6)]),
  ("kingdom_5_reinforcements_b", "{!}kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_cairhien_bannerman,2,4),(trp_cairhien_crossbowman,3,6),(trp_cairhien_light_cavalry,3,6),(trp_cairhien_lancer,2,4)]),
  ("kingdom_5_reinforcements_c", "{!}kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_cairhien_recruit,5,10),(trp_cairhien_militia,4,8),(trp_cairhien_pikeman,3,6),(trp_cairhien_man_at_arms,3,6)]),
  ("kingdom_5_reinforcements_d", "{!}kingdom_5_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_cairhien_bannerman,2,4),(trp_cairhien_crossbowman,3,6),(trp_cairhien_light_cavalry,3,6),(trp_cairhien_lancer,2,4)]),
  ("kingdom_5_reinforcements_e", "{!}kingdom_5_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_cairhien_recruit,5,10),(trp_cairhien_militia,4,8),(trp_cairhien_pikeman,3,6),(trp_cairhien_man_at_arms,3,6)]),
  ("kingdom_5_reinforcements_f", "{!}kingdom_5_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_cairhien_bannerman,2,4),(trp_cairhien_crossbowman,3,6),(trp_cairhien_light_cavalry,3,6),(trp_cairhien_lancer,2,4)]),
  ("kingdom_5_reinforcements_g", "{!}kingdom_5_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_cairhien_recruit,5,10),(trp_cairhien_militia,4,8),(trp_cairhien_pikeman,3,6),(trp_cairhien_man_at_arms,3,6)]),
  ("kingdom_5_reinforcements_h", "{!}kingdom_5_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_cairhien_bannerman,2,4),(trp_cairhien_crossbowman,3,6),(trp_cairhien_light_cavalry,3,6),(trp_cairhien_lancer,2,4)]),

  # illian
  ("kingdom_6_reinforcements_a", "{!}kingdom_6_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_illian_recruit,5,10),(trp_illian_militia,4,8),(trp_illian_swordsman,3,6),(trp_illian_companion,2,4),(trp_illian_bowman,3,6),(trp_illian_crossbowman,2,4)]),
  ("kingdom_6_reinforcements_b", "{!}kingdom_6_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_illian_scout,3,6),(trp_illian_companion_captain,1,2),(trp_illian_marksman,2,4),(trp_illian_man_at_arms,2,4)]),
  ("kingdom_6_reinforcements_c", "{!}kingdom_6_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_illian_recruit,5,10),(trp_illian_militia,4,8),(trp_illian_swordsman,3,6),(trp_illian_companion,2,4),(trp_illian_bowman,3,6),(trp_illian_crossbowman,2,4)]),
  ("kingdom_6_reinforcements_d", "{!}kingdom_6_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_illian_scout,3,6),(trp_illian_companion_captain,1,2),(trp_illian_marksman,2,4),(trp_illian_man_at_arms,2,4)]),
  ("kingdom_6_reinforcements_e", "{!}kingdom_6_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_illian_recruit,5,10),(trp_illian_militia,4,8),(trp_illian_swordsman,3,6),(trp_illian_companion,2,4),(trp_illian_bowman,3,6),(trp_illian_crossbowman,2,4)]),
  ("kingdom_6_reinforcements_f", "{!}kingdom_6_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_illian_scout,3,6),(trp_illian_companion_captain,1,2),(trp_illian_marksman,2,4),(trp_illian_man_at_arms,2,4)]),
  ("kingdom_6_reinforcements_g", "{!}kingdom_6_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_illian_recruit,5,10),(trp_illian_militia,4,8),(trp_illian_swordsman,3,6),(trp_illian_companion,2,4),(trp_illian_bowman,3,6),(trp_illian_crossbowman,2,4)]),
  ("kingdom_6_reinforcements_h", "{!}kingdom_6_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_illian_scout,3,6),(trp_illian_companion_captain,1,2),(trp_illian_marksman,2,4),(trp_illian_man_at_arms,2,4)]),

  # murandy
  ("kingdom_7_reinforcements_a", "{!}kingdom_7_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_murandy_recruit,5,10),(trp_murandy_militia,4,8),(trp_murandy_maceman,3,6),(trp_murandy_bowman,4,8),(trp_murandy_scout,3,6),(trp_murandy_lancer,2,4)]),
  ("kingdom_7_reinforcements_b", "{!}kingdom_7_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_murandy_berserker,2,4),(trp_murandy_marksman,2,4),(trp_murandy_captain,1,2)]),
  ("kingdom_7_reinforcements_c", "{!}kingdom_7_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_murandy_recruit,5,10),(trp_murandy_militia,4,8),(trp_murandy_maceman,3,6),(trp_murandy_bowman,4,8),(trp_murandy_scout,3,6),(trp_murandy_lancer,2,4)]),
  ("kingdom_7_reinforcements_d", "{!}kingdom_7_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_murandy_berserker,2,4),(trp_murandy_marksman,2,4),(trp_murandy_captain,1,2)]),
  ("kingdom_7_reinforcements_e", "{!}kingdom_7_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_murandy_recruit,5,10),(trp_murandy_militia,4,8),(trp_murandy_maceman,3,6),(trp_murandy_bowman,4,8),(trp_murandy_scout,3,6),(trp_murandy_lancer,2,4)]),
  ("kingdom_7_reinforcements_f", "{!}kingdom_7_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_murandy_berserker,2,4),(trp_murandy_marksman,2,4),(trp_murandy_captain,1,2)]),
  ("kingdom_7_reinforcements_g", "{!}kingdom_7_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_murandy_recruit,5,10),(trp_murandy_militia,4,8),(trp_murandy_maceman,3,6),(trp_murandy_bowman,4,8),(trp_murandy_scout,3,6),(trp_murandy_lancer,2,4)]),
  ("kingdom_7_reinforcements_h", "{!}kingdom_7_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_murandy_berserker,2,4),(trp_murandy_marksman,2,4),(trp_murandy_captain,1,2)]),

  # altara
  ("kingdom_8_reinforcements_a", "{!}kingdom_8_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_altara_recruit,5,10),(trp_altara_dueler,4,8),(trp_altara_swordsman,3,6),(trp_altara_scout,3,6)]),
  ("kingdom_8_reinforcements_b", "{!}kingdom_8_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_altara_royal_guard,2,4),(trp_altara_knife_thrower,4,8),(trp_altara_man_at_arms,2,4),(trp_altara_skirmisher,2,4)]),
  ("kingdom_8_reinforcements_c", "{!}kingdom_8_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_altara_recruit,5,10),(trp_altara_dueler,4,8),(trp_altara_swordsman,3,6),(trp_altara_scout,3,6)]),
  ("kingdom_8_reinforcements_d", "{!}kingdom_8_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_altara_royal_guard,2,4),(trp_altara_knife_thrower,4,8),(trp_altara_man_at_arms,2,4),(trp_altara_skirmisher,2,4)]),
  ("kingdom_8_reinforcements_e", "{!}kingdom_8_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_altara_recruit,5,10),(trp_altara_dueler,4,8),(trp_altara_swordsman,3,6),(trp_altara_scout,3,6)]),
  ("kingdom_8_reinforcements_f", "{!}kingdom_8_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_altara_royal_guard,2,4),(trp_altara_knife_thrower,4,8),(trp_altara_man_at_arms,2,4),(trp_altara_skirmisher,2,4)]),
  ("kingdom_8_reinforcements_g", "{!}kingdom_8_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_altara_recruit,5,10),(trp_altara_dueler,4,8),(trp_altara_swordsman,3,6),(trp_altara_scout,3,6)]),
  ("kingdom_8_reinforcements_h", "{!}kingdom_8_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_altara_royal_guard,2,4),(trp_altara_knife_thrower,4,8),(trp_altara_man_at_arms,2,4),(trp_altara_skirmisher,2,4)]),

  # arad doman
  ("kingdom_9_reinforcements_a", "{!}kingdom_9_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_arad_doman_recruit,3,6),(trp_arad_doman_rabble,5,10),(trp_arad_doman_swordsman,3,6),(trp_arad_doman_scout,3,6)]),
  ("kingdom_9_reinforcements_b", "{!}kingdom_9_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_arad_doman_long_swordsman,2,4),(trp_arad_doman_bowman,4,8),(trp_arad_doman_man_at_arms,2,4)]),
  ("kingdom_9_reinforcements_c", "{!}kingdom_9_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_arad_doman_recruit,3,6),(trp_arad_doman_rabble,5,10),(trp_arad_doman_swordsman,3,6),(trp_arad_doman_scout,3,6)]),
  ("kingdom_9_reinforcements_d", "{!}kingdom_9_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_arad_doman_long_swordsman,2,4),(trp_arad_doman_bowman,4,8),(trp_arad_doman_man_at_arms,2,4)]),
  ("kingdom_9_reinforcements_e", "{!}kingdom_9_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_arad_doman_recruit,3,6),(trp_arad_doman_rabble,5,10),(trp_arad_doman_swordsman,3,6),(trp_arad_doman_scout,3,6)]),
  ("kingdom_9_reinforcements_f", "{!}kingdom_9_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_arad_doman_long_swordsman,2,4),(trp_arad_doman_bowman,4,8),(trp_arad_doman_man_at_arms,2,4)]),
  ("kingdom_9_reinforcements_g", "{!}kingdom_9_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_arad_doman_recruit,3,6),(trp_arad_doman_rabble,5,10),(trp_arad_doman_swordsman,3,6),(trp_arad_doman_scout,3,6)]),
  ("kingdom_9_reinforcements_h", "{!}kingdom_9_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_arad_doman_long_swordsman,2,4),(trp_arad_doman_bowman,4,8),(trp_arad_doman_man_at_arms,2,4)]),

  # tear
  ("kingdom_10_reinforcements_a", "{!}kingdom_10_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_tear_recruit,5,10),(trp_tear_town_watch,4,8),(trp_tear_swordsman,3,6),(trp_tear_defender,2,4),(trp_tear_bowman,4,8),(trp_tear_scout,4,8)]),
  ("kingdom_10_reinforcements_b", "{!}kingdom_10_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_tear_lancer,3,6),(trp_tear_blademaster,1,2),(trp_tear_defender_captain,1,2),(trp_tear_crossbowman,2,4),(trp_tear_light_cavalry,3,6),(trp_tear_heavy_lancer,2,4)]),
  ("kingdom_10_reinforcements_c", "{!}kingdom_10_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_tear_recruit,5,10),(trp_tear_town_watch,4,8),(trp_tear_swordsman,3,6),(trp_tear_defender,2,4),(trp_tear_bowman,4,8),(trp_tear_scout,4,8)]),
  ("kingdom_10_reinforcements_d", "{!}kingdom_10_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_tear_lancer,3,6),(trp_tear_blademaster,1,2),(trp_tear_defender_captain,1,2),(trp_tear_crossbowman,2,4),(trp_tear_light_cavalry,3,6),(trp_tear_heavy_lancer,2,4)]),
  ("kingdom_10_reinforcements_e", "{!}kingdom_10_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_tear_recruit,5,10),(trp_tear_town_watch,4,8),(trp_tear_swordsman,3,6),(trp_tear_defender,2,4),(trp_tear_bowman,4,8),(trp_tear_scout,4,8)]),
  ("kingdom_10_reinforcements_f", "{!}kingdom_10_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_tear_lancer,3,6),(trp_tear_blademaster,1,2),(trp_tear_defender_captain,1,2),(trp_tear_crossbowman,2,4),(trp_tear_light_cavalry,3,6),(trp_tear_heavy_lancer,2,4)]),
  ("kingdom_10_reinforcements_g", "{!}kingdom_10_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_tear_recruit,5,10),(trp_tear_town_watch,4,8),(trp_tear_swordsman,3,6),(trp_tear_defender,2,4),(trp_tear_bowman,4,8),(trp_tear_scout,4,8)]),
  ("kingdom_10_reinforcements_h", "{!}kingdom_10_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_tear_lancer,3,6),(trp_tear_blademaster,1,2),(trp_tear_defender_captain,1,2),(trp_tear_crossbowman,2,4),(trp_tear_light_cavalry,3,6),(trp_tear_heavy_lancer,2,4)]),

  # andor
  ("kingdom_11_reinforcements_a", "{!}kingdom_11_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_andor_recruit,5,10),(trp_andor_militia,4,8),(trp_andor_swordsman,3,6),(trp_andor_bowman,4,8),(trp_andor_scout,4,8),(trp_andor_lancer,3,6)]),
  ("kingdom_11_reinforcements_b", "{!}kingdom_11_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_andor_queens_guard,2,4),(trp_andor_blademaster,1,2),(trp_andor_halberdier,2,4),(trp_andor_crossbowman,3,4),(trp_andor_man_at_arms,3,6),(trp_andor_bannerman,1,2)]),
  ("kingdom_11_reinforcements_c", "{!}kingdom_11_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_andor_recruit,5,10),(trp_andor_militia,4,8),(trp_andor_swordsman,3,6),(trp_andor_bowman,4,8),(trp_andor_scout,4,8),(trp_andor_lancer,3,6)]),
  ("kingdom_11_reinforcements_d", "{!}kingdom_11_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_andor_queens_guard,2,4),(trp_andor_blademaster,1,2),(trp_andor_halberdier,2,4),(trp_andor_crossbowman,3,4),(trp_andor_man_at_arms,3,6),(trp_andor_bannerman,1,2)]),
  ("kingdom_11_reinforcements_e", "{!}kingdom_11_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_andor_recruit,5,10),(trp_andor_militia,4,8),(trp_andor_swordsman,3,6),(trp_andor_bowman,4,8),(trp_andor_scout,4,8),(trp_andor_lancer,3,6)]),
  ("kingdom_11_reinforcements_f", "{!}kingdom_11_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_andor_queens_guard,2,4),(trp_andor_blademaster,1,2),(trp_andor_halberdier,2,4),(trp_andor_crossbowman,3,4),(trp_andor_man_at_arms,3,6),(trp_andor_bannerman,1,2)]),
  ("kingdom_11_reinforcements_g", "{!}kingdom_11_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_andor_recruit,5,10),(trp_andor_militia,4,8),(trp_andor_swordsman,3,6),(trp_andor_bowman,4,8),(trp_andor_scout,4,8),(trp_andor_lancer,3,6)]),
  ("kingdom_11_reinforcements_h", "{!}kingdom_11_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_andor_queens_guard,2,4),(trp_andor_blademaster,1,2),(trp_andor_halberdier,2,4),(trp_andor_crossbowman,3,4),(trp_andor_man_at_arms,3,6),(trp_andor_bannerman,1,2)]),

  # ghealdan
  ("kingdom_12_reinforcements_a", "{!}kingdom_12_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_ghealdan_recruit,5,10),(trp_ghealdan_militia,4,8),(trp_ghealdan_axeman,3,6),(trp_ghealdan_bowman,4,8),(trp_ghealdan_scout,4,8),(trp_ghealdan_lancer,3,6)]),
  ("kingdom_12_reinforcements_b", "{!}kingdom_12_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_ghealdan_heavy_axeman,2,4),(trp_ghealdan_marksman,2,4),(trp_ghealdan_man_at_arms,3,6),(trp_ghealdan_royal_guard,2,4)]),
  ("kingdom_12_reinforcements_c", "{!}kingdom_12_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_ghealdan_recruit,5,10),(trp_ghealdan_militia,4,8),(trp_ghealdan_axeman,3,6),(trp_ghealdan_bowman,4,8),(trp_ghealdan_scout,4,8),(trp_ghealdan_lancer,3,6)]),
  ("kingdom_12_reinforcements_d", "{!}kingdom_12_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_ghealdan_heavy_axeman,2,4),(trp_ghealdan_marksman,2,4),(trp_ghealdan_man_at_arms,3,6),(trp_ghealdan_royal_guard,2,4)]),
  ("kingdom_12_reinforcements_e", "{!}kingdom_12_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_ghealdan_recruit,5,10),(trp_ghealdan_militia,4,8),(trp_ghealdan_axeman,3,6),(trp_ghealdan_bowman,4,8),(trp_ghealdan_scout,4,8),(trp_ghealdan_lancer,3,6)]),
  ("kingdom_12_reinforcements_f", "{!}kingdom_12_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_ghealdan_heavy_axeman,2,4),(trp_ghealdan_marksman,2,4),(trp_ghealdan_man_at_arms,3,6),(trp_ghealdan_royal_guard,2,4)]),
  ("kingdom_12_reinforcements_g", "{!}kingdom_12_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_ghealdan_recruit,5,10),(trp_ghealdan_militia,4,8),(trp_ghealdan_axeman,3,6),(trp_ghealdan_bowman,4,8),(trp_ghealdan_scout,4,8),(trp_ghealdan_lancer,3,6)]),
  ("kingdom_12_reinforcements_h", "{!}kingdom_12_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_ghealdan_heavy_axeman,2,4),(trp_ghealdan_marksman,2,4),(trp_ghealdan_man_at_arms,3,6),(trp_ghealdan_royal_guard,2,4)]),

  # far madding
  ("kingdom_13_reinforcements_a", "{!}kingdom_13_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_far_madding_recruit,5,10),(trp_far_madding_footman,4,8),(trp_far_madding_city_guard,3,6),(trp_far_madding_crossbowman,4,8)]),
  ("kingdom_13_reinforcements_b", "{!}kingdom_13_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_far_madding_recruit,5,10),(trp_far_madding_footman,4,8),(trp_far_madding_city_guard,3,6),(trp_far_madding_crossbowman,4,8)]),
  ("kingdom_13_reinforcements_c", "{!}kingdom_13_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_far_madding_recruit,5,10),(trp_far_madding_footman,4,8),(trp_far_madding_city_guard,3,6),(trp_far_madding_crossbowman,4,8)]),
  ("kingdom_13_reinforcements_d", "{!}kingdom_13_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_far_madding_recruit,5,10),(trp_far_madding_footman,4,8),(trp_far_madding_city_guard,3,6),(trp_far_madding_crossbowman,4,8)]),
  ("kingdom_13_reinforcements_e", "{!}kingdom_13_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_far_madding_recruit,5,10),(trp_far_madding_footman,4,8),(trp_far_madding_city_guard,3,6),(trp_far_madding_crossbowman,4,8)]),
  ("kingdom_13_reinforcements_f", "{!}kingdom_13_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_far_madding_recruit,5,10),(trp_far_madding_footman,4,8),(trp_far_madding_city_guard,3,6),(trp_far_madding_crossbowman,4,8)]),
  ("kingdom_13_reinforcements_g", "{!}kingdom_13_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_far_madding_recruit,5,10),(trp_far_madding_footman,4,8),(trp_far_madding_city_guard,3,6),(trp_far_madding_crossbowman,4,8)]),
  ("kingdom_13_reinforcements_h", "{!}kingdom_13_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_far_madding_recruit,5,10),(trp_far_madding_footman,4,8),(trp_far_madding_city_guard,3,6),(trp_far_madding_crossbowman,4,8)]),

  # tarabon
  ("kingdom_14_reinforcements_a", "{!}kingdom_14_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_tarabon_recruit,3,6),(trp_tarabon_rabble,5,10),(trp_tarabon_bowman,4,8),(trp_tarabon_scout,4,8)]),
  ("kingdom_14_reinforcements_b", "{!}kingdom_14_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_tarabon_spearman,3,6),(trp_tarabon_marksman,3,6),(trp_tarabon_lancer,3,6),(trp_tarabon_skirmisher,3,6)]),
  ("kingdom_14_reinforcements_c", "{!}kingdom_14_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_tarabon_recruit,3,6),(trp_tarabon_rabble,5,10),(trp_tarabon_bowman,4,8),(trp_tarabon_scout,4,8)]),
  ("kingdom_14_reinforcements_d", "{!}kingdom_14_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_tarabon_spearman,3,6),(trp_tarabon_marksman,3,6),(trp_tarabon_lancer,3,6),(trp_tarabon_skirmisher,3,6)]),
  ("kingdom_14_reinforcements_e", "{!}kingdom_14_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_tarabon_recruit,3,6),(trp_tarabon_rabble,5,10),(trp_tarabon_bowman,4,8),(trp_tarabon_scout,4,8)]),
  ("kingdom_14_reinforcements_f", "{!}kingdom_14_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_tarabon_spearman,3,6),(trp_tarabon_marksman,3,6),(trp_tarabon_lancer,3,6),(trp_tarabon_skirmisher,3,6)]),
  ("kingdom_14_reinforcements_g", "{!}kingdom_14_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_tarabon_recruit,3,6),(trp_tarabon_rabble,5,10),(trp_tarabon_bowman,4,8),(trp_tarabon_scout,4,8)]),
  ("kingdom_14_reinforcements_h", "{!}kingdom_14_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_tarabon_spearman,3,6),(trp_tarabon_marksman,3,6),(trp_tarabon_lancer,3,6),(trp_tarabon_skirmisher,3,6)]),

  # amadicia
  ("kingdom_15_reinforcements_a", "{!}kingdom_15_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_amadicia_recruit,5,10),(trp_amadicia_militia,4,8),(trp_amadicia_pikeman,3,6),(trp_amadicia_bowman,4,8),(trp_amadicia_captain,2,4),(trp_amadicia_skirmisher,2,4)]),
  ("kingdom_15_reinforcements_b", "{!}kingdom_15_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_amadicia_recruit,5,10),(trp_amadicia_militia,4,8),(trp_amadicia_pikeman,3,6),(trp_amadicia_bowman,4,8),(trp_amadicia_captain,2,4),(trp_amadicia_skirmisher,2,4)]),
  ("kingdom_15_reinforcements_c", "{!}kingdom_15_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_amadicia_recruit,5,10),(trp_amadicia_militia,4,8),(trp_amadicia_pikeman,3,6),(trp_amadicia_bowman,4,8),(trp_amadicia_captain,2,4),(trp_amadicia_skirmisher,2,4)]),
  ("kingdom_15_reinforcements_d", "{!}kingdom_15_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_amadicia_recruit,5,10),(trp_amadicia_militia,4,8),(trp_amadicia_pikeman,3,6),(trp_amadicia_bowman,4,8),(trp_amadicia_captain,2,4),(trp_amadicia_skirmisher,2,4)]),
  ("kingdom_15_reinforcements_e", "{!}kingdom_15_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_amadicia_recruit,5,10),(trp_amadicia_militia,4,8),(trp_amadicia_pikeman,3,6),(trp_amadicia_bowman,4,8),(trp_amadicia_captain,2,4),(trp_amadicia_skirmisher,2,4)]),
  ("kingdom_15_reinforcements_f", "{!}kingdom_15_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_amadicia_recruit,5,10),(trp_amadicia_militia,4,8),(trp_amadicia_pikeman,3,6),(trp_amadicia_bowman,4,8),(trp_amadicia_captain,2,4),(trp_amadicia_skirmisher,2,4)]),
  ("kingdom_15_reinforcements_g", "{!}kingdom_15_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_amadicia_recruit,5,10),(trp_amadicia_militia,4,8),(trp_amadicia_pikeman,3,6),(trp_amadicia_bowman,4,8),(trp_amadicia_captain,2,4),(trp_amadicia_skirmisher,2,4)]),
  ("kingdom_15_reinforcements_h", "{!}kingdom_15_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_amadicia_recruit,5,10),(trp_amadicia_militia,4,8),(trp_amadicia_pikeman,3,6),(trp_amadicia_bowman,4,8),(trp_amadicia_captain,2,4),(trp_amadicia_skirmisher,2,4)]),

  # whitecloaks
  ("kingdom_16_reinforcements_a", "{!}kingdom_16_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_whitecloak_recruit,5,10),(trp_whitecloak_footman,4,8),(trp_whitecloak_swordsman,3,6),(trp_whitecloak_bowman,4,8),(trp_whitecloak_man_at_arms,3,6)]),
  ("kingdom_16_reinforcements_b", "{!}kingdom_16_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_whitecloak_captain,2,4),(trp_whitecloak_crossbowman,3,6),(trp_whitecloak_lancer,3,6)]),
  ("kingdom_16_reinforcements_c", "{!}kingdom_16_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_whitecloak_recruit,5,10),(trp_whitecloak_footman,4,8),(trp_whitecloak_swordsman,3,6),(trp_whitecloak_bowman,4,8),(trp_whitecloak_man_at_arms,3,6)]),
  ("kingdom_16_reinforcements_d", "{!}kingdom_16_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_whitecloak_captain,2,4),(trp_whitecloak_crossbowman,3,6),(trp_whitecloak_lancer,3,6)]),
  ("kingdom_16_reinforcements_e", "{!}kingdom_16_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_whitecloak_recruit,5,10),(trp_whitecloak_footman,4,8),(trp_whitecloak_swordsman,3,6),(trp_whitecloak_bowman,4,8),(trp_whitecloak_man_at_arms,3,6)]),
  ("kingdom_16_reinforcements_f", "{!}kingdom_16_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_whitecloak_captain,2,4),(trp_whitecloak_crossbowman,3,6),(trp_whitecloak_lancer,3,6)]),
  ("kingdom_16_reinforcements_g", "{!}kingdom_16_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_whitecloak_recruit,5,10),(trp_whitecloak_footman,4,8),(trp_whitecloak_swordsman,3,6),(trp_whitecloak_bowman,4,8),(trp_whitecloak_man_at_arms,3,6)]),
  ("kingdom_16_reinforcements_h", "{!}kingdom_16_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_whitecloak_captain,2,4),(trp_whitecloak_crossbowman,3,6),(trp_whitecloak_lancer,3,6)]),

  # shienar
  ("kingdom_17_reinforcements_a", "{!}kingdom_17_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_shienar_recruit,5,10),(trp_shienar_militia,4,8),(trp_shienar_spearman,3,6),(trp_shienar_swordsman,3,6),(trp_shienar_bowman,4,8),(trp_shienar_light_cavalry,4,8)]),
  ("kingdom_17_reinforcements_b", "{!}kingdom_17_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_shienar_lancer,3,6),(trp_shienar_heavy_lancer,2,4),(trp_shienar_pikeman,2,4),(trp_shienar_blademaster,1,3)]),
  ("kingdom_17_reinforcements_c", "{!}kingdom_17_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_shienar_marksman,3,6),(trp_shienar_crossbowman,3,6),(trp_shienar_captain,1,3)]),
  ("kingdom_17_reinforcements_d", "{!}kingdom_17_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_shienar_recruit,5,10),(trp_shienar_militia,4,8),(trp_shienar_spearman,3,6),(trp_shienar_swordsman,3,6),(trp_shienar_bowman,4,8),(trp_shienar_light_cavalry,4,8)]),
  ("kingdom_17_reinforcements_e", "{!}kingdom_17_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_shienar_lancer,3,6),(trp_shienar_heavy_lancer,2,4),(trp_shienar_pikeman,2,4),(trp_shienar_blademaster,1,3)]),
  ("kingdom_17_reinforcements_f", "{!}kingdom_17_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_shienar_marksman,3,6),(trp_shienar_crossbowman,3,6),(trp_shienar_captain,1,3)]),
  ("kingdom_17_reinforcements_g", "{!}kingdom_17_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_shienar_recruit,5,10),(trp_shienar_militia,4,8),(trp_shienar_spearman,3,6),(trp_shienar_swordsman,3,6),(trp_shienar_bowman,4,8),(trp_shienar_light_cavalry,4,8)]),
  ("kingdom_17_reinforcements_h", "{!}kingdom_17_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_shienar_lancer,3,6),(trp_shienar_heavy_lancer,2,4),(trp_shienar_pikeman,2,4),(trp_shienar_blademaster,1,3)]),

  # arafel
  ("kingdom_18_reinforcements_a", "{!}kingdom_18_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_arafel_recruit,5,10),(trp_arafel_militia,4,8),(trp_arafel_swordsman,3,6),(trp_arafel_halberdier,3,6),(trp_arafel_bowman,4,8),(trp_arafel_man_at_arms,3,6)]),
  ("kingdom_18_reinforcements_b", "{!}kingdom_18_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_arafel_blademaster,2,4),(trp_arafel_bannerman,1,2),(trp_arafel_marksman,2,4),(trp_arafel_lancer,2,4),(trp_arafel_skirmisher,3,6)]),
  ("kingdom_18_reinforcements_c", "{!}kingdom_18_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_arafel_recruit,5,10),(trp_arafel_militia,4,8),(trp_arafel_swordsman,3,6),(trp_arafel_halberdier,3,6),(trp_arafel_bowman,4,8),(trp_arafel_man_at_arms,3,6)]),
  ("kingdom_18_reinforcements_d", "{!}kingdom_18_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_arafel_blademaster,2,4),(trp_arafel_bannerman,1,2),(trp_arafel_marksman,2,4),(trp_arafel_lancer,2,4),(trp_arafel_skirmisher,3,6)]),
  ("kingdom_18_reinforcements_e", "{!}kingdom_18_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_arafel_recruit,5,10),(trp_arafel_militia,4,8),(trp_arafel_swordsman,3,6),(trp_arafel_halberdier,3,6),(trp_arafel_bowman,4,8),(trp_arafel_man_at_arms,3,6)]),
  ("kingdom_18_reinforcements_f", "{!}kingdom_18_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_arafel_blademaster,2,4),(trp_arafel_bannerman,1,2),(trp_arafel_marksman,2,4),(trp_arafel_lancer,2,4),(trp_arafel_skirmisher,3,6)]),
  ("kingdom_18_reinforcements_g", "{!}kingdom_18_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_arafel_recruit,5,10),(trp_arafel_militia,4,8),(trp_arafel_swordsman,3,6),(trp_arafel_halberdier,3,6),(trp_arafel_bowman,4,8),(trp_arafel_man_at_arms,3,6)]),
  ("kingdom_18_reinforcements_h", "{!}kingdom_18_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_arafel_blademaster,2,4),(trp_arafel_bannerman,1,2),(trp_arafel_marksman,2,4),(trp_arafel_lancer,2,4),(trp_arafel_skirmisher,3,6)]),

  # kandor
  ("kingdom_19_reinforcements_a", "{!}kingdom_19_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_kandor_recruit,5,10),(trp_kandor_militia,4,5),(trp_kandor_axeman,3,6),(trp_kandor_berserker,2,4),(trp_kandor_bowman,4,8),(trp_kandor_man_at_arms,3,6)]),
  ("kingdom_19_reinforcements_b", "{!}kingdom_19_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_kandor_captain,1,3),(trp_kandor_maceman,2,4),(trp_kandor_crossbowman,3,6),(trp_kandor_heavy_horseman,2,4),(trp_kandor_skirmisher,2,4)]),
  ("kingdom_19_reinforcements_c", "{!}kingdom_19_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_kandor_recruit,5,10),(trp_kandor_militia,4,5),(trp_kandor_axeman,3,6),(trp_kandor_berserker,2,4),(trp_kandor_bowman,4,8),(trp_kandor_man_at_arms,3,6)]),
  ("kingdom_19_reinforcements_d", "{!}kingdom_19_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_kandor_captain,1,3),(trp_kandor_maceman,2,4),(trp_kandor_crossbowman,3,6),(trp_kandor_heavy_horseman,2,4),(trp_kandor_skirmisher,2,4)]),
  ("kingdom_19_reinforcements_e", "{!}kingdom_19_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_kandor_recruit,5,10),(trp_kandor_militia,4,5),(trp_kandor_axeman,3,6),(trp_kandor_berserker,2,4),(trp_kandor_bowman,4,8),(trp_kandor_man_at_arms,3,6)]),
  ("kingdom_19_reinforcements_f", "{!}kingdom_19_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_kandor_captain,1,3),(trp_kandor_maceman,2,4),(trp_kandor_crossbowman,3,6),(trp_kandor_heavy_horseman,2,4),(trp_kandor_skirmisher,2,4)]),
  ("kingdom_19_reinforcements_g", "{!}kingdom_19_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_kandor_recruit,5,10),(trp_kandor_militia,4,5),(trp_kandor_axeman,3,6),(trp_kandor_berserker,2,4),(trp_kandor_bowman,4,8),(trp_kandor_man_at_arms,3,6)]),
  ("kingdom_19_reinforcements_h", "{!}kingdom_19_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_kandor_captain,1,3),(trp_kandor_maceman,2,4),(trp_kandor_crossbowman,3,6),(trp_kandor_heavy_horseman,2,4),(trp_kandor_skirmisher,2,4)]),

  # saldaea - uy7huy7hdtyuhitdyuh7i8 (code from cecily's typing - pretty accomplished for being 1 month old)
  ("kingdom_20_reinforcements_a", "{!}kingdom_20_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_saldaea_recruit,5,10),(trp_saldaea_militia,4,8),(trp_saldaea_swordsman,3,6),(trp_saldaea_bowman,4,8),(trp_saldaea_cavalry,4,8),(trp_saldaea_light_cavalry,3,6)]),
  ("kingdom_20_reinforcements_b", "{!}kingdom_20_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_saldaea_elite_light_cavalry,2,4),(trp_saldaea_skirmisher,3,6),(trp_saldaea_bannerman,2,4),(trp_saldaea_halberdier,3,6)]),
  ("kingdom_20_reinforcements_c", "{!}kingdom_20_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_saldaea_marksman,3,5),(trp_saldaea_quartermaster,1,3),(trp_saldaea_elite_skirmisher,1,3)]),
  ("kingdom_20_reinforcements_d", "{!}kingdom_20_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_saldaea_recruit,5,10),(trp_saldaea_militia,4,8),(trp_saldaea_swordsman,3,6),(trp_saldaea_bowman,4,8),(trp_saldaea_cavalry,4,8),(trp_saldaea_light_cavalry,3,6)]),
  ("kingdom_20_reinforcements_e", "{!}kingdom_20_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_saldaea_elite_light_cavalry,2,4),(trp_saldaea_skirmisher,3,6),(trp_saldaea_bannerman,2,4),(trp_saldaea_halberdier,3,6)]),
  ("kingdom_20_reinforcements_f", "{!}kingdom_20_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_saldaea_marksman,3,5),(trp_saldaea_quartermaster,1,3),(trp_saldaea_elite_skirmisher,1,3)]),
  ("kingdom_20_reinforcements_g", "{!}kingdom_20_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_saldaea_recruit,5,10),(trp_saldaea_militia,4,8),(trp_saldaea_swordsman,3,6),(trp_saldaea_bowman,4,8),(trp_saldaea_cavalry,4,8),(trp_saldaea_light_cavalry,3,6)]),
  ("kingdom_20_reinforcements_h", "{!}kingdom_20_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_saldaea_elite_light_cavalry,2,4),(trp_saldaea_skirmisher,3,6),(trp_saldaea_bannerman,2,4),(trp_saldaea_halberdier,3,6)]),

  # white tower
  ("kingdom_21_reinforcements_a", "{!}kingdom_21_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sedai_recruit_soldier,10,15),(trp_tar_valon_street_patrol,8,12),(trp_tower_guard_infantry,5,10),(trp_tower_guard_captain,2,4),(trp_tower_guard_crossbowman,5,10)]),
  ("kingdom_21_reinforcements_b", "{!}kingdom_21_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sedai_recruit_soldier,10,15),(trp_tar_valon_street_patrol,8,12),(trp_tower_guard_infantry,5,10),(trp_tower_guard_captain,2,4),(trp_tower_guard_crossbowman,5,10)]),
  ("kingdom_21_reinforcements_c", "{!}kingdom_21_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sedai_recruit_soldier,10,15),(trp_tar_valon_street_patrol,8,12),(trp_tower_guard_infantry,5,10),(trp_tower_guard_captain,2,4),(trp_tower_guard_crossbowman,5,10)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)
  ("kingdom_21_reinforcements_d", "{!}kingdom_21_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_warder_trainee,4,8),(trp_youngling_infantry,3,6),(trp_youngling_cavalry,3,6)]),
  ("kingdom_21_reinforcements_e", "{!}kingdom_21_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_novice_social,1,2),(trp_accepted_medical,2,3),(trp_aes_sedai_yellow,2,3),(trp_aes_sedai_yellow_veteran,1,2)]),
  ("kingdom_21_reinforcements_f", "{!}kingdom_21_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_novice_social,1,2),(trp_accepted_academic,2,3),(trp_aes_sedai_brown,2,3),(trp_aes_sedai_brown_veteran,1,2),(trp_aes_sedai_white,2,3),(trp_aes_sedai_white_veteran,1,2)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)
  ("kingdom_21_reinforcements_g", "{!}kingdom_21_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_novice_civil,1,2),(trp_accepted_political,2,3),(trp_aes_sedai_blue,2,3),(trp_aes_sedai_blue_veteran,1,2),(trp_aes_sedai_grey,2,3),(trp_aes_sedai_grey_veteran,1,2)]),
  ("kingdom_21_reinforcements_h", "{!}kingdom_21_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_novice_civil,1,2),(trp_accepted_military,2,3),(trp_aes_sedai_red,2,3),(trp_aes_sedai_red_veteran,1,2),(trp_aes_sedai_green,2,3),(trp_aes_sedai_green_veteran,1,2)]),

  # aiel
  ("kingdom_22_reinforcements_a", "{!}kingdom_22_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_wise_one_apprentice,2,4),(trp_wise_one,3,5),(trp_wise_one_dream_walker,2,3)]),
  ("kingdom_22_reinforcements_b", "{!}kingdom_22_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_wise_one_apprentice,2,4),(trp_wise_one,3,5),(trp_wise_one_dream_walker,2,3)]),
  ("kingdom_22_reinforcements_c", "{!}kingdom_22_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_aiel_recruit_lithe,10,15),(trp_aiel_raider,5,10),(trp_knife_hand,3,6),(trp_night_spear,3,6)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)
  ("kingdom_22_reinforcements_d", "{!}kingdom_22_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_aiel_recruit_athletic,10,15),(trp_aiel_runner,5,10),(trp_dawn_runner,3,6),(trp_mountain_dancer,3,6)]),
  ("kingdom_22_reinforcements_e", "{!}kingdom_22_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_aiel_recruit_athletic,10,15),(trp_aiel_scout,5,10),(trp_maiden_of_the_spear,3,6),(trp_water_seeker,3,6)]),
  ("kingdom_22_reinforcements_f", "{!}kingdom_22_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_aiel_recruit_bulky,10,15),(trp_aiel_enforcer,5,10),(trp_stone_dog,3,6),(trp_red_shield,3,6)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)
  ("kingdom_22_reinforcements_g", "{!}kingdom_22_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_aiel_recruit_warrior,10,15),(trp_aiel_brute,5,10),(trp_brother_of_the_eagle,3,6),(trp_brotherless,3,6)]),
  ("kingdom_22_reinforcements_h", "{!}kingdom_22_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_aiel_recruit_warrior,10,15),(trp_aiel_grappler,5,10),(trp_black_eye,3,6),(trp_true_blood,3,6)]),  

  # seanchan
  ("kingdom_23_reinforcements_a", "{!}kingdom_23_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_suldam,3,5),(trp_der_suldam,2,4)]),
  ("kingdom_23_reinforcements_b", "{!}kingdom_23_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_seanchan_armsman,15,20),(trp_seanchan_swordsman,5,10),(trp_seanchan_deathwatch_guard,2,4),(trp_seanchan_marksman,4,8),(trp_seanchan_scout,4,8),(trp_seanchan_lancer,3,6)]),
  ("kingdom_23_reinforcements_c", "{!}kingdom_23_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_seanchan_footman,10,15),(trp_seanchan_blademaster,4,8),(trp_seanchan_pikeman,8,4),(trp_seanchan_halberdier,2,4),(trp_seanchan_bowman,5,10),(trp_seanchan_crossbowman,4,8)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)
  ("kingdom_23_reinforcements_d", "{!}kingdom_23_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_seanchan_scout,4,8),(trp_seanchan_man_at_arms,5,10),(trp_seanchan_lancer,3,6),(trp_seanchan_captain,2,4),(trp_seanchan_skirmisher,4,8)]),
  ("kingdom_23_reinforcements_e", "{!}kingdom_23_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_seanchan_armsman,10,15),(trp_seanchan_swordsman,4,8),(trp_seanchan_deathwatch_guard,2,4),(trp_seanchan_marksman,4,8),(trp_seanchan_scout,4,8),(trp_seanchan_lancer,2,4)]),
  ("kingdom_23_reinforcements_f", "{!}kingdom_23_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_seanchan_tarabon_ally,4,8),(trp_tarabon_bowman,4,8),(trp_tarabon_marksman,2,4),(trp_tarabon_scout,3,6),(trp_tarabon_lancer,3,6),(trp_tarabon_skirmisher,2,4)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)
  ("kingdom_23_reinforcements_g", "{!}kingdom_23_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_seanchan_amadicia_ally,4,8),(trp_amadicia_pikeman,4,8),(trp_amadicia_captain,2,4),(trp_whitecloak_man_at_arms,3,6),(trp_whitecloak_lancer,3,6)]),
  ("kingdom_23_reinforcements_h", "{!}kingdom_23_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_seanchan_altara_ally,4,8),(trp_altara_swordsman,4,8),(trp_altara_royal_guard,3,6),(trp_altara_knife_thrower,2,4)]),

  # shadowspawn  
  ("kingdom_24_reinforcements_a", "{!}kingdom_24_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_shadowspawn_recruit_creature,20,30),(trp_trolloc_grunt,10,20),(trp_trolloc_hewer,8,16),(trp_trolloc_berserker,4,12),(trp_trolloc_clan_chief,4,8),(trp_myrddraal,2,4)]),
  ("kingdom_24_reinforcements_b", "{!}kingdom_24_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_shadowspawn_recruit_creature,20,30),(trp_trolloc_grunt,10,20),(trp_trolloc_hewer,8,16),(trp_trolloc_berserker,4,12),(trp_trolloc_clan_chief,4,8),(trp_myrddraal,2,4)]),
  ("kingdom_24_reinforcements_c", "{!}kingdom_24_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_shadowspawn_recruit_creature,20,30),(trp_trolloc_grunt,10,20),(trp_trolloc_hewer,8,16),(trp_trolloc_berserker,4,12),(trp_trolloc_clan_chief,4,8),(trp_myrddraal,2,4)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)
  ("kingdom_24_reinforcements_d", "{!}kingdom_24_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_trolloc_archer,8,16),(trp_trolloc_stalker,8,16),(trp_draghkar,2,4)]),
  ("kingdom_24_reinforcements_e", "{!}kingdom_24_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_trolloc_archer,8,16),(trp_trolloc_stalker,8,16),(trp_draghkar,2,4)]),
  ("kingdom_24_reinforcements_f", "{!}kingdom_24_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_darkfriend_channeler,4,6),(trp_aes_sedai_black,6,8),(trp_dreadlord,4,6)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)
  ("kingdom_24_reinforcements_g", "{!}kingdom_24_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_darkfriend_initiate,15,25),(trp_darkfriend_murderer,6,10),(trp_darkfriend_assassin,4,8),(trp_darkfriend_ambusher,6,10),(trp_darkfriend_leader,4,8),(trp_darkfriend_marksman,8,14)]),
  ("kingdom_24_reinforcements_h", "{!}kingdom_24_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_darkfriend_initiate,15,25),(trp_darkfriend_murderer,6,10),(trp_darkfriend_assassin,4,8),(trp_darkfriend_ambusher,6,10),(trp_darkfriend_leader,4,8),(trp_darkfriend_marksman,8,14)]),

  # shara
  ("kingdom_25_reinforcements_a", "{!}kingdom_25_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_ayyad_villager,2,4),(trp_ayyad_village_leader,3,5),(trp_ayyad_counsel_member,2,3)]),
  ("kingdom_25_reinforcements_b", "{!}kingdom_25_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_ayyad_villager,2,4),(trp_ayyad_village_leader,3,5),(trp_ayyad_counsel_member,2,3)]),
  ("kingdom_25_reinforcements_c", "{!}kingdom_25_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_shara_recruit,5,10),(trp_shara_armsman,4,8),(trp_shara_town_guard,3,6),(trp_shara_border_guard,2,4),(trp_shara_defender,1,2)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)
  ("kingdom_25_reinforcements_d", "{!}kingdom_25_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_shara_swordsman,2,4),(trp_shara_captain,1,2),(trp_shara_bowman,3,6),(trp_shara_marksman,2,4),(trp_shara_crossbowman,2,4)]),
  ("kingdom_25_reinforcements_e", "{!}kingdom_25_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_shara_scout,4,8),(trp_shara_man_at_arms,3,6),(trp_shara_shbo_guardsman,2,4),(trp_shara_skirmisher,3,6)]),
  ("kingdom_25_reinforcements_f", "{!}kingdom_25_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_shara_recruit,5,10),(trp_shara_armsman,4,8),(trp_shara_town_guard,3,6),(trp_shara_border_guard,2,4),(trp_shara_defender,1,2)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)
  ("kingdom_25_reinforcements_g", "{!}kingdom_25_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_shara_swordsman,2,4),(trp_shara_captain,1,2),(trp_shara_bowman,3,6),(trp_shara_marksman,2,4),(trp_shara_crossbowman,2,4)]),
  ("kingdom_25_reinforcements_h", "{!}kingdom_25_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_shara_scout,4,8),(trp_shara_man_at_arms,3,6),(trp_shara_shbo_guardsman,2,4),(trp_shara_skirmisher,3,6)]),

  # sea folk
  ("kingdom_26_reinforcements_a", "{!}kingdom_26_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_sea_folk_recruit_channeler,2,4),(trp_sea_folk_pupil,3,5),(trp_sea_folk_windfinder,2,3)]),
  ("kingdom_26_reinforcements_b", "{!}kingdom_26_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_sea_folk_recruit_channeler,2,4),(trp_sea_folk_pupil,3,5),(trp_sea_folk_windfinder,2,3)]),
  ("kingdom_26_reinforcements_c", "{!}kingdom_26_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_sea_folk_recruit,5,10),(trp_sea_folk_bilge_hand,4,8),(trp_sea_folk_deck_hand,3,6),(trp_sea_folk_boatswain,2,4),(trp_sea_folk_cargomaster,1,2)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)
  ("kingdom_26_reinforcements_d", "{!}kingdom_26_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_sea_folk_dogwatcher,3,6),(trp_sea_folk_deck_defender,2,4),(trp_sea_folk_weatherly,4,8),(trp_sea_folk_quarterling,3,6),(trp_sea_folk_sailmistress,2,4),(trp_sea_folk_wavemistress,1,2)]),
  ("kingdom_26_reinforcements_e", "{!}kingdom_26_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_sea_folk_recruit,5,10),(trp_sea_folk_bilge_hand,4,8),(trp_sea_folk_deck_hand,3,6),(trp_sea_folk_boatswain,2,4),(trp_sea_folk_cargomaster,1,2)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)
  ("kingdom_26_reinforcements_f", "{!}kingdom_26_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_sea_folk_dogwatcher,3,6),(trp_sea_folk_deck_defender,2,4),(trp_sea_folk_weatherly,4,8),(trp_sea_folk_quarterling,3,6),(trp_sea_folk_sailmistress,2,4),(trp_sea_folk_wavemistress,1,2)]),
  ("kingdom_26_reinforcements_g", "{!}kingdom_26_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_sea_folk_recruit,5,10),(trp_sea_folk_bilge_hand,4,8),(trp_sea_folk_deck_hand,3,6),(trp_sea_folk_boatswain,2,4),(trp_sea_folk_cargomaster,1,2)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)
  ("kingdom_26_reinforcements_h", "{!}kingdom_26_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_sea_folk_dogwatcher,3,6),(trp_sea_folk_deck_defender,2,4),(trp_sea_folk_weatherly,4,8),(trp_sea_folk_quarterling,3,6),(trp_sea_folk_sailmistress,2,4),(trp_sea_folk_wavemistress,1,2)]),

  # madmen
  ("kingdom_27_reinforcements_a", "{!}kingdom_27_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_madmen_air_shifter,2,4),(trp_madmen_fire_tamer,3,5),(trp_madmen_storm_caller,2,3)]),
  ("kingdom_27_reinforcements_b", "{!}kingdom_27_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_madmen_air_shifter,2,4),(trp_madmen_fire_tamer,3,5),(trp_madmen_storm_caller,2,3)]),
  ("kingdom_27_reinforcements_c", "{!}kingdom_27_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_madmen_recruit,5,10),(trp_madmen_wanderer,4,8),(trp_madmen_villager,3,6),(trp_madmen_clansman,2,4),(trp_madmen_chieftan,1,2)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)
  ("kingdom_27_reinforcements_d", "{!}kingdom_27_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_madmen_looter,2,4),(trp_madmen_pillager,1,2),(trp_madmen_hunter,3,6),(trp_madmen_ambusher,2,4),(trp_madmen_assassin,1,2)]),
  ("kingdom_27_reinforcements_e", "{!}kingdom_27_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_madmen_horse_tamer,4,8),(trp_madmen_slave_catcher,3,6),(trp_madmen_thunderhoof,2,4),(trp_madmen_plains_rider,3,6)]),
  ("kingdom_27_reinforcements_f", "{!}kingdom_27_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_madmen_recruit,5,10),(trp_madmen_wanderer,4,8),(trp_madmen_villager,3,6),(trp_madmen_clansman,2,4),(trp_madmen_chieftan,1,2)]), #Swadians are a bit less-powered thats why they have a bit more troops in their modernised party template (3-6, others 3-5)
  ("kingdom_27_reinforcements_g", "{!}kingdom_27_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_madmen_looter,2,4),(trp_madmen_pillager,1,2),(trp_madmen_hunter,3,6),(trp_madmen_ambusher,2,4),(trp_madmen_assassin,1,2)]),
  ("kingdom_27_reinforcements_h", "{!}kingdom_27_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_madmen_horse_tamer,4,8),(trp_madmen_slave_catcher,3,6),(trp_madmen_thunderhoof,2,4),(trp_madmen_plains_rider,3,6)]),

  # toman head
  ("kingdom_28_reinforcements_a", "{!}kingdom_28_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_toman_head_recruit,5,10),(trp_toman_head_footman,4,8),(trp_toman_head_city_guard,3,6),(trp_toman_head_bowman,3,6),(trp_toman_head_scout,4,8)]),  
  ("kingdom_28_reinforcements_b", "{!}kingdom_28_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_toman_head_recruit,5,10),(trp_toman_head_footman,4,8),(trp_toman_head_city_guard,3,6),(trp_toman_head_bowman,3,6),(trp_toman_head_scout,4,8)]),
  ("kingdom_28_reinforcements_c", "{!}kingdom_28_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_toman_head_recruit,5,10),(trp_toman_head_footman,4,8),(trp_toman_head_city_guard,3,6),(trp_toman_head_bowman,3,6),(trp_toman_head_scout,4,8)]),
  ("kingdom_28_reinforcements_d", "{!}kingdom_28_reinforcements_d", 0, 0, fac_commoners, 0, [(trp_toman_head_recruit,5,10),(trp_toman_head_footman,4,8),(trp_toman_head_city_guard,3,6),(trp_toman_head_bowman,3,6),(trp_toman_head_scout,4,8)]),
  ("kingdom_28_reinforcements_e", "{!}kingdom_28_reinforcements_e", 0, 0, fac_commoners, 0, [(trp_toman_head_recruit,5,10),(trp_toman_head_footman,4,8),(trp_toman_head_city_guard,3,6),(trp_toman_head_bowman,3,6),(trp_toman_head_scout,4,8)]),
  ("kingdom_28_reinforcements_f", "{!}kingdom_28_reinforcements_f", 0, 0, fac_commoners, 0, [(trp_toman_head_recruit,5,10),(trp_toman_head_footman,4,8),(trp_toman_head_city_guard,3,6),(trp_toman_head_bowman,3,6),(trp_toman_head_scout,4,8)]),
  ("kingdom_28_reinforcements_g", "{!}kingdom_28_reinforcements_g", 0, 0, fac_commoners, 0, [(trp_toman_head_recruit,5,10),(trp_toman_head_footman,4,8),(trp_toman_head_city_guard,3,6),(trp_toman_head_bowman,3,6),(trp_toman_head_scout,4,8)]),
  ("kingdom_28_reinforcements_h", "{!}kingdom_28_reinforcements_h", 0, 0, fac_commoners, 0, [(trp_toman_head_recruit,5,10),(trp_toman_head_footman,4,8),(trp_toman_head_city_guard,3,6),(trp_toman_head_bowman,3,6),(trp_toman_head_scout,4,8)]),

  #end edited for TGS
  
##  ("kingdom_1_reinforcements_a", "kingdom_1_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_swadian_footman,3,7),(trp_swadian_skirmisher,5,10),(trp_swadian_militia,11,26)]),
##  ("kingdom_1_reinforcements_b", "kingdom_1_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_swadian_man_at_arms,5,10),(trp_swadian_infantry,5,10),(trp_swadian_crossbowman,3,8)]),
##  ("kingdom_1_reinforcements_c", "kingdom_1_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_swadian_knight,2,6),(trp_swadian_sergeant,2,5),(trp_swadian_sharpshooter,2,5)]),
##
##  ("kingdom_2_reinforcements_a", "kingdom_2_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_vaegir_veteran,3,7),(trp_vaegir_skirmisher,5,10),(trp_vaegir_footman,11,26)]),
##  ("kingdom_2_reinforcements_b", "kingdom_2_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_vaegir_horseman,4,9),(trp_vaegir_infantry,5,10),(trp_vaegir_archer,3,8)]),
##  ("kingdom_2_reinforcements_c", "kingdom_2_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_vaegir_knight,3,7),(trp_vaegir_guard,2,5),(trp_vaegir_marksman,2,5)]),
##
##  ("kingdom_3_reinforcements_a", "kingdom_3_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,3,7),(trp_khergit_skirmisher,5,10),(trp_khergit_tribesman,11,26)]),
##  ("kingdom_3_reinforcements_b", "kingdom_3_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_khergit_veteran_horse_archer,4,9),(trp_khergit_horse_archer,5,10),(trp_khergit_horseman,3,8)]),
##  ("kingdom_3_reinforcements_c", "kingdom_3_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_khergit_lancer,3,7),(trp_khergit_veteran_horse_archer,2,5),(trp_khergit_horse_archer,2,5)]),
##
##  ("kingdom_4_reinforcements_a", "kingdom_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nord_trained_footman,3,7),(trp_nord_footman,5,10),(trp_nord_recruit,11,26)]),
##  ("kingdom_4_reinforcements_b", "kingdom_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nord_veteran,4,9),(trp_nord_warrior,5,10),(trp_nord_footman,3,8)]),
##  ("kingdom_4_reinforcements_c", "kingdom_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nord_champion,1,3),(trp_nord_veteran,2,5),(trp_nord_warrior,2,5)]),
##
##  ("kingdom_5_reinforcements_a", "kingdom_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_spearman,3,7),(trp_rhodok_crossbowman,5,10),(trp_rhodok_tribesman,11,26)]),
##  ("kingdom_5_reinforcements_b", "kingdom_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_trained_spearman,4,9),(trp_rhodok_spearman,5,10),(trp_rhodok_crossbowman,3,8)]),
##  ("kingdom_5_reinforcements_c", "kingdom_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_sergeant,3,7),(trp_rhodok_veteran_spearman,2,5),(trp_rhodok_veteran_crossbowman,2,5)]),



  # edited for TGS
  ("steppe_bandit_lair" ,"Dragonsworn Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_arad_doman_rabble, 10, 30), (trp_tarabon_rabble, 10, 30), (trp_forest_bandit, 10, 20), (trp_tarabon_scout, 10, 20), (trp_mountain_bandit, 10, 20), (trp_caravan_guard, 15, 20)]),
  ("taiga_bandit_lair","Dragonsworn Bandit Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_arad_doman_rabble, 10, 30), (trp_tarabon_rabble, 10, 30), (trp_forest_bandit, 10, 20), (trp_tarabon_scout, 10, 20), (trp_mountain_bandit, 10, 20), (trp_caravan_guard, 15, 20)]),
  ("desert_bandit_lair" ,"Aiel Renegades Lair",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_aiel_raider,10,45), (trp_aiel_runner, 10,45), (trp_dawn_runner, 5, 10), (trp_maiden_of_the_spear, 5, 10)]),
  ("forest_bandit_lair" ,"Forest Raiders Camp",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_forest_bandit,15,58), (trp_murandy_bowman, 10, 20), (trp_illian_scout, 5, 15), (trp_shienar_spearman, 5, 10), (trp_ghealdan_militia, 10, 20)]),
  ("mountain_bandit_lair" ,"Bandit Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_mountain_bandit,15,58), (trp_saldaea_skirmisher, 10, 20), (trp_sedai_recruit_soldier, 10, 20), (trp_murandy_maceman, 10, 20), (trp_andor_bowman, 10, 20), (trp_cairhien_light_cavalry, 10, 20)]),
  ("sea_raider_lair","Coastal Raider Landing",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_illian_militia,10,50), (trp_tear_recruit,10,25),(trp_altara_dueler,10,25), (trp_altara_knife_thrower, 10, 20), (trp_tarabon_bowman, 10, 20), (trp_mayene_swordsman, 5, 20)]),
  # end edited for TGS
  ("looter_lair","Kidnappers' Hideout",icon_bandit_lair|carries_goods(2)|pf_is_static|pf_hide_defenders,0,fac_neutral,bandit_personality,[(trp_looter,15,25)]),
  
  ("bandit_lair_templates_end","{!}bandit_lair_templates_end",icon_axeman|carries_goods(2)|pf_is_static,0,fac_outlaws,bandit_personality,[(trp_sea_raider,15,50)]),

  ("leaded_looters","Band of robbers",icon_axeman|carries_goods(8)|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_looter_leader,1,1),(trp_looter,3,3)]),
  
   ##diplomacy begin
  ("dplmc_spouse","Your spouse",icon_woman|pf_civilian|pf_show_faction,0,fac_neutral,merchant_personality,[]),

  ("dplmc_gift_caravan","Your Caravan",icon_mule|carries_goods(25)|pf_show_faction,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_caravan_guard,5,25)]),
#recruiter kit begin
   ("dplmc_recruiter","Recruiter",icon_gray_knight|pf_show_faction,0,fac_neutral,merchant_personality,[(trp_dplmc_recruiter,1,1)]),
#recruiter kit end
   ##diplomacy end
]
