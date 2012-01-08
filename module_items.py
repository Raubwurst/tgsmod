from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *

####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################

# Some constants for ease of use.
imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
imodbits_cloth  = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_armor  = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_plate  = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_shield  = imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced
imodbits_sword   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered
imodbits_sword_high   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork
imodbits_axe   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_mace   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_pick   = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork
imodbits_crossbow = imodbit_cracked | imodbit_bent | imodbit_masterwork
imodbits_missile   = imodbit_bent | imodbit_large_bag
imodbits_thrown   = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent | imodbit_balanced| imodbit_large_bag

imodbits_horse_good = imodbit_spirited|imodbit_heavy
imodbits_good   = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad    = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent
# Replace winged mace/spiked mace with: Flanged mace / Knobbed mace?
# Fauchard (majowski glaive)
items = [
# item_name, mesh_name, item_properties, item_capabilities, slot_no, cost, bonus_flags, weapon_flags, scale, view_dir, pos_offset
 ["no_item","INVALID ITEM", [("invalid_item",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

 ["tutorial_spear", "Spear", [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 0 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
 ["tutorial_club", "Club", [("club",0)], itp_type_one_handed_wpn| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 0 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
 ["tutorial_battle_axe", "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(5)|difficulty(0)|spd_rtng(88) | weapon_length(108)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_arrows","Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(0,pierce)|max_ammo(20),imodbits_missile],
 ["tutorial_bolts","Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|abundance(90)|weapon_length(55)|thrust_damage(0,pierce)|max_ammo(18),imodbits_missile],
 ["tutorial_short_bow", "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 0 , weight(1)|difficulty(0)|spd_rtng(98) | shoot_speed(49) | thrust_damage(12 ,  pierce  ),imodbits_bow ],
 ["tutorial_crossbow", "Crossbow", [("crossbow",0)], itp_type_crossbow |itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0 , weight(3)|difficulty(0)|spd_rtng(42)|  shoot_speed(68) | thrust_damage(32,pierce)|max_ammo(1),imodbits_crossbow ],
 ["tutorial_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_missile ],
 ["tutorial_saddle_horse", "Saddle Horse", [("saddle_horse",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
 ["tutorial_shield", "Kite Shield", [("shield_kite_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield ],
 ["tutorial_staff_no_attack","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],
 ["tutorial_staff","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(16,blunt) | thrust_damage(16,blunt),imodbits_none],
 ["tutorial_sword", "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 0 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(18 , cut) | thrust_damage(15 ,  pierce),imodbits_sword ],
 ["tutorial_axe", "Axe", [("iron_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(4)|difficulty(0)|spd_rtng(91) | weapon_length(108)|swing_damage(19 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

 ["tutorial_dagger","Dagger", [("practice_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(40)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],


 ["horse_meat","Horse Meat", [("raw_meat",0)], itp_type_goods|itp_consumable|itp_food, 0, 12,weight(40)|food_quality(30)|max_ammo(40),imodbits_none],
# Items before this point are hardwired and their order should not be changed!
 ["practice_sword","Practice Sword", [("practice_sword",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_wooden_parry|itp_wooden_attack, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(22,blunt)|thrust_damage(20,blunt),imodbits_none],
 ["heavy_practice_sword","Heavy Practice Sword", [("heavy_practicesword",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_greatsword,
    21, weight(6.25)|spd_rtng(94)|weapon_length(128)|swing_damage(30,blunt)|thrust_damage(24,blunt),imodbits_none],
 ["practice_dagger","Practice Dagger", [("practice_dagger",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry|itp_wooden_attack, itc_dagger|itcf_carry_dagger_front_left, 2,weight(0.5)|spd_rtng(110)|weapon_length(47)|swing_damage(16,blunt)|thrust_damage(14,blunt),imodbits_none],
 ["practice_axe", "Practice Axe", [("hatchet",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, 24 , weight(2) | spd_rtng(95) | weapon_length(75) | swing_damage(24, blunt) | thrust_damage(0, pierce), imodbits_axe],
 ["arena_axe", "Axe", [("arena_axe",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 137 , weight(1.5)|spd_rtng(100) | weapon_length(69)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["arena_sword", "Sword", [("arena_sword_one_handed",0),("sword_medieval_b_scabbard", ixmesh_carry),], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 243 , weight(1.5)|spd_rtng(99) | weapon_length(95)|swing_damage(22 , blunt) | thrust_damage(20 ,  blunt),imodbits_sword_high ],
 ["arena_sword_two_handed",  "Two Handed Sword", [("arena_sword_two_handed",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
 670 , weight(2.75)|spd_rtng(93) | weapon_length(110)|swing_damage(30 , blunt) | thrust_damage(24 ,  blunt),imodbits_sword_high ],
 ["arena_lance",         "Lance", [("arena_lance",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,
 90 , weight(2.5)|spd_rtng(96) | weapon_length(150)|swing_damage(20 , blunt) | thrust_damage(25 ,  blunt),imodbits_polearm ],
 ["practice_staff","Practice Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(2.5)|spd_rtng(103) | weapon_length(118)|swing_damage(18,blunt) | thrust_damage(18,blunt),imodbits_none],
 ["practice_lance","Practice Lance", [("joust_of_peace",0)], itp_couchable|itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_greatlance, 18,weight(4.25)|spd_rtng(58)|weapon_length(240)|swing_damage(0,blunt)|thrust_damage(15,blunt),imodbits_none],
 ["practice_shield","Practice Shield", [("shield_round_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield, 20,weight(3.5)|body_armor(1)|hit_points(200)|spd_rtng(100)|shield_width(50),imodbits_none],
 ["practice_bow","Practice Bow", [("hunting_bow",0), ("hunting_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90) | shoot_speed(40) | thrust_damage(21, blunt),imodbits_bow ],
##                                                     ("hunting_bow",0)],                  itp_type_bow|itp_two_handed|itp_primary|itp_attach_left_hand, itcf_shoot_bow, 4,weight(1.5)|spd_rtng(90)|shoot_speed(40)|thrust_damage(19,blunt),imodbits_none],
 ["practice_crossbow", "Practice Crossbow", [("crossbow_a",0)], itp_type_crossbow |itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0, weight(3)|spd_rtng(42)| shoot_speed(68) | thrust_damage(32,blunt)|max_ammo(1),imodbits_crossbow],
 ["practice_javelin", "Practice Javelins", [("javelin",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_primary|itp_next_item_as_melee,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 0, weight(5) | spd_rtng(91) | shoot_speed(28) | thrust_damage(27, blunt) | max_ammo(50) | weapon_length(75), imodbits_thrown],
 ["practice_javelin_melee", "practice_javelin_melee", [("javelin",0)], itp_type_polearm|itp_primary|itp_penalty_with_shield|itp_wooden_parry , itc_staff, 0, weight(1)|difficulty(0)|spd_rtng(91) |swing_damage(12, blunt)| thrust_damage(14,  blunt)|weapon_length(75),imodbits_polearm ],
 ["practice_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16, blunt)|max_ammo(10)|weapon_length(0),imodbits_thrown ],
 ["practice_throwing_daggers_100_amount", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16, blunt)|max_ammo(100)|weapon_length(0),imodbits_thrown ],
# ["cheap_shirt","Cheap Shirt", [("shirt",0)], itp_type_body_armor|itp_covers_legs, 0, 4,weight(1.25)|body_armor(3),imodbits_none],
 ["practice_horse","Practice Horse", [("saddle_horse",0)], itp_type_horse, 0, 37,body_armor(10)|horse_speed(40)|horse_maneuver(37)|horse_charge(14),imodbits_none],
 ["practice_arrows","Practice Arrows", [("arena_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_missile],
## ["practice_arrows","Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo)], itp_type_arrows, 0, 31,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_none],
 ["practice_bolts","Practice Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|weapon_length(55)|max_ammo(49),imodbits_missile],
 ["practice_arrows_10_amount","Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(10),imodbits_missile],
 ["practice_arrows_100_amount","Practice Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(100),imodbits_missile],
 ["practice_bolts_9_amount","Practice Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|weapon_length(55)|max_ammo(9),imodbits_missile],
 ["practice_boots", "Practice Boots", [("boot_nomad_a",0)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 11 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10), imodbits_cloth ],
 ["red_tourney_armor","Red Tourney Armor", [("tourn_armor_a",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["blue_tourney_armor","Blue Tourney Armor", [("mail_shirt",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["green_tourney_armor","Green Tourney Armor", [("leather_vest",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["gold_tourney_armor","Gold Tourney Armor", [("padded_armor",0)], itp_type_body_armor|itp_covers_legs, 0, 152,weight(15.0)|body_armor(20)|leg_armor(6),imodbits_none],
 ["red_tourney_helmet","Red Tourney Helmet",[("flattop_helmet",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
 ["blue_tourney_helmet","Blue Tourney Helmet",[("segmented_helm",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
 ["green_tourney_helmet","Green Tourney Helmet",[("hood_c",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],
 ["gold_tourney_helmet","Gold Tourney Helmet",[("hood_a",0)],itp_type_head_armor,0,126, weight(2)|head_armor(16),imodbits_none],

["arena_shield_red", "Shield", [("arena_shield_red",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_shield_blue", "Shield", [("arena_shield_blue",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_shield_green", "Shield", [("arena_shield_green",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],
["arena_shield_yellow", "Shield", [("arena_shield_yellow",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|weapon_length(60),imodbits_shield ],

["arena_armor_white", "Arena Armor White", [("arena_armorW_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_red", "Arena Armor Red", [("arena_armorR_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_blue", "Arena Armor Blue", [("arena_armorB_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_green", "Arena Armor Green", [("arena_armorG_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_armor_yellow", "Arena Armor Yellow", [("arena_armorY_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(29)|leg_armor(13), imodbits_armor ],
["arena_tunic_white", "Arena Tunic White ", [("arena_tunicW_new",0)], itp_type_body_armor |itp_covers_legs ,0, 47 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
["arena_tunic_red", "Arena Tunic Red", [("arena_tunicR_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
["arena_tunic_blue", "Arena Tunic Blue", [("arena_tunicB_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
["arena_tunic_green", "Arena Tunic Green", [("arena_tunicG_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
["arena_tunic_yellow", "Arena Tunic Yellow", [("arena_tunicY_new",0)], itp_type_body_armor |itp_covers_legs ,0, 27 , weight(2)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(6), imodbits_cloth ],
#headwear
["arena_helmet_red", "Arena Helmet Red", [("arena_helmetR",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_blue", "Arena Helmet Blue", [("arena_helmetB",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_green", "Arena Helmet Green", [("arena_helmetG",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_helmet_yellow", "Arena Helmet Yellow", [("arena_helmetY",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_white", "Steppe Helmet White", [("steppe_helmetW",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_red", "Steppe Helmet Red", [("steppe_helmetR",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_blue", "Steppe Helmet Blue", [("steppe_helmetB",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_green", "Steppe Helmet Green", [("steppe_helmetG",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ],
["steppe_helmet_yellow", "Steppe Helmet Yellow", [("steppe_helmetY",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_white", "Tourney Helm White", [("tourney_helmR",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_red", "Tourney Helm Red", [("tourney_helmR",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_blue", "Tourney Helm Blue", [("tourney_helmB",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_green", "Tourney Helm Green", [("tourney_helmG",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["tourney_helm_yellow", "Tourney Helm Yellow", [("tourney_helmY",0)], itp_type_head_armor|itp_covers_head,0, 760 , weight(2.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_red", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_blue", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_green", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],
["arena_turban_yellow", "Arena Turban", [("tuareg_open",0)], itp_type_head_armor|itp_fit_to_head ,0, 187 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0), imodbits_plate ],

# A treatise on The Method of Mechanical Theorems Archimedes

#This book must be at the beginning of readable books
 ["book_tactics","De Re Militari", [("book_a",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],
 ["book_persuasion","Rhetorica ad Herennium", [("book_b",0)], itp_type_book, 0, 5000,weight(2)|abundance(100),imodbits_none],
 ["book_leadership","The Life of Alixenus the Great", [("book_d",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none],
 ["book_intelligence","Essays on Logic", [("book_e",0)], itp_type_book, 0, 2900,weight(2)|abundance(100),imodbits_none],
 ["book_trade","A Treatise on the Value of Things", [("book_f",0)], itp_type_book, 0, 3100,weight(2)|abundance(100),imodbits_none],
 ["book_weapon_mastery", "On the Art of Fighting with Swords", [("book_d",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none],
 ["book_engineering","Method of Mechanical Theorems", [("book_open",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none],

#Reference books
#This book must be at the beginning of reference books
 ["book_wound_treatment_reference","The Book of Healing", [("book_c",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
 ["book_training_reference","Manual of Arms", [("book_open",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
 ["book_surgery_reference","The Great Book of Surgery", [("book_c",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],

 #other trade goods (first one is spice)
 ["spice","Spice", [("spice_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 880,weight(40)|abundance(25)|max_ammo(50),imodbits_none],
 ["salt","Salt", [("salt_sack",0)], itp_merchandise|itp_type_goods, 0, 255,weight(50)|abundance(120),imodbits_none],


 #["flour","Flour", [("salt_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 40,weight(50)|abundance(100)|food_quality(45)|max_ammo(50),imodbits_none],

 ["oil","Oil", [("oil",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 450,weight(50)|abundance(60)|max_ammo(50),imodbits_none],

 ["pottery","Pottery", [("jug",0)], itp_merchandise|itp_type_goods, 0, 100,weight(50)|abundance(90),imodbits_none],

 ["raw_flax","Flax Bundle", [("raw_flax",0)], itp_merchandise|itp_type_goods, 0, 150,weight(40)|abundance(90),imodbits_none],
 ["linen","Linen", [("linen",0)], itp_merchandise|itp_type_goods, 0, 250,weight(40)|abundance(90),imodbits_none],

 ["wool","Wool", [("wool_sack",0)], itp_merchandise|itp_type_goods, 0, 130,weight(40)|abundance(90),imodbits_none],
 ["wool_cloth","Wool Cloth", [("wool_cloth",0)], itp_merchandise|itp_type_goods, 0, 250,weight(40)|abundance(90),imodbits_none],

 ["raw_silk","Raw Silk", [("raw_silk_bundle",0)], itp_merchandise|itp_type_goods, 0, 600,weight(30)|abundance(90),imodbits_none],
 ["raw_dyes","Dyes", [("dyes",0)], itp_merchandise|itp_type_goods, 0, 200,weight(10)|abundance(90),imodbits_none],
 ["velvet","Velvet", [("velvet",0)], itp_merchandise|itp_type_goods, 0, 1025,weight(40)|abundance(30),imodbits_none],

 ["iron","Iron", [("iron",0)], itp_merchandise|itp_type_goods, 0,264,weight(60)|abundance(60),imodbits_none],
 ["tools","Tools", [("iron_hammer",0)], itp_merchandise|itp_type_goods, 0, 410,weight(50)|abundance(90),imodbits_none],

 ["raw_leather","Hides", [("leatherwork_inventory",0)], itp_merchandise|itp_type_goods, 0, 120,weight(40)|abundance(90),imodbits_none],
 ["leatherwork","Leatherwork", [("leatherwork_frame",0)], itp_merchandise|itp_type_goods, 0, 220,weight(40)|abundance(90),imodbits_none],

 ["raw_date_fruit","Date Fruit", [("date_inventory",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 120,weight(40)|food_quality(10)|max_ammo(10),imodbits_none],
 ["furs","Furs", [("fur_pack",0)], itp_merchandise|itp_type_goods, 0, 391,weight(40)|abundance(90),imodbits_none],

 ["wine","Wine", [("amphora_slim",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 220,weight(30)|abundance(60)|max_ammo(50),imodbits_none],
 ["ale","Ale", [("ale_barrel",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 120,weight(30)|abundance(70)|max_ammo(50),imodbits_none],

# ["dry_bread", "wheat_sack", itp_type_goods|itp_consumable, 0, slt_none,view_goods,95,weight(2),max_ammo(50),imodbits_none],
#foods (first one is smoked_fish)
 ["smoked_fish","Smoked Fish", [("smoked_fish",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 65,weight(15)|abundance(110)|food_quality(50)|max_ammo(50),imodbits_none],
 ["cheese","Cheese", [("cheese_b",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 75,weight(6)|abundance(110)|food_quality(40)|max_ammo(30),imodbits_none],
 ["honey","Honey", [("honey_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 220,weight(5)|abundance(110)|food_quality(40)|max_ammo(30),imodbits_none],
 ["sausages","Sausages", [("sausages",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 85,weight(10)|abundance(110)|food_quality(40)|max_ammo(40),imodbits_none],
 ["cabbages","Cabbages", [("cabbage",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 30,weight(15)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
 ["dried_meat","Dried Meat", [("smoked_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 85,weight(15)|abundance(100)|food_quality(70)|max_ammo(50),imodbits_none],
 ["apples","Fruit", [("apple_basket",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 44,weight(20)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
 ["raw_grapes","Grapes", [("grapes_inventory",0)], itp_merchandise|itp_consumable|itp_type_goods, 0, 75,weight(40)|abundance(90)|food_quality(10)|max_ammo(10),imodbits_none], #x2 for wine
 ["raw_olives","Olives", [("olive_inventory",0)], itp_merchandise|itp_consumable|itp_type_goods, 0, 100,weight(40)|abundance(90)|food_quality(10)|max_ammo(10),imodbits_none], #x3 for oil
 ["grain","Grain", [("wheat_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 30,weight(30)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],

 ["cattle_meat","Beef", [("raw_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 80,weight(20)|abundance(100)|food_quality(80)|max_ammo(50),imodbits_none],
 ["bread","Bread", [("bread_a",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 50,weight(30)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
 ["chicken","Chicken", [("chicken",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 95,weight(10)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
 ["pork","Pork", [("pork",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 75,weight(15)|abundance(100)|food_quality(70)|max_ammo(50),imodbits_none],
 ["butter","Butter", [("butter_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 150,weight(6)|abundance(110)|food_quality(40)|max_ammo(30),imodbits_none],


 #Would like to remove flour altogether and reduce chicken, pork and butter (perishables) to non-trade items. Apples could perhaps become a generic "fruit", also representing dried fruit and grapes
 # Armagan: changed order so that it'll be easier to remove them from trade goods if necessary.
#************************************************************************************************
# ITEMS before this point are hardcoded into item_codes.h and their order should not be changed!
#************************************************************************************************

# Quest Items

 ["siege_supply","Supplies", [("ale_barrel",0)], itp_type_goods, 0, 96,weight(40)|abundance(70),imodbits_none],
 ["quest_wine","Wine", [("amphora_slim",0)], itp_type_goods, 0, 46,weight(40)|abundance(60)|max_ammo(50),imodbits_none],
 ["quest_ale","Ale", [("ale_barrel",0)], itp_type_goods, 0, 31,weight(40)|abundance(70)|max_ammo(50),imodbits_none],


# Tutorial Items

 ["tutorial_sword", "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 0 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(18 , cut) | thrust_damage(15 ,  pierce),imodbits_sword ],
 ["tutorial_axe", "Axe", [("iron_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(4)|difficulty(0)|spd_rtng(91) | weapon_length(108)|swing_damage(19 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_spear", "Spear", [("spear",0)], itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 0 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(0 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],
 ["tutorial_club", "Club", [("club",0)], itp_type_one_handed_wpn| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar, 0 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
 ["tutorial_battle_axe", "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 0 , weight(5)|difficulty(0)|spd_rtng(88) | weapon_length(108)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["tutorial_arrows","Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(0,pierce)|max_ammo(20),imodbits_missile],
 ["tutorial_bolts","Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 0,weight(2.25)|abundance(90)|weapon_length(63)|thrust_damage(0,pierce)|max_ammo(18),imodbits_missile],
 ["tutorial_short_bow", "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 0 , weight(1)|difficulty(0)|spd_rtng(98) | shoot_speed(49) | thrust_damage(12 ,  pierce  ),imodbits_bow ],
 ["tutorial_crossbow", "Crossbow", [("crossbow_a",0)], itp_type_crossbow |itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 0 , weight(3)|difficulty(0)|spd_rtng(42)|  shoot_speed(68) | thrust_damage(32,pierce)|max_ammo(1),imodbits_crossbow ],
 ["tutorial_throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(3.5)|difficulty(0)|spd_rtng(102) | shoot_speed(25) | thrust_damage(16 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_missile ],
 ["tutorial_saddle_horse", "Saddle Horse", [("saddle_horse",0)], itp_type_horse, 0, 0,abundance(90)|body_armor(3)|difficulty(0)|horse_speed(40)|horse_maneuver(38)|horse_charge(8),imodbits_horse_basic],
 ["tutorial_shield", "Kite Shield", [("shield_kite_a",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(150),imodbits_shield ],
 ["tutorial_staff_no_attack","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],
 ["tutorial_staff","Staff", [("wooden_staff",0)],itp_type_polearm|itp_offset_lance|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack,itc_staff|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(16,blunt) | thrust_damage(16,blunt),imodbits_none],

# Horses: sumpter horse/ pack horse, saddle horse, steppe horse, warm blood, geldling, stallion,   war mount, charger,
# Carthorse, hunter, heavy hunter, hackney, palfrey, courser, destrier.
 ["sumpter_horse","Sumpter Horse", [("sumpter_horse",0)], itp_merchandise|itp_type_horse, 0, 134,abundance(90)|hit_points(100)|body_armor(14)|difficulty(1)|horse_speed(37)|horse_maneuver(39)|horse_charge(9)|horse_scale(100),imodbits_horse_basic],
 ["saddle_horse","Saddle Horse", [("saddle_horse",0),("horse_c",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0, 240,abundance(90)|hit_points(100)|body_armor(8)|difficulty(1)|horse_speed(45)|horse_maneuver(44)|horse_charge(10)|horse_scale(104),imodbits_horse_basic],
 ["steppe_horse","Steppe Horse", [("steppe_horse",0)], itp_merchandise|itp_type_horse, 0, 192,abundance(80)|hit_points(120)|body_armor(10)|difficulty(2)|horse_speed(40)|horse_maneuver(51)|horse_charge(8)|horse_scale(98),imodbits_horse_basic, [], [fac_kingdom_2, fac_kingdom_3]],
 ["arabian_horse_a","Desert Horse", [("arabian_horse_a",0)], itp_merchandise|itp_type_horse, 0, 550,abundance(80)|hit_points(110)|body_armor(10)|difficulty(2)|horse_speed(42)|horse_maneuver(50)|horse_charge(12)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_3, fac_kingdom_6]],
 ["courser","Courser", [("courser",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(70)|body_armor(12)|hit_points(110)|difficulty(2)|horse_speed(50)|horse_maneuver(44)|horse_charge(12)|horse_scale(106),imodbits_horse_basic|imodbit_champion],
 ["arabian_horse_b","Sarranid Horse", [("arabian_horse_b",0)], itp_merchandise|itp_type_horse, 0, 700,abundance(80)|hit_points(120)|body_armor(10)|difficulty(3)|horse_speed(43)|horse_maneuver(54)|horse_charge(16)|horse_scale(100),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_6]],
 ["hunter","Hunter", [("hunting_horse",0),("hunting_horse",imodbits_horse_good)], itp_merchandise|itp_type_horse, 0, 810,abundance(60)|hit_points(160)|body_armor(18)|difficulty(3)|horse_speed(43)|horse_maneuver(44)|horse_charge(24)|horse_scale(108),imodbits_horse_basic|imodbit_champion],
 ["warhorse","War Horse", [("warhorse_chain",0)], itp_merchandise|itp_type_horse, 0, 1224,abundance(50)|hit_points(165)|body_armor(40)|difficulty(4)|horse_speed(40)|horse_maneuver(41)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion],
 ["charger","Charger", [("charger_new",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(165)|body_armor(58)|difficulty(4)|horse_speed(40)|horse_maneuver(44)|horse_charge(32)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_1, fac_kingdom_5]],



#whalebone crossbow, yew bow, war bow, arming sword
 ["arrows","Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise|itp_default_ammo, itcf_carry_quiver_back, 72,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(1,pierce)|max_ammo(30),imodbits_missile],
 ["khergit_arrows","Khergit Arrows", [("arrow_b",0),("flying_missile",ixmesh_flying_ammo),("quiver_b", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 410,weight(3.5)|abundance(30)|weapon_length(95)|thrust_damage(3,pierce)|max_ammo(30),imodbits_missile],
 ["barbed_arrows","Barbed Arrows", [("barbed_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver_d", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 124,weight(3)|abundance(70)|weapon_length(95)|thrust_damage(2,pierce)|max_ammo(30),imodbits_missile],
 ["bodkin_arrows","Bodkin Arrows", [("piercing_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver_c", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 350,weight(3)|abundance(50)|weapon_length(91)|thrust_damage(3,pierce)|max_ammo(28),imodbits_missile],
 ["bolts","Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts|itp_merchandise|itp_default_ammo|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 64,weight(2.25)|abundance(90)|weapon_length(63)|thrust_damage(1,pierce)|max_ammo(29),imodbits_missile],
 ["steel_bolts","Steel Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag_c", ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield, itcf_carry_quiver_right_vertical, 210,weight(2.5)|abundance(20)|weapon_length(63)|thrust_damage(2,pierce)|max_ammo(29),imodbits_missile],
 ["cartridges","Cartridges", [("cartridge_a",0)], itp_type_bullets|itp_merchandise|itp_can_penetrate_shield|itp_default_ammo, 0, 41,weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(1,pierce)|max_ammo(50),imodbits_missile],

["pilgrim_disguise", "Pilgrim Disguise", [("pilgrim_outfit",0)], 0| itp_type_body_armor |itp_covers_legs |itp_civilian ,0, 25 , weight(2)|abundance(100)|head_armor(0)|body_armor(19)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["pilgrim_hood", "Pilgrim Hood", [("pilgrim_hood",0)], 0| itp_type_head_armor |itp_civilian  ,0, 35 , weight(1.25)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

# ARMOR
#handwear
["leather_gloves","Leather Gloves", [("leather_gloves_L",0)], itp_merchandise|itp_type_hand_armor,0, 90, weight(0.25)|abundance(120)|body_armor(2)|difficulty(0),imodbits_cloth],
["mail_mittens","Mail Mittens", [("mail_mittens_L",0)], itp_merchandise|itp_type_hand_armor,0, 350, weight(0.5)|abundance(100)|body_armor(4)|difficulty(0),imodbits_armor],
["scale_gauntlets","Scale Gauntlets", [("scale_gauntlets_b_L",0)], itp_merchandise|itp_type_hand_armor,0, 710, weight(0.75)|abundance(100)|body_armor(5)|difficulty(0),imodbits_armor],
["lamellar_gauntlets","Lamellar Gauntlets", [("scale_gauntlets_a_L",0)], itp_merchandise|itp_type_hand_armor,0, 910, weight(0.75)|abundance(100)|body_armor(5)|difficulty(0),imodbits_armor],
["gauntlets","Gauntlets", [("gauntlets_L",0),("gauntlets_L",imodbit_reinforced)], itp_merchandise|itp_type_hand_armor,0, 1040, weight(1.0)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor],

#footwear
["wrapping_boots", "Wrapping Boots", [("wrapping_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 3 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(3)|difficulty(0) ,imodbits_cloth ],
["woolen_hose", "Woolen Hose", [("woolen_hose_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
["blue_hose", "Blue Hose", [("blue_hose_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 11 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
["hunter_boots", "Hunter Boots", [("hunter_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature,0,
 19 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
["hide_boots", "Hide Boots", [("hide_boots_a",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 34 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["ankle_boots", "Ankle Boots", [("ankle_boots_a_new",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 75 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["nomad_boots", "Nomad Boots", [("nomad_boots_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 90 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["leather_boots", "Leather Boots", [("leather_boots_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 174 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["splinted_leather_greaves", "Splinted Leather Greaves", [("leather_greaves_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 310 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(21)|difficulty(0) ,imodbits_armor ],
## TGS: mat: Edited
["mail_chausses", "Mail Chausses", [("mail_chausses_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  |itp_civilian,0,
 530 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(24)|difficulty(0) ,imodbits_armor ],
["splinted_greaves", "Splinted Greaves", [("splinted_greaves_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 853 , weight(2.75)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(28)|difficulty(7) ,imodbits_armor ],
## TGS: mat: End
["mail_boots", "Mail Boots", [("mail_boots_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature  ,0,
 1250 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(31)|difficulty(8) ,imodbits_armor ],
["iron_greaves", "Iron Greaves", [("iron_greaves_a",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_armor ],
["black_greaves", "Black Greaves", [("black_greaves",0)], itp_type_foot_armor  | itp_attach_armature,0,
 2361 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(35)|difficulty(0) ,imodbits_armor ],
["khergit_leather_boots", "Khergit Leather Boots", [("khergit_leather_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 120 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_cloth ],
["sarranid_boots_a", "Sarranid Shoes", [("sarranid_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["sarranid_boots_b", "Sarranid Leather Boots", [("sarranid_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 120 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["sarranid_boots_c", "Plated Boots", [("sarranid_camel_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 280 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_plate ],
["sarranid_boots_d", "Sarranid Mail Boots", [("sarranid_mail_chausses",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 920 , weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_armor ],

["sarranid_head_cloth", "Lady Head Cloth", [("tulbent",0)],  itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["sarranid_head_cloth_b", "Lady Head Cloth", [("tulbent_b",0)],  itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["sarranid_felt_head_cloth", "Head Cloth", [("common_tulbent",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["sarranid_felt_head_cloth_b", "Head Cloth", [("common_tulbent_b",0)],  itp_type_head_armor  |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],


#bodywear
["lady_dress_ruby", "Lady Dress", [("lady_dress_r",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["lady_dress_green", "Lady Dress", [("lady_dress_g",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["lady_dress_blue", "Lady Dress", [("lady_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["red_dress", "Red Dress", [("red_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["brown_dress", "Brown Dress", [("brown_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["green_dress", "Green Dress", [("green_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["khergit_lady_dress", "Khergit Lady Dress", [("khergit_lady_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["khergit_lady_dress_b", "Khergit Leather Lady Dress", [("khergit_lady_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["sarranid_lady_dress", "Sarranid Lady Dress", [("sarranid_lady_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["sarranid_lady_dress_b", "Sarranid Lady Dress", [("sarranid_lady_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["sarranid_common_dress", "Sarranid Dress", [("sarranid_common_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["sarranid_common_dress_b", "Sarranid Dress", [("sarranid_common_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["courtly_outfit", "Courtly Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["nobleman_outfit", "Nobleman Outfit", [("nobleman_outfit_b_new",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["nomad_armor", "Nomad Armor", [("nomad_armor_new",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs   ,0, 25 , weight(2)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["khergit_armor", "Khergit Armor", [("khergit_armor_new",0)], itp_merchandise| itp_type_body_armor | itp_covers_legs ,0, 38 , weight(2)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["leather_jacket", "Leather Jacket", [("leather_jacket_new",0)], itp_merchandise| itp_type_body_armor | itp_covers_legs  |itp_civilian ,0, 50 , weight(3)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

#NEW:
["rawhide_coat", "Rawhide Coat", [("coat_of_plates_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 12 , weight(5)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
#NEW: was lthr_armor_a
["leather_armor", "Leather Armor", [("tattered_leather_armor_a",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs  ,0, 65 , weight(7)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["fur_coat", "Fur Coat", [("fur_coat",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0, 117 , weight(6)|abundance(100)|head_armor(0)|body_armor(13)|leg_armor(6)|difficulty(0) ,imodbits_armor ],



#for future:
["coat", "Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["leather_coat", "Leather Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["mail_coat", "Coat of Mail", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["long_mail_coat", "Long Coat of Mail", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["mail_with_tunic_red", "Mail with Tunic", [("arena_armorR_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(8), imodbits_armor ],
["mail_with_tunic_green", "Mail with Tunic", [("arena_armorG_new",0)], itp_type_body_armor  |itp_covers_legs ,0, 650 , weight(16)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(8), imodbits_armor ],
["hide_coat", "Hide Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["merchant_outfit", "Merchant Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["homespun_dress", "Homespun Dress", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["thick_coat", "Thick Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["coat_with_cape", "Coat with Cape", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["steppe_outfit", "Steppe Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["nordic_outfit", "Nordic Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["nordic_armor", "Nordic Armor", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["hide_armor", "Hide Armor", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["cloaked_tunic", "Cloaked Tunic", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["sleeveless_tunic", "Sleeveless Tunic", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["sleeveless_leather_tunic", "Sleeveless Leather Tunic", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["linen_shirt", "Linen Shirt", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["wool_coat", "Wool Coat", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
#end

["dress", "Dress", [("dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["blue_dress", "Blue Dress", [("blue_dress_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["peasant_dress", "Peasant Dress", [("peasant_dress_b_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["woolen_dress", "Woolen Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor|itp_civilian  |itp_covers_legs ,0,
 10 , weight(1.75)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["shirt", "Shirt", [("shirt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 3 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
 #NEW: was "linen_tunic"
["linen_tunic", "Linen Tunic", [("shirt_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
 #NEW was cvl_costume_a
["short_tunic", "Red Tunic", [("rich_tunic_a",0)], itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
#TODO:
 ["red_shirt", "Red Shirt", [("rich_tunic_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
 ["red_tunic", "Red Tunic", [("arena_tunicR_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],

 ["green_tunic", "Green Tunic", [("arena_tunicG_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
 ["blue_tunic", "Blue Tunic", [("arena_tunicB_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["robe", "Robe", [("robe",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 31 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#NEW: was coarse_tunic
["coarse_tunic", "Tunic with vest", [("coarse_tunic_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 47 , weight(2)|abundance(100)|head_armor(0)|body_armor(11)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["leather_apron", "Leather Apron", [("leather_apron",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 61 , weight(3)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
#NEW: was tabard_a
["tabard", "Tabard", [("tabard_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 107 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#NEW: was leather_vest
["leather_vest", "Leather Vest", [("leather_vest_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 146 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["steppe_armor", "Steppe Armor", [("lamellar_leather",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 195 , weight(5)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["gambeson", "Gambeson", [("white_gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 260 , weight(5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
["blue_gambeson", "Blue Gambeson", [("blue_gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 270 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
#NEW: was red_gambeson
["red_gambeson", "Red Gambeson", [("red_gambeson_a",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 275 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
#NEW: was aketon_a
["padded_cloth", "Aketon", [("padded_cloth_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 297 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#NEW:
 ["aketon_green", "Padded Cloth", [("padded_cloth_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 297 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 #NEW: was "leather_jerkin"
["leather_jerkin", "Leather Jerkin", [("ragged_leather_jerkin",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 321 , weight(6)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["nomad_vest", "Nomad Vest", [("nomad_vest_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 360 , weight(7)|abundance(50)|head_armor(0)|body_armor(22)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["ragged_outfit", "Ragged Outfit", [("ragged_outfit_a_new",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 390 , weight(7)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
 #NEW: was padded_leather
["padded_leather", "Padded Leather", [("leather_armor_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian,0,
 454 , weight(12)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["tribal_warrior_outfit", "Tribal Warrior Outfit", [("tribal_warrior_outfit_a_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 520 , weight(14)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["nomad_robe", "Nomad Robe", [("nomad_robe_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0,
 610 , weight(15)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
#["heraldric_armor", "Heraldric Armor", [("tourn_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 442 , weight(17)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#NEW: was "std_lthr_coat"
["studded_leather_coat", "Studded Leather Coat", [("leather_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 690 , weight(14)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(10)|difficulty(7) ,imodbits_armor ],

["byrnie", "Byrnie", [("byrnie_a_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 795 , weight(17)|abundance(100)|head_armor(0)|body_armor(39)|leg_armor(6)|difficulty(7) ,imodbits_armor ],
#["blackwhite_surcoat", "Black and White Surcoat", [("surcoat_blackwhite",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 348 , weight(16)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#["green_surcoat", "Green Surcoat", [("surcoat_green",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 348 , weight(16)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#["blue_surcoat", "Blue Surcoat", [("surcoat_blue",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 350 , weight(16)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#["red_surcoat", "Red Surcoat", [("surcoat_red",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0, 350 , weight(16)|abundance(100)|head_armor(0)|body_armor(33)|leg_armor(8)|difficulty(7) ,imodbits_armor ],
#NEW: was "haubergeon_a"
["haubergeon", "Haubergeon", [("haubergeon_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 863 , weight(18)|abundance(100)|head_armor(0)|body_armor(41)|leg_armor(6)|difficulty(6) ,imodbits_armor ],

["lamellar_vest", "Lamellar Vest", [("lamellar_vest_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 970 , weight(18)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_cloth ],

["lamellar_vest_khergit", "Khergit Lamellar Vest", [("lamellar_vest_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 970 , weight(18)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(8)|difficulty(7) ,imodbits_cloth ],

 #NEW: was mail_shirt
["mail_shirt", "Mail Shirt", [("mail_shirt_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1040 , weight(19)|abundance(100)|head_armor(0)|body_armor(37)|leg_armor(12)|difficulty(7) ,imodbits_armor ],

["mail_hauberk", "Mail Hauberk", [("hauberk_a_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1320 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(7) ,imodbits_armor ],

["mail_with_surcoat", "Mail with Surcoat", [("mail_long_surcoat_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1544 , weight(22)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
["surcoat_over_mail", "Surcoat over Mail", [("surcoat_over_mail_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1720 , weight(22)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
#["lamellar_cuirass", "Lamellar Cuirass", [("lamellar_armor",0)], itp_type_body_armor  |itp_covers_legs,0, 1020 , weight(25)|abundance(100)|head_armor(0)|body_armor(43)|leg_armor(15)|difficulty(9) ,imodbits_armor ],
#NEW: was "brigandine_a"
["brigandine_red", "Brigandine", [("brigandine_b",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs,0,
 1830 , weight(19)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(12)|difficulty(0) ,imodbits_armor ],
["lamellar_armor", "Lamellar Armor", [("lamellar_armor_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2410 , weight(25)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(13)|difficulty(0) ,imodbits_armor ],
["scale_armor", "Scale Armor", [("lamellar_armor_e",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2558 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(13)|difficulty(8) ,imodbits_armor ],
 #NEW: was "reinf_jerkin"
["banded_armor", "Banded Armor", [("banded_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 2710 , weight(23)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(14)|difficulty(8) ,imodbits_armor ],
#NEW: was hard_lthr_a
["cuir_bouilli", "Cuir Bouilli", [("cuir_bouilli_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3100 , weight(24)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(15)|difficulty(8) ,imodbits_armor ],
## TGS: mat: Edited
["coat_of_plates", "Coat of Plates", [("coat_of_plates_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
## TGS: mat: End
["coat_of_plates_red", "Coat of Plates", [("coat_of_plates_red",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["plate_armor", "Plate Armor", [("full_plate_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 6553 , weight(27)|abundance(100)|head_armor(0)|body_armor(55)|leg_armor(17)|difficulty(9) ,imodbits_plate ],
["black_armor", "Black Armor", [("black_armor",0)], itp_type_body_armor  |itp_covers_legs ,0,
 9496 , weight(28)|abundance(100)|head_armor(0)|body_armor(57)|leg_armor(18)|difficulty(10) ,imodbits_plate ],

##armors_d
## TGS: mat: Edited
["pelt_coat", "Pelt Coat", [("thick_coat_a",0)],  itp_merchandise|itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 14, weight(2)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
## TGS: mat: End
##armors_e
["khergit_elite_armor", "Khergit Elite Armor", [("lamellar_armor_d",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
## TGS: mat: Edited
["vaegir_elite_armor", "Vaegir Elite Armor", [("lamellar_armor_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
## TGS: mat: End
["sarranid_elite_armor", "Sarranid Elite Armor", [("tunic_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian ,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],


 ["sarranid_dress_a", "Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 33 , weight(1)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
 ["sarranid_dress_b", "Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 33 , weight(1)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
 ["sarranid_cloth_robe", "Worn Robe", [("sar_robe",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 33 , weight(1)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
 ["sarranid_cloth_robe_b", "Worn Robe", [("sar_robe_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 33 , weight(1)|abundance(100)|head_armor(0)|body_armor(9)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
["skirmisher_armor", "Skirmisher Armor", [("skirmisher_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 74 , weight(3)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
["archers_vest", "Archer's Padded Vest", [("archers_vest",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 260 , weight(6)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["sarranid_leather_armor", "Sarranid Leather Armor", [("sarranid_leather_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 650 , weight(9)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_armor ],
["sarranid_cavalry_robe", "Cavalry Robe", [("arabian_armor_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 990 , weight(15)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(8)|difficulty(0) ,imodbits_armor ],
["arabian_armor_b", "Sarranid Guard Armor", [("arabian_armor_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1200 , weight(19)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(8)|difficulty(0) ,imodbits_armor],
 ["sarranid_mail_shirt", "Sarranid Mail Shirt", [("sarranian_mail_shirt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 1400 , weight(19)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
["mamluke_mail", "Mamluke Mail", [("sarranid_elite_cavalary",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0,
2900 , weight(24)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(8) ,imodbits_armor ],

#Quest-specific - perhaps can be used for prisoners,
["burlap_tunic", "Burlap Tunic", [("shirt",0)], itp_type_body_armor  |itp_covers_legs ,0,
 5 , weight(1)|abundance(100)|head_armor(0)|body_armor(3)|leg_armor(1)|difficulty(0) ,imodbits_armor ],


["heraldic_mail_with_surcoat", "Heraldic Mail with Surcoat", [("heraldic_armor_new_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3454 , weight(22)|abundance(100)|head_armor(0)|body_armor(49)|leg_armor(17)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":agent_no", ":troop_no")])]],
["heraldic_mail_with_tunic", "Heraldic Mail", [("heraldic_armor_new_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3520 , weight(22)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(16)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_b", ":agent_no", ":troop_no")])]],
["heraldic_mail_with_tunic_b", "Heraldic Mail", [("heraldic_armor_new_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3610 , weight(22)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(16)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_c", ":agent_no", ":troop_no")])]],
["heraldic_mail_with_tabard", "Heraldic Mail with Tabard", [("heraldic_armor_new_d",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 3654 , weight(21)|abundance(100)|head_armor(0)|body_armor(51)|leg_armor(15)|difficulty(7) ,imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_d", ":agent_no", ":troop_no")])]],
["turret_hat_ruby", "Turret Hat", [("turret_hat_r",0)], itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 70 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["turret_hat_blue", "Turret Hat", [("turret_hat_b",0)], itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 80 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["turret_hat_green", "Barbette", [("barbette_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,70, weight(0.5)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["head_wrappings","Head Wrapping",[("head_wrapping",0)],itp_type_head_armor|itp_fit_to_head,0,16, weight(0.25)|head_armor(3),imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick],
["court_hat", "Turret Hat", [("court_hat",0)], itp_type_head_armor  |itp_civilian|itp_fit_to_head ,0, 80 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["wimple_a", "Wimple", [("wimple_a_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,10, weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["wimple_with_veil", "Wimple with Veil", [("wimple_b_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian|itp_fit_to_head,0,10, weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["straw_hat", "Straw Hat", [("straw_hat_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["common_hood", "Hood", [("hood_new",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["hood_b", "Hood", [("hood_b",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["hood_c", "Hood", [("hood_c",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["hood_d", "Hood", [("hood_d",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["headcloth", "Headcloth", [("headcloth_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_hood", "Woolen Hood", [("woolen_hood",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["arming_cap", "Arming Cap", [("arming_cap_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 5 , weight(1)|abundance(100)|head_armor(7)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["fur_hat", "Fur Hat", [("fur_hat_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["nomad_cap", "Nomad Cap", [("nomad_cap_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["nomad_cap_b", "Nomad Cap", [("nomad_cap_b_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(13)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["steppe_cap", "Steppe Cap", [("steppe_cap_a_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 14 , weight(1)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["padded_coif", "Padded Coif", [("padded_coif_a_new",0)], itp_merchandise| itp_type_head_armor   ,0, 6 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_cap", "Woolen Cap", [("woolen_cap_new",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["felt_hat", "Felt Hat", [("felt_hat_a_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["felt_hat_b", "Felt Hat", [("felt_hat_b_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["leather_cap", "Leather Cap", [("leather_cap_a_new",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 8, weight(1)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["female_hood", "Lady's Hood", [("ladys_hood_new",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 9 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["leather_steppe_cap_a", "Steppe Cap", [("leather_steppe_cap_a_new",0)], itp_merchandise|itp_type_head_armor   ,0,
24 , weight(1)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["leather_steppe_cap_b", "Steppe Cap ", [("tattered_steppe_cap_b_new",0)], itp_merchandise|itp_type_head_armor   ,0,
36 , weight(1)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["leather_steppe_cap_c", "Steppe Cap", [("steppe_cap_a_new",0)], itp_merchandise|itp_type_head_armor   ,0, 51 , weight(1)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["leather_warrior_cap", "Leather Warrior Cap", [("skull_cap_new_b",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 14 , weight(1)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["skullcap", "Skullcap", [("skull_cap_new_a",0)], itp_merchandise| itp_type_head_armor   ,0, 60 , weight(1.0)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],
["mail_coif", "Mail Coif", [("mail_coif_new",0)], itp_merchandise| itp_type_head_armor   ,0, 71 , weight(1.25)|abundance(100)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_armor ],
["footman_helmet", "Footman's Helmet", [("skull_cap_new",0)], itp_merchandise| itp_type_head_armor   ,0, 95 , weight(1.5)|abundance(100)|head_armor(24)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],
#missing...
["nasal_helmet", "Nasal Helmet", [("nasal_helmet_b",0)], itp_merchandise| itp_type_head_armor   ,0, 121 , weight(1.25)|abundance(100)|head_armor(26)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["norman_helmet", "Helmet with Cap", [("norman_helmet_a",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0, 147 , weight(1.25)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["segmented_helmet", "Segmented Helmet", [("segmented_helm_new",0)], itp_merchandise| itp_type_head_armor   ,0, 174 , weight(1.25)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["helmet_with_neckguard", "Helmet with Neckguard", [("neckguard_helm_new",0)], itp_merchandise| itp_type_head_armor   ,0,
190 , weight(1.5)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["flat_topped_helmet", "Flat Topped Helmet", [("flattop_helmet_new",0)], itp_merchandise| itp_type_head_armor   ,0,
203 , weight(1.75)|abundance(100)|head_armor(33)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["kettle_hat", "Kettle Hat", [("kettle_hat_new",0)], itp_merchandise| itp_type_head_armor,0,
240 , weight(1.75)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["spiked_helmet", "Spiked Helmet", [("spiked_helmet_new",0)], itp_merchandise| itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["nordic_helmet", "Nordic Helmet", [("helmet_w_eyeguard_new",0)], itp_merchandise| itp_type_head_armor   ,0, 340 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["khergit_lady_hat", "Khergit Lady Hat", [("khergit_lady_hat",0)],  itp_type_head_armor   |itp_civilian |itp_doesnt_cover_hair | itp_fit_to_head,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["khergit_lady_hat_b", "Khergit Lady Leather Hat", [("khergit_lady_hat_b",0)], itp_type_head_armor  | itp_doesnt_cover_hair | itp_fit_to_head  |itp_civilian ,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["sarranid_felt_hat", "Sarranid Felt Hat", [("sar_helmet3",0)], itp_merchandise| itp_type_head_armor   ,0, 16 , weight(2)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth ],
["turban", "Turban", [("tuareg_open",0)], itp_merchandise| itp_type_head_armor   ,0, 28 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth ],
["desert_turban", "Desert Turban", [("tuareg",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard ,0, 38 , weight(1.50)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_cloth ],
["sarranid_warrior_cap", "Sarranid Warrior Cap", [("tuareg_helmet",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard  ,0, 90 , weight(2)|abundance(100)|head_armor(19)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["sarranid_horseman_helmet", "Horseman Helmet", [("sar_helmet2",0)], itp_merchandise| itp_type_head_armor   ,0, 180 , weight(2.75)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["sarranid_helmet1", "Sarranid Keffiyeh Helmet", [("sar_helmet1",0)], itp_merchandise| itp_type_head_armor   ,0, 290 , weight(2.50)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["sarranid_mail_coif", "Sarranid Mail Coif", [("tuareg_helmet2",0)], itp_merchandise| itp_type_head_armor ,0, 430 , weight(3)|abundance(100)|head_armor(41)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["sarranid_veiled_helmet", "Sarranid Veiled Helmet", [("sar_helmet4",0)], itp_merchandise| itp_type_head_armor | itp_covers_beard  ,0, 810 , weight(3.50)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["nordic_archer_helmet", "Nordic Leather Helmet", [("Helmet_A_vs2",0)], itp_merchandise| itp_type_head_armor    ,0, 40 , weight(1.25)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["nordic_veteran_archer_helmet", "Nordic Leather Helmet", [("Helmet_A",0)], itp_merchandise| itp_type_head_armor,0, 70 , weight(1.5)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["nordic_footman_helmet", "Nordic Footman Helmet", [("Helmet_B_vs2",0)], itp_merchandise| itp_type_head_armor |itp_fit_to_head ,0, 150 , weight(1.75)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["nordic_fighter_helmet", "Nordic Fighter Helmet", [("Helmet_B",0)], itp_merchandise| itp_type_head_armor|itp_fit_to_head ,0, 240 , weight(2)|abundance(100)|head_armor(34)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["nordic_huscarl_helmet", "Nordic Huscarl's Helmet", [("Helmet_C_vs2",0)], itp_merchandise| itp_type_head_armor   ,0, 390 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["nordic_warlord_helmet", "Nordic Warlord Helmet", [("Helmet_C",0)], itp_merchandise| itp_type_head_armor ,0, 880 , weight(2.25)|abundance(100)|head_armor(48)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

["vaegir_fur_cap", "Cap with Fur", [("vaeg_helmet3",0)], itp_merchandise| itp_type_head_armor   ,0, 50 , weight(1)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["vaegir_fur_helmet", "Vaegir Helmet", [("vaeg_helmet2",0)], itp_merchandise| itp_type_head_armor   ,0, 110 , weight(2)|abundance(100)|head_armor(21)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["vaegir_spiked_helmet", "Spiked Cap", [("vaeg_helmet1",0)], itp_merchandise| itp_type_head_armor   ,0, 230 , weight(2.50)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["vaegir_lamellar_helmet", "Helmet with Lamellar Guard", [("vaeg_helmet4",0)], itp_merchandise| itp_type_head_armor   ,0, 360 , weight(2.75)|abundance(100)|head_armor(38)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["vaegir_noble_helmet", "Vaegir Nobleman Helmet", [("vaeg_helmet7",0)], itp_merchandise| itp_type_head_armor   ,0, 710, weight(2.75)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["vaegir_war_helmet", "Vaegir War Helmet", [("vaeg_helmet6",0)], itp_merchandise| itp_type_head_armor   ,0, 820 , weight(3)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["vaegir_mask", "Vaegir War Mask", [("vaeg_helmet9",0)], itp_merchandise| itp_type_head_armor |itp_covers_beard ,0, 950 , weight(3.50)|abundance(100)|head_armor(52)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

#TODO:
#["skullcap_b", "Skullcap_b", [("skull_cap_new_b",0)], itp_merchandise| itp_type_head_armor   ,0, 71 , weight(1.5)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_plate ],

["bascinet", "Bascinet", [("bascinet_avt_new",0)], itp_merchandise|itp_type_head_armor   ,0, 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["bascinet_2", "Bascinet with Aventail", [("bascinet_new_a",0)], itp_merchandise|itp_type_head_armor   ,0, 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["bascinet_3", "Bascinet with Nose Guard", [("bascinet_new_b",0)], itp_merchandise|itp_type_head_armor   ,0, 479 , weight(2.25)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],
["guard_helmet", "Guard Helmet", [("reinf_helmet_new",0)], itp_merchandise| itp_type_head_armor   ,0, 555 , weight(2.5)|abundance(100)|head_armor(47)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["black_helmet", "Black Helmet", [("black_helm",0)], itp_type_head_armor,0, 638 , weight(2.75)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],
["full_helm", "Full Helm", [("great_helmet_new_b",0)], itp_merchandise| itp_type_head_armor |itp_covers_head ,0, 811 , weight(2.5)|abundance(100)|head_armor(51)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["great_helmet", "Great Helmet", [("great_helmet_new",0)], itp_merchandise| itp_type_head_armor|itp_covers_head,0, 980 , weight(2.75)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],
["winged_great_helmet", "Winged Great Helmet", [("maciejowski_helmet_new",0)], itp_merchandise|itp_type_head_armor|itp_covers_head,0, 1240 , weight(2.75)|abundance(100)|head_armor(55)|body_armor(0)|leg_armor(0)|difficulty(10) ,imodbits_plate ],


#WEAPONS
["wooden_stick",         "Wooden Stick", [("wooden_stick",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
4 , weight(2.5)|difficulty(0)|spd_rtng(99) | weapon_length(63)|swing_damage(13 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["cudgel",         "Cudgel", [("club",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
4 , weight(2.5)|difficulty(0)|spd_rtng(99) | weapon_length(70)|swing_damage(13 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["hammer",         "Hammer", [("iron_hammer_new",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar,
7 , weight(2)|difficulty(0)|spd_rtng(100) | weapon_length(55)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["club",         "Club", [("club",0)], itp_type_one_handed_wpn|itp_merchandise| itp_can_knock_down|itp_primary|itp_wooden_parry|itp_wooden_attack, itc_scimitar,
11 , weight(2.5)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(20 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
["winged_mace",         "Flanged Mace", [("flanged_mace",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
122 , weight(3.5)|difficulty(0)|spd_rtng(103) | weapon_length(70)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["spiked_mace",         "Spiked Mace", [("spiked_mace_new",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
180 , weight(3.5)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(28 , blunt) | thrust_damage(0 ,  pierce),imodbits_pick ],
["military_hammer", "Military Hammer", [("military_hammer",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
317 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(70)|swing_damage(31 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["maul",         "Maul", [("maul_b",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down |itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,
97 , weight(6)|difficulty(11)|spd_rtng(83) | weapon_length(79)|swing_damage(36 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["sledgehammer", "Sledgehammer", [("maul_c",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,
101 , weight(7)|difficulty(12)|spd_rtng(81) | weapon_length(82)|swing_damage(39, blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["warhammer",         "Great Hammer", [("maul_d",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear,
290 , weight(9)|difficulty(14)|spd_rtng(79) | weapon_length(75)|swing_damage(45 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["pickaxe",         "Pickaxe", [("fighting_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
27 , weight(3)|difficulty(0)|spd_rtng(99) | weapon_length(70)|swing_damage(19 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["spiked_club",         "Spiked Club", [("spiked_club",0)], itp_type_one_handed_wpn|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
83 , weight(3)|difficulty(0)|spd_rtng(97) | weapon_length(70)|swing_damage(21 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["fighting_pick", "Fighting Pick", [("fighting_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
108 , weight(1.0)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(22 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["military_pick", "Military Pick", [("steel_pick_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
280 , weight(1.5)|difficulty(0)|spd_rtng(97) | weapon_length(70)|swing_damage(31 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],
["morningstar",         "Morningstar", [("mace_morningstar_new",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_primary|itp_wooden_parry|itp_unbalanced, itc_morningstar|itcf_carry_mace_left_hip,
305 , weight(4.5)|difficulty(13)|spd_rtng(95) | weapon_length(85)|swing_damage(38 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],


["sickle",         "Sickle", [("sickle",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver,
9 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(40)|swing_damage(20 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["cleaver",         "Cleaver", [("cleaver_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver,
14 , weight(1.5)|difficulty(0)|spd_rtng(103) | weapon_length(35)|swing_damage(24 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["knife",         "Knife", [("peasant_knife_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left,
18 , weight(0.5)|difficulty(0)|spd_rtng(110) | weapon_length(40)|swing_damage(21 , cut) | thrust_damage(13 ,  pierce),imodbits_sword ],
["butchering_knife", "Butchering Knife", [("khyber_knife_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right,
23 , weight(0.75)|difficulty(0)|spd_rtng(108) | weapon_length(60)|swing_damage(24 , cut) | thrust_damage(17 ,  pierce),imodbits_sword ],
["dagger",         "Dagger", [("dagger_b",0),("dagger_b_scabbard",ixmesh_carry),("dagger_b",imodbits_good),("dagger_b_scabbard",ixmesh_carry|imodbits_good)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn,
37 , weight(0.75)|difficulty(0)|spd_rtng(109) | weapon_length(47)|swing_damage(22 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
#["nordic_sword", "Nordic Sword", [("viking_sword",0),("scab_vikingsw", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 142 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(98)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],
#["arming_sword", "Arming Sword", [("b_long_sword",0),("scab_longsw_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 156 , weight(1.5)|difficulty(0)|spd_rtng(101) | weapon_length(100)|swing_damage(25 , cut) | thrust_damage(22 ,  pierce),imodbits_sword ],
#["sword",         "Sword", [("long_sword",0),("scab_longsw_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 148 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(102)|swing_damage(26 , cut) | thrust_damage(23 ,  pierce),imodbits_sword ],
["falchion",         "Falchion", [("falchion_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
105 , weight(2.5)|difficulty(8)|spd_rtng(96) | weapon_length(73)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
#["broadsword",         "Broadsword", [("broadsword",0),("scab_broadsword", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 122 , weight(2.5)|difficulty(8)|spd_rtng(91) | weapon_length(101)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
#["scimitar",         "Scimitar", [("scimeter",0),("scab_scimeter", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
#108 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(29 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["scimitar",         "Scimitar", [("scimitar_a",0),("scab_scimeter_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
210 , weight(1.5)|difficulty(0)|spd_rtng(101) | weapon_length(97)|swing_damage(30 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
["scimitar_b",         "Elite Scimitar", [("scimitar_b",0),("scab_scimeter_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
290 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(103)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["arabian_sword_a",         "Sarranid Sword", [("arabian_sword_a",0),("scab_arabian_sword_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
108 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(97)|swing_damage(26 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
["arabian_sword_b",         "Sarranid Arming Sword", [("arabian_sword_b",0),("scab_arabian_sword_b", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
218 , weight(1.7)|difficulty(0)|spd_rtng(99) | weapon_length(97)|swing_damage(28 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
["sarranid_cavalry_sword",         "Sarranid Cavalry Sword", [("arabian_sword_c",0),("scab_arabian_sword_c", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
310 , weight(1.5)|difficulty(0)|spd_rtng(98) | weapon_length(105)|swing_damage(28 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
["arabian_sword_d",         "Sarranid Guard Sword", [("arabian_sword_d",0),("scab_arabian_sword_d", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
420 , weight(1.7)|difficulty(0)|spd_rtng(99) | weapon_length(97)|swing_damage(30 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],


#["nomad_sabre",         "Nomad Sabre", [("shashqa",0),("scab_shashqa", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 115 , weight(1.75)|difficulty(0)|spd_rtng(101) | weapon_length(100)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_sword ],
#["bastard_sword", "Bastard Sword", [("bastard_sword",0),("scab_bastardsw", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 279 , weight(2.25)|difficulty(9)|spd_rtng(102) | weapon_length(120)|swing_damage(33 , cut) | thrust_damage(27 ,  pierce),imodbits_sword ],
["great_sword",         "Great Sword", [("b_bastard_sword",0),("scab_bastardsw_b", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn,
 423 , weight(2.75)|difficulty(10)|spd_rtng(95) | weapon_length(125)|swing_damage(39 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_high ],
["sword_of_war", "Sword of War", [("b_bastard_sword",0),("scab_bastardsw_b", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn,
 524 , weight(3)|difficulty(11)|spd_rtng(94) | weapon_length(130)|swing_damage(40 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_high ],
["hatchet",         "Hatchet", [("hatchet",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
13 , weight(2)|difficulty(0)|spd_rtng(97) | weapon_length(60)|swing_damage(23 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["hand_axe",         "Hand Axe", [("hatchet",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
24 , weight(2)|difficulty(7)|spd_rtng(95) | weapon_length(75)|swing_damage(27 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["fighting_axe", "Fighting Axe", [("fighting_ax",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
77 , weight(2.5)|difficulty(9)|spd_rtng(92) | weapon_length(90)|swing_damage(31 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["axe",                 "Axe", [("iron_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
65 , weight(4)|difficulty(8)|spd_rtng(91) | weapon_length(108)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["voulge",         "Voulge", [("voulge",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
129 , weight(4.5)|difficulty(8)|spd_rtng(87) | weapon_length(119)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["battle_axe",         "Battle Axe", [("battle_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
240 , weight(5)|difficulty(9)|spd_rtng(88) | weapon_length(108)|swing_damage(41 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["war_axe",         "War Axe", [("war_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back,
264 , weight(5)|difficulty(10)|spd_rtng(86) | weapon_length(110)|swing_damage(43 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
#["double_axe",         "Double Axe", [("dblhead_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 359 , weight(6.5)|difficulty(12)|spd_rtng(85) | weapon_length(95)|swing_damage(43 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
#["great_axe",         "Great Axe", [("great_ax",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_nodachi|itcf_carry_axe_back, 415 , weight(7)|difficulty(13)|spd_rtng(82) | weapon_length(120)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["sword_two_handed_b",         "Two Handed Sword", [("sword_two_handed_b",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
 670 , weight(2.75)|difficulty(10)|spd_rtng(97) | weapon_length(110)|swing_damage(40 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high ],
["sword_two_handed_a",         "Great Sword", [("sword_two_handed_a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
 1123 , weight(2.75)|difficulty(10)|spd_rtng(96) | weapon_length(120)|swing_damage(42 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high ],


["khergit_sword_two_handed_a",         "Two Handed Sabre", [("khergit_sword_two_handed_a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
 523 , weight(2.75)|difficulty(10)|spd_rtng(96) | weapon_length(120)|swing_damage(40 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
["khergit_sword_two_handed_b",         "Two Handed Sabre", [("khergit_sword_two_handed_b",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
 920 , weight(2.75)|difficulty(10)|spd_rtng(96) | weapon_length(120)|swing_damage(44 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["two_handed_cleaver", "War Cleaver", [("military_cleaver_a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
 640 , weight(2.75)|difficulty(10)|spd_rtng(93) | weapon_length(120)|swing_damage(45 , cut) | thrust_damage(0 ,  cut),imodbits_sword_high ],
["military_cleaver_b", "Soldier's Cleaver", [("military_cleaver_b",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
 193 , weight(1.5)|difficulty(0)|spd_rtng(96) | weapon_length(95)|swing_damage(31 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
["military_cleaver_c", "Military Cleaver", [("military_cleaver_c",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip,
 263 , weight(1.5)|difficulty(0)|spd_rtng(96) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["military_sickle_a", "Military Sickle", [("military_sickle_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 220 , weight(1.0)|difficulty(9)|spd_rtng(100) | weapon_length(75)|swing_damage(26 , pierce) | thrust_damage(0 ,  pierce),imodbits_axe ],


["bastard_sword_a", "Bastard Sword", [("bastard_sword_a",0),("bastard_sword_a_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 294 , weight(2.0)|difficulty(9)|spd_rtng(98) | weapon_length(101)|swing_damage(35 , cut) | thrust_damage(26 ,  pierce),imodbits_sword_high ],
["bastard_sword_b", "Heavy Bastard Sword", [("bastard_sword_b",0),("bastard_sword_b_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 526 , weight(2.25)|difficulty(9)|spd_rtng(97) | weapon_length(105)|swing_damage(37 , cut) | thrust_damage(27 ,  pierce),imodbits_sword_high ],

["one_handed_war_axe_a", "One Handed Axe", [("one_handed_war_axe_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 87 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(71)|swing_damage(32 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_battle_axe_a", "One Handed Battle Axe", [("one_handed_battle_axe_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 142 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(73)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_war_axe_b", "One Handed War Axe", [("one_handed_war_axe_b",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 190 , weight(1.5)|difficulty(9)|spd_rtng(98) | weapon_length(76)|swing_damage(34 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_battle_axe_b", "One Handed Battle Axe", [("one_handed_battle_axe_b",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 230 , weight(1.75)|difficulty(9)|spd_rtng(98) | weapon_length(72)|swing_damage(36 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["one_handed_battle_axe_c", "One Handed Battle Axe", [("one_handed_battle_axe_c",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 550 , weight(2.0)|difficulty(9)|spd_rtng(98) | weapon_length(76)|swing_damage(37 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],


["two_handed_axe",         "Two Handed Axe", [("two_handed_battle_axe_a",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 90 , weight(4.5)|difficulty(10)|spd_rtng(96) | weapon_length(90)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["two_handed_battle_axe_2",         "Two Handed War Axe", [("two_handed_battle_axe_b",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 152 , weight(4.5)|difficulty(10)|spd_rtng(96) | weapon_length(92)|swing_damage(44 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["shortened_voulge",         "Shortened Voulge", [("two_handed_battle_axe_c",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 228 , weight(4.5)|difficulty(10)|spd_rtng(92) | weapon_length(100)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["great_axe",         "Great Axe", [("two_handed_battle_axe_e",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 316 , weight(4.5)|difficulty(10)|spd_rtng(94) | weapon_length(96)|swing_damage(47 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["long_axe",         "Long Axe", [("long_axe_a",0)], itp_type_polearm|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_next_item_as_melee|itp_unbalanced|itp_merchandise,itc_staff|itcf_carry_axe_back,
 390 , weight(4.75)|difficulty(10)|spd_rtng(93) | weapon_length(120)|swing_damage(46 , cut) | thrust_damage(19 ,  blunt),imodbits_axe ],
["long_axe_alt",         "Long Axe", [("long_axe_a",0)],itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 390 , weight(4.75)|difficulty(10)|spd_rtng(88) | weapon_length(120)|swing_damage(46 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["long_axe_b",         "Long War Axe", [("long_axe_b",0)], itp_type_polearm| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_next_item_as_melee|itp_unbalanced|itp_merchandise, itc_staff|itcf_carry_axe_back,
 510 , weight(5.0)|difficulty(10)|spd_rtng(92) | weapon_length(125)|swing_damage(50 , cut) | thrust_damage(18 ,  blunt),imodbits_axe ],
["long_axe_b_alt",         "Long War Axe", [("long_axe_b",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 510 , weight(5.0)|difficulty(10)|spd_rtng(87) | weapon_length(125)|swing_damage(50 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
 ["long_axe_c",         "Great Long Axe", [("long_axe_c",0)], itp_type_polearm| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_next_item_as_melee|itp_unbalanced|itp_merchandise, itc_staff|itcf_carry_axe_back,
 660 , weight(5.5)|difficulty(10)|spd_rtng(91) | weapon_length(127)|swing_damage(54 , cut) | thrust_damage(19 ,  blunt),imodbits_axe ],
["long_axe_c_alt",      "Great Long Axe", [("long_axe_c",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 660 , weight(5.5)|difficulty(10)|spd_rtng(85) | weapon_length(127)|swing_damage(54 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

 ["bardiche",         "Bardiche", [("two_handed_battle_axe_d",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 291 , weight(4.75)|difficulty(10)|spd_rtng(91) | weapon_length(102)|swing_damage(47 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["great_bardiche",         "Great Bardiche", [("two_handed_battle_axe_f",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 617 , weight(5.0)|difficulty(10)|spd_rtng(89) | weapon_length(116)|swing_damage(50 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],




["voulge",         "Voulge", [("two_handed_battle_long_axe_a",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_staff,
 120 , weight(3.0)|difficulty(10)|spd_rtng(88) | weapon_length(175)|swing_damage(40 , cut) | thrust_damage(18 ,  pierce),imodbits_axe ],
["long_bardiche",         "Long Bardiche", [("two_handed_battle_long_axe_b",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_staff,
390 , weight(4.75)|difficulty(11)|spd_rtng(89) | weapon_length(140)|swing_damage(48 , cut) | thrust_damage(17 ,  pierce),imodbits_axe ],
["great_long_bardiche",         "Great Long Bardiche", [("two_handed_battle_long_axe_c",0)], itp_type_polearm|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry, itc_staff,
 660 , weight(5.0)|difficulty(12)|spd_rtng(88) | weapon_length(155)|swing_damage(50 , cut) | thrust_damage(17 ,  pierce),imodbits_axe ],

 ["hafted_blade_b",         "Hafted Blade", [("khergit_pike_b",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao,
 185 , weight(2.75)|difficulty(0)|spd_rtng(95) | weapon_length(135)|swing_damage(37 , cut) | thrust_damage(20 ,  pierce),imodbits_polearm ],
 ["hafted_blade_a",         "Hafted Blade", [("khergit_pike_a",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_spear|itc_guandao,
 350 , weight(3.25)|difficulty(0)|spd_rtng(93) | weapon_length(153)|swing_damage(39 , cut) | thrust_damage(19 ,  pierce),imodbits_polearm ],

["shortened_military_scythe",         "Shortened Military Scythe", [("two_handed_battle_scythe_a",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back,
 264 , weight(3.0)|difficulty(10)|spd_rtng(90) | weapon_length(112)|swing_damage(45 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],

["sword_medieval_a", "Sword", [("sword_medieval_a",0),("sword_medieval_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 163 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(27 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],
#["sword_medieval_a_long", "Sword", [("sword_medieval_a_long",0),("sword_medieval_a_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 156 , weight(1.5)|difficulty(0)|spd_rtng(97) | weapon_length(105)|swing_damage(25 , cut) | thrust_damage(22 ,  pierce),imodbits_sword ],
["sword_medieval_b", "Sword", [("sword_medieval_b",0),("sword_medieval_b_scabbard", ixmesh_carry),("sword_rusty_a",imodbit_rusty),("sword_rusty_a_scabbard", ixmesh_carry|imodbit_rusty)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 243 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(28 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high ],
["sword_medieval_b_small", "Short Sword", [("sword_medieval_b_small",0),("sword_medieval_b_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 152 , weight(1)|difficulty(0)|spd_rtng(102) | weapon_length(85)|swing_damage(26, cut) | thrust_damage(24, pierce),imodbits_sword_high ],
["sword_medieval_c", "Arming Sword", [("sword_medieval_c",0),("sword_medieval_c_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 410 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(29 , cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ],
["sword_medieval_c_small", "Short Arming Sword", [("sword_medieval_c_small",0),("sword_medieval_c_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 243 , weight(1)|difficulty(0)|spd_rtng(103) | weapon_length(86)|swing_damage(26, cut) | thrust_damage(24 ,  pierce),imodbits_sword_high ],
["sword_medieval_c_long", "Arming Sword", [("sword_medieval_c_long",0),("sword_medieval_c_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 480 , weight(1.7)|difficulty(0)|spd_rtng(99) | weapon_length(100)|swing_damage(29 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high ],
["sword_medieval_d_long", "Long Arming Sword", [("sword_medieval_d_long",0),("sword_medieval_d_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 550 , weight(1.8)|difficulty(0)|spd_rtng(96) | weapon_length(105)|swing_damage(33 , cut) | thrust_damage(28 ,  pierce),imodbits_sword ],

#["sword_medieval_d", "sword_medieval_d", [("sword_medieval_d",0),("sword_medieval_d_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
# 131 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(24 , cut) | thrust_damage(21 ,  pierce),imodbits_sword ],
#["sword_medieval_e", "sword_medieval_e", [("sword_medieval_e",0),("sword_medieval_e_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
# 131 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(24 , cut) | thrust_damage(21 ,  pierce),imodbits_sword ],

["sword_viking_1", "Nordic Sword", [("sword_viking_c",0),("sword_viking_c_scabbard ", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 147 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(94)|swing_damage(28 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ] ,
["sword_viking_2", "Nordic Sword", [("sword_viking_b",0),("sword_viking_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 276 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(29 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
["sword_viking_2_small", "Nordic Short Sword", [("sword_viking_b_small",0),("sword_viking_b_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 162 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(85)|swing_damage(28 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
["sword_viking_3", "Nordic War Sword", [("sword_viking_a",0),("sword_viking_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 394 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(30 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
#["sword_viking_a_long", "sword_viking_a_long", [("sword_viking_a_long",0),("sword_viking_a_long_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
# 142 , weight(1.5)|difficulty(0)|spd_rtng(97) | weapon_length(105)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],
["sword_viking_3_small", "Nordic Short War Sword", [("sword_viking_a_small",0),("sword_viking_a_small_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 280 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(86)|swing_damage(29 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],
#["sword_viking_c_long", "sword_viking_c_long", [("sword_viking_c_long",0),("sword_viking_c_long_scabbard ", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
# 142 , weight(1.5)|difficulty(0)|spd_rtng(95) | weapon_length(105)|swing_damage(27 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ] ,

["sword_khergit_1", "Nomad Sabre", [("khergit_sword_b",0),("khergit_sword_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 105 , weight(1.25)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(29 , cut),imodbits_sword_high ],
["sword_khergit_2", "Sabre", [("khergit_sword_c",0),("khergit_sword_c_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 191 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(97)|swing_damage(30 , cut),imodbits_sword_high ],
["sword_khergit_3", "Sabre", [("khergit_sword_a",0),("khergit_sword_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 294 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(98)|swing_damage(31 , cut),imodbits_sword_high ],
["sword_khergit_4", "Heavy Sabre", [("khergit_sword_d",0),("khergit_sword_d_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 384 , weight(1.75)|difficulty(0)|spd_rtng(98) | weapon_length(96)|swing_damage(33 , cut),imodbits_sword_high ],



["mace_1",         "Spiked Club", [("mace_d",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 45 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(70)|swing_damage(19 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],
["mace_2",         "Knobbed_Mace", [("mace_a",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 98 , weight(2.5)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(21 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["mace_3",         "Spiked Mace", [("mace_c",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 152 , weight(2.75)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(23 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["mace_4",         "Winged_Mace", [("mace_b",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 212 , weight(2.75)|difficulty(0)|spd_rtng(98) | weapon_length(70)|swing_damage(24 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
# Goedendag
 ["club_with_spike_head",  "Spiked Staff", [("mace_e",0)],  itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_wooden_parry, itc_bastardsword|itcf_carry_axe_back,
 200 , weight(2.80)|difficulty(9)|spd_rtng(95) | weapon_length(117)|swing_damage(24 , blunt) | thrust_damage(20 ,  pierce),imodbits_mace ],

["long_spiked_club",         "Long Spiked Club", [("mace_long_c",0)], itp_type_polearm|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_axe_back,
 264 , weight(3)|difficulty(0)|spd_rtng(96) | weapon_length(126)|swing_damage(23 , pierce) | thrust_damage(20 ,  blunt),imodbits_mace ],
["long_hafted_knobbed_mace",         "Long Hafted Knobbed Mace", [("mace_long_a",0)], itp_type_polearm| itp_can_knock_down|itp_primary|itp_wooden_parry, itc_staff|itcf_carry_axe_back,
 324 , weight(3)|difficulty(0)|spd_rtng(95) | weapon_length(133)|swing_damage(26 , blunt) | thrust_damage(23 ,  blunt),imodbits_mace ],
["long_hafted_spiked_mace",         "Long Hafted Spiked Mace", [("mace_long_b",0)], itp_type_polearm|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_axe_back,
 310 , weight(3)|difficulty(0)|spd_rtng(94) | weapon_length(140)|swing_damage(28 , blunt) | thrust_damage(26 ,  blunt),imodbits_mace ],

["sarranid_two_handed_mace_1",         "Iron Mace", [("mace_long_d",0)], itp_type_two_handed_wpn|itp_can_knock_down|itp_two_handed|itp_merchandise| itp_primary|itp_crush_through|itp_unbalanced, itc_greatsword|itcf_carry_axe_back,
470 , weight(4.5)|difficulty(0)|spd_rtng(90) | weapon_length(95)|swing_damage(35 , blunt) | thrust_damage(22 ,  blunt),imodbits_mace ],


["sarranid_mace_1",         "Iron Mace", [("mace_small_d",0)], itp_type_one_handed_wpn|itp_merchandise|itp_can_knock_down |itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip,
 45 , weight(2.0)|difficulty(0)|spd_rtng(99) | weapon_length(73)|swing_damage(22 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
["sarranid_axe_a", "Iron Battle Axe", [("one_handed_battle_axe_g",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 250 , weight(1.65)|difficulty(9)|spd_rtng(97) | weapon_length(71)|swing_damage(35 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["sarranid_axe_b", "Iron War Axe", [("one_handed_battle_axe_h",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip,
 360 , weight(1.75)|difficulty(9)|spd_rtng(97) | weapon_length(71)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

["sarranid_two_handed_axe_a",         "Sarranid Battle Axe", [("two_handed_battle_axe_g",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 350 , weight(3.0)|difficulty(10)|spd_rtng(89) | weapon_length(95)|swing_damage(49 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["sarranid_two_handed_axe_b",         "Sarranid War Axe", [("two_handed_battle_axe_h",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 280 , weight(2.50)|difficulty(10)|spd_rtng(90) | weapon_length(90)|swing_damage(46 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],




["scythe",         "Scythe", [("scythe",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear, 43 , weight(2)|difficulty(0)|spd_rtng(97) | weapon_length(182)|swing_damage(30 , cut) | thrust_damage(14 ,  pierce),imodbits_polearm ],
["pitch_fork",         "Pitch Fork", [("pitch_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry,itc_staff, 19 , weight(1.5)|difficulty(0)|spd_rtng(87) | weapon_length(154)|swing_damage(16 , blunt) | thrust_damage(22 ,  pierce),imodbits_polearm ],
["military_fork", "Military Fork", [("military_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry,itc_staff, 153 , weight(2)|difficulty(0)|spd_rtng(95) | weapon_length(135)|swing_damage(15 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],
["battle_fork",         "Battle Fork", [("battle_fork",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry,itc_staff, 282 , weight(2.2)|difficulty(0)|spd_rtng(90) | weapon_length(144)|swing_damage(15, blunt) | thrust_damage(35 ,  pierce),imodbits_polearm ],
["boar_spear",         "Boar Spear", [("spear",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry,itc_staff|itcf_carry_spear,
76 , weight(1.5)|difficulty(0)|spd_rtng(90) | weapon_length(157)|swing_damage(26 , cut) | thrust_damage(23 ,  pierce),imodbits_polearm ],
#["spear",         "Spear", [("spear",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear, 173 , weight(4.5)|difficulty(0)|spd_rtng(80) | weapon_length(158)|swing_damage(17 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],


["jousting_lance", "Jousting Lance", [("joust_of_peace",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance, 158 , weight(5)|difficulty(0)|spd_rtng(61) | weapon_length(240)|swing_damage(0 , cut) | thrust_damage(17 ,  blunt),imodbits_polearm ],
#["lance",         "Lance", [("pike",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_spear, 196 , weight(5)|difficulty(0)|spd_rtng(72) | weapon_length(170)|swing_damage(0 , cut) | thrust_damage(20 ,  pierce),imodbits_polearm ],
["double_sided_lance", "Double Sided Lance", [("lance_dblhead",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff, 261 , weight(4.0)|difficulty(0)|spd_rtng(95) | weapon_length(128)|swing_damage(25, cut) | thrust_damage(27 ,  pierce),imodbits_polearm ],
#["pike",         "Pike", [("pike",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_spear,
# 212 , weight(6)|difficulty(0)|spd_rtng(77) | weapon_length(167)|swing_damage(0 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],
["glaive",         "Glaive", [("glaive_b",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear,
 352 , weight(4.5)|difficulty(0)|spd_rtng(90) | weapon_length(157)|swing_damage(39 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm ],
["poleaxe",         "Poleaxe", [("pole_ax",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff,
 384 , weight(4.5)|difficulty(13)|spd_rtng(77) | weapon_length(180)|swing_damage(50 , cut) | thrust_damage(15 ,  blunt),imodbits_polearm ],
["polehammer",         "Polehammer", [("pole_hammer",0)], itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff,
 169 , weight(7)|difficulty(18)|spd_rtng(50) | weapon_length(126)|swing_damage(50 , blunt) | thrust_damage(35 ,  blunt),imodbits_polearm ],
["staff",         "Staff", [("wooden_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,
 36 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(130)|swing_damage(18 , blunt) | thrust_damage(19 ,  blunt),imodbits_polearm ],
["quarter_staff", "Quarter Staff", [("quarter_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry|itp_wooden_attack, itc_staff|itcf_carry_sword_back,
 60 , weight(2)|difficulty(0)|spd_rtng(104) | weapon_length(140)|swing_damage(20 , blunt) | thrust_damage(20 ,  blunt),imodbits_polearm ],
["iron_staff",         "Iron Staff", [("iron_staff",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary, itc_staff|itcf_carry_sword_back,
 202 , weight(2)|difficulty(0)|spd_rtng(97) | weapon_length(140)|swing_damage(25 , blunt) | thrust_damage(26 ,  blunt),imodbits_polearm ],

#["glaive_b",         "Glaive_b", [("glaive_b",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_staff|itcf_carry_spear,
# 352 , weight(4.5)|difficulty(0)|spd_rtng(83) | weapon_length(157)|swing_damage(38 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm ],


["shortened_spear",         "Shortened Spear", [("spear_g_1-9m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
 53 , weight(2.0)|difficulty(0)|spd_rtng(102) | weapon_length(120)|swing_damage(19 , blunt) | thrust_damage(25 ,  pierce),imodbits_polearm ],
["spear",         "Spear", [("spear_h_2-15m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
 85 , weight(2.25)|difficulty(0)|spd_rtng(98) | weapon_length(135)|swing_damage(20 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],

["bamboo_spear",         "Bamboo Spear", [("arabian_spear_a_3m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,
 80 , weight(2.0)|difficulty(0)|spd_rtng(88) | weapon_length(200)|swing_damage(15 , blunt) | thrust_damage(20 ,  pierce),imodbits_polearm ],




["war_spear",         "War Spear", [("spear_i_2-3m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
 140 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(150)|swing_damage(20 , blunt) | thrust_damage(27 ,  pierce),imodbits_polearm ],
#TODO:["shortened_spear",         "shortened_spear", [("spear_e_2-1m",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
# 65 , weight(2.0)|difficulty(0)|spd_rtng(98) | weapon_length(110)|swing_damage(17 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],
#TODO:["spear_2-4m",         "spear", [("spear_e_2-25m",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,
# 67 , weight(2.0)|difficulty(0)|spd_rtng(95) | weapon_length(125)|swing_damage(17 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],
["military_scythe",         "Military Scythe", [("spear_e_2-5m",0),("spear_c_2-5m",imodbits_bad)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,
 155 , weight(2.5)|difficulty(0)|spd_rtng(90) | weapon_length(155)|swing_damage(36 , cut) | thrust_damage(25 ,  pierce),imodbits_polearm ],
["light_lance",         "Light Lance", [("spear_b_2-75m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
 180 , weight(2.5)|difficulty(0)|spd_rtng(85) | weapon_length(175)|swing_damage(16 , blunt) | thrust_damage(27 ,  pierce),imodbits_polearm ],
["lance",         "Lance", [("spear_d_2-8m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
 270 , weight(2.5)|difficulty(0)|spd_rtng(80) | weapon_length(180)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["heavy_lance",         "Heavy Lance", [("spear_f_2-9m",0)], itp_couchable|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear,
 360 , weight(2.75)|difficulty(10)|spd_rtng(75) | weapon_length(190)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
["great_lance",         "Great Lance", [("heavy_lance",0)], itp_couchable|itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_greatlance,
 410 , weight(5)|difficulty(11)|spd_rtng(55) | weapon_length(240)|swing_damage(0 , cut) | thrust_damage(21 ,  pierce),imodbits_polearm ],
["pike",         "Pike", [("spear_a_3m",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_cutting_spear,
 125 , weight(3.0)|difficulty(0)|spd_rtng(81) | weapon_length(245)|swing_damage(16 , blunt) | thrust_damage(26 ,  pierce),imodbits_polearm ],
##["spear_e_3-25m",         "Spear_3-25m", [("spear_e_3-25m",0)], itp_type_polearm|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
## 150 , weight(4.5)|difficulty(0)|spd_rtng(81) | weapon_length(225)|swing_damage(19 , blunt) | thrust_damage(23 ,  pierce),imodbits_polearm ],
["ashwood_pike", "Ashwood Pike", [("pike",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_cutting_spear,
 205 , weight(3.5)|difficulty(9)|spd_rtng(90) | weapon_length(170)|swing_damage(19 , blunt) | thrust_damage(29,  pierce),imodbits_polearm ],
["awlpike",    "Awlpike", [("awl_pike_b",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 345 , weight(2.25)|difficulty(0)|spd_rtng(92) | weapon_length(165)|swing_damage(20 , blunt) | thrust_damage(33 ,  pierce),imodbits_polearm ],
["awlpike_long",  "Long Awlpike", [("awl_pike_a",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
 385 , weight(2.25)|difficulty(0)|spd_rtng(89) | weapon_length(185)|swing_damage(20 , blunt) | thrust_damage(32 ,  pierce),imodbits_polearm ],
#["awlpike",         "Awlpike", [("pike",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry, itc_cutting_spear|itcf_carry_spear,
# 378 , weight(3.5)|difficulty(12)|spd_rtng(92) | weapon_length(160)|swing_damage(20 ,blunt) | thrust_damage(31 ,  pierce),imodbits_polearm ],

["bec_de_corbin_a",  "War Hammer", [("bec_de_corbin_a",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_cutting_spear|itcf_carry_spear,
 125 , weight(3.0)|difficulty(0)|spd_rtng(81) | weapon_length(120)|swing_damage(38, blunt) | thrust_damage(38 ,  pierce),imodbits_polearm ],



# SHIELDS

["wooden_shield", "Wooden Shield", [("shield_round_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
##["wooden_shield", "Wooden Shield", [("shield_round_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  42 , weight(2)|hit_points(360)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield,




#["round_shield", "Round Shield", [("shield_round_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  64 , weight(2)|hit_points(400)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
["nordic_shield", "Nordic Shield", [("shield_round_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  95 , weight(2)|hit_points(440)|body_armor(1)|spd_rtng(100)|shield_width(50),imodbits_shield ],
#["kite_shield",         "Kite Shield", [("shield_kite_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["kite_shield_", "Kite Shield", [("shield_kite_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["large_shield", "Large Shield", [("shield_kite_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  165 , weight(2.5)|hit_points(520)|body_armor(1)|spd_rtng(80)|shield_width(92),imodbits_shield ],
#["battle_shield", "Battle Shield", [("shield_kite_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  196 , weight(3)|hit_points(560)|body_armor(1)|spd_rtng(78)|shield_width(94),imodbits_shield ],
["fur_covered_shield",  "Fur Covered Shield", [("shield_kite_m",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  227 , weight(3.5)|hit_points(600)|body_armor(1)|spd_rtng(76)|shield_width(81),imodbits_shield ],
#["heraldric_shield", "Heraldric Shield", [("shield_heraldic",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  301 , weight(3.5)|hit_points(640)|body_armor(1)|spd_rtng(83)|shield_width(65),imodbits_shield ],
#["heater_shield", "Heater Shield", [("shield_heater_a",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  477 , weight(3.5)|hit_points(710)|body_armor(4)|spd_rtng(80)|shield_width(60),imodbits_shield ],
["steel_shield", "Steel Shield", [("shield_dragon",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  697 , weight(4)|hit_points(700)|body_armor(17)|spd_rtng(61)|shield_width(40),imodbits_shield ],
#["nomad_shield", "Nomad Shield", [("shield_wood_b",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  12 , weight(2)|hit_points(260)|body_armor(6)|spd_rtng(110)|shield_width(30),imodbits_shield ],

["plate_covered_round_shield", "Plate Covered Round Shield", [("shield_round_e",0)], itp_type_shield, itcf_carry_round_shield,  140 , weight(4)|hit_points(330)|body_armor(16)|spd_rtng(90)|shield_width(40),imodbits_shield ],
["leather_covered_round_shield", "Leather Covered Round Shield", [("shield_round_d",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  80 , weight(2.5)|hit_points(310)|body_armor(8)|spd_rtng(96)|shield_width(40),imodbits_shield ],
["hide_covered_round_shield", "Hide Covered Round Shield", [("shield_round_f",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  40 , weight(2)|hit_points(260)|body_armor(3)|spd_rtng(100)|shield_width(40),imodbits_shield ],

["shield_heater_c", "Heater Shield", [("shield_heater_c",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  277 , weight(3.5)|hit_points(410)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
#["shield_heater_d", "Heater Shield", [("shield_heater_d",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  477 , weight(3.5)|hit_points(710)|body_armor(4)|spd_rtng(80)|shield_width(60),imodbits_shield ],

#["shield_kite_g",         "Kite Shield g", [("shield_kite_g",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["shield_kite_h",         "Kite Shield h", [("shield_kite_h",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["shield_kite_i",         "Kite Shield i ", [("shield_kite_i",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
#["shield_kite_k",         "Kite Shield k", [("shield_kite_k",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],

["norman_shield_1",         "Kite Shield", [("norman_shield_1",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_2",         "Kite Shield", [("norman_shield_2",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_3",         "Kite Shield", [("norman_shield_3",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_4",         "Kite Shield", [("norman_shield_4",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_5",         "Kite Shield", [("norman_shield_5",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_6",         "Kite Shield", [("norman_shield_6",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_7",         "Kite Shield", [("norman_shield_7",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],
["norman_shield_8",         "Kite Shield", [("norman_shield_8",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|shield_width(90),imodbits_shield ],

["tab_shield_round_a", "Old Round Shield", [("tableau_shield_round_5",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
26 , weight(2.5)|hit_points(195)|body_armor(4)|spd_rtng(93)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_5", ":agent_no", ":troop_no")])]],
["tab_shield_round_b", "Plain Round Shield", [("tableau_shield_round_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
65 , weight(3)|hit_points(260)|body_armor(8)|spd_rtng(90)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_3", ":agent_no", ":troop_no")])]],
["tab_shield_round_c", "Round Shield", [("tableau_shield_round_2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
105 , weight(3.5)|hit_points(310)|body_armor(12)|spd_rtng(87)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner","tableau_round_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_round_d", "Heavy Round Shield", [("tableau_shield_round_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
210 , weight(4)|hit_points(350)|body_armor(15)|spd_rtng(84)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_round_e", "Huscarl's Round Shield", [("tableau_shield_round_4",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,
430 , weight(4.5)|hit_points(410)|body_armor(19)|spd_rtng(81)|shield_width(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_round_shield_4", ":agent_no", ":troop_no")])]],

["tab_shield_kite_a", "Old Kite Shield",   [("tableau_shield_kite_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
33 , weight(2)|hit_points(165)|body_armor(5)|spd_rtng(96)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_kite_b", "Plain Kite Shield",   [("tableau_shield_kite_3" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
70 , weight(2.5)|hit_points(215)|body_armor(10)|spd_rtng(93)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_3", ":agent_no", ":troop_no")])]],
["tab_shield_kite_c", "Kite Shield",   [("tableau_shield_kite_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
156 , weight(3)|hit_points(265)|body_armor(13)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_kite_d", "Heavy Kite Shield",   [("tableau_shield_kite_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
320 , weight(3.5)|hit_points(310)|body_armor(18)|spd_rtng(87)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_kite_cav_a", "Horseman's Kite Shield",   [("tableau_shield_kite_4" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
205 , weight(2)|hit_points(165)|body_armor(14)|spd_rtng(103)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":agent_no", ":troop_no")])]],
["tab_shield_kite_cav_b", "Knightly Kite Shield",   [("tableau_shield_kite_4" ,0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,
360 , weight(2.5)|hit_points(225)|body_armor(23)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_kite_shield_4", ":agent_no", ":troop_no")])]],

["tab_shield_heater_a", "Old Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
36 , weight(2)|hit_points(160)|body_armor(6)|spd_rtng(96)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_b", "Plain Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
74 , weight(2.5)|hit_points(210)|body_armor(11)|spd_rtng(93)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_c", "Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
160 , weight(3)|hit_points(260)|body_armor(14)|spd_rtng(90)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_d", "Heavy Heater Shield",   [("tableau_shield_heater_1" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
332 , weight(3.5)|hit_points(305)|body_armor(19)|spd_rtng(87)|shield_width(36)|shield_height(70),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_heater_cav_a", "Horseman's Heater Shield",   [("tableau_shield_heater_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
229 , weight(2)|hit_points(160)|body_armor(16)|spd_rtng(103)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_heater_cav_b", "Knightly Heater Shield",   [("tableau_shield_heater_2" ,0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
390 , weight(2.5)|hit_points(220)|body_armor(23)|spd_rtng(100)|shield_width(30)|shield_height(50),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heater_shield_2", ":agent_no", ":troop_no")])]],

["tab_shield_pavise_a", "Old Board Shield",   [("tableau_shield_pavise_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
60 , weight(3.5)|hit_points(280)|body_armor(4)|spd_rtng(89)|shield_width(43)|shield_height(100),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_pavise_b", "Plain Board Shield",   [("tableau_shield_pavise_2" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
114 , weight(4)|hit_points(360)|body_armor(8)|spd_rtng(85)|shield_width(43)|shield_height(100),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_2", ":agent_no", ":troop_no")])]],
["tab_shield_pavise_c", "Board Shield",   [("tableau_shield_pavise_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
210 , weight(4.5)|hit_points(430)|body_armor(10)|spd_rtng(81)|shield_width(43)|shield_height(100),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_pavise_d", "Heavy Board Shield",   [("tableau_shield_pavise_1" ,0)], itp_merchandise|itp_type_shield|itp_cant_use_on_horseback|itp_wooden_parry, itcf_carry_board_shield,
370 , weight(5)|hit_points(550)|body_armor(14)|spd_rtng(78)|shield_width(43)|shield_height(100),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_pavise_shield_1", ":agent_no", ":troop_no")])]],

["tab_shield_small_round_a", "Plain Cavalry Shield", [("tableau_shield_small_round_3",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
96 , weight(2)|hit_points(160)|body_armor(8)|spd_rtng(105)|shield_width(40),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_3", ":agent_no", ":troop_no")])]],
["tab_shield_small_round_b", "Round Cavalry Shield", [("tableau_shield_small_round_1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,
195 , weight(2.5)|hit_points(200)|body_armor(14)|spd_rtng(103)|shield_width(40),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_1", ":agent_no", ":troop_no")])]],
["tab_shield_small_round_c", "Elite Cavalry Shield", [("tableau_shield_small_round_2",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,
370 , weight(3)|hit_points(250)|body_armor(22)|spd_rtng(100)|shield_width(40),imodbits_shield,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_small_round_shield_2", ":agent_no", ":troop_no")])]],


 #RANGED


#TODO:
["darts",         "Darts", [("dart_b",0),("dart_b_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_right_vertical|itcf_show_holster_when_drawn,
155 , weight(4)|difficulty(1)|spd_rtng(95) | shoot_speed(28) | thrust_damage(22 ,  pierce)|max_ammo(7)|weapon_length(32),imodbits_thrown ],
["war_darts",         "War Darts", [("dart_a",0),("dart_a_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,
285 , weight(5)|difficulty(1)|spd_rtng(93) | shoot_speed(27) | thrust_damage(25 ,  pierce)|max_ammo(7)|weapon_length(45),imodbits_thrown ],

["javelin",         "Javelins", [("javelin",0),("javelins_quiver_new", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,
300, weight(4)|difficulty(1)|spd_rtng(91) | shoot_speed(25) | thrust_damage(34 ,  pierce)|max_ammo(5)|weapon_length(75),imodbits_thrown ],
["javelin_melee",         "Javelin", [("javelin",0)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_staff,
300, weight(1)|difficulty(0)|spd_rtng(95) |swing_damage(12, cut)| thrust_damage(14,  pierce)|weapon_length(75),imodbits_polearm ],

["throwing_spears",         "Throwing Spears", [("jarid_new_b",0),("jarid_new_b_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,
525 , weight(3)|difficulty(2)|spd_rtng(87) | shoot_speed(22) | thrust_damage(44 ,  pierce)|max_ammo(4)|weapon_length(65),imodbits_thrown ],
["throwing_spear_melee",         "Throwing Spear", [("jarid_new_b",0),("javelins_quiver", ixmesh_carry)],itp_type_polearm|itp_primary|itp_wooden_parry , itc_staff,
525 , weight(1)|difficulty(1)|spd_rtng(91) | swing_damage(18, cut) | thrust_damage(23 ,  pierce)|weapon_length(75),imodbits_thrown ],

["jarid",         "Jarids", [("jarid_new",0),("jarid_quiver", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn,
560 , weight(2.75)|difficulty(2)|spd_rtng(89) | shoot_speed(24) | thrust_damage(45 ,  pierce)|max_ammo(4)|weapon_length(65),imodbits_thrown ],
["jarid_melee",         "Jarid", [("jarid_new",0),("jarid_quiver", ixmesh_carry)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_staff,
560 , weight(1)|difficulty(2)|spd_rtng(93) | swing_damage(16, cut) | thrust_damage(20 ,  pierce)|weapon_length(65),imodbits_thrown ],


#TODO:
#TODO: Heavy throwing Spear
["stones",         "Stones", [("throwing_stone",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_stone, 1 , weight(4)|difficulty(0)|spd_rtng(97) | shoot_speed(30) | thrust_damage(11 ,  blunt)|max_ammo(18)|weapon_length(8),imodbit_large_bag ],

["throwing_knives", "Throwing Knives", [("throwing_knife",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_knife, 76 , weight(2.5)|difficulty(0)|spd_rtng(121) | shoot_speed(25) | thrust_damage(19 ,  cut)|max_ammo(14)|weapon_length(0),imodbits_thrown ],
["throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_knife, 193 , weight(2.5)|difficulty(0)|spd_rtng(110) | shoot_speed(24) | thrust_damage(25 ,  cut)|max_ammo(13)|weapon_length(0),imodbits_thrown ],
#TODO: Light Trowing axe, Heavy Throwing Axe
["light_throwing_axes", "Light Throwing Axes", [("francisca",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
360, weight(5)|difficulty(2)|spd_rtng(99) | shoot_speed(18) | thrust_damage(35,cut)|max_ammo(4)|weapon_length(53),imodbits_thrown_minus_heavy ],
["light_throwing_axes_melee", "Light Throwing Axe", [("francisca",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
360, weight(1)|difficulty(2)|spd_rtng(99)|weapon_length(53)| swing_damage(26,cut),imodbits_thrown_minus_heavy ],
["throwing_axes", "Throwing Axes", [("throwing_axe_a",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
490, weight(5)|difficulty(3)|spd_rtng(98) | shoot_speed(18) | thrust_damage(39,cut)|max_ammo(4)|weapon_length(53),imodbits_thrown_minus_heavy ],
["throwing_axes_melee", "Throwing Axe", [("throwing_axe_a",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
490, weight(1)|difficulty(3)|spd_rtng(98) | swing_damage(29,cut)|weapon_length(53),imodbits_thrown_minus_heavy ],
["heavy_throwing_axes", "Heavy Throwing Axes", [("throwing_axe_b",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
620, weight(5)|difficulty(4)|spd_rtng(97) | shoot_speed(18) | thrust_damage(44,cut)|max_ammo(4)|weapon_length(53),imodbits_thrown_minus_heavy ],
["heavy_throwing_axes_melee", "Heavy Throwing Axe", [("throwing_axe_b",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
620, weight(1)|difficulty(4)|spd_rtng(97) | swing_damage(32,cut)|weapon_length(53),imodbits_thrown_minus_heavy ],



["hunting_bow",         "Hunting Bow", [("hunting_bow",0),("hunting_bow_carry",ixmesh_carry)],itp_type_bow |itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back,
17 , weight(1)|difficulty(0)|spd_rtng(100) | shoot_speed(52) | thrust_damage(15 ,  pierce),imodbits_bow ],
["short_bow",         "Short Bow", [("short_bow",0),("short_bow_carry",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back,
58 , weight(1)|difficulty(1)|spd_rtng(97) | shoot_speed(55) | thrust_damage(18 ,  pierce  ),imodbits_bow ],
["nomad_bow",         "Nomad Bow", [("nomad_bow",0),("nomad_bow_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,
164 , weight(1.25)|difficulty(2)|spd_rtng(94) | shoot_speed(56) | thrust_damage(20 ,  pierce),imodbits_bow ],
["long_bow",         "Long Bow", [("long_bow",0),("long_bow_carry",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back,
145 , weight(1.75)|difficulty(3)|spd_rtng(79) | shoot_speed(56) | thrust_damage(22 ,  pierce),imodbits_bow ],
["khergit_bow",         "Khergit Bow", [("khergit_bow",0),("khergit_bow_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,
269 , weight(1.25)|difficulty(3)|spd_rtng(90) | shoot_speed(57) | thrust_damage(21 ,pierce),imodbits_bow ],
["strong_bow",         "Strong Bow", [("strong_bow",0),("strong_bow_case", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn,
437 , weight(1.25)|difficulty(3)|spd_rtng(88) | shoot_speed(58) | thrust_damage(23 ,pierce),imodbit_cracked | imodbit_bent | imodbit_masterwork ],
["war_bow",         "War Bow", [("war_bow",0),("war_bow_carry",ixmesh_carry)],itp_type_bow|itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back,
728 , weight(1.5)|difficulty(4)|spd_rtng(84) | shoot_speed(59) | thrust_damage(25 ,pierce),imodbits_bow ],
["hunting_crossbow", "Hunting Crossbow", [("crossbow_a",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back,
22 , weight(2.25)|difficulty(0)|spd_rtng(47) | shoot_speed(50) | thrust_damage(37 ,  pierce)|max_ammo(1),imodbits_crossbow ],
["light_crossbow", "Light Crossbow", [("crossbow_b",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_crossbow|itcf_carry_crossbow_back,
67 , weight(2.5)|difficulty(8)|spd_rtng(45) | shoot_speed(59) | thrust_damage(44 ,  pierce)|max_ammo(1),imodbits_crossbow ],
["crossbow",         "Crossbow",         [("crossbow_a",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back,
182 , weight(3)|difficulty(8)|spd_rtng(43) | shoot_speed(66) | thrust_damage(49,pierce)|max_ammo(1),imodbits_crossbow ],
["heavy_crossbow", "Heavy Crossbow", [("crossbow_c",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back,
349 , weight(3.5)|difficulty(9)|spd_rtng(41) | shoot_speed(68) | thrust_damage(58 ,pierce)|max_ammo(1),imodbits_crossbow ],
["sniper_crossbow", "Siege Crossbow", [("crossbow_c",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back,
683 , weight(3.75)|difficulty(10)|spd_rtng(37) | shoot_speed(70) | thrust_damage(63 ,pierce)|max_ammo(1),imodbits_crossbow ],
["flintlock_pistol", "Flintlock Pistol", [("flintlock_pistol",0)], itp_type_pistol |itp_merchandise|itp_primary ,itcf_shoot_pistol|itcf_reload_pistol, 230 , weight(1.5)|difficulty(0)|spd_rtng(38) | shoot_speed(160) | thrust_damage(45 ,pierce)|max_ammo(1)|accuracy(65),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_pistol_shot"),(position_move_x, pos1,27),(position_move_y, pos1,36),(particle_system_burst, "psys_pistol_smoke", pos1, 15)])]],
["torch",         "Torch", [("club",0)], itp_type_one_handed_wpn|itp_primary, itc_scimitar, 11 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(11 , blunt) | thrust_damage(0 ,  pierce),imodbits_none,
 [(ti_on_init_item, [(set_position_delta,0,60,0),(particle_system_add_new, "psys_torch_fire"),(particle_system_add_new, "psys_torch_smoke"),(set_current_color,150, 130, 70),(add_point_light, 10, 30),
])]],

["lyre",         "Lyre", [("lyre",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],
["lute",         "Lute", [("lute",0)], itp_type_shield|itp_wooden_parry|itp_civilian, itcf_carry_bow_back,  118 , weight(2.5)|hit_points(480)|body_armor(1)|spd_rtng(82)|weapon_length(90),0 ],

##["short_sword", "Short Sword",
## [("sword_norman",0),("sword_norman_scabbard", ixmesh_carry),("sword_norman_rusty",imodbit_rusty),("sword_norman_rusty_scabbard", ixmesh_carry|imodbit_rusty)],
## itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 183 , weight(1.25)|difficulty(0)|spd_rtng(103) | weapon_length(75)|swing_damage(25 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],

["strange_armor",  "Strange Armor", [("samurai_armor",0)], itp_type_body_armor  |itp_covers_legs ,0, 1259 , weight(18)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(19)|difficulty(7) ,imodbits_armor ],
["strange_boots",  "Strange Boots", [("samurai_boots",0)], itp_type_foot_armor | itp_attach_armature,0, 465 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(21)|difficulty(0) ,imodbits_cloth ],
["strange_helmet", "Strange Helmet", [("samurai_helmet",0)], itp_type_head_armor   ,0, 824 , weight(2)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["strange_sword", "Strange Sword", [("katana",0),("katana_scabbard",ixmesh_carry)], itp_type_two_handed_wpn| itp_primary, itc_bastardsword|itcf_carry_katana|itcf_show_holster_when_drawn, 679 , weight(2.0)|difficulty(9)|spd_rtng(108) | weapon_length(95)|swing_damage(32 , cut) | thrust_damage(18 ,  pierce),imodbits_sword ],
["strange_great_sword",  "Strange Great Sword", [("no_dachi",0),("no_dachi_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_nodachi|itcf_carry_sword_back|itcf_show_holster_when_drawn, 920 , weight(3.5)|difficulty(11)|spd_rtng(92) | weapon_length(125)|swing_damage(38 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],
["strange_short_sword", "Strange Short Sword", [("wakizashi",0),("wakizashi_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_wakizashi|itcf_show_holster_when_drawn, 321 , weight(1.25)|difficulty(0)|spd_rtng(108) | weapon_length(65)|swing_damage(25 , cut) | thrust_damage(19 ,  pierce),imodbits_sword ],
["court_dress", "Court Dress", [("court_dress",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
["rich_outfit", "Rich Outfit", [("merchant_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 348 , weight(4)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
["khergit_guard_armor", "Khergit Guard Armor", [("lamellar_armor_a",0)], itp_type_body_armor|itp_covers_legs   ,0,
3048 , weight(25)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(18)|difficulty(0) ,imodbits_armor ],
#["leather_steppe_cap_c", "Leather Steppe Cap", [("leather_steppe_cap_c",0)], itp_type_head_armor   ,0, 51 , weight(2)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["felt_steppe_cap", "Felt Steppe Cap", [("felt_steppe_cap",0)], itp_type_head_armor   ,0, 237 , weight(2)|abundance(100)|head_armor(16)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["khergit_war_helmet", "Khergit War Helmet", [("tattered_steppe_cap_a_new",0)], itp_type_head_armor | itp_merchandise   ,0, 200 , weight(2)|abundance(100)|head_armor(31)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["khergit_helmet", "Khergit Helmet", [("khergit_guard_helmet",0)], itp_type_head_armor   ,0, 361 , weight(2)|abundance(100)|head_armor(33)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
#["khergit_sword", "Khergit Sword", [("khergit_sword",0),("khergit_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 183 , weight(1.25)|difficulty(0)|spd_rtng(100) | weapon_length(97)|swing_damage(23 , cut) | thrust_damage(14 ,  pierce),imodbits_sword ],
["khergit_guard_boots",  "Khergit Guard Boots", [("lamellar_boots_a",0)], itp_type_foot_armor | itp_attach_armature,0, 254 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],
["khergit_guard_helmet", "Khergit Guard Helmet", [("lamellar_helmet_a",0)], itp_type_head_armor |itp_merchandise   ,0, 433 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["khergit_cavalry_helmet", "Khergit Cavalry Helmet", [("lamellar_helmet_b",0)], itp_type_head_armor | itp_merchandise   ,0, 333 , weight(2)|abundance(100)|head_armor(36)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],

["black_hood", "Black Hood", [("hood_black",0)], itp_type_head_armor|itp_merchandise   ,0, 193 , weight(2)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["light_leather", "Light Leather", [("light_leather",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 352 , weight(5)|abundance(100)|head_armor(0)|body_armor(26)|leg_armor(7)|difficulty(0) ,imodbits_armor ],
["light_leather_boots",  "Light Leather Boots", [("light_leather_boots",0)], itp_type_foot_armor |itp_merchandise| itp_attach_armature,0, 91 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
["mail_and_plate", "Mail and Plate", [("mail_and_plate",0)], itp_type_body_armor|itp_covers_legs   ,0, 593 , weight(16)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(12)|difficulty(0) ,imodbits_armor ],
["light_mail_and_plate", "Light Mail and Plate", [("light_mail_and_plate",0)], itp_type_body_armor|itp_covers_legs   ,0, 532 , weight(10)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_armor ],

["byzantion_helmet_a", "Byzantion Helmet", [("byzantion_helmet_a",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["magyar_helmet_a", "Magyar Helmet", [("magyar_helmet_a",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["rus_helmet_a", "Rus Helmet", [("rus_helmet_a",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["sipahi_helmet_a", "Sipahi Helmet", [("sipahi_helmet_a",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["shahi", "Shahi", [("shahi",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["rabati", "Rabati", [("rabati",0)], itp_type_head_armor   ,0, 278 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],

["tunic_with_green_cape", "Tunic with Green Cape", [("peasant_man_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["keys", "Ring of Keys", [("throwing_axe_a",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
240, weight(5)|spd_rtng(98) | swing_damage(29,cut)|max_ammo(5)|weapon_length(53),imodbits_thrown ],
["bride_dress", "Bride Dress", [("bride_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["bride_crown", "Crown of Flowers", [("bride_crown",0)],  itp_type_head_armor | itp_doesnt_cover_hair |itp_civilian |itp_attach_armature,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bride_shoes", "Bride Shoes", [("bride_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],

["practice_bow_2","Practice Bow", [("hunting_bow",0), ("hunting_bow_carry",ixmesh_carry)], itp_type_bow |itp_primary|itp_two_handed,itcf_shoot_bow|itcf_carry_bow_back, 0, weight(1.5)|spd_rtng(90) | shoot_speed(40) | thrust_damage(21, blunt),imodbits_bow ],
["practice_arrows_2","Practice Arrows", [("arena_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 0,weight(1.5)|weapon_length(95)|max_ammo(80),imodbits_missile],


["plate_boots", "Plate Boots", [("plate_boots",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 1770 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_plate ],

["heraldic_mail_with_surcoat_for_tableau", "{!}Heraldic Mail with Surcoat", [("heraldic_armor_new_a",0)], itp_type_body_armor |itp_covers_legs ,0,
 1, weight(22)|abundance(100)|head_armor(0)|body_armor(1)|leg_armor(1),imodbits_armor,
 [(ti_on_init_item, [(store_trigger_param_1, ":agent_no"),(store_trigger_param_2, ":troop_no"),(call_script, "script_shield_item_set_banner", "tableau_heraldic_armor_a", ":agent_no", ":troop_no")])]],
["mail_boots_for_tableau", "Mail Boots", [("mail_boots_a",0)], itp_type_foot_armor | itp_attach_armature  ,0,
 1, weight(3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(1) ,imodbits_armor ],
["warhorse_sarranid","Sarranian War Horse", [("warhorse_sarranid",0)], itp_merchandise|itp_type_horse, 0, 1811,abundance(40)|hit_points(165)|body_armor(58)|difficulty(4)|horse_speed(40)|horse_maneuver(44)|horse_charge(32)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_6]],
["warhorse_steppe","Steppe Charger", [("warhorse_steppe",0)], itp_merchandise|itp_type_horse, 0, 1400,abundance(45)|hit_points(150)|body_armor(40)|difficulty(4)|horse_speed(40)|horse_maneuver(50)|horse_charge(28)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_3,fac_kingdom_2]],

##diplomacy begin
["dplmc_coat_of_plates_red_constable", "Constable Coat of Plates", [("coat_of_plates_red",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(0) ,imodbits_armor, [], []],
##diplomacy end


##################################### 
###insert new items for TGS
#####################################
 #weight(2.25)
 ["power_ammo","One Power Ammo", [("cartridge_a",0),("practice_arrows_2",ixmesh_flying_ammo)], itp_type_bullets|itp_can_penetrate_shield|itp_default_ammo, 0, 5,weight(0.01)|abundance(90)|weapon_length(3)|thrust_damage(1,pierce)|max_ammo(200),imodbits_missile],
#

#####################################
#Magic items for test  (itcf_thrust_onehanded|itcf_thrust_onehanded_lance_horseback)
#####################################
 #["power_player","One Power", [("dagger_b",0),("practice_arrows_2",ixmesh_flying_ammo)],itp_type_pistol|itp_primary|itp_secondary|itp_bonus_against_shield , itcf_shoot_crossbow, 5 , weight(4)|spd_rtng(250) | shoot_speed(150) | thrust_damage(1 ,  pierce)|max_ammo(5000)|weapon_length(65),imodbits_missile,
 
 ["power_player","One Power", [("cuindiar_disc",0),("practice_arrows_2",ixmesh_flying_ammo)],itp_type_pistol|itp_primary|itp_secondary|itp_bonus_against_shield , itcf_shoot_crossbow, 5 , weight(4)|spd_rtng(250) | shoot_speed(120) | thrust_damage(1 ,  pierce)|max_ammo(255)|weapon_length(65),imodbits_none,
  [(ti_on_weapon_attack, [

#            (assign,":distance",99999),   
#            (try_for_agents,":agent"),
#                (agent_is_alive,":agent"),
#                (neg|agent_is_wounded,":agent"), ## add this to not re-count wounded people
#                (agent_is_human,":agent"),
#                (agent_get_look_position, pos2, ":agent"), 
#                (get_distance_between_positions,":dist",pos1,pos2),
#                (lt,":dist",":distance"),
#                (assign,":chosen",":agent"), # 'chosen' is the shooter
#                (assign,":distance",":dist"),
#            (try_end),
            
            (store_trigger_param_1, ":chosen"),

## Run the channeling code only if the channeling agent is not shielded
            (agent_get_slot, ":agent_is_shielded", ":chosen", slot_agent_is_shielded),

            (try_begin),
            (eq, ":agent_is_shielded", 0),
                (call_script, "script_tgs_select_weave",":chosen"),
######################################### Run the "Shield Breaker" code if the channeler is shielded...
            (else_try),
                (call_script,"script_tgs_break_shield",":chosen"),
            (try_end),

#   Player specific code
            (try_begin),
            (neg|agent_is_non_player, ":chosen"),
                (val_add, "$g_number_of_weaves_used", 1),
                (try_begin),
                (ge, "$g_number_of_weaves_used", 130),
                    (display_message, "str_almost_out_of_ammo"),
                (try_end),
                (val_add, "$g_channeling_proficiency_modifier", 5),
            (try_end),

                         ],),
    ]],


############################################################
############################################################
#itcf_thrust_onehanded|itcf_thrust_onehanded_lance_horseback
 
 ["power_npc_companion_ranged","One Power", [("cuindiar_disc",0),("practice_arrows_2",ixmesh_flying_ammo)],itp_type_pistol|itp_primary|itp_bonus_against_shield , itcf_shoot_crossbow, 5 , weight(4)|spd_rtng(140) | shoot_speed(150) | thrust_damage(1 ,  pierce)|max_ammo(5000)|weapon_length(65)|difficulty(0),imodbits_missile,
  [(ti_on_weapon_attack, [

#            (get_player_agent_no,":player_agent"),

            (assign,":distance",99999),
                     
            (try_for_agents,":agent"),
                (agent_is_alive,":agent"),
                (neg|agent_is_wounded,":agent"), ## add this to not re-count wounded people
                (agent_is_human,":agent"),
                (agent_get_look_position, pos2, ":agent"), 
                (get_distance_between_positions,":dist",pos1,pos2),
                (lt,":dist",":distance"),
                (assign,":chosen",":agent"), # 'chosen' is the shooter
                (assign,":distance",":dist"),
            (try_end),

            (agent_get_slot, ":shielded", ":chosen", slot_agent_is_shielded),

            (try_begin),
            (eq, ":shielded", 0), # try if not shielded

                (agent_get_horse, ":chosen_horse", ":chosen"),
                (agent_get_team, ":chosen_team", ":chosen"),

                (store_random_in_range, ":random", 1, 100),

                (try_begin),
                (le, ":random", 100), # percent chance that weave will work (depends on the 'experience' of the unit that will use the item)

                # Start npc companion weave selection code
                    (agent_get_troop_id, ":chosen_troop_id", ":chosen"),
                    (troop_get_slot, ":chosen_primary_weave", ":chosen_troop_id", slot_troop_npc_companion_primary_weave),
                    (troop_get_slot, ":chosen_secondary_weave", ":chosen_troop_id", slot_troop_npc_companion_secondary_weave),
            
                    (try_begin),
                    (gt, ":chosen_primary_weave", 0),
                    (gt, ":chosen_secondary_weave", 0),
                        # Primary and secondary weaves have been selected.  (75% of the time, the primary weave will be used, 25% of the time, the secondary weave will be used.)
                        (store_random_in_range, ":random", 1, 100),
                        (try_begin),
                        (le, ":random", 75),
                            (assign, ":active_weave", ":chosen_primary_weave"),
                        (else_try),
                            (assign, ":active_weave", ":chosen_secondary_weave"),
                        (try_end),
                    (else_try), # Only the primary weave has been selected
                    (gt, ":chosen_primary_weave", 0),
                    (eq, ":chosen_secondary_weave", 0),
                        (assign, ":active_weave", ":chosen_primary_weave"),
                    (else_try), # Only the secondary weave has been selected
                    (eq, ":chosen_primary_weave", 0),
                    (gt, ":chosen_secondary_weave", 0),
                        (assign, ":active_weave", ":chosen_secondary_weave"),
                    (else_try), # Neither a primary weave nor a secondary weave has been selected
                    (eq, ":chosen_primary_weave", 0),
                    (eq, ":chosen_secondary_weave", 0),
                        (troop_get_slot, ":known_weaves", ":chosen_troop_id", slot_troop_npc_companion_known_weaves),
                        (val_add, ":known_weaves", 1),
                        (store_random_in_range, ":active_weave", 1, ":known_weaves"),
                    (try_end),

                # End npc companion weave selection code            


################################## Weave 2
                    (try_begin),
                    (eq, ":active_weave", 1),
                         #Freeze Weave

                        (assign, ":times_near_ground", 0),
                        (assign, ":near_enemy", 0),

                        (try_for_range,reg5,1,500),  ###was 500
                        (eq, ":times_near_ground", 0),
                            (particle_system_burst, "psys_freeze_blast", pos1, 10),
                            (position_move_y,pos1,30),

                            #added for gravity effect and flight randomness
                            (store_mod, ":fall", reg5, 2),
                            (try_begin),
                            (eq, ":fall", 0),
                                (position_move_x,pos1,3),
                            (try_end),

                            (store_mod, ":weave", reg5, 5),
                            (try_begin),
                            (eq, ":weave", 0),
                                (store_random_in_range, ":random", -7, 8),
                                (position_move_z,pos1,":random"),
                            (try_end),
                            #end added for gravity effect and flight randomness
            
                            (copy_position,pos2,pos1),
                            (position_set_z_to_ground_level, pos2),
                            (get_distance_between_positions,":dist",pos1,pos2),

                            (position_get_z, ":z_ground", pos2),
                            (store_add, ":z_ground_low", ":z_ground", 200),
                            (store_add, ":z_ground_high", ":z_ground", 2000),

                            (try_for_agents, ":agent"),
                            (eq, ":near_enemy", 0),
                                (neq, ":chosen", ":agent"),
                                (neq, ":chosen_horse", ":agent"),
                                (agent_get_team, ":agent_team", ":agent"),
                                (teams_are_enemies, ":chosen_team", ":agent_team"),
                                (agent_is_alive, ":agent"),
                                (neg|agent_is_wounded, ":agent"),
                                (agent_get_look_position, pos4, ":agent"),
                                (get_distance_between_positions, ":dist_2", pos2, pos4),
                                (position_get_z, ":z_attack_trail", pos1),
                                (lt, ":dist_2", 50), # near agent (x-y)
                                (is_between, ":z_attack_trail", ":z_ground_low", ":z_ground_high"), # within the agent's body (z height)
                                (assign, ":dist", 5),
                                (assign, ":near_enemy", 1),
                            (try_end),
                    
                            (try_begin),
                            (lt,":dist",10),
                                (val_add, ":times_near_ground", 1),
                                (particle_system_burst, "psys_tsunami", pos1, 75),  # effect needs a long duration
                                (play_sound,"snd_freeze"), # need a sound for freeze
                                (copy_position, pos3, pos1),
                                (scene_prop_get_instance,":instance", "spr_snowy_heap_a", 0),  #need
                                (position_copy_origin,pos2,pos1),
                                (prop_instance_set_position,":instance",pos2),
                                (assign,reg5,1000),  #was 1000
                            (try_end),
                        (try_end),
                                
                        (try_for_agents,":agent"),
                            (neq,":chosen",":agent"), ## added this to avoid freezing shooter
                            (neq, ":chosen_horse", ":agent"),
#                            (neg|agent_is_ally,":agent"), ## add this to avoid freezing allies
                            (agent_is_alive,":agent"), ## add this to not freeze dead people
                            (neg|agent_is_wounded,":agent"), ## add this to not freeze wounded people

                            #partial friendly fire protection
                            (agent_get_team, ":agent_team_ff", ":agent"),
                            (assign, ":deliver_damage", 1),
                            (try_begin),
                            (neg|teams_are_enemies, ":chosen_team", ":agent_team_ff"),
                                (store_random_in_range, ":random", 1, 5),
                                (try_begin),
                                (gt, ":random", 1), # 3 in 4 chance that ally will not be hurt by damaging weave that is targeting enemy
                                    (assign, ":deliver_damage", 0),
                                (try_end),
                            (try_end),
                            (eq, ":deliver_damage", 1),
                            #end partial friendly fire protection
            
                            (agent_get_position,pos2,":agent"),
                            (get_distance_between_positions,":dist",pos3,pos2),
                         
                            (try_begin),
                            (lt,":dist",250),  # freeze (slowed movement) if blast within 250 of agent
                                (agent_set_speed_limit, ":agent", 0),
                                (agent_deliver_damage_to_agent,":chosen",":agent"),
                                (try_begin), # add to channeling multiplier if agent is player
                                (neg|agent_is_non_player, ":chosen"),
                                    (val_add, "$g_channeling_proficiency_modifier", 80),
                                (try_end),
                                (add_xp_to_troop,40,":chosen"),
                            (try_end),
                    
                        (try_end),
                            
                        #Freeze weave end


#########################################  Weave 3
                    (else_try),
                    (eq, ":active_weave", 2),
                        # Heal Nearest Ally Weave

                        (assign, ":distance",99999),
                        (assign, ":number_of_allies", 0),

                        (try_for_agents,":agent"),
                            (agent_is_alive,":agent"), ## don't heal dead
                            (neg|agent_is_wounded,":agent"), ## don't heal wounded
                            (agent_get_team, ":agent_team", ":agent"),
                            (neg|teams_are_enemies, ":chosen_team", ":agent_team"), ## don't heal enemies
                            (agent_is_human,":agent"), ## don't look for horses on the first round
                            (neq, ":chosen", ":agent"), ## shooter can't heal self
                            (store_agent_hit_points,":health",":agent",0),
                            (lt,":health",75),
                            (agent_get_look_position, pos2, ":agent"),
                            (get_distance_between_positions,":dist",pos1,pos2),
                            (lt,":dist",":distance"),
                            (assign,":nearest_hurt_ally",":agent"),
                            (assign,":distance",":dist"),
                            (val_add, ":number_of_allies", 1),
                        (try_end),

                        (try_begin),
                        (ge, ":number_of_allies", 1),
                            (agent_set_hit_points,":nearest_hurt_ally",100,0),
                            (agent_get_look_position, pos2, ":nearest_hurt_ally"),
                            (particle_system_burst, "psys_heal_aura", pos2, 50),
                            (play_sound, "snd_heal"),
                            (try_begin), # add to channeling multiplier if agent is player
                            (neg|agent_is_non_player, ":chosen"),
                                (val_add, "$g_channeling_proficiency_modifier", 80),
                            (try_end),
                            (add_xp_to_troop,40,":chosen"),
                        (else_try),
                            (assign, ":distance",99999),
                            (assign, ":number_of_allies", 0),

                            (try_for_agents,":agent"),
                                (agent_is_alive,":agent"), ## don't heal dead
                                (neg|agent_is_wounded,":agent"), ## don't heal wounded
                                (agent_get_team, ":agent_team", ":agent"),
                                (neg|teams_are_enemies, ":chosen_team", ":agent_team"), ## don't heal enemies
                                (neg|agent_is_human,":agent"), ## look for horses on the second round
                                (neq, ":chosen", ":agent"), ## shooter can't heal self
                                (store_agent_hit_points,":health",":agent",0),
                                (lt,":health",75),
                                (agent_get_look_position, pos2, ":agent"),
                                (get_distance_between_positions,":dist",pos1,pos2),
                                (lt,":dist",":distance"),
                                (assign,":nearest_hurt_ally",":agent"),
                                (assign,":distance",":dist"),
                                (val_add, ":number_of_allies", 1),
                            (try_end),

                            (try_begin),
                            (ge, ":number_of_allies", 1),
                                (agent_set_hit_points,":nearest_hurt_ally",100,0),
                                (agent_get_look_position, pos2, ":nearest_hurt_ally"),
                                (particle_system_burst, "psys_heal_aura", pos2, 50),
                                (play_sound, "snd_heal"),
                                (try_begin), # add to channeling multiplier if agent is player
                                (neg|agent_is_non_player, ":chosen"),
                                    (val_add, "$g_channeling_proficiency_modifier", 80),
                                (try_end),
                                (add_xp_to_troop,40,":chosen"),
                            (try_end),
                        (try_end),
                        
                    # End Heal Nearest Ally Weave            


################################## Weave 4
                    (else_try),
                    (eq, ":active_weave", 3),
                         #Fire Ball (do damage based on how close agent is to the blast)

                        (assign, ":times_near_ground", 0),
                        (assign, ":near_enemy", 0),

                        (try_for_range,reg5,1,500),  ###was 500
                        (eq, ":times_near_ground", 0),
                            (particle_system_burst, "psys_torch_fire", pos1, 15),
                            (position_move_y,pos1,30),

                            #added for gravity effect and flight randomness
                            (store_mod, ":fall", reg5, 2),
                            (try_begin),
                            (eq, ":fall", 0),
                                (position_move_x,pos1,3),
                            (try_end),

                            (store_mod, ":weave", reg5, 5),
                            (try_begin),
                            (eq, ":weave", 0),
                                (store_random_in_range, ":random", -7, 8),
                                (position_move_z,pos1,":random"),
                            (try_end),
                            #end added for gravity effect and flight randomness
            
                            (copy_position,pos2,pos1),
                            (position_set_z_to_ground_level, pos2),
                            (get_distance_between_positions,":dist",pos1,pos2),

                            (position_get_z, ":z_ground", pos2),
                            (store_add, ":z_ground_low", ":z_ground", 200),
                            (store_add, ":z_ground_high", ":z_ground", 2000),

                            (try_for_agents, ":agent"),
                            (eq, ":near_enemy", 0),
                                (neq, ":chosen", ":agent"),
                                (neq, ":chosen_horse", ":agent"),
                                (agent_get_team, ":agent_team", ":agent"),
                                (teams_are_enemies, ":chosen_team", ":agent_team"),
                                (agent_is_alive, ":agent"),
                                (neg|agent_is_wounded, ":agent"),
                                (agent_get_look_position, pos4, ":agent"),
                                (get_distance_between_positions, ":dist_2", pos2, pos4),
                                (position_get_z, ":z_attack_trail", pos1),
                                (lt, ":dist_2", 50), # near agent (x-y)
                                (is_between, ":z_attack_trail", ":z_ground_low", ":z_ground_high"), # within the agent's body (z height)
                                (assign, ":dist", 5),
                                (assign, ":near_enemy", 1),
                            (try_end),
                    
                            (try_begin),
                            (lt,":dist",10),
                                (val_add, ":times_near_ground", 1),
                                (particle_system_burst, "psys_massive_fire", pos1, 15),  #need
                                (particle_system_burst, "psys_war_smoke_tall", pos1, 15),  #need
                                (play_sound,"snd_fire_ball"),
                                (copy_position, pos3, pos1),
                                (scene_prop_get_instance,":instance", "spr_explosion", 0),  #need
                                (position_copy_origin,pos2,pos1),
                                (prop_instance_set_position,":instance",pos2),
                                (position_move_z,pos2,1000),
                                (prop_instance_animate_to_position,":instance",pos2,175),
                                (assign,reg5,1000),  #was 1000
                            (try_end),
                        (try_end),
                                
                        (try_for_agents,":agent"),
                            (neq,":chosen",":agent"), ## added this to avoid killing shooter
                            (neq, ":chosen_horse", ":agent"),
#                            (neg|agent_is_ally,":agent"), ## add this to avoid killing allies
                            (agent_is_alive,":agent"), ## add this to not re-kill dead people
                            (neg|agent_is_wounded,":agent"), ## add this to not re-kill wounded people

                            #partial friendly fire protection
                            (agent_get_team, ":agent_team_ff", ":agent"),
                            (assign, ":deliver_damage", 1),
                            (try_begin),
                            (neg|teams_are_enemies, ":chosen_team", ":agent_team_ff"),
                                (store_random_in_range, ":random", 1, 5),
                                (try_begin),
                                (gt, ":random", 1), # 3 in 4 chance that ally will not be hurt by damaging weave that is targeting enemy
                                    (assign, ":deliver_damage", 0),
                                (try_end),
                            (try_end),
                            (eq, ":deliver_damage", 1),
                            #end partial friendly fire protection
            
                            (agent_get_position,pos2,":agent"),
                            (get_distance_between_positions,":dist",pos3,pos2),
                         
                            # do 25 damage if fireball within 50 of agent
                            (try_begin),
                                (lt,":dist",50),  #was 300
                                (store_agent_hit_points,":target_health",":agent",1),
                                (try_begin),
                                    (gt,":target_health",25),
                                    (val_sub,":target_health",25),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 40),
                                    (try_end),
                                    (add_xp_to_troop,20,":chosen"),
                                    (agent_set_slot, ":agent", slot_agent_on_fire, 1),
                                    (agent_set_slot, ":agent", slot_agent_fire_starter, ":chosen"),
                                    (agent_set_slot, ":agent", slot_agent_fire_duration, 20),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 50),
                                    (try_end),
                                    (add_xp_to_troop,25,":chosen"),
                                    (position_get_z, ":z_temp", pos2),
                                    (val_add, ":z_temp", 300),
                                    (position_set_z, pos2, ":z_temp"),
                                    (particle_system_burst, "psys_torch_fire", pos2, 100),
                                (try_end),
                            # do 15 damage if fireball within 50 to 125 of agent
                            (else_try),
                                (is_between,":dist",50,125),  #was 300
                                (store_agent_hit_points,":target_health",":agent",1),
                                (try_begin),
                                    (gt,":target_health",15),
                                    (val_sub,":target_health",15),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 30),
                                    (try_end),
                                    (add_xp_to_troop,15,":chosen"),
                                    (agent_set_slot, ":agent", slot_agent_on_fire, 1),
                                    (agent_set_slot, ":agent", slot_agent_fire_starter, ":chosen"),
                                    (agent_set_slot, ":agent", slot_agent_fire_duration, 15),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 40),
                                    (try_end),
                                    (add_xp_to_troop,20,":chosen"),
                                    (position_get_z, ":z_temp", pos2),
                                    (val_add, ":z_temp", 300),
                                    (position_set_z, pos2, ":z_temp"),
                                    (particle_system_burst, "psys_torch_fire", pos2, 100),
                                (try_end),
                            # do 10 damage if fireball within 125 to 225 of agent
                            (else_try),
                                (is_between,":dist",125,225),  #was 300
                                (store_agent_hit_points,":target_health",":agent",1),
                                (try_begin),
                                    (gt,":target_health",10),
                                    (val_sub,":target_health",10),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 20),
                                    (try_end),
                                    (add_xp_to_troop,10,":chosen"),
                                    (agent_set_slot, ":agent", slot_agent_on_fire, 1),
                                    (agent_set_slot, ":agent", slot_agent_fire_starter, ":chosen"),
                                    (agent_set_slot, ":agent", slot_agent_fire_duration, 10),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 30),
                                    (try_end),
                                    (add_xp_to_troop,15,":chosen"),
                                    (position_get_z, ":z_temp", pos2),
                                    (val_add, ":z_temp", 300),
                                    (position_set_z, pos2, ":z_temp"),
                                    (particle_system_burst, "psys_torch_fire", pos2, 100),
                                (try_end),
                            # do 5 damage if fireball within 225 to 350 of agent
                            (else_try),
                                (is_between,":dist",225,350),  #was 300
                                (store_agent_hit_points,":target_health",":agent",1),
                                (try_begin),
                                    (gt,":target_health",5),
                                    (val_sub,":target_health",5),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 10),
                                    (try_end),
                                    (add_xp_to_troop,5,":chosen"),
                                    (agent_set_slot, ":agent", slot_agent_on_fire, 1),
                                    (agent_set_slot, ":agent", slot_agent_fire_starter, ":chosen"),
                                    (agent_set_slot, ":agent", slot_agent_fire_duration, 5),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 20),
                                    (try_end),
                                    (add_xp_to_troop,10,":chosen"),
                                    (position_get_z, ":z_temp", pos2),
                                    (val_add, ":z_temp", 300),
                                    (position_set_z, pos2, ":z_temp"),
                                    (particle_system_burst, "psys_torch_fire", pos2, 100),
                                (try_end),
                            (try_end),

                        (try_end),
                
                        #Fireball weave end


#########################################  Weave 5
                    (else_try),
                    (eq, ":active_weave", 4),
                        # Unravel Weave

                        (assign, ":chosen_active_effect", 0),
                        (assign, ":chosen_horse_on_fire", 0),
                        (assign, ":teammate_active_effect", 5),
                

                        (agent_get_slot, ":chosen_seeker", ":chosen", slot_agent_has_active_seeker),
                        (try_begin),
                        (eq, ":chosen_seeker", 1),
                            (assign, ":chosen_active_effect", 1),
                
                        (else_try), # chosen doesn't have a seeker
                            (agent_get_slot, ":chosen_fire", ":chosen", slot_agent_on_fire),
                            (try_begin),
                            (eq, ":chosen_fire", 1),
                                (assign, ":chosen_active_effect", 3),
                
                            (else_try), # chosen not on fire
                                (agent_get_slot, ":chosen_bound", ":chosen", slot_agent_is_bound),
                                (try_begin),
                                (eq, ":chosen_bound", 1),
                                    (assign, ":chosen_active_effect", 4),
                
                                (else_try), # chosen not bound
                                    (agent_get_horse, ":chosen_horse", ":chosen"),
                                    (try_begin),
                                    (ge, ":chosen_horse", 0),
                                        (agent_get_slot, ":chosen_horse_fire", ":chosen_horse", slot_agent_on_fire),
                                    (try_end),
                
                                    (try_begin),
                                    (eq, ":chosen_horse_fire", 1),
                                        (assign, ":chosen_horse_on_fire", 1),

                                    (else_try), # chosen horse not on fire
                                        
                                        (try_for_agents,":agent"),
                                            (agent_is_alive,":agent"), ## don't help dead
                                            (neg|agent_is_wounded,":agent"), ## don't help wounded
#                                            (agent_is_human,":agent"), ## don't help horses
                
                                            # determine if agents under compulsion used to be teammates
                                            (agent_get_slot, ":compulsion_present", ":agent", slot_agent_under_compulsion),
                                            (assign, ":agent_ally", 0),
                                            (try_begin),
                                            (eq, ":compulsion_present", 1),
                                                (agent_get_slot, ":original_team", ":agent", slot_agent_compelled_start_team),
                                                (agent_get_team, ":agent_team", ":agent"),
                                                (try_begin),
                                                (ge, ":original_team", 0),
                                                (neg|teams_are_enemies, ":original_team", ":chosen_team"), # used to be teammate
                                                    (assign, ":agent_ally", 2),
                                                (else_try),
                                                (neg|teams_are_enemies, ":chosen_team", ":agent_team"), # teammate by compulsion
                                                    (assign, ":agent_ally", 1),
                                                (try_end),
                                            (else_try),
                                            (agent_get_team, ":agent_team", ":agent"),
                                            (neg|teams_are_enemies, ":chosen_team", ":agent_team"), # always been teammate
                                                (assign, ":agent_ally", 1),
                                            (try_end),
                                                
                                            (gt, ":agent_ally", 0), ## don't help enemies
                                            (neq, ":chosen", ":agent"), ## this code will not look at 'chosen'
                
                                            (try_begin),
                                            (neq, ":teammate_active_effect", 1),
                                                (agent_get_slot, ":teammate_seeker", ":agent", slot_agent_has_active_seeker),
                                                (try_begin),
                                                (eq, ":teammate_seeker", 1),
                                                (eq, ":agent_ally", 1),
                                                    (assign, ":teammate_active_effect", 1),
                                                (else_try),
                                                (neq, ":teammate_active_effect", 2),
                                                    (agent_get_slot, ":teammate_compelled", ":agent", slot_agent_under_compulsion),
                                                    (try_begin),
                                                    (eq, ":teammate_compelled", 1),
                                                    (eq, ":agent_ally", 2),
                                                        (assign, ":teammate_active_effect", 2),
                                                    (else_try),
                                                    (neq, ":teammate_active_effect", 3),
                                                        (agent_get_slot, ":teammate_fire", ":agent", slot_agent_on_fire),
                                                        (try_begin),
                                                        (eq, ":teammate_fire", 1),
                                                        (eq, ":agent_ally", 1),
                                                            (assign, ":teammate_active_effect", 3),
                                                        (else_try),
                                                        (neq, ":teammate_active_effect", 4),
                                                            (agent_get_slot, ":teammate_bound", ":agent", slot_agent_is_bound),
                                                            (try_begin),
                                                            (eq, ":teammate_bound", 1),
                                                            (eq, ":agent_ally", 1), 
                                                                (assign, ":teammate_active_effect", 4),
                                                            (try_end),
                                                        (try_end),
                                                    (try_end),
                                                (try_end),
                                            (try_end),
                
                                        (try_end),

                                        (assign, ":distance", 99999),
                                
                                        (try_for_agents,":agent"),
                                            (agent_is_alive,":agent"), ## don't help dead
                                            (neg|agent_is_wounded,":agent"), ## don't help wounded
#                                            (agent_is_human,":agent"), ## don't help horses
                
                                            # determine if agents under compulsion used to be teammates
                                            (agent_get_slot, ":compulsion_present", ":agent", slot_agent_under_compulsion),
                                            (assign, ":agent_ally", 0),
                                            (try_begin),
                                            (eq, ":compulsion_present", 1),
                                                (agent_get_slot, ":original_team", ":agent", slot_agent_compelled_start_team),
                                                (agent_get_team, ":agent_team", ":agent"),
                                                (try_begin),
                                                (ge, ":original_team", 0),
                                                (neg|teams_are_enemies, ":original_team", ":chosen_team"), # used to be teammate
                                                    (assign, ":agent_ally", 2),
                                                (else_try),
                                                (neg|teams_are_enemies, ":chosen_team", ":agent_team"), # teammate by compulsion
                                                    (assign, ":agent_ally", 1),
                                                (try_end),
                                            (else_try),
                                            (agent_get_team, ":agent_team", ":agent"),
                                            (neg|teams_are_enemies, ":chosen_team", ":agent_team"), # always been teammate
                                                (assign, ":agent_ally", 1),
                                            (try_end),
                                                
                                            (gt, ":agent_ally", 0), ## don't help enemies
                                            (neq, ":chosen", ":agent"), ## this code will not look at 'chosen'

                                            (try_begin),
                                            (eq, ":teammate_active_effect", 1),
                                                (agent_get_slot, ":teammate_seeker", ":agent", slot_agent_has_active_seeker),
                                                (eq, ":teammate_seeker", 1),
                                                (eq, ":agent_ally", 1),
                                                    (agent_get_look_position, pos2, ":agent"),
                                                    (get_distance_between_positions,":dist",pos1,pos2),
                                                    (lt,":dist",":distance"),
                                                    (assign,":nearest_affected_ally",":agent"),
                                                    (assign,":distance",":dist"),
                                            (else_try),
                                            (eq, ":teammate_active_effect", 2),
                                                (agent_get_slot, ":teammate_compelled", ":agent", slot_agent_under_compulsion),
                                                (eq, ":teammate_compelled", 1),
                                                (eq, ":agent_ally", 2),
                                                    (agent_get_look_position, pos2, ":agent"),
                                                    (get_distance_between_positions,":dist",pos1,pos2),
                                                    (lt,":dist",":distance"),
                                                    (assign,":nearest_affected_ally",":agent"),
                                                    (assign,":distance",":dist"),
                                            (else_try),
                                            (eq, ":teammate_active_effect", 3),
                                                (agent_get_slot, ":teammate_fire", ":agent", slot_agent_on_fire),
                                                (eq, ":teammate_fire", 1),
                                                (eq, ":agent_ally", 1),
                                                    (agent_get_look_position, pos2, ":agent"),
                                                    (get_distance_between_positions,":dist",pos1,pos2),
                                                    (lt,":dist",":distance"),
                                                    (assign,":nearest_affected_ally",":agent"),
                                                    (assign,":distance",":dist"),
                                            (else_try),
                                            (eq, ":teammate_active_effect", 4),
                                                (agent_get_slot, ":teammate_bound", ":agent", slot_agent_is_bound),
                                                (eq, ":teammate_bound", 1),
                                                (eq, ":agent_ally", 1),
                                                    (agent_get_look_position, pos2, ":agent"),
                                                    (get_distance_between_positions,":dist",pos1,pos2),
                                                    (lt,":dist",":distance"),
                                                    (assign,":nearest_affected_ally",":agent"),
                                                    (assign,":distance",":dist"),
                                            (try_end),
                                        (try_end),
                                        # End of loops for finding closest affected ally
                                    (try_end),
                                    # End of loops for finding horse on fire
                
                                (try_end),
                            (try_end),
                        (try_end),
                        # End of if statements for does 'chosen' have active effects

                        (try_begin),
                        (gt, ":chosen_active_effect", 0), # chosen unraveling weave on self
                            (try_begin),
                            (eq, ":chosen_active_effect", 1),
                                (agent_get_slot, ":seeker_shooter", ":chosen", slot_agent_seeker_shooter),
                
                                (agent_get_troop_id, ":shooter_id", ":seeker_shooter"),
                                (troop_get_xp, ":shooter_xp", ":shooter_id"),
                                (agent_get_troop_id, ":chosen_id", ":chosen"),
                                (troop_get_xp, ":chosen_xp", ":chosen_id"),
                
                                (try_begin),
                                (gt, ":chosen_xp", ":shooter_xp"), # chosen more experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 25),
                                        (agent_set_slot, ":chosen", slot_agent_has_active_seeker, 0),
                                        (val_sub, "$g_number_seekers_active", 1),
                
                                        (try_begin),
                                        (eq, "$g_seeker_slot_1_target", ":chosen"),
                                            (assign, "$g_seeker_slot_1", 0),
                                            (copy_position, pos1, pos31),
                                        (else_try),
                                        (eq, "$g_seeker_slot_2_target", ":chosen"),
                                            (assign, "$g_seeker_slot_2", 0),
                                            (copy_position, pos1, pos32),
                                        (else_try),
                                        (eq, "$g_seeker_slot_3_target", ":chosen"),
                                            (assign, "$g_seeker_slot_3", 0),
                                            (copy_position, pos1, pos33),
                                        (else_try),
                                        (eq, "$g_seeker_slot_4_target", ":chosen"),
                                            (assign, "$g_seeker_slot_4", 0),
                                            (copy_position, pos1, pos34),
                                        (else_try),
                                        (eq, "$g_seeker_slot_5_target", ":chosen"),
                                            (assign, "$g_seeker_slot_5", 0),
                                            (copy_position, pos1, pos35),
                                        (else_try),
                                        (eq, "$g_seeker_slot_6_target", ":chosen"),
                                            (assign, "$g_seeker_slot_6", 0),
                                            (copy_position, pos1, pos36),
                                        (else_try),
                                        (eq, "$g_seeker_slot_7_target", ":chosen"),
                                            (assign, "$g_seeker_slot_7", 0),
                                            (copy_position, pos1, pos37),
                                        (else_try),
                                        (eq, "$g_seeker_slot_8_target", ":chosen"),
                                            (assign, "$g_seeker_slot_8", 0),
                                            (copy_position, pos1, pos38),
                                        (else_try),
                                        (eq, "$g_seeker_slot_9_target", ":chosen"),
                                            (assign, "$g_seeker_slot_9", 0),
                                            (copy_position, pos1, pos39),
                                        (else_try),
                                        (eq, "$g_seeker_slot_10_target", ":chosen"),
                                            (assign, "$g_seeker_slot_10", 0),
                                            (copy_position, pos1, pos40),
                                        (else_try),
                                        (eq, "$g_seeker_slot_11_target", ":chosen"),
                                            (assign, "$g_seeker_slot_11", 0),
                                            (copy_position, pos1, pos41),
                                        (else_try),
                                        (eq, "$g_seeker_slot_12_target", ":chosen"),
                                            (assign, "$g_seeker_slot_12", 0),
                                            (copy_position, pos1, pos42),
                                        (else_try),
                                        (eq, "$g_seeker_slot_13_target", ":chosen"),
                                            (assign, "$g_seeker_slot_13", 0),
                                            (copy_position, pos1, pos43),
                                        (else_try),
                                        (eq, "$g_seeker_slot_14_target", ":chosen"),
                                            (assign, "$g_seeker_slot_14", 0),
                                            (copy_position, pos1, pos44),
                                        (else_try),
                                        (eq, "$g_seeker_slot_15_target", ":chosen"),
                                            (assign, "$g_seeker_slot_15", 0),
                                            (copy_position, pos1, pos45),
                                        (else_try),
                                        (eq, "$g_seeker_slot_16_target", ":chosen"),
                                            (assign, "$g_seeker_slot_16", 0),
                                            (copy_position, pos1, pos46),
                                        (else_try),
                                        (eq, "$g_seeker_slot_17_target", ":chosen"),
                                            (assign, "$g_seeker_slot_17", 0),
                                            (copy_position, pos1, pos47),
                                        (else_try),
                                        (eq, "$g_seeker_slot_18_target", ":chosen"),
                                            (assign, "$g_seeker_slot_18", 0),
                                            (copy_position, pos1, pos48),
                                        (else_try),
                                        (eq, "$g_seeker_slot_19_target", ":chosen"),
                                            (assign, "$g_seeker_slot_19", 0),
                                            (copy_position, pos1, pos49),
                                        (else_try),
                                        (eq, "$g_seeker_slot_20_target", ":chosen"),
                                            (assign, "$g_seeker_slot_20", 0),
                                            (copy_position, pos1, pos50),
                                        (try_end),
                
                                        (particle_system_burst, "psys_unravel_aura", pos1, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 100),
                                        (try_end),
                                        (add_xp_to_troop,50,":chosen"),
                                (else_try), # chosen less experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 50),
                                        (agent_set_slot, ":chosen", slot_agent_has_active_seeker, 0),
                                        (val_sub, "$g_number_seekers_active", 1),
                
                                        (try_begin),
                                        (eq, "$g_seeker_slot_1_target", ":chosen"),
                                            (assign, "$g_seeker_slot_1", 0),
                                            (copy_position, pos1, pos31),
                                        (else_try),
                                        (eq, "$g_seeker_slot_2_target", ":chosen"),
                                            (assign, "$g_seeker_slot_2", 0),
                                            (copy_position, pos1, pos32),
                                        (else_try),
                                        (eq, "$g_seeker_slot_3_target", ":chosen"),
                                            (assign, "$g_seeker_slot_3", 0),
                                            (copy_position, pos1, pos33),
                                        (else_try),
                                        (eq, "$g_seeker_slot_4_target", ":chosen"),
                                            (assign, "$g_seeker_slot_4", 0),
                                            (copy_position, pos1, pos34),
                                        (else_try),
                                        (eq, "$g_seeker_slot_5_target", ":chosen"),
                                            (assign, "$g_seeker_slot_5", 0),
                                            (copy_position, pos1, pos35),
                                        (else_try),
                                        (eq, "$g_seeker_slot_6_target", ":chosen"),
                                            (assign, "$g_seeker_slot_6", 0),
                                            (copy_position, pos1, pos36),
                                        (else_try),
                                        (eq, "$g_seeker_slot_7_target", ":chosen"),
                                            (assign, "$g_seeker_slot_7", 0),
                                            (copy_position, pos1, pos37),
                                        (else_try),
                                        (eq, "$g_seeker_slot_8_target", ":chosen"),
                                            (assign, "$g_seeker_slot_8", 0),
                                            (copy_position, pos1, pos38),
                                        (else_try),
                                        (eq, "$g_seeker_slot_9_target", ":chosen"),
                                            (assign, "$g_seeker_slot_9", 0),
                                            (copy_position, pos1, pos39),
                                        (else_try),
                                        (eq, "$g_seeker_slot_10_target", ":chosen"),
                                            (assign, "$g_seeker_slot_10", 0),
                                            (copy_position, pos1, pos40),
                                        (else_try),
                                        (eq, "$g_seeker_slot_11_target", ":chosen"),
                                            (assign, "$g_seeker_slot_11", 0),
                                            (copy_position, pos1, pos41),
                                        (else_try),
                                        (eq, "$g_seeker_slot_12_target", ":chosen"),
                                            (assign, "$g_seeker_slot_12", 0),
                                            (copy_position, pos1, pos42),
                                        (else_try),
                                        (eq, "$g_seeker_slot_13_target", ":chosen"),
                                            (assign, "$g_seeker_slot_13", 0),
                                            (copy_position, pos1, pos43),
                                        (else_try),
                                        (eq, "$g_seeker_slot_14_target", ":chosen"),
                                            (assign, "$g_seeker_slot_14", 0),
                                            (copy_position, pos1, pos44),
                                        (else_try),
                                        (eq, "$g_seeker_slot_15_target", ":chosen"),
                                            (assign, "$g_seeker_slot_15", 0),
                                            (copy_position, pos1, pos45),
                                        (else_try),
                                        (eq, "$g_seeker_slot_16_target", ":chosen"),
                                            (assign, "$g_seeker_slot_16", 0),
                                            (copy_position, pos1, pos46),
                                        (else_try),
                                        (eq, "$g_seeker_slot_17_target", ":chosen"),
                                            (assign, "$g_seeker_slot_17", 0),
                                            (copy_position, pos1, pos47),
                                        (else_try),
                                        (eq, "$g_seeker_slot_18_target", ":chosen"),
                                            (assign, "$g_seeker_slot_18", 0),
                                            (copy_position, pos1, pos48),
                                        (else_try),
                                        (eq, "$g_seeker_slot_19_target", ":chosen"),
                                            (assign, "$g_seeker_slot_19", 0),
                                            (copy_position, pos1, pos49),
                                        (else_try),
                                        (eq, "$g_seeker_slot_20_target", ":chosen"),
                                            (assign, "$g_seeker_slot_20", 0),
                                            (copy_position, pos1, pos50),
                                        (try_end),

                                        (particle_system_burst, "psys_unravel_aura", pos1, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 150),
                                        (try_end),
                                        (add_xp_to_troop,75,":chosen"),
                                (try_end),
                            (else_try),
                            (eq, ":chosen_active_effect", 3),
                                (agent_get_slot, ":fire_shooter", ":chosen", slot_agent_fire_starter),
                
                                (agent_get_troop_id, ":shooter_id", ":fire_shooter"),
                                (troop_get_xp, ":shooter_xp", ":shooter_id"),
                                (agent_get_troop_id, ":chosen_id", ":chosen"),
                                (troop_get_xp, ":chosen_xp", ":chosen_id"),
                
                                (try_begin),
                                (gt, ":chosen_xp", ":shooter_xp"), # chosen more experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 25),
                                        (agent_set_slot, ":chosen", slot_agent_on_fire, 0),
                                        (particle_system_burst, "psys_unravel_aura", pos1, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 100),
                                        (try_end),
                                        (add_xp_to_troop,50,":chosen"),
                                (else_try), # chosen less experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 50),
                                        (agent_set_slot, ":chosen", slot_agent_on_fire, 0),
                                        (particle_system_burst, "psys_unravel_aura", pos1, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 150),
                                        (try_end),
                                        (add_xp_to_troop,75,":chosen"),
                                (try_end),
                            (else_try),
                            (eq, ":chosen_active_effect", 4),
                                (agent_get_slot, ":bind_shooter", ":chosen", slot_agent_bound_by),
                
                                (agent_get_troop_id, ":shooter_id", ":bind_shooter"),
                                (troop_get_xp, ":shooter_xp", ":shooter_id"),
                                (agent_get_troop_id, ":chosen_id", ":chosen"),
                                (troop_get_xp, ":chosen_xp", ":chosen_id"),
                
                                (try_begin),
                                (gt, ":chosen_xp", ":shooter_xp"), # chosen more experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 25),
                                        (agent_set_slot, ":chosen", slot_agent_is_bound, 0),
                                        (particle_system_burst, "psys_unravel_aura", pos1, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 100),
                                        (try_end),
                                        (add_xp_to_troop,50,":chosen"),
                                (else_try), # chosen less experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 50),
                                        (agent_set_slot, ":chosen", slot_agent_is_bound, 0),
                                        (particle_system_burst, "psys_unravel_aura", pos1, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 150),
                                        (try_end),
                                        (add_xp_to_troop,75,":chosen"),
                                (try_end),
                            (try_end),

                        (else_try), # chosen unraveling weave on horse
                        (eq, ":chosen_horse_on_fire", 1),
                            (agent_get_slot, ":fire_shooter", ":chosen_horse", slot_agent_fire_starter),

                            (agent_get_troop_id, ":shooter_id", ":fire_shooter"),
                            (troop_get_xp, ":shooter_xp", ":shooter_id"),
                            (agent_get_troop_id, ":chosen_id", ":chosen"),
                            (troop_get_xp, ":chosen_xp", ":chosen_id"),

                            (agent_get_position, pos2, ":chosen_horse"),
                
                            (try_begin),
                            (gt, ":chosen_xp", ":shooter_xp"), # chosen more experienced than shooter
                                (store_random_in_range, ":random", 1, 100),
                                (gt, ":random", 25),
                                    (agent_set_slot, ":chosen_horse", slot_agent_on_fire, 0),
                                    (particle_system_burst, "psys_unravel_aura", pos2, 50),
                                    (play_sound, "snd_unravel"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 100),
                                    (try_end),
                                    (add_xp_to_troop,50,":chosen"),
                            (else_try), # chosen less experienced than shooter
                                (store_random_in_range, ":random", 1, 100),
                                (gt, ":random", 50),
                                    (agent_set_slot, ":chosen_horse", slot_agent_on_fire, 0),
                                    (particle_system_burst, "psys_unravel_aura", pos2, 50),
                                    (play_sound, "snd_unravel"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 150),
                                    (try_end),
                                    (add_xp_to_troop,75,":chosen"),
                            (try_end),

                        (else_try),
                        (lt, ":teammate_active_effect", 5), # chosen unraveling weave on teammate
                            (try_begin),
                            (eq, ":teammate_active_effect", 1),
                                (agent_get_slot, ":seeker_shooter", ":nearest_affected_ally", slot_agent_seeker_shooter),
                
                                (agent_get_troop_id, ":shooter_id", ":seeker_shooter"),
                                (troop_get_xp, ":shooter_xp", ":shooter_id"),
                                (agent_get_troop_id, ":chosen_id", ":chosen"),
                                (troop_get_xp, ":chosen_xp", ":chosen_id"),

                                (agent_get_position, pos2, ":nearest_affected_ally"),
                
                                (try_begin),
                                (gt, ":chosen_xp", ":shooter_xp"), # chosen more experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 25),
                                        (agent_set_slot, ":nearest_affected_ally", slot_agent_has_active_seeker, 0),
                                        (val_sub, "$g_number_seekers_active", 1),
                
                                        (try_begin),
                                        (eq, "$g_seeker_slot_1_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_1", 0),
                                            (copy_position, pos1, pos31),
                                        (else_try),
                                        (eq, "$g_seeker_slot_2_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_2", 0),
                                            (copy_position, pos1, pos32),
                                        (else_try),
                                        (eq, "$g_seeker_slot_3_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_3", 0),
                                            (copy_position, pos1, pos33),
                                        (else_try),
                                        (eq, "$g_seeker_slot_4_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_4", 0),
                                            (copy_position, pos1, pos34),
                                        (else_try),
                                        (eq, "$g_seeker_slot_5_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_5", 0),
                                            (copy_position, pos1, pos35),
                                        (else_try),
                                        (eq, "$g_seeker_slot_6_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_6", 0),
                                            (copy_position, pos1, pos36),
                                        (else_try),
                                        (eq, "$g_seeker_slot_7_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_7", 0),
                                            (copy_position, pos1, pos37),
                                        (else_try),
                                        (eq, "$g_seeker_slot_8_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_8", 0),
                                            (copy_position, pos1, pos38),
                                        (else_try),
                                        (eq, "$g_seeker_slot_9_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_9", 0),
                                            (copy_position, pos1, pos39),
                                        (else_try),
                                        (eq, "$g_seeker_slot_10_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_10", 0),
                                            (copy_position, pos1, pos40),
                                        (else_try),
                                        (eq, "$g_seeker_slot_11_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_11", 0),
                                            (copy_position, pos1, pos41),
                                        (else_try),
                                        (eq, "$g_seeker_slot_12_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_12", 0),
                                            (copy_position, pos1, pos42),
                                        (else_try),
                                        (eq, "$g_seeker_slot_13_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_13", 0),
                                            (copy_position, pos1, pos43),
                                        (else_try),
                                        (eq, "$g_seeker_slot_14_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_14", 0),
                                            (copy_position, pos1, pos44),
                                        (else_try),
                                        (eq, "$g_seeker_slot_15_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_15", 0),
                                            (copy_position, pos1, pos45),
                                        (else_try),
                                        (eq, "$g_seeker_slot_16_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_16", 0),
                                            (copy_position, pos1, pos46),
                                        (else_try),
                                        (eq, "$g_seeker_slot_17_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_17", 0),
                                            (copy_position, pos1, pos47),
                                        (else_try),
                                        (eq, "$g_seeker_slot_18_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_18", 0),
                                            (copy_position, pos1, pos48),
                                        (else_try),
                                        (eq, "$g_seeker_slot_19_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_19", 0),
                                            (copy_position, pos1, pos49),
                                        (else_try),
                                        (eq, "$g_seeker_slot_20_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_20", 0),
                                            (copy_position, pos1, pos50),
                                        (try_end),
                
                                        (particle_system_burst, "psys_unravel_aura", pos1, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 100),
                                        (try_end),
                                        (add_xp_to_troop,50,":chosen"),
                                (else_try), # chosen less experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 50),
                                        (agent_set_slot, ":nearest_affected_ally", slot_agent_has_active_seeker, 0),
                                        (val_sub, "$g_number_seekers_active", 1),
                
                                        (try_begin),
                                        (eq, "$g_seeker_slot_1_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_1", 0),
                                            (copy_position, pos1, pos31),
                                        (else_try),
                                        (eq, "$g_seeker_slot_2_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_2", 0),
                                            (copy_position, pos1, pos32),
                                        (else_try),
                                        (eq, "$g_seeker_slot_3_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_3", 0),
                                            (copy_position, pos1, pos33),
                                        (else_try),
                                        (eq, "$g_seeker_slot_4_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_4", 0),
                                            (copy_position, pos1, pos34),
                                        (else_try),
                                        (eq, "$g_seeker_slot_5_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_5", 0),
                                            (copy_position, pos1, pos35),
                                        (else_try),
                                        (eq, "$g_seeker_slot_6_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_6", 0),
                                            (copy_position, pos1, pos36),
                                        (else_try),
                                        (eq, "$g_seeker_slot_7_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_7", 0),
                                            (copy_position, pos1, pos37),
                                        (else_try),
                                        (eq, "$g_seeker_slot_8_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_8", 0),
                                            (copy_position, pos1, pos38),
                                        (else_try),
                                        (eq, "$g_seeker_slot_9_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_9", 0),
                                            (copy_position, pos1, pos39),
                                        (else_try),
                                        (eq, "$g_seeker_slot_10_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_10", 0),
                                            (copy_position, pos1, pos40),
                                        (else_try),
                                        (eq, "$g_seeker_slot_11_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_11", 0),
                                            (copy_position, pos1, pos41),
                                        (else_try),
                                        (eq, "$g_seeker_slot_12_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_12", 0),
                                            (copy_position, pos1, pos42),
                                        (else_try),
                                        (eq, "$g_seeker_slot_13_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_13", 0),
                                            (copy_position, pos1, pos43),
                                        (else_try),
                                        (eq, "$g_seeker_slot_14_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_14", 0),
                                            (copy_position, pos1, pos44),
                                        (else_try),
                                        (eq, "$g_seeker_slot_15_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_15", 0),
                                            (copy_position, pos1, pos45),
                                        (else_try),
                                        (eq, "$g_seeker_slot_16_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_16", 0),
                                            (copy_position, pos1, pos46),
                                        (else_try),
                                        (eq, "$g_seeker_slot_17_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_17", 0),
                                            (copy_position, pos1, pos47),
                                        (else_try),
                                        (eq, "$g_seeker_slot_18_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_18", 0),
                                            (copy_position, pos1, pos48),
                                        (else_try),
                                        (eq, "$g_seeker_slot_19_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_19", 0),
                                            (copy_position, pos1, pos49),
                                        (else_try),
                                        (eq, "$g_seeker_slot_20_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_20", 0),
                                            (copy_position, pos1, pos50),
                                        (try_end),
                
                                        (particle_system_burst, "psys_unravel_aura", pos1, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 150),
                                        (try_end),
                                        (add_xp_to_troop,75,":chosen"),
                                (try_end),
                            (else_try),
                            (eq, ":teammate_active_effect", 2),
                                (agent_get_slot, ":compulsion_shooter", ":nearest_affected_ally", slot_agent_compelled_by),
                
                                (agent_get_troop_id, ":shooter_id", ":compulsion_shooter"),
                                (troop_get_xp, ":shooter_xp", ":shooter_id"),
                                (agent_get_troop_id, ":chosen_id", ":chosen"),
                                (troop_get_xp, ":chosen_xp", ":chosen_id"),

                                (agent_get_position, pos2, ":nearest_affected_ally"),
                
                                (try_begin),
                                (gt, ":chosen_xp", ":shooter_xp"), # chosen more experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 25),
                                        (agent_get_slot, ":start_team", ":nearest_affected_ally", slot_agent_compelled_start_team),
                                        (agent_set_team, ":nearest_affected_ally", ":start_team"),
                                        (agent_set_slot, ":nearest_affected_ally", slot_agent_under_compulsion, 0),
                                        (particle_system_burst, "psys_unravel_aura", pos2, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 100),
                                        (try_end),
                                        (add_xp_to_troop,50,":chosen"),
                                (else_try), # chosen less experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 50),
                                        (agent_get_slot, ":start_team", ":nearest_affected_ally", slot_agent_compelled_start_team),
                                        (agent_set_team, ":nearest_affected_ally", ":start_team"),
                                        (agent_set_slot, ":nearest_affected_ally", slot_agent_under_compulsion, 0),
                                        (particle_system_burst, "psys_unravel_aura", pos2, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 150),
                                        (try_end),
                                        (add_xp_to_troop,75,":chosen"),
                                (try_end),
                            (else_try),
                            (eq, ":teammate_active_effect", 3),
                                (agent_get_slot, ":fire_shooter", ":nearest_affected_ally", slot_agent_fire_starter),
                
                                (agent_get_troop_id, ":shooter_id", ":fire_shooter"),
                                (troop_get_xp, ":shooter_xp", ":shooter_id"),
                                (agent_get_troop_id, ":chosen_id", ":chosen"),
                                (troop_get_xp, ":chosen_xp", ":chosen_id"),

                                (agent_get_position, pos2, ":nearest_affected_ally"),
                
                                (try_begin),
                                (gt, ":chosen_xp", ":shooter_xp"), # chosen more experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 25),
                                        (agent_set_slot, ":nearest_affected_ally", slot_agent_on_fire, 0),
                                        (particle_system_burst, "psys_unravel_aura", pos2, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 100),
                                        (try_end),
                                        (add_xp_to_troop,50,":chosen"),
                                (else_try), # chosen less experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 50),
                                        (agent_set_slot, ":nearest_affected_ally", slot_agent_on_fire, 0),
                                        (particle_system_burst, "psys_unravel_aura", pos2, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 150),
                                        (try_end),
                                        (add_xp_to_troop,75,":chosen"),
                                (try_end),
                            (else_try),
                            (eq, ":teammate_active_effect", 4),
                                (agent_get_slot, ":bind_shooter", ":nearest_affected_ally", slot_agent_bound_by),
                
                                (agent_get_troop_id, ":shooter_id", ":bind_shooter"),
                                (troop_get_xp, ":shooter_xp", ":shooter_id"),
                                (agent_get_troop_id, ":chosen_id", ":chosen"),
                                (troop_get_xp, ":chosen_xp", ":chosen_id"),

                                (agent_get_position, pos2, ":nearest_affected_ally"),
                
                                (try_begin),
                                (gt, ":chosen_xp", ":shooter_xp"), # chosen more experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 25),
                                        (agent_set_slot, ":nearest_affected_ally", slot_agent_is_bound, 0),
                                        (particle_system_burst, "psys_unravel_aura", pos2, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 100),
                                        (try_end),
                                        (add_xp_to_troop,50,":chosen"),
                                (else_try), # chosen less experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 50),
                                        (agent_set_slot, ":nearest_affected_ally", slot_agent_is_bound, 0),
                                        (particle_system_burst, "psys_unravel_aura", pos2, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 150),
                                        (try_end),
                                        (add_xp_to_troop,75,":chosen"),
                                (try_end),
                            (try_end),
                        (else_try),
                        (neg|agent_is_non_player, ":chosen"),
                            (display_message, "@No active weaves to unravel..."),
                        (try_end),
                        
                    # End Unravel Weave


################################## Weave 7
                    (else_try),
                    (eq, ":active_weave", 5),
                         # Ranged Earth Blast

                        (assign, ":times_near_ground", 0),
                        (assign, ":near_enemy", 0),

                        (try_for_range,reg5,1,500),  ###was 500
                        (eq, ":times_near_ground", 0),
                            (particle_system_burst, "psys_dust_blast", pos1, 10),
                            (position_move_y,pos1,30),

                            #added for gravity effect and flight randomness
                            (store_mod, ":fall", reg5, 2),
                            (try_begin),
                            (eq, ":fall", 0),
                                (position_move_x,pos1,3),
                            (try_end),

                            (store_mod, ":weave", reg5, 5),
                            (try_begin),
                            (eq, ":weave", 0),
                                (store_random_in_range, ":random", -7, 8),
                                (position_move_z,pos1,":random"),
                            (try_end),
                            #end added for gravity effect and flight randomness
            
                            (copy_position,pos2,pos1),
                            (position_set_z_to_ground_level, pos2),
                            (get_distance_between_positions,":dist",pos1,pos2),

                            (position_get_z, ":z_ground", pos2),
                            (store_add, ":z_ground_low", ":z_ground", 200),
                            (store_add, ":z_ground_high", ":z_ground", 2000),

                            (try_for_agents, ":agent"),
                            (eq, ":near_enemy", 0),
                                (neq, ":chosen", ":agent"),
                                (neq, ":chosen_horse", ":agent"),
                                (agent_get_team, ":agent_team", ":agent"),
                                (teams_are_enemies, ":chosen_team", ":agent_team"),
                                (agent_is_alive, ":agent"),
                                (neg|agent_is_wounded, ":agent"),
                                (agent_get_look_position, pos4, ":agent"),
                                (get_distance_between_positions, ":dist_2", pos2, pos4),
                                (position_get_z, ":z_attack_trail", pos1),
                                (lt, ":dist_2", 50), # near agent (x-y)
                                (is_between, ":z_attack_trail", ":z_ground_low", ":z_ground_high"), # within the agent's body (z height)
                                (assign, ":dist", 5),
                                (assign, ":near_enemy", 1),
                            (try_end),
                    
                            (try_begin),
                            (lt,":dist",10),
                                (val_add, ":times_near_ground", 1),
                                (particle_system_burst, "psys_earthquake", pos1, 25),  # effect needs a long duration
                                (play_sound,"snd_explosion"),
                                (copy_position, pos3, pos1),
                                (scene_prop_get_instance,":instance", "spr_snowy_heap_a", 0),  #need
                                (position_copy_origin,pos2,pos1),
                                (prop_instance_set_position,":instance",pos2),
                                (assign,reg5,1000),  #was 1000
                            (try_end),
                        (try_end),
                    
                        (try_for_agents,":agent"),
                            (neq,":chosen",":agent"), ## added this to avoid affecting shooter
                            (neq, ":chosen_horse", ":agent"),
#                            (neg|agent_is_ally,":agent"), ## add this to avoid hurting allies
                            (agent_is_alive,":agent"), ## add this to not affect dead people
                            (neg|agent_is_wounded,":agent"), ## add this to not affect wounded people

                            #partial friendly fire protection
                            (agent_get_team, ":agent_team_ff", ":agent"),
                            (assign, ":deliver_damage", 1),
                            (try_begin),
                            (neg|teams_are_enemies, ":chosen_team", ":agent_team_ff"),
                                (store_random_in_range, ":random", 1, 5),
                                (try_begin),
                                (gt, ":random", 1), # 3 in 4 chance that ally will not be hurt by damaging weave that is targeting enemy
                                    (assign, ":deliver_damage", 0),
                                (try_end),
                            (try_end),
                            (eq, ":deliver_damage", 1),
                            #end partial friendly fire protection
            
                            (agent_get_position,pos2,":agent"),
                            (get_distance_between_positions,":dist",pos3,pos2),
                            (store_agent_hit_points,":target_health",":agent",1),
                    
                            (try_begin),
                            (lt,":dist",750),

#                                (agent_set_slot, ":agent", slot_agent_is_airborne, 1),

                                (position_get_x, ":attacker_x", pos1),
                                (position_get_y, ":attacker_y", pos1),
                                (position_get_x, ":target_x", pos2),
                                (position_get_y, ":target_y", pos2),

                                (store_sub, ":run", ":target_x", ":attacker_x"),
                                (store_sub, ":rise", ":target_y", ":attacker_y"),

                                (agent_set_slot, ":agent", slot_agent_airborne_x_movement, ":run"),
                                (agent_set_slot, ":agent", slot_agent_airborne_y_movement, ":rise"),

                                (get_distance_between_positions, ":dist_from_chosen", pos1, pos2),
                                (try_begin),
                                (lt, ":dist_from_chosen", 100),
                                    (agent_set_slot, ":agent", slot_agent_airborne_power_factor, 20),
                                (else_try),
                                (is_between, ":dist_from_chosen", 100, 250),
                                    (agent_set_slot, ":agent", slot_agent_airborne_power_factor, 15),
                                (else_try),
                                (is_between, ":dist_from_chosen", 250, 450),
                                    (agent_set_slot, ":agent", slot_agent_airborne_power_factor, 10),
                                (else_try),
                                (is_between, ":dist_from_chosen", 450, 750),
                                    (agent_set_slot, ":agent", slot_agent_airborne_power_factor, 5),
                                (try_end),
                            (try_end),

                            (try_begin),
                            (lt, ":dist", 100),
                                (try_begin),
                                    (gt,":target_health",15),
                                    (val_sub,":target_health",15),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 20),
                                    (try_end),
                                    (add_xp_to_troop,10,":chosen"),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 30),
                                    (try_end),
                                    (add_xp_to_troop,15,":chosen"),
                                (try_end),
                            (else_try),
                            (is_between,":dist",100,250),
                                (try_begin),
                                    (gt,":target_health",10),
                                    (val_sub,":target_health",10),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 10),
                                    (try_end),
                                    (add_xp_to_troop,5,":chosen"),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 20),
                                    (try_end),
                                    (add_xp_to_troop,10,":chosen"),
                                (try_end),
                            (else_try),
                            (is_between,":dist",250,450),
                                (try_begin),
                                    (gt,":target_health",6),
                                    (val_sub,":target_health",6),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 10),
                                    (try_end),
                                    (add_xp_to_troop,5,":chosen"),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 20),
                                    (try_end),
                                    (add_xp_to_troop,10,":chosen"),
                                (try_end),
                            (else_try),
                            (is_between,":dist",450,750),
                                (try_begin),
                                    (gt,":target_health",3),
                                    (val_sub,":target_health",3),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 10),
                                    (try_end),
                                    (add_xp_to_troop,5,":chosen"),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 20),
                                    (try_end),
                                    (add_xp_to_troop,10,":chosen"),
                                (try_end),
                            (try_end),
                        (try_end),
                                                
                        #End Ranged Earth Blast


#########################################  Weave 8
                    (else_try),
                    (eq, ":active_weave", 6),
                        # Bind Weave (attempt to bind nearest enemy)

                        (assign, ":distance",99999),
                        (assign, ":number_of_enemies", 0),

                        (try_for_agents,":agent"),
                            (agent_is_alive,":agent"), ## don't bind dead
                            (neg|agent_is_wounded,":agent"), ## don't bind wounded
                            (agent_is_human,":agent"), ## don't bind horses
                            (agent_get_team, ":agent_team", ":agent"),
                            (teams_are_enemies, ":chosen_team", ":agent_team"), ## don't bind enemies
                            (neq, ":chosen", ":agent"), ## shooter can't bind self
                            (agent_get_slot, ":already_bound", ":agent", slot_agent_is_bound),
                            (eq, ":already_bound", 0),
                            (agent_get_look_position, pos2, ":agent"),
                            (get_distance_between_positions,":dist",pos1,pos2),
                            (lt,":dist",":distance"),
                            (assign,":target",":agent"),
                            (assign,":distance",":dist"),
                            (val_add, ":number_of_enemies", 1),
                        (try_end),

                        (try_begin),
                        (ge, ":number_of_enemies", 1),
                            (agent_get_slot, ":target_is_channeler", ":target", slot_agent_is_channeler),
                            (agent_get_slot, ":target_is_shielded", ":target", slot_agent_is_shielded),
                    
                            (try_begin),
                            (eq, ":target_is_channeler", 1),  # harder to bind channelers
                            (eq, ":target_is_shielded", 0),  # unless they are shielded
                                (agent_get_troop_id, ":target_id", ":target"),
                                (troop_get_xp, ":target_xp", ":target_id"),
                                (agent_get_troop_id, ":chosen_id", ":chosen"),
                                (troop_get_xp, ":chosen_xp", ":chosen_id"),
                    
                                (try_begin),
                                (gt, ":chosen_xp", ":target_xp"),
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 25),
                                        (agent_get_look_position, pos3, ":target"),
                                        (position_get_x, ":target_x", pos3),
                                        (position_get_y, ":target_y", pos3),
                                        # set slots
                                        (agent_set_slot, ":target", slot_agent_is_bound, 1),
                                        (agent_set_slot, ":target", slot_agent_bound_by, ":chosen"),
                                        (agent_set_slot, ":target", slot_agent_bound_x, ":target_x"),
                                        (agent_set_slot, ":target", slot_agent_bound_y, ":target_y"),
                                        (agent_set_slot, ":target", slot_agent_bound_duration, 10),

                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 60),
                                        (try_end),
                                        (add_xp_to_troop,30,":chosen"),
                                (else_try),
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 75),
                                        (agent_get_look_position, pos3, ":target"),
                                        (position_get_x, ":target_x", pos3),
                                        (position_get_y, ":target_y", pos3),
                                        # set slots
                                        (agent_set_slot, ":target", slot_agent_is_bound, 1),
                                        (agent_set_slot, ":target", slot_agent_bound_by, ":chosen"),
                                        (agent_set_slot, ":target", slot_agent_bound_x, ":target_x"),
                                        (agent_set_slot, ":target", slot_agent_bound_y, ":target_y"),
                                        (agent_set_slot, ":target", slot_agent_bound_duration, 10),

                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 120),
                                        (try_end),
                                        (add_xp_to_troop,60,":chosen"),
                                (try_end),
                    
                            (else_try),
                                (agent_get_look_position, pos3, ":target"),
                                (position_get_x, ":target_x", pos3),
                                (position_get_y, ":target_y", pos3),
                                # set slots
                                (agent_set_slot, ":target", slot_agent_is_bound, 1),
                                (agent_set_slot, ":target", slot_agent_bound_by, ":chosen"),
                                (agent_set_slot, ":target", slot_agent_bound_x, ":target_x"),
                                (agent_set_slot, ":target", slot_agent_bound_y, ":target_y"),
                                (agent_set_slot, ":target", slot_agent_bound_duration, 10),

                                (try_begin), # add to channeling multiplier if agent is player
                                (neg|agent_is_non_player, ":chosen"),
                                    (val_add, "$g_channeling_proficiency_modifier", 30),
                                (try_end),
                                (add_xp_to_troop,15,":chosen"),
                            (try_end),

                            (play_sound, "snd_man_grunt_long"),
                        (try_end),

                    # End Bind Weave


################################## Weave 9
                    (else_try),
                    (eq, ":active_weave", 7),
                         #Chain Lightning Weave

                        (assign, ":victim_1", 0),
                        (assign, ":victim_2", 0),
                        (assign, ":victim_3", 0),
                        (assign, ":victim_4", 0),
                        (assign, ":victim_5", 0),
                        (assign, ":victim_6", 0),
                        (assign, ":victim_7", 0),
                        (assign, ":victim_8", 0),

                        (assign, ":times_near_ground", 0),
                        (assign, ":near_enemy", 0),

                        (try_for_range,reg5,1,500),  ###was 500
                        (eq, ":times_near_ground", 0),
                            (particle_system_burst, "psys_electricity_blast", pos1, 10),
                            (position_move_y,pos1,30),

                            #added for gravity effect and flight randomness
                            (store_mod, ":fall", reg5, 2),
                            (try_begin),
                            (eq, ":fall", 0),
                                (position_move_x,pos1,3),
                            (try_end),

                            (store_mod, ":weave", reg5, 5),
                            (try_begin),
                            (eq, ":weave", 0),
                                (store_random_in_range, ":random", -7, 8),
                                (position_move_z,pos1,":random"),
                            (try_end),
                            #end added for gravity effect and flight randomness
            
                            (copy_position,pos2,pos1),
                            (position_set_z_to_ground_level, pos2),
                            (get_distance_between_positions,":dist",pos1,pos2),

                            (position_get_z, ":z_ground", pos2),
                            (store_add, ":z_ground_low", ":z_ground", 200),
                            (store_add, ":z_ground_high", ":z_ground", 2000),

                            (try_for_agents, ":agent"),
                            (eq, ":near_enemy", 0),
                                (neq, ":chosen", ":agent"),
                                (neq, ":chosen_horse", ":agent"),
                                (agent_get_team, ":agent_team", ":agent"),
                                (teams_are_enemies, ":chosen_team", ":agent_team"),
                                (agent_is_alive, ":agent"),
                                (neg|agent_is_wounded, ":agent"),
                                (agent_get_look_position, pos4, ":agent"),
                                (get_distance_between_positions, ":dist_2", pos2, pos4),
                                (position_get_z, ":z_attack_trail", pos1),
                                (lt, ":dist_2", 50), # near agent (x-y)
                                (is_between, ":z_attack_trail", ":z_ground_low", ":z_ground_high"), # within the agent's body (z height)
                                (assign, ":dist", 5),
                                (assign, ":near_enemy", 1),
                            (try_end),
                    
                            (try_begin),
                            (lt,":dist",10),
                                (val_add, ":times_near_ground", 1),
                                (particle_system_burst, "psys_electricity_sparks", pos1, 25),
                                (play_sound,"snd_chain_lightning"), # need a sound for freeze
                                (copy_position, pos3, pos1),
                                (scene_prop_get_instance,":instance", "spr_snowy_heap_a", 0),  #need
                                (position_copy_origin,pos2,pos1),
                                (prop_instance_set_position,":instance",pos2),
                                (assign,reg5,1000),  #was 1000
                            (try_end),
                        (try_end),

                        (try_for_range, ":counter", 1, 8),
                            (assign, ":distance", 99999),
                            (assign, ":number_near_blast", 0),
                        ## Look for agents near initial strike zone
                            (try_for_agents,":agent"),
                                (neq,":chosen",":agent"), ## added this to avoid shocking shooter
                                (neq, ":chosen_horse", ":agent"),
#                                (neg|agent_is_ally,":agent"), ## add this to avoid shocking allies
                                (agent_is_alive,":agent"), ## add this to not shock dead people
                                (neg|agent_is_wounded,":agent"), ## add this to not shock wounded people
                                (agent_get_slot, ":already_shocked", ":agent", slot_agent_has_been_shocked),
                                (eq, ":already_shocked", 0),

                                #partial friendly fire protection
                                (agent_get_team, ":agent_team_ff", ":agent"),
                                (assign, ":deliver_damage", 1),
                                (try_begin),
                                (neg|teams_are_enemies, ":chosen_team", ":agent_team_ff"),
                                    (store_random_in_range, ":random", 1, 5),
                                    (try_begin),
                                    (gt, ":random", 1), # 3 in 4 chance that ally will not be hurt by damaging weave that is targeting enemy
                                        (assign, ":deliver_damage", 0),
                                    (try_end),
                                (try_end),
                                (eq, ":deliver_damage", 1),
                                #end partial friendly fire protection
            
                                (agent_get_position,pos2,":agent"),
                                (get_distance_between_positions,":dist",pos3,pos2),
                                (lt,":dist",":distance"),
                                    (assign,":agent_closest_to_blast",":agent"),
                                    (assign,":distance",":dist"),
                                    (val_add, ":number_near_blast", 1),
                            (try_end),

                            (try_begin), # apply charge if agent close enough
                            (ge, ":number_near_blast", 1),
                            (lt, ":dist", 1500),
                                (store_agent_hit_points,":target_health",":agent_closest_to_blast",1),

                                (try_begin),
                                (is_between, ":counter", 1, 3),
                                    (try_begin),
                                    (gt, ":target_health", 15),
                                        (val_sub,":target_health",15),
                                        (agent_set_hit_points,":agent_closest_to_blast",":target_health",1),
                                        (agent_deliver_damage_to_agent,":chosen",":agent_closest_to_blast"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 30),
                                        (try_end),
                                        (add_xp_to_troop,15,":chosen"),
                                    (else_try),
                                        (agent_set_hit_points,":agent_closest_to_blast",0,0),
                                        (agent_deliver_damage_to_agent,":chosen",":agent_closest_to_blast"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 60),
                                        (try_end),
                                        (add_xp_to_troop,30,":chosen"),
                                    (try_end),
                                (else_try),
                                (is_between, ":counter", 3, 5),
                                    (try_begin),
                                    (gt, ":target_health", 12),
                                        (val_sub,":target_health",12),
                                        (agent_set_hit_points,":agent_closest_to_blast",":target_health",1),
                                        (agent_deliver_damage_to_agent,":chosen",":agent_closest_to_blast"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 30),
                                        (try_end),
                                        (add_xp_to_troop,15,":chosen"),
                                    (else_try),
                                        (agent_set_hit_points,":agent_closest_to_blast",0,0),
                                        (agent_deliver_damage_to_agent,":chosen",":agent_closest_to_blast"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 60),
                                        (try_end),
                                        (add_xp_to_troop,30,":chosen"),
                                    (try_end),
                                (else_try),
                                (is_between, ":counter", 5, 7),
                                    (try_begin),
                                    (gt, ":target_health", 9),
                                        (val_sub,":target_health",9),
                                        (agent_set_hit_points,":agent_closest_to_blast",":target_health",1),
                                        (agent_deliver_damage_to_agent,":chosen",":agent_closest_to_blast"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 30),
                                        (try_end),
                                        (add_xp_to_troop,15,":chosen"),
                                    (else_try),
                                        (agent_set_hit_points,":agent_closest_to_blast",0,0),
                                        (agent_deliver_damage_to_agent,":chosen",":agent_closest_to_blast"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 60),
                                        (try_end),
                                        (add_xp_to_troop,30,":chosen"),
                                    (try_end),
                                (else_try),
                                (is_between, ":counter", 7, 9),
                                    (try_begin),
                                    (gt, ":target_health", 6),
                                        (val_sub,":target_health",6),
                                        (agent_set_hit_points,":agent_closest_to_blast",":target_health",1),
                                        (agent_deliver_damage_to_agent,":chosen",":agent_closest_to_blast"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 30),
                                        (try_end),
                                        (add_xp_to_troop,15,":chosen"),
                                    (else_try),
                                        (agent_set_hit_points,":agent_closest_to_blast",0,0),
                                        (agent_deliver_damage_to_agent,":chosen",":agent_closest_to_blast"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 60),
                                        (try_end),
                                        (add_xp_to_troop,30,":chosen"),
                                    (try_end),
                                (try_end),
                    

                                # set victim slots
                                (agent_set_slot, ":agent_closest_to_blast", slot_agent_has_been_shocked, 1),

                                (try_begin),
                                (eq, ":counter", 1),
                                    (assign, ":victim_1", ":agent_closest_to_blast"),
                                (else_try),
                                (eq, ":counter", 2),
                                    (assign, ":victim_2", ":agent_closest_to_blast"),
                                (else_try),
                                (eq, ":counter", 3),
                                    (assign, ":victim_3", ":agent_closest_to_blast"),
                                (else_try),
                                (eq, ":counter", 4),
                                    (assign, ":victim_4", ":agent_closest_to_blast"),
                                (else_try),
                                (eq, ":counter", 5),
                                    (assign, ":victim_5", ":agent_closest_to_blast"),
                                (else_try),
                                (eq, ":counter", 6),
                                    (assign, ":victim_6", ":agent_closest_to_blast"),
                                (else_try),
                                (eq, ":counter", 7),
                                    (assign, ":victim_7", ":agent_closest_to_blast"),
                                (else_try),
                                (eq, ":counter", 8),
                                    (assign, ":victim_8", ":agent_closest_to_blast"),
                                (end_try),

                                # calculate blast travel
                                (agent_get_position, pos2, ":agent_closest_to_blast"),
                                (position_get_x, ":x_end", pos2),
                                (position_get_y, ":y_end", pos2),
                                (position_get_z, ":z_end", pos2),
                                (val_add, ":z_end", 1250),

                                (position_get_x, ":x_start", pos3),
                                (position_get_y, ":y_start", pos3),
                                (position_get_z, ":z_start", pos3),
                    
                                (try_begin),
                                (gt, ":counter", 1),
                                    (val_add, ":z_start", 1250),
                                (try_end),

                                (store_sub, ":run", ":x_end", ":x_start"),
                                (store_sub, ":rise", ":y_end", ":y_start"),
                                (store_sub, ":vert", ":z_end", ":z_start"),

                                (assign, ":interval", 60),

                                (val_div, ":run", ":interval"),
                                (val_div, ":rise", ":interval"),
                                (val_div, ":vert", ":interval"),

                                (try_for_range, ":unused", 0, ":interval"),
                                    (val_add, ":x_start", ":run"),
                                    (val_add, ":y_start", ":rise"),
                                    (val_add, ":z_start", ":vert"),

                                    (position_set_x, pos3, ":x_start"),
                                    (position_set_y, pos3, ":y_start"),
                                    (position_set_z, pos3, ":z_start"),

                                    (particle_system_burst, "psys_electricity_blast", pos3, 10),
                                (try_end),
                    
                                (particle_system_burst, "psys_electricity_sparks", pos2, 25),

                                (copy_position, pos3, pos2),
                    
                            (try_end),

                        # reset victim slots
                        (try_end),

                        (try_begin),
                        (neq, ":victim_1", 0),
                            (agent_set_slot, ":victim_1", slot_agent_has_been_shocked, 0),
                        (try_end),

                        (try_begin),
                        (neq, ":victim_2", 0),
                            (agent_set_slot, ":victim_2", slot_agent_has_been_shocked, 0),
                        (try_end),

                        (try_begin),
                        (neq, ":victim_3", 0),
                            (agent_set_slot, ":victim_3", slot_agent_has_been_shocked, 0),
                        (try_end),

                        (try_begin),
                        (neq, ":victim_4", 0),
                            (agent_set_slot, ":victim_4", slot_agent_has_been_shocked, 0),
                        (try_end),

                        (try_begin),
                        (neq, ":victim_5", 0),
                            (agent_set_slot, ":victim_5", slot_agent_has_been_shocked, 0),
                        (try_end),

                        (try_begin),
                        (neq, ":victim_6", 0),
                            (agent_set_slot, ":victim_6", slot_agent_has_been_shocked, 0),
                        (try_end),

                        (try_begin),
                        (neq, ":victim_7", 0),
                            (agent_set_slot, ":victim_7", slot_agent_has_been_shocked, 0),
                        (try_end),

                        (try_begin),
                        (neq, ":victim_8", 0),
                            (agent_set_slot, ":victim_8", slot_agent_has_been_shocked, 0),
                        (try_end),
                    
                        #Chain Lightening end


#########################################  Weave 11
                    (else_try),
                    (eq, ":active_weave", 8),
                        # Shield Weave (attempt to shield nearest enemy channeler)

                        (assign, ":distance",99999),
                        (assign, ":number_of_enemies", 0),

                        (try_for_agents,":agent"),
                            (agent_is_alive,":agent"), ## don't shield dead
                            (neg|agent_is_wounded,":agent"), ## don't shield wounded
                            (agent_is_human,":agent"), ## don't shield horses
                            (agent_get_team, ":agent_team", ":agent"),
                            (teams_are_enemies, ":chosen_team", ":agent_team"), ## don't shield allies
                            (neq, ":chosen", ":agent"), ## shooter can't shield self
                            (agent_get_slot, ":channeler", ":agent", slot_agent_is_channeler),
                            (eq, ":channeler", 1),
                            (agent_get_slot, ":already_shielded", ":agent", slot_agent_is_shielded),
                            (eq, ":already_shielded", 0),
                            (agent_get_look_position, pos2, ":agent"),
                            (get_distance_between_positions,":dist",pos1,pos2),
                            (lt,":dist",":distance"),
                            (assign,":target",":agent"),
                            (assign,":distance",":dist"),
                            (val_add, ":number_of_enemies", 1),
                        (try_end),

                        (try_begin),
                        (ge, ":number_of_enemies", 1),
                            (agent_get_troop_id, ":target_id", ":target"),
                            (troop_get_xp, ":target_xp", ":target_id"),
                            (agent_get_troop_id, ":chosen_id", ":chosen"),
                            (troop_get_xp, ":chosen_xp", ":chosen_id"),
                    
                            (try_begin),
                            (gt, ":chosen_xp", ":target_xp"),
                                (store_random_in_range, ":random", 1, 100),
                                (gt, ":random", 25),
                                    # set slot
                                    (agent_set_slot, ":target", slot_agent_is_shielded, 1),
                                    (agent_set_slot, ":target", slot_agent_shielded_by, ":chosen"),

                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 60),
                                    (try_end),
                                    (add_xp_to_troop,30,":chosen"),
                                    (play_sound, "snd_shield"),  # new sound?
                            (else_try),
                                (store_random_in_range, ":random", 1, 100),
                                (gt, ":random", 75),
                                    # set slot
                                    (agent_set_slot, ":target", slot_agent_is_shielded, 1),
                                    (agent_set_slot, ":target", slot_agent_shielded_by, ":chosen"),
                    
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 120),
                                    (try_end),
                                    (add_xp_to_troop,60,":chosen"),
                                    (play_sound, "snd_shield"),  # new sound?
                            (try_end),
                        (try_end),

                    # End Shield Weave


#########################################  Weave 12
                    (else_try),
                    (eq, ":active_weave", 9),
                        # Seeker Weave

                        (assign, ":distance",99999),
                        (assign, ":number_of_enemies", 0),

                        (try_for_agents,":agent"),
                            (agent_is_alive,":agent"), ## don't hurt dead
                            (neg|agent_is_wounded,":agent"), ## don't hurt wounded
                            (agent_is_human,":agent"), ## don't hurt horses
                            (agent_get_team, ":agent_team", ":agent"),
                            (teams_are_enemies, ":chosen_team", ":agent_team"), ## don't hurt allies
                            (neq, ":chosen", ":agent"), ## shooter can't hurt self
                            (agent_get_slot, ":already_targeted", ":agent", slot_agent_has_active_seeker),
                            (eq, ":already_targeted", 0),
                            (agent_get_look_position, pos2, ":agent"),
                            (get_distance_between_positions,":dist",pos1,pos2),
                            (lt,":dist",":distance"),
                            (assign,":target",":agent"),
                            (assign,":distance",":dist"),
                            (val_add, ":number_of_enemies", 1),
                        (try_end),

#                    (assign, reg45, ":dist"),
#                    (display_message, "@Target is {reg45} from shooter..."),

                        (try_begin),
                        (ge, ":number_of_enemies", 1),
                        (le, "$g_number_seekers_active", 20),
                            (assign, ":slot_found", 0),
                    
                            (try_begin),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_1", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos31, pos1),  # cur position for seeker 1
                                (assign, "$g_seeker_slot_1_target", ":target"), # make target global target for slot 1
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), # slot chosen as the target's shooter
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), # show that agent is getting tracked
                                (val_add, "$g_number_seekers_active", 1), # add to total number of active seekers
                                (assign, "$g_seeker_slot_1", 1), # globally show that the seeker slot is full
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_2", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos32, pos1),
                                (assign, "$g_seeker_slot_2_target", ":target"),
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"),
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1),
                                (val_add, "$g_number_seekers_active", 1),
                                (assign, "$g_seeker_slot_2", 1),
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_3", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos33, pos1),  
                                (assign, "$g_seeker_slot_3_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_3", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_4", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos34, pos1),  
                                (assign, "$g_seeker_slot_4_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_4", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_5", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos35, pos1),  
                                (assign, "$g_seeker_slot_5_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_5", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_6", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos36, pos1),  
                                (assign, "$g_seeker_slot_6_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_6", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_7", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos37, pos1),  
                                (assign, "$g_seeker_slot_7_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_7", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_8", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos38, pos1),  
                                (assign, "$g_seeker_slot_8_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_8", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_9", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos39, pos1),  
                                (assign, "$g_seeker_slot_9_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_9", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_10", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos40, pos1),  
                                (assign, "$g_seeker_slot_10_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_10", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_11", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos41, pos1),  # cur position for seeker 11
                                (assign, "$g_seeker_slot_11_target", ":target"), # make target global target for slot 11
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), # slot chosen as the target's shooter
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), # show that agent is getting tracked
                                (val_add, "$g_number_seekers_active", 1), # add to total number of active seekers
                                (assign, "$g_seeker_slot_11", 1), # globally show that the seeker slot is full
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_12", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos42, pos1),
                                (assign, "$g_seeker_slot_12_target", ":target"),
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"),
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1),
                                (val_add, "$g_number_seekers_active", 1),
                                (assign, "$g_seeker_slot_12", 1),
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_13", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos43, pos1),  
                                (assign, "$g_seeker_slot_13_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_13", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_14", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos44, pos1),  
                                (assign, "$g_seeker_slot_14_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_14", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_15", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos45, pos1),  
                                (assign, "$g_seeker_slot_15_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_15", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_16", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos46, pos1),  
                                (assign, "$g_seeker_slot_16_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_16", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_17", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos47, pos1),  
                                (assign, "$g_seeker_slot_17_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_17", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_18", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos48, pos1),  
                                (assign, "$g_seeker_slot_18_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_18", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_19", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos49, pos1),  
                                (assign, "$g_seeker_slot_19_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_19", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_20", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos50, pos1),  
                                (assign, "$g_seeker_slot_20_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_20", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (try_end),
                        (else_try),
                        (ge, ":number_of_enemies", 1),
                        (eq, "$g_number_seekers_active", 20),
                        (neg|agent_is_non_player, ":chosen"),
                            (display_message, "@Too many active seekers!!"), 
                        (try_end),
                        
                    # End Seeker Weave


#########################################  Weave 13
                    (else_try),
                    (eq, ":active_weave", 10),
                        # Compulsion Weave

                        (assign, ":distance",99999),
                        (assign, ":number_of_enemies", 0),

                        (try_for_agents,":agent"),
                            (agent_is_alive,":agent"), ## don't compel dead
                            (neg|agent_is_wounded,":agent"), ## don't compel wounded
                            (agent_is_human,":agent"), ## don't compel horses
                            (agent_get_team, ":agent_team", ":agent"),
                            (teams_are_enemies, ":chosen_team", ":agent_team"), ## don't compel allies
                            (neq, ":chosen", ":agent"), ## shooter can't compel self
                            (get_player_agent_no,":player_agent"),
                            (neq, ":agent", ":player_agent"), ## shooter can't compel player (too many complications)
                            (agent_get_slot, ":already_compelled", ":agent", slot_agent_under_compulsion),
                            (eq, ":already_compelled", 0),
                            (agent_get_look_position, pos2, ":agent"),
                            (get_distance_between_positions,":dist",pos1,pos2),
                            (lt,":dist",":distance"),
                            (assign,":target",":agent"),
                            (assign,":distance",":dist"),
                            (val_add, ":number_of_enemies", 1),
                        (try_end),

                        (try_begin),
                        (ge, ":number_of_enemies", 1),
                            (agent_get_troop_id, ":target_id", ":target"),
                            (troop_get_xp, ":target_xp", ":target_id"),
                            (agent_get_troop_id, ":chosen_id", ":chosen"),
                            (troop_get_xp, ":chosen_xp", ":chosen_id"),

                            (agent_get_slot, ":channeler", ":agent", slot_agent_is_channeler),

                            (agent_get_team, ":chosen_team", ":chosen"),
                            (agent_get_team, ":target_team", ":target"),
                    
                            (try_begin),
                            (eq, ":channeler", 1), # target is channeler
                                (try_begin),
                                (gt, ":chosen_xp", ":target_xp"), # target less experienced
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 60),
                                        (agent_set_team, ":target", ":chosen_team"),
                
                                        # set slot
                                        (agent_set_slot, ":target", slot_agent_under_compulsion, 1),
                                        (agent_set_slot, ":target", slot_agent_compelled_by, ":chosen"),
                                        (agent_set_slot, ":target", slot_agent_compelled_start_team, ":target_team"),

                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 150),
                                        (try_end),
                                        (add_xp_to_troop,75,":chosen"),
                                        (play_sound, "snd_compulsion"),
                                (else_try), # target more experienced
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 85),
                                        (agent_set_team, ":target", ":chosen_team"),
                
                                        # set slot
                                        (agent_set_slot, ":target", slot_agent_under_compulsion, 1),
                                        (agent_set_slot, ":target", slot_agent_compelled_by, ":chosen"),
                                        (agent_set_slot, ":target", slot_agent_compelled_start_team, ":target_team"),

                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 200),
                                        (try_end),
                                        (add_xp_to_troop,100,":chosen"),
                                        (play_sound, "snd_compulsion"),
                                (try_end),
                            (else_try), # target is non-channeler
                                (try_begin),
                                (gt, ":chosen_xp", ":target_xp"), # target less experienced
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 10),
                                        (agent_set_team, ":target", ":chosen_team"),
                
                                        # set slot
                                        (agent_set_slot, ":target", slot_agent_under_compulsion, 1),
                                        (agent_set_slot, ":target", slot_agent_compelled_by, ":chosen"),
                                        (agent_set_slot, ":target", slot_agent_compelled_start_team, ":target_team"),

                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 50),
                                        (try_end),
                                        (add_xp_to_troop,25,":chosen"),
                                        (play_sound, "snd_compulsion"),
                                (else_try), # target more experienced
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 35),
                                        (agent_set_team, ":target", ":chosen_team"),
                
                                        # set slot
                                        (agent_set_slot, ":target", slot_agent_under_compulsion, 1),
                                        (agent_set_slot, ":target", slot_agent_compelled_by, ":chosen"),
                                        (agent_set_slot, ":target", slot_agent_compelled_start_team, ":target_team"),

                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 100),
                                        (try_end),
                                        (add_xp_to_troop,50,":chosen"),
                                        (play_sound, "snd_compulsion"),
                                (try_end),
                            (try_end),
                        (try_end),

                    # End Compulsion Weave


################################## Weave 14
                    (else_try),
                    (eq, ":active_weave", 11),

                         #Balefire Weave (rip victom from pattern and undo their last actions)

                        (assign, ":times_near_ground", 0),

                        (try_for_range,reg5,1,500),  ###was 500
                        (eq, ":times_near_ground", 0),
                            (particle_system_burst, "psys_balefire_beam", pos1, 15), ## need balefire trail
                            (position_move_y,pos1,30),

                            #added for gravity effect and flight randomness
                            (store_mod, ":fall", reg5, 2),
                            (try_begin),
                            (eq, ":fall", 0),
                                (position_move_x,pos1,3),
                            (try_end),

                            (store_mod, ":weave", reg5, 5),
                            (try_begin),
                            (eq, ":weave", 0),
                                (store_random_in_range, ":random", -7, 8),
                                (position_move_z,pos1,":random"),
                            (try_end),
                            #end added for gravity effect and flight randomness
            
                            (copy_position,pos2,pos1),
                            (position_set_z_to_ground_level, pos2),
                            (get_distance_between_positions,":dist",pos1,pos2),

                            (position_get_z, ":z_ground", pos2),
                            (store_add, ":z_ground_low", ":z_ground", 200),
                            (store_add, ":z_ground_high", ":z_ground", 2000),

                            (try_for_agents, ":agent"),
                                (neq, ":chosen", ":agent"),
                                (neq, ":chosen_horse", ":agent"),
#                                (neg|agent_is_ally, ":agent"),
                                (agent_is_alive, ":agent"),
                                (neg|agent_is_wounded, ":agent"),
                                (agent_get_look_position, pos4, ":agent"),
                                (get_distance_between_positions, ":dist_2", pos2, pos4),
                                (position_get_z, ":z_attack_trail", pos1),
                                (lt, ":dist_2", 50), # balefire must be near the agent (x-y radius)
                                (is_between, ":z_attack_trail", ":z_ground_low", ":z_ground_high"), # balefire must be within the agent's body (z height)
                                (agent_set_slot, ":agent", slot_agent_hit_by_balefire, 1),
                                (agent_set_slot, ":agent", slot_agent_balefire_shooter, ":chosen"),
                                (try_for_range, ":unused", 1, 10),
                                    (particle_system_burst, "psys_balefire_strike", pos4, 20),  #need
                                    (position_move_z, pos4, 20),
                                (try_end),
                            (try_end),
                    
                            (try_begin),
                            (lt,":dist",10),
                                (val_add, ":times_near_ground", 1),
                                (play_sound,"snd_balefire"),
                                (copy_position, pos3, pos1),
                                (scene_prop_get_instance,":instance", "spr_explosion", 0),  #need
                                (position_copy_origin,pos2,pos1),
                                (prop_instance_set_position,":instance",pos2),
                                (position_move_z,pos2,1000),
                                (prop_instance_animate_to_position,":instance",pos2,175),
                                (assign,reg5,1000),  #was 1000
                            (try_end),
                        (try_end),
                                
                        #Balefire weave end


### Be sure to leave this (try_end), at the end of the active weave code
                    (try_end),


                (else_try),  ## if beginner channeler fails to make weave, then show a small attempt weave

                    (position_move_y, pos1, 50),
                    (particle_system_burst, "psys_electricity_blast", pos1, 50),
                    (add_xp_to_troop, 5, ":chosen"),

                (try_end),


######################################### Run the "Shield Breaker" code if the channeler is shielded...
            (else_try),
                (agent_get_slot, ":shield_holder", ":chosen", slot_agent_shielded_by),

                (agent_get_troop_id, ":shield_holder_id", ":shield_holder"),
                (troop_get_xp, ":shield_holder_xp", ":shield_holder_id"),
                (agent_get_troop_id, ":chosen_id", ":chosen"),
                (troop_get_xp, ":chosen_xp", ":chosen_id"),

                (try_begin),
                (agent_is_alive, ":shield_holder"), # shield creator is alive
                (neg|agent_is_wounded, ":shield_holder"),
                    (try_begin),
                    (gt, ":chosen_xp", ":shield_holder_xp"), # shield holder 'weaker'
                        (store_random_in_range, ":random", 1, 100),
                        (gt, ":random", 50),
                            (agent_set_slot, ":chosen", slot_agent_is_shielded, 0),
                            (play_sound, "snd_unravel"),
                            (try_begin), # add to channeling multiplier if agent is player
                            (neg|agent_is_non_player, ":chosen"),
                                (val_add, "$g_channeling_proficiency_modifier", 60),
                                (display_message, "@You are no longer shielded from the One Power!!"),
                            (try_end),
                            (add_xp_to_troop,30,":chosen"),
                    (else_try), # shield holder 'stronger'
                        (store_random_in_range, ":random", 1, 100),
                        (gt, ":random", 90),
                            (agent_set_slot, ":chosen", slot_agent_is_shielded, 0),
                            (play_sound, "snd_unravel"),
                            (try_begin), # add to channeling multiplier if agent is player
                            (neg|agent_is_non_player, ":chosen"),
                                (val_add, "$g_channeling_proficiency_modifier", 120),
                                (display_message, "@You are no longer shielded from the One Power!!"),
                            (try_end),
                            (add_xp_to_troop,60,":chosen"),
                    (try_end),
                (else_try), # shield creator is dead / wounded
                    (store_random_in_range, ":random", 1, 100),
                    (gt, ":random", 25),
                        (agent_set_slot, ":chosen", slot_agent_is_shielded, 0),
                        (play_sound, "snd_unravel"),
                        (try_begin), # add to channeling multiplier if agent is player
                        (neg|agent_is_non_player, ":chosen"),
                            (val_add, "$g_channeling_proficiency_modifier", 30),
                            (display_message, "@You are no longer shielded from the One Power!!"),
                        (try_end),
                        (add_xp_to_troop,15,":chosen"),
                (try_end),
                
            # End of Shield Breaker code
                
            (try_end),

                         ],),
    ]],
 

################################################################################
############### Multiplayer One Power Item #####################################
################################################################################

 ["power_player_multiplayer","One Power", [("cuindiar_disc",0),("practice_arrows_2",ixmesh_flying_ammo)],itp_type_pistol|itp_primary|itp_secondary|itp_bonus_against_shield , itcf_shoot_crossbow, 5 , weight(4)|spd_rtng(250) | shoot_speed(150) | thrust_damage(1 ,  pierce)|max_ammo(5000)|weapon_length(65),imodbits_missile,
  [(ti_on_weapon_attack, [

#                    (get_player_agent_no,":player_agent"),

            # new for multiplayer
            (multiplayer_get_my_player, ":player"),
            (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
            (try_begin),
            (eq, ":active_channeling_weave", 1),
                (assign, ":stamina_cost", 600),
            (else_try),
            (eq, ":active_channeling_weave", 2),
                (assign, ":stamina_cost", 1050),
            (else_try),
            (eq, ":active_channeling_weave", 3),
                (assign, ":stamina_cost", 1500),
            (else_try),
            (eq, ":active_channeling_weave", 4),
                (assign, ":stamina_cost", 2100),
            (else_try),
            (eq, ":active_channeling_weave", 5),
                (assign, ":stamina_cost", 2550),
            (else_try),
            (eq, ":active_channeling_weave", 6),
                (assign, ":stamina_cost", 2850),
            (else_try),
            (eq, ":active_channeling_weave", 7),
                (assign, ":stamina_cost", 3150),
            (else_try),
            (eq, ":active_channeling_weave", 8),
                (assign, ":stamina_cost", 3600),
            (else_try),
            (eq, ":active_channeling_weave", 9),
                (assign, ":stamina_cost", 4350),
            (else_try),
            (eq, ":active_channeling_weave", 10),
                (assign, ":stamina_cost", 5100),
            (else_try),
            (eq, ":active_channeling_weave", 11),
                (assign, ":stamina_cost", 5850),
            (else_try),
            (eq, ":active_channeling_weave", 12),
                (assign, ":stamina_cost", 6600),
            (else_try),
            (eq, ":active_channeling_weave", 13),
                (assign, ":stamina_cost", 7350),
            (else_try),
            (eq, ":active_channeling_weave", 14),
                (assign, ":stamina_cost", 8100),
            (try_end),
            
            (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
            (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
            (try_begin),
            (lt, ":stamina_check", 0),
                (display_message, "@You are too tired to channel..."),
            (else_try),
                (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                (multiplayer_send_int_to_server, multiplayer_event_send_one_power_use_to_server, ":active_channeling_weave"),
            (try_end),


                         ],),
    ]], 

#################################################################
######## The backup of the 2nd try at Multiplayer ###############
#################################################################

 ["power_player_multiplayer_backup","One Power", [("cuindiar_disc",0),("practice_arrows_2",ixmesh_flying_ammo)],itp_type_pistol|itp_primary|itp_secondary|itp_bonus_against_shield , itcf_shoot_crossbow, 5 , weight(4)|spd_rtng(250) | shoot_speed(150) | thrust_damage(1 ,  pierce)|max_ammo(5000)|weapon_length(65),imodbits_missile,
  [(ti_on_weapon_attack, [

#                    (get_player_agent_no,":player_agent"),

            # new for multiplayer
            (multiplayer_get_my_player, ":player"),
            # end

            (assign,":distance",99999),
                         
            (try_for_agents,":agent"),
                (agent_is_alive,":agent"),
                (neg|agent_is_wounded,":agent"), ## add this to not re-count wounded people
                (agent_is_human,":agent"),
                (agent_get_look_position, pos2, ":agent"), 
                (get_distance_between_positions,":dist",pos1,pos2),
                (lt,":dist",":distance"),
                (assign,":chosen",":agent"), # 'chosen' is the shooter
                (assign,":distance",":dist"),
            (try_end),

            (agent_get_horse, ":chosen_horse", ":chosen"),
            (agent_get_team, ":chosen_team", ":chosen"),

## Run the channeling code only if the channeling agent is not shielded
            (agent_get_slot, ":agent_is_shielded", ":chosen", slot_agent_is_shielded),

            (try_begin),
            (eq, ":agent_is_shielded", 0),

                
################################## Weave 1
                (try_begin),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 1),
                # end
                    #Air Blast (push agent and do a little damage)
                    (assign, ":stamina_cost", 600),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end

                        (copy_position, pos3, pos1),
                        (position_move_y, pos3, 350),
                        (position_set_z_to_ground_level,pos3),
                        
                        (try_for_agents,":agent"),
                            (neq,":chosen",":agent"), ## added this to avoid killing shooter
                            (neq, ":chosen_horse", ":agent"),
#                            (neg|agent_is_ally,":agent"), ## add this to avoid killing allies
                            (agent_is_alive,":agent"), ## add this to not re-kill dead people
                            (neg|agent_is_wounded,":agent"), ## add this to not re-kill wounded people
                            (agent_get_look_position,pos2,":agent"),
                            (get_distance_between_positions,":dist",pos3,pos2),
                            (store_agent_hit_points,":target_health",":agent",1),
                            (lt,":dist",400),

                                #(agent_set_slot, ":agent", slot_agent_is_airborne, 1),
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_is_airborne, 1),

                                (position_get_x, ":attacker_x", pos1),
                                (position_get_y, ":attacker_y", pos1),
                                (position_get_x, ":target_x", pos2),
                                (position_get_y, ":target_y", pos2),

                                (store_sub, ":run", ":target_x", ":attacker_x"),
                                (store_sub, ":rise", ":target_y", ":attacker_y"),

                                #(agent_set_slot, ":agent", slot_agent_airborne_x_movement, ":run"),
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_airborne_x_movement, ":run"),
                                #(agent_set_slot, ":agent", slot_agent_airborne_y_movement, ":rise"),
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_airborne_y_movement, ":rise"),

                                (get_distance_between_positions, ":dist_from_chosen", pos1, pos2),
                                (try_begin),
                                (lt, ":dist_from_chosen", 100),
                                    #(agent_set_slot, ":agent", slot_agent_airborne_power_factor, 8),
                                    (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_airborne_power_factor, 8),
                                (else_try),
                                (is_between, ":dist_from_chosen", 100, 250),
                                    #(agent_set_slot, ":agent", slot_agent_airborne_power_factor, 6),
                                    (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_airborne_power_factor, 6),
                                (else_try),
                                (is_between, ":dist_from_chosen", 250, 450),
                                    #(agent_set_slot, ":agent", slot_agent_airborne_power_factor, 4),
                                    (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_airborne_power_factor, 4),
                                (else_try),
                                (is_between, ":dist_from_chosen", 450, 750),
                                    #(agent_set_slot, ":agent", slot_agent_airborne_power_factor, 2),
                                    (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_airborne_power_factor, 2),
                                (try_end),
                                
                                (try_begin),
                                    (gt,":target_health",5),
                                    (val_sub,":target_health",5),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                (try_end),
                            
                        (try_end),
                        (particle_system_burst, "psys_massive_pistol_smoke", pos1, 25),
                        #(play_sound,"snd_air_blast"),
                        (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_air_blast"),
            
                    (try_end),

                # air blast weave end


################################## Weave 2
                (else_try),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 2),
                # end
                    #Freeze Weave
                    (assign, ":stamina_cost", 1000),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end

                        (assign, ":times_near_ground", 0),
                        (assign, ":near_enemy", 0),

                        (try_for_range,reg5,1,1000),  ###was 500
                        (eq, ":times_near_ground", 0),
                            (particle_system_burst, "psys_freeze_blast", pos1, 10),
                            (position_move_y,pos1,20), # was 10
                            (copy_position,pos2,pos1),
                            (position_set_z_to_ground_level, pos2),
                            (get_distance_between_positions,":dist",pos1,pos2),

                            (position_get_z, ":z_ground", pos2),
                            (store_add, ":z_ground_low", ":z_ground", 20), 
                            (store_add, ":z_ground_high", ":z_ground", 200),

                            (try_for_agents, ":agent"),
                            (eq, ":near_enemy", 0),
                                (neq, ":chosen", ":agent"),
                                (neq, ":chosen_horse", ":agent"),
                                (agent_get_team, ":agent_team", ":agent"),
                                (teams_are_enemies, ":chosen_team", ":agent_team"),
                                (agent_is_alive, ":agent"),
                                (neg|agent_is_wounded, ":agent"),
                                (agent_get_look_position, pos4, ":agent"),
                                (get_distance_between_positions, ":dist_2", pos2, pos4),
                                (position_get_z, ":z_attack_trail", pos1),
                                (lt, ":dist_2", 50), # near agent (x-y)
                                (is_between, ":z_attack_trail", ":z_ground_low", ":z_ground_high"), # within the agent's body (z height)
                                (assign, ":dist", 5),
                                (assign, ":near_enemy", 1),
                            (try_end),
                    
                            (try_begin),
                            (lt,":dist",10),
                                (val_add, ":times_near_ground", 1),
                                (particle_system_burst, "psys_tsunami", pos1, 75),  # effect needs a long duration
                                #(play_sound,"snd_freeze"), # need a sound for freeze
                                (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_freeze"),
                                (copy_position, pos3, pos1),
                                #(scene_prop_get_instance,":instance", "spr_snowy_heap_a", 0),  #need
                                #(position_copy_origin,pos2,pos1),
                                #(prop_instance_set_position,":instance",pos2),
                                (assign,reg5,2000),  #was 1000
                            (try_end),
                        (try_end),
                                
                        (try_for_agents,":agent"),
                            (neq,":chosen",":agent"), ## added this to avoid freezing shooter
                            (neq, ":chosen_horse", ":agent"),
#                            (neg|agent_is_ally,":agent"), ## add this to avoid freezing allies
                            (agent_is_alive,":agent"), ## add this to not freeze dead people
                            (neg|agent_is_wounded,":agent"), ## add this to not freeze wounded people
                            (agent_get_position,pos2,":agent"),
                            (get_distance_between_positions,":dist",pos3,pos2),
                         
                            (try_begin),
                            (lt,":dist",250),  # freeze (slowed movement) if blast within 250 of agent
                                (agent_set_speed_limit, ":agent", 0),
                                # add damage to freeze for multiplayer
                                (try_begin),
                                    (gt,":target_health",5),
                                    (val_sub,":target_health",5),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    # new for multiplayer
                                    (player_get_gold, ":gold", ":player"),
                                    (val_add, ":gold", 3),
                                    (player_set_gold, ":player", ":gold", 15000),
                                    # end
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                (try_end),
                            (try_end),
                    
                        (try_end),
            
                    (try_end),
                            
                    #Freeze weave end


#########################################  Weave 3
                (else_try),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 3),
                # end
                    # Heal Nearest Ally Weave
                    (assign, ":stamina_cost", 1500),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end

                        (assign, ":distance",99999),
                        (assign, ":number_of_allies", 0),

                        (try_for_agents,":agent"),
                            (agent_is_alive,":agent"), ## don't heal dead
                            (neg|agent_is_wounded,":agent"), ## don't heal wounded
                            (agent_is_ally,":agent"), ## don't heal enemies
                            (agent_is_human,":agent"), ## don't look for horses on the first round
                            (neq, ":chosen", ":agent"), ## shooter can't heal self
                            (store_agent_hit_points,":health",":agent",0),
                            (lt,":health",75),
                            (agent_get_look_position, pos2, ":agent"),
                            (get_distance_between_positions,":dist",pos1,pos2),
                            (lt,":dist",":distance"),
                            (assign,":nearest_hurt_ally",":agent"),
                            (assign,":distance",":dist"),
                            (val_add, ":number_of_allies", 1),
                        (try_end),

                        (try_begin),
                        (ge, ":number_of_allies", 1),
                            (agent_set_hit_points,":nearest_hurt_ally",100,0),
                            (agent_get_look_position, pos2, ":nearest_hurt_ally"),
                            (particle_system_burst, "psys_heal_aura", pos2, 50),
                            #(play_sound, "snd_heal"),
                            (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_heal"),
                            # new for multiplayer
                            (player_get_gold, ":gold", ":player"),
                            (val_add, ":gold", 3),
                            (player_set_gold, ":player", ":gold", 15000),
                            # end
                        (try_end),

                    (try_end),
                        
                    # End Heal Nearest Ally Weave


################################## Weave 4
                (else_try),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 4),
                # end
                    #Fire Ball (do damage based on how close agent is to the blast)
                    (assign, ":stamina_cost", 2100),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end

                        (assign, ":times_near_ground", 0),
                        (assign, ":near_enemy", 0),

                        (try_for_range,reg5,1,1000),  ###was 500
                        (eq, ":times_near_ground", 0),
                            (particle_system_burst, "psys_torch_fire", pos1, 15),
                            (position_move_y,pos1,20),
                            (copy_position,pos2,pos1),
                            (position_set_z_to_ground_level, pos2),
                            (get_distance_between_positions,":dist",pos1,pos2),

                            (position_get_z, ":z_ground", pos2),
                            (store_add, ":z_ground_low", ":z_ground", 20),
                            (store_add, ":z_ground_high", ":z_ground", 200),

                            (try_for_agents, ":agent"),
                            (eq, ":near_enemy", 0),
                                (neq, ":chosen", ":agent"),
                                (neq, ":chosen_horse", ":agent"),
                                (agent_get_team, ":agent_team", ":agent"),
                                (teams_are_enemies, ":chosen_team", ":agent_team"),
                                (agent_is_alive, ":agent"),
                                (neg|agent_is_wounded, ":agent"),
                                (agent_get_look_position, pos4, ":agent"),
                                (get_distance_between_positions, ":dist_2", pos2, pos4),
                                (position_get_z, ":z_attack_trail", pos1),
                                (lt, ":dist_2", 50), # near agent (x-y)
                                (is_between, ":z_attack_trail", ":z_ground_low", ":z_ground_high"), # within the agent's body (z height)
                                (assign, ":dist", 5),
                                (assign, ":near_enemy", 1),
                            (try_end),
                    
                            (try_begin),
                            (lt,":dist",10),
                                (val_add, ":times_near_ground", 1),
                                (particle_system_burst, "psys_massive_fire", pos1, 15),  #need
                                (particle_system_burst, "psys_war_smoke_tall", pos1, 15),  #need
                                #(play_sound,"snd_fire_ball"),
                                (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_fire_ball"),
                                (copy_position, pos3, pos1),
                                #(scene_prop_get_instance,":instance", "spr_explosion", 0),  #need
                                #(position_copy_origin,pos2,pos1),
                                #(prop_instance_set_position,":instance",pos2),
                                #(position_move_z,pos2,1000),
                                #(prop_instance_animate_to_position,":instance",pos2,175),
                                (assign,reg5,2000),  #was 1000
                            (try_end),
                        (try_end),
                                
                        (try_for_agents,":agent"),
                            (neq,":chosen",":agent"), ## added this to avoid killing shooter
                            (neq, ":chosen_horse", ":agent"),
#                            (neg|agent_is_ally,":agent"), ## add this to avoid killing allies
                            (agent_is_alive,":agent"), ## add this to not re-kill dead people
                            (neg|agent_is_wounded,":agent"), ## add this to not re-kill wounded people
                            (agent_get_position,pos2,":agent"),
                            (get_distance_between_positions,":dist",pos3,pos2),
                         
                            # do 25 damage if fireball within 50 of agent
                            (try_begin),
                                (lt,":dist",50),  #was 300
                                (store_agent_hit_points,":target_health",":agent",1),
                                (try_begin),
                                    (gt,":target_health",25),
                                    (val_sub,":target_health",25),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    #(agent_set_slot, ":agent", slot_agent_on_fire, 1),
                                    (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_on_fire, 1),
                                    #(agent_set_slot, ":agent", slot_agent_fire_starter, ":chosen"),
                                    (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_fire_starter, ":chosen"),
                                    #(agent_set_slot, ":agent", slot_agent_fire_duration, 20),
                                    (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_fire_duration, 20),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                (try_end),
                            # do 15 damage if fireball within 50 to 125 of agent
                            (else_try),
                                (is_between,":dist",50,125),  #was 300
                                (store_agent_hit_points,":target_health",":agent",1),
                                (try_begin),
                                    (gt,":target_health",15),
                                    (val_sub,":target_health",15),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    #(agent_set_slot, ":agent", slot_agent_on_fire, 1),
                                    (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_on_fire, 1),
                                    #(agent_set_slot, ":agent", slot_agent_fire_starter, ":chosen"),
                                    (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_fire_starter, ":chosen"),
                                    #(agent_set_slot, ":agent", slot_agent_fire_duration, 15),
                                    (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_fire_duration, 15),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                (try_end),
                            # do 10 damage if fireball within 125 to 225 of agent
                            (else_try),
                                (is_between,":dist",125,225),  #was 300
                                (store_agent_hit_points,":target_health",":agent",1),
                                (try_begin),
                                    (gt,":target_health",10),
                                    (val_sub,":target_health",10),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    #(agent_set_slot, ":agent", slot_agent_on_fire, 1),
                                    (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_on_fire, 1),
                                    #(agent_set_slot, ":agent", slot_agent_fire_starter, ":chosen"),
                                    (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_fire_starter, ":chosen"),
                                    #(agent_set_slot, ":agent", slot_agent_fire_duration, 10),
                                    (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_fire_duration, 10),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                (try_end),
                            # do 5 damage if fireball within 225 to 350 of agent
                            (else_try),
                                (is_between,":dist",225,350),  #was 300
                                (store_agent_hit_points,":target_health",":agent",1),
                                (try_begin),
                                    (gt,":target_health",5),
                                    (val_sub,":target_health",5),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    #(agent_set_slot, ":agent", slot_agent_on_fire, 1),
                                    (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_on_fire, 1),
                                    #(agent_set_slot, ":agent", slot_agent_fire_starter, ":chosen"),
                                    (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_fire_starter, ":chosen"),
                                    #(agent_set_slot, ":agent", slot_agent_fire_duration, 5),
                                    (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_fire_duration, 5),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                (try_end),
                            (try_end),

                        (try_end),

                    (try_end),
                
                    #Fireball weave end


#########################################  Weave 5
                (else_try),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 5),
                # end
                    # Unravel Weave
                    (assign, ":stamina_cost", 2500),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end

                        (assign, ":chosen_active_effect", 0),
                        (assign, ":chosen_horse_on_fire", 0),
                        (assign, ":teammate_active_effect", 5),
                

                        (agent_get_slot, ":chosen_seeker", ":chosen", slot_agent_has_active_seeker),
                        (try_begin),
                        (eq, ":chosen_seeker", 1),
                            (assign, ":chosen_active_effect", 1),
                
                        (else_try), # chosen doesn't have a seeker
                            (agent_get_slot, ":chosen_fire", ":chosen", slot_agent_on_fire),
                            (try_begin),
                            (eq, ":chosen_fire", 1),
                                (assign, ":chosen_active_effect", 3),
                
                            (else_try), # chosen not on fire
                                (agent_get_slot, ":chosen_bound", ":chosen", slot_agent_is_bound),
                                (try_begin),
                                (eq, ":chosen_bound", 1),
                                    (assign, ":chosen_active_effect", 4),
                
                                (else_try), # chosen not bound
                                    (agent_get_horse, ":chosen_horse", ":chosen"),
                                    (try_begin),
                                    (ge, ":chosen_horse", 0),
                                        (agent_get_slot, ":chosen_horse_fire", ":chosen_horse", slot_agent_on_fire),
                                    (try_end),
                
                                    (try_begin),
                                    (eq, ":chosen_horse_fire", 1),
                                        (assign, ":chosen_horse_on_fire", 1),

                                    (else_try), # chosen horse not on fire
                                        
                                        (try_for_agents,":agent"),
                                            (agent_is_alive,":agent"), ## don't help dead
                                            (neg|agent_is_wounded,":agent"), ## don't help wounded
#                                            (agent_is_human,":agent"), ## don't help horses
                
                                            # determine if agents under compulsion used to be teammates
                                            (agent_get_slot, ":compulsion_present", ":agent", slot_agent_under_compulsion),
                                            (assign, ":agent_ally", 0),
                                            (try_begin),
                                            (eq, ":compulsion_present", 1),
                                                (agent_get_slot, ":original_team", ":agent", slot_agent_compelled_start_team),
                                                (try_begin),
                                                (ge, ":original_team", 0),
                                                (eq, ":original_team", ":chosen_team"), # used to be teammate
                                                    (assign, ":agent_ally", 2),
                                                (else_try),
                                                (agent_is_ally, ":agent"), # teammate by compulsion
                                                    (assign, ":agent_ally", 1),
                                                (try_end),
                                            (else_try),
                                            (agent_is_ally, ":agent"), # always been teammate
                                                (assign, ":agent_ally", 1),
                                            (try_end),
                                                
                                            (gt, ":agent_ally", 0), ## don't help enemies
                                            (neq, ":chosen", ":agent"), ## this code will not look at 'chosen'
                
                                            (try_begin),
                                            (neq, ":teammate_active_effect", 1),
                                                (agent_get_slot, ":teammate_seeker", ":agent", slot_agent_has_active_seeker),
                                                (try_begin),
                                                (eq, ":teammate_seeker", 1),
                                                (eq, ":agent_ally", 1), # stop seekers for agents currently on chosen's team
                                                    (assign, ":teammate_active_effect", 1),
                                                (else_try),
                                                (neq, ":teammate_active_effect", 2),
                                                    (agent_get_slot, ":teammate_compelled", ":agent", slot_agent_under_compulsion),
                                                    (try_begin),
                                                    (eq, ":teammate_compelled", 1),
                                                    (eq, ":agent_ally", 2), # break compulsion on compelled allies
                                                        (assign, ":teammate_active_effect", 2),
                                                    (else_try),
                                                    (neq, ":teammate_active_effect", 3),
                                                        (agent_get_slot, ":teammate_fire", ":agent", slot_agent_on_fire),
                                                        (try_begin),
                                                        (eq, ":teammate_fire", 1),
                                                        (eq, ":agent_ally", 1), # stop fire for agents currently on chosen's team
                                                            (assign, ":teammate_active_effect", 3),
                                                        (else_try),
                                                        (neq, ":teammate_active_effect", 4),
                                                            (agent_get_slot, ":teammate_bound", ":agent", slot_agent_is_bound),
                                                            (try_begin),
                                                            (eq, ":teammate_bound", 1),
                                                            (eq, ":agent_ally", 1), # break bound for agents currently on chosen's team
                                                                (assign, ":teammate_active_effect", 4),
                                                            (try_end),
                                                        (try_end),
                                                    (try_end),
                                                (try_end),
                                            (try_end),
                
                                        (try_end),

                                        (assign, ":distance", 99999),
                                
                                        (try_for_agents,":agent"),
                                            (agent_is_alive,":agent"), ## don't help dead
                                            (neg|agent_is_wounded,":agent"), ## don't help wounded
#                                            (agent_is_human,":agent"), ## don't help horses
                
                                            # determine if agents under compulsion used to be teammates
                                            (agent_get_slot, ":compulsion_present", ":agent", slot_agent_under_compulsion),
                                            (assign, ":agent_ally", 0),
                                            (try_begin),
                                            (eq, ":compulsion_present", 1),
                                                (agent_get_slot, ":original_team", ":agent", slot_agent_compelled_start_team),
                                                (try_begin),
                                                (ge, ":original_team", 0),
                                                (eq, ":original_team", ":chosen_team"), # used to be teammate
                                                    (assign, ":agent_ally", 2),
                                                (else_try),
                                                (agent_is_ally, ":agent"), # teammate by compulsion
                                                    (assign, ":agent_ally", 1),
                                                (try_end),
                                            (else_try),
                                            (agent_is_ally, ":agent"), # always been teammate
                                                (assign, ":agent_ally", 1),
                                            (try_end),
                                                
                                            (gt, ":agent_ally", 0), ## don't help enemies
                                            (neq, ":chosen", ":agent"), ## this code will not look at 'chosen'

                                            (try_begin),
                                            (eq, ":teammate_active_effect", 1),
                                                (agent_get_slot, ":teammate_seeker", ":agent", slot_agent_has_active_seeker),
                                                (eq, ":teammate_seeker", 1),
                                                (eq, ":agent_ally", 1),
                                                    (agent_get_look_position, pos2, ":agent"),
                                                    (get_distance_between_positions,":dist",pos1,pos2),
                                                    (lt,":dist",":distance"),
                                                    (assign,":nearest_affected_ally",":agent"),
                                                    (assign,":distance",":dist"),
                                            (else_try),
                                            (eq, ":teammate_active_effect", 2),
                                                (agent_get_slot, ":teammate_compelled", ":agent", slot_agent_under_compulsion),
                                                (eq, ":teammate_compelled", 1),
                                                (eq, ":agent_ally", 2),
                                                    (agent_get_look_position, pos2, ":agent"),
                                                    (get_distance_between_positions,":dist",pos1,pos2),
                                                    (lt,":dist",":distance"),
                                                    (assign,":nearest_affected_ally",":agent"),
                                                    (assign,":distance",":dist"),
                                            (else_try),
                                            (eq, ":teammate_active_effect", 3),
                                                (agent_get_slot, ":teammate_fire", ":agent", slot_agent_on_fire),
                                                (eq, ":teammate_fire", 1),
                                                (eq, ":agent_ally", 1),
                                                    (agent_get_look_position, pos2, ":agent"),
                                                    (get_distance_between_positions,":dist",pos1,pos2),
                                                    (lt,":dist",":distance"),
                                                    (assign,":nearest_affected_ally",":agent"),
                                                    (assign,":distance",":dist"),
                                            (else_try),
                                            (eq, ":teammate_active_effect", 4),
                                                (agent_get_slot, ":teammate_bound", ":agent", slot_agent_is_bound),
                                                (eq, ":teammate_bound", 1),
                                                (eq, ":agent_ally", 1),
                                                    (agent_get_look_position, pos2, ":agent"),
                                                    (get_distance_between_positions,":dist",pos1,pos2),
                                                    (lt,":dist",":distance"),
                                                    (assign,":nearest_affected_ally",":agent"),
                                                    (assign,":distance",":dist"),
                                            (try_end),
                                        (try_end),
                                        # End of loops for finding closest affected ally
                                    (try_end),
                                    # End of loops for finding horse on fire
                
                                (try_end),
                            (try_end),
                        (try_end),
                        # End of if statements for does 'chosen' have active effects

                        (try_begin),
                        (gt, ":chosen_active_effect", 0), # chosen unraveling weave on self
                            (try_begin),
                            (eq, ":chosen_active_effect", 1),
                
                                (try_begin),
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 50),
                                        #(agent_set_slot, ":chosen", slot_agent_has_active_seeker, 0),
                                        (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":chosen", slot_agent_has_active_seeker, 0),
                
                                        (try_begin),
                                        (eq, "$g_seeker_slot_1_target_multi", ":chosen"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 1, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_2_target_multi", ":chosen"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 2, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_3_target_multi", ":chosen"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 3, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_4_target_multi", ":chosen"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 4, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_5_target_multi", ":chosen"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 5, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_6_target_multi", ":chosen"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 6, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_7_target_multi", ":chosen"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 7, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_8_target_multi", ":chosen"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 8, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_9_target_multi", ":chosen"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 9, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_10_target_multi", ":chosen"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 10, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_11_target_multi", ":chosen"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 11, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_12_target_multi", ":chosen"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 12, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_13_target_multi", ":chosen"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 13, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_14_target_multi", ":chosen"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 14, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_15_target_multi", ":chosen"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 15, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_16_target_multi", ":chosen"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 16, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_17_target_multi", ":chosen"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 17, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_18_target_multi", ":chosen"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 18, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_19_target_multi", ":chosen"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 19, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_20_target_multi", ":chosen"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 20, -1, 0, 0),
                                        (try_end),
                
                                        #(particle_system_burst, "psys_unravel_aura", pos1, 50), # handle this on the server side
                                        #(play_sound, "snd_unravel"),
                                        (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_unravel"),
                                        # new for multiplayer
                                        (player_get_gold, ":gold", ":player"),
                                        (val_add, ":gold", 10),
                                        (player_set_gold, ":player", ":gold", 15000),
                                        # end
                                (try_end),
                                    
                            (else_try),
                            (eq, ":chosen_active_effect", 3),
                
                                (try_begin),
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 25),
                                        #(agent_set_slot, ":chosen", slot_agent_on_fire, 0),
                                        (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":chosen", slot_agent_on_fire, 0),
                                        (particle_system_burst, "psys_unravel_aura", pos1, 50),
                                        #(play_sound, "snd_unravel"),
                                        (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_unravel"),
                                        # new for multiplayer
                                        (player_get_gold, ":gold", ":player"),
                                        (val_add, ":gold", 5),
                                        (player_set_gold, ":player", ":gold", 15000),
                                        # end
                                (try_end),
                            (else_try),
                            (eq, ":chosen_active_effect", 4),
                
                                (try_begin),
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 25),
                                        #(agent_set_slot, ":chosen", slot_agent_is_bound, 0),
                                        (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":chosen", slot_agent_is_bound, 0),
                                        (particle_system_burst, "psys_unravel_aura", pos1, 50),
                                        #(play_sound, "snd_unravel"),
                                        (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_unravel"),
                                        # new for multiplayer
                                        (player_get_gold, ":gold", ":player"),
                                        (val_add, ":gold", 5),
                                        (player_set_gold, ":player", ":gold", 15000),
                                        # end
                                (try_end),
                            (try_end),

                        (else_try), # chosen unraveling weave on horse
                        (eq, ":chosen_horse_on_fire", 1),

                            (agent_get_position, pos2, ":chosen_horse"),
                
                            (try_begin),
                                (store_random_in_range, ":random", 1, 100),
                                (gt, ":random", 25),
                                    #(agent_set_slot, ":chosen_horse", slot_agent_on_fire, 0),
                                    (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":chosen_horse", slot_agent_on_fire, 0),
                                    (particle_system_burst, "psys_unravel_aura", pos2, 50),
                                    #(play_sound, "snd_unravel"),
                                    (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_unravel"),
                                    # new for multiplayer
                                    (player_get_gold, ":gold", ":player"),
                                    (val_add, ":gold", 5),
                                    (player_set_gold, ":player", ":gold", 15000),
                                    # end
                            (try_end),

                        (else_try),
                        (lt, ":teammate_active_effect", 5), # chosen unraveling weave on teammate
                            (try_begin),
                            (eq, ":teammate_active_effect", 1),

                                (try_begin),
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 50),
                                        #(agent_set_slot, ":nearest_affected_ally", slot_agent_has_active_seeker, 0),
                                        (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":nearest_affected_ally", slot_agent_has_active_seeker, 0),
                
                                        (try_begin),
                                        (eq, "$g_seeker_slot_1_target_multi", ":nearest_affected_ally"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 1, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_2_target_multi", ":nearest_affected_ally"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 2, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_3_target_multi", ":nearest_affected_ally"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 3, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_4_target_multi", ":nearest_affected_ally"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 4, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_5_target_multi", ":nearest_affected_ally"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 5, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_6_target_multi", ":nearest_affected_ally"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 6, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_7_target_multi", ":nearest_affected_ally"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 7, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_8_target_multi", ":nearest_affected_ally"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 8, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_9_target_multi", ":nearest_affected_ally"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 9, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_10_target_multi", ":nearest_affected_ally"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 10, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_11_target_multi", ":nearest_affected_ally"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 11, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_12_target_multi", ":nearest_affected_ally"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 12, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_13_target_multi", ":nearest_affected_ally"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 13, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_14_target_multi", ":nearest_affected_ally"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 14, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_15_target_multi", ":nearest_affected_ally"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 15, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_16_target_multi", ":nearest_affected_ally"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 16, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_17_target_multi", ":nearest_affected_ally"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 17, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_18_target_multi", ":nearest_affected_ally"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 18, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_19_target_multi", ":nearest_affected_ally"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 19, -1, 0, 0),
                                        (else_try),
                                        (eq, "$g_seeker_slot_20_target_multi", ":nearest_affected_ally"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 20, -1, 0, 0),
                                        (try_end),
                
                                        #(particle_system_burst, "psys_unravel_aura", pos1, 50), # handle this on the server side
                                        #(play_sound, "snd_unravel"),
                                        (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_unravel"),
                                        # new for multiplayer
                                        (player_get_gold, ":gold", ":player"),
                                        (val_add, ":gold", 10),
                                        (player_set_gold, ":player", ":gold", 15000),
                                        # end
                                (try_end),

                            (else_try),
                            (eq, ":teammate_active_effect", 2),

                                (agent_get_position, pos2, ":nearest_affected_ally"),
                
                                (try_begin),
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 50),
                                        (agent_get_slot, ":start_team", ":nearest_affected_ally", slot_agent_compelled_start_team),
                                        (agent_set_team, ":nearest_affected_ally", ":start_team"),
                                        #(agent_set_slot, ":nearest_affected_ally", slot_agent_under_compulsion, 0),
                                        (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":nearest_affected_ally", slot_agent_under_compulsion, 0),
                                        (particle_system_burst, "psys_unravel_aura", pos2, 50),
                                        #(play_sound, "snd_unravel"),
                                        (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_unravel"),
                                        # new for multiplayer
                                        (player_get_gold, ":gold", ":player"),
                                        (val_add, ":gold", 10),
                                        (player_set_gold, ":player", ":gold", 15000),
                                        # end
                                (try_end),
                            (else_try),
                            (eq, ":teammate_active_effect", 3),

                                (agent_get_position, pos2, ":nearest_affected_ally"),
                
                                (try_begin),
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 25),
                                        #(agent_set_slot, ":nearest_affected_ally", slot_agent_on_fire, 0),
                                        (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":nearest_affected_ally", slot_agent_on_fire, 0),
                                        (particle_system_burst, "psys_unravel_aura", pos2, 50),
                                        #(play_sound, "snd_unravel"),
                                        (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_unravel"),
                                        # new for multiplayer
                                        (player_get_gold, ":gold", ":player"),
                                        (val_add, ":gold", 5),
                                        (player_set_gold, ":player", ":gold", 15000),
                                        # end
                                (try_end),
                            (else_try),
                            (eq, ":teammate_active_effect", 4),

                                (agent_get_position, pos2, ":nearest_affected_ally"),
                
                                (try_begin),
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 25),
                                        #(agent_set_slot, ":nearest_affected_ally", slot_agent_is_bound, 0),
                                        (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":nearest_affected_ally", slot_agent_is_bound, 0),
                                        (particle_system_burst, "psys_unravel_aura", pos2, 50),
                                        #(play_sound, "snd_unravel"),
                                        (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_unravel"),
                                        # new for multiplayer
                                        (player_get_gold, ":gold", ":player"),
                                        (val_add, ":gold", 5),
                                        (player_set_gold, ":player", ":gold", 15000),
                                        # end
                                (try_end),
                            (try_end),
                        (else_try),
                        (neg|agent_is_non_player, ":chosen"),
                            (display_message, "@No active weaves to unravel..."),
                        (try_end),

                    (try_end),
                        
                    # End Unravel Weave


#########################################  Weave 6
                (else_try),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 6),
                # end
                    # Defensive Blast Weave
                    (assign, ":stamina_cost", 2800),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end

                        (try_for_agents,":agent"),
                            (agent_is_alive,":agent"), ## don't hurt dead
                            (neg|agent_is_wounded,":agent"), ## don't hurt wounded
#                            (neg|agent_is_ally,":agent"), ## don't hurt allies
                            (neq,":chosen",":agent"), ## don't hurt self
                            (neq, ":chosen_horse", ":agent"),
                            (agent_get_look_position, pos2, ":agent"),
                            (get_distance_between_positions,":dist",pos1,pos2),
                            (store_agent_hit_points,":target_health",":agent",1),
                    
                            (try_begin),
                            (lt,":dist",750),

                                #(agent_set_slot, ":agent", slot_agent_is_airborne, 1),
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_is_airborne, 1),

                                (position_get_x, ":attacker_x", pos1),
                                (position_get_y, ":attacker_y", pos1),
                                (position_get_x, ":target_x", pos2),
                                (position_get_y, ":target_y", pos2),

                                (store_sub, ":run", ":target_x", ":attacker_x"),
                                (store_sub, ":rise", ":target_y", ":attacker_y"),

                                #(agent_set_slot, ":agent", slot_agent_airborne_x_movement, ":run"),
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_airborne_x_movement, ":run"),
                                #(agent_set_slot, ":agent", slot_agent_airborne_y_movement, ":rise"),
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_airborne_y_movement, ":rise"),

                                (get_distance_between_positions, ":dist_from_chosen", pos1, pos2),
                                (try_begin),
                                (lt, ":dist_from_chosen", 100),
                                    #(agent_set_slot, ":agent", slot_agent_airborne_power_factor, 20),
                                    (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_airborne_power_factor, 20),
                                (else_try),
                                (is_between, ":dist_from_chosen", 100, 250),
                                    #(agent_set_slot, ":agent", slot_agent_airborne_power_factor, 15),
                                    (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_airborne_power_factor, 15),
                                (else_try),
                                (is_between, ":dist_from_chosen", 250, 450),
                                    #(agent_set_slot, ":agent", slot_agent_airborne_power_factor, 10),
                                    (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_airborne_power_factor, 10),
                                (else_try),
                                (is_between, ":dist_from_chosen", 450, 750),
                                    #(agent_set_slot, ":agent", slot_agent_airborne_power_factor, 5),
                                    (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_airborne_power_factor, 5),
                                (try_end),
                            (try_end),

                            (try_begin),
                            (lt, ":dist", 400),
                                (try_begin),
                                    (gt,":target_health",15),
                                    (val_sub,":target_health",15),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                (try_end),
                            (else_try),
                            (is_between,":dist",400,700),
                                (try_begin),
                                    (gt,":target_health",10),
                                    (val_sub,":target_health",10),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                (try_end),
                            (try_end),
                        (try_end),

                        (particle_system_burst, "psys_massive_pistol_smoke", pos1, 25),
                        #(play_sound, "snd_explosion"),
                        (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_explosion"),

                    (try_end),
                        
                    # End Defensive Blast Weave


################################## Weave 7
                (else_try),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 7),
                # end
                    # Ranged Earth Blast
                    (assign, ":stamina_cost", 3100),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end

                        (assign, ":times_near_ground", 0),
                        (assign, ":near_enemy", 0),

                        (try_for_range,reg5,1,1000),  ###was 500
                        (eq, ":times_near_ground", 0),
                            (particle_system_burst, "psys_dust_blast", pos1, 10),
                            (position_move_y,pos1,20),
                            (copy_position,pos2,pos1),
                            (position_set_z_to_ground_level, pos2),
                            (get_distance_between_positions,":dist",pos1,pos2),

                            (position_get_z, ":z_ground", pos2),
                            (store_add, ":z_ground_low", ":z_ground", 20),
                            (store_add, ":z_ground_high", ":z_ground", 200),

                            (try_for_agents, ":agent"),
                            (eq, ":near_enemy", 0),
                                (neq, ":chosen", ":agent"),
                                (neq, ":chosen_horse", ":agent"),
                                (agent_get_team, ":agent_team", ":agent"),
                                (teams_are_enemies, ":chosen_team", ":agent_team"),
                                (agent_is_alive, ":agent"),
                                (neg|agent_is_wounded, ":agent"),
                                (agent_get_look_position, pos4, ":agent"),
                                (get_distance_between_positions, ":dist_2", pos2, pos4),
                                (position_get_z, ":z_attack_trail", pos1),
                                (lt, ":dist_2", 50), # near agent (x-y)
                                (is_between, ":z_attack_trail", ":z_ground_low", ":z_ground_high"), # within the agent's body (z height)
                                (assign, ":dist", 5),
                                (assign, ":near_enemy", 1),
                            (try_end),
                    
                            (try_begin),
                            (lt,":dist",10),
                                (val_add, ":times_near_ground", 1),
                                (particle_system_burst, "psys_earthquake", pos1, 25),  # effect needs a long duration
                                #(play_sound,"snd_explosion"),
                                (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_explosion"),
                                (copy_position, pos3, pos1),
                                #(scene_prop_get_instance,":instance", "spr_snowy_heap_a", 0),  #need
                                #(position_copy_origin,pos2,pos1),
                                #(prop_instance_set_position,":instance",pos2),
                                (assign,reg5,2000),  #was 1000
                            (try_end),
                        (try_end),
                    
                        (try_for_agents,":agent"),
                            (neq,":chosen",":agent"), ## added this to avoid affecting shooter
                            (neq, ":chosen_horse", ":agent"),
#                            (neg|agent_is_ally,":agent"), ## add this to avoid hurting allies
                            (agent_is_alive,":agent"), ## add this to not affect dead people
                            (neg|agent_is_wounded,":agent"), ## add this to not affect wounded people
                            (agent_get_position,pos2,":agent"),
                            (get_distance_between_positions,":dist",pos3,pos2),
                            (store_agent_hit_points,":target_health",":agent",1),
                    
                            (try_begin),
                            (lt,":dist",750),

                                #(agent_set_slot, ":agent", slot_agent_is_airborne, 1),
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_is_airborne, 1),

                                (position_get_x, ":attacker_x", pos1),
                                (position_get_y, ":attacker_y", pos1),
                                (position_get_x, ":target_x", pos2),
                                (position_get_y, ":target_y", pos2),

                                (store_sub, ":run", ":target_x", ":attacker_x"),
                                (store_sub, ":rise", ":target_y", ":attacker_y"),

                                #(agent_set_slot, ":agent", slot_agent_airborne_x_movement, ":run"),
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_airborne_x_movement, ":run"),
                                #(agent_set_slot, ":agent", slot_agent_airborne_y_movement, ":rise"),
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_airborne_y_movement, ":rise"),

                                (get_distance_between_positions, ":dist_from_chosen", pos1, pos2),
                                (try_begin),
                                (lt, ":dist_from_chosen", 100),
                                    #(agent_set_slot, ":agent", slot_agent_airborne_power_factor, 20),
                                    (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_airborne_power_factor, 20),
                                (else_try),
                                (is_between, ":dist_from_chosen", 100, 250),
                                    #(agent_set_slot, ":agent", slot_agent_airborne_power_factor, 15),
                                    (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_airborne_power_factor, 15),
                                (else_try),
                                (is_between, ":dist_from_chosen", 250, 450),
                                    #(agent_set_slot, ":agent", slot_agent_airborne_power_factor, 10),
                                    (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_airborne_power_factor, 10),
                                (else_try),
                                (is_between, ":dist_from_chosen", 450, 750),
                                    #(agent_set_slot, ":agent", slot_agent_airborne_power_factor, 5),
                                    (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_airborne_power_factor, 5),
                                (try_end),
                            (try_end),

                            (try_begin),
                            (lt, ":dist", 100),
                                (try_begin),
                                    (gt,":target_health",15),
                                    (val_sub,":target_health",15),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                (try_end),
                            (else_try),
                            (is_between,":dist",100,250),
                                (try_begin),
                                    (gt,":target_health",10),
                                    (val_sub,":target_health",10),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                (try_end),
                            (try_end),
                            (else_try),
                            (is_between,":dist",250,450),
                                (try_begin),
                                    (gt,":target_health",6),
                                    (val_sub,":target_health",6),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                (try_end),
                            (else_try),
                            (is_between,":dist",450,750),
                                (try_begin),
                                    (gt,":target_health",3),
                                    (val_sub,":target_health",3),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                (try_end),
                        (try_end),

                    (try_end),
                                                
                    #End Ranged Earth Blast


#########################################  Weave 8
                (else_try),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 8),
                # end
                    # Bind Weave (attempt to bind nearest enemy)
                    (assign, ":stamina_cost", 3600),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end

                        (assign, ":distance",99999),
                        (assign, ":number_of_enemies", 0),

                        (try_for_agents,":agent"),
                            (agent_is_alive,":agent"), ## don't bind dead
                            (neg|agent_is_wounded,":agent"), ## don't bind wounded
                            (agent_is_human,":agent"), ## don't bind horses
                            (neg|agent_is_ally,":agent"), ## don't bind allies
                            (neq, ":chosen", ":agent"), ## shooter can't bind self
                            (agent_get_slot, ":already_bound", ":agent", slot_agent_is_bound),
                            (eq, ":already_bound", 0),
                            (agent_get_look_position, pos2, ":agent"),
                            (get_distance_between_positions,":dist",pos1,pos2),
                            (lt,":dist",":distance"),
                            (assign,":target",":agent"),
                            (assign,":distance",":dist"),
                            (val_add, ":number_of_enemies", 1),
                        (try_end),

                        (try_begin),
                        (ge, ":number_of_enemies", 1),
                            (agent_get_slot, ":target_is_channeler", ":target", slot_agent_is_channeler),
                            (agent_get_slot, ":target_is_shielded", ":target", slot_agent_is_shielded),
                    
                            (try_begin),
                            (eq, ":target_is_channeler", 1),  # harder to bind channelers
                            (eq, ":target_is_shielded", 0),  # unless they are shielded
                    
                                (try_begin),
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 50),
                                        (agent_get_look_position, pos3, ":target"),
                                        (position_get_x, ":target_x", pos3),
                                        (position_get_y, ":target_y", pos3),
                                        # set slots
                                        #(agent_set_slot, ":target", slot_agent_is_bound, 1),
                                        (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":target", slot_agent_is_bound, 1),
                                        #(agent_set_slot, ":target", slot_agent_bound_by, ":chosen"),
                                        (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":target", slot_agent_bound_by, ":chosen"),
                                        #(agent_set_slot, ":target", slot_agent_bound_x, ":target_x"),
                                        (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":target", slot_agent_bound_x, ":target_x"),
                                        #(agent_set_slot, ":target", slot_agent_bound_y, ":target_y"),
                                        (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":target", slot_agent_bound_y, ":target_y"),
                                        #(agent_set_slot, ":target", slot_agent_bound_duration, 10),
                                        (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":target", slot_agent_bound_duration, 10),
                                (try_end),
                    
                            (else_try),
                                (agent_get_look_position, pos3, ":target"),
                                (position_get_x, ":target_x", pos3),
                                (position_get_y, ":target_y", pos3),
                                # set slots
                                #(agent_set_slot, ":target", slot_agent_is_bound, 1),
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":target", slot_agent_is_bound, 1),
                                #(agent_set_slot, ":target", slot_agent_bound_by, ":chosen"),
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":target", slot_agent_bound_by, ":chosen"),
                                #(agent_set_slot, ":target", slot_agent_bound_x, ":target_x"),
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":target", slot_agent_bound_x, ":target_x"),
                                #(agent_set_slot, ":target", slot_agent_bound_y, ":target_y"),
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":target", slot_agent_bound_y, ":target_y"),
                                #(agent_set_slot, ":target", slot_agent_bound_duration, 10),
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":target", slot_agent_bound_duration, 10),
                            (try_end),

                            #(play_sound, "snd_man_grunt_long"),
                            (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_man_grunt_long"),

                        (try_end),

                    (try_end),

                    # End Bind Weave


################################## Weave 9
                (else_try),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 9),
                # end
                    #Chain Lightning Weave
                    (assign, ":stamina_cost", 4300),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end

                        (assign, ":victim_1", 0),
                        (assign, ":victim_2", 0),
                        (assign, ":victim_3", 0),
                        (assign, ":victim_4", 0),
                        (assign, ":victim_5", 0),
                        (assign, ":victim_6", 0),
                        (assign, ":victim_7", 0),
                        (assign, ":victim_8", 0),

                        (assign, ":times_near_ground", 0),
                        (assign, ":near_enemy", 0),

                        (try_for_range,reg5,1,1000),  ###was 500
                        (eq, ":times_near_ground", 0),
                            (particle_system_burst, "psys_electricity_blast", pos1, 10),
                            (position_move_y,pos1,20),
                            (copy_position,pos2,pos1),
                            (position_set_z_to_ground_level, pos2),
                            (get_distance_between_positions,":dist",pos1,pos2),

                            (position_get_z, ":z_ground", pos2),
                            (store_add, ":z_ground_low", ":z_ground", 20),
                            (store_add, ":z_ground_high", ":z_ground", 200),

                            (try_for_agents, ":agent"),
                            (eq, ":near_enemy", 0),
                                (neq, ":chosen", ":agent"),
                                (neq, ":chosen_horse", ":agent"),
                                (agent_get_team, ":agent_team", ":agent"),
                                (teams_are_enemies, ":chosen_team", ":agent_team"),
                                (agent_is_alive, ":agent"),
                                (neg|agent_is_wounded, ":agent"),
                                (agent_get_look_position, pos4, ":agent"),
                                (get_distance_between_positions, ":dist_2", pos2, pos4),
                                (position_get_z, ":z_attack_trail", pos1),
                                (lt, ":dist_2", 50), # near agent (x-y)
                                (is_between, ":z_attack_trail", ":z_ground_low", ":z_ground_high"), # within the agent's body (z height)
                                (assign, ":dist", 5),
                                (assign, ":near_enemy", 1),
                            (try_end),
                    
                            (try_begin),
                            (lt,":dist",10),
                                (val_add, ":times_near_ground", 1),
                                (particle_system_burst, "psys_electricity_sparks", pos1, 25),
                                #(play_sound,"snd_chain_lightning"), # need a sound for freeze
                                (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_chain_lightning"),
                                (copy_position, pos3, pos1),
                                #(scene_prop_get_instance,":instance", "spr_snowy_heap_a", 0),  #need
                                #(position_copy_origin,pos2,pos1),
                                #(prop_instance_set_position,":instance",pos2),
                                (assign,reg5,2000),  #was 1000
                            (try_end),
                        (try_end),

                        (try_for_range, ":counter", 1, 8),
                            (assign, ":distance", 99999),
                            (assign, ":number_near_blast", 0),
                        ## Look for agents near initial strike zone
                            (try_for_agents,":agent"),
                                (neq,":chosen",":agent"), ## added this to avoid shocking shooter
                                (neq, ":chosen_horse", ":agent"),
#                                (neg|agent_is_ally,":agent"), ## add this to avoid shocking allies
                                (agent_is_alive,":agent"), ## add this to not shock dead people
                                (neg|agent_is_wounded,":agent"), ## add this to not shock wounded people
                                (agent_get_slot, ":already_shocked", ":agent", slot_agent_has_been_shocked),
                                (eq, ":already_shocked", 0),
                                (agent_get_position,pos2,":agent"),
                                (get_distance_between_positions,":dist",pos3,pos2),
                                (lt,":dist",":distance"),
                                    (assign,":agent_closest_to_blast",":agent"),
                                    (assign,":distance",":dist"),
                                    (val_add, ":number_near_blast", 1),
                            (try_end),

                            (try_begin), # apply charge if agent close enough
                            (ge, ":number_near_blast", 1),
                            (lt, ":dist", 1500),
                                (store_agent_hit_points,":target_health",":agent_closest_to_blast",1),

                                (try_begin),
                                (is_between, ":counter", 1, 3),
                                    (try_begin),
                                    (gt, ":target_health", 15),
                                        (val_sub,":target_health",15),
                                        (agent_set_hit_points,":agent_closest_to_blast",":target_health",1),
                                        (agent_deliver_damage_to_agent,":chosen",":agent_closest_to_blast"),
                                    (else_try),
                                        (agent_set_hit_points,":agent_closest_to_blast",0,0),
                                        (agent_deliver_damage_to_agent,":chosen",":agent_closest_to_blast"),
                                    (try_end),
                                (else_try),
                                (is_between, ":counter", 3, 5),
                                    (try_begin),
                                    (gt, ":target_health", 12),
                                        (val_sub,":target_health",12),
                                        (agent_set_hit_points,":agent_closest_to_blast",":target_health",1),
                                        (agent_deliver_damage_to_agent,":chosen",":agent_closest_to_blast"),
                                    (else_try),
                                        (agent_set_hit_points,":agent_closest_to_blast",0,0),
                                        (agent_deliver_damage_to_agent,":chosen",":agent_closest_to_blast"),
                                    (try_end),
                                (else_try),
                                (is_between, ":counter", 5, 7),
                                    (try_begin),
                                    (gt, ":target_health", 9),
                                        (val_sub,":target_health",9),
                                        (agent_set_hit_points,":agent_closest_to_blast",":target_health",1),
                                        (agent_deliver_damage_to_agent,":chosen",":agent_closest_to_blast"),
                                    (else_try),
                                        (agent_set_hit_points,":agent_closest_to_blast",0,0),
                                        (agent_deliver_damage_to_agent,":chosen",":agent_closest_to_blast"),
                                    (try_end),
                                (else_try),
                                (is_between, ":counter", 7, 9),
                                    (try_begin),
                                    (gt, ":target_health", 6),
                                        (val_sub,":target_health",6),
                                        (agent_set_hit_points,":agent_closest_to_blast",":target_health",1),
                                        (agent_deliver_damage_to_agent,":chosen",":agent_closest_to_blast"),
                                    (else_try),
                                        (agent_set_hit_points,":agent_closest_to_blast",0,0),
                                        (agent_deliver_damage_to_agent,":chosen",":agent_closest_to_blast"),
                                    (try_end),
                                (try_end),
                    

                                # set victim slots
                                #(agent_set_slot, ":agent_closest_to_blast", slot_agent_has_been_shocked, 1),
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent_closest_to_blast", slot_agent_has_been_shocked, 1),

                                (try_begin),
                                (eq, ":counter", 1),
                                    (assign, ":victim_1", ":agent_closest_to_blast"),
                                (else_try),
                                (eq, ":counter", 2),
                                    (assign, ":victim_2", ":agent_closest_to_blast"),
                                (else_try),
                                (eq, ":counter", 3),
                                    (assign, ":victim_3", ":agent_closest_to_blast"),
                                (else_try),
                                (eq, ":counter", 4),
                                    (assign, ":victim_4", ":agent_closest_to_blast"),
                                (else_try),
                                (eq, ":counter", 5),
                                    (assign, ":victim_5", ":agent_closest_to_blast"),
                                (else_try),
                                (eq, ":counter", 6),
                                    (assign, ":victim_6", ":agent_closest_to_blast"),
                                (else_try),
                                (eq, ":counter", 7),
                                    (assign, ":victim_7", ":agent_closest_to_blast"),
                                (else_try),
                                (eq, ":counter", 8),
                                    (assign, ":victim_8", ":agent_closest_to_blast"),
                                (end_try),

                                # calculate blast travel
                                (agent_get_position, pos2, ":agent_closest_to_blast"),
                                (position_get_x, ":x_end", pos2),
                                (position_get_y, ":y_end", pos2),
                                (position_get_z, ":z_end", pos2),
                                (val_add, ":z_end", 1250),

                                (position_get_x, ":x_start", pos3),
                                (position_get_y, ":y_start", pos3),
                                (position_get_z, ":z_start", pos3),
                    
                                (try_begin),
                                (gt, ":counter", 1),
                                    (val_add, ":z_start", 1250),
                                (try_end),

                                (store_sub, ":run", ":x_end", ":x_start"),
                                (store_sub, ":rise", ":y_end", ":y_start"),
                                (store_sub, ":vert", ":z_end", ":z_start"),

                                (assign, ":interval", 60),

                                (val_div, ":run", ":interval"),
                                (val_div, ":rise", ":interval"),
                                (val_div, ":vert", ":interval"),

                                (try_for_range, ":unused", 0, ":interval"),
                                    (val_add, ":x_start", ":run"),
                                    (val_add, ":y_start", ":rise"),
                                    (val_add, ":z_start", ":vert"),

                                    (position_set_x, pos3, ":x_start"),
                                    (position_set_y, pos3, ":y_start"),
                                    (position_set_z, pos3, ":z_start"),

                                    (particle_system_burst, "psys_electricity_blast", pos3, 10),
                                (try_end),
                    
                                (particle_system_burst, "psys_electricity_sparks", pos2, 25),

                                (copy_position, pos3, pos2),
                    
                            (try_end),

                        # reset victim slots
                        (try_end),

                        (try_begin),
                        (neq, ":victim_1", 0),
                            #(agent_set_slot, ":victim_1", slot_agent_has_been_shocked, 0),
                            (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":victim_1", slot_agent_has_been_shocked, 0),
                        (try_end),

                        (try_begin),
                        (neq, ":victim_2", 0),
                            #(agent_set_slot, ":victim_2", slot_agent_has_been_shocked, 0),
                            (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":victim_2", slot_agent_has_been_shocked, 0),
                        (try_end),

                        (try_begin),
                        (neq, ":victim_3", 0),
                            #(agent_set_slot, ":victim_3", slot_agent_has_been_shocked, 0),
                            (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":victim_3", slot_agent_has_been_shocked, 0),
                        (try_end),

                        (try_begin),
                        (neq, ":victim_4", 0),
                            #(agent_set_slot, ":victim_4", slot_agent_has_been_shocked, 0),
                            (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":victim_4", slot_agent_has_been_shocked, 0),
                        (try_end),

                        (try_begin),
                        (neq, ":victim_5", 0),
                            #(agent_set_slot, ":victim_5", slot_agent_has_been_shocked, 0),
                            (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":victim_5", slot_agent_has_been_shocked, 0),
                        (try_end),

                        (try_begin),
                        (neq, ":victim_6", 0),
                            #(agent_set_slot, ":victim_6", slot_agent_has_been_shocked, 0),
                            (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":victim_6", slot_agent_has_been_shocked, 0),
                        (try_end),

                        (try_begin),
                        (neq, ":victim_7", 0),
                            #(agent_set_slot, ":victim_7", slot_agent_has_been_shocked, 0),
                            (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":victim_7", slot_agent_has_been_shocked, 0),
                        (try_end),

                        (try_begin),
                        (neq, ":victim_8", 0),
                            #(agent_set_slot, ":victim_8", slot_agent_has_been_shocked, 0),
                            (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":victim_8", slot_agent_has_been_shocked, 0),
                        (try_end),

                    (try_end),
                    
                    #Chain Lightening end


#########################################  Weave 10
                (else_try),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 10),
                # end
                    # Fire Curtain Weave
                    (assign, ":stamina_cost", 5100),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end
                    
                         (agent_get_position,pos1,":chosen"),
                    
                         (position_move_y,pos1,1000),  # how far out the flame wall is  (was 500)
                         #(play_sound,"snd_fire_curtain"),
                         (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_fire_curtain"),
                         (assign,":mul",1),
                         (try_for_range,":num",1,16),  # was (try_for_range,":num",1,11),
                            (val_mul,":num",":mul"),
                            (val_mul,":num",300),      # was (val_mul,":num",200),  # is how wide the flame wall is
                            (position_move_x,pos1,":num"),
                            (particle_system_burst,"psys_massive_fire",pos1,125),  #was 75  (this number is the duration
                            (try_for_agents,":agent"),
                                (neq,":chosen",":agent"), ### added this to avoid killing shooter
                                (neq, ":chosen_horse", ":agent"),
#                                (neg|agent_is_ally,":agent"),## added this to avoid killing allies
                                (agent_is_alive,":agent"), ## add this to not re-kill dead people
                                (neg|agent_is_wounded,":agent"), ## add this to not re-kill wounded people
                                (agent_get_position,pos2,":agent"),
                                (get_distance_between_positions,":dist",pos1,pos2),
                    
                                # instant kill if fire curtain within 50 of agent
                                (try_begin),
                                (lt,":dist",50),  #was 300
                                        (agent_set_hit_points,":agent",0,0),
                                        (agent_deliver_damage_to_agent,":chosen",":agent"),
                                # do 25 damage if fire curtain within 50 to 100 of agent
                                (else_try),
                                    (is_between,":dist",50, 100),  #was 300
                                    (store_agent_hit_points,":target_health",":agent",1),
                                    (try_begin),
                                        (gt,":target_health",25),
                                        (val_sub,":target_health",25),
                                        (agent_set_hit_points,":agent",":target_health",1),
                                        (agent_deliver_damage_to_agent,":chosen",":agent"),
                                        #(agent_set_slot, ":agent", slot_agent_on_fire, 1),
                                        (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_on_fire, 1),
                                        #(agent_set_slot, ":agent", slot_agent_fire_starter, ":chosen"),
                                        (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_fire_starter, ":chosen"),
                                        #(agent_set_slot, ":agent", slot_agent_fire_duration, 20),
                                        (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_fire_duration, 20),
                                    (else_try),
                                        (agent_set_hit_points,":agent",0,0),
                                        (agent_deliver_damage_to_agent,":chosen",":agent"),
                                        (position_get_z, ":z_temp", pos2),
                                        (val_add, ":z_temp", 300),
                                        (position_set_z, pos2, ":z_temp"),
                                        #(particle_system_burst, "psys_torch_fire", pos2, 100),
                                    (try_end),
                                # do 15 damage if fire curtain within 100 to 200 of agent
                                (else_try),
                                    (is_between,":dist",100,200),  #was 300
                                    (store_agent_hit_points,":target_health",":agent",1),
                                    (try_begin),
                                        (gt,":target_health",15),
                                        (val_sub,":target_health",15),
                                        (agent_set_hit_points,":agent",":target_health",1),
                                        (agent_deliver_damage_to_agent,":chosen",":agent"),
                                        #(agent_set_slot, ":agent", slot_agent_on_fire, 1),
                                        (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_on_fire, 1),
                                        #(agent_set_slot, ":agent", slot_agent_fire_starter, ":chosen"),
                                        (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_fire_starter, ":chosen"),
                                        #(agent_set_slot, ":agent", slot_agent_fire_duration, 15),
                                        (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_fire_duration, 15),
                                    (else_try),
                                        (agent_set_hit_points,":agent",0,0),
                                        (agent_deliver_damage_to_agent,":chosen",":agent"),
                                        (position_get_z, ":z_temp", pos2),
                                        (val_add, ":z_temp", 300),
                                        (position_set_z, pos2, ":z_temp"),
                                        #(particle_system_burst, "psys_torch_fire", pos2, 100),
                                    (try_end),
                                # do 10 damage if fire curtain within 200 to 300 of agent
                                (else_try),
                                    (is_between,":dist",200,300),  #was 300
                                    (store_agent_hit_points,":target_health",":agent",1),
                                    (try_begin),
                                        (gt,":target_health",10),
                                        (val_sub,":target_health",10),
                                        (agent_set_hit_points,":agent",":target_health",1),
                                        (agent_deliver_damage_to_agent,":chosen",":agent"),
                                        #(agent_set_slot, ":agent", slot_agent_on_fire, 1),
                                        (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_on_fire, 1),
                                        #(agent_set_slot, ":agent", slot_agent_fire_starter, ":chosen"),
                                        (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_fire_starter, ":chosen"),
                                        #(agent_set_slot, ":agent", slot_agent_fire_duration, 10),
                                        (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_fire_duration, 10),
                                    (else_try),
                                        (agent_set_hit_points,":agent",0,0),
                                        (agent_deliver_damage_to_agent,":chosen",":agent"),
                                        (position_get_z, ":z_temp", pos2),
                                        (val_add, ":z_temp", 300),
                                        (position_set_z, pos2, ":z_temp"),
                                        #(particle_system_burst, "psys_torch_fire", pos2, 100),
                                    (try_end),
                                # do 5 damage if fire curtain within 300 to 400 of agent
                                (else_try),
                                    (is_between,":dist",300,400),  #was 300
                                    (store_agent_hit_points,":target_health",":agent",1),
                                    (try_begin),
                                        (gt,":target_health",5),
                                        (val_sub,":target_health",5),
                                        (agent_set_hit_points,":agent",":target_health",1),
                                        (agent_deliver_damage_to_agent,":chosen",":agent"),
                                        #(agent_set_slot, ":agent", slot_agent_on_fire, 1),
                                        (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_on_fire, 1),
                                        #(agent_set_slot, ":agent", slot_agent_fire_starter, ":chosen"),
                                        (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_fire_starter, ":chosen"),
                                        #(agent_set_slot, ":agent", slot_agent_fire_duration, 5),
                                        (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_fire_duration, 5),
                                    (else_try),
                                        (agent_set_hit_points,":agent",0,0),
                                        (agent_deliver_damage_to_agent,":chosen",":agent"),
                                        (position_get_z, ":z_temp", pos2),
                                        (val_add, ":z_temp", 300),
                                        (position_set_z, pos2, ":z_temp"),
                                        #(particle_system_burst, "psys_torch_fire", pos2, 100),
                                    (try_end),
                                (try_end),
                    
                            (try_end),
                            (val_mul,":mul",-1),
                        (try_end),

                    (try_end),

                    # End Fire Curtain Weave


#########################################  Weave 11
                (else_try),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 11),
                # end
                    # Shield Weave (attempt to shield nearest enemy channeler)
                    (assign, ":stamina_cost", 5800),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end

                        (assign, ":distance",99999),
                        (assign, ":number_of_enemies", 0),

                        (try_for_agents,":agent"),
                            (agent_is_alive,":agent"), ## don't shield dead
                            (neg|agent_is_wounded,":agent"), ## don't shield wounded
                            (agent_is_human,":agent"), ## don't shield horses
                            (neg|agent_is_ally,":agent"), ## don't shield allies
                            (neq, ":chosen", ":agent"), ## shooter can't shield self
                            (agent_get_slot, ":channeler", ":agent", slot_agent_is_channeler),
                            (eq, ":channeler", 1),
                            (agent_get_slot, ":already_shielded", ":agent", slot_agent_is_shielded),
                            (eq, ":already_shielded", 0),
                            (agent_get_look_position, pos2, ":agent"),
                            (get_distance_between_positions,":dist",pos1,pos2),
                            (lt,":dist",":distance"),
                            (assign,":target",":agent"),
                            (assign,":distance",":dist"),
                            (val_add, ":number_of_enemies", 1),
                        (try_end),

                        (try_begin),
                        (ge, ":number_of_enemies", 1),
                    
                            (try_begin),
                                (store_random_in_range, ":random", 1, 100),
                                (gt, ":random", 60),
                                    # set slot
                                    #(agent_set_slot, ":target", slot_agent_is_shielded, 1),
                                    (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":target", slot_agent_is_shielded, 1),
                                    #(agent_set_slot, ":target", slot_agent_shielded_by, ":chosen"),
                                    (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":target", slot_agent_shielded_by, ":chosen"),
                                    #(play_sound, "snd_shield"),  # new sound?
                                    (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_shield"),
                                    # new for multiplayer
                                    (player_get_gold, ":gold", ":player"),
                                    (val_add, ":gold", 10),
                                    (player_set_gold, ":player", ":gold", 15000),
                                    # end
                            (try_end),
                        (try_end),

                    (try_end),

                    # End Shield Weave


#########################################  Weave 12
                (else_try),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 12),
                # end
                    # Seeker Weave
                    (assign, ":stamina_cost", 6600),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end

                        (assign, ":distance",99999),
                        (assign, ":number_of_enemies", 0),

                        (try_for_agents,":agent"),
                            (agent_is_alive,":agent"), ## don't hurt dead
                            (neg|agent_is_wounded,":agent"), ## don't hurt wounded
                            (agent_is_human,":agent"), ## don't hurt horses
                            (neg|agent_is_ally,":agent"), ## don't hurt allies
                            (neq, ":chosen", ":agent"), ## shooter can't hurt self
                            (agent_get_slot, ":already_targeted", ":agent", slot_agent_has_active_seeker),
                            (eq, ":already_targeted", 0),
                            (agent_get_look_position, pos2, ":agent"),
                            (get_distance_between_positions,":dist",pos1,pos2),
                            (lt,":dist",":distance"),
                            (assign,":target",":agent"),
                            (assign,":distance",":dist"),
                            (val_add, ":number_of_enemies", 1),
                        (try_end),

#                    (assign, reg45, ":dist"),
#                    (display_message, "@Target is {reg45} from shooter..."),

                        (try_begin),
                        (ge, ":number_of_enemies", 1),
                        (le, "$g_number_seekers_active_multi", 20),
                            (assign, ":slot_found", 0),
                            (try_begin),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_1_multi", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos31, pos1),  # cur position for seeker 1
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 1, 1, 1, ":target"),
                                (assign, ":slot_found", 1),
                                #(play_sound, "snd_seeker"),
                                (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_2_multi", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos31, pos1),  # cur position for seeker 1
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 2, 1, 1, ":target"),
                                (assign, ":slot_found", 1),
                                #(play_sound, "snd_seeker"),
                                (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_3_multi", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos31, pos1),  # cur position for seeker 1
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 3, 1, 1, ":target"),
                                (assign, ":slot_found", 1),
                                #(play_sound, "snd_seeker"),
                                (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_4_multi", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos31, pos1),  # cur position for seeker 1
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 4, 1, 1, ":target"),
                                (assign, ":slot_found", 1),
                                #(play_sound, "snd_seeker"),
                                (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_5_multi", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos31, pos1),  # cur position for seeker 1
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 5, 1, 1, ":target"),
                                (assign, ":slot_found", 1),
                                #(play_sound, "snd_seeker"),
                                (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_6_multi", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos31, pos1),  # cur position for seeker 1
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 6, 1, 1, ":target"),
                                (assign, ":slot_found", 1),
                                #(play_sound, "snd_seeker"),
                                (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_7_multi", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos31, pos1),  # cur position for seeker 1
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 7, 1, 1, ":target"),
                                (assign, ":slot_found", 1),
                                #(play_sound, "snd_seeker"),
                                (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_8_multi", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos31, pos1),  # cur position for seeker 1
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 8, 1, 1, ":target"),
                                (assign, ":slot_found", 1),
                                #(play_sound, "snd_seeker"),
                                (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_9_multi", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos31, pos1),  # cur position for seeker 1
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 9, 1, 1, ":target"),
                                (assign, ":slot_found", 1),
                                #(play_sound, "snd_seeker"),
                                (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_10_multi", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos31, pos1),  # cur position for seeker 1
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 10, 1, 1, ":target"),
                                (assign, ":slot_found", 1),
                                #(play_sound, "snd_seeker"),
                                (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_11_multi", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos31, pos1),  # cur position for seeker 1
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 11, 1, 1, ":target"),
                                (assign, ":slot_found", 1),
                                #(play_sound, "snd_seeker"),
                                (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_12_multi", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos31, pos1),  # cur position for seeker 1
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 12, 1, 1, ":target"),
                                (assign, ":slot_found", 1),
                                #(play_sound, "snd_seeker"),
                                (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_13_multi", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos31, pos1),  # cur position for seeker 1
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 13, 1, 1, ":target"),
                                (assign, ":slot_found", 1),
                                #(play_sound, "snd_seeker"),
                                (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_14_multi", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos31, pos1),  # cur position for seeker 1
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 14, 1, 1, ":target"),
                                (assign, ":slot_found", 1),
                                #(play_sound, "snd_seeker"),
                                (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_15_multi", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos31, pos1),  # cur position for seeker 1
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 15, 1, 1, ":target"),
                                (assign, ":slot_found", 1),
                                #(play_sound, "snd_seeker"),
                                (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_16_multi", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos31, pos1),  # cur position for seeker 1
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 16, 1, 1, ":target"),
                                (assign, ":slot_found", 1),
                                #(play_sound, "snd_seeker"),
                                (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_17_multi", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos31, pos1),  # cur position for seeker 1
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 17, 1, 1, ":target"),
                                (assign, ":slot_found", 1),
                                #(play_sound, "snd_seeker"),
                                (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_18_multi", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos31, pos1),  # cur position for seeker 1
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 18, 1, 1, ":target"),
                                (assign, ":slot_found", 1),
                                #(play_sound, "snd_seeker"),
                                (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_19_multi", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos31, pos1),  # cur position for seeker 1
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 19, 1, 1, ":target"),
                                (assign, ":slot_found", 1),
                                #(play_sound, "snd_seeker"),
                                (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_20_multi", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos31, pos1),  # cur position for seeker 1
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_seeker_info_to_server, 20, 1, 1, ":target"),
                                (assign, ":slot_found", 1),
                                #(play_sound, "snd_seeker"),
                                (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_seeker"),
                            (try_end),
                        (else_try),
                        (ge, ":number_of_enemies", 1),
                        (eq, "$g_number_seekers_active_multi", 20),
                            (display_message, "@Too many active seekers!!"), 
                        (try_end),

                    (try_end),
                        
                    # End Seeker Weave


#########################################  Weave 13
                (else_try),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 13),
                # end
                    # Compulsion Weave
                    (assign, ":stamina_cost", 7300),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end

                        (assign, ":distance",99999),
                        (assign, ":number_of_enemies", 0),

                        (try_for_agents,":agent"),
                            (agent_is_alive,":agent"), ## don't compel dead
                            (neg|agent_is_wounded,":agent"), ## don't compel wounded
                            (agent_is_human,":agent"), ## don't compel horses
                            (neg|agent_is_ally,":agent"), ## don't compel allies
                            (neq, ":chosen", ":agent"), ## shooter can't compel self
                            (get_player_agent_no,":player_agent"),
                            (neq, ":agent", ":player_agent"), ## shooter can't compel player (too many complications)
                            (agent_get_slot, ":already_compelled", ":agent", slot_agent_under_compulsion),
                            (eq, ":already_compelled", 0),
                            (agent_get_look_position, pos2, ":agent"),
                            (get_distance_between_positions,":dist",pos1,pos2),
                            (lt,":dist",":distance"),
                            (assign,":target",":agent"),
                            (assign,":distance",":dist"),
                            (val_add, ":number_of_enemies", 1),
                        (try_end),

                        (try_begin),
                        (ge, ":number_of_enemies", 1),

                            (agent_get_slot, ":channeler", ":agent", slot_agent_is_channeler),

                            (agent_get_team, ":chosen_team", ":chosen"),
                            (agent_get_team, ":target_team", ":target"),
            
                            (try_begin),
                            (agent_is_non_player), # run this for bots
                    
                                (try_begin),
                                (eq, ":channeler", 1), # target is channeler
                                    (try_begin),
                                        (store_random_in_range, ":random", 1, 100),
                                        (gt, ":random", 60),
                                            (agent_set_team, ":target", ":chosen_team"),
                                            (agent_clear_scripted_mode, ":target"),
                    
                                            # set slot
                                            #(agent_set_slot, ":target", slot_agent_under_compulsion, 1),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":target", slot_agent_under_compulsion, 1),
                                            #(agent_set_slot, ":target", slot_agent_compelled_by, ":chosen"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":target", slot_agent_compelled_by, ":chosen"),
                                            #(agent_set_slot, ":target", slot_agent_compelled_start_team, ":target_team"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":target", slot_agent_compelled_start_team, ":target_team"),
    
                                            #(play_sound, "snd_compulsion"),
                                            (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_compulsion"),
                                            # new for multiplayer
                                            (player_get_gold, ":gold", ":player"),
                                            (val_add, ":gold", 10),
                                            (player_set_gold, ":player", ":gold", 15000),
                                            # end
                                    (try_end),
                                (else_try), # target is non-channeler
                                    (try_begin),
                                        (store_random_in_range, ":random", 1, 100),
                                        (gt, ":random", 30),
                                            (agent_set_team, ":target", ":chosen_team"),
                                            (agent_clear_scripted_mode, ":target"),
                    
                                            # set slot
                                            #(agent_set_slot, ":target", slot_agent_under_compulsion, 1),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":target", slot_agent_under_compulsion, 1),
                                            #(agent_set_slot, ":target", slot_agent_compelled_by, ":chosen"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":target", slot_agent_compelled_by, ":chosen"),
                                            #(agent_set_slot, ":target", slot_agent_compelled_start_team, ":target_team"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":target", slot_agent_compelled_start_team, ":target_team"),
    
                                            #(play_sound, "snd_compulsion"),
                                            (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_compulsion"),
                                            # new for multiplayer
                                            (player_get_gold, ":gold", ":player"),
                                            (val_add, ":gold", 10),
                                            (player_set_gold, ":player", ":gold", 15000),
                                            # end
                                    (try_end),
                                (try_end),
            
                            (else_try), # agent is human
            
                                (try_begin),
                                (eq, ":channeler", 1), # target is channeler
                                    (try_begin),
                                        (store_random_in_range, ":random", 1, 100),
                                        (gt, ":random", 60),
                                            # Remove the following two lines for humans
                                            #(agent_set_team, ":target", ":chosen_team"),
                                            #(agent_clear_scripted_mode, ":target"),
                    
                                            # set slot
                                            #(agent_set_slot, ":target", slot_agent_under_compulsion, 1),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":target", slot_agent_under_compulsion, 1),
                                            #(agent_set_slot, ":target", slot_agent_compelled_by, ":chosen"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":target", slot_agent_compelled_by, ":chosen"),
                                            #(agent_set_slot, ":target", slot_agent_compelled_start_team, ":target_team"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":target", slot_agent_compelled_start_team, ":target_team"),
    
                                            #(play_sound, "snd_compulsion"),
                                            (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_compulsion"),
                                            # new for multiplayer
                                            (player_get_gold, ":gold", ":player"),
                                            (val_add, ":gold", 10),
                                            (player_set_gold, ":player", ":gold", 15000),
                                            # end
                                    (try_end),
                                (else_try), # target is non-channeler
                                    (try_begin),
                                        (store_random_in_range, ":random", 1, 100),
                                        (gt, ":random", 30),
                                            # Remove the following two lines for humans
                                            #(agent_set_team, ":target", ":chosen_team"),
                                            #(agent_clear_scripted_mode, ":target"),
                    
                                            # set slot
                                            #(agent_set_slot, ":target", slot_agent_under_compulsion, 1),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":target", slot_agent_under_compulsion, 1),
                                            #(agent_set_slot, ":target", slot_agent_compelled_by, ":chosen"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":target", slot_agent_compelled_by, ":chosen"),
                                            #(agent_set_slot, ":target", slot_agent_compelled_start_team, ":target_team"),
                                            (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":target", slot_agent_compelled_start_team, ":target_team"),
    
                                            #(play_sound, "snd_compulsion"),
                                            (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_compulsion"),
                                            # new for multiplayer
                                            (player_get_gold, ":gold", ":player"),
                                            (val_add, ":gold", 10),
                                            (player_set_gold, ":player", ":gold", 15000),
                                            # end
                                    (try_end),
                                (try_end),
            
                            (try_end),
            
                        (try_end),

                    (try_end),

                    # End Compulsion Weave


################################## Weave 14
                (else_try),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 14),
                # end
                    #Balefire Weave (rip victom from pattern and undo their last actions)
                    (assign, ":stamina_cost", 8100),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end

                        (assign, ":times_near_ground", 0),

                        (try_for_range,reg5,1,1000),  ###was 500
                        (eq, ":times_near_ground", 0),
                            (particle_system_burst, "psys_balefire_beam", pos1, 15), ## need balefire trail
                            (position_move_y,pos1,20),
                            (copy_position,pos2,pos1),
                            (position_set_z_to_ground_level, pos2),
                            (get_distance_between_positions,":dist",pos1,pos2),

                            (position_get_z, ":z_ground", pos2),
                            (store_add, ":z_ground_low", ":z_ground", 20),
                            (store_add, ":z_ground_high", ":z_ground", 200),

                            (try_for_agents, ":agent"),
                                (neq, ":chosen", ":agent"),
                                (neq, ":chosen_horse", ":agent"),
#                                (neg|agent_is_ally, ":agent"),
                                (agent_is_alive, ":agent"),
                                (neg|agent_is_wounded, ":agent"),
                                (agent_get_look_position, pos4, ":agent"),
                                (get_distance_between_positions, ":dist_2", pos2, pos4),
                                (position_get_z, ":z_attack_trail", pos1),
                                (lt, ":dist_2", 50), # balefire must be near the agent (x-y radius)
                                (is_between, ":z_attack_trail", ":z_ground_low", ":z_ground_high"), # balefire must be within the agent's body (z height)
                                #(agent_set_slot, ":agent", slot_agent_hit_by_balefire, 1),
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_hit_by_balefire, 1),
                                #(agent_set_slot, ":agent", slot_agent_balefire_shooter, ":chosen"),
                                (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":agent", slot_agent_balefire_shooter, ":chosen"),
                                (try_for_range, ":unused", 1, 10),
                                    (particle_system_burst, "psys_balefire_strike", pos4, 20),  #need
                                    (position_move_z, pos4, 20),
                                (try_end),
                            (try_end),
                    
                            (try_begin),
                            (lt,":dist",10),
                                (val_add, ":times_near_ground", 1),
                                #(play_sound,"snd_balefire"),
                                (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_balefire"),
                                (copy_position, pos3, pos1),
                                #(scene_prop_get_instance,":instance", "spr_explosion", 0),  #need
                                #(position_copy_origin,pos2,pos1),
                                #(prop_instance_set_position,":instance",pos2),
                                #(position_move_z,pos2,1000),
                                #(prop_instance_animate_to_position,":instance",pos2,175),
                                (assign,reg5,2000),  #was 1000
                            (try_end),
                        (try_end),

                    (try_end),
                                
                    #Balefire weave end


                    
### Be sure to leave this (try_end), at the end of the active weave code
                (try_end),

######################################### Run the "Shield Breaker" code if the channeler is shielded...
            (else_try),
                (agent_get_slot, ":shield_holder", ":chosen", slot_agent_shielded_by),

                (try_begin),
                (agent_is_alive, ":shield_holder"), # shield creator is alive
                (neg|agent_is_wounded, ":shield_holder"),
                    (try_begin),
                        (store_random_in_range, ":random", 1, 100),
                        (gt, ":random", 65),
                            #(agent_set_slot, ":chosen", slot_agent_is_shielded, 0),
                            (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":chosen", slot_agent_is_shielded, 0),
                            #(play_sound, "snd_unravel"),
                            (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_unravel"),
                    (try_end),
                (else_try), # shield creator is dead / wounded
                    (store_random_in_range, ":random", 1, 100),
                    (gt, ":random", 25),
                        #(agent_set_slot, ":chosen", slot_agent_is_shielded, 0),
                        (multiplayer_send_4_int_to_server, multiplayer_event_send_agent_slot_info_to_server, 1, ":chosen", slot_agent_is_shielded, 0),
                        #(play_sound, "snd_unravel"),
                        (multiplayer_send_int_to_server, multiplayer_event_sound_made_by_player, "snd_unravel"),
                (try_end),

#                (store_mod, ":counter", "$g_number_of_weaves_used", 4),
#                (try_begin),
#                (eq, ":counter", 0),
                    (display_message, "@You are shielded..."),
#                (try_end),
                
            # End of Shield Breaker code
                
            (try_end),


#   Counts the number of times the player has used the channeling item
#            (val_add, "$g_number_of_weaves_used", 1),
#            (assign, reg5, "$g_number_of_weaves_used"),
#            (display_message, "@Player has channeled {reg5} times ..."),
#   Warns that the player is almost out of 'ammo'
#            (try_begin),
#            (ge, "$g_number_of_weaves_used", 130),
#                (display_message, "str_almost_out_of_ammo"),
#            (try_end),
#   Displays the player's channeling proficiency modifier
#            (assign, reg4,"$g_channeling_proficiency_modifier"),
#            (display_message, "@Current channeling proficiency modifier is {reg4} ..."),


                         ],),
    ]],


################################################################################ 
#### Backup (Original) version of the multiplayer One Power Item ###############

 ["power_player_multiplayer_backup_original","One Power", [("cuindiar_disc",0),("practice_arrows_2",ixmesh_flying_ammo)],itp_type_pistol|itp_primary|itp_secondary|itp_bonus_against_shield , itcf_shoot_crossbow, 5 , weight(4)|spd_rtng(250) | shoot_speed(150) | thrust_damage(1 ,  pierce)|max_ammo(5000)|weapon_length(65),imodbits_missile,
  [(ti_on_weapon_attack, [

#                    (get_player_agent_no,":player_agent"),

            # new for multiplayer
            (multiplayer_get_my_player, ":player"),
            # end

            (assign,":distance",99999),
                         
            (try_for_agents,":agent"),
                (agent_is_alive,":agent"),
                (neg|agent_is_wounded,":agent"), ## add this to not re-count wounded people
                (agent_is_human,":agent"),
                (agent_get_look_position, pos2, ":agent"), 
                (get_distance_between_positions,":dist",pos1,pos2),
                (lt,":dist",":distance"),
                (assign,":chosen",":agent"), # 'chosen' is the shooter
                (assign,":distance",":dist"),
            (try_end),

            (agent_get_horse, ":chosen_horse", ":chosen"),
            (agent_get_team, ":chosen_team", ":chosen"),

## Run the channeling code only if the channeling agent is not shielded
            (agent_get_slot, ":agent_is_shielded", ":chosen", slot_agent_is_shielded),

            (try_begin),
            (eq, ":agent_is_shielded", 0),

                
################################## Weave 1
                (try_begin),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 1),
                # end
                    #Air Blast (push agent and do a little damage)
                    (assign, ":stamina_cost", 600),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end

                        (copy_position, pos3, pos1),
                        (position_move_y, pos3, 350),
                        (position_set_z_to_ground_level,pos3),
                        
                        (try_for_agents,":agent"),
                            (neq,":chosen",":agent"), ## added this to avoid killing shooter
                            (neq, ":chosen_horse", ":agent"),
#                            (neg|agent_is_ally,":agent"), ## add this to avoid killing allies
                            (agent_is_alive,":agent"), ## add this to not re-kill dead people
                            (neg|agent_is_wounded,":agent"), ## add this to not re-kill wounded people
                            (agent_get_look_position,pos2,":agent"),
                            (get_distance_between_positions,":dist",pos3,pos2),
                            (store_agent_hit_points,":target_health",":agent",1),
                            (lt,":dist",400),

                                (agent_set_slot, ":agent", slot_agent_is_airborne, 1),

                                (position_get_x, ":attacker_x", pos1),
                                (position_get_y, ":attacker_y", pos1),
                                (position_get_x, ":target_x", pos2),
                                (position_get_y, ":target_y", pos2),

                                (store_sub, ":run", ":target_x", ":attacker_x"),
                                (store_sub, ":rise", ":target_y", ":attacker_y"),

                                (agent_set_slot, ":agent", slot_agent_airborne_x_movement, ":run"),
                                (agent_set_slot, ":agent", slot_agent_airborne_y_movement, ":rise"),

                                (get_distance_between_positions, ":dist_from_chosen", pos1, pos2),
                                (try_begin),
                                (lt, ":dist_from_chosen", 100),
                                    (agent_set_slot, ":agent", slot_agent_airborne_power_factor, 8),
                                (else_try),
                                (is_between, ":dist_from_chosen", 100, 250),
                                    (agent_set_slot, ":agent", slot_agent_airborne_power_factor, 6),
                                (else_try),
                                (is_between, ":dist_from_chosen", 250, 450),
                                    (agent_set_slot, ":agent", slot_agent_airborne_power_factor, 4),
                                (else_try),
                                (is_between, ":dist_from_chosen", 450, 750),
                                    (agent_set_slot, ":agent", slot_agent_airborne_power_factor, 2),
                                (try_end),
                                
                                (try_begin),
                                    (gt,":target_health",5),
                                    (val_sub,":target_health",5),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 10),
                                    (try_end),
                                    (add_xp_to_troop,3,":chosen"),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 20),
                                    (try_end),
                                    (add_xp_to_troop,6,":chosen"),
                                (try_end),
                            
                        (try_end),
                        (particle_system_burst, "psys_massive_pistol_smoke", pos1, 25),
                        (play_sound,"snd_air_blast"),
            
                    (try_end),

                # air blast weave end


################################## Weave 2
                (else_try),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 2),
                # end
                    #Freeze Weave
                    (assign, ":stamina_cost", 1000),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end

                        (assign, ":times_near_ground", 0),
                        (assign, ":near_enemy", 0),

                        (try_for_range,reg5,1,1000),  ###was 500
                        (eq, ":times_near_ground", 0),
                            (particle_system_burst, "psys_freeze_blast", pos1, 10),
                            (position_move_y,pos1,20), # was 10
                            (copy_position,pos2,pos1),
                            (position_set_z_to_ground_level, pos2),
                            (get_distance_between_positions,":dist",pos1,pos2),

                            (position_get_z, ":z_ground", pos2),
                            (store_add, ":z_ground_low", ":z_ground", 20), 
                            (store_add, ":z_ground_high", ":z_ground", 200),

                            (try_for_agents, ":agent"),
                            (eq, ":near_enemy", 0),
                                (neq, ":chosen", ":agent"),
                                (neq, ":chosen_horse", ":agent"),
                                (agent_get_team, ":agent_team", ":agent"),
                                (teams_are_enemies, ":chosen_team", ":agent_team"),
                                (agent_is_alive, ":agent"),
                                (neg|agent_is_wounded, ":agent"),
                                (agent_get_look_position, pos4, ":agent"),
                                (get_distance_between_positions, ":dist_2", pos2, pos4),
                                (position_get_z, ":z_attack_trail", pos1),
                                (lt, ":dist_2", 50), # near agent (x-y)
                                (is_between, ":z_attack_trail", ":z_ground_low", ":z_ground_high"), # within the agent's body (z height)
                                (assign, ":dist", 5),
                                (assign, ":near_enemy", 1),
                            (try_end),
                    
                            (try_begin),
                            (lt,":dist",10),
                                (val_add, ":times_near_ground", 1),
                                (particle_system_burst, "psys_tsunami", pos1, 75),  # effect needs a long duration
                                (play_sound,"snd_freeze"), # need a sound for freeze
                                (copy_position, pos3, pos1),
                                (scene_prop_get_instance,":instance", "spr_snowy_heap_a", 0),  #need
                                (position_copy_origin,pos2,pos1),
                                (prop_instance_set_position,":instance",pos2),
                                (assign,reg5,2000),  #was 1000
                            (try_end),
                        (try_end),
                                
                        (try_for_agents,":agent"),
                            (neq,":chosen",":agent"), ## added this to avoid freezing shooter
                            (neq, ":chosen_horse", ":agent"),
#                            (neg|agent_is_ally,":agent"), ## add this to avoid freezing allies
                            (agent_is_alive,":agent"), ## add this to not freeze dead people
                            (neg|agent_is_wounded,":agent"), ## add this to not freeze wounded people
                            (agent_get_position,pos2,":agent"),
                            (get_distance_between_positions,":dist",pos3,pos2),
                         
                            (try_begin),
                            (lt,":dist",250),  # freeze (slowed movement) if blast within 250 of agent
                                (agent_set_speed_limit, ":agent", 0),
                                (agent_deliver_damage_to_agent,":chosen",":agent"),
                                (try_begin), # add to channeling multiplier if agent is player
                                (neg|agent_is_non_player, ":chosen"),
                                    (val_add, "$g_channeling_proficiency_modifier", 80),
                                (try_end),
                                (add_xp_to_troop,40,":chosen"),
                            (try_end),
                    
                        (try_end),
            
                    (try_end),
                            
                    #Freeze weave end


#########################################  Weave 3
                (else_try),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 3),
                # end
                    # Heal Nearest Ally Weave
                    (assign, ":stamina_cost", 1500),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end

                        (assign, ":distance",99999),
                        (assign, ":number_of_allies", 0),

                        (try_for_agents,":agent"),
                            (agent_is_alive,":agent"), ## don't heal dead
                            (neg|agent_is_wounded,":agent"), ## don't heal wounded
                            (agent_is_ally,":agent"), ## don't heal enemies
                            (agent_is_human,":agent"), ## don't look for horses on the first round
                            (neq, ":chosen", ":agent"), ## shooter can't heal self
                            (store_agent_hit_points,":health",":agent",0),
                            (lt,":health",75),
                            (agent_get_look_position, pos2, ":agent"),
                            (get_distance_between_positions,":dist",pos1,pos2),
                            (lt,":dist",":distance"),
                            (assign,":nearest_hurt_ally",":agent"),
                            (assign,":distance",":dist"),
                            (val_add, ":number_of_allies", 1),
                        (try_end),

                        (try_begin),
                        (ge, ":number_of_allies", 1),
                            (agent_set_hit_points,":nearest_hurt_ally",100,0),
                            (agent_get_look_position, pos2, ":nearest_hurt_ally"),
                            (particle_system_burst, "psys_heal_aura", pos2, 50),
                            (play_sound, "snd_heal"),
                            (try_begin), # add to channeling multiplier if agent is player
                            (neg|agent_is_non_player, ":chosen"),
                                (val_add, "$g_channeling_proficiency_modifier", 80),
                            (try_end),
                            (add_xp_to_troop,40,":chosen"),
                        (else_try),
                            (assign, ":distance",99999),
                            (assign, ":number_of_allies", 0),

                            (try_for_agents,":agent"),
                                (agent_is_alive,":agent"), ## don't heal dead
                                (neg|agent_is_wounded,":agent"), ## don't heal wounded
                                (agent_is_ally,":agent"), ## don't heal enemies
                                (neg|agent_is_human,":agent"), ## look for horses on the second round
                                (neq, ":chosen", ":agent"), ## shooter can't heal self
                                (store_agent_hit_points,":health",":agent",0),
                                (lt,":health",75),
                                (agent_get_look_position, pos2, ":agent"),
                                (get_distance_between_positions,":dist",pos1,pos2),
                                (lt,":dist",":distance"),
                                (assign,":nearest_hurt_ally",":agent"),
                                (assign,":distance",":dist"),
                                (val_add, ":number_of_allies", 1),
                            (try_end),

                            (try_begin),
                            (ge, ":number_of_allies", 1),
                                (agent_set_hit_points,":nearest_hurt_ally",100,0),
                                (agent_get_look_position, pos2, ":nearest_hurt_ally"),
                                (particle_system_burst, "psys_heal_aura", pos2, 50),
                                (play_sound, "snd_heal"),
                                (try_begin), # add to channeling multiplier if agent is player
                                (neg|agent_is_non_player, ":chosen"),
                                    (val_add, "$g_channeling_proficiency_modifier", 80),
                                (try_end),
                                (add_xp_to_troop,40,":chosen"),
                            (try_end),
                        (try_end),

                    (try_end),
                        
                    # End Heal Nearest Ally Weave


################################## Weave 4
                (else_try),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 4),
                # end
                    #Fire Ball (do damage based on how close agent is to the blast)
                    (assign, ":stamina_cost", 2100),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end

                        (assign, ":times_near_ground", 0),
                        (assign, ":near_enemy", 0),

                        (try_for_range,reg5,1,1000),  ###was 500
                        (eq, ":times_near_ground", 0),
                            (particle_system_burst, "psys_torch_fire", pos1, 15),
                            (position_move_y,pos1,20),
                            (copy_position,pos2,pos1),
                            (position_set_z_to_ground_level, pos2),
                            (get_distance_between_positions,":dist",pos1,pos2),

                            (position_get_z, ":z_ground", pos2),
                            (store_add, ":z_ground_low", ":z_ground", 20),
                            (store_add, ":z_ground_high", ":z_ground", 200),

                            (try_for_agents, ":agent"),
                            (eq, ":near_enemy", 0),
                                (neq, ":chosen", ":agent"),
                                (neq, ":chosen_horse", ":agent"),
                                (agent_get_team, ":agent_team", ":agent"),
                                (teams_are_enemies, ":chosen_team", ":agent_team"),
                                (agent_is_alive, ":agent"),
                                (neg|agent_is_wounded, ":agent"),
                                (agent_get_look_position, pos4, ":agent"),
                                (get_distance_between_positions, ":dist_2", pos2, pos4),
                                (position_get_z, ":z_attack_trail", pos1),
                                (lt, ":dist_2", 50), # near agent (x-y)
                                (is_between, ":z_attack_trail", ":z_ground_low", ":z_ground_high"), # within the agent's body (z height)
                                (assign, ":dist", 5),
                                (assign, ":near_enemy", 1),
                            (try_end),
                    
                            (try_begin),
                            (lt,":dist",10),
                                (val_add, ":times_near_ground", 1),
                                (particle_system_burst, "psys_massive_fire", pos1, 15),  #need
                                (particle_system_burst, "psys_war_smoke_tall", pos1, 15),  #need
                                (play_sound,"snd_fire_ball"),
                                (copy_position, pos3, pos1),
                                (scene_prop_get_instance,":instance", "spr_explosion", 0),  #need
                                (position_copy_origin,pos2,pos1),
                                (prop_instance_set_position,":instance",pos2),
                                (position_move_z,pos2,1000),
                                (prop_instance_animate_to_position,":instance",pos2,175),
                                (assign,reg5,2000),  #was 1000
                            (try_end),
                        (try_end),
                                
                        (try_for_agents,":agent"),
                            (neq,":chosen",":agent"), ## added this to avoid killing shooter
                            (neq, ":chosen_horse", ":agent"),
#                            (neg|agent_is_ally,":agent"), ## add this to avoid killing allies
                            (agent_is_alive,":agent"), ## add this to not re-kill dead people
                            (neg|agent_is_wounded,":agent"), ## add this to not re-kill wounded people
                            (agent_get_position,pos2,":agent"),
                            (get_distance_between_positions,":dist",pos3,pos2),
                         
                            # do 25 damage if fireball within 50 of agent
                            (try_begin),
                                (lt,":dist",50),  #was 300
                                (store_agent_hit_points,":target_health",":agent",1),
                                (try_begin),
                                    (gt,":target_health",25),
                                    (val_sub,":target_health",25),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 40),
                                    (try_end),
                                    (add_xp_to_troop,20,":chosen"),
                                    (agent_set_slot, ":agent", slot_agent_on_fire, 1),
                                    (agent_set_slot, ":agent", slot_agent_fire_starter, ":chosen"),
                                    (agent_set_slot, ":agent", slot_agent_fire_duration, 20),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 50),
                                    (try_end),
                                    (add_xp_to_troop,25,":chosen"),
                                    (position_get_z, ":z_temp", pos2),
                                    (val_add, ":z_temp", 300),
                                    (position_set_z, pos2, ":z_temp"),
                                    #(particle_system_burst, "psys_torch_fire", pos2, 100),
                                (try_end),
                            # do 15 damage if fireball within 50 to 125 of agent
                            (else_try),
                                (is_between,":dist",50,125),  #was 300
                                (store_agent_hit_points,":target_health",":agent",1),
                                (try_begin),
                                    (gt,":target_health",15),
                                    (val_sub,":target_health",15),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 30),
                                    (try_end),
                                    (add_xp_to_troop,15,":chosen"),
                                    (agent_set_slot, ":agent", slot_agent_on_fire, 1),
                                    (agent_set_slot, ":agent", slot_agent_fire_starter, ":chosen"),
                                    (agent_set_slot, ":agent", slot_agent_fire_duration, 15),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 40),
                                    (try_end),
                                    (add_xp_to_troop,20,":chosen"),
                                    (position_get_z, ":z_temp", pos2),
                                    (val_add, ":z_temp", 300),
                                    (position_set_z, pos2, ":z_temp"),
                                    #(particle_system_burst, "psys_torch_fire", pos2, 100),
                                (try_end),
                            # do 10 damage if fireball within 125 to 225 of agent
                            (else_try),
                                (is_between,":dist",125,225),  #was 300
                                (store_agent_hit_points,":target_health",":agent",1),
                                (try_begin),
                                    (gt,":target_health",10),
                                    (val_sub,":target_health",10),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 20),
                                    (try_end),
                                    (add_xp_to_troop,10,":chosen"),
                                    (agent_set_slot, ":agent", slot_agent_on_fire, 1),
                                    (agent_set_slot, ":agent", slot_agent_fire_starter, ":chosen"),
                                    (agent_set_slot, ":agent", slot_agent_fire_duration, 10),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 30),
                                    (try_end),
                                    (add_xp_to_troop,15,":chosen"),
                                    (position_get_z, ":z_temp", pos2),
                                    (val_add, ":z_temp", 300),
                                    (position_set_z, pos2, ":z_temp"),
                                    #(particle_system_burst, "psys_torch_fire", pos2, 100),
                                (try_end),
                            # do 5 damage if fireball within 225 to 350 of agent
                            (else_try),
                                (is_between,":dist",225,350),  #was 300
                                (store_agent_hit_points,":target_health",":agent",1),
                                (try_begin),
                                    (gt,":target_health",5),
                                    (val_sub,":target_health",5),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 10),
                                    (try_end),
                                    (add_xp_to_troop,5,":chosen"),
                                    (agent_set_slot, ":agent", slot_agent_on_fire, 1),
                                    (agent_set_slot, ":agent", slot_agent_fire_starter, ":chosen"),
                                    (agent_set_slot, ":agent", slot_agent_fire_duration, 5),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 20),
                                    (try_end),
                                    (add_xp_to_troop,10,":chosen"),
                                    (position_get_z, ":z_temp", pos2),
                                    (val_add, ":z_temp", 300),
                                    (position_set_z, pos2, ":z_temp"),
                                    #(particle_system_burst, "psys_torch_fire", pos2, 100),
                                (try_end),
                            (try_end),

                        (try_end),

                    (try_end),
                
                    #Fireball weave end


#########################################  Weave 5
                (else_try),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 5),
                # end
                    # Unravel Weave
                    (assign, ":stamina_cost", 2500),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end

                        (assign, ":chosen_active_effect", 0),
                        (assign, ":chosen_horse_on_fire", 0),
                        (assign, ":teammate_active_effect", 5),
                

                        (agent_get_slot, ":chosen_seeker", ":chosen", slot_agent_has_active_seeker),
                        (try_begin),
                        (eq, ":chosen_seeker", 1),
                            (assign, ":chosen_active_effect", 1),
                
                        (else_try), # chosen doesn't have a seeker
                            (agent_get_slot, ":chosen_fire", ":chosen", slot_agent_on_fire),
                            (try_begin),
                            (eq, ":chosen_fire", 1),
                                (assign, ":chosen_active_effect", 3),
                
                            (else_try), # chosen not on fire
                                (agent_get_slot, ":chosen_bound", ":chosen", slot_agent_is_bound),
                                (try_begin),
                                (eq, ":chosen_bound", 1),
                                    (assign, ":chosen_active_effect", 4),
                
                                (else_try), # chosen not bound
                                    (agent_get_horse, ":chosen_horse", ":chosen"),
                                    (try_begin),
                                    (ge, ":chosen_horse", 0),
                                        (agent_get_slot, ":chosen_horse_fire", ":chosen_horse", slot_agent_on_fire),
                                    (try_end),
                
                                    (try_begin),
                                    (eq, ":chosen_horse_fire", 1),
                                        (assign, ":chosen_horse_on_fire", 1),

                                    (else_try), # chosen horse not on fire
                                        
                                        (try_for_agents,":agent"),
                                            (agent_is_alive,":agent"), ## don't help dead
                                            (neg|agent_is_wounded,":agent"), ## don't help wounded
#                                            (agent_is_human,":agent"), ## don't help horses
                
                                            # determine if agents under compulsion used to be teammates
                                            (agent_get_slot, ":compulsion_present", ":agent", slot_agent_under_compulsion),
                                            (assign, ":agent_ally", 0),
                                            (try_begin),
                                            (eq, ":compulsion_present", 1),
                                                (agent_get_slot, ":original_team", ":agent", slot_agent_compelled_start_team),
                                                (try_begin),
                                                (ge, ":original_team", 0),
                                                (eq, ":original_team", ":chosen_team"), # used to be teammate
                                                    (assign, ":agent_ally", 2),
                                                (else_try),
                                                (agent_is_ally, ":agent"), # teammate by compulsion
                                                    (assign, ":agent_ally", 1),
                                                (try_end),
                                            (else_try),
                                            (agent_is_ally, ":agent"), # always been teammate
                                                (assign, ":agent_ally", 1),
                                            (try_end),
                                                
                                            (gt, ":agent_ally", 0), ## don't help enemies
                                            (neq, ":chosen", ":agent"), ## this code will not look at 'chosen'
                
                                            (try_begin),
                                            (neq, ":teammate_active_effect", 1),
                                                (agent_get_slot, ":teammate_seeker", ":agent", slot_agent_has_active_seeker),
                                                (try_begin),
                                                (eq, ":teammate_seeker", 1),
                                                (eq, ":agent_ally", 1), # stop seekers for agents currently on chosen's team
                                                    (assign, ":teammate_active_effect", 1),
                                                (else_try),
                                                (neq, ":teammate_active_effect", 2),
                                                    (agent_get_slot, ":teammate_compelled", ":agent", slot_agent_under_compulsion),
                                                    (try_begin),
                                                    (eq, ":teammate_compelled", 1),
                                                    (eq, ":agent_ally", 2), # break compulsion on compelled allies
                                                        (assign, ":teammate_active_effect", 2),
                                                    (else_try),
                                                    (neq, ":teammate_active_effect", 3),
                                                        (agent_get_slot, ":teammate_fire", ":agent", slot_agent_on_fire),
                                                        (try_begin),
                                                        (eq, ":teammate_fire", 1),
                                                        (eq, ":agent_ally", 1), # stop fire fore agents currently on chosen's team
                                                            (assign, ":teammate_active_effect", 3),
                                                        (else_try),
                                                        (neq, ":teammate_active_effect", 4),
                                                            (agent_get_slot, ":teammate_bound", ":agent", slot_agent_is_bound),
                                                            (try_begin),
                                                            (eq, ":teammate_bound", 1),
                                                            (eq, ":agent_ally", 1), # break bound for agents currently on chosen's team
                                                                (assign, ":teammate_active_effect", 4),
                                                            (try_end),
                                                        (try_end),
                                                    (try_end),
                                                (try_end),
                                            (try_end),
                
                                        (try_end),

                                        (assign, ":distance", 99999),
                                
                                        (try_for_agents,":agent"),
                                            (agent_is_alive,":agent"), ## don't help dead
                                            (neg|agent_is_wounded,":agent"), ## don't help wounded
#                                            (agent_is_human,":agent"), ## don't help horses
                
                                            # determine if agents under compulsion used to be teammates
                                            (agent_get_slot, ":compulsion_present", ":agent", slot_agent_under_compulsion),
                                            (assign, ":agent_ally", 0),
                                            (try_begin),
                                            (eq, ":compulsion_present", 1),
                                                (agent_get_slot, ":original_team", ":agent", slot_agent_compelled_start_team),
                                                (try_begin),
                                                (ge, ":original_team", 0),
                                                (eq, ":original_team", ":chosen_team"), # used to be teammate
                                                    (assign, ":agent_ally", 2),
                                                (else_try),
                                                (agent_is_ally, ":agent"), # teammate by compulsion
                                                    (assign, ":agent_ally", 1),
                                                (try_end),
                                            (else_try),
                                            (agent_is_ally, ":agent"), # always been teammate
                                                (assign, ":agent_ally", 1),
                                            (try_end),
                                                
                                            (gt, ":agent_ally", 0), ## don't help enemies
                                            (neq, ":chosen", ":agent"), ## this code will not look at 'chosen'

                                            (try_begin),
                                            (eq, ":teammate_active_effect", 1),
                                                (agent_get_slot, ":teammate_seeker", ":agent", slot_agent_has_active_seeker),
                                                (eq, ":teammate_seeker", 1),
                                                (eq, ":agent_ally", 1),
                                                    (agent_get_look_position, pos2, ":agent"),
                                                    (get_distance_between_positions,":dist",pos1,pos2),
                                                    (lt,":dist",":distance"),
                                                    (assign,":nearest_affected_ally",":agent"),
                                                    (assign,":distance",":dist"),
                                            (else_try),
                                            (eq, ":teammate_active_effect", 2),
                                                (agent_get_slot, ":teammate_compelled", ":agent", slot_agent_under_compulsion),
                                                (eq, ":teammate_compelled", 1),
                                                (eq, ":agent_ally", 2),
                                                    (agent_get_look_position, pos2, ":agent"),
                                                    (get_distance_between_positions,":dist",pos1,pos2),
                                                    (lt,":dist",":distance"),
                                                    (assign,":nearest_affected_ally",":agent"),
                                                    (assign,":distance",":dist"),
                                            (else_try),
                                            (eq, ":teammate_active_effect", 3),
                                                (agent_get_slot, ":teammate_fire", ":agent", slot_agent_on_fire),
                                                (eq, ":teammate_fire", 1),
                                                (eq, ":agent_ally", 1),
                                                    (agent_get_look_position, pos2, ":agent"),
                                                    (get_distance_between_positions,":dist",pos1,pos2),
                                                    (lt,":dist",":distance"),
                                                    (assign,":nearest_affected_ally",":agent"),
                                                    (assign,":distance",":dist"),
                                            (else_try),
                                            (eq, ":teammate_active_effect", 4),
                                                (agent_get_slot, ":teammate_bound", ":agent", slot_agent_is_bound),
                                                (eq, ":teammate_bound", 1),
                                                (eq, ":agent_ally", 1),
                                                    (agent_get_look_position, pos2, ":agent"),
                                                    (get_distance_between_positions,":dist",pos1,pos2),
                                                    (lt,":dist",":distance"),
                                                    (assign,":nearest_affected_ally",":agent"),
                                                    (assign,":distance",":dist"),
                                            (try_end),
                                        (try_end),
                                        # End of loops for finding closest affected ally
                                    (try_end),
                                    # End of loops for finding horse on fire
                
                                (try_end),
                            (try_end),
                        (try_end),
                        # End of if statements for does 'chosen' have active effects

                        (try_begin),
                        (gt, ":chosen_active_effect", 0), # chosen unraveling weave on self
                            (try_begin),
                            (eq, ":chosen_active_effect", 1),
                                (agent_get_slot, ":seeker_shooter", ":chosen", slot_agent_seeker_shooter),
                
                                (agent_get_troop_id, ":shooter_id", ":seeker_shooter"),
                                (troop_get_xp, ":shooter_xp", ":shooter_id"),
                                (agent_get_troop_id, ":chosen_id", ":chosen"),
                                (troop_get_xp, ":chosen_xp", ":chosen_id"),
                
                                (try_begin),
                                (gt, ":chosen_xp", ":shooter_xp"), # chosen more experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 25),
                                        (agent_set_slot, ":chosen", slot_agent_has_active_seeker, 0),
                                        (val_sub, "$g_number_seekers_active", 1),
                
                                        (try_begin),
                                        (eq, "$g_seeker_slot_1_target", ":chosen"),
                                            (assign, "$g_seeker_slot_1", 0),
                                            (copy_position, pos1, pos31),
                                        (else_try),
                                        (eq, "$g_seeker_slot_2_target", ":chosen"),
                                            (assign, "$g_seeker_slot_2", 0),
                                            (copy_position, pos1, pos32),
                                        (else_try),
                                        (eq, "$g_seeker_slot_3_target", ":chosen"),
                                            (assign, "$g_seeker_slot_3", 0),
                                            (copy_position, pos1, pos33),
                                        (else_try),
                                        (eq, "$g_seeker_slot_4_target", ":chosen"),
                                            (assign, "$g_seeker_slot_4", 0),
                                            (copy_position, pos1, pos34),
                                        (else_try),
                                        (eq, "$g_seeker_slot_5_target", ":chosen"),
                                            (assign, "$g_seeker_slot_5", 0),
                                            (copy_position, pos1, pos35),
                                        (else_try),
                                        (eq, "$g_seeker_slot_6_target", ":chosen"),
                                            (assign, "$g_seeker_slot_6", 0),
                                            (copy_position, pos1, pos36),
                                        (else_try),
                                        (eq, "$g_seeker_slot_7_target", ":chosen"),
                                            (assign, "$g_seeker_slot_7", 0),
                                            (copy_position, pos1, pos37),
                                        (else_try),
                                        (eq, "$g_seeker_slot_8_target", ":chosen"),
                                            (assign, "$g_seeker_slot_8", 0),
                                            (copy_position, pos1, pos38),
                                        (else_try),
                                        (eq, "$g_seeker_slot_9_target", ":chosen"),
                                            (assign, "$g_seeker_slot_9", 0),
                                            (copy_position, pos1, pos39),
                                        (else_try),
                                        (eq, "$g_seeker_slot_10_target", ":chosen"),
                                            (assign, "$g_seeker_slot_10", 0),
                                            (copy_position, pos1, pos40),
                                        (else_try),
                                        (eq, "$g_seeker_slot_11_target", ":chosen"),
                                            (assign, "$g_seeker_slot_11", 0),
                                            (copy_position, pos1, pos41),
                                        (else_try),
                                        (eq, "$g_seeker_slot_12_target", ":chosen"),
                                            (assign, "$g_seeker_slot_12", 0),
                                            (copy_position, pos1, pos42),
                                        (else_try),
                                        (eq, "$g_seeker_slot_13_target", ":chosen"),
                                            (assign, "$g_seeker_slot_13", 0),
                                            (copy_position, pos1, pos43),
                                        (else_try),
                                        (eq, "$g_seeker_slot_14_target", ":chosen"),
                                            (assign, "$g_seeker_slot_14", 0),
                                            (copy_position, pos1, pos44),
                                        (else_try),
                                        (eq, "$g_seeker_slot_15_target", ":chosen"),
                                            (assign, "$g_seeker_slot_15", 0),
                                            (copy_position, pos1, pos45),
                                        (else_try),
                                        (eq, "$g_seeker_slot_16_target", ":chosen"),
                                            (assign, "$g_seeker_slot_16", 0),
                                            (copy_position, pos1, pos46),
                                        (else_try),
                                        (eq, "$g_seeker_slot_17_target", ":chosen"),
                                            (assign, "$g_seeker_slot_17", 0),
                                            (copy_position, pos1, pos47),
                                        (else_try),
                                        (eq, "$g_seeker_slot_18_target", ":chosen"),
                                            (assign, "$g_seeker_slot_18", 0),
                                            (copy_position, pos1, pos48),
                                        (else_try),
                                        (eq, "$g_seeker_slot_19_target", ":chosen"),
                                            (assign, "$g_seeker_slot_19", 0),
                                            (copy_position, pos1, pos49),
                                        (else_try),
                                        (eq, "$g_seeker_slot_20_target", ":chosen"),
                                            (assign, "$g_seeker_slot_20", 0),
                                            (copy_position, pos1, pos50),
                                        (try_end),
                
                                        (particle_system_burst, "psys_unravel_aura", pos1, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 100),
                                        (try_end),
                                        (add_xp_to_troop,50,":chosen"),
                                (else_try), # chosen less experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 50),
                                        (agent_set_slot, ":chosen", slot_agent_has_active_seeker, 0),
                                        (val_sub, "$g_number_seekers_active", 1),
                
                                        (try_begin),
                                        (eq, "$g_seeker_slot_1_target", ":chosen"),
                                            (assign, "$g_seeker_slot_1", 0),
                                            (copy_position, pos1, pos31),
                                        (else_try),
                                        (eq, "$g_seeker_slot_2_target", ":chosen"),
                                            (assign, "$g_seeker_slot_2", 0),
                                            (copy_position, pos1, pos32),
                                        (else_try),
                                        (eq, "$g_seeker_slot_3_target", ":chosen"),
                                            (assign, "$g_seeker_slot_3", 0),
                                            (copy_position, pos1, pos33),
                                        (else_try),
                                        (eq, "$g_seeker_slot_4_target", ":chosen"),
                                            (assign, "$g_seeker_slot_4", 0),
                                            (copy_position, pos1, pos34),
                                        (else_try),
                                        (eq, "$g_seeker_slot_5_target", ":chosen"),
                                            (assign, "$g_seeker_slot_5", 0),
                                            (copy_position, pos1, pos35),
                                        (else_try),
                                        (eq, "$g_seeker_slot_6_target", ":chosen"),
                                            (assign, "$g_seeker_slot_6", 0),
                                            (copy_position, pos1, pos36),
                                        (else_try),
                                        (eq, "$g_seeker_slot_7_target", ":chosen"),
                                            (assign, "$g_seeker_slot_7", 0),
                                            (copy_position, pos1, pos37),
                                        (else_try),
                                        (eq, "$g_seeker_slot_8_target", ":chosen"),
                                            (assign, "$g_seeker_slot_8", 0),
                                            (copy_position, pos1, pos38),
                                        (else_try),
                                        (eq, "$g_seeker_slot_9_target", ":chosen"),
                                            (assign, "$g_seeker_slot_9", 0),
                                            (copy_position, pos1, pos39),
                                        (else_try),
                                        (eq, "$g_seeker_slot_10_target", ":chosen"),
                                            (assign, "$g_seeker_slot_10", 0),
                                            (copy_position, pos1, pos40),
                                        (else_try),
                                        (eq, "$g_seeker_slot_11_target", ":chosen"),
                                            (assign, "$g_seeker_slot_11", 0),
                                            (copy_position, pos1, pos41),
                                        (else_try),
                                        (eq, "$g_seeker_slot_12_target", ":chosen"),
                                            (assign, "$g_seeker_slot_12", 0),
                                            (copy_position, pos1, pos42),
                                        (else_try),
                                        (eq, "$g_seeker_slot_13_target", ":chosen"),
                                            (assign, "$g_seeker_slot_13", 0),
                                            (copy_position, pos1, pos43),
                                        (else_try),
                                        (eq, "$g_seeker_slot_14_target", ":chosen"),
                                            (assign, "$g_seeker_slot_14", 0),
                                            (copy_position, pos1, pos44),
                                        (else_try),
                                        (eq, "$g_seeker_slot_15_target", ":chosen"),
                                            (assign, "$g_seeker_slot_15", 0),
                                            (copy_position, pos1, pos45),
                                        (else_try),
                                        (eq, "$g_seeker_slot_16_target", ":chosen"),
                                            (assign, "$g_seeker_slot_16", 0),
                                            (copy_position, pos1, pos46),
                                        (else_try),
                                        (eq, "$g_seeker_slot_17_target", ":chosen"),
                                            (assign, "$g_seeker_slot_17", 0),
                                            (copy_position, pos1, pos47),
                                        (else_try),
                                        (eq, "$g_seeker_slot_18_target", ":chosen"),
                                            (assign, "$g_seeker_slot_18", 0),
                                            (copy_position, pos1, pos48),
                                        (else_try),
                                        (eq, "$g_seeker_slot_19_target", ":chosen"),
                                            (assign, "$g_seeker_slot_19", 0),
                                            (copy_position, pos1, pos49),
                                        (else_try),
                                        (eq, "$g_seeker_slot_20_target", ":chosen"),
                                            (assign, "$g_seeker_slot_20", 0),
                                            (copy_position, pos1, pos50),
                                        (try_end),

                                        (particle_system_burst, "psys_unravel_aura", pos1, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 150),
                                        (try_end),
                                        (add_xp_to_troop,75,":chosen"),
                                (try_end),
                            (else_try),
                            (eq, ":chosen_active_effect", 3),
                                (agent_get_slot, ":fire_shooter", ":chosen", slot_agent_fire_starter),
                
                                (agent_get_troop_id, ":shooter_id", ":fire_shooter"),
                                (troop_get_xp, ":shooter_xp", ":shooter_id"),
                                (agent_get_troop_id, ":chosen_id", ":chosen"),
                                (troop_get_xp, ":chosen_xp", ":chosen_id"),
                
                                (try_begin),
                                (gt, ":chosen_xp", ":shooter_xp"), # chosen more experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 25),
                                        (agent_set_slot, ":chosen", slot_agent_on_fire, 0),
                                        (particle_system_burst, "psys_unravel_aura", pos1, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 100),
                                        (try_end),
                                        (add_xp_to_troop,50,":chosen"),
                                (else_try), # chosen less experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 50),
                                        (agent_set_slot, ":chosen", slot_agent_on_fire, 0),
                                        (particle_system_burst, "psys_unravel_aura", pos1, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 150),
                                        (try_end),
                                        (add_xp_to_troop,75,":chosen"),
                                (try_end),
                            (else_try),
                            (eq, ":chosen_active_effect", 4),
                                (agent_get_slot, ":bind_shooter", ":chosen", slot_agent_bound_by),
                
                                (agent_get_troop_id, ":shooter_id", ":bind_shooter"),
                                (troop_get_xp, ":shooter_xp", ":shooter_id"),
                                (agent_get_troop_id, ":chosen_id", ":chosen"),
                                (troop_get_xp, ":chosen_xp", ":chosen_id"),
                
                                (try_begin),
                                (gt, ":chosen_xp", ":shooter_xp"), # chosen more experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 25),
                                        (agent_set_slot, ":chosen", slot_agent_is_bound, 0),
                                        (particle_system_burst, "psys_unravel_aura", pos1, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 100),
                                        (try_end),
                                        (add_xp_to_troop,50,":chosen"),
                                (else_try), # chosen less experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 50),
                                        (agent_set_slot, ":chosen", slot_agent_is_bound, 0),
                                        (particle_system_burst, "psys_unravel_aura", pos1, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 150),
                                        (try_end),
                                        (add_xp_to_troop,75,":chosen"),
                                (try_end),
                            (try_end),

                        (else_try), # chosen unraveling weave on horse
                        (eq, ":chosen_horse_on_fire", 1),
                            (agent_get_slot, ":fire_shooter", ":chosen_horse", slot_agent_fire_starter),

                            (agent_get_troop_id, ":shooter_id", ":fire_shooter"),
                            (troop_get_xp, ":shooter_xp", ":shooter_id"),
                            (agent_get_troop_id, ":chosen_id", ":chosen"),
                            (troop_get_xp, ":chosen_xp", ":chosen_id"),

                            (agent_get_position, pos2, ":chosen_horse"),
                
                            (try_begin),
                            (gt, ":chosen_xp", ":shooter_xp"), # chosen more experienced than shooter
                                (store_random_in_range, ":random", 1, 100),
                                (gt, ":random", 25),
                                    (agent_set_slot, ":chosen_horse", slot_agent_on_fire, 0),
                                    (particle_system_burst, "psys_unravel_aura", pos2, 50),
                                    (play_sound, "snd_unravel"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 100),
                                    (try_end),
                                    (add_xp_to_troop,50,":chosen"),
                            (else_try), # chosen less experienced than shooter
                                (store_random_in_range, ":random", 1, 100),
                                (gt, ":random", 50),
                                    (agent_set_slot, ":chosen_horse", slot_agent_on_fire, 0),
                                    (particle_system_burst, "psys_unravel_aura", pos2, 50),
                                    (play_sound, "snd_unravel"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 150),
                                    (try_end),
                                    (add_xp_to_troop,75,":chosen"),
                            (try_end),

                        (else_try),
                        (lt, ":teammate_active_effect", 5), # chosen unraveling weave on teammate
                            (try_begin),
                            (eq, ":teammate_active_effect", 1),
                                (agent_get_slot, ":seeker_shooter", ":nearest_affected_ally", slot_agent_seeker_shooter),
                
                                (agent_get_troop_id, ":shooter_id", ":seeker_shooter"),
                                (troop_get_xp, ":shooter_xp", ":shooter_id"),
                                (agent_get_troop_id, ":chosen_id", ":chosen"),
                                (troop_get_xp, ":chosen_xp", ":chosen_id"),

                                (agent_get_position, pos2, ":nearest_affected_ally"),
                
                                (try_begin),
                                (gt, ":chosen_xp", ":shooter_xp"), # chosen more experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 25),
                                        (agent_set_slot, ":nearest_affected_ally", slot_agent_has_active_seeker, 0),
                                        (val_sub, "$g_number_seekers_active", 1),
                
                                        (try_begin),
                                        (eq, "$g_seeker_slot_1_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_1", 0),
                                            (copy_position, pos1, pos31),
                                        (else_try),
                                        (eq, "$g_seeker_slot_2_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_2", 0),
                                            (copy_position, pos1, pos32),
                                        (else_try),
                                        (eq, "$g_seeker_slot_3_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_3", 0),
                                            (copy_position, pos1, pos33),
                                        (else_try),
                                        (eq, "$g_seeker_slot_4_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_4", 0),
                                            (copy_position, pos1, pos34),
                                        (else_try),
                                        (eq, "$g_seeker_slot_5_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_5", 0),
                                            (copy_position, pos1, pos35),
                                        (else_try),
                                        (eq, "$g_seeker_slot_6_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_6", 0),
                                            (copy_position, pos1, pos36),
                                        (else_try),
                                        (eq, "$g_seeker_slot_7_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_7", 0),
                                            (copy_position, pos1, pos37),
                                        (else_try),
                                        (eq, "$g_seeker_slot_8_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_8", 0),
                                            (copy_position, pos1, pos38),
                                        (else_try),
                                        (eq, "$g_seeker_slot_9_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_9", 0),
                                            (copy_position, pos1, pos39),
                                        (else_try),
                                        (eq, "$g_seeker_slot_10_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_10", 0),
                                            (copy_position, pos1, pos40),
                                        (else_try),
                                        (eq, "$g_seeker_slot_11_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_11", 0),
                                            (copy_position, pos1, pos41),
                                        (else_try),
                                        (eq, "$g_seeker_slot_12_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_12", 0),
                                            (copy_position, pos1, pos42),
                                        (else_try),
                                        (eq, "$g_seeker_slot_13_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_13", 0),
                                            (copy_position, pos1, pos43),
                                        (else_try),
                                        (eq, "$g_seeker_slot_14_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_14", 0),
                                            (copy_position, pos1, pos44),
                                        (else_try),
                                        (eq, "$g_seeker_slot_15_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_15", 0),
                                            (copy_position, pos1, pos45),
                                        (else_try),
                                        (eq, "$g_seeker_slot_16_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_16", 0),
                                            (copy_position, pos1, pos46),
                                        (else_try),
                                        (eq, "$g_seeker_slot_17_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_17", 0),
                                            (copy_position, pos1, pos47),
                                        (else_try),
                                        (eq, "$g_seeker_slot_18_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_18", 0),
                                            (copy_position, pos1, pos48),
                                        (else_try),
                                        (eq, "$g_seeker_slot_19_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_19", 0),
                                            (copy_position, pos1, pos49),
                                        (else_try),
                                        (eq, "$g_seeker_slot_20_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_20", 0),
                                            (copy_position, pos1, pos50),
                                        (try_end),
                
                                        (particle_system_burst, "psys_unravel_aura", pos1, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 100),
                                        (try_end),
                                        (add_xp_to_troop,50,":chosen"),
                                (else_try), # chosen less experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 50),
                                        (agent_set_slot, ":nearest_affected_ally", slot_agent_has_active_seeker, 0),
                                        (val_sub, "$g_number_seekers_active", 1),
                
                                        (try_begin),
                                        (eq, "$g_seeker_slot_1_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_1", 0),
                                            (copy_position, pos1, pos31),
                                        (else_try),
                                        (eq, "$g_seeker_slot_2_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_2", 0),
                                            (copy_position, pos1, pos32),
                                        (else_try),
                                        (eq, "$g_seeker_slot_3_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_3", 0),
                                            (copy_position, pos1, pos33),
                                        (else_try),
                                        (eq, "$g_seeker_slot_4_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_4", 0),
                                            (copy_position, pos1, pos34),
                                        (else_try),
                                        (eq, "$g_seeker_slot_5_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_5", 0),
                                            (copy_position, pos1, pos35),
                                        (else_try),
                                        (eq, "$g_seeker_slot_6_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_6", 0),
                                            (copy_position, pos1, pos36),
                                        (else_try),
                                        (eq, "$g_seeker_slot_7_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_7", 0),
                                            (copy_position, pos1, pos37),
                                        (else_try),
                                        (eq, "$g_seeker_slot_8_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_8", 0),
                                            (copy_position, pos1, pos38),
                                        (else_try),
                                        (eq, "$g_seeker_slot_9_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_9", 0),
                                            (copy_position, pos1, pos39),
                                        (else_try),
                                        (eq, "$g_seeker_slot_10_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_10", 0),
                                            (copy_position, pos1, pos40),
                                        (else_try),
                                        (eq, "$g_seeker_slot_11_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_11", 0),
                                            (copy_position, pos1, pos41),
                                        (else_try),
                                        (eq, "$g_seeker_slot_12_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_12", 0),
                                            (copy_position, pos1, pos42),
                                        (else_try),
                                        (eq, "$g_seeker_slot_13_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_13", 0),
                                            (copy_position, pos1, pos43),
                                        (else_try),
                                        (eq, "$g_seeker_slot_14_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_14", 0),
                                            (copy_position, pos1, pos44),
                                        (else_try),
                                        (eq, "$g_seeker_slot_15_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_15", 0),
                                            (copy_position, pos1, pos45),
                                        (else_try),
                                        (eq, "$g_seeker_slot_16_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_16", 0),
                                            (copy_position, pos1, pos46),
                                        (else_try),
                                        (eq, "$g_seeker_slot_17_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_17", 0),
                                            (copy_position, pos1, pos47),
                                        (else_try),
                                        (eq, "$g_seeker_slot_18_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_18", 0),
                                            (copy_position, pos1, pos48),
                                        (else_try),
                                        (eq, "$g_seeker_slot_19_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_19", 0),
                                            (copy_position, pos1, pos49),
                                        (else_try),
                                        (eq, "$g_seeker_slot_20_target", ":nearest_affected_ally"),
                                            (assign, "$g_seeker_slot_20", 0),
                                            (copy_position, pos1, pos50),
                                        (try_end),
                
                                        (particle_system_burst, "psys_unravel_aura", pos1, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 150),
                                        (try_end),
                                        (add_xp_to_troop,75,":chosen"),
                                (try_end),
                            (else_try),
                            (eq, ":teammate_active_effect", 2),
                                (agent_get_slot, ":compulsion_shooter", ":nearest_affected_ally", slot_agent_compelled_by),
                
                                (agent_get_troop_id, ":shooter_id", ":compulsion_shooter"),
                                (troop_get_xp, ":shooter_xp", ":shooter_id"),
                                (agent_get_troop_id, ":chosen_id", ":chosen"),
                                (troop_get_xp, ":chosen_xp", ":chosen_id"),

                                (agent_get_position, pos2, ":nearest_affected_ally"),
                
                                (try_begin),
                                (gt, ":chosen_xp", ":shooter_xp"), # chosen more experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 25),
                                        (agent_get_slot, ":start_team", ":nearest_affected_ally", slot_agent_compelled_start_team),
                                        (agent_set_team, ":nearest_affected_ally", ":start_team"),
                                        (agent_set_slot, ":nearest_affected_ally", slot_agent_under_compulsion, 0),
                                        (particle_system_burst, "psys_unravel_aura", pos2, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 100),
                                        (try_end),
                                        (add_xp_to_troop,50,":chosen"),
                                (else_try), # chosen less experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 50),
                                        (agent_get_slot, ":start_team", ":nearest_affected_ally", slot_agent_compelled_start_team),
                                        (agent_set_team, ":nearest_affected_ally", ":start_team"),
                                        (agent_set_slot, ":nearest_affected_ally", slot_agent_under_compulsion, 0),
                                        (particle_system_burst, "psys_unravel_aura", pos2, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 150),
                                        (try_end),
                                        (add_xp_to_troop,75,":chosen"),
                                (try_end),
                            (else_try),
                            (eq, ":teammate_active_effect", 3),
                                (agent_get_slot, ":fire_shooter", ":nearest_affected_ally", slot_agent_fire_starter),
                
                                (agent_get_troop_id, ":shooter_id", ":fire_shooter"),
                                (troop_get_xp, ":shooter_xp", ":shooter_id"),
                                (agent_get_troop_id, ":chosen_id", ":chosen"),
                                (troop_get_xp, ":chosen_xp", ":chosen_id"),

                                (agent_get_position, pos2, ":nearest_affected_ally"),
                
                                (try_begin),
                                (gt, ":chosen_xp", ":shooter_xp"), # chosen more experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 25),
                                        (agent_set_slot, ":nearest_affected_ally", slot_agent_on_fire, 0),
                                        (particle_system_burst, "psys_unravel_aura", pos2, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 100),
                                        (try_end),
                                        (add_xp_to_troop,50,":chosen"),
                                (else_try), # chosen less experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 50),
                                        (agent_set_slot, ":nearest_affected_ally", slot_agent_on_fire, 0),
                                        (particle_system_burst, "psys_unravel_aura", pos2, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 150),
                                        (try_end),
                                        (add_xp_to_troop,75,":chosen"),
                                (try_end),
                            (else_try),
                            (eq, ":teammate_active_effect", 4),
                                (agent_get_slot, ":bind_shooter", ":nearest_affected_ally", slot_agent_bound_by),
                
                                (agent_get_troop_id, ":shooter_id", ":bind_shooter"),
                                (troop_get_xp, ":shooter_xp", ":shooter_id"),
                                (agent_get_troop_id, ":chosen_id", ":chosen"),
                                (troop_get_xp, ":chosen_xp", ":chosen_id"),

                                (agent_get_position, pos2, ":nearest_affected_ally"),
                
                                (try_begin),
                                (gt, ":chosen_xp", ":shooter_xp"), # chosen more experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 25),
                                        (agent_set_slot, ":nearest_affected_ally", slot_agent_is_bound, 0),
                                        (particle_system_burst, "psys_unravel_aura", pos2, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 100),
                                        (try_end),
                                        (add_xp_to_troop,50,":chosen"),
                                (else_try), # chosen less experienced than shooter
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 50),
                                        (agent_set_slot, ":nearest_affected_ally", slot_agent_is_bound, 0),
                                        (particle_system_burst, "psys_unravel_aura", pos2, 50),
                                        (play_sound, "snd_unravel"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 150),
                                        (try_end),
                                        (add_xp_to_troop,75,":chosen"),
                                (try_end),
                            (try_end),
                        (else_try),
                        (neg|agent_is_non_player, ":chosen"),
                            (display_message, "@No active weaves to unravel..."),
                        (try_end),

                    (try_end),
                        
                    # End Unravel Weave


#########################################  Weave 6
                (else_try),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 6),
                # end
                    # Defensive Blast Weave
                    (assign, ":stamina_cost", 2800),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end

                        (try_for_agents,":agent"),
                            (agent_is_alive,":agent"), ## don't hurt dead
                            (neg|agent_is_wounded,":agent"), ## don't hurt wounded
#                            (neg|agent_is_ally,":agent"), ## don't hurt allies
                            (neq,":chosen",":agent"), ## don't hurt self
                            (neq, ":chosen_horse", ":agent"),
                            (agent_get_look_position, pos2, ":agent"),
                            (get_distance_between_positions,":dist",pos1,pos2),
                            (store_agent_hit_points,":target_health",":agent",1),
                    
                            (try_begin),
                            (lt,":dist",750),

                                (agent_set_slot, ":agent", slot_agent_is_airborne, 1),

                                (position_get_x, ":attacker_x", pos1),
                                (position_get_y, ":attacker_y", pos1),
                                (position_get_x, ":target_x", pos2),
                                (position_get_y, ":target_y", pos2),

                                (store_sub, ":run", ":target_x", ":attacker_x"),
                                (store_sub, ":rise", ":target_y", ":attacker_y"),

                                (agent_set_slot, ":agent", slot_agent_airborne_x_movement, ":run"),
                                (agent_set_slot, ":agent", slot_agent_airborne_y_movement, ":rise"),

                                (get_distance_between_positions, ":dist_from_chosen", pos1, pos2),
                                (try_begin),
                                (lt, ":dist_from_chosen", 100),
                                    (agent_set_slot, ":agent", slot_agent_airborne_power_factor, 20),
                                (else_try),
                                (is_between, ":dist_from_chosen", 100, 250),
                                    (agent_set_slot, ":agent", slot_agent_airborne_power_factor, 15),
                                (else_try),
                                (is_between, ":dist_from_chosen", 250, 450),
                                    (agent_set_slot, ":agent", slot_agent_airborne_power_factor, 10),
                                (else_try),
                                (is_between, ":dist_from_chosen", 450, 750),
                                    (agent_set_slot, ":agent", slot_agent_airborne_power_factor, 5),
                                (try_end),
                            (try_end),

                            (try_begin),
                            (lt, ":dist", 400),
                                (try_begin),
                                    (gt,":target_health",15),
                                    (val_sub,":target_health",15),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 20),
                                    (try_end),
                                    (add_xp_to_troop,10,":chosen"),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 30),
                                    (try_end),
                                    (add_xp_to_troop,15,":chosen"),
                                (try_end),
                            (else_try),
                            (is_between,":dist",400,700),
                                (try_begin),
                                    (gt,":target_health",10),
                                    (val_sub,":target_health",10),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 10),
                                    (try_end),
                                    (add_xp_to_troop,5,":chosen"),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 20),
                                    (try_end),
                                    (add_xp_to_troop,10,":chosen"),
                                (try_end),
                            (try_end),
                        (try_end),

                        (particle_system_burst, "psys_massive_pistol_smoke", pos1, 25),
                        (play_sound, "snd_explosion"),

                    (try_end),
                        
                    # End Defensive Blast Weave


################################## Weave 7
                (else_try),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 7),
                # end
                    # Ranged Earth Blast
                    (assign, ":stamina_cost", 3100),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end

                        (assign, ":times_near_ground", 0),
                        (assign, ":near_enemy", 0),

                        (try_for_range,reg5,1,1000),  ###was 500
                        (eq, ":times_near_ground", 0),
                            (particle_system_burst, "psys_dust_blast", pos1, 10),
                            (position_move_y,pos1,20),
                            (copy_position,pos2,pos1),
                            (position_set_z_to_ground_level, pos2),
                            (get_distance_between_positions,":dist",pos1,pos2),

                            (position_get_z, ":z_ground", pos2),
                            (store_add, ":z_ground_low", ":z_ground", 20),
                            (store_add, ":z_ground_high", ":z_ground", 200),

                            (try_for_agents, ":agent"),
                            (eq, ":near_enemy", 0),
                                (neq, ":chosen", ":agent"),
                                (neq, ":chosen_horse", ":agent"),
                                (agent_get_team, ":agent_team", ":agent"),
                                (teams_are_enemies, ":chosen_team", ":agent_team"),
                                (agent_is_alive, ":agent"),
                                (neg|agent_is_wounded, ":agent"),
                                (agent_get_look_position, pos4, ":agent"),
                                (get_distance_between_positions, ":dist_2", pos2, pos4),
                                (position_get_z, ":z_attack_trail", pos1),
                                (lt, ":dist_2", 50), # near agent (x-y)
                                (is_between, ":z_attack_trail", ":z_ground_low", ":z_ground_high"), # within the agent's body (z height)
                                (assign, ":dist", 5),
                                (assign, ":near_enemy", 1),
                            (try_end),
                    
                            (try_begin),
                            (lt,":dist",10),
                                (val_add, ":times_near_ground", 1),
                                (particle_system_burst, "psys_earthquake", pos1, 25),  # effect needs a long duration
                                (play_sound,"snd_explosion"),
                                (copy_position, pos3, pos1),
                                (scene_prop_get_instance,":instance", "spr_snowy_heap_a", 0),  #need
                                (position_copy_origin,pos2,pos1),
                                (prop_instance_set_position,":instance",pos2),
                                (assign,reg5,2000),  #was 1000
                            (try_end),
                        (try_end),
                    
                        (try_for_agents,":agent"),
                            (neq,":chosen",":agent"), ## added this to avoid affecting shooter
                            (neq, ":chosen_horse", ":agent"),
#                            (neg|agent_is_ally,":agent"), ## add this to avoid hurting allies
                            (agent_is_alive,":agent"), ## add this to not affect dead people
                            (neg|agent_is_wounded,":agent"), ## add this to not affect wounded people
                            (agent_get_position,pos2,":agent"),
                            (get_distance_between_positions,":dist",pos3,pos2),
                            (store_agent_hit_points,":target_health",":agent",1),
                    
                            (try_begin),
                            (lt,":dist",750),

                                (agent_set_slot, ":agent", slot_agent_is_airborne, 1),

                                (position_get_x, ":attacker_x", pos1),
                                (position_get_y, ":attacker_y", pos1),
                                (position_get_x, ":target_x", pos2),
                                (position_get_y, ":target_y", pos2),

                                (store_sub, ":run", ":target_x", ":attacker_x"),
                                (store_sub, ":rise", ":target_y", ":attacker_y"),

                                (agent_set_slot, ":agent", slot_agent_airborne_x_movement, ":run"),
                                (agent_set_slot, ":agent", slot_agent_airborne_y_movement, ":rise"),

                                (get_distance_between_positions, ":dist_from_chosen", pos1, pos2),
                                (try_begin),
                                (lt, ":dist_from_chosen", 100),
                                    (agent_set_slot, ":agent", slot_agent_airborne_power_factor, 20),
                                (else_try),
                                (is_between, ":dist_from_chosen", 100, 250),
                                    (agent_set_slot, ":agent", slot_agent_airborne_power_factor, 15),
                                (else_try),
                                (is_between, ":dist_from_chosen", 250, 450),
                                    (agent_set_slot, ":agent", slot_agent_airborne_power_factor, 10),
                                (else_try),
                                (is_between, ":dist_from_chosen", 450, 750),
                                    (agent_set_slot, ":agent", slot_agent_airborne_power_factor, 5),
                                (try_end),
                            (try_end),

                            (try_begin),
                            (lt, ":dist", 100),
                                (try_begin),
                                    (gt,":target_health",15),
                                    (val_sub,":target_health",15),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 20),
                                    (try_end),
                                    (add_xp_to_troop,10,":chosen"),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 30),
                                    (try_end),
                                    (add_xp_to_troop,15,":chosen"),
                                (try_end),
                            (else_try),
                            (is_between,":dist",100,250),
                                (try_begin),
                                    (gt,":target_health",10),
                                    (val_sub,":target_health",10),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 10),
                                    (try_end),
                                    (add_xp_to_troop,5,":chosen"),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 20),
                                    (try_end),
                                    (add_xp_to_troop,10,":chosen"),
                                (try_end),
                            (try_end),
                            (else_try),
                            (is_between,":dist",250,450),
                                (try_begin),
                                    (gt,":target_health",6),
                                    (val_sub,":target_health",6),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 10),
                                    (try_end),
                                    (add_xp_to_troop,5,":chosen"),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 20),
                                    (try_end),
                                    (add_xp_to_troop,10,":chosen"),
                                (try_end),
                            (else_try),
                            (is_between,":dist",450,750),
                                (try_begin),
                                    (gt,":target_health",3),
                                    (val_sub,":target_health",3),
                                    (agent_set_hit_points,":agent",":target_health",1),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 10),
                                    (try_end),
                                    (add_xp_to_troop,5,":chosen"),
                                (else_try),
                                    (agent_set_hit_points,":agent",0,0),
                                    (agent_deliver_damage_to_agent,":chosen",":agent"),
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 20),
                                    (try_end),
                                    (add_xp_to_troop,10,":chosen"),
                                (try_end),
                        (try_end),

                    (try_end),
                                                
                    #End Ranged Earth Blast


#########################################  Weave 8
                (else_try),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 8),
                # end
                    # Bind Weave (attempt to bind nearest enemy)
                    (assign, ":stamina_cost", 3600),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end

                        (assign, ":distance",99999),
                        (assign, ":number_of_enemies", 0),

                        (try_for_agents,":agent"),
                            (agent_is_alive,":agent"), ## don't bind dead
                            (neg|agent_is_wounded,":agent"), ## don't bind wounded
                            (agent_is_human,":agent"), ## don't bind horses
                            (neg|agent_is_ally,":agent"), ## don't bind allies
                            (neq, ":chosen", ":agent"), ## shooter can't bind self
                            (agent_get_slot, ":already_bound", ":agent", slot_agent_is_bound),
                            (eq, ":already_bound", 0),
                            (agent_get_look_position, pos2, ":agent"),
                            (get_distance_between_positions,":dist",pos1,pos2),
                            (lt,":dist",":distance"),
                            (assign,":target",":agent"),
                            (assign,":distance",":dist"),
                            (val_add, ":number_of_enemies", 1),
                        (try_end),

                        (try_begin),
                        (ge, ":number_of_enemies", 1),
                            (agent_get_slot, ":target_is_channeler", ":target", slot_agent_is_channeler),
                            (agent_get_slot, ":target_is_shielded", ":target", slot_agent_is_shielded),
                    
                            (try_begin),
                            (eq, ":target_is_channeler", 1),  # harder to bind channelers
                            (eq, ":target_is_shielded", 0),  # unless they are shielded
                                (agent_get_troop_id, ":target_id", ":target"),
                                (troop_get_xp, ":target_xp", ":target_id"),
                                (agent_get_troop_id, ":chosen_id", ":chosen"),
                                (troop_get_xp, ":chosen_xp", ":chosen_id"),
                    
                                (try_begin),
                                (gt, ":chosen_xp", ":target_xp"),
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 25),
                                        (agent_get_look_position, pos3, ":target"),
                                        (position_get_x, ":target_x", pos3),
                                        (position_get_y, ":target_y", pos3),
                                        # set slots
                                        (agent_set_slot, ":target", slot_agent_is_bound, 1),
                                        (agent_set_slot, ":target", slot_agent_bound_by, ":chosen"),
                                        (agent_set_slot, ":target", slot_agent_bound_x, ":target_x"),
                                        (agent_set_slot, ":target", slot_agent_bound_y, ":target_y"),
                                        (agent_set_slot, ":target", slot_agent_bound_duration, 10),

                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 60),
                                        (try_end),
                                        (add_xp_to_troop,30,":chosen"),
                                (else_try),
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 75),
                                        (agent_get_look_position, pos3, ":target"),
                                        (position_get_x, ":target_x", pos3),
                                        (position_get_y, ":target_y", pos3),
                                        # set slots
                                        (agent_set_slot, ":target", slot_agent_is_bound, 1),
                                        (agent_set_slot, ":target", slot_agent_bound_by, ":chosen"),
                                        (agent_set_slot, ":target", slot_agent_bound_x, ":target_x"),
                                        (agent_set_slot, ":target", slot_agent_bound_y, ":target_y"),
                                        (agent_set_slot, ":target", slot_agent_bound_duration, 10),

                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 120),
                                        (try_end),
                                        (add_xp_to_troop,60,":chosen"),
                                (try_end),
                    
                            (else_try),
                                (agent_get_look_position, pos3, ":target"),
                                (position_get_x, ":target_x", pos3),
                                (position_get_y, ":target_y", pos3),
                                # set slots
                                (agent_set_slot, ":target", slot_agent_is_bound, 1),
                                (agent_set_slot, ":target", slot_agent_bound_by, ":chosen"),
                                (agent_set_slot, ":target", slot_agent_bound_x, ":target_x"),
                                (agent_set_slot, ":target", slot_agent_bound_y, ":target_y"),
                                (agent_set_slot, ":target", slot_agent_bound_duration, 10),

                                (try_begin), # add to channeling multiplier if agent is player
                                (neg|agent_is_non_player, ":chosen"),
                                    (val_add, "$g_channeling_proficiency_modifier", 30),
                                (try_end),
                                (add_xp_to_troop,15,":chosen"),
                            (try_end),

                            (play_sound, "snd_man_grunt_long"),
                        (try_end),

                    (try_end),

                    # End Bind Weave


################################## Weave 9
                (else_try),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 9),
                # end
                    #Chain Lightning Weave
                    (assign, ":stamina_cost", 4300),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end

                        (assign, ":victim_1", 0),
                        (assign, ":victim_2", 0),
                        (assign, ":victim_3", 0),
                        (assign, ":victim_4", 0),
                        (assign, ":victim_5", 0),
                        (assign, ":victim_6", 0),
                        (assign, ":victim_7", 0),
                        (assign, ":victim_8", 0),

                        (assign, ":times_near_ground", 0),
                        (assign, ":near_enemy", 0),

                        (try_for_range,reg5,1,1000),  ###was 500
                        (eq, ":times_near_ground", 0),
                            (particle_system_burst, "psys_electricity_blast", pos1, 10),
                            (position_move_y,pos1,20),
                            (copy_position,pos2,pos1),
                            (position_set_z_to_ground_level, pos2),
                            (get_distance_between_positions,":dist",pos1,pos2),

                            (position_get_z, ":z_ground", pos2),
                            (store_add, ":z_ground_low", ":z_ground", 20),
                            (store_add, ":z_ground_high", ":z_ground", 200),

                            (try_for_agents, ":agent"),
                            (eq, ":near_enemy", 0),
                                (neq, ":chosen", ":agent"),
                                (neq, ":chosen_horse", ":agent"),
                                (agent_get_team, ":agent_team", ":agent"),
                                (teams_are_enemies, ":chosen_team", ":agent_team"),
                                (agent_is_alive, ":agent"),
                                (neg|agent_is_wounded, ":agent"),
                                (agent_get_look_position, pos4, ":agent"),
                                (get_distance_between_positions, ":dist_2", pos2, pos4),
                                (position_get_z, ":z_attack_trail", pos1),
                                (lt, ":dist_2", 50), # near agent (x-y)
                                (is_between, ":z_attack_trail", ":z_ground_low", ":z_ground_high"), # within the agent's body (z height)
                                (assign, ":dist", 5),
                                (assign, ":near_enemy", 1),
                            (try_end),
                    
                            (try_begin),
                            (lt,":dist",10),
                                (val_add, ":times_near_ground", 1),
                                (particle_system_burst, "psys_electricity_sparks", pos1, 25),
                                (play_sound,"snd_chain_lightning"), # need a sound for freeze
                                (copy_position, pos3, pos1),
                                (scene_prop_get_instance,":instance", "spr_snowy_heap_a", 0),  #need
                                (position_copy_origin,pos2,pos1),
                                (prop_instance_set_position,":instance",pos2),
                                (assign,reg5,2000),  #was 1000
                            (try_end),
                        (try_end),

                        (try_for_range, ":counter", 1, 8),
                            (assign, ":distance", 99999),
                            (assign, ":number_near_blast", 0),
                        ## Look for agents near initial strike zone
                            (try_for_agents,":agent"),
                                (neq,":chosen",":agent"), ## added this to avoid shocking shooter
                                (neq, ":chosen_horse", ":agent"),
#                                (neg|agent_is_ally,":agent"), ## add this to avoid shocking allies
                                (agent_is_alive,":agent"), ## add this to not shock dead people
                                (neg|agent_is_wounded,":agent"), ## add this to not shock wounded people
                                (agent_get_slot, ":already_shocked", ":agent", slot_agent_has_been_shocked),
                                (eq, ":already_shocked", 0),
                                (agent_get_position,pos2,":agent"),
                                (get_distance_between_positions,":dist",pos3,pos2),
                                (lt,":dist",":distance"),
                                    (assign,":agent_closest_to_blast",":agent"),
                                    (assign,":distance",":dist"),
                                    (val_add, ":number_near_blast", 1),
                            (try_end),

                            (try_begin), # apply charge if agent close enough
                            (ge, ":number_near_blast", 1),
                            (lt, ":dist", 1500),
                                (store_agent_hit_points,":target_health",":agent_closest_to_blast",1),

                                (try_begin),
                                (is_between, ":counter", 1, 3),
                                    (try_begin),
                                    (gt, ":target_health", 15),
                                        (val_sub,":target_health",15),
                                        (agent_set_hit_points,":agent_closest_to_blast",":target_health",1),
                                        (agent_deliver_damage_to_agent,":chosen",":agent_closest_to_blast"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 30),
                                        (try_end),
                                        (add_xp_to_troop,15,":chosen"),
                                    (else_try),
                                        (agent_set_hit_points,":agent_closest_to_blast",0,0),
                                        (agent_deliver_damage_to_agent,":chosen",":agent_closest_to_blast"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 60),
                                        (try_end),
                                        (add_xp_to_troop,30,":chosen"),
                                    (try_end),
                                (else_try),
                                (is_between, ":counter", 3, 5),
                                    (try_begin),
                                    (gt, ":target_health", 12),
                                        (val_sub,":target_health",12),
                                        (agent_set_hit_points,":agent_closest_to_blast",":target_health",1),
                                        (agent_deliver_damage_to_agent,":chosen",":agent_closest_to_blast"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 30),
                                        (try_end),
                                        (add_xp_to_troop,15,":chosen"),
                                    (else_try),
                                        (agent_set_hit_points,":agent_closest_to_blast",0,0),
                                        (agent_deliver_damage_to_agent,":chosen",":agent_closest_to_blast"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 60),
                                        (try_end),
                                        (add_xp_to_troop,30,":chosen"),
                                    (try_end),
                                (else_try),
                                (is_between, ":counter", 5, 7),
                                    (try_begin),
                                    (gt, ":target_health", 9),
                                        (val_sub,":target_health",9),
                                        (agent_set_hit_points,":agent_closest_to_blast",":target_health",1),
                                        (agent_deliver_damage_to_agent,":chosen",":agent_closest_to_blast"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 30),
                                        (try_end),
                                        (add_xp_to_troop,15,":chosen"),
                                    (else_try),
                                        (agent_set_hit_points,":agent_closest_to_blast",0,0),
                                        (agent_deliver_damage_to_agent,":chosen",":agent_closest_to_blast"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 60),
                                        (try_end),
                                        (add_xp_to_troop,30,":chosen"),
                                    (try_end),
                                (else_try),
                                (is_between, ":counter", 7, 9),
                                    (try_begin),
                                    (gt, ":target_health", 6),
                                        (val_sub,":target_health",6),
                                        (agent_set_hit_points,":agent_closest_to_blast",":target_health",1),
                                        (agent_deliver_damage_to_agent,":chosen",":agent_closest_to_blast"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 30),
                                        (try_end),
                                        (add_xp_to_troop,15,":chosen"),
                                    (else_try),
                                        (agent_set_hit_points,":agent_closest_to_blast",0,0),
                                        (agent_deliver_damage_to_agent,":chosen",":agent_closest_to_blast"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 60),
                                        (try_end),
                                        (add_xp_to_troop,30,":chosen"),
                                    (try_end),
                                (try_end),
                    

                                # set victim slots
                                (agent_set_slot, ":agent_closest_to_blast", slot_agent_has_been_shocked, 1),

                                (try_begin),
                                (eq, ":counter", 1),
                                    (assign, ":victim_1", ":agent_closest_to_blast"),
                                (else_try),
                                (eq, ":counter", 2),
                                    (assign, ":victim_2", ":agent_closest_to_blast"),
                                (else_try),
                                (eq, ":counter", 3),
                                    (assign, ":victim_3", ":agent_closest_to_blast"),
                                (else_try),
                                (eq, ":counter", 4),
                                    (assign, ":victim_4", ":agent_closest_to_blast"),
                                (else_try),
                                (eq, ":counter", 5),
                                    (assign, ":victim_5", ":agent_closest_to_blast"),
                                (else_try),
                                (eq, ":counter", 6),
                                    (assign, ":victim_6", ":agent_closest_to_blast"),
                                (else_try),
                                (eq, ":counter", 7),
                                    (assign, ":victim_7", ":agent_closest_to_blast"),
                                (else_try),
                                (eq, ":counter", 8),
                                    (assign, ":victim_8", ":agent_closest_to_blast"),
                                (end_try),

                                # calculate blast travel
                                (agent_get_position, pos2, ":agent_closest_to_blast"),
                                (position_get_x, ":x_end", pos2),
                                (position_get_y, ":y_end", pos2),
                                (position_get_z, ":z_end", pos2),
                                (val_add, ":z_end", 1250),

                                (position_get_x, ":x_start", pos3),
                                (position_get_y, ":y_start", pos3),
                                (position_get_z, ":z_start", pos3),
                    
                                (try_begin),
                                (gt, ":counter", 1),
                                    (val_add, ":z_start", 1250),
                                (try_end),

                                (store_sub, ":run", ":x_end", ":x_start"),
                                (store_sub, ":rise", ":y_end", ":y_start"),
                                (store_sub, ":vert", ":z_end", ":z_start"),

                                (assign, ":interval", 60),

                                (val_div, ":run", ":interval"),
                                (val_div, ":rise", ":interval"),
                                (val_div, ":vert", ":interval"),

                                (try_for_range, ":unused", 0, ":interval"),
                                    (val_add, ":x_start", ":run"),
                                    (val_add, ":y_start", ":rise"),
                                    (val_add, ":z_start", ":vert"),

                                    (position_set_x, pos3, ":x_start"),
                                    (position_set_y, pos3, ":y_start"),
                                    (position_set_z, pos3, ":z_start"),

                                    (particle_system_burst, "psys_electricity_blast", pos3, 10),
                                (try_end),
                    
                                (particle_system_burst, "psys_electricity_sparks", pos2, 25),

                                (copy_position, pos3, pos2),
                    
                            (try_end),

                        # reset victim slots
                        (try_end),

                        (try_begin),
                        (neq, ":victim_1", 0),
                            (agent_set_slot, ":victim_1", slot_agent_has_been_shocked, 0),
                        (try_end),

                        (try_begin),
                        (neq, ":victim_2", 0),
                            (agent_set_slot, ":victim_2", slot_agent_has_been_shocked, 0),
                        (try_end),

                        (try_begin),
                        (neq, ":victim_3", 0),
                            (agent_set_slot, ":victim_3", slot_agent_has_been_shocked, 0),
                        (try_end),

                        (try_begin),
                        (neq, ":victim_4", 0),
                            (agent_set_slot, ":victim_4", slot_agent_has_been_shocked, 0),
                        (try_end),

                        (try_begin),
                        (neq, ":victim_5", 0),
                            (agent_set_slot, ":victim_5", slot_agent_has_been_shocked, 0),
                        (try_end),

                        (try_begin),
                        (neq, ":victim_6", 0),
                            (agent_set_slot, ":victim_6", slot_agent_has_been_shocked, 0),
                        (try_end),

                        (try_begin),
                        (neq, ":victim_7", 0),
                            (agent_set_slot, ":victim_7", slot_agent_has_been_shocked, 0),
                        (try_end),

                        (try_begin),
                        (neq, ":victim_8", 0),
                            (agent_set_slot, ":victim_8", slot_agent_has_been_shocked, 0),
                        (try_end),

                    (try_end),
                    
                    #Chain Lightening end


#########################################  Weave 10
                (else_try),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 10),
                # end
                    # Fire Curtain Weave
                    (assign, ":stamina_cost", 5100),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end
                    
                         (agent_get_position,pos1,":chosen"),
                    
                         (position_move_y,pos1,1000),  # how far out the flame wall is  (was 500)
                         (play_sound,"snd_fire_curtain"),
                         (assign,":mul",1),
                         (try_for_range,":num",1,16),  # was (try_for_range,":num",1,11),
                            (val_mul,":num",":mul"),
                            (val_mul,":num",300),      # was (val_mul,":num",200),  # is how wide the flame wall is
                            (position_move_x,pos1,":num"),
                            (particle_system_burst,"psys_massive_fire",pos1,125),  #was 75  (this number is the duration
                            (try_for_agents,":agent"),
                                (neq,":chosen",":agent"), ### added this to avoid killing shooter
                                (neq, ":chosen_horse", ":agent"),
#                                (neg|agent_is_ally,":agent"),## added this to avoid killing allies
                                (agent_is_alive,":agent"), ## add this to not re-kill dead people
                                (neg|agent_is_wounded,":agent"), ## add this to not re-kill wounded people
                                (agent_get_position,pos2,":agent"),
                                (get_distance_between_positions,":dist",pos1,pos2),
                    
                                # instant kill if fire curtain within 50 of agent
                                (try_begin),
                                (lt,":dist",50),  #was 300
                                        (agent_set_hit_points,":agent",0,0),
                                        (agent_deliver_damage_to_agent,":chosen",":agent"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 75),
                                        (try_end),
                                        (add_xp_to_troop,40,":chosen"),
                                # do 25 damage if fire curtain within 50 to 100 of agent
                                (else_try),
                                    (is_between,":dist",50, 100),  #was 300
                                    (store_agent_hit_points,":target_health",":agent",1),
                                    (try_begin),
                                        (gt,":target_health",25),
                                        (val_sub,":target_health",25),
                                        (agent_set_hit_points,":agent",":target_health",1),
                                        (agent_deliver_damage_to_agent,":chosen",":agent"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 40),
                                        (try_end),
                                        (add_xp_to_troop,20,":chosen"),
                                        (agent_set_slot, ":agent", slot_agent_on_fire, 1),
                                        (agent_set_slot, ":agent", slot_agent_fire_starter, ":chosen"),
                                        (agent_set_slot, ":agent", slot_agent_fire_duration, 20),
                                    (else_try),
                                        (agent_set_hit_points,":agent",0,0),
                                        (agent_deliver_damage_to_agent,":chosen",":agent"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 50),
                                        (try_end),
                                        (add_xp_to_troop,25,":chosen"),
                                        (position_get_z, ":z_temp", pos2),
                                        (val_add, ":z_temp", 300),
                                        (position_set_z, pos2, ":z_temp"),
                                        #(particle_system_burst, "psys_torch_fire", pos2, 100),
                                    (try_end),
                                # do 15 damage if fire curtain within 100 to 200 of agent
                                (else_try),
                                    (is_between,":dist",100,200),  #was 300
                                    (store_agent_hit_points,":target_health",":agent",1),
                                    (try_begin),
                                        (gt,":target_health",15),
                                        (val_sub,":target_health",15),
                                        (agent_set_hit_points,":agent",":target_health",1),
                                        (agent_deliver_damage_to_agent,":chosen",":agent"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 30),
                                        (try_end),
                                        (add_xp_to_troop,15,":chosen"),
                                        (agent_set_slot, ":agent", slot_agent_on_fire, 1),
                                        (agent_set_slot, ":agent", slot_agent_fire_starter, ":chosen"),
                                        (agent_set_slot, ":agent", slot_agent_fire_duration, 15),
                                    (else_try),
                                        (agent_set_hit_points,":agent",0,0),
                                        (agent_deliver_damage_to_agent,":chosen",":agent"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 40),
                                        (try_end),
                                        (add_xp_to_troop,20,":chosen"),
                                        (position_get_z, ":z_temp", pos2),
                                        (val_add, ":z_temp", 300),
                                        (position_set_z, pos2, ":z_temp"),
                                        #(particle_system_burst, "psys_torch_fire", pos2, 100),
                                    (try_end),
                                # do 10 damage if fire curtain within 200 to 300 of agent
                                (else_try),
                                    (is_between,":dist",200,300),  #was 300
                                    (store_agent_hit_points,":target_health",":agent",1),
                                    (try_begin),
                                        (gt,":target_health",10),
                                        (val_sub,":target_health",10),
                                        (agent_set_hit_points,":agent",":target_health",1),
                                        (agent_deliver_damage_to_agent,":chosen",":agent"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 20),
                                        (try_end),
                                        (add_xp_to_troop,10,":chosen"),
                                        (agent_set_slot, ":agent", slot_agent_on_fire, 1),
                                        (agent_set_slot, ":agent", slot_agent_fire_starter, ":chosen"),
                                        (agent_set_slot, ":agent", slot_agent_fire_duration, 10),
                                    (else_try),
                                        (agent_set_hit_points,":agent",0,0),
                                        (agent_deliver_damage_to_agent,":chosen",":agent"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 30),
                                        (try_end),
                                        (add_xp_to_troop,15,":chosen"),
                                        (position_get_z, ":z_temp", pos2),
                                        (val_add, ":z_temp", 300),
                                        (position_set_z, pos2, ":z_temp"),
                                        #(particle_system_burst, "psys_torch_fire", pos2, 100),
                                    (try_end),
                                # do 5 damage if fire curtain within 300 to 400 of agent
                                (else_try),
                                    (is_between,":dist",300,400),  #was 300
                                    (store_agent_hit_points,":target_health",":agent",1),
                                    (try_begin),
                                        (gt,":target_health",5),
                                        (val_sub,":target_health",5),
                                        (agent_set_hit_points,":agent",":target_health",1),
                                        (agent_deliver_damage_to_agent,":chosen",":agent"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 10),
                                        (try_end),
                                        (add_xp_to_troop,5,":chosen"),
                                        (agent_set_slot, ":agent", slot_agent_on_fire, 1),
                                        (agent_set_slot, ":agent", slot_agent_fire_starter, ":chosen"),
                                        (agent_set_slot, ":agent", slot_agent_fire_duration, 5),
                                    (else_try),
                                        (agent_set_hit_points,":agent",0,0),
                                        (agent_deliver_damage_to_agent,":chosen",":agent"),
                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 20),
                                        (try_end),
                                        (add_xp_to_troop,10,":chosen"),
                                        (position_get_z, ":z_temp", pos2),
                                        (val_add, ":z_temp", 300),
                                        (position_set_z, pos2, ":z_temp"),
                                        #(particle_system_burst, "psys_torch_fire", pos2, 100),
                                    (try_end),
                                (try_end),
                    
                            (try_end),
                            (val_mul,":mul",-1),
                        (try_end),

                    (try_end),

                    # End Fire Curtain Weave


#########################################  Weave 11
                (else_try),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 11),
                # end
                    # Shield Weave (attempt to shield nearest enemy channeler)
                    (assign, ":stamina_cost", 5800),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end

                        (assign, ":distance",99999),
                        (assign, ":number_of_enemies", 0),

                        (try_for_agents,":agent"),
                            (agent_is_alive,":agent"), ## don't shield dead
                            (neg|agent_is_wounded,":agent"), ## don't shield wounded
                            (agent_is_human,":agent"), ## don't shield horses
                            (neg|agent_is_ally,":agent"), ## don't shield allies
                            (neq, ":chosen", ":agent"), ## shooter can't shield self
                            (agent_get_slot, ":channeler", ":agent", slot_agent_is_channeler),
                            (eq, ":channeler", 1),
                            (agent_get_slot, ":already_shielded", ":agent", slot_agent_is_shielded),
                            (eq, ":already_shielded", 0),
                            (agent_get_look_position, pos2, ":agent"),
                            (get_distance_between_positions,":dist",pos1,pos2),
                            (lt,":dist",":distance"),
                            (assign,":target",":agent"),
                            (assign,":distance",":dist"),
                            (val_add, ":number_of_enemies", 1),
                        (try_end),

                        (try_begin),
                        (ge, ":number_of_enemies", 1),
                            (agent_get_troop_id, ":target_id", ":target"),
                            (troop_get_xp, ":target_xp", ":target_id"),
                            (agent_get_troop_id, ":chosen_id", ":chosen"),
                            (troop_get_xp, ":chosen_xp", ":chosen_id"),
                    
                            (try_begin),
                            (gt, ":chosen_xp", ":target_xp"),
                                (store_random_in_range, ":random", 1, 100),
                                (gt, ":random", 25),
                                    # set slot
                                    (agent_set_slot, ":target", slot_agent_is_shielded, 1),
                                    (agent_set_slot, ":target", slot_agent_shielded_by, ":chosen"),

                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 60),
                                    (try_end),
                                    (add_xp_to_troop,30,":chosen"),
                                    (play_sound, "snd_shield"),  # new sound?
                            (else_try),
                                (store_random_in_range, ":random", 1, 100),
                                (gt, ":random", 75),
                                    # set slot
                                    (agent_set_slot, ":target", slot_agent_is_shielded, 1),
                                    (agent_set_slot, ":target", slot_agent_shielded_by, ":chosen"),
                    
                                    (try_begin), # add to channeling multiplier if agent is player
                                    (neg|agent_is_non_player, ":chosen"),
                                        (val_add, "$g_channeling_proficiency_modifier", 120),
                                    (try_end),
                                    (add_xp_to_troop,60,":chosen"),
                                    (play_sound, "snd_shield"),  # new sound?
                            (try_end),
                        (try_end),

                    (try_end),

                    # End Shield Weave


#########################################  Weave 12
                (else_try),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 12),
                # end
                    # Seeker Weave
                    (assign, ":stamina_cost", 6600),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end

                        (assign, ":distance",99999),
                        (assign, ":number_of_enemies", 0),

                        (try_for_agents,":agent"),
                            (agent_is_alive,":agent"), ## don't hurt dead
                            (neg|agent_is_wounded,":agent"), ## don't hurt wounded
                            (agent_is_human,":agent"), ## don't hurt horses
                            (neg|agent_is_ally,":agent"), ## don't hurt allies
                            (neq, ":chosen", ":agent"), ## shooter can't hurt self
                            (agent_get_slot, ":already_targeted", ":agent", slot_agent_has_active_seeker),
                            (eq, ":already_targeted", 0),
                            (agent_get_look_position, pos2, ":agent"),
                            (get_distance_between_positions,":dist",pos1,pos2),
                            (lt,":dist",":distance"),
                            (assign,":target",":agent"),
                            (assign,":distance",":dist"),
                            (val_add, ":number_of_enemies", 1),
                        (try_end),

#                    (assign, reg45, ":dist"),
#                    (display_message, "@Target is {reg45} from shooter..."),

                        (try_begin),
                        (ge, ":number_of_enemies", 1),
                        (le, "$g_number_seekers_active", 20),
                            (assign, ":slot_found", 0),
                    
                            (try_begin),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_1", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos31, pos1),  # cur position for seeker 1
                                (assign, "$g_seeker_slot_1_target", ":target"), # make target global target for slot 1
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), # slot chosen as the target's shooter
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), # show that agent is getting tracked
                                (val_add, "$g_number_seekers_active", 1), # add to total number of active seekers
                                (assign, "$g_seeker_slot_1", 1), # globally show that the seeker slot is full
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_2", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos32, pos1),
                                (assign, "$g_seeker_slot_2_target", ":target"),
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"),
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1),
                                (val_add, "$g_number_seekers_active", 1),
                                (assign, "$g_seeker_slot_2", 1),
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_3", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos33, pos1),  
                                (assign, "$g_seeker_slot_3_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_3", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_4", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos34, pos1),  
                                (assign, "$g_seeker_slot_4_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_4", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_5", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos35, pos1),  
                                (assign, "$g_seeker_slot_5_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_5", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_6", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos36, pos1),  
                                (assign, "$g_seeker_slot_6_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_6", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_7", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos37, pos1),  
                                (assign, "$g_seeker_slot_7_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_7", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_8", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos38, pos1),  
                                (assign, "$g_seeker_slot_8_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_8", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_9", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos39, pos1),  
                                (assign, "$g_seeker_slot_9_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_9", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_10", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos40, pos1),  
                                (assign, "$g_seeker_slot_10_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_10", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_11", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos41, pos1),  # cur position for seeker 11
                                (assign, "$g_seeker_slot_11_target", ":target"), # make target global target for slot 11
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), # slot chosen as the target's shooter
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), # show that agent is getting tracked
                                (val_add, "$g_number_seekers_active", 1), # add to total number of active seekers
                                (assign, "$g_seeker_slot_11", 1), # globally show that the seeker slot is full
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_12", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos42, pos1),
                                (assign, "$g_seeker_slot_12_target", ":target"),
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"),
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1),
                                (val_add, "$g_number_seekers_active", 1),
                                (assign, "$g_seeker_slot_12", 1),
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_13", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos43, pos1),  
                                (assign, "$g_seeker_slot_13_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_13", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_14", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos44, pos1),  
                                (assign, "$g_seeker_slot_14_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_14", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_15", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos45, pos1),  
                                (assign, "$g_seeker_slot_15_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_15", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_16", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos46, pos1),  
                                (assign, "$g_seeker_slot_16_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_16", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_17", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos47, pos1),  
                                (assign, "$g_seeker_slot_17_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_17", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_18", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos48, pos1),  
                                (assign, "$g_seeker_slot_18_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_18", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_19", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos49, pos1),  
                                (assign, "$g_seeker_slot_19_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_19", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (else_try),
                            (eq, ":slot_found", 0),
                            (eq, "$g_seeker_slot_20", 0),
                                (agent_get_look_position, pos1, ":chosen"),
                                (copy_position, pos50, pos1),  
                                (assign, "$g_seeker_slot_20_target", ":target"), 
                                (agent_set_slot, ":target", slot_agent_seeker_shooter, ":chosen"), 
                                (agent_set_slot, ":target", slot_agent_has_active_seeker, 1), 
                                (val_add, "$g_number_seekers_active", 1), 
                                (assign, "$g_seeker_slot_20", 1), 
                                (assign, ":slot_found", 1),
                                (play_sound, "snd_seeker"),
                            (try_end),
                        (else_try),
                        (ge, ":number_of_enemies", 1),
                        (eq, "$g_number_seekers_active", 20),
                        (neg|agent_is_non_player, ":chosen"),
                            (display_message, "@Too many active seekers!!"), 
                        (try_end),

                    (try_end),
                        
                    # End Seeker Weave


#########################################  Weave 13
                (else_try),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 13),
                # end
                    # Compulsion Weave
                    (assign, ":stamina_cost", 7300),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end

                        (assign, ":distance",99999),
                        (assign, ":number_of_enemies", 0),

                        (try_for_agents,":agent"),
                            (agent_is_alive,":agent"), ## don't compel dead
                            (neg|agent_is_wounded,":agent"), ## don't compel wounded
                            (agent_is_human,":agent"), ## don't compel horses
                            (neg|agent_is_ally,":agent"), ## don't compel allies
                            (neq, ":chosen", ":agent"), ## shooter can't compel self
                            (get_player_agent_no,":player_agent"),
                            (neq, ":agent", ":player_agent"), ## shooter can't compel player (too many complications)
                            (agent_get_slot, ":already_compelled", ":agent", slot_agent_under_compulsion),
                            (eq, ":already_compelled", 0),
                            (agent_get_look_position, pos2, ":agent"),
                            (get_distance_between_positions,":dist",pos1,pos2),
                            (lt,":dist",":distance"),
                            (assign,":target",":agent"),
                            (assign,":distance",":dist"),
                            (val_add, ":number_of_enemies", 1),
                        (try_end),

                        (try_begin),
                        (ge, ":number_of_enemies", 1),
                            (agent_get_troop_id, ":target_id", ":target"),
                            (troop_get_xp, ":target_xp", ":target_id"),
                            (agent_get_troop_id, ":chosen_id", ":chosen"),
                            (troop_get_xp, ":chosen_xp", ":chosen_id"),

                            (agent_get_slot, ":channeler", ":agent", slot_agent_is_channeler),

                            (agent_get_team, ":chosen_team", ":chosen"),
                            (agent_get_team, ":target_team", ":target"),
                    
                            (try_begin),
                            (eq, ":channeler", 1), # target is channeler
                                (try_begin),
                                (gt, ":chosen_xp", ":target_xp"), # target less experienced
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 60),
                                        (agent_set_team, ":target", ":chosen_team"),
                                        (agent_clear_scripted_mode, ":target"),
                
                                        # set slot
                                        (agent_set_slot, ":target", slot_agent_under_compulsion, 1),
                                        (agent_set_slot, ":target", slot_agent_compelled_by, ":chosen"),
                                        (agent_set_slot, ":target", slot_agent_compelled_start_team, ":target_team"),

                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 150),
                                        (try_end),
                                        (add_xp_to_troop,75,":chosen"),
                                        (play_sound, "snd_compulsion"),
                                (else_try), # target more experienced
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 85),
                                        (agent_set_team, ":target", ":chosen_team"),
                                        (agent_clear_scripted_mode, ":target"),
                
                                        # set slot
                                        (agent_set_slot, ":target", slot_agent_under_compulsion, 1),
                                        (agent_set_slot, ":target", slot_agent_compelled_by, ":chosen"),
                                        (agent_set_slot, ":target", slot_agent_compelled_start_team, ":target_team"),

                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 200),
                                        (try_end),
                                        (add_xp_to_troop,100,":chosen"),
                                        (play_sound, "snd_compulsion"),
                                (try_end),
                            (else_try), # target is non-channeler
                                (try_begin),
                                (gt, ":chosen_xp", ":target_xp"), # target less experienced
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 10),
                                        (agent_set_team, ":target", ":chosen_team"),
                                        (agent_clear_scripted_mode, ":target"),
                
                                        # set slot
                                        (agent_set_slot, ":target", slot_agent_under_compulsion, 1),
                                        (agent_set_slot, ":target", slot_agent_compelled_by, ":chosen"),
                                        (agent_set_slot, ":target", slot_agent_compelled_start_team, ":target_team"),

                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 50),
                                        (try_end),
                                        (add_xp_to_troop,25,":chosen"),
                                        (play_sound, "snd_compulsion"),
                                (else_try), # target more experienced
                                    (store_random_in_range, ":random", 1, 100),
                                    (gt, ":random", 35),
                                        (agent_set_team, ":target", ":chosen_team"),
                                        (agent_clear_scripted_mode, ":target"),
                
                                        # set slot
                                        (agent_set_slot, ":target", slot_agent_under_compulsion, 1),
                                        (agent_set_slot, ":target", slot_agent_compelled_by, ":chosen"),
                                        (agent_set_slot, ":target", slot_agent_compelled_start_team, ":target_team"),

                                        (try_begin), # add to channeling multiplier if agent is player
                                        (neg|agent_is_non_player, ":chosen"),
                                            (val_add, "$g_channeling_proficiency_modifier", 100),
                                        (try_end),
                                        (add_xp_to_troop,50,":chosen"),
                                        (play_sound, "snd_compulsion"),
                                (try_end),
                            (try_end),
                        (try_end),

                    (try_end),

                    # End Compulsion Weave


################################## Weave 14
                (else_try),
                # new method for multiplayer
                (player_get_slot, ":active_channeling_weave", ":player", slot_player_current_weave),
                (eq, ":active_channeling_weave", 14),
                # end
                    #Balefire Weave (rip victom from pattern and undo their last actions)
                    (assign, ":stamina_cost", 8100),
                    # new method for multiplayer
                    (player_get_slot, ":current_channeling_stamina", ":player", slot_player_current_channeling_stamina),
                    (store_sub, ":stamina_check", ":current_channeling_stamina", ":stamina_cost"),
                    # end
                    (try_begin),
                    (lt, ":stamina_check", 0),
                        (display_message, "@You are too tired to channel..."),
                    (else_try),
                        # new method for multiplayer
                        (val_sub, ":current_channeling_stamina", ":stamina_cost"),
                        (player_set_slot, ":player", slot_player_current_channeling_stamina, ":current_channeling_stamina"),
                        # end

                        (assign, ":times_near_ground", 0),

                        (try_for_range,reg5,1,1000),  ###was 500
                        (eq, ":times_near_ground", 0),
                            (particle_system_burst, "psys_balefire_beam", pos1, 15), ## need balefire trail
                            (position_move_y,pos1,20),
                            (copy_position,pos2,pos1),
                            (position_set_z_to_ground_level, pos2),
                            (get_distance_between_positions,":dist",pos1,pos2),

                            (position_get_z, ":z_ground", pos2),
                            (store_add, ":z_ground_low", ":z_ground", 20),
                            (store_add, ":z_ground_high", ":z_ground", 200),

                            (try_for_agents, ":agent"),
                                (neq, ":chosen", ":agent"),
                                (neq, ":chosen_horse", ":agent"),
#                                (neg|agent_is_ally, ":agent"),
                                (agent_is_alive, ":agent"),
                                (neg|agent_is_wounded, ":agent"),
                                (agent_get_look_position, pos4, ":agent"),
                                (get_distance_between_positions, ":dist_2", pos2, pos4),
                                (position_get_z, ":z_attack_trail", pos1),
                                (lt, ":dist_2", 50), # balefire must be near the agent (x-y radius)
                                (is_between, ":z_attack_trail", ":z_ground_low", ":z_ground_high"), # balefire must be within the agent's body (z height)
                                (agent_set_slot, ":agent", slot_agent_hit_by_balefire, 1),
                                (agent_set_slot, ":agent", slot_agent_balefire_shooter, ":chosen"),
                                (try_for_range, ":unused", 1, 10),
                                    (particle_system_burst, "psys_balefire_strike", pos4, 20),  #need
                                    (position_move_z, pos4, 20),
                                (try_end),
                            (try_end),
                    
                            (try_begin),
                            (lt,":dist",10),
                                (val_add, ":times_near_ground", 1),
                                (play_sound,"snd_balefire"),
                                (copy_position, pos3, pos1),
                                (scene_prop_get_instance,":instance", "spr_explosion", 0),  #need
                                (position_copy_origin,pos2,pos1),
                                (prop_instance_set_position,":instance",pos2),
                                (position_move_z,pos2,1000),
                                (prop_instance_animate_to_position,":instance",pos2,175),
                                (assign,reg5,2000),  #was 1000
                            (try_end),
                        (try_end),

                    (try_end),
                                
                    #Balefire weave end


                    
### Be sure to leave this (try_end), at the end of the active weave code
                (try_end),

######################################### Run the "Shield Breaker" code if the channeler is shielded...
            (else_try),
                (agent_get_slot, ":shield_holder", ":chosen", slot_agent_shielded_by),

                (agent_get_troop_id, ":shield_holder_id", ":shield_holder"),
                (troop_get_xp, ":shield_holder_xp", ":shield_holder_id"),
                (agent_get_troop_id, ":chosen_id", ":chosen"),
                (troop_get_xp, ":chosen_xp", ":chosen_id"),

                (try_begin),
                (agent_is_alive, ":shield_holder"), # shield creator is alive
                (neg|agent_is_wounded, ":shield_holder"),
                    (try_begin),
                    (gt, ":chosen_xp", ":shield_holder_xp"), # shield holder 'weaker'
                        (store_random_in_range, ":random", 1, 100),
                        (gt, ":random", 60),
                            (agent_set_slot, ":chosen", slot_agent_is_shielded, 0),
                            (play_sound, "snd_unravel"),
                            (try_begin), # add to channeling multiplier if agent is player
                            (neg|agent_is_non_player, ":chosen"),
                                (val_add, "$g_channeling_proficiency_modifier", 60),
                                (display_message, "@You are no longer shielded from the One Power!!"),
                            (try_end),
                            (add_xp_to_troop,30,":chosen"),
                    (else_try), # shield holder 'stronger'
                        (store_random_in_range, ":random", 1, 100),
                        (gt, ":random", 90),
                            (agent_set_slot, ":chosen", slot_agent_is_shielded, 0),
                            (play_sound, "snd_unravel"),
                            (try_begin), # add to channeling multiplier if agent is player
                            (neg|agent_is_non_player, ":chosen"),
                                (val_add, "$g_channeling_proficiency_modifier", 120),
                                (display_message, "@You are no longer shielded from the One Power!!"),
                            (try_end),
                            (add_xp_to_troop,60,":chosen"),
                    (try_end),
                (else_try), # shield creator is dead / wounded
                    (store_random_in_range, ":random", 1, 100),
                    (gt, ":random", 25),
                        (agent_set_slot, ":chosen", slot_agent_is_shielded, 0),
                        (play_sound, "snd_unravel"),
                        (try_begin), # add to channeling multiplier if agent is player
                        (neg|agent_is_non_player, ":chosen"),
                            (val_add, "$g_channeling_proficiency_modifier", 30),
                            (display_message, "@You are no longer shielded from the One Power!!"),
                        (try_end),
                        (add_xp_to_troop,15,":chosen"),
                (try_end),

#                (store_mod, ":counter", "$g_number_of_weaves_used", 4),
#                (try_begin),
#                (eq, ":counter", 0),
#                    (display_message, "@You are shielded..."),
#                (try_end),
                
            # End of Shield Breaker code
                
            (try_end),



#   Counts the number of times the player has used the channeling item
            (val_add, "$g_number_of_weaves_used", 1),
#            (assign, reg5, "$g_number_of_weaves_used"),
#            (display_message, "@Player has channeled {reg5} times ..."),
#   Warns that the player is almost out of 'ammo'
            (try_begin),
            (ge, "$g_number_of_weaves_used", 130),
                (display_message, "str_almost_out_of_ammo"),
            (try_end),
#   Displays the player's channeling proficiency modifier
#            (assign, reg4,"$g_channeling_proficiency_modifier"),
#            (display_message, "@Current channeling proficiency modifier is {reg4} ..."),


                         ],),
    ]],
 


#end magic items

 

# other special items
["suldam_dagger",         "Sul'dam Dagger", [("dagger_b",0),("dagger_b_scabbard",ixmesh_carry),("dagger_b",imodbits_good),("dagger_b_scabbard",ixmesh_carry|imodbits_good)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn, 
37 , weight(0.75)|difficulty(1)|spd_rtng(109) | weapon_length(47)|swing_damage(22 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
["der_suldam_dagger",         "Der Sul'dam Dagger", [("dagger_b",0),("dagger_b_scabbard",ixmesh_carry),("dagger_b",imodbits_good),("dagger_b_scabbard",ixmesh_carry|imodbits_good)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn, 
37 , weight(0.75)|difficulty(1)|spd_rtng(109) | weapon_length(47)|swing_damage(22 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],

 ["channeler_dagger",         "Dagger", [("dagger_b",0),("dagger_b_scabbard",ixmesh_carry),("dagger_b",imodbits_good),("dagger_b_scabbard",ixmesh_carry|imodbits_good)], itp_type_one_handed_wpn|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn, 
37 , weight(0.75)|difficulty(0)|spd_rtng(109) | weapon_length(47)|swing_damage(22 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],
["sword_secondary", "Sword", [("sword_medieval_a",0),("sword_medieval_a_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 163 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(27 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],


# end other special items


################################
# Narf's Transitional Armor Pack
################################

["corrazina_red_wot", "Corrazina", [("corrazina_red",0)],  itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 4228 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(18)|difficulty(8) ,imodbits_armor ],

["corrazina_green_wot", "Corrazina", [("corrazina_green",0)],  itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 4228 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(18)|difficulty(8) ,imodbits_armor ],

["corrazina_grey_wot", "Corrazina", [("corrazina_grey",0)],  itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 4228 , weight(23)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(18)|difficulty(8) ,imodbits_armor ],

["churburg_13_wot", "Full Plate", [("churburg_13",0)],  itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 4828 , weight(27)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(20)|difficulty(8) ,imodbits_armor ],

["churburg_13_brass_wot", "Ornate Full Plate", [("churburg_13_brass",0)],  itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 4828 , weight(27)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(20)|difficulty(8) ,imodbits_armor ],

["churburg_13_mail_wot", "Ornate Full Plate", [("churburg_13_mail",0)],  itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 4828 , weight(27)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(20)|difficulty(8) ,imodbits_armor ],

["padded_jack_wot", "Padded Jack", [("gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 415 , weight(6)|abundance(100)|head_armor(0)|body_armor(26)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],

["early_transitional_blue_wot", "Heavy Mail and Plate", [("early_transitional_blue",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],

["early_transitional_orange_wot", "Heavy Mail and Plate", [("early_transitional_orange",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],

["early_transitional_white_wot", "Heavy Mail and Plate", [("early_transitional_white",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 3828 , weight(25)|abundance(100)|head_armor(0)|body_armor(52)|leg_armor(16)|difficulty(8) ,imodbits_armor ],  

["splinted_greaves_spurs_wot", "Splinted Greaves with Spurs", [("splinted_greaves_spurs",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 960 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(7) ,imodbits_plate ],
 
 ["splinted_greaves_nospurs_wot", "Splinted Greaves", [("splinted_greaves_nospurs",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 960 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(7) ,imodbits_plate ],

["shynbaulds_wot", "Shynbaulds", [("shynbaulds",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 1200 , weight(3.0)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(32)|difficulty(8) ,imodbits_plate ],

["steel_greaves_wot", "Cased Greaves", [("steel_greaves",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 1100 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(33)|difficulty(9) ,imodbits_plate ],  

["oniontop_bascinet_wot", "Onion-top Bascinet", [("onion-top_bascinet",0)], itp_merchandise|itp_type_head_armor   |itp_civilian,0, 650 , weight(2.25)|abundance(100)|head_armor(46)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],

["pigface_klappvisor_wot", "Pigface Bascinet", [("pigface_klappvisor",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian,0, 1180 , weight(2.75)|abundance(100)|head_armor(56)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],

["pigface_klappvisor_open_wot", "Pigface Bascinet", [("pigface_klappvisor_open",0)], itp_merchandise|itp_type_head_armor   |itp_civilian,0, 1180 , weight(2.75)|abundance(100)|head_armor(50)|body_armor(0)|leg_armor(0)|difficulty(8) ,imodbits_plate ],

["hounskull_wot", "Hounskull Bascinet", [("hounskull",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian,0, 1180 , weight(2.75)|abundance(100)|head_armor(56)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],

["sugarloaf_wot", "Sugarloaf Greathelm", [("sugarloaf",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian,0, 1200 , weight(3.25)|abundance(100)|head_armor(53)|body_armor(0)|leg_armor(0)|difficulty(9) ,imodbits_plate ],

["kettle_hat_wot", "Kettle Hat", [("prato_chapel-de-fer",0)], itp_merchandise| itp_type_head_armor|itp_civilian,0, 
240 , weight(1.75)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

["wisby_gauntlets_black_wot","Splinted Leather Gauntlets", [("wisby_gauntlets_black_L",0)], itp_merchandise|itp_type_hand_armor|itp_civilian,0, 860, weight(0.75)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor],

["wisby_gauntlets_red_wot","Splinted Leather Gauntlets", [("wisby_gauntlets_red_L",0)], itp_merchandise|itp_type_hand_armor|itp_civilian,0, 860, weight(0.75)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor],

["mail_gauntlets_wot","Mail Gauntlets", [("mail_gauntlets_L",0)], itp_merchandise|itp_type_hand_armor|itp_civilian,0, 490, weight(0.5)|abundance(100)|body_armor(4)|difficulty(0),imodbits_armor],

["hourglass_gauntlets_ornate_wot","Ornate Hourglass Gauntlets", [("hourglass_gauntlets_ornate_L",0)], itp_merchandise|itp_type_hand_armor|itp_civilian,0, 1190, weight(1.0)|abundance(100)|body_armor(7)|difficulty(0),imodbits_armor],

["hourglass_gauntlets_wot","Hourglass Gauntlets", [("hourglass_gauntlets_L",0)], itp_merchandise|itp_type_hand_armor|itp_civilian,0, 990, weight(1.0)|abundance(100)|body_armor(7)|difficulty(0),imodbits_armor],

["steel_buckler1_wot", "Steel Buckler", [("steel_buckler1",0)], itp_merchandise|itp_type_shield, itcf_carry_buckler_left,  120 , weight(2)|hit_points(330)|body_armor(12)|spd_rtng(98)|shield_width(35)|shield_height(35),imodbits_shield ],

["steel_buckler2_wot", "Steel Buckler", [("steel_buckler2",0)], itp_merchandise|itp_type_shield, itcf_carry_buckler_left,  120 , weight(2)|hit_points(330)|body_armor(12)|spd_rtng(98)|shield_width(28)|shield_height(45),imodbits_shield ],
# End Narf's Transitional Armor



##########################
#Samurai Armor and Weapons
##########################

["claymore_chevalier01_wot", "claymore chevalier01", [("claymore_chevalier01",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
 1123 , weight(2.75)|difficulty(10)|spd_rtng(96) | weapon_length(120)|swing_damage(42 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high ],
["epee_courte_chevalier01_wot", "epee courte chevalier01", [("epee_courte_chevalier01",0)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 480 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(100)|swing_damage(29 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high ],
["epee_courte_chevalier02_wot", "epee courte chevalier02", [("epee_courte_chevalier02",0),("epee_courte_chevalier02_fourreau", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 480 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(100)|swing_damage(29 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high ],

["armure_samurai01_wot", "armure samurai01", [("armure_samurai01",0)], itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
2900 , weight(24)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(8) ,imodbits_armor ],



# TGS Specific Items

# Legion of the Dragon
 ["legion_recruit_tunic", "Dark Blue Tunic", [("legion_recruit_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
500 , weight(10)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(5)|difficulty(4) ,imodbits_armor ],
 ["ashaman_soldier_coat", "Ashaman Soldier Coat", [("ashaman_soldier_coat",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
750 , weight(10)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(6)|difficulty(4) ,imodbits_armor ],
 ["ashaman_dedicated_coat", "Ashaman Dedicated Coat", [("ashaman_dedicated_coat",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
1000 , weight(15)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(7)|difficulty(6) ,imodbits_armor ],
 ["ashaman_coat", "Ashaman Coat", [("ashaman_coat",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
1500 , weight(15)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(8)|difficulty(6) ,imodbits_armor ],
["black_leather_boots", "Black Leather Boots", [("black_leather_boots_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 200 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],

 ["legion_army_tunic", "Legion Army Tunic", [("legion_army_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
500 , weight(10)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(4) ,imodbits_armor ],
 ["legion_army_armor", "Legion Army Armor", [("legion_army_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
1000 , weight(15)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(17)|difficulty(6) ,imodbits_armor ],
 ["legion_plate", "Legion Plate", [("legion_plate",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 2000 , weight(27)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(20)|difficulty(8) ,imodbits_armor ],
["legion_shield_weak", "Legion Shield", [("legion_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 200 , weight(3.5)|hit_points(100)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["legion_shield_normal", "Legion Shield", [("legion_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 600 , weight(3.5)|hit_points(300)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["legion_shield_strong", "Legion Shield", [("legion_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 1200 , weight(3.5)|hit_points(500)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["andoran_helmet", "Andoran Helmet", [("milanese_sallet",0)], itp_merchandise| itp_type_head_armor   ,0,
  800 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

 ["red_hand_tunic", "Red Hand Tunic", [("red_hand_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
500 , weight(10)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(4) ,imodbits_armor ],
 ["red_arm_tunic", "Red Arm Tunic", [("red_arm_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
600 , weight(10)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(4) ,imodbits_armor ],
 ["red_hand_plate", "Red Hand Plate", [("red_hand_plate",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 1500 , weight(27)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(20)|difficulty(8) ,imodbits_armor ],
["red_hand_shield_weak", "Red Hand Shield", [("red_hand_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 200 , weight(3.5)|hit_points(100)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["red_hand_shield_normal", "Red Hand Shield", [("red_hand_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 600 , weight(3.5)|hit_points(300)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["red_hand_shield_strong", "Red Hand Shield", [("red_hand_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 1200 , weight(3.5)|hit_points(500)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["red_hand_bell_helm", "Red Hand Bell Helm", [("red_hand_bell_helm",0)], itp_merchandise| itp_type_head_armor   ,0,
  800 , weight(2)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
 ["red_hand_kettle_helm", "Red Hand Kettle Helm", [("red_hand_kettle_helm",0)], itp_merchandise| itp_type_head_armor   ,0,
  1000 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
 ["red_hand_plate_gauntlets","Red Hand Plate Gauntlets", [("red_hand_plate_gauntlets_L",0), ("red_hand_plate_gauntlets_Lx",0)], itp_merchandise|itp_type_hand_armor,0,
  860, weight(0.75)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor],
 ["red_hand_greaves_spurs", "Red Hand Greaves with Spurs", [("red_hand_greaves_spurs",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 960 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(7) ,imodbits_plate ],
 ["red_hand_greaves", "Red Hand Greaves", [("red_hand_greaves",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 960 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(7) ,imodbits_plate ],
 ["red_hand_fast_crossbow", "Red Hand Fast Crossbow", [("crossbow_c",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
3000 , weight(3.5)|difficulty(9)|spd_rtng(115) | shoot_speed(68) | thrust_damage(58 ,pierce)|max_ammo(1),imodbits_crossbow ],
  ["red_arm_club",  "Red Arm Club", [("Faradon_IronClub",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
400 , weight(3.5)|difficulty(0)|spd_rtng(98) | weapon_length(75)|swing_damage(28 , blunt) | thrust_damage(0 ,  pierce),imodbits_pick ],
 ["red_arm_hammer",  "Red Arm Hammer", [("Faradon_warhammer",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
350 , weight(3.5)|difficulty(0)|spd_rtng(98) | weapon_length(75)|swing_damage(28 , blunt) | thrust_damage(0 ,  pierce),imodbits_pick ],

 ["two_rivers_armor", "Two River's Armor", [("two_rivers_armor",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 750 , weight(5)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
 ["two_rivers_long_bow", "Long Bow", [("long_bow",0),("long_bow_carry",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bow_back, 
2000 , weight(1.75)|difficulty(3)|spd_rtng(105) | shoot_speed(70) | thrust_damage(28 ,  pierce),imodbits_bow ],
 ["halberd","Halberd", [("talak_halberd",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,
 350 , weight(2.5)|difficulty(10)|spd_rtng(89) | weapon_length(155)|swing_damage(36 , cut) | thrust_damage(25 ,  pierce),imodbits_polearm ],


# Southlander Coalition
 ["mayene_recruit_tunic", "Mayene Recruit Tunic", [("mayene_recruit_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
200 , weight(10)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(4) ,imodbits_armor ],
 ["mayene_army_armor", "Mayene Army Armor", [("mayene_army_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
500 , weight(15)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(17)|difficulty(6) ,imodbits_armor ],
 ["mayene_plate", "Mayene Plate", [("mayene_plate",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 1500 , weight(27)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(20)|difficulty(8) ,imodbits_armor ],
["mayene_shield_weak", "Mayene Shield", [("mayene_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 200 , weight(3.5)|hit_points(100)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["mayene_shield_normal", "Mayene Shield", [("mayene_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 600 , weight(3.5)|hit_points(300)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
["mayene_shield_strong", "Mayene Shield", [("mayene_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 1000 , weight(3.5)|hit_points(500)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["mayene_winged_guard_helmet", "Mayene Winged Guard Helmet", [("mayene_winged_guard_helmet",0)], itp_merchandise| itp_type_head_armor   ,0,
  800 , weight(2)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
 ["mayene_greaves", "Mayene Greaves", [("mayene_greaves",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 960 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(7) ,imodbits_plate ],
 ["mayene_gauntlets_red","Mayene Gauntlets", [("mayene_gauntlets_red_L",0), ("mayene_gauntlets_red_Lx",0)], itp_merchandise|itp_type_hand_armor,0,
  860, weight(0.75)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor],
 ["mayene_sword", "Mayene_sword", [("talak_katzbalger",0),("talak_scab_katzbalger", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 480 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(100)|swing_damage(29 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high ],

 ["cairhien_recruit_tunic", "Cairhien Recruit Tunic", [("cairhien_recruit_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
200 , weight(10)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(4) ,imodbits_armor ],
 ["cairhien_army_armor", "Cairhien Army Armor", [("cairhien_army_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
500 , weight(15)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(17)|difficulty(6) ,imodbits_armor ],
 ["cairhien_plate", "Cairhien Plate", [("cairhien_plate",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 1200 , weight(27)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(20)|difficulty(8) ,imodbits_armor ],
["cairhien_shield_weak", "Cairhien Shield", [("cairhien_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 200 , weight(3.5)|hit_points(100)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["cairhien_shield_normal", "Cairhien Shield", [("cairhien_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 600 , weight(3.5)|hit_points(300)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["cairhien_shield_strong", "Cairhien Shield", [("cairhien_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 1000 , weight(3.5)|hit_points(500)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["cairhien_helmet", "Cairhien Helmet", [("open_sallet",0)], itp_merchandise| itp_type_head_armor   ,0,
  500 , weight(2)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

 ["illian_recruit_tunic", "Illian Recruit Tunic", [("illian_recruit_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
200 , weight(10)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(4) ,imodbits_armor ],
 ["illian_army_armor", "Illian Army Armor", [("illian_army_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
500 , weight(15)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(17)|difficulty(6) ,imodbits_armor ],
 ["illian_companion_surcoat", "Illian Companion Surcoat", [("illian_companion_surcoat",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1200 , weight(27)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(18)|difficulty(8) ,imodbits_armor ],
 ["illian_companion_captain_surcoat", "Illian Companion Captain Surcoat", [("illian_companion_captain_surcoat",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 1800 , weight(27)|abundance(100)|head_armor(0)|body_armor(55)|leg_armor(21)|difficulty(10) ,imodbits_armor ],
["illian_shield_weak", "Illian Shield", [("illian_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 200 , weight(3.5)|hit_points(200)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["illian_shield_normal", "Illian Shield", [("illian_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 600 , weight(3.5)|hit_points(400)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["illian_shield_strong", "Illian Shield", [("illian_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 1200 , weight(3.5)|hit_points(600)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["illian_helmet", "Illian Helmet", [("illian_helmet",0)], itp_merchandise| itp_type_head_armor   ,0,
  800 , weight(2)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
 ["illian_seax", "Illian Seax", [("talak_seax",0),("talak_scab_seax", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 480 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(80)|swing_damage(25 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],

 ["large_heron_mark_blade", "Large Heron Mark Blade", [("large_heron_mark_blade",0),("large_heron_mark_blade_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn,
 2000 , weight(3)|difficulty(11)|spd_rtng(94) | weapon_length(130)|swing_damage(40 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_high ],
 ["heron_mark_blade", "Heron Mark Blade", [("heron_mark_blade",0),("heron_mark_blade_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 1500 , weight(1.5)|difficulty(9)|spd_rtng(99) | weapon_length(100)|swing_damage(35 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high ],

  ["murandy_recruit_tunic", "Murandy Recruit Tunic", [("murandy_recruit_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
200 , weight(10)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(4) ,imodbits_armor ],
 ["murandy_leather_armor", "Murandy Leather Armor", [("murandy_leather_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
500 , weight(15)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(17)|difficulty(6) ,imodbits_armor ],
 ["murandy_elite_armor", "Murandy Elite Armor", [("murandy_elite_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 1500 , weight(27)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(18)|difficulty(8) ,imodbits_armor ],
["murandy_shield_weak", "Murandy Shield", [("murandy_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 200 , weight(3.5)|hit_points(100)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["murandy_shield_normal", "Murandy Shield", [("murandy_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 600 , weight(3.5)|hit_points(300)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["murandy_shield_strong", "Murandy Shield", [("murandy_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 1000 , weight(3.5)|hit_points(500)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],

 ["altara_recruit_armor", "Altara Recruit Armor", [("altara_recruit_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
200 , weight(10)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(4) ,imodbits_armor ],
 ["altara_army_armor", "Altara Army Armor", [("altara_army_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
600 , weight(15)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(17)|difficulty(6) ,imodbits_armor ],
 ["altara_royal_guard_armor", "Altara Royal Guard Armor", [("altara_royal_guard_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 1200 , weight(27)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(20)|difficulty(8) ,imodbits_armor ],
["altara_shield_weak", "Altara Shield", [("altara_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 200 , weight(3.5)|hit_points(100)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["altara_shield_normal", "Altara Shield", [("altara_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 500 , weight(3.5)|hit_points(300)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["altara_shield_strong", "Altara Shield", [("altara_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 1000 , weight(3.5)|hit_points(500)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["altara_royal_guard_helmet", "Altara Royal Guard Helmet", [("altara_royal_guard_helmet",0)], itp_merchandise| itp_type_head_armor   ,0,
  800 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
 ["altara_green_boots", "Altara Green Boots", [("altara_green_boots",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 500 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(7) ,imodbits_plate ],
 ["altara_royal_guard_boots", "Altara Royal Guard Boots", [("altara_royal_guard_boots",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 960 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(7) ,imodbits_plate ],
 ["altara_royal_guard_halberd", "Altara Royal Guard Halberd", [("altara_royal_guard_halberd",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_penalty_with_shield|itp_wooden_parry, itc_staff|itcf_carry_spear,
 800 , weight(2.5)|difficulty(10)|spd_rtng(89) | weapon_length(155)|swing_damage(36 , cut) | thrust_damage(25 ,  pierce),imodbits_polearm ],

  ["arad_doman_recruit_tunic", "Arad Doman Recruit Tunic", [("arad_doman_recruit_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
200 , weight(10)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(4) ,imodbits_armor ],
 ["arad_doman_army_armor", "Arad Doman Army Armor", [("arad_doman_army_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
500 , weight(15)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(17)|difficulty(6) ,imodbits_armor ],
 ["arad_doman_elite_armor", "Arad Doman Elite Armor", [("arad_doman_elite_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 1200 , weight(27)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(20)|difficulty(8) ,imodbits_armor ],
["arad_doman_shield_weak", "Arad Doman Shield", [("arad_doman_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 200 , weight(3.5)|hit_points(200)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["arad_doman_shield_normal", "Arad Doman Shield", [("arad_doman_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 500 , weight(3.5)|hit_points(400)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["arad_doman_shield_strong", "Arad Doman Shield", [("arad_doman_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 1000 , weight(3.5)|hit_points(600)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],


# Southlander Alliance
  ["tear_recruit_tunic", "Tear Recruit Tunic", [("tear_recruit_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 200 , weight(10)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(4) ,imodbits_armor ],
 ["tear_plate", "Tear Plate", [("tear_plate",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 800 , weight(15)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(15)|difficulty(6) ,imodbits_armor ],
 ["tear_gilded_plate", "Tear Gilded Plate", [("tear_gilded_plate",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian |itp_civilian ,0, 
 1200 , weight(15)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(17)|difficulty(6) ,imodbits_armor ],
 ["tear_defender_armor", "Tear Defender Armor", [("tear_defender_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 1500 , weight(27)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(18)|difficulty(8) ,imodbits_armor ],
 ["tear_defender_captain_armor", "Tear Defender Captain Armor", [("tear_defender_captain_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 2000 , weight(27)|abundance(100)|head_armor(0)|body_armor(55)|leg_armor(21)|difficulty(10) ,imodbits_armor ],
 ["tear_defender_gauntlets","Tear Defender Gauntlets", [("tear_defender_gauntlet_L",0), ("tear_defender_gauntlet_Lx",0)], itp_merchandise|itp_type_hand_armor,0,
  860, weight(0.75)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor],
 ["tear_helmet", "Tear Helmet", [("kettlehat",0)], itp_merchandise| itp_type_head_armor   ,0,
  800 , weight(2)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
 ["tear_elite_helmet", "Tear Elite Helmet", [("combed_morion",0)], itp_merchandise| itp_type_head_armor   ,0,
  850 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
 ["tear_defender_helmet", "Tear Defender Helmet", [("combed_morion_blued",0)], itp_merchandise| itp_type_head_armor   ,0,
  1000 , weight(2)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["tear_shield_weak", "Tear Shield", [("tear_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 200 , weight(3.5)|hit_points(100)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["tear_shield_normal", "Tear Shield", [("tear_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 600 , weight(3.5)|hit_points(300)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["tear_shield_strong", "Tear Shield", [("tear_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 1000 , weight(3.5)|hit_points(500)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["flamberge", "Flamberge", [("flamberge",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back,
 650 , weight(3)|difficulty(9)|spd_rtng(94) | weapon_length(145)|swing_damage(35 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high ],

 ["andor_recruit_tunic", "Andor Recruit Tunic", [("andor_recruit_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 200 , weight(10)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(4) ,imodbits_armor ],
 ["andor_army_armor", "Andor Army Armor", [("andor_army_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 600 , weight(15)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(12)|difficulty(6) ,imodbits_armor ],
 ["andor_plate", "Andor Plate", [("andor_plate",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 
 1200 , weight(15)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(17)|difficulty(6) ,imodbits_armor ],
 ["andor_queens_guard_armor", "Andor Queens Guard Armor", [("andor_queens_guard_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 1500 , weight(27)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(18)|difficulty(8) ,imodbits_armor ],
["andor_shield_weak", "Andor Shield", [("andor_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 277 , weight(3.5)|hit_points(100)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["andor_shield_normal", "Andor Shield", [("andor_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 600 , weight(3.5)|hit_points(300)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["andor_shield_strong", "Andor Shield", [("andor_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 1200 , weight(3.5)|hit_points(500)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],

 ["ghealdan_recruit_tunic", "Ghealdan Recruit Tunic", [("ghealdan_recruit_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
200 , weight(10)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(4) ,imodbits_armor ],
 ["ghealdan_army_armor", "Ghealdan Army Armor", [("ghealdan_army_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
600 , weight(15)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(17)|difficulty(6) ,imodbits_armor ],
 ["ghealdan_plate", "Ghealdan Plate", [("ghealdan_plate",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 1500 , weight(27)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(20)|difficulty(8) ,imodbits_armor ],
["ghealdan_shield_weak", "Ghealdan Shield", [("ghealdan_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 277 , weight(3.5)|hit_points(200)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["ghealdan_shield_normal", "Ghealdan Shield", [("ghealdan_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 600 , weight(3.5)|hit_points(400)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["ghealdan_shield_strong", "Ghealdan Shield", [("ghealdan_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 1000 , weight(3.5)|hit_points(600)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],

  ["far_madding_recruit_tunic", "Far Madding Recruit Tunic", [("far_madding_recruit_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 200 , weight(10)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(4) ,imodbits_armor ],
 ["far_madding_armor", "Far Madding Armor", [("far_madding_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 600 , weight(15)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(17)|difficulty(6) ,imodbits_armor ],
["far_madding_shield_weak", "Far Madding Shield", [("far_madding_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 277 , weight(3.5)|hit_points(100)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["far_madding_shield_normal", "Far Madding Shield", [("far_madding_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 600 , weight(3.5)|hit_points(300)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],

  ["tarabon_recruit_tunic", "Tarabon Recruit Tunic", [("tarabon_recruit_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
200 , weight(10)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(4) ,imodbits_armor ],
 ["tarabon_army_armor", "Tarabon Army Armor", [("tarabon_army_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
600 , weight(15)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(17)|difficulty(6) ,imodbits_armor ],
 ["tarabon_elite_armor", "Tarabon Elite Armor", [("tarabon_elite_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 1200 , weight(27)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(20)|difficulty(8) ,imodbits_armor ],
["tarabon_shield_weak", "Tarabon Shield", [("tarabon_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 277 , weight(3.5)|hit_points(100)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["tarabon_shield_normal", "Tarabon Shield", [("tarabon_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 600 , weight(3.5)|hit_points(300)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["tarabon_shield_strong", "Tarabon Shield", [("tarabon_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 1000 , weight(3.5)|hit_points(500)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],

 ["amadicia_recruit_tunic", "Amadicia Recruit Tunic", [("amadicia_recruit_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
200 , weight(10)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(4) ,imodbits_armor ],
 ["amadicia_army_armor", "Amadicia Army Armor", [("amadicia_army_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
600 , weight(15)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(17)|difficulty(6) ,imodbits_armor ],
 ["amadicia_elite_armor", "Amadicia Elite Armor", [("amadicia_elite_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 1200 , weight(27)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(18)|difficulty(8) ,imodbits_armor ],
["amadicia_shield_weak", "Amadicia Shield", [("amadicia_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 200 , weight(3.5)|hit_points(100)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["amadicia_shield_normal", "Amadicia Shield", [("amadicia_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 600 , weight(3.5)|hit_points(300)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["amadicia_shield_strong", "Amadicia Shield", [("amadicia_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 1000 , weight(3.5)|hit_points(500)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],

 ["whitecloak_recruit_tunic", "Whitecloak Recruit Tunic", [("whitecloak_recruit_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
200 , weight(10)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(4) ,imodbits_armor ],
  ["whitecloak_questioner_tabbard", "Whitecloak Questioner Tabbard", [("whitecloak_questioner_tabbard",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
800 , weight(24)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
 ["whitecloak_tabbard", "Whitecloak Tabbard", [("whitecloak_tabbard",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
1000 , weight(24)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["whitecloak_shield_weak", "Whitecloak Shield", [("whitecloak_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 277 , weight(3.5)|hit_points(100)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["whitecloak_shield_normal", "Whitecloak Shield", [("whitecloak_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 600 , weight(3.5)|hit_points(300)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["whitecloak_shield_strong", "Whitecloak Shield", [("whitecloak_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 1000 , weight(3.5)|hit_points(500)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["whitecloak_helmet", "Whitecloak Helmet", [("open_sallet_coif",0)], itp_merchandise| itp_type_head_armor   ,0,
  800 , weight(2)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],


# Borderlands
 ["shienar_recruit_tunic", "Shienar Recruit Tunic", [("shienar_recruit_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
200 , weight(10)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(4) ,imodbits_armor ],
 ["shienar_leather_armor", "Shienar Leather Armor", [("shienar_leather_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
500 , weight(15)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(17)|difficulty(6) ,imodbits_armor ],
 ["shienar_captain_armor", "Shienar Captain Armor", [("milanese_plate",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 4000 , weight(27)|abundance(100)|head_armor(0)|body_armor(65)|leg_armor(30)|difficulty(10) ,imodbits_armor ],
 ["shienar_captain_gauntlets","Shienar Captain Gauntlets", [("milanese_gauntlet_L",0), ("milanese_gauntlet_Lx",0)], itp_merchandise|itp_type_hand_armor,0,
  1200, weight(0.75)|abundance(100)|body_armor(8)|difficulty(0),imodbits_armor],
["shienar_shield_weak", "Shienar Shield", [("shienar_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 277 , weight(3.5)|hit_points(100)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["shienar_shield_normal", "Shienar Shield", [("shienar_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 600 , weight(3.5)|hit_points(300)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["shienar_shield_strong", "Shienar Shield", [("shienar_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 1000 , weight(3.5)|hit_points(500)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["heavy_charger","Heavy Charger", [("heavy_charger",0)], itp_merchandise|itp_type_horse, 0,
  4000,abundance(35)|hit_points(200)|body_armor(63)|difficulty(5)|horse_speed(41)|horse_maneuver(46)|horse_charge(35)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_4]],

 ["arafel_recruit_tunic", "Arafel Recruit Tunic", [("arafel_recruit_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 200 , weight(10)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(4) ,imodbits_armor ],
 ["arafel_army_armor", "Arafel Army Armor", [("arafel_army_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 600 , weight(15)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(12)|difficulty(6) ,imodbits_armor ],
 ["arafel_tabbard", "Arafel Tabbard", [("arafel_tabbard",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 1200 , weight(15)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(17)|difficulty(6) ,imodbits_armor ],
 ["arafel_mail_and_plate", "Arafel Mail and Plate", [("arafel_mail_and_plate",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 3000 , weight(27)|abundance(100)|head_armor(0)|body_armor(55)|leg_armor(18)|difficulty(8) ,imodbits_armor ],
["arafel_shield_weak", "Arafel Shield", [("arafel_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 277 , weight(3.5)|hit_points(100)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["arafel_shield_normal", "Arafel Shield", [("arafel_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 600 , weight(3.5)|hit_points(300)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["arafel_shield_strong", "Arafel Shield", [("arafel_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 1000 , weight(3.5)|hit_points(500)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],

 ["kandor_recruit_tunic", "Kandor Recruit Tunic", [("kandor_recruit_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 200 , weight(10)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(4) ,imodbits_armor ],
 ["kandor_leather_armor", "Kandor Leather Armor", [("kandor_leather_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 500 , weight(15)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(12)|difficulty(6) ,imodbits_armor ],
 ["kandor_army_armor", "Kandor Army Armor", [("kandor_army_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 600 , weight(15)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(14)|difficulty(6) ,imodbits_armor ],
 ["kandor_surcoat", "Kandor Surcoat", [("kandor_surcoat",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1000 , weight(27)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
 ["visored_sallet", "Visored Sallet", [("visored_sallet",0)], itp_merchandise| itp_type_head_armor   ,0,
  800 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
 ["kandor_visored_sallet", "Kandor Visored Sallet", [("kandor_visored_sallet",0)], itp_merchandise| itp_type_head_armor   ,0,
  900 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
["kandor_shield_weak", "Kandor Shield", [("kandor_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 277 , weight(3.5)|hit_points(200)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["kandor_shield_normal", "Kandor Shield", [("kandor_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 600 , weight(3.5)|hit_points(400)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["kandor_shield_strong", "Kandor Shield", [("kandor_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 1000 , weight(3.5)|hit_points(600)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["kandor_long_mace", "Kandor Long Mace", [("talak_long_mace",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear, 
450 , weight(4.5)|difficulty(13)|spd_rtng(95) | weapon_length(85)|swing_damage(38 , pierce) | thrust_damage(0 ,  pierce),imodbits_mace ],

 ["saldaea_recruit_tunic", "Saldaea Recruit Tunic", [("saldaea_recruit_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 200 , weight(10)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(4) ,imodbits_armor ],
 ["saldaea_warrior_outfit", "Saldaea Warrior Outfit", [("saldaea_warrior_outfit",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 600 , weight(15)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(12)|difficulty(6) ,imodbits_armor ],
 ["saldaea_army_armor", "Saldaea Army Armor", [("saldaea_army_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 1000 , weight(15)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(14)|difficulty(6) ,imodbits_armor ],
  ["heavy_lamellar_armor_wot", "Heavy Lamellar Armor", [("heavy_lamellar_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 1400 , weight(27)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
["saldaea_shield_weak", "Saldaea Shield", [("saldaea_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 277 , weight(3.5)|hit_points(200)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["saldaea_shield_normal", "Saldaea Shield", [("saldaea_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 600 , weight(3.5)|hit_points(400)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["saldaea_shield_strong", "Saldaea Shield", [("saldaea_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 1000 , weight(3.5)|hit_points(600)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["saldaea_warhorse","Saldaea War Horse", [("kher_warhorse",0)], itp_merchandise|itp_type_horse, 0,
  2500,abundance(50)|hit_points(150)|body_armor(40)|difficulty(4)|horse_speed(45)|horse_maneuver(43)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_4]],
 ["saldaea_charger","Saldaea Charger", [("sarranid_heavy_horse3",0)], itp_merchandise|itp_type_horse, 0,
  3000,abundance(45)|hit_points(175)|body_armor(50)|difficulty(4)|horse_speed(48)|horse_maneuver(45)|horse_charge(30)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], [fac_kingdom_4]],


# White Tower
 ["aes_sedai_white_dress", "White Ajah Dress", [("aes_sedai_white_ajah_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
 ["aes_sedai_grey_dress", "Grey Ajah Dress", [("aes_sedai_grey_ajah_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
 ["aes_sedai_blue_dress", "Blue Ajah Dress", [("aes_sedai_blue_ajah_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
 ["aes_sedai_yellow_dress", "Yellow Ajah Dress", [("aes_sedai_yellow_ajah_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
 ["aes_sedai_green_dress", "Green Ajah Dress", [("aes_sedai_green_ajah_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
 ["aes_sedai_red_dress", "Red Ajah Dress", [("aes_sedai_red_ajah_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
 ["aes_sedai_brown_dress", "Brown Ajah Dress", [("aes_sedai_brown_ajah_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],

 ["aes_sedai_white_shoes", "White Ajah Shoes", [("aes_sedai_white_ajah_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
 ["aes_sedai_grey_shoes", "Grey Ajah Shoes", [("aes_sedai_grey_ajah_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
 ["aes_sedai_blue_shoes", "Blue Ajah Shoes", [("aes_sedai_blue_ajah_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
 ["aes_sedai_yellow_shoes", "Yellow Ajah Shoes", [("aes_sedai_yellow_ajah_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
 ["aes_sedai_green_shoes", "Green Ajah Shoes", [("aes_sedai_green_ajah_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
 ["aes_sedai_red_shoes", "Red Ajah Shoes", [("aes_sedai_red_ajah_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
 ["aes_sedai_brown_shoes", "Brown Ajah Shoes", [("aes_sedai_brown_ajah_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],

 ["veteran_aes_sedai_white_shoes", "White Ajah Shoes", [("aes_sedai_white_ajah_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
 ["veteran_aes_sedai_grey_shoes", "Grey Ajah Shoes", [("aes_sedai_grey_ajah_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
 ["veteran_aes_sedai_blue_shoes", "Blue Ajah Shoes", [("aes_sedai_blue_ajah_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
 ["veteran_aes_sedai_yellow_shoes", "Yellow Ajah Shoes", [("aes_sedai_yellow_ajah_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
 ["veteran_aes_sedai_green_shoes", "Green Ajah Shoes", [("aes_sedai_green_ajah_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
 ["veteran_aes_sedai_red_shoes", "Red Ajah Shoes", [("aes_sedai_red_ajah_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
 ["veteran_aes_sedai_brown_shoes", "Brown Ajah Shoes", [("aes_sedai_brown_ajah_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],

 ["novice_dress", "Novice Dress", [("novice_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(4)|leg_armor(4)|difficulty(0) ,imodbits_cloth],
 ["accepted_dress", "Accepted Dress", [("accepted_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 300 , weight(3)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(6)|difficulty(0) ,imodbits_cloth],

 ["novice_accepted_damane_shoes", "Novice Shoes", [("novice_accepted_damane_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0, 25 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],

# ["wig_blond_long", "Wig Blonde Long", [("wig_blond_long",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_blond_bun", "Wig Blonde Bun", [("wig_blond_bun",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_blond_longer", "Wig Blonde Longer", [("wig_blond_longer",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_blond_ponytail", "Wig Blonde Ponytail", [("wig_blond_ponytail",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_blond_braid", "Wig Blonde Braid", [("wig_blond_braid",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_blond_full_braid", "Wig Blonde Full Braid", [("wig_blond_full_braid",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_blond_short", "Wig Blonde Short", [("wig_blond_short",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_man_blonde_short", "Wig Man Blonde Short", [("wig_man_blonde_short",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_man_blonde_long", "Wig Man Blonde Long", [("wig_man_blonde_long",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

# ["wig_black_long", "Wig Black Long", [("wig_black_long",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_black_bun", "Wig Black Bun", [("wig_black_bun",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_black_longer", "Wig Black Longer", [("wig_black_longer",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_black_ponytail", "Wig Black Ponytail", [("wig_black_ponytail",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_black_braid", "Wig Black Braid", [("wig_black_braid",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_black_full_braid", "Wig Black Full Braid", [("wig_black_full_braid",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_black_short", "Wig Black Short", [("wig_black_short",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_man_black_short", "Wig Man Black Short", [("wig_man_black_short",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_man_black_long", "Wig Man Black Long", [("wig_man_black_long",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

# ["wig_red_long", "Wig Red Long", [("wig_red_long",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_red_bun", "Wig Red Bun", [("wig_red_bun",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_red_longer", "Wig Red Longer", [("wig_red_longer",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_red_ponytail", "Wig Red Ponytail", [("wig_red_ponytail",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_red_braid", "Wig Red Braid", [("wig_red_braid",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_red_full_braid", "Wig Red Full Braid", [("wig_red_full_braid",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_red_short", "Wig Red Short", [("wig_red_short",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_man_red_short", "Wig Man Red Short", [("wig_man_red_short",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_man_red_long", "Wig Man Red Long", [("wig_man_red_long",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

# ["wig_brown_long", "Wig Brown Long", [("wig_brown_long",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_brown_bun", "Wig Brown Bun", [("wig_brown_bun",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_brown_longer", "Wig Brown Longer", [("wig_brown_longer",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_brown_ponytail", "Wig Brown Ponytail", [("wig_brown_ponytail",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_brown_braid", "Wig Brown Braid", [("wig_brown_braid",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_brown_full_braid", "Wig Brown Full Braid", [("wig_brown_full_braid",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_brown_short", "Wig Brown Short", [("wig_brown_short",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_man_brown_short", "Wig Man Brown Short", [("wig_man_brown_short",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_man_brown_long", "Wig Man Brown Long", [("wig_man_brown_long",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

# ["wig_white_long", "Wig White Long", [("wig_white_long",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_white_bun", "Wig White Bun", [("wig_white_bun",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_white_longer", "Wig White Longer", [("wig_white_longer",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_white_ponytail", "Wig White Ponytail", [("wig_white_ponytail",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_white_braid", "Wig White Braid", [("wig_white_braid",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_white_full_braid", "Wig White Full Braid", [("wig_white_full_braid",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_white_short", "Wig White Short", [("wig_white_short",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_man_white_short", "Wig Man White Short", [("wig_man_white_short",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["wig_man_white_long", "Wig Man White Long", [("wig_man_white_long",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 6 , weight(0.75)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["white_tower_patrol_tunic", "White Tower Patrol Tunic", [("white_tower_patrol_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
200 , weight(10)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(4) ,imodbits_armor ],
 ["white_tower_guard_armor", "White Tower Guard Armor", [("white_tower_guard_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
500 , weight(15)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(17)|difficulty(6) ,imodbits_armor ],
 ["white_tower_captain_armor", "White Tower Captain Armor", [("white_tower_captain",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
600 , weight(20)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(20)|difficulty(8) ,imodbits_armor ],
 
 ["street_patrol_club",  "Street Patrol Club", [("Faradon_LargeClub",0)], itp_type_one_handed_wpn|itp_can_knock_down|itp_merchandise| itp_primary|itp_wooden_parry, itc_scimitar|itcf_carry_mace_left_hip, 
200 , weight(3.5)|difficulty(0)|spd_rtng(98) | weapon_length(75)|swing_damage(28 , blunt) | thrust_damage(0 ,  pierce),imodbits_pick ],
["steel_buckler2", "Steel Buckler", [("steel_buckler2",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,
 697 , weight(4)|hit_points(750)|body_armor(17)|spd_rtng(61)|shield_width(35),imodbits_shield ],
["trainee_gambeson", "Gambeson", [("gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 260 , weight(5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],


 # Aiel Nation
 ["wise_one_dress", "Wise One Dress", [("wise_one_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
   500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
 ["wise_one_dress_with_shawl", "Wise One Dress with Shawl", [("wise_one_dress_with_shawl",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
   600 , weight(3)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(15)|difficulty(0) ,imodbits_cloth],

 ["cadinsor_grey", "Grey Cadin'sor", [("cadinsor_grey",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 300 , weight(5)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(15)|difficulty(4) ,imodbits_armor ],
 ["cadinsor_green", "Green Cadin'sor", [("cadinsor_green",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 600 , weight(6)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(17)|difficulty(6) ,imodbits_armor ],
 ["cadinsor", "Cadin'sor", [("cadinsor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 1200 , weight(7)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(20)|difficulty(6) ,imodbits_armor ],
 ["shoufa_grey", "Grey Shoufa", [("shoufa_grey",0)], itp_merchandise| itp_type_head_armor   ,0,
  200 , weight(1)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
 ["shoufa_green", "Green Shoufa", [("shoufa_green",0)], itp_merchandise| itp_type_head_armor   ,0,
  500 , weight(1)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
 ["shoufa", "Shoufa", [("shoufa",0)], itp_merchandise| itp_type_head_armor   ,0,
  800 , weight(1)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
 ["cadinsor_boots_grey", "Grey Cadin'sor Boots", [("cadinsor_boots_grey",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 174 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(13)|difficulty(0) ,imodbits_cloth ],
 ["cadinsor_boots_green", "Green Cadin'sor Boots", [("cadinsor_boots_green",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 250 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
 ["cadinsor_boots", "Cadin'sor Boots", [("cadinsor_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 500 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(19)|difficulty(0) ,imodbits_cloth ],

["hide_buckler_weak", "Hide Buckler", [("hide_buckler",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 277 , weight(3.5)|hit_points(200)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["hide_buckler_normal", "Hide Buckler", [("hide_buckler",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 600 , weight(3.5)|hit_points(400)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["hide_buckler_strong", "Hide Buckler", [("hide_buckler",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 1000 , weight(3.5)|hit_points(600)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],

 ["aiel_spear", "Aiel Spear", [("spear_g_1-9m",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_staff|itcf_carry_spear,
 800 , weight(2.0)|difficulty(0)|spd_rtng(120) | weapon_length(110)|swing_damage(30 , cut) | thrust_damage(35 ,  pierce),imodbits_polearm ],
 ["aiel_knife", "Aiel Knife", [("talak_seax",0),("talak_scab_seax", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 550 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(75)|swing_damage(30 , cut) | thrust_damage(28 ,  pierce),imodbits_sword_high ],


 # Seanchan
 ["damane_dress", "Damane Dress", [("damane_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
  200 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
 ["suldam_dress", "Sul'dam Dress", [("suldam_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
  600 , weight(3)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
 ["damane_boots", "Damane Boots", [("damane_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 50 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
 ["suldam_boots", "Sul'dam Boots", [("suldam_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 174 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],

 ["seanchan_low_armor", "Seanchan Low Armor", [("armure_samurai02",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 300 , weight(10)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(4) ,imodbits_armor ],
 ["seanchan_middle_armor", "Seanchan Middle Armor", [("armure_samurai01",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 600 , weight(15)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(12)|difficulty(6) ,imodbits_armor ],
 ["seanchan_high_armor", "Seanchan High Armor", [("samurai_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 1000 , weight(15)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(14)|difficulty(6) ,imodbits_armor ],
 ["deathwatch_guard_armor", "Deathwatch Armor", [("deathwatch_guard_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 1500 , weight(27)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
 ["seanchan_low_helmet", "Seanchan Low Helmet", [("casque_samurai02",0)], itp_merchandise| itp_type_head_armor   ,0,
  390 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
 ["seanchan_middle_helmet", "Seanchan Middle Helmet", [("casque_samurai01",0)], itp_merchandise| itp_type_head_armor   ,0,
  500 , weight(2)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
 ["seanchan_high_helmet", "Seanchan High Helmet", [("samurai_helmet",0)], itp_merchandise| itp_type_head_armor   ,0,
  700 , weight(2)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
 ["deathwatch_guard_helmet", "Deathwatch Guard Helmet", [("deathwatch_guard_helmet",0)], itp_merchandise| itp_type_head_armor   ,0,
  900 , weight(2)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
 ["seanchan_low_boots", "Seanchan Low Boots", [("bottes_samurai02",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 200 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(7) ,imodbits_plate ],
 ["seanchan_middle_boots", "Seanchan Middle Boots", [("bottes_samurai01",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature,0,
 350 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(7) ,imodbits_plate ],
 ["seanchan_high_boots", "Seanchan High Boots", [("samurai_boots",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 500 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(7) ,imodbits_plate ],
 ["deathwatch_guard_boots", "Deathwatch Guard Boots", [("deathwatch_guard_boots",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 600 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(35)|difficulty(7) ,imodbits_plate ],
 ["seanchan_low_gloves","Seanchan Low Gloves", [("gants_samurai02_L",0), ("gants_samurai02_Lx",0)], itp_merchandise|itp_type_hand_armor,0,
  300, weight(0.75)|abundance(100)|body_armor(2)|difficulty(0),imodbits_armor],
 ["seanchan_middle_gloves","Seanchan Middle Gloves", [("gants_samurai01_L",0), ("gants_samurai01_Lx",0)], itp_merchandise|itp_type_hand_armor,0,
  400, weight(0.75)|abundance(100)|body_armor(3)|difficulty(0),imodbits_armor],
 ["seanchan_high_gloves","Seanchan High Gloves", [("samurai_gloves_L",0), ("samurai_gloves_Lx",0)], itp_merchandise|itp_type_hand_armor,0,
  500, weight(0.75)|abundance(100)|body_armor(4)|difficulty(0),imodbits_armor],
 ["deathwatch_guard_gloves","Deathwatch Guard Gloves", [("deathwatch_guard_gloves_L",0), ("deathwatch_guard_gloves_Lx",0)], itp_merchandise|itp_type_hand_armor,0,
  600, weight(0.75)|abundance(100)|body_armor(6)|difficulty(0),imodbits_armor],

 ["seanchan_large_sword", "Seanchan Large Sword", [("no_dachi_samurai11",0),("no_dachi_samurai11_fourreau", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn,
 1000 , weight(3)|difficulty(10)|spd_rtng(94) | weapon_length(130)|swing_damage(37 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high ],
 ["seanchan_sword", "Seanchan Sword", [("katana_samurai10",0),("katana_samurai10_fourreau", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 800 , weight(1.5)|difficulty(8)|spd_rtng(99) | weapon_length(100)|swing_damage(31 , cut) | thrust_damage(25 ,  pierce),imodbits_sword_high ],
 ["seanchan_straight_sword", "Seanchan Straight Sword", [("wakizashi_samurai02",0),("wakizashi_samurai02_fourreau", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 300 , weight(1.5)|difficulty(6)|spd_rtng(99) | weapon_length(95)|swing_damage(27 , cut) | thrust_damage(21 ,  pierce),imodbits_sword_high ],


 # Shadowspawn
 ["trolloc_hawk_helmet", "Trolloc Hawk Helmet", [("trolloc_hawk_helmet",0)], itp_type_head_armor|itp_covers_head   ,0,
  300 , weight(2)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
 ["trolloc_wolf_helmet", "Trolloc Wolf Helmet", [("trolloc_wolf_helmet",0)], itp_type_head_armor|itp_covers_head    ,0,
  500 , weight(2)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
 ["trolloc_goat_helmet", "Trolloc Goat Helmet", [("trolloc_goat_helmet",0)], itp_type_head_armor|itp_covers_head   ,0,
  900 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
 ["myrddraal_hood_helmet", "Myrddraal Helmet", [("myrddraal_hood_helmet",0)], itp_type_head_armor|itp_covers_head   ,0,
  1500 , weight(2)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
 ["draghkar_helmet", "Draghkar Helmet", [("draghkar_helmet",0)], itp_type_head_armor|itp_covers_head   ,0,
  1200 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

 ["trolloc_weak_armor", "Trolloc Weak Armor", [("trolloc_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 300 , weight(10)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(4) ,imodbits_armor ],
 ["trolloc_normal_armor", "Trolloc Normal Armor", [("trolloc_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 500 , weight(15)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(12)|difficulty(6) ,imodbits_armor ],
 ["trolloc_strong_armor", "Trolloc Strong Armor", [("trolloc_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 900 , weight(15)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
 ["myrddraal_armor", "Myrddraal Armor", [("myrddraal_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 1500 , weight(15)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(16)|difficulty(8) ,imodbits_armor ],
 ["darkfriend_tunic", "Darkfriend Tunic", [("darkfriend_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 200 , weight(10)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(4) ,imodbits_armor ],
 ["darkfriend_armor", "Darkfriend Armor", [("darkfriend_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 400 , weight(15)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(12)|difficulty(6) ,imodbits_armor ],
 ["darkfriend_plate", "Darkfriend Plate", [("darkfriend_plate",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 800 , weight(15)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(14)|difficulty(7) ,imodbits_armor ],
 ["draghkar_tunic", "Draghkar Tunic", [("draghkar_tunic",0)], itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 400 , weight(15)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(4) ,imodbits_armor ],
 ["dreadlord_coat", "Dreadlord Coat", [("dreadlord_coat",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 800 , weight(15)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(12)|difficulty(6) ,imodbits_armor ],
 ["aes_sedai_black_ajah_dress", "Black Ajah Dress", [("aes_sedai_black_ajah_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
  500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],

 ["aes_sedai_black_ajah_shoes", "Black Ajah Shoes", [("aes_sedai_black_ajah_shoes",0)], itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
  30 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],

 ["black_mail_gauntlets","Black Mail Gauntlets", [("black_mail_gauntlets_L",0), ("black_mail_gauntlets_Lx",0)], itp_merchandise|itp_type_hand_armor,0,
  400, weight(0.75)|abundance(100)|body_armor(5)|difficulty(0),imodbits_armor],
 ["draghkar_gloves","Draghkar Gloves", [("draghkar_gloves_L",0), ("draghkar_gloves_Lx",0)], itp_type_hand_armor,0,
  200, weight(0.75)|abundance(100)|body_armor(5)|difficulty(0),imodbits_armor],

 ["trolloc_mace", "Trolloc Mace", [("mace_morningstar_new",0)], itp_crush_through|itp_type_two_handed_wpn|itp_merchandise|itp_can_knock_down|itp_primary|itp_two_handed|itp_wooden_parry|itp_wooden_attack|itp_unbalanced, itc_nodachi|itcf_carry_spear, 
650 , weight(9)|difficulty(14)|spd_rtng(79) | weapon_length(75)|swing_damage(40 , blunt) | thrust_damage(0 ,  pierce),imodbits_mace ],
  ["myrddraal_blade", "Myrddraal Blade", [("myrddraal_blade",0),("myrddraal_blade_scabbard", ixmesh_carry)], itp_type_two_handed_wpn| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn,
 1900 , weight(3)|difficulty(11)|spd_rtng(94) | weapon_length(130)|swing_damage(40 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_high ],
 ["draghkar_dagger", "Draghkar Dagger", [("dagger_b",0),("dagger_b_scabbard",ixmesh_carry),("dagger_b",imodbits_good),("dagger_b_scabbard",ixmesh_carry|imodbits_good)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn, 
200 , weight(0.75)|difficulty(1)|spd_rtng(109) | weapon_length(47)|swing_damage(12 , cut) | thrust_damage(9 ,  pierce),imodbits_sword_high ],


 ["darkfriend_shield_weak", "Darkfriend Shield", [("darkfriend_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 277 , weight(3.5)|hit_points(100)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["darkfriend_shield_normal", "Darkfriend Shield", [("darkfriend_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 600 , weight(3.5)|hit_points(300)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["darkfriend_shield_strong", "Darkfriend Shield", [("darkfriend_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 1000 , weight(3.5)|hit_points(500)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],


 ["myrddraal_horse","Myrddraal Horse", [("myrddraal_horse",0)], itp_merchandise|itp_type_horse, 0,
 2400,abundance(45)|hit_points(200)|body_armor(35)|difficulty(4)|horse_speed(45)|horse_maneuver(44)|horse_charge(22)|horse_scale(105),imodbits_horse_basic],

 ## Other Items ##

 ["padan_fain_dagger", "Padan Fain's Dagger", [("dagger_b",0),("dagger_b_scabbard",ixmesh_carry),("dagger_b",imodbits_good),("dagger_b_scabbard",ixmesh_carry|imodbits_good)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left|itcf_show_holster_when_drawn, 
5000 , weight(0.75)|difficulty(1)|spd_rtng(109) | weapon_length(47)|swing_damage(22 , cut) | thrust_damage(19 ,  pierce),imodbits_sword_high ],

 ["lord_warhorse_1","Lordly War Horse", [("kher_warhorse1",0)], itp_merchandise|itp_type_horse, 0,
  3000,abundance(3)|hit_points(150)|body_armor(50)|difficulty(4)|horse_speed(45)|horse_maneuver(43)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], []],
 ["lord_warhorse_2","Lordly War Horse", [("lamellar_warhorse1",0)], itp_merchandise|itp_type_horse, 0,
  3000,abundance(3)|hit_points(150)|body_armor(50)|difficulty(4)|horse_speed(45)|horse_maneuver(43)|horse_charge(30)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], []],
 ["lord_warhorse_3","Lordly War Horse", [("sar_warhorse",0)], itp_merchandise|itp_type_horse, 0,
  3000,abundance(3)|hit_points(150)|body_armor(50)|difficulty(4)|horse_speed(45)|horse_maneuver(43)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], []],
 ["lord_warhorse_4","Lordly War Horse", [("sar_warhorse1",0)], itp_merchandise|itp_type_horse, 0,
  3000,abundance(3)|hit_points(150)|body_armor(50)|difficulty(4)|horse_speed(45)|horse_maneuver(43)|horse_charge(30)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], []],
 ["lord_warhorse_5","Lordly War Horse", [("sar_warhorse2",0)], itp_merchandise|itp_type_horse, 0,
  3000,abundance(3)|hit_points(150)|body_armor(50)|difficulty(4)|horse_speed(45)|horse_maneuver(43)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], []],
 ["lord_warhorse_6","Lordly War Horse", [("sar_warhorse3",0)], itp_merchandise|itp_type_horse, 0,
  3000,abundance(3)|hit_points(150)|body_armor(50)|difficulty(4)|horse_speed(45)|horse_maneuver(43)|horse_charge(30)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], []],
 ["lord_warhorse_7","Lordly War Horse", [("sarranid_heavy_horse1",0)], itp_merchandise|itp_type_horse, 0,
  3000,abundance(3)|hit_points(150)|body_armor(50)|difficulty(4)|horse_speed(45)|horse_maneuver(43)|horse_charge(28)|horse_scale(110),imodbits_horse_basic|imodbit_champion, [], []],
 ["lord_warhorse_8","Lordly War Horse", [("sarranid_heavy_horse2",0)], itp_merchandise|itp_type_horse, 0,
  3000,abundance(3)|hit_points(150)|body_armor(50)|difficulty(4)|horse_speed(45)|horse_maneuver(43)|horse_charge(30)|horse_scale(112),imodbits_horse_basic|imodbit_champion, [], []],

  ["whitecloak_inquisitor_tabbard", "Whitecloak High Inquisitor Tabbard", [("whitecloak_inquisitor_tabbard",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
2900 , weight(24)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(8) ,imodbits_armor ],


## Shara Items

 ["shara_recruit_scout_armor", "Shara Recruit Armor", [("shara_recruit_scout_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 200 , weight(10)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(4) ,imodbits_armor ],
 ["shara_bowman_armor", "Shara Bowman Armor", [("shara_bowman_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 200 , weight(10)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(4) ,imodbits_armor ],
 
 ["shara_armsman_armor", "Shara Armsman Armor", [("shara_armsman_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 600 , weight(15)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(12)|difficulty(6) ,imodbits_armor ],
 ["shara_crossbowman_armor", "Shara Crossbowman Armor", [("shara_crossbowman_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 600 , weight(15)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(12)|difficulty(6) ,imodbits_armor ],
 ["shara_marksman_armor", "Shara Marksman Armor", [("shara_marksman_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
 600 , weight(15)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(12)|difficulty(6) ,imodbits_armor ],

 ["shara_town_guard_armor", "Shara Town Guard Armor", [("shara_town_guard_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 
 1200 , weight(15)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(15)|difficulty(6) ,imodbits_armor ],
 
 ["shara_mid_cavalry_armor", "Shara Cavalry Armor", [("shara_mid_cavalry_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 
 1200 , weight(15)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(17)|difficulty(6) ,imodbits_armor ],
 ["shara_border_guard_armor", "Shara Border Guard Armor", [("shara_border_guard_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian ,0, 
 1200 , weight(15)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(17)|difficulty(6) ,imodbits_armor ],
 
 ["shara_elite_armor", "Shara Elite Armor", [("shara_elite_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 1500 , weight(27)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(18)|difficulty(8) ,imodbits_armor ],
 ["shara_shbo_guardsman_armor", "Shara Sh'bo Guardsman Armor", [("shara_shbo_guardsman_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 1500 , weight(27)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(18)|difficulty(8) ,imodbits_armor ],

 ["ayyad_villager_tunic", "Ayyad Villager Tunic", [("ayyad_villager_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
750 , weight(10)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(6)|difficulty(4) ,imodbits_armor ],
 ["ayyad_village_leader_tunic", "Ayyad Village Leader Tunic", [("ayyad_village_leader_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
1000 , weight(15)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(7)|difficulty(6) ,imodbits_armor ],
 ["ayyad_counsel_member_tunic", "Ayyad Counsel Member Tunic", [("ayyad_counsel_member_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
1500 , weight(15)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(8)|difficulty(6) ,imodbits_armor ],

 ["black_turban", "Black Turban", [("tuareg_open_black",0)], itp_merchandise| itp_type_head_armor   ,0,
  200 , weight(1)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
 
 ["black_turban_helmet", "Black Turban with Cap", [("black_sar_helmet1",0)], itp_merchandise| itp_type_head_armor   ,0,
  500 , weight(1)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
 ["black_turban_helmet2", "Black Turban with Cap", [("tuareg_helmet_black",0)], itp_merchandise| itp_type_head_armor   ,0,
  500 , weight(1)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
 
 ["helmet2_brass", "Brass Chain Helmet", [("sar_helmet2_brass",0)], itp_merchandise| itp_type_head_armor   ,0,
  700 , weight(1)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
 
 ["helmet5_brass", "Brass Veil Helmet", [("sar_helmet5",0)], itp_merchandise| itp_type_head_armor   ,0,
  800 , weight(1)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

 ["brass_veil_helm", "Brass Veil Helm", [("brass_veil_helm",0)], itp_merchandise| itp_type_head_armor   ,0,
  900 , weight(2)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],
 ["noken_helmet", "Shara Elite Helmet", [("khergit_noken_helmet",0)], itp_merchandise| itp_type_head_armor   ,0,
  900 , weight(2)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

 ["brass_boots", "Brass Chain Boots", [("sar_brass_boots",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 500 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(7) ,imodbits_plate ],

 ["brass_shield", "Brass Shield", [("brass_shield2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 600 , weight(3.5)|hit_points(300)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["dec_steel_shield", "Decorated Steel Shield", [("dec_steel_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 1000 , weight(3.5)|hit_points(500)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["brass_shield_elite", "Brass Shield", [("brass_shield1",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 1200 , weight(3.5)|hit_points(600)|body_armor(3)|spd_rtng(80)|shield_width(50),imodbits_shield ],

 ["camel","Camel", [("camel",0)], itp_merchandise|itp_type_horse, 0,
 1000,abundance(45)|hit_points(150)|body_armor(25)|difficulty(4)|horse_speed(42)|horse_maneuver(42)|horse_charge(18)|horse_scale(100),imodbits_horse_basic],

 
## Sea Folk Items

 ["sea_folk_tunic", "Sea Folk Tunic", [("sea_folk_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
200 , weight(10)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(8)|difficulty(4) ,imodbits_armor ],
# ["sea_folk_armor", "Sea Folk Armor", [("sea_folk_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
#600 , weight(15)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(15)|difficulty(6) ,imodbits_armor ],
 ["sea_folk_padded_armor", "Sea Folk Padded Armor", [("sea_folk_armor_b",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
800 , weight(15)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(20)|difficulty(6) ,imodbits_armor ], 
 ["sea_folk_elite_armor", "Sea Folk Elite Armor", [("sea_folk_armor_elite",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 1200 , weight(27)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(23)|difficulty(8) ,imodbits_armor ],

 ["sea_folk_elite_helmet", "Sea Folk Helmet", [("sea_folk_elite_helmet",0)], itp_merchandise| itp_type_head_armor   ,0,
  800 , weight(2)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(7) ,imodbits_plate ],

 ["sea_folk_female_tunic", "Sea Folk Tunic", [("sea_folk_female_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
200 , weight(10)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(8)|difficulty(4) ,imodbits_armor ],
 ["sea_folk_female_tunic_2", "Sea Folk Tunic", [("sea_folk_female_tunic_2",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
600 , weight(15)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(15)|difficulty(6) ,imodbits_armor ],
 ["sea_folk_female_armor", "Sea Folk Padded Armor", [("sea_folk_female_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
800 , weight(15)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(20)|difficulty(6) ,imodbits_armor ],  

["wooden_round_shield", "Wooden Round Shield", [("shield_round_g",0)], itp_type_shield|itp_wooden_parry, itcf_carry_round_shield,  80 , weight(2.5)|hit_points(310)|body_armor(8)|spd_rtng(96)|shield_width(40),imodbits_shield ],


## Madmen Items
 
  ["madmen_paint_1", "Madmen Warpaint", [("mad_men_1",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
200 , weight(10)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(8)|difficulty(4) ,imodbits_armor ],
  ["madmen_paint_2", "Madmen Warpaint", [("mad_men_2",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
200 , weight(10)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(8)|difficulty(4) ,imodbits_armor ],
  ["madmen_paint_3", "Madmen Warpaint", [("mad_men_3",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
200 , weight(10)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(8)|difficulty(4) ,imodbits_armor ],
  ["madmen_paint_4", "Madmen Warpaint", [("mad_men_4",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
200 , weight(10)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(8)|difficulty(4) ,imodbits_armor ],

  ["madmen_rawhide_coat", "Clansman Coat", [("coat_of_plates_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
   500 , weight(5)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(10)|difficulty(4) ,imodbits_armor ],


## Toman Head Items
 
  ["toman_head_recruit_tunic", "Toman Head Recruit Tunic", [("toman_head_recruit_tunic",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
200 , weight(10)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(4) ,imodbits_armor ],
 ["toman_head_army_armor", "Toman Head Army Armor", [("toman_head_army_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs|itp_civilian  ,0, 
500 , weight(15)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(17)|difficulty(6) ,imodbits_armor ],
 ["toman_head_mail_and_plate", "Toman Head Mail and Plate", [("toman_head_mail_and_plate",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 1500 , weight(27)|abundance(100)|head_armor(0)|body_armor(54)|leg_armor(20)|difficulty(8) ,imodbits_armor ],
["toman_head_shield_weak", "Toman Head Shield", [("toman_head_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 200 , weight(3.5)|hit_points(100)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 ["toman_head_shield_normal", "Toman Head Shield", [("toman_head_shield",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,
 600 , weight(3.5)|hit_points(300)|body_armor(2)|spd_rtng(80)|shield_width(50),imodbits_shield ],
 


#Mat Cauthon's Items

["mats_hat", "Mat Cauthon's Hat", [("mats_hat",0)],itp_unique|itp_type_head_armor|itp_doesnt_cover_hair|itp_civilian,0,9, weight(1)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
# Feel free to edit values such as weight and armor value etc etc
# Currently Buggy Model 
 
["ashandarei",         "Ashandarei", [("ashandarei_ravens",0)], itp_unique|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_wooden_parry, itc_ashandarei|itcf_carry_spear,
 0 , weight(3.5)|difficulty(5)|spd_rtng(100) | weapon_length(150)|swing_damage(55 , cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],
# Again, feel free to edit values such as length, difficulty, damage etc etc
# I put value(in-game) to 0 as I'd imagine only Mat will have it...
# And if you don't want the ravens, just take "_ravens" out of the mesh name entry.
######################


# end TGS Specific Items


###end TGS changes 

["items_end", "Items End", [("shield_round_a",0)], 0, 0, 1, 0, 0],

]
