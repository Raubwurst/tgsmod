import random

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *

####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
#  2) Toop name (string).
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn_reyvadin_castle|entry(1) puts troop in reyvadin castle's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
#     The function wp(x) will create random weapon proficiencies close to value x.
#     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
#           wp_archery(160) | wp(60)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
# 14) Troop image (string): If this variable is set, the troop will use an image rather than its 3D visual during the conversations
#  town_1   Sargoth
#  town_2   Tihr
#  town_3   Veluca
#  town_4   Suno
#  town_5   Jelkala
#  town_6   Praven
#  town_7   Uxkhal
#  town_8   Reyvadin
#  town_9   Khudan
#  town_10  Tulga
#  town_11  Curaw
#  town_12  Wercheg
#  town_13  Rivacheg
#  town_14  Halmar
####################################################################################################################

# Some constant and function declarations to be used below... 
# wp_one_handed () | wp_two_handed () | wp_polearm () | wp_archery () | wp_crossbow () | wp_throwing ()
def wp(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
#  n |= wp_archery(x + random.randrange(r))
#  n |= wp_crossbow(x + random.randrange(r))
#  n |= wp_throwing(x + random.randrange(r))
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  n |= wp_archery(x)
  n |= wp_crossbow(x)
  n |= wp_throwing(x)
  return n

def wpe(m,a,c,t):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wpex(o,w,p,a,c,t):
   n = 0
   n |= wp_one_handed(o)
   n |= wp_two_handed(w)
   n |= wp_polearm(p)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n
   
def wp_melee(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
  n |= wp_one_handed(x + 20)
  n |= wp_two_handed(x)
  n |= wp_polearm(x + 10)
  return n

#Skills
knows_common = knows_riding_1|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1
def_attrib = str_7 | agi_5 | int_4 | cha_4
def_attrib_multiplayer = str_14 | agi_14 | int_4 | cha_4



knows_lord_1 = knows_riding_3|knows_trade_2|knows_inventory_management_2|knows_tactics_4|knows_prisoner_management_4|knows_leadership_7

knows_warrior_npc = knows_weapon_master_2|knows_ironflesh_1|knows_athletics_1|knows_power_strike_2|knows_riding_2|knows_shield_1|knows_inventory_management_2
knows_merchant_npc = knows_riding_2|knows_trade_3|knows_inventory_management_3 #knows persuasion
knows_tracker_npc = knows_weapon_master_1|knows_athletics_2|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_ironflesh_1|knows_inventory_management_2

lord_attrib = str_20|agi_20|int_20|cha_20|level(38)

knight_attrib_1 = str_15|agi_14|int_8|cha_16|level(22)
knight_attrib_2 = str_16|agi_16|int_10|cha_18|level(26)
knight_attrib_3 = str_18|agi_17|int_12|cha_20|level(30)
knight_attrib_4 = str_19|agi_19|int_13|cha_22|level(35)
knight_attrib_5 = str_20|agi_20|int_15|cha_25|level(41)
knight_skills_1 = knows_riding_3|knows_ironflesh_2|knows_power_strike_3|knows_athletics_1|knows_tactics_2|knows_prisoner_management_1|knows_leadership_3
knight_skills_2 = knows_riding_4|knows_ironflesh_3|knows_power_strike_4|knows_athletics_2|knows_tactics_3|knows_prisoner_management_2|knows_leadership_5
knight_skills_3 = knows_riding_5|knows_ironflesh_4|knows_power_strike_5|knows_athletics_3|knows_tactics_4|knows_prisoner_management_2|knows_leadership_6
knight_skills_4 = knows_riding_6|knows_ironflesh_5|knows_power_strike_6|knows_athletics_4|knows_tactics_5|knows_prisoner_management_3|knows_leadership_7
knight_skills_5 = knows_riding_7|knows_ironflesh_6|knows_power_strike_7|knows_athletics_5|knows_tactics_6|knows_prisoner_management_3|knows_leadership_9

#### Skills and Attributes for TGS #####

#Infantry
knows_wot_infantry_1 = knows_weapon_master_1|knows_ironflesh_1|knows_athletics_1|knows_power_strike_2|knows_shield_1|knows_inventory_management_2
knows_wot_infantry_2 = knows_weapon_master_2|knows_ironflesh_2|knows_athletics_2|knows_power_strike_3|knows_shield_2|knows_inventory_management_2
knows_wot_infantry_3 = knows_weapon_master_3|knows_ironflesh_3|knows_athletics_3|knows_power_strike_4|knows_shield_3|knows_inventory_management_2
knows_wot_infantry_4 = knows_weapon_master_4|knows_ironflesh_4|knows_athletics_4|knows_power_strike_5|knows_shield_4|knows_inventory_management_2
knows_wot_infantry_5 = knows_weapon_master_5|knows_ironflesh_5|knows_athletics_5|knows_power_strike_6|knows_shield_5|knows_inventory_management_2

def_attrib_wot_infantry_1 = str_7|agi_5|int_4|cha_4|level(5)
def_attrib_wot_infantry_2 = str_10|agi_7|int_5|cha_5|level(8)
def_attrib_wot_infantry_3 = str_13|agi_9|int_6|cha_6|level(12)
def_attrib_wot_infantry_4 = str_16|agi_11|int_7|cha_7|level(16)
def_attrib_wot_infantry_5 = str_20|agi_14|int_8|cha_8|level(20)

#Cavalry
knows_wot_cavalry_1 = knows_weapon_master_1|knows_ironflesh_1|knows_athletics_1|knows_power_strike_2|knows_shield_1|knows_riding_2|knows_inventory_management_2
knows_wot_cavalry_2 = knows_weapon_master_2|knows_ironflesh_2|knows_athletics_1|knows_power_strike_3|knows_shield_1|knows_riding_3|knows_inventory_management_2
knows_wot_cavalry_3 = knows_weapon_master_3|knows_ironflesh_3|knows_athletics_2|knows_power_strike_4|knows_shield_2|knows_riding_3|knows_inventory_management_2
knows_wot_cavalry_4 = knows_weapon_master_4|knows_ironflesh_4|knows_athletics_2|knows_power_strike_5|knows_shield_2|knows_riding_4|knows_inventory_management_2
knows_wot_cavalry_5 = knows_weapon_master_5|knows_ironflesh_5|knows_athletics_3|knows_power_strike_6|knows_shield_3|knows_riding_5|knows_inventory_management_2

def_attrib_wot_cavalry_1 = str_10|agi_5|int_6|cha_6|level(7)
def_attrib_wot_cavalry_2 = str_13|agi_6|int_7|cha_7|level(10)
def_attrib_wot_cavalry_3 = str_16|agi_7|int_8|cha_8|level(15)
def_attrib_wot_cavalry_4 = str_19|agi_8|int_9|cha_9|level(20)
def_attrib_wot_cavalry_5 = str_24|agi_10|int_10|cha_10|level(25)

#Archer
knows_wot_archer_1 = knows_weapon_master_1|knows_ironflesh_1|knows_athletics_1|knows_power_draw_1|knows_inventory_management_2
knows_wot_archer_2 = knows_weapon_master_1|knows_ironflesh_1|knows_athletics_2|knows_power_draw_2|knows_inventory_management_2
knows_wot_archer_3 = knows_weapon_master_2|knows_ironflesh_2|knows_athletics_3|knows_power_draw_3|knows_inventory_management_2
knows_wot_archer_4 = knows_weapon_master_2|knows_ironflesh_2|knows_athletics_4|knows_power_draw_4|knows_inventory_management_2
knows_wot_archer_5 = knows_weapon_master_3|knows_ironflesh_3|knows_athletics_5|knows_power_draw_5|knows_inventory_management_2

#Thrower
knows_wot_thrower_1 = knows_weapon_master_1|knows_ironflesh_1|knows_athletics_1|knows_power_throw_1|knows_inventory_management_2
knows_wot_thrower_2 = knows_weapon_master_1|knows_ironflesh_1|knows_athletics_2|knows_power_throw_2|knows_inventory_management_2
knows_wot_thrower_3 = knows_weapon_master_2|knows_ironflesh_2|knows_athletics_3|knows_power_throw_3|knows_inventory_management_2
knows_wot_thrower_4 = knows_weapon_master_2|knows_ironflesh_2|knows_athletics_4|knows_power_throw_4|knows_inventory_management_2
knows_wot_thrower_5 = knows_weapon_master_3|knows_ironflesh_3|knows_athletics_5|knows_power_throw_5|knows_inventory_management_2

#Horse Archer
knows_wot_horse_archer_1 = knows_weapon_master_1|knows_ironflesh_1|knows_athletics_1|knows_power_strike_2|knows_horse_archery_1|knows_shield_1|knows_riding_2|knows_inventory_management_2
knows_wot_horse_archer_2 = knows_weapon_master_2|knows_ironflesh_2|knows_athletics_1|knows_power_strike_3|knows_horse_archery_2|knows_shield_1|knows_riding_3|knows_inventory_management_2
knows_wot_horse_archer_3 = knows_weapon_master_3|knows_ironflesh_3|knows_athletics_2|knows_power_strike_4|knows_horse_archery_3|knows_shield_2|knows_riding_3|knows_inventory_management_2
knows_wot_horse_archer_4 = knows_weapon_master_4|knows_ironflesh_4|knows_athletics_2|knows_power_strike_5|knows_horse_archery_4|knows_shield_2|knows_riding_4|knows_inventory_management_2
knows_wot_horse_archer_5 = knows_weapon_master_5|knows_ironflesh_5|knows_athletics_3|knows_power_strike_6|knows_horse_archery_5|knows_shield_3|knows_riding_5|knows_inventory_management_2

#Aiel/Trolloc
knows_wot_super_infantry_1 = knows_weapon_master_1|knows_ironflesh_2|knows_athletics_2|knows_power_strike_2|knows_shield_2|knows_power_draw_2|knows_power_throw_2|knows_inventory_management_2
knows_wot_super_infantry_2 = knows_weapon_master_2|knows_ironflesh_3|knows_athletics_3|knows_power_strike_3|knows_shield_3|knows_power_draw_3|knows_power_throw_3|knows_inventory_management_2
knows_wot_super_infantry_3 = knows_weapon_master_3|knows_ironflesh_4|knows_athletics_4|knows_power_strike_4|knows_shield_4|knows_power_draw_4|knows_power_throw_4|knows_inventory_management_2
knows_wot_super_infantry_4 = knows_weapon_master_4|knows_ironflesh_5|knows_athletics_5|knows_power_strike_5|knows_shield_5|knows_power_draw_5|knows_power_throw_5|knows_inventory_management_2
knows_wot_super_infantry_5 = knows_weapon_master_5|knows_ironflesh_7|knows_athletics_7|knows_power_strike_7|knows_shield_6|knows_power_draw_6|knows_power_throw_6|knows_inventory_management_2

def_attrib_wot_super_infantry_1 = str_8|agi_9|int_6|cha_6|level(5)
def_attrib_wot_super_infantry_2 = str_12|agi_13|int_7|cha_7|level(9)
def_attrib_wot_super_infantry_3 = str_16|agi_18|int_8|cha_8|level(13)
def_attrib_wot_super_infantry_4 = str_20|agi_23|int_9|cha_9|level(18)
def_attrib_wot_super_infantry_5 = str_25|agi_30|int_10|cha_10|level(22)

#### End Skills and Attributes for TGS #####

#These face codes are generated by the in-game face generator.
#Enable edit mode and press ctrl+E in face generator screen to obtain face codes.


reserved = 0

no_scene = 0

swadian_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
swadian_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
swadian_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
swadian_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
swadian_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

swadian_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

vaegir_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
vaegir_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
vaegir_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
vaegir_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
vaegir_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

vaegir_face_younger_2 = 0x000000003f00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_young_2   = 0x00000003bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_middle_2  = 0x00000007bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_old_2     = 0x0000000cbf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_older_2   = 0x0000000ff100230c4deeffffffffffff00000000001efff90000000000000000

khergit_face_younger_1 = 0x0000000009003109207000000000000000000000001c80470000000000000000
khergit_face_young_1   = 0x00000003c9003109207000000000000000000000001c80470000000000000000
khergit_face_middle_1  = 0x00000007c9003109207000000000000000000000001c80470000000000000000
khergit_face_old_1     = 0x0000000b89003109207000000000000000000000001c80470000000000000000
khergit_face_older_1   = 0x0000000fc9003109207000000000000000000000001c80470000000000000000

khergit_face_younger_2 = 0x000000003f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_young_2   = 0x00000003bf0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_middle_2  = 0x000000077f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_old_2     = 0x0000000b3f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_older_2   = 0x0000000fff0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000

nord_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
nord_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
nord_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
nord_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
nord_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

nord_face_younger_2 = 0x00000000310023084deeffffffffffff00000000001efff90000000000000000
nord_face_young_2   = 0x00000003b10023084deeffffffffffff00000000001efff90000000000000000
nord_face_middle_2  = 0x00000008310023084deeffffffffffff00000000001efff90000000000000000
nord_face_old_2     = 0x0000000c710023084deeffffffffffff00000000001efff90000000000000000
nord_face_older_2   = 0x0000000ff10023084deeffffffffffff00000000001efff90000000000000000

rhodok_face_younger_1 = 0x0000000009002003140000000000000000000000001c80400000000000000000
rhodok_face_young_1   = 0x0000000449002003140000000000000000000000001c80400000000000000000
rhodok_face_middle_1  = 0x0000000849002003140000000000000000000000001c80400000000000000000
rhodok_face_old_1     = 0x0000000cc9002003140000000000000000000000001c80400000000000000000
rhodok_face_older_1   = 0x0000000fc9002003140000000000000000000000001c80400000000000000000

rhodok_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

# added for TGS

#mayene
mayene_man_face_younger  = 0x00000000ff00354837236e58d26d391b00000000001db91b0000000000000000
mayene_man_face_young    = 0x000000053f00354837236e58d26d391b00000000001db91b0000000000000000
mayene_man_face_middle   = 0x00000009ff00354837236e58d26d391b00000000001db91b0000000000000000
mayene_man_face_old      = 0x0000000dbf00354837236e58d26d391b00000000001db91b0000000000000000
mayene_man_face_older    = 0x0000000f3f00354837236e58d26d391b00000000001db91b0000000000000000

mayene_woman_face_younger  = 0x00000001a9002006472c6e29236ab4ab00000000001eb8db0000000000000000
mayene_woman_face_young    = 0x00000001a9002006472c6e29236ab4ab00000000001eb8db0000000000000000
mayene_woman_face_middle   = 0x0000000969002006472c6e29236ab4ab00000000001eb8db0000000000000000
mayene_woman_face_old      = 0x0000000de9002006472c6e29236ab4ab00000000001eb8db0000000000000000
mayene_woman_face_older    = 0x0000000f69002006472c6e29236ab4ab00000000001eb8db0000000000000000

#tear
tear_man_face_younger  = 0x000000013f00650837236e58d26d391b00000000001db91b0000000000000000
tear_man_face_young    = 0x000000043f00650837236e58d26d391b00000000001db91b0000000000000000
tear_man_face_middle   = 0x000000093f00650837236e58d26d391b00000000001db91b0000000000000000
tear_man_face_old      = 0x0000000e3f00650837236e58d26d391b00000000001db91b0000000000000000
tear_man_face_older    = 0x0000000f3f00650837236e58d26d391b00000000001db91b0000000000000000

tear_woman_face_younger  = 0x00000001bf00300147636d38d372b89b00000000001d38db0000000000000000
tear_woman_face_young    = 0x00000006bf00300147636d38d372b89b00000000001d38db0000000000000000
tear_woman_face_middle   = 0x0000000bbf00300147636d38d372b89b00000000001d38db0000000000000000
tear_woman_face_old      = 0x0000000e7f00300147636d38d372b89b00000000001d38db0000000000000000
tear_woman_face_older    = 0x0000000f7f00300147636d38d372b89b00000000001d38db0000000000000000

#far madding
far_madding_man_face_younger  = 0x00000000c9004188392a6e58e576a8a300000000001e38dd0000000000000000
far_madding_man_face_young    = 0x00000005c9004188392a6e58e576a8a300000000001e38dd0000000000000000
far_madding_man_face_middle   = 0x0000000889004188392a6e58e576a8a300000000001e38dd0000000000000000
far_madding_man_face_old      = 0x0000000c49004188392a6e58e576a8a300000000001e38dd0000000000000000
far_madding_man_face_older    = 0x0000000e89004188392a6e58e576a8a300000000001e38dd0000000000000000

far_madding_woman_face_younger  = 0x00000001a60000042763aeb8d57638e300000000001eeb230000000000000000
far_madding_woman_face_young    = 0x00000001a60000042763aeb8d57638e300000000001eeb230000000000000000
far_madding_woman_face_middle   = 0x0000000b660000042763aeb8d57638e300000000001eeb230000000000000000
far_madding_woman_face_old      = 0x0000000de60000042763aeb8d57638e300000000001eeb230000000000000000
far_madding_woman_face_older    = 0x0000000fe60000042763aeb8d57638e300000000001eeb230000000000000000

#illian
illian_man_face_younger  = 0x000000026d0065c549223254a576a69e00000000001d389d0000000000000000
illian_man_face_young    = 0x00000006ed0065c549223254a576a69e00000000001d389d0000000000000000
illian_man_face_middle   = 0x0000000c6d0065c549223254a576a69e00000000001d389d0000000000000000
illian_man_face_old      = 0x0000000e2d0065c549223254a576a69e00000000001d389d0000000000000000
illian_man_face_older    = 0x0000000ead0065c549223254a576a69e00000000001d389d0000000000000000

illian_woman_face_younger  = 0x00000000e600100347636dc8d5964b6400000000001ec9640000000000000000
illian_woman_face_young    = 0x00000006e600100347636dc8d5964b6400000000001ec9640000000000000000
illian_woman_face_middle   = 0x0000000ba600100347636dc8d5964b6400000000001ec9640000000000000000
illian_woman_face_old      = 0x0000000ea600100347636dc8d5964b6400000000001ec9640000000000000000
illian_woman_face_older    = 0x0000000fe600100347636dc8d5964b6400000000001ec9640000000000000000

#murandy
murandy_man_face_younger  = 0x00000001d000548449223254a576a69e00000000001d389d0000000000000000
murandy_man_face_young    = 0x00000007d000548449223254a576a69e00000000001d389d0000000000000000
murandy_man_face_middle   = 0x0000000ad000548449223254a576a69e00000000001d389d0000000000000000
murandy_man_face_old      = 0x0000000d5000548449223254a576a69e00000000001d389d0000000000000000
murandy_man_face_older    = 0x0000000f5000548449223254a576a69e00000000001d389d0000000000000000

murandy_woman_face_younger  = 0x00000000e60020024b61ab66d3b62acc00000000001d46d40000000000000000
murandy_woman_face_young    = 0x00000005260020024b61ab66d3b62acc00000000001d46d40000000000000000
murandy_woman_face_middle   = 0x0000000a660020024b61ab66d3b62acc00000000001d46d40000000000000000
murandy_woman_face_old      = 0x0000000de60020024b61ab66d3b62acc00000000001d46d40000000000000000
murandy_woman_face_older    = 0x0000000fa60020024b61ab66d3b62acc00000000001d46d40000000000000000

#altara
altara_man_face_younger  = 0x0000000094002149452371d8e46d371b00000000001dc51b0000000000000000
altara_man_face_young    = 0x0000000654002149452371d8e46d371b00000000001dc51b0000000000000000
altara_man_face_middle   = 0x00000009d4002149452371d8e46d371b00000000001dc51b0000000000000000
altara_man_face_old      = 0x0000000d94002149452371d8e46d371b00000000001dc51b0000000000000000
altara_man_face_older    = 0x0000000f94002149452371d8e46d371b00000000001dc51b0000000000000000

altara_woman_face_younger  = 0x000000012600000124e5ab4cf3ca5acd00000000001f48e40000000000000000
altara_woman_face_young    = 0x000000072600000124e5ab4cf3ca5acd00000000001f48e40000000000000000
altara_woman_face_middle   = 0x0000000aa600000124e5ab4cf3ca5acd00000000001f48e40000000000000000
altara_woman_face_old      = 0x0000000e6600000124e5ab4cf3ca5acd00000000001f48e40000000000000000
altara_woman_face_older    = 0x0000000fa600000124e5ab4cf3ca5acd00000000001f48e40000000000000000

#ghealdan
ghealdan_man_face_younger  = 0x00000002c4005581572292a2a596d69c00000000001d395e0000000000000000
ghealdan_man_face_young    = 0x0000000744005581572292a2a596d69c00000000001d395e0000000000000000
ghealdan_man_face_middle   = 0x0000000a04005581572292a2a596d69c00000000001d395e0000000000000000
ghealdan_man_face_old      = 0x0000000dc4005581572292a2a596d69c00000000001d395e0000000000000000
ghealdan_man_face_older    = 0x0000000ec4005581572292a2a596d69c00000000001d395e0000000000000000

ghealdan_woman_face_younger  = 0x000000013e00100628d52a36f47658cb00000000001d26ec0000000000000000
ghealdan_woman_face_young    = 0x00000005be00100628d52a36f47658cb00000000001d26ec0000000000000000
ghealdan_woman_face_middle   = 0x0000000a3e00100628d52a36f47658cb00000000001d26ec0000000000000000
ghealdan_woman_face_old      = 0x0000000dfe00100628d52a36f47658cb00000000001d26ec0000000000000000
ghealdan_woman_face_older    = 0x0000000fbe00100628d52a36f47658cb00000000001d26ec0000000000000000

#amadicia
amadicia_man_face_younger  = 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000
amadicia_man_face_young    = 0x00000003e000500f36db6db6db6db6db00000000001db6db0000000000000000
amadicia_man_face_middle   = 0x000000082000500f36db6db6db6db6db00000000001db6db0000000000000000
amadicia_man_face_old      = 0x0000000e6000500f36db6db6db6db6db00000000001db6db0000000000000000
amadicia_man_face_older    = 0x0000000be000500f36db6db6db6db6db00000000001db6db0000000000000000

amadicia_woman_face_younger  = 0x000000023e0010052daeaab6f37338d300000000001f6ced0000000000000000
amadicia_woman_face_young    = 0x00000006be0010052daeaab6f37338d300000000001f6ced0000000000000000
amadicia_woman_face_middle   = 0x0000000b3e0010052daeaab6f37338d300000000001f6ced0000000000000000
amadicia_woman_face_old      = 0x0000000e3e0010052daeaab6f37338d300000000001f6ced0000000000000000
amadicia_woman_face_older    = 0x0000000fbe0010052daeaab6f37338d300000000001f6ced0000000000000000

#tarabon
tarabon_man_face_younger  = 0x00000003360063d4572292a2a596d69c00000000001d395e0000000000000000
tarabon_man_face_young    = 0x00000006f60063d4572292a2a596d69c00000000001d395e0000000000000000
tarabon_man_face_middle   = 0x0000000af60063d4572292a2a596d69c00000000001d395e0000000000000000
tarabon_man_face_old      = 0x0000000df60063d4572292a2a596d69c00000000001d395e0000000000000000
tarabon_man_face_older    = 0x0000000ef60063d4572292a2a596d69c00000000001d395e0000000000000000

tarabon_woman_face_younger  = 0x000000023e00300326a36a475572bb1300000000001db6d50000000000000000
tarabon_woman_face_young    = 0x000000023e00300326a36a475572bb1300000000001db6d50000000000000000
tarabon_woman_face_middle   = 0x000000097e00300326a36a475572bb1300000000001db6d50000000000000000
tarabon_woman_face_old      = 0x0000000dbe00300326a36a475572bb1300000000001db6d50000000000000000
tarabon_woman_face_older    = 0x0000000efe00300326a36a475572bb1300000000001db6d50000000000000000

#arad doman
arad_doman_man_face_younger  = 0x00000003000044c9551969a8a59636e400000000001ed36e0000000000000000
arad_doman_man_face_young    = 0x00000006800044c9551969a8a59636e400000000001ed36e0000000000000000
arad_doman_man_face_middle   = 0x00000009000044c9551969a8a59636e400000000001ed36e0000000000000000
arad_doman_man_face_old      = 0x0000000d000044c9551969a8a59636e400000000001ed36e0000000000000000
arad_doman_man_face_older    = 0x0000000e400044c9551969a8a59636e400000000001ed36e0000000000000000

arad_doman_woman_face_younger  = 0x000000017e0000022933d266d572ab2500000000001ddb550000000000000000
arad_doman_woman_face_young    = 0x00000005be0000022933d266d572ab2500000000001ddb550000000000000000
arad_doman_woman_face_middle   = 0x0000000b3e0000022933d266d572ab2500000000001ddb550000000000000000
arad_doman_woman_face_old      = 0x0000000e3e0000022933d266d572ab2500000000001ddb550000000000000000
arad_doman_woman_face_older    = 0x0000000efe0000022933d266d572ab2500000000001ddb550000000000000000

#saldaea
saldaea_man_face_younger  = 0x0000000216006181539665a8a59636e400000000001ed37e0000000000000000
saldaea_man_face_young    = 0x00000009d6006181539665a8a59636e400000000001ed37e0000000000000000
saldaea_man_face_middle   = 0x0000000d16006181539665a8a59636e400000000001ed37e0000000000000000
saldaea_man_face_old      = 0x0000000ed6006181539665a8a59636e400000000001ed37e0000000000000000
saldaea_man_face_older    = 0x0000000ed6006181539665a8a59636e400000000001ed37e0000000000000000

saldaea_woman_face_younger  = 0x0000000154002003312f32d71c6aaae300000000001e46e20000000000000000
saldaea_woman_face_young    = 0x0000000614002003312f32d71c6aaae300000000001e46e20000000000000000
saldaea_woman_face_middle   = 0x0000000b54002003312f32d71c6aaae300000000001e46e20000000000000000
saldaea_woman_face_old      = 0x0000000dd4002003312f32d71c6aaae300000000001e46e20000000000000000
saldaea_woman_face_older    = 0x0000000fd4002003312f32d71c6aaae300000000001e46e20000000000000000

#kandor
kandor_man_face_younger  = 0x00000002000032d4339665a8a59636e400000000001db6d20000000000000000
kandor_man_face_young    = 0x00000006c00032d4339665a8a59636e400000000001db6d20000000000000000
kandor_man_face_middle   = 0x00000009000032d4339665a8a59636e400000000001db6d20000000000000000
kandor_man_face_old      = 0x0000000d800032d4339665a8a59636e400000000001db6d20000000000000000
kandor_man_face_older    = 0x0000000f400032d4339665a8a59636e400000000001db6d20000000000000000

kandor_woman_face_younger  = 0x00000001d400000631373ad71c6aaae300000000001e46e20000000000000000
kandor_woman_face_young    = 0x000000069400000631373ad71c6aaae300000000001e46e20000000000000000
kandor_woman_face_middle   = 0x00000009d400000631373ad71c6aaae300000000001e46e20000000000000000
kandor_woman_face_old      = 0x0000000e5400000631373ad71c6aaae300000000001e46e20000000000000000
kandor_woman_face_older    = 0x0000000fd400000631373ad71c6aaae300000000001e46e20000000000000000

#arafel
arafel_man_face_younger  = 0x00000001a20013113395b9a8a59636e400000000001db6d20000000000000000
arafel_man_face_young    = 0x00000005a20013113395b9a8a59636e400000000001db6d20000000000000000
arafel_man_face_middle   = 0x00000009e20013113395b9a8a59636e400000000001db6d20000000000000000
arafel_man_face_old      = 0x0000000e220013113395b9a8a59636e400000000001db6d20000000000000000
arafel_man_face_older    = 0x0000000f620013113395b9a8a59636e400000000001db6d20000000000000000

arafel_woman_face_younger  = 0x00000001d600100239322ed7e366a6dc00000000001da7620000000000000000
arafel_woman_face_young    = 0x000000069600100239322ed7e366a6dc00000000001da7620000000000000000
arafel_woman_face_middle   = 0x000000095600100239322ed7e366a6dc00000000001da7620000000000000000
arafel_woman_face_old      = 0x0000000e1600100239322ed7e366a6dc00000000001da7620000000000000000
arafel_woman_face_older    = 0x0000000f9600100239322ed7e366a6dc00000000001da7620000000000000000

#shienar
shienar_man_face_younger  = 0x00000000bf00558b36d2b1b8e45646d200000000001e6b640000000000000000
shienar_man_face_young    = 0x000000067f00558b36d2b1b8e45646d200000000001e6b640000000000000000
shienar_man_face_middle   = 0x0000000a3f00558b36d2b1b8e45646d200000000001e6b640000000000000000
shienar_man_face_old      = 0x0000000d7f00558b36d2b1b8e45646d200000000001e6b640000000000000000
shienar_man_face_older    = 0x0000000fff00558b36d2b1b8e45646d200000000001e6b640000000000000000

shienar_woman_face_younger  = 0x00000000ff00200449328e57e476b6dc00000000001da69a0000000000000000
shienar_woman_face_young    = 0x00000005ff00200449328e57e476b6dc00000000001da69a0000000000000000
shienar_woman_face_middle   = 0x000000093f00200449328e57e476b6dc00000000001da69a0000000000000000
shienar_woman_face_old      = 0x0000000e3f00200449328e57e476b6dc00000000001da69a0000000000000000
shienar_woman_face_older    = 0x0000000fbf00200449328e57e476b6dc00000000001da69a0000000000000000

#tar valon
tar_valon_man_face_younger  = 0x000000029e00158636dc91b92c4acb5c00000000001f5ba40000000000000000
tar_valon_man_face_young    = 0x00000008de00158636dc91b92c4acb5c00000000001f5ba40000000000000000
tar_valon_man_face_middle   = 0x0000000c5e00158636dc91b92c4acb5c00000000001f5ba40000000000000000
tar_valon_man_face_old      = 0x0000000e9e00158636dc91b92c4acb5c00000000001f5ba40000000000000000
tar_valon_man_face_older    = 0x0000000fde00158636dc91b92c4acb5c00000000001f5ba40000000000000000

tar_valon_woman_face_younger  = 0x00000000ff000004492a8e54e47534c900000000001deb6c0000000000000000
tar_valon_woman_face_young    = 0x00000003bf000004492a8e54e47534c900000000001deb6c0000000000000000
tar_valon_woman_face_middle   = 0x000000083f000004492a8e54e47534c900000000001deb6c0000000000000000
tar_valon_woman_face_old      = 0x0000000b7f000004492a8e54e47534c900000000001deb6c0000000000000000
tar_valon_woman_face_older    = 0x0000000f3f000004492a8e54e47534c900000000001deb6c0000000000000000

#cairhien
cairhien_man_face_younger  = 0x00000002bf003012376469c8ec8dc64a00000000001dd7240000000000000000
cairhien_man_face_young    = 0x000000073f003012376469c8ec8dc64a00000000001dd7240000000000000000
cairhien_man_face_middle   = 0x000000097f003012376469c8ec8dc64a00000000001dd7240000000000000000
cairhien_man_face_old      = 0x0000000cbf003012376469c8ec8dc64a00000000001dd7240000000000000000
cairhien_man_face_older    = 0x0000000ebf003012376469c8ec8dc64a00000000001dd7240000000000000000

cairhien_woman_face_younger  = 0x000000063f002004296b8dcd76b6cb2100000000001e6b6a0000000000000000
cairhien_woman_face_young    = 0x000000063f002004296b8dcd76b6cb2100000000001e6b6a0000000000000000
cairhien_woman_face_middle   = 0x0000000aff002004296b8dcd76b6cb2100000000001e6b6a0000000000000000
cairhien_woman_face_old      = 0x0000000d7f002004296b8dcd76b6cb2100000000001e6b6a0000000000000000
cairhien_woman_face_older    = 0x0000000f3f002004296b8dcd76b6cb2100000000001e6b6a0000000000000000

#andor
andor_man_face_younger  = 0x000000040800300f376449d6f4d2eb6c00000000001e57230000000000000000
andor_man_face_young    = 0x00000008c800300f376449d6f4d2eb6c00000000001e57230000000000000000
andor_man_face_middle   = 0x0000000cc800300f376449d6f4d2eb6c00000000001e57230000000000000000
andor_man_face_old      = 0x0000000e0800300f376449d6f4d2eb6c00000000001e57230000000000000000
andor_man_face_older    = 0x0000000f4800300f376449d6f4d2eb6c00000000001e57230000000000000000

andor_woman_face_younger  = 0x0000000140002002296ba59d5e69492900000000001d156a0000000000000000
andor_woman_face_young    = 0x0000000580002002296ba59d5e69492900000000001d156a0000000000000000
andor_woman_face_middle   = 0x00000009c0002002296ba59d5e69492900000000001d156a0000000000000000
andor_woman_face_old      = 0x0000000dc0002002296ba59d5e69492900000000001d156a0000000000000000
andor_woman_face_older    = 0x0000000f80002002296ba59d5e69492900000000001d156a0000000000000000

#aiel
aiel_1_man_face_younger  = 0x00000004000010145d6dd258a296d8dd00000000001dd72c0000000000000000
aiel_1_man_face_young    = 0x00000006800010145d6dd258a296d8dd00000000001dd72c0000000000000000
aiel_1_man_face_middle   = 0x0000000ac00010145d6dd258a296d8dd00000000001dd72c0000000000000000
aiel_1_man_face_old      = 0x0000000d800010145d6dd258a296d8dd00000000001dd72c0000000000000000
aiel_1_man_face_older    = 0x0000000f800010145d6dd258a296d8dd00000000001dd72c0000000000000000

aiel_1_woman_face_younger  = 0x000000000000000728d979c55db1496c00000000001e452b0000000000000000
aiel_1_woman_face_young    = 0x000000058000000728d979c55db1496c00000000001e452b0000000000000000
aiel_1_woman_face_middle   = 0x000000090000000728d979c55db1496c00000000001e452b0000000000000000
aiel_1_woman_face_old      = 0x0000000d0000000728d979c55db1496c00000000001e452b0000000000000000
aiel_1_woman_face_older    = 0x0000000f8000000728d979c55db1496c00000000001e452b0000000000000000

aiel_2_man_face_younger  = 0x00000000930010145d6dd258a296d8dd00000000001dd72c0000000000000000
aiel_2_man_face_young    = 0x00000006930010145d6dd258a296d8dd00000000001dd72c0000000000000000
aiel_2_man_face_middle   = 0x0000000a930010145d6dd258a296d8dd00000000001dd72c0000000000000000
aiel_2_man_face_old      = 0x0000000dd30010145d6dd258a296d8dd00000000001dd72c0000000000000000
aiel_2_man_face_older    = 0x0000000e930010145d6dd258a296d8dd00000000001dd72c0000000000000000

aiel_2_woman_face_younger  = 0x000000000000100728d979c55db1496c00000000001e452b0000000000000000
aiel_2_woman_face_young    = 0x00000005c000100728d979c55db1496c00000000001e452b0000000000000000
aiel_2_woman_face_middle   = 0x000000098000100728d979c55db1496c00000000001e452b0000000000000000
aiel_2_woman_face_old      = 0x0000000dc000100728d979c55db1496c00000000001e452b0000000000000000
aiel_2_woman_face_older    = 0x0000000fc000100728d979c55db1496c00000000001e452b0000000000000000

#seanchan
seanchan_1_man_face_younger  = 0x0000000213004007589d5158a38db4dd00000000001da7240000000000000000
seanchan_1_man_face_young    = 0x0000000693004007589d5158a38db4dd00000000001da7240000000000000000
seanchan_1_man_face_middle   = 0x0000000b53004007589d5158a38db4dd00000000001da7240000000000000000
seanchan_1_man_face_old      = 0x0000000dd3004007589d5158a38db4dd00000000001da7240000000000000000
seanchan_1_man_face_older    = 0x0000000e93004007589d5158a38db4dd00000000001da7240000000000000000

seanchan_1_woman_face_younger  = 0x0000000180002006291979c555b6c8ea00000000001e65ad0000000000000000
seanchan_1_woman_face_young    = 0x0000000780002006291979c555b6c8ea00000000001e65ad0000000000000000
seanchan_1_woman_face_middle   = 0x0000000c00002006291979c555b6c8ea00000000001e65ad0000000000000000
seanchan_1_woman_face_old      = 0x0000000fc0002006291979c555b6c8ea00000000001e65ad0000000000000000
seanchan_1_woman_face_older    = 0x0000000f40002006291979c555b6c8ea00000000001e65ad0000000000000000

seanchan_2_man_face_younger  = 0x000000018000715436db75356b4dc8db00000000001ed4dc0000000000000000
seanchan_2_man_face_young    = 0x000000060000715436db75356b4dc8db00000000001ed4dc0000000000000000
seanchan_2_man_face_middle   = 0x000000094000715436db75356b4dc8db00000000001ed4dc0000000000000000
seanchan_2_man_face_old      = 0x0000000dc000715436db75356b4dc8db00000000001ed4dc0000000000000000
seanchan_2_man_face_older    = 0x0000000f0000715436db75356b4dc8db00000000001ed4dc0000000000000000

seanchan_2_woman_face_younger  = 0x0000000184004003495d69d525774ca200000000001e249d0000000000000000
seanchan_2_woman_face_young    = 0x00000005c4004003495d69d525774ca200000000001e249d0000000000000000
seanchan_2_woman_face_middle   = 0x00000009c4004003495d69d525774ca200000000001e249d0000000000000000
seanchan_2_woman_face_old      = 0x0000000d84004003495d69d525774ca200000000001e249d0000000000000000
seanchan_2_woman_face_older    = 0x0000000f44004003495d69d525774ca200000000001e249d0000000000000000

# end added for TGS

man_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
man_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
man_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
man_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
man_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

man_face_younger_2 = 0x000000003f0052064deeffffffffffff00000000001efff90000000000000000
man_face_young_2   = 0x00000003bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_middle_2  = 0x00000007bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_old_2     = 0x0000000bff0052064deeffffffffffff00000000001efff90000000000000000
man_face_older_2   = 0x0000000fff0052064deeffffffffffff00000000001efff90000000000000000

merchant_face_1    = man_face_young_1
merchant_face_2    = man_face_older_2

woman_face_1    = 0x0000000000000001000000000000000000000000001c00000000000000000000
woman_face_2    = 0x00000003bf0030067ff7fbffefff6dff00000000001f6dbf0000000000000000

swadian_woman_face_1 = 0x0000000180102006124925124928924900000000001c92890000000000000000
swadian_woman_face_2 = 0x00000001bf1000061db6d75db6b6dbad00000000001c92890000000000000000

khergit_woman_face_1 = 0x0000000180103006124925124928924900000000001c92890000000000000000
khergit_woman_face_2 = 0x00000001af1030025b6eb6dd6db6dd6d00000000001eedae0000000000000000

refugee_face1 = woman_face_1
refugee_face2 = woman_face_2
girl_face1    = woman_face_1
girl_face2    = woman_face_2

mercenary_face_1 = 0x0000000000000000000000000000000000000000001c00000000000000000000
mercenary_face_2 = 0x0000000cff00730b6db6db6db7fbffff00000000001efffe0000000000000000

vaegir_face1  = vaegir_face_young_1
vaegir_face2  = vaegir_face_older_2

bandit_face1  = man_face_young_1
bandit_face2  = man_face_older_2

undead_face1  = 0x00000000002000000000000000000000
undead_face2  = 0x000000000020010000001fffffffffff

#NAMES:
#

tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield
# added for TGS
tf_guarantee_all_cavalry = tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield
# end added for TGS


troops = [
    # wp(15)
  ["player","Player","Player",tf_hero|tf_unmoveable_in_party_window,no_scene,reserved,fac_player_faction,
   [],
   str_4|agi_4|int_4|cha_4,wp(15),0,0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_male","multiplayer_profile_troop_male","multiplayer_profile_troop_male", tf_hero|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_leather_jerkin, itm_leather_boots],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["multiplayer_profile_troop_female","multiplayer_profile_troop_female","multiplayer_profile_troop_female", tf_hero|tf_female|tf_guarantee_all, 0, 0,fac_commoners,
   [itm_tribal_warrior_outfit, itm_leather_boots],
   0, 0, 0, 0x000000018000000136db6db6db6db6db00000000001db6db0000000000000000],
  ["temp_troop","Temp Troop","Temp Troop",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
##  ["game","Game","Game",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common,0],
##  ["unarmed_troop","Unarmed Troop","Unarmed Troops",tf_hero,no_scene,reserved,fac_commoners,[itm_arrows,itm_short_bow],def_attrib|str_14,0,knows_common|knows_power_draw_2,0],

####################################################################################################################
# Troops before this point are hardwired into the game and their order should not be changed!
####################################################################################################################
  ["find_item_cheat","find_item_cheat","find_item_cheat",tf_hero|tf_is_merchant,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["random_town_sequence","Random Town Sequence","Random Town Sequence",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["tournament_participants","Tournament Participants","Tournament Participants",tf_hero,no_scene,reserved,fac_commoners,[],def_attrib,0,knows_common|knows_inventory_management_10,0],
  ["tutorial_maceman","Maceman","Maceman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_tutorial_club,itm_leather_jerkin,itm_hide_boots],
   str_6|agi_6|level(1),wp(50),knows_common,mercenary_face_1,mercenary_face_2],
  ["tutorial_archer","Archer","Archer",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_tutorial_short_bow,itm_tutorial_arrows,itm_linen_tunic,itm_hide_boots],
   str_6|agi_6|level(5),wp(100),knows_common|knows_power_draw_4,mercenary_face_1,mercenary_face_2],
  ["tutorial_swordsman","Swordsman","Swordsman",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_tutorial_sword,itm_leather_vest,itm_hide_boots],
   str_6|agi_6|level(5),wp(80),knows_common,mercenary_face_1,mercenary_face_2],

  ["novice_fighter","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_6|agi_6|level(5),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
  ["regular_fighter","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_8|agi_8|level(11),wp(90),knows_common|knows_ironflesh_1|knows_power_strike_1|knows_athletics_1|knows_riding_1|knows_shield_2,mercenary_face_1, mercenary_face_2],
  ["veteran_fighter","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,0,fac_commoners,
   [itm_hide_boots],
   str_10|agi_10|level(17),wp(110),knows_common|knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2|knows_shield_3,mercenary_face_1, mercenary_face_2],
  ["champion_fighter","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_12|agi_11|level(22),wp(140),knows_common|knows_ironflesh_4|knows_power_strike_3|knows_athletics_3|knows_riding_3|knows_shield_4,mercenary_face_1, mercenary_face_2],

  ["arena_training_fighter_1","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_6|agi_6|level(5),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_2","Novice Fighter","Novice Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_7|agi_6|level(7),wp(70),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_3","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_8|agi_7|level(9),wp(80),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_4","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_8|agi_8|level(11),wp(90),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_5","Regular Fighter","Regular Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_9|agi_8|level(13),wp(100),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_6","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_10|agi_9|level(15),wp(110),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_7","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_10|agi_10|level(17),wp(120),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_8","Veteran Fighter","Veteran Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_11|agi_10|level(19),wp(130),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_9","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_12|agi_11|level(21),wp(140),knows_common,mercenary_face_1, mercenary_face_2],
  ["arena_training_fighter_10","Champion Fighter","Champion Fighters",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_hide_boots],
   str_12|agi_12|level(23),wp(150),knows_common,mercenary_face_1, mercenary_face_2],

  ["cattle","Cattle","Cattle",0,no_scene,reserved,fac_neutral, [], def_attrib|level(1),wp(60),0,mercenary_face_1, mercenary_face_2],


#soldiers:
#This troop is the troop marked as soldiers_begin
  ["farmer","Farmer","Farmers",tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
  ["townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_club,itm_quarter_staff,itm_dagger,itm_stones,itm_leather_cap,itm_linen_tunic,itm_coarse_tunic,itm_leather_apron,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,mercenary_face_1, mercenary_face_2],
  ["watchman","Watchman","Watchmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_bolts,itm_spiked_club,itm_fighting_pick,itm_sword_medieval_a,itm_boar_spear,itm_hunting_crossbow,itm_light_crossbow,itm_tab_shield_round_a,itm_tab_shield_round_b,itm_padded_cloth,itm_leather_jerkin,itm_leather_cap,itm_padded_coif,itm_footman_helmet,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(9),wp(75),knows_common|knows_shield_1,mercenary_face_1, mercenary_face_2],
  ["caravan_guard","Caravan Guard","Caravan Guards",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_shield,no_scene,0,fac_commoners,
   [itm_spear,itm_fighting_pick,itm_sword_medieval_a,itm_voulge,itm_tab_shield_round_b,itm_tab_shield_round_c,itm_leather_jerkin,itm_leather_vest,itm_hide_boots,itm_padded_coif,itm_nasal_helmet,itm_footman_helmet,itm_saddle_horse],
   def_attrib|level(14),wp(85),knows_common|knows_riding_2|knows_ironflesh_1|knows_shield_3,mercenary_face_1, mercenary_face_2],
  ["mercenary_swordsman","Mercenary Swordsman","Mercenary Swordsmen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_bastard_sword_a,itm_sword_medieval_b,itm_sword_medieval_b_small,itm_tab_shield_heater_c,itm_mail_hauberk,itm_haubergeon,itm_leather_boots,itm_mail_chausses,itm_kettle_hat,itm_mail_coif,itm_flat_topped_helmet, itm_helmet_with_neckguard],
   def_attrib|level(20),wp(100),knows_common|knows_riding_3|knows_ironflesh_3|knows_shield_3|knows_power_strike_3,mercenary_face_1, mercenary_face_2],
  ["hired_blade","Hired Blade","Hired Blades",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_bastard_sword_b,itm_sword_medieval_c,itm_tab_shield_heater_cav_a,itm_haubergeon,itm_mail_chausses,itm_iron_greaves,itm_plate_boots,itm_guard_helmet,itm_great_helmet,itm_bascinet, itm_leather_gloves],
   def_attrib|level(25),wp(130),knows_common|knows_riding_3|knows_athletics_5|knows_shield_5|knows_power_strike_5|knows_ironflesh_5,mercenary_face_1, mercenary_face_2],
  ["mercenary_crossbowman","Mercenary Crossbowman","Mercenary Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,no_scene,reserved,fac_commoners,
   [itm_bolts,itm_spiked_club,itm_fighting_pick,itm_sword_medieval_a,itm_boar_spear,itm_crossbow,itm_tab_shield_pavise_a,itm_tab_shield_round_b,itm_padded_cloth,itm_leather_jerkin,itm_leather_cap,itm_padded_coif,itm_footman_helmet,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(19),wp_one_handed (90) | wp_two_handed (90) | wp_polearm (90) | wp_archery (90) | wp_crossbow (130) | wp_throwing (90),knows_common|knows_athletics_5|knows_shield_1,mercenary_face_1, mercenary_face_2],
  ["mercenary_horseman","Mercenary Horseman","Mercenary Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_lance,itm_bastard_sword_a,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_mail_shirt,itm_haubergeon,itm_leather_boots,itm_norman_helmet,itm_mail_coif,itm_helmet_with_neckguard,itm_saddle_horse,itm_courser],
   def_attrib|level(20),wp(100),knows_common|knows_riding_4|knows_ironflesh_3|knows_shield_2|knows_power_strike_3,mercenary_face_1, mercenary_face_2],
  ["mercenary_cavalry","Mercenary Cavalry","Mercenary Cavalry",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,no_scene,reserved,fac_commoners,
   [itm_heavy_lance,itm_bastard_sword_a,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_cuir_bouilli,itm_banded_armor,itm_hide_boots,itm_kettle_hat,itm_mail_coif,itm_flat_topped_helmet,itm_helmet_with_neckguard,itm_warhorse,itm_hunter],
   def_attrib|level(25),wp(130),knows_common|knows_riding_5|knows_ironflesh_4|knows_shield_5|knows_power_strike_4,mercenary_face_1, mercenary_face_2],
  ["mercenaries_end","mercenaries_end","mercenaries_end",0,no_scene,reserved,fac_commoners,
   [],
   def_attrib|level(4),wp(60),knows_common,mercenary_face_1, mercenary_face_2],

###############################################################
##### native faction troops commented out for TGS
###############################################################

#peasant - retainer - footman - man-at-arms -  knight
#  ["swadian_recruit","Swadian Recruit","Swadian Recruits",tf_guarantee_armor,0,0,fac_kingdom_1,
#   [itm_scythe,itm_hatchet,itm_pickaxe,itm_club,itm_stones,itm_tab_shield_heater_a,itm_leather_cap,itm_felt_hat,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_nomad_boots,itm_wrapping_boots],
#   def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
#  ["swadian_militia","Swadian Militia","Swadian Militia",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_1,
#   [itm_bolts,itm_spiked_club,itm_fighting_pick,itm_boar_spear,itm_hunting_crossbow,itm_tab_shield_heater_a,
#    itm_padded_cloth,itm_leather_armor,itm_leather_cap,itm_arming_cap,itm_padded_coif,itm_ankle_boots,itm_wrapping_boots],
#   def_attrib|level(9),wp(75),knows_common,swadian_face_young_1, swadian_face_old_2],
#  ["swadian_footman","Swadian Footman","Swadian Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_1,
#   [itm_spear,itm_fighting_pick,itm_sword_medieval_b_small,itm_sword_medieval_a,itm_tab_shield_heater_b,
#    itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
#   def_attrib|level(14),wp_melee(85),knows_common|knows_ironflesh_1|knows_shield_2|knows_athletics_2|knows_power_strike_1,swadian_face_young_1, swadian_face_old_2],
#  ["swadian_infantry","Swadian Infantry","Swadian Infantry",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
#   [itm_pike,itm_fighting_pick,itm_bastard_sword_a,itm_sword_medieval_a,itm_sword_medieval_b_small,itm_tab_shield_heater_c,
#    itm_mail_with_surcoat,itm_haubergeon,itm_hide_boots,itm_ankle_boots,itm_kettle_hat,itm_mail_coif,itm_flat_topped_helmet,itm_helmet_with_neckguard],
#   def_attrib|level(20),wp_melee(105),knows_common|knows_riding_3|knows_ironflesh_2|knows_power_strike_2|knows_shield_3|knows_athletics_3,swadian_face_middle_1, swadian_face_old_2],
#  ["swadian_sergeant","Swadian Sergeant","Swadian Sergeants",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
#   [itm_awlpike,itm_bastard_sword_b,itm_morningstar,itm_sword_medieval_c,itm_tab_shield_heater_d,
#    itm_coat_of_plates,itm_mail_with_surcoat,itm_mail_chausses,itm_iron_greaves,itm_guard_helmet,itm_helmet_with_neckguard,itm_bascinet,itm_guard_helmet,itm_leather_gloves],
#   def_attrib|level(25),wp_melee(135),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_4|knows_athletics_4,swadian_face_middle_1, swadian_face_older_2],
#  ["swadian_skirmisher","Swadian Skirmisher","Swadian Skirmishers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
#   [itm_bolts,itm_light_crossbow,itm_hunting_crossbow,itm_dagger,itm_club,itm_voulge,itm_tab_shield_heater_a,
#    itm_leather_armor,itm_padded_cloth,itm_ankle_boots,itm_padded_coif,itm_arming_cap,itm_footman_helmet],
#   def_attrib|level(14),wp(80),knows_common|knows_riding_2|knows_ironflesh_1,swadian_face_young_1, swadian_face_middle_2],
#  ["swadian_crossbowman","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_1,
#   [itm_bolts,itm_crossbow,itm_light_crossbow,itm_fighting_pick,itm_dagger,itm_sword_medieval_a,itm_voulge,itm_tab_shield_heater_b,
#    itm_leather_jerkin,itm_leather_armor,itm_hide_boots,itm_ankle_boots,itm_padded_coif,itm_nasal_helmet,itm_footman_helmet],
#   def_attrib|level(19),wp_melee(90)|wp_crossbow(100),knows_common|knows_riding_2|knows_ironflesh_1|knows_athletics_1,swadian_face_young_1, swadian_face_old_2],
#  ["swadian_sharpshooter","Swadian Sharpshooter","Swadian Sharpshooters",tf_guarantee_ranged|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
#   [itm_bolts,itm_arrows,itm_crossbow,itm_crossbow,itm_heavy_crossbow,itm_sword_medieval_b_small,itm_sword_medieval_a,itm_voulge,itm_tab_shield_heater_c,
#    itm_haubergeon,itm_padded_leather,itm_hide_boots,itm_norman_helmet,itm_nasal_helmet,itm_kettle_hat,itm_kettle_hat,itm_leather_gloves],
#   def_attrib|str_14|level(24),wp_melee(100)|wp_crossbow(130),knows_common|knows_power_draw_3|knows_ironflesh_1|knows_power_strike_1|knows_athletics_2,swadian_face_middle_1, swadian_face_older_2],
#  ["swadian_man_at_arms","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_1,
#   [itm_lance,itm_fighting_pick,itm_bastard_sword_a,itm_sword_medieval_b,itm_sword_medieval_c_small,itm_tab_shield_heater_cav_a,
#    itm_haubergeon,itm_mail_with_surcoat,itm_hide_boots,itm_norman_helmet,itm_mail_coif,itm_flat_topped_helmet,itm_helmet_with_neckguard,itm_warhorse,itm_warhorse,itm_hunter],
#   def_attrib|level(21),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
#  ["swadian_knight","Swadian Knight","Swadian Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_1,
#   [itm_heavy_lance,itm_bastard_sword_b,itm_morningstar,itm_sword_medieval_c,itm_tab_shield_heater_cav_b,
#    itm_coat_of_plates,itm_cuir_bouilli,itm_mail_with_surcoat,itm_mail_chausses,itm_plate_boots,itm_guard_helmet,itm_great_helmet,itm_bascinet,itm_hunter,itm_warhorse,itm_leather_gloves,itm_mail_mittens],
#   def_attrib|level(28),wp_melee(130),knows_common|knows_riding_5|knows_shield_3|knows_ironflesh_4|knows_power_strike_4,swadian_face_middle_1, swadian_face_older_2],

#  ["swadian_messenger","Swadian Messenger","Swadian Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_1,
#   [itm_sword_medieval_a,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],
#   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5,swadian_face_young_1, swadian_face_old_2],
#  ["swadian_deserter","Swadian Deserter","Swadian Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
#   [itm_bolts,itm_light_crossbow,itm_hunting_crossbow,itm_dagger,itm_club,itm_voulge,itm_wooden_shield,itm_leather_jerkin,itm_padded_cloth,itm_hide_boots,itm_padded_coif,itm_nasal_helmet,itm_footman_helmet],
#   def_attrib|level(14),wp(80),knows_common|knows_riding_2|knows_ironflesh_1,swadian_face_young_1, swadian_face_old_2],
#  ["swadian_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
#   [itm_awlpike,itm_pike,itm_great_sword,itm_morningstar,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_coat_of_plates,itm_plate_armor,itm_mail_chausses,itm_iron_greaves,itm_guard_helmet,itm_helmet_with_neckguard,itm_bascinet,itm_guard_helmet,itm_leather_gloves],
#   def_attrib|level(25),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
#  ["swadian_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
#   [itm_awlpike,itm_pike,itm_great_sword,itm_morningstar,itm_sword_medieval_b,itm_tab_shield_heater_c,itm_tab_shield_heater_d,itm_coat_of_plates,itm_plate_armor,itm_mail_chausses,itm_iron_greaves,itm_guard_helmet,itm_helmet_with_neckguard,itm_bascinet,itm_guard_helmet,itm_leather_gloves],
#   def_attrib|level(25),wp(130),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],

# Vaegir watchman? itm_stones,itm_scythe,itm_hatchet,itm_cudgel,itm_axe,itm_tab_shield_kite_a,
#  ["vaegir_recruit","Vaegir Recruit","Vaegir Recruits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_all,0,0,fac_kingdom_2,
#   [itm_power_ashaman_soldier_ranged, itm_power_ashaman_soldier_non_ranged, itm_power_ammo,itm_linen_tunic, itm_rawhide_coat,itm_nomad_boots],
#    def_attrib|level(4),wp(60)|wp_firearm(100),knows_common,vaegir_face_younger_1, vaegir_face_middle_2],
#  ["vaegir_footman","Vaegir Footman","Vaegir Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_2,
#   [itm_spiked_club,itm_hand_axe,itm_sword_viking_1,itm_two_handed_axe,itm_tab_shield_kite_a,itm_tab_shield_kite_b,itm_spear,itm_nomad_cap,itm_vaegir_fur_cap,itm_rawhide_coat,itm_nomad_armor,itm_nomad_boots],
#   def_attrib|level(9),wp(75),knows_common, vaegir_face_young_1, vaegir_face_middle_2],
#  ["vaegir_skirmisher","Vaegir Skirmisher","Vaegir Skirmishers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
#   [itm_arrows,itm_spiked_mace,itm_axe,itm_sword_khergit_1,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
#   def_attrib|str_10|level(14),wp(60),knows_ironflesh_1|knows_power_draw_1|knows_power_throw_1,vaegir_face_young_1, vaegir_face_old_2],
#  ["vaegir_archer","Vaegir Archer","Vaegir Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
#   [itm_arrows,itm_axe,itm_sword_khergit_1,itm_nomad_bow,itm_nomad_bow,itm_short_bow,
#    itm_leather_jerkin,itm_leather_vest,itm_nomad_boots,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_vaegir_fur_cap,itm_nomad_cap],
#   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_3|knows_athletics_2|knows_power_throw_1,vaegir_face_young_1, vaegir_face_older_2],
#  ["vaegir_marksman","Vaegir Marksman","Vaegir Marksmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
#   [itm_barbed_arrows,itm_axe,itm_voulge,itm_sword_khergit_2,itm_strong_bow,itm_nomad_bow,itm_nomad_bow,
#    itm_leather_vest,itm_studded_leather_coat,itm_nomad_boots,itm_vaegir_lamellar_helmet,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet],
#   def_attrib|str_14|level(24),wp_melee(80)|wp_archery(140),knows_ironflesh_2|knows_power_draw_5|knows_athletics_3|knows_power_throw_1,vaegir_face_young_1, vaegir_face_older_2],
#  ["vaegir_veteran","Vaegir Veteran","Vaegir Veterans",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_2,
#   [itm_spiked_mace,itm_two_handed_axe,itm_sword_viking_1,itm_tab_shield_kite_b,itm_tab_shield_kite_c,itm_spear,
#    itm_steppe_cap,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_vaegir_fur_cap,itm_leather_jerkin,itm_studded_leather_coat,itm_nomad_boots,itm_saddle_horse],
#   def_attrib|level(14),wp_melee(85),knows_athletics_2|knows_ironflesh_1|knows_power_strike_2|knows_shield_2,vaegir_face_young_1, vaegir_face_old_2],
#  ["vaegir_infantry","Vaegir Infantry","Vaegir Infantries",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
#   [itm_pike,itm_battle_axe,itm_sword_viking_2,itm_sword_khergit_2,itm_tab_shield_kite_c,itm_spear,
#    itm_mail_hauberk,itm_lamellar_vest,itm_nomad_boots,itm_vaegir_lamellar_helmet,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet],
#   def_attrib|level(19),wp_melee(100),knows_athletics_3|knows_ironflesh_2|knows_power_strike_3|knows_shield_2,vaegir_face_young_1, vaegir_face_older_2],
#  ["vaegir_guard","Vaegir Guard","Vaegir Guards",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
#   [itm_ashwood_pike,itm_battle_fork,itm_bardiche,itm_battle_axe,itm_fighting_axe,itm_tab_shield_kite_d,
#    itm_banded_armor,itm_lamellar_vest,itm_lamellar_armor,itm_mail_chausses,itm_iron_greaves,itm_vaegir_war_helmet,itm_vaegir_war_helmet,itm_vaegir_lamellar_helmet,itm_leather_gloves],
#   def_attrib|level(24),wp_melee(130),knows_riding_2|knows_athletics_4|knows_shield_2|knows_ironflesh_3|knows_power_strike_4,vaegir_face_middle_1, vaegir_face_older_2],
#  ["vaegir_horseman","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
#   [itm_battle_axe,itm_sword_khergit_2,itm_lance,itm_tab_shield_kite_cav_a,itm_spear,
#    itm_studded_leather_coat,itm_lamellar_vest,itm_nomad_boots,itm_vaegir_lamellar_helmet,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_steppe_horse,itm_hunter],
#   def_attrib|level(21),wp(100),knows_riding_3|knows_ironflesh_2|knows_power_strike_2,vaegir_face_young_1, vaegir_face_older_2],
#  ["vaegir_knight","Vaegir Knight","Vaegir Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
#   [itm_bardiche,itm_war_axe,itm_fighting_axe,itm_lance,itm_lance,itm_tab_shield_kite_cav_b,
#    itm_banded_armor,itm_lamellar_vest,itm_lamellar_armor,itm_mail_chausses,itm_plate_boots,itm_vaegir_war_helmet,itm_vaegir_war_helmet,itm_vaegir_lamellar_helmet,itm_hunter, itm_warhorse,itm_leather_gloves],
#   def_attrib|level(26),wp(130),knows_riding_4|knows_shield_2|knows_ironflesh_3|knows_power_strike_3,vaegir_face_middle_1, vaegir_face_older_2],

#  ["vaegir_messenger","Vaegir Messenger","Vaegir Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_2,
#   [itm_sword_medieval_b,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
#   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,vaegir_face_young_1, vaegir_face_older_2],
#  ["vaegir_deserter","Vaegir Deserter","Vaegir Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
#   [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
#   def_attrib|str_10|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,vaegir_face_young_1, vaegir_face_older_2],
#  ["vaegir_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
#   [itm_ashwood_pike,itm_battle_fork,itm_bardiche,itm_battle_axe,itm_fighting_axe,itm_tab_shield_kite_b,itm_studded_leather_coat,itm_lamellar_armor,itm_mail_chausses,itm_iron_greaves,itm_nordic_helmet,itm_nordic_helmet,itm_nordic_helmet,itm_spiked_helmet,itm_leather_gloves],
#   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,vaegir_face_middle_1, vaegir_face_older_2],
#  ["vaegir_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_2,
#   [itm_ashwood_pike,itm_battle_fork,itm_bardiche,itm_battle_axe,itm_fighting_axe,itm_tab_shield_kite_d,itm_studded_leather_coat,itm_lamellar_armor,itm_mail_chausses,itm_iron_greaves,itm_nordic_helmet,itm_nordic_helmet,itm_nordic_helmet,itm_spiked_helmet,itm_leather_gloves],
#   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,vaegir_face_middle_1, vaegir_face_older_2],


#  ["khergit_tribesman","Khergit Tribesman","Khergit Tribesmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_3,
#   [itm_arrows,itm_club,itm_spear,itm_hunting_bow,
#    itm_steppe_cap,itm_nomad_cap_b,itm_leather_vest,itm_steppe_armor,itm_nomad_boots,itm_khergit_leather_boots],
#   def_attrib|level(5),wp(50),knows_common|knows_riding_3|knows_power_draw_2|knows_horse_archery_2,khergit_face_younger_1, khergit_face_old_2],
#  ["khergit_skirmisher","Khergit Skirmisher","Khergit Skirmishers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_3,
#   [itm_arrows,itm_sword_khergit_1,itm_winged_mace,itm_spear,itm_nomad_bow,itm_javelin,itm_tab_shield_small_round_a,
#    itm_steppe_cap,itm_nomad_cap_b,itm_leather_steppe_cap_a,itm_khergit_armor,itm_steppe_armor,itm_leather_vest,itm_nomad_boots,itm_khergit_leather_boots,itm_steppe_horse,itm_saddle_horse],
#   def_attrib|level(10),wp(60)|wp_archery(80)|wp_throwing(80),knows_common|knows_riding_4|knows_power_draw_3|knows_power_throw_1|knows_horse_archery_3,khergit_face_younger_1, khergit_face_old_2],
#  ["khergit_horseman","Khergit Horseman","Khergit Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_3,
#  [itm_arrows,itm_light_lance,itm_nomad_bow,itm_sword_khergit_2,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,itm_spear,
#   itm_leather_steppe_cap_a, itm_leather_steppe_cap_b,itm_nomad_robe,itm_nomad_vest,itm_khergit_leather_boots,itm_hide_boots,itm_spiked_helmet,itm_nomad_cap,itm_steppe_horse,itm_hunter],
#   def_attrib|level(14),wp(80),knows_common|knows_riding_5|knows_power_draw_4|knows_ironflesh_1|knows_power_throw_1,khergit_face_young_1, khergit_face_older_2],
#  ["khergit_horse_archer","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_3,
#   [itm_arrows,itm_sword_khergit_2,itm_winged_mace,itm_spear,itm_khergit_bow,itm_tab_shield_small_round_a,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,itm_bodkin_arrows,itm_arrows,itm_javelin,
#    itm_leather_steppe_cap_b,itm_nomad_cap_b,itm_tribal_warrior_outfit,itm_nomad_robe,itm_khergit_leather_boots,itm_tab_shield_small_round_a,itm_tab_shield_small_round_b,itm_steppe_horse],
#   def_attrib|level(14),wp(80)|wp_archery(110),knows_riding_5|knows_power_draw_3|knows_ironflesh_1|knows_horse_archery_4|knows_power_throw_1,khergit_face_young_1, khergit_face_older_2],
#  ["khergit_veteran_horse_archer","Khergit Veteran Horse Archer","Khergit Veteran Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
#   [itm_sword_khergit_3,itm_winged_mace,itm_spear,itm_khergit_bow,itm_nomad_bow,itm_nomad_bow,itm_arrows,itm_khergit_arrows,itm_khergit_arrows,itm_javelin,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,
#    itm_khergit_cavalry_helmet,itm_khergit_cavalry_helmet,itm_leather_warrior_cap,itm_lamellar_vest_khergit,itm_tribal_warrior_outfit,itm_khergit_leather_boots,itm_leather_gloves,itm_steppe_horse,itm_courser],
#   def_attrib|level(21),wp(90)|wp_archery(130),knows_riding_7|knows_power_draw_5|knows_ironflesh_3|knows_horse_archery_5|knows_power_throw_3,khergit_face_middle_1, khergit_face_older_2],
#  ["khergit_lancer","Khergit Lancer","Khergit Lancers",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
#   [itm_sword_khergit_4,itm_spiked_mace,itm_one_handed_war_axe_b,itm_one_handed_war_axe_a,itm_hafted_blade_a,itm_hafted_blade_b,itm_heavy_lance,itm_lance,
#    itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_war_helmet,itm_lamellar_vest_khergit,itm_lamellar_armor,itm_khergit_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves,itm_scale_gauntlets,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,itm_courser],
#   def_attrib|level(23),wp(150),knows_riding_7|knows_power_strike_5|knows_power_draw_2|knows_power_throw_2|knows_ironflesh_5|knows_horse_archery_1,khergit_face_middle_1, khergit_face_older_2],

#  ["khergit_messenger","Khergit Messenger","Khergit Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_3,
#   [itm_sword_khergit_2,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
#   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,khergit_face_young_1, khergit_face_older_2],
#  ["khergit_deserter","Khergit Deserter","Khergit Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
#   [itm_arrows,itm_spiked_mace,itm_axe,itm_sword_khergit_1,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap_b,itm_khergit_armor,itm_steppe_armor,itm_tribal_warrior_outfit,itm_nomad_boots],
#   def_attrib|str_10|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,khergit_face_young_1, khergit_face_older_2],
#  ["khergit_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
#   [itm_sword_khergit_3,itm_tab_shield_small_round_b,itm_tab_shield_small_round_a,itm_lamellar_vest_khergit,itm_lamellar_armor,itm_khergit_leather_boots,itm_iron_greaves,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_leather_warrior_cap],
#   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,khergit_face_middle_1, khergit_face_older_2],
#  ["khergit_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_3,
#   [itm_sword_khergit_4,itm_tab_shield_small_round_b,itm_tab_shield_small_round_a,itm_lamellar_vest_khergit,itm_lamellar_armor,itm_khergit_leather_boots,itm_iron_greaves,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_leather_warrior_cap],
#   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,khergit_face_middle_1, khergit_face_older_2],


#  ["nord_recruit","Nord Recruit","Nord Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
#   [itm_axe,itm_hatchet,itm_spear,itm_tab_shield_round_a,itm_tab_shield_round_a,
#    itm_blue_tunic,itm_coarse_tunic,itm_hide_boots,itm_nomad_boots],
#   def_attrib|level(6),wp(50),knows_power_strike_1|knows_power_throw_1|knows_riding_1|knows_athletics_1,nord_face_younger_1, nord_face_old_2],
#  ["nord_footman","Nord Footman","Nord Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_4,
#   [itm_fighting_axe,itm_one_handed_war_axe_a,itm_spear,itm_tab_shield_round_a,itm_tab_shield_round_b,itm_javelin,itm_throwing_axes,
#    itm_leather_cap,itm_skullcap,itm_nomad_vest,itm_leather_boots,itm_nomad_boots],
#   def_attrib|level(10),wp(70),knows_ironflesh_2|knows_power_strike_2|knows_power_throw_2|knows_riding_2|knows_athletics_2|knows_shield_1,nord_face_young_1, nord_face_old_2],
#  ["nord_trained_footman","Nord Trained Footman","Nord Trained Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
#   [itm_one_handed_war_axe_a,itm_one_handed_war_axe_b,itm_one_handed_battle_axe_a,itm_tab_shield_round_b,
#    itm_skullcap,itm_nasal_helmet,itm_nordic_footman_helmet,itm_byrnie,itm_studded_leather_coat,itm_leather_boots],
#   def_attrib|level(14),wp(100),knows_ironflesh_3|knows_power_strike_3|knows_power_throw_2|knows_riding_2|knows_athletics_3|knows_shield_2,nord_face_young_1, nord_face_old_2],
#  ["nord_warrior","Nord Warrior","Nord Warriors",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
#   [itm_sword_viking_1,itm_one_handed_war_axe_b,itm_one_handed_battle_axe_a,itm_tab_shield_round_c,itm_javelin,
#    itm_nordic_footman_helmet,itm_nordic_fighter_helmet,itm_mail_shirt,itm_studded_leather_coat,itm_hunter_boots,itm_leather_boots],
#   def_attrib|level(19),wp(115),knows_ironflesh_4|knows_power_strike_4|knows_power_throw_3|knows_riding_2|knows_athletics_4|knows_shield_3,nord_face_young_1, nord_face_older_2],
#  ["nord_veteran","Nord Veteran","Nord Veterans",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
#   [itm_sword_viking_2,itm_sword_viking_2_small,itm_one_handed_battle_axe_b,itm_spiked_mace,itm_tab_shield_round_d,itm_javelin,itm_throwing_axes,
#    itm_nordic_helmet,itm_nordic_fighter_helmet,itm_mail_hauberk,itm_mail_shirt,itm_splinted_leather_greaves,itm_leather_boots,itm_leather_gloves],
#   def_attrib|level(24),wp(145),knows_ironflesh_5|knows_power_strike_5|knows_power_throw_4|knows_riding_3|knows_athletics_5|knows_shield_4,nord_face_young_1, nord_face_older_2],
#  ["nord_champion","Nord Huscarl","Nord Huscarls",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_4,
#   [itm_sword_viking_3,itm_sword_viking_3_small,itm_great_axe,itm_one_handed_battle_axe_c,itm_tab_shield_round_e,itm_throwing_spears,itm_heavy_throwing_axes,itm_heavy_throwing_axes,
#    itm_nordic_huscarl_helmet,itm_nordic_warlord_helmet,itm_banded_armor,itm_mail_boots,itm_mail_chausses,itm_mail_mittens],
#   def_attrib|level(28),wp(170),knows_ironflesh_7|knows_power_strike_7|knows_power_throw_5|knows_riding_2|knows_athletics_7|knows_shield_6,nord_face_middle_1, nord_face_older_2],
#  ["nord_huntsman","Nord Huntsman","Nord Huntsmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
#   [itm_arrows,itm_rawhide_coat,itm_hatchet,itm_hunting_bow,itm_hide_boots],
#   def_attrib|str_10|level(11),wp_melee(60)|wp_archery(70),knows_ironflesh_1|knows_power_draw_1|knows_athletics_2,nord_face_young_1, nord_face_old_2],
#  ["nord_archer","Nord Archer","Nord Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
#   [itm_arrows,itm_axe,itm_short_bow,itm_leather_jerkin,itm_leather_boots,itm_nasal_helmet,itm_nordic_archer_helmet,itm_leather_cap],
#   def_attrib|str_11|level(15),wp_melee(80)|wp_archery(90),knows_ironflesh_2|knows_power_draw_3|knows_athletics_5,nord_face_young_1, nord_face_old_2],
#  ["nord_veteran_archer","Nord Veteran Archer","Nord Veteran Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_4,
#   [itm_bodkin_arrows,itm_axe,itm_sword_viking_1,itm_long_bow,itm_leather_jerkin,itm_padded_leather,itm_leather_boots,itm_nordic_archer_helmet,itm_nordic_veteran_archer_helmet],
#   def_attrib|str_12|level(19),wp_melee(95)|wp_archery(120),knows_power_strike_3|knows_ironflesh_4|knows_power_draw_5|knows_athletics_7,nord_face_middle_1, nord_face_older_2],

#  ["nord_messenger","Nord Messenger","Nord Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_4,
#   [itm_sword_viking_2,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
#   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,nord_face_young_1, nord_face_older_2],
#  ["nord_deserter","Nord Deserter","Nord Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
#   [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
#   def_attrib|str_10|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,nord_face_young_1, nord_face_older_2],
#  ["nord_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
#   [itm_ashwood_pike,itm_battle_fork,itm_battle_axe,itm_fighting_axe,itm_tab_shield_round_d,itm_mail_hauberk,itm_mail_chausses,itm_iron_greaves,itm_nordic_helmet,itm_nordic_helmet,itm_nordic_helmet,itm_spiked_helmet,itm_leather_gloves],
#   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,nord_face_middle_1, nord_face_older_2],
#  ["nord_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
#   [itm_ashwood_pike,itm_battle_fork,itm_battle_axe,itm_fighting_axe,itm_tab_shield_round_d,itm_tab_shield_round_e,itm_mail_hauberk,itm_heraldic_mail_with_tabard,itm_mail_chausses,itm_iron_greaves,itm_nordic_helmet,itm_nordic_helmet,itm_nordic_helmet,itm_spiked_helmet,itm_leather_gloves],
#   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,nord_face_middle_1, nord_face_older_2],


#  ["rhodok_tribesman","Rhodok Tribesman","Rhodok Tribesmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_5,
#   [itm_pitch_fork,itm_tab_shield_pavise_a,
#    itm_shirt,itm_coarse_tunic,itm_wrapping_boots,itm_nomad_boots,itm_head_wrappings],
#   def_attrib|level(4),wp(55),knows_common|knows_power_draw_2|knows_ironflesh_1,rhodok_face_younger_1, rhodok_face_old_2],
#  ["rhodok_spearman","Rhodok Spearman","Rhodok Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_5,
#   [itm_spear,itm_tab_shield_pavise_a,itm_tab_shield_pavise_a,
#    itm_leather_cap,itm_common_hood,itm_leather_vest,itm_leather_vest,itm_wrapping_boots,itm_nomad_boots],
#   def_attrib|level(9),wp(80),knows_common|knows_ironflesh_2|knows_shield_1|knows_power_strike_2|knows_athletics_1,rhodok_face_young_1, rhodok_face_old_2],
#  ["rhodok_trained_spearman","Rhodok Trained Spearman","Rhodok Trained Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_5,
#   [itm_pike,itm_spear,itm_tab_shield_pavise_b,
#    itm_leather_cap,itm_leather_vest,itm_ragged_outfit,itm_padded_cloth,itm_gambeson,itm_nomad_boots],
#   def_attrib|level(14),wp(105),knows_common|knows_ironflesh_3|knows_shield_2|knows_power_strike_2|knows_athletics_2,rhodok_face_young_1, rhodok_face_older_2],
#  ["rhodok_veteran_spearman","Rhodok Veteran Spearman","Rhodok Veteran Spearmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_5,
#   [itm_ashwood_pike,itm_war_spear,itm_pike,itm_club_with_spike_head,itm_tab_shield_pavise_c,itm_sword_medieval_a,
#    itm_leather_cap,itm_skullcap,itm_byrnie,itm_ragged_outfit,itm_nomad_boots],
#   def_attrib|level(19),wp(115),knows_common|knows_ironflesh_5|knows_shield_3|knows_power_strike_4|knows_athletics_3,rhodok_face_young_1, rhodok_face_older_2],
#  ["rhodok_sergeant","Rhodok Sergeant","Rhodok Sergeants",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_shield,0,0,fac_kingdom_5,
#   [itm_glaive,itm_military_hammer,itm_war_spear,itm_sword_medieval_b,itm_tab_shield_pavise_d,
#    itm_kettle_hat, itm_bascinet_3,itm_bascinet_2,itm_surcoat_over_mail,itm_banded_armor,itm_nomad_boots,],
#   def_attrib|level(25),wp(130),knows_common|knows_ironflesh_7|knows_shield_5|knows_power_strike_5|knows_athletics_5,rhodok_face_middle_1, rhodok_face_older_2],
#  ["rhodok_crossbowman","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged,0,0,fac_kingdom_5,
#   [itm_sword_medieval_a,itm_falchion,itm_club_with_spike_head,itm_tab_shield_pavise_a,itm_crossbow,itm_bolts,
#    itm_leather_jerkin,itm_ragged_outfit,itm_nomad_boots],
#   def_attrib|level(10),wp(85),knows_common|knows_ironflesh_2|knows_shield_1|knows_power_strike_1|knows_athletics_2,rhodok_face_young_1, rhodok_face_older_2],
#  ["rhodok_trained_crossbowman","Rhodok Trained Crossbowman","Rhodok Trained Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_5,
#   [itm_sword_medieval_a,itm_sword_medieval_b_small,itm_club_with_spike_head,itm_tab_shield_pavise_a,itm_tab_shield_pavise_a,itm_crossbow,itm_bolts,
#    itm_leather_cap,itm_leather_jerkin,itm_ragged_outfit,itm_nomad_boots],
#   def_attrib|level(15),wp_melee(90)|wp_crossbow(105),knows_common|knows_ironflesh_3|knows_shield_2|knows_power_strike_2|knows_athletics_3,rhodok_face_young_1, rhodok_face_older_2],
#  ["rhodok_veteran_crossbowman","Rhodok Veteran Crossbowman","Rhodok Veteran Crossbowmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_5,
#   [itm_sword_medieval_a,itm_sword_medieval_b_small,itm_fighting_pick,itm_club_with_spike_head,itm_tab_shield_pavise_a,itm_tab_shield_pavise_b,itm_tab_shield_pavise_c,itm_heavy_crossbow,itm_bolts,
#    itm_leather_cap,itm_leather_jerkin,itm_padded_leather,itm_nomad_boots],
#   def_attrib|level(20),wp_melee(100)|wp_crossbow(120),knows_common|knows_ironflesh_4|knows_shield_3|knows_power_strike_3|knows_athletics_4,rhodok_face_middle_1, rhodok_face_older_2],
#  ["rhodok_sharpshooter","Rhodok Sharpshooter","Rhodok Sharpshooters",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_5,
#   [itm_sword_medieval_b,itm_military_pick,itm_military_hammer,itm_tab_shield_pavise_c,itm_sniper_crossbow,itm_steel_bolts,
#    itm_kettle_hat,itm_leather_cap,itm_byrnie,itm_padded_leather,itm_leather_boots],
#   def_attrib|level(25),wp_melee(110)|wp_crossbow(140),knows_common|knows_ironflesh_5|knows_shield_4|knows_power_strike_4|knows_athletics_6,rhodok_face_middle_1, rhodok_face_older_2],

#  ["rhodok_messenger","Rhodok Messenger","Rhodok Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_4,
#   [itm_sword_medieval_b,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_short_bow,itm_arrows],
#   def_attrib|agi_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_power_draw_5,rhodok_face_middle_1, rhodok_face_older_2],
#  ["rhodok_deserter","Rhodok Deserter","Rhodok Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
#   [itm_arrows,itm_spiked_mace,itm_axe,itm_falchion,itm_short_bow,itm_short_bow,itm_hunting_bow,itm_javelin,itm_javelin,itm_steppe_cap,itm_nomad_cap,itm_leather_vest,itm_leather_vest,itm_nomad_armor,itm_nomad_boots],
#   def_attrib|str_10|level(14),wp(80),knows_ironflesh_1|knows_power_draw_1,rhodok_face_middle_1, rhodok_face_older_2],
#  ["rhodok_prison_guard","Prison Guard","Prison Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
#   [itm_ashwood_pike,itm_battle_fork,itm_battle_axe,itm_fighting_axe,itm_tab_shield_pavise_b,itm_mail_hauberk,itm_byrnie,itm_mail_chausses,itm_iron_greaves,itm_guard_helmet,itm_leather_gloves],
#   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,rhodok_face_middle_1, rhodok_face_older_2],
#  ["rhodok_castle_guard","Castle Guard","Castle Guards", tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_4,
#   [itm_ashwood_pike,itm_battle_fork,itm_battle_axe,itm_fighting_axe,itm_tab_shield_pavise_c,itm_mail_hauberk,itm_byrnie,itm_mail_chausses,itm_iron_greaves,itm_guard_helmet,itm_leather_gloves],
#   def_attrib|level(24),wp(130),knows_athletics_3|knows_shield_2|knows_ironflesh_3,rhodok_face_middle_1, rhodok_face_older_2],
#peasant - retainer - footman - man-at-arms -  knight


# ["sarranid_recruit","Sarranid Recruit","Sarranid Recruits",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
#   [itm_scythe,itm_hatchet,itm_pickaxe,itm_club,itm_stones,itm_tab_shield_heater_a,itm_sarranid_felt_hat,itm_turban,itm_sarranid_boots_a,
#    itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b],
#   def_attrib|level(4),wp(60),knows_common|knows_athletics_1,swadian_face_younger_1, swadian_face_middle_2],
# ["sarranid_footman","Sarranid Footman","Sarranid Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_kingdom_6,
#   [itm_bamboo_spear,itm_arabian_sword_a,itm_tab_shield_kite_a,itm_desert_turban,
#    itm_skirmisher_armor,itm_turban,itm_sarranid_boots_a,itm_sarranid_boots_b],
#   def_attrib|level(9),wp(75),knows_common|knows_athletics_2,swadian_face_young_1, swadian_face_old_2],
# ["sarranid_veteran_footman","Sarranid Veteran Footman","Sarranid Veteran Footmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield|tf_guarantee_helmet,0,0,fac_kingdom_6,
#   [itm_bamboo_spear,itm_sarranid_mail_coif,itm_arabian_sword_a,itm_arabian_sword_b,itm_tab_shield_kite_b,
#    itm_sarranid_boots_b,itm_sarranid_leather_armor,itm_arabian_sword_a,itm_mace_3],
#   def_attrib|level(14),wp_melee(85)|wp_throwing(80),knows_common|knows_ironflesh_1|knows_shield_2,swadian_face_young_1, swadian_face_old_2],
# ["sarranid_infantry","Sarranid Infantry","Sarranid Infantries",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
#   [itm_sarranid_mail_shirt,itm_sarranid_warrior_cap,itm_sarranid_boots_c,itm_sarranid_boots_b,itm_arabian_sword_b,itm_mace_3,itm_spear,itm_tab_shield_kite_c],
#   def_attrib|level(20),wp_melee(105)|wp_throwing(90),knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_3|knows_athletics_3,swadian_face_middle_1, swadian_face_old_2],
# ["sarranid_guard","Sarranid Guard","Sarranid Guards",tf_mounted|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
#   [itm_military_pick,itm_arabian_sword_b,itm_scimitar_b,itm_war_spear,itm_mace_4,itm_sarranid_boots_d, itm_sarranid_boots_c,itm_arabian_armor_b,itm_sarranid_mail_coif,itm_sarranid_veiled_helmet,itm_mail_mittens,itm_leather_gloves,itm_tab_shield_kite_d],
#   def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3|knows_athletics_5,swadian_face_middle_1, swadian_face_older_2],
# ["sarranid_skirmisher","Sarranid Skirmisher","Sarranid Skirmishers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
#   [itm_turban,itm_desert_turban,itm_skirmisher_armor,itm_jarid,itm_jarid,itm_arabian_sword_a,itm_spiked_club,itm_tab_shield_small_round_a,itm_sarranid_warrior_cap,itm_sarranid_boots_a],
#   def_attrib|level(14),wp(80),knows_common|knows_riding_2|knows_power_throw_1|knows_power_draw_1|knows_ironflesh_1|knows_athletics_2,swadian_face_young_1, swadian_face_middle_2],
# ["sarranid_archer","Sarranid Archer","Sarranid Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
#   [itm_arrows,itm_nomad_bow,itm_arabian_sword_a,itm_archers_vest,itm_sarranid_boots_b,itm_sarranid_helmet1,itm_turban,itm_desert_turban],
#   def_attrib|level(19),wp_melee(90)|wp_archery(100),knows_common|knows_riding_2|knows_power_draw_2|knows_ironflesh_1|knows_athletics_2,swadian_face_young_1, swadian_face_old_2],
# ["sarranid_master_archer","Sarranid Master Archer","Sarranid Master Archers",tf_guarantee_ranged|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
#   [itm_arrows,itm_arabian_sword_b,itm_mace_3,itm_strong_bow,
#    itm_arabian_armor_b,itm_leather_boots,itm_arrows,itm_sarranid_boots_c,itm_sarranid_boots_b,itm_sarranid_mail_coif],
#   def_attrib|str_14|level(24),wp_melee(100)|wp_archery(120),knows_common|knows_power_draw_3|knows_ironflesh_1|knows_athletics_3,swadian_face_middle_1, swadian_face_older_2],
# ["sarranid_horseman","Sarranid Horseman","Sarranid Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
#   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
#    itm_sarranid_mail_shirt,itm_sarranid_boots_c,itm_sarranid_boots_b, itm_sarranid_horseman_helmet,itm_courser,itm_hunter],
#   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
# ["sarranid_mamluke","Sarranid Mamluke","Sarranid Mamlukes",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
#   [itm_heavy_lance,itm_scimitar_b,itm_morningstar,itm_sarranid_cavalry_sword,itm_tab_shield_small_round_c,
#    itm_mamluke_mail,itm_sarranid_boots_d,itm_sarranid_boots_c,itm_sarranid_veiled_helmet,itm_arabian_horse_a,itm_warhorse,itm_leather_gloves,itm_mail_mittens],
#   def_attrib|level(27),wp_melee(130),knows_common|knows_riding_5|knows_shield_3|knows_ironflesh_4|knows_power_strike_5,swadian_face_middle_1, swadian_face_older_2],

#  ["sarranid_messenger","Sarranid Messenger","Sarranid Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_kingdom_1,
#   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
#    itm_sarranid_mail_shirt,itm_mail_chausses,itm_sarranid_helmet1,itm_courser,itm_hunter],
#   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
#  ["sarranid_deserter","Sarranid Deserter","Sarranid Deserters",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_deserters,
#   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
#    itm_sarranid_mail_shirt,itm_mail_chausses,itm_desert_turban,itm_arabian_horse_a],
#   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
#  ["sarranid_prison_guard","Prison Guard","Prison Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
#   [itm_arabian_sword_b,itm_scimitar_b,itm_war_spear,itm_mace_4,itm_sarranid_boots_c,itm_arabian_armor_b,itm_sarranid_mail_coif,itm_sarranid_helmet1,itm_sarranid_horseman_helmet,itm_mail_boots,itm_iron_greaves,itm_mail_mittens,itm_leather_gloves,itm_tab_shield_kite_d],
#   def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_middle_1, swadian_face_older_2],
#  ["sarranid_castle_guard","Castle Guard","Castle Guards",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_1,
#   [itm_arabian_sword_b,itm_scimitar_b,itm_war_spear,itm_mace_4,itm_sarranid_boots_c, itm_sarranid_boots_d,itm_arabian_armor_b,itm_sarranid_mail_coif,itm_sarranid_helmet1,itm_sarranid_horseman_helmet,itm_mail_boots,itm_iron_greaves,itm_mail_mittens,itm_leather_gloves,itm_tab_shield_kite_d],
#   def_attrib|level(25),wp_melee(135)|wp_throwing(100),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_3,swadian_face_middle_1, swadian_face_older_2],

###############################################################
##### end native faction troops commented out for TGS
###############################################################

######################################
##### WoT Faction Troops (Upgradeable)
######################################


# Legion of the Dragon
#  ["legion_recruit","Legion Recruit","Legion Recruits",tf_guarantee_armor,0,0,fac_kingdom_1,
#   [itm_scythe,itm_hatchet,itm_stones,itm_leather_cap,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_wrapping_boots],
#   def_attrib|level(2),wp(60),knows_common,mayene_man_face_young, tear_man_face_old],
#
    ["legion_recruit_channeler","Legion Recruit (Channeler)","Legion Recruits (Channeler)",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_power_player, itm_power_ammo,itm_channeler_dagger, itm_legion_recruit_tunic, itm_wrapping_boots],
   def_attrib_wot_infantry_1 ,wp_firearm(65)|wp(60),knows_wot_infantry_1|knows_power_draw_1|knows_fire_1|knows_earth_1|knows_spirit_1|knows_water_3|knows_air_1 ,far_madding_man_face_younger, illian_man_face_older],

    ["ashaman_soldier","Asha'man Soldier","Asha'man Soldiers",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_power_player, itm_power_ammo, itm_sword_secondary, itm_ashaman_soldier_coat, itm_black_leather_boots],
   def_attrib_wot_infantry_1,wp_firearm(105)|wp_one_handed(100)|wp(75),knows_wot_infantry_1|knows_power_draw_2|knows_fire_4|knows_earth_2|knows_spirit_3|knows_water_4|knows_air_2,murandy_man_face_young, altara_man_face_older],

    ["ashaman_dedicated","Asha'man Dedicated","Asha'man Dedicated",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_power_player, itm_power_ammo, itm_ashaman_dedicated_coat, itm_black_leather_boots],
   def_attrib_wot_infantry_2,wp_firearm(130)|wp_one_handed(110)|wp(80),knows_wot_infantry_2|knows_power_draw_3|knows_fire_5|knows_earth_6|knows_spirit_5|knows_water_4|knows_air_4,ghealdan_man_face_younger, amadicia_man_face_older],
  
    ["ashaman","Asha'man","Asha'man",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_power_player, itm_power_ammo, itm_ashaman_coat, itm_black_leather_boots, itm_saddle_horse],
   def_attrib_wot_infantry_2,wp_firearm(175)|wp_one_handed(110)|wp(90),knows_wot_horse_archer_2|knows_power_draw_4|knows_fire_7|knows_earth_6|knows_spirit_6|knows_water_5|knows_air_4,tarabon_man_face_younger, arad_doman_man_face_older],
  
#    ["legion_recruit_soldier","Legion Recruit Soldier","Legion Recruits (Soldier)",tf_guarantee_all,0,0,fac_kingdom_1,
#   [itm_sword_medieval_a, itm_legion_recruit_tunic, itm_wrapping_boots],
#   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1 ,man_face_young_1, man_face_old_2],
  
    ["legion_recruit_army","Legion Recruit (Army)","Legion Recruits (Army)",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_sword_medieval_a, itm_legion_shield_weak, itm_legion_recruit_tunic, itm_wrapping_boots],
   def_attrib_wot_infantry_1 ,wp_one_handed(80)|wp(70),knows_wot_infantry_1 ,man_face_young_1, man_face_old_2],
  
    ["legion_footman","Legion Footman","Legion Footmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_sword_medieval_b, itm_legion_shield_weak, itm_legion_army_tunic, itm_leather_boots, itm_leather_gloves, itm_skullcap],
   def_attrib_wot_infantry_2 ,wp_one_handed(90)|wp(70),knows_wot_infantry_2 ,man_face_young_1, man_face_old_2],
  
    ["legion_infantry","Legion Infantry","Legion Infantry",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_hammer, itm_legion_army_tunic, itm_legion_shield_normal, itm_leather_boots, itm_leather_gloves, itm_nordic_helmet],
   def_attrib_wot_infantry_2 ,wp_one_handed(110)|wp(75),knows_wot_infantry_2 ,man_face_young_1, man_face_old_2],
  
    ["legion_swordsman","Legion Swordsman","Legion Swordsmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_sword_medieval_b, itm_legion_army_armor, itm_legion_shield_strong, itm_leather_boots, itm_leather_gloves, itm_nordic_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(125)|wp(80),knows_wot_infantry_3 ,man_face_young_1, man_face_old_2],
  
    ["legion_pikeman","Legion Pikeman","Legion Pikemen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_pike, itm_legion_army_armor,itm_legion_shield_strong, itm_leather_boots, itm_leather_gloves, itm_nordic_helmet],
   def_attrib_wot_infantry_3 ,wp_polearm(125)|wp(80),knows_wot_infantry_3 ,man_face_young_1, man_face_old_2],
  
    ["legion_crossbowman","Legion Crossbowman","Legion Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_crossbow, itm_bolts, itm_sword_secondary, itm_legion_army_tunic, itm_leather_boots, itm_leather_gloves, itm_skullcap],
   def_attrib_wot_infantry_2 ,wp_crossbow(100)|wp_one_handed(90)|wp(70),knows_wot_archer_2 ,man_face_young_1, man_face_old_2],
  
    ["legion_cavalry","Legion Cavalry","Legion Cavalry",tf_guarantee_all_cavalry,0,0,fac_kingdom_1,
   [itm_war_spear, itm_sword_medieval_a, itm_legion_army_tunic, itm_leather_boots, itm_leather_gloves, itm_skullcap, itm_saddle_horse],
   def_attrib_wot_cavalry_1 ,wp_polearm(100)|wp_one_handed(95)|wp(70),knows_wot_cavalry_1 ,man_face_young_1, man_face_old_2],
  
    ["legion_lancer","Legion Lancer","Legion Lancers",tf_guarantee_all_cavalry,0,0,fac_kingdom_1,
   [itm_lance, itm_sword_medieval_c_long, itm_legion_shield_normal, itm_legion_army_armor, itm_leather_boots, itm_leather_gloves, itm_nordic_helmet, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_polearm(120)|wp_one_handed(110)|wp(85),knows_wot_cavalry_2 ,man_face_young_1, man_face_old_2],
  
    ["legion_man_at_arms","Legion Man at Arms","Legion Man at Arms",tf_guarantee_all_cavalry,0,0,fac_kingdom_1,
   [itm_spiked_mace, itm_legion_shield_normal, itm_sword_viking_3, itm_legion_army_armor, itm_leather_boots, itm_leather_gloves, itm_nordic_helmet, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_polearm(120)|wp_one_handed(120)|wp(85),knows_wot_cavalry_2 ,man_face_young_1, man_face_old_2],
  
#    ["legion_ally","Legion Ally","Legion Allies",tf_guarantee_armor,0,0,fac_kingdom_1,
#   [itm_scythe,itm_hatchet,itm_stones,itm_leather_cap,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_wrapping_boots],
#   def_attrib|level(2),wp(60),knows_common,man_face_young_1, man_face_old_2],
  
#    ["legion_true_ally","Legion True Ally","Legion True Allies",tf_guarantee_armor,0,0,fac_kingdom_1,
#   [itm_scythe,itm_hatchet,itm_stones,itm_leather_cap,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_wrapping_boots],
#   def_attrib|level(3),wp(65),knows_common,man_face_young_1, man_face_old_2],
  
#    ["legion_true_ally_mat","Legion True Ally (Mat)","Legion True Allies (Mat)",tf_guarantee_armor,0,0,fac_kingdom_1,
#   [itm_scythe,itm_hatchet,itm_stones,itm_leather_cap,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_wrapping_boots],
#   def_attrib|level(3),wp(65),knows_common,man_face_young_1, man_face_old_2],

# Conquered Legion Ally troops will be listed under their respective faction troop sets
#    ["legion_conquered_ally","Legion Conquered Ally","Legion Conquered Allies",tf_guarantee_armor,0,0,fac_kingdom_1,
#   [itm_scythe,itm_hatchet,itm_stones,itm_leather_cap,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_wrapping_boots],
#   def_attrib|level(3),wp(65),knows_common, man_face_young_1, man_face_old_2],
  
#    ["legion_north_east_ally","Legion North East Ally","Legion North East Allies",tf_guarantee_armor,0,0,fac_kingdom_1,
#   [itm_scythe,itm_hatchet,itm_stones,itm_leather_cap,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_wrapping_boots],
#   def_attrib|level(3),wp(65),knows_common, man_face_young_1, man_face_old_2],
  
    ["legion_cairhien_ally","Legion Cairhien Ally","Legion Cairhien Allies",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_cudgel, itm_cairhien_recruit_tunic, itm_wrapping_boots, itm_woolen_cap],
   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1 ,cairhien_man_face_young, cairhien_man_face_older],
  
    ["legion_andor_ally","Legion Andor Ally","Legion Andor Allies",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_club, itm_andor_recruit_tunic, itm_wrapping_boots],
   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1, andor_man_face_young, andor_man_face_older],
  
#    ["legion_south_east_ally","Legion South East Ally","Legion South East Allies",tf_guarantee_armor,0,0,fac_kingdom_1,
#   [itm_scythe,itm_hatchet,itm_stones,itm_leather_cap,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_wrapping_boots],
#   def_attrib|level(3),wp(65),knows_common, man_face_young_1, man_face_old_2],
  
    ["legion_tear_ally","Legion Tear Ally","Legion Tear Allies",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_hand_axe, itm_tear_recruit_tunic, itm_wrapping_boots],
   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1, tear_man_face_young, tear_man_face_older],
  
    ["legion_illian_ally","Legion Illian Ally","Legion Illian Allies",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_illian_seax, itm_illian_recruit_tunic, itm_wrapping_boots],
   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1, illian_man_face_young, illian_man_face_older],  

## Band of the Red Hand  
    ["red_hand_recruit","Red Hand Recruit","Red Hand Recruits",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
   [itm_sword_medieval_a, itm_red_hand_tunic, itm_wrapping_boots],
   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1 ,man_face_young_1, man_face_old_2],
  
    ["red_hand_infantry","Red Hand Redarm","Red Hand Redarms",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
   [itm_red_arm_club, itm_red_arm_tunic, itm_red_hand_shield_weak, itm_leather_boots, itm_leather_gloves, itm_red_hand_bell_helm],
   def_attrib_wot_infantry_2 ,wp_one_handed(110)|wp(75),knows_wot_infantry_2 ,man_face_young_1, man_face_old_2],
  
    ["red_hand_pikeman","Red Hand Pikeman","Red Hand Pikemen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
   [itm_pike, itm_red_hand_tunic,itm_red_hand_shield_normal, itm_leather_boots, itm_leather_gloves, itm_red_hand_bell_helm],
   def_attrib_wot_infantry_3 ,wp_polearm(125)|wp(80),knows_wot_infantry_3 ,man_face_young_1, man_face_old_2],
  
    ["red_hand_crossbowman","Red Hand Crossbowman","Red Hand Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_crossbow, itm_bolts, itm_sword_secondary, itm_red_hand_tunic, itm_leather_boots, itm_leather_gloves, itm_red_hand_bell_helm],
   def_attrib_wot_infantry_2 ,wp_crossbow(100)|wp_one_handed(90)|wp(70),knows_wot_archer_2 ,man_face_young_1, man_face_old_2],
  
    ["red_hand_man_at_arms","Red Hand Man at Arms","Red Hand Man at Arms",tf_guarantee_all_cavalry,0,0,fac_kingdom_2,
   [itm_red_arm_hammer, itm_red_hand_shield_weak, itm_sword_viking_3, itm_red_arm_tunic, itm_leather_boots, itm_leather_gloves, itm_red_hand_bell_helm, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_polearm(120)|wp_one_handed(120)|wp(85),knows_wot_cavalry_2 ,man_face_young_1, man_face_old_2],
  
    ["red_hand_light_cavalry","Red Hand Light Cavalry","Red Hand Light Cavalry",tf_guarantee_all_cavalry,0,0,fac_kingdom_2,
   [itm_war_spear, itm_sword_medieval_a, itm_red_hand_shield_normal, itm_red_hand_tunic, itm_leather_boots, itm_leather_gloves, itm_red_hand_bell_helm, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_polearm(120)|wp_one_handed(110)|wp(85),knows_wot_cavalry_2 ,man_face_young_1, man_face_old_2],
  #
#    ["legion_true_ally_perrin","Legion True Ally (Perrin)","Legion True Allies (Perrin)",tf_guarantee_armor,0,0,fac_kingdom_1,
#   [itm_scythe,itm_hatchet,itm_stones,itm_leather_cap,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_wrapping_boots],
#   def_attrib|level(3),wp(65),knows_common, andor_man_face_younger, andor_man_face_older],

## Two Rivers  
    ["two_rivers_farmer","Two Rivers Farmer","Two Rivers Farmers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
   [itm_hatchet, itm_scythe, itm_leather_apron, itm_ragged_outfit, itm_leather_cap, itm_felt_hat, itm_leather_boots],
   def_attrib_wot_infantry_1 ,wp(75),knows_wot_infantry_1, andor_man_face_younger, andor_man_face_older],
  
    ["two_rivers_spearman","Two Rivers Spearman","Two Rivers Spearmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
   [itm_spear, itm_ragged_outfit, itm_leather_jerkin, itm_leather_boots, itm_leather_gloves, itm_leather_cap, itm_segmented_helmet],
   def_attrib_wot_infantry_2 ,wp_polearm(125)|wp(80),knows_wot_infantry_2, andor_man_face_younger, andor_man_face_older],
  
    ["two_rivers_longbowman","Two Rivers Longbowman","Two Rivers Longbowmen",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_long_bow, itm_arrows, itm_sword_secondary, itm_ragged_outfit, itm_leather_jerkin, itm_leather_boots, itm_leather_gloves, itm_leather_cap, itm_segmented_helmet],
   def_attrib_wot_infantry_4 ,wp_archery(125)|wp_one_handed(110)|wp(100),knows_wot_archer_4 ,andor_man_face_younger, andor_man_face_older],
  



# Southlander Coalition (1)

#  ["southlander_1_recruit","Southlander Coalition Recruit","Southlander Coalition Recruits",tf_guarantee_armor,0,0,fac_kingdom_2,
#   [itm_scythe,itm_hatchet,itm_stones,itm_leather_cap,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_wrapping_boots],
#   def_attrib|level(2),wp(60),knows_common,man_face_young_1, man_face_old_2],
  
#  ["southlander_1_recruit_east_central","Southlander Coalition Recruit (East Central)","Southlander Coalition Recruits (East Central)",tf_guarantee_armor,0,0,fac_kingdom_2,
#   [itm_scythe,itm_hatchet,itm_stones,itm_leather_cap,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_wrapping_boots],
#   def_attrib|level(2),wp(62),knows_common,man_face_young_1, man_face_old_2],
  
#  ["southlander_1_recruit_east","Southlander Coalition Recruit (East)","Southlander Coalition Recruits (East)",tf_guarantee_armor,0,0,fac_kingdom_2,
#   [itm_scythe,itm_hatchet,itm_stones,itm_leather_cap,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_wrapping_boots],
#   def_attrib|level(3),wp(65),knows_common,man_face_young_1, man_face_old_2],

## Mayene  
  ["mayene_recruit","Mayene Recruit","Mayene Recruits",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_4,
   [itm_sword_medieval_a, itm_mayene_recruit_tunic, itm_wrapping_boots],
   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1 ,mayene_man_face_young, mayene_man_face_older],
  
  ["mayene_militia","Mayene Militia","Mayene Militia",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_4,
   [itm_fighting_pick, itm_mayene_shield_weak, itm_mayene_recruit_tunic, itm_leather_boots, itm_leather_cap],
   def_attrib_wot_infantry_2 ,wp_one_handed(90)|wp(70),knows_wot_infantry_2 ,mayene_man_face_young, mayene_man_face_older],
  
  ["mayene_man_at_arms","Mayene Man at Arms","Mayene Man at Arms",tf_guarantee_all_cavalry,0,0,fac_kingdom_4,
   [itm_mayene_sword, itm_mayene_shield_weak, itm_mayene_army_armor, itm_leather_boots, itm_leather_gloves, itm_kettle_hat_wot, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_polearm(120)|wp_one_handed(120)|wp(85),knows_wot_cavalry_2 ,mayene_man_face_young, mayene_man_face_older],
  
  ["mayene_lancer","Mayene Lancer","Mayene Lancers",tf_guarantee_all_cavalry,0,0,fac_kingdom_4,
   [itm_lance, itm_sword_medieval_c_long, itm_mayene_shield_normal, itm_mayene_army_armor, itm_leather_boots, itm_leather_gloves, itm_kettle_hat_wot, itm_courser, itm_hunter],
   def_attrib_wot_cavalry_3 ,wp_polearm(150)|wp_one_handed(120)|wp(85),knows_wot_cavalry_3 ,mayene_man_face_young, mayene_man_face_older],

## Cairhien  
  ["cairhien_recruit","Cairhien Recruit","Cairhien Recruits",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_5,
   [itm_cudgel, itm_cairhien_recruit_tunic, itm_wrapping_boots, itm_woolen_cap],
   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1 ,cairhien_man_face_young, cairhien_man_face_older],
  
  ["cairhien_militia","Cairhien Militia","Cairhien Militia",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_5,
   [itm_sword_medieval_b, itm_cairhien_shield_weak, itm_cairhien_recruit_tunic, itm_leather_boots, itm_leather_cap],
   def_attrib_wot_infantry_2 ,wp_one_handed(90)|wp(70),knows_wot_infantry_2 ,cairhien_man_face_young, cairhien_man_face_older],
  
  ["cairhien_pikeman","Cairhien Pikeman","Cairhien Pikemen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_5,
   [itm_pike, itm_cairhien_army_armor ,itm_cairhien_shield_normal, itm_leather_boots, itm_leather_gloves, itm_bascinet],
   def_attrib_wot_infantry_3 ,wp_polearm(120)|wp(80),knows_wot_infantry_3 ,cairhien_man_face_young, cairhien_man_face_older],
  
  ["cairhien_man_at_arms","Cairhien Man at Arms","Cairhien Man at Arms",tf_guarantee_all_cavalry,0,0,fac_kingdom_5,
   [itm_fighting_axe, itm_cairhien_shield_normal, itm_cairhien_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_bascinet, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_one_handed(120)|wp(85),knows_wot_cavalry_2 ,cairhien_man_face_young, cairhien_man_face_older],
  
#  ["southlander_1_recruit_central","Southlander Coalition Recruit (Central)","Southlander Coalition Recruits (Central)",tf_guarantee_armor,0,0,fac_kingdom_2,
#   [itm_scythe,itm_hatchet,itm_stones,itm_leather_cap,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_wrapping_boots],
#   def_attrib|level(3),wp(65),knows_common,man_face_young_1, man_face_old_2],

## Illian  
  ["illian_recruit","Illian Recruit","Illian Recruits",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_6,
   [itm_illian_seax, itm_illian_recruit_tunic, itm_wrapping_boots],
   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1, illian_man_face_young, illian_man_face_older],
  
  ["illian_militia","Illian Militia","Illian Militia",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_6,
   [itm_illian_seax, itm_illian_shield_weak, itm_illian_recruit_tunic, itm_leather_boots, itm_skullcap],
   def_attrib_wot_infantry_2 ,wp_one_handed(90)|wp(70),knows_wot_infantry_2, illian_man_face_young, illian_man_face_older],
  
  ["illian_swordsman","Illian Swordsman","Illian Swordsmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_6,
   [itm_sword_medieval_b, itm_illian_army_armor, itm_illian_shield_normal, itm_leather_boots, itm_leather_gloves, itm_khergit_war_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(120)|wp(80),knows_wot_infantry_3, illian_man_face_young, illian_man_face_older],
  
  ["illian_companion","Illian Companion","Illian Companions",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_6,
   [itm_military_cleaver_b, itm_illian_companion_surcoat, itm_illian_shield_strong, itm_mail_chausses, itm_leather_gloves, itm_bascinet_3],
   def_attrib_wot_infantry_4 ,wp_one_handed(145)|wp(100),knows_wot_infantry_4, illian_man_face_young, illian_man_face_older],
  
  ["illian_bowman","Illian Bowman","Illian Bowmen",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_short_bow, itm_arrows, itm_sword_secondary, itm_illian_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_skullcap],
   def_attrib_wot_infantry_2 ,wp_archery(90)|wp_one_handed(85)|wp(80),knows_wot_archer_2, illian_man_face_young, illian_man_face_older],
  
  ["illian_crossbowman","Illian Crossbowman","Illian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_crossbow, itm_bolts, itm_sword_secondary, itm_illian_army_armor, itm_leather_boots, itm_leather_gloves, itm_khergit_war_helmet],
   def_attrib_wot_infantry_3 ,wp_crossbow(110)|wp_one_handed(100)|wp(80),knows_wot_archer_3, illian_man_face_young, illian_man_face_older],
  
  ["illian_scout","Illian Scout","Illian Scouts",tf_guarantee_all_cavalry,0,0,fac_kingdom_6,
   [itm_war_spear, itm_sword_medieval_a, itm_illian_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_skullcap, itm_saddle_horse],
   def_attrib_wot_cavalry_1 ,wp_polearm(100)|wp_one_handed(95)|wp(70),knows_wot_cavalry_1, illian_man_face_young, illian_man_face_older],

## Murandy  
  ["murandy_recruit","Murandy Recruit","Murandy Recruits",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_7,
   [itm_spiked_club, itm_murandy_recruit_tunic, itm_wrapping_boots],
   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1, murandy_man_face_young, murandy_man_face_older],
  
  ["murandy_militia","Murandy Militia","Murandy Militia",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_7,
   [itm_fighting_pick, itm_murandy_shield_weak, itm_murandy_recruit_tunic, itm_leather_boots, itm_leather_warrior_cap],
   def_attrib_wot_infantry_2 ,wp_one_handed(90)|wp(70),knows_wot_infantry_2, murandy_man_face_young, murandy_man_face_older],
  
  ["murandy_maceman","Murandy Maceman","Murandy Macemen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_7,
   [itm_maul, itm_murandy_leather_armor, itm_leather_boots, itm_leather_gloves, itm_nordic_fighter_helmet],
   def_attrib_wot_infantry_3 ,wp_two_handed(120)|wp(80),knows_wot_infantry_3, murandy_man_face_young, murandy_man_face_older],
  
  ["murandy_bowman","Murandy Bowman","Murandy Bowmen",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_nomad_bow, itm_arrows, itm_sword_secondary, itm_murandy_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_leather_warrior_cap],
   def_attrib_wot_infantry_3 ,wp_archery(100)|wp_one_handed(90)|wp(80),knows_wot_archer_3, murandy_man_face_young, murandy_man_face_older],
  
  ["murandy_scout","Murandy Scout","Murandy Scouts",tf_guarantee_all_cavalry,0,0,fac_kingdom_7,
   [itm_hammer, itm_sword_medieval_a, itm_murandy_shield_weak, itm_murandy_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_leather_warrior_cap, itm_steppe_horse],
   def_attrib_wot_cavalry_1 ,wp_one_handed(100)|wp(70),knows_wot_cavalry_1, murandy_man_face_young, murandy_man_face_older],
  
  ["murandy_lancer","Murandy Lancer","Murandy Lancers",tf_guarantee_all_cavalry,0,0,fac_kingdom_7,
   [itm_lance, itm_sword_medieval_c_long, itm_murandy_shield_normal, itm_murandy_leather_armor, itm_leather_boots, itm_leather_gloves, itm_nordic_fighter_helmet, itm_courser, itm_hunter],
   def_attrib_wot_cavalry_2 ,wp_polearm(120)|wp_one_handed(110)|wp(85),knows_wot_cavalry_2 ,murandy_man_face_young, murandy_man_face_older],
  
#  ["southlander_1_recruit_west","Southlander Coalition Recruit (West)","Southlander Coalition Recruits (West)",tf_guarantee_armor,0,0,fac_kingdom_2,
#   [itm_scythe,itm_hatchet,itm_stones,itm_leather_cap,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_wrapping_boots],
#   def_attrib|level(3),wp(65),knows_common,man_face_young_1, man_face_old_2],

## Altara
  ["altara_recruit","Altara Recruit","Altara Recruits",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_8,
   [itm_cleaver, itm_altara_recruit_armor, itm_altara_green_boots],
   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1, altara_man_face_young, altara_man_face_older],
  
  ["altara_dueler","Altara Dueler","Altara Duelers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_8,
   [itm_dagger, itm_altara_recruit_armor, itm_altara_green_boots, itm_spiked_helmet],
   def_attrib_wot_infantry_2 ,wp_one_handed(90)|wp(70),knows_wot_infantry_2, altara_man_face_young, altara_man_face_older],
  
  ["altara_swordsman","Altara Swordsman","Altara Swordsmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_8,
   [itm_scimitar_b, itm_altara_shield_normal, itm_altara_army_armor, itm_altara_green_boots, itm_leather_gloves, itm_vaegir_spiked_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(120)|wp(80),knows_wot_infantry_3, altara_man_face_young, altara_man_face_older],
  
  ["altara_scout","Altara Scout","Altara Scouts",tf_guarantee_all_cavalry,0,0,fac_kingdom_8,
   [itm_war_spear, itm_sword_medieval_a, itm_altara_shield_weak, itm_altara_recruit_armor, itm_altara_green_boots, itm_leather_gloves, itm_spiked_helmet, itm_saddle_horse],
   def_attrib_wot_cavalry_1 ,wp_polearm(100)|wp_one_handed(95)|wp(70),knows_wot_cavalry_1, altara_man_face_young, altara_man_face_older],

## Arad Doman  
  ["arad_doman_recruit","Arad Doman Recruit","Arad Doman Recruits",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_9,
   [itm_sword_viking_2_small, itm_arad_doman_recruit_tunic, itm_wrapping_boots],
   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1, arad_doman_man_face_young, arad_doman_man_face_older],
  
  ["arad_doman_rabble","Arad Doman Rabble","Arad Doman Rabble",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_9,
   [itm_butchering_knife, itm_pitch_fork, itm_boar_spear, itm_pelt_coat, itm_sarranid_cloth_robe, itm_linen_tunic, itm_wrapping_boots, itm_steppe_cap],
   def_attrib_wot_infantry_2 ,wp_one_handed(90)|wp(70),knows_wot_infantry_2,arad_doman_man_face_young, arad_doman_man_face_older],
  
  ["arad_doman_swordsman","Arad Doman Swordsman","Arad Doman Swordsmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_9,
   [itm_sword_viking_3, itm_arad_doman_shield_normal, itm_arad_doman_army_armor, itm_light_leather_boots, itm_leather_gloves, itm_nordic_archer_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(120)|wp(80),knows_wot_infantry_3, arad_doman_man_face_young, arad_doman_man_face_older],
  
  ["arad_doman_scout","Arad Doman Scout","Arad Doman Scouts",tf_guarantee_all_cavalry,0,0,fac_kingdom_9,
   [itm_war_spear, itm_sword_medieval_a, itm_arad_doman_shield_weak, itm_arad_doman_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_steppe_cap, itm_saddle_horse],
   def_attrib_wot_cavalry_1 ,wp_polearm(100)|wp_one_handed(95)|wp(70),knows_wot_cavalry_1, arad_doman_man_face_young, arad_doman_man_face_older],


# Southlander Alliance (2)

#  ["southlander_2_recruit","Southlander Alliance Recruit","Southlander Alliance Recruits",tf_guarantee_armor,0,0,fac_kingdom_3,
#   [itm_scythe,itm_hatchet,itm_stones,itm_leather_cap,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_wrapping_boots],
#   def_attrib|level(2),wp(60),knows_common,man_face_young_1, man_face_old_2],
  
#  ["southlander_2_recruit_east_central","Southlander Alliance Recruit (East Central)","Southlander Alliance Recruits (East Central)",tf_guarantee_armor,0,0,fac_kingdom_3,
#   [itm_scythe,itm_hatchet,itm_stones,itm_leather_cap,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_wrapping_boots],
#   def_attrib|level(2),wp(62),knows_common,man_face_young_1, man_face_old_2],
  
#  ["southlander_2_recruit_east","Southlander Alliance Recruit (East)","Southlander Alliance Recruits (East)",tf_guarantee_armor,0,0,fac_kingdom_3,
#   [itm_scythe,itm_hatchet,itm_stones,itm_leather_cap,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_wrapping_boots],
#   def_attrib|level(3),wp(65),knows_common,man_face_young_1, man_face_old_2],

## Tear  
  ["tear_recruit","Tear Recruit","Tear Recruits",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_10,
   [itm_hand_axe, itm_tear_recruit_tunic, itm_wrapping_boots],
   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1, tear_man_face_young, tear_man_face_older],
  
  ["tear_town_watch","Tear Town Watch","Tear Town Watch",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_10,
   [itm_street_patrol_club, itm_tear_recruit_tunic, itm_arming_cap, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_1 ,wp_one_handed(100)|wp(70),knows_wot_infantry_1 ,tear_man_face_young, tear_man_face_old],
  
  ["tear_swordsman","Tear Swordsman","Tear Swordsmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_10,
   [itm_sword_medieval_c_long, itm_tear_shield_normal, itm_tear_plate, itm_splinted_greaves_nospurs_wot, itm_leather_gloves, itm_tear_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(120)|wp(80),knows_wot_infantry_3, tear_man_face_young, tear_man_face_old],
  
  ["tear_defender","Tear Defender","Tear Defenders",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_10,
   [itm_war_spear, itm_tear_defender_armor, itm_black_leather_boots, itm_tear_defender_gauntlets, itm_tear_defender_helmet],
   def_attrib_wot_infantry_4 ,wp_polearm(135)|wp(90),knows_wot_infantry_4, tear_man_face_young, tear_man_face_old],
  
  ["tear_bowman","Tear Bowman","Tear Bowmen",tf_guarantee_all,0,0,fac_kingdom_10,
   [itm_strong_bow, itm_arrows, itm_sword_secondary, itm_tear_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_arming_cap],
   def_attrib_wot_infantry_3 ,wp_archery(100)|wp_one_handed(90)|wp(80),knows_wot_archer_3, tear_man_face_young, tear_man_face_old],
  
  ["tear_scout","Tear Scout","Tear Scouts",tf_guarantee_all_cavalry,0,0,fac_kingdom_10,
   [itm_war_spear, itm_sword_medieval_a, itm_tear_shield_weak, itm_tear_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_arming_cap, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_polearm(110)|wp_one_handed(100)|wp(75),knows_wot_cavalry_2, tear_man_face_young, tear_man_face_old],
  
  ["tear_lancer","Tear Lancer","Tear Lancers",tf_guarantee_all_cavalry,0,0,fac_kingdom_10,
   [itm_lance, itm_sword_medieval_c_long, itm_tear_shield_normal, itm_tear_plate, itm_splinted_greaves_spurs_wot, itm_leather_gloves, itm_tear_helmet, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_3 ,wp_polearm(135)|wp_one_handed(110)|wp(85),knows_wot_cavalry_3 ,tear_man_face_young, tear_man_face_old],

## Andor  
  ["andor_recruit","Andor Recruit","Andor Recruits",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_11,
   [itm_club, itm_andor_recruit_tunic, itm_wrapping_boots],
   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1, andor_man_face_young, andor_man_face_older],
  
  ["andor_militia","Andor Militia","Andor Militia",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_11,
   [itm_falchion, itm_andor_shield_weak, itm_andor_recruit_tunic, itm_skullcap, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2 ,wp_one_handed(100)|wp(70),knows_wot_infantry_2 ,andor_man_face_young, andor_man_face_older],
  
  ["andor_swordsman","Andor Swordsman","Andor Swordsmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_11,
   [itm_sword_viking_3, itm_andor_shield_normal, itm_andor_army_armor, itm_leather_boots, itm_leather_gloves, itm_nordic_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(120)|wp(80),knows_wot_infantry_3, andor_man_face_young, andor_man_face_older],
  
  ["andor_bowman","Andor Bowman","Andor Bowmen",tf_guarantee_all,0,0,fac_kingdom_11,
   [itm_strong_bow, itm_arrows, itm_sword_secondary, itm_andor_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_skullcap],
   def_attrib_wot_infantry_3 ,wp_archery(100)|wp_one_handed(90)|wp(80),knows_wot_archer_3, andor_man_face_young, andor_man_face_older],
  
  ["andor_scout","Andor Scout","Andor Scouts",tf_guarantee_all_cavalry,0,0,fac_kingdom_11,
   [itm_sword_medieval_a, itm_andor_shield_weak, itm_andor_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_skullcap, itm_saddle_horse],
   def_attrib_wot_cavalry_2 ,wp_one_handed(105)|wp(75),knows_wot_cavalry_2, andor_man_face_young, andor_man_face_older],
  
  ["andor_lancer","Andor Lancer","Andor Lancers",tf_guarantee_all_cavalry,0,0,fac_kingdom_11,
   [itm_lance, itm_sword_medieval_c_long, itm_andor_shield_normal, itm_andor_plate, itm_steel_greaves_wot, itm_leather_gloves, itm_andoran_helmet, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_polearm(135)|wp_one_handed(110)|wp(85),knows_wot_cavalry_3 ,andor_man_face_young, andor_man_face_older],
  
  ["andor_queens_guard","Andor Queen's Guard","Andor Queen's Guards",tf_guarantee_all_cavalry,0,0,fac_kingdom_11,
   [itm_lance, itm_sword_medieval_c_long, itm_andor_shield_strong, itm_andor_queens_guard_armor, itm_steel_greaves_wot, itm_wisby_gauntlets_red_wot, itm_andoran_helmet, itm_courser, itm_hunter],
   def_attrib_wot_cavalry_4 ,wp_polearm(150)|wp_one_handed(120)|wp(85),knows_wot_cavalry_4 ,andor_man_face_young, andor_man_face_older],
  #
#  ["southlander_2_recruit_central","Southlander Alliance Recruit (Central)","Southlander Alliance Recruits (Central)",tf_guarantee_armor,0,0,fac_kingdom_3,
#   [itm_scythe,itm_hatchet,itm_stones,itm_leather_cap,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_wrapping_boots],
#   def_attrib|level(3),wp(65),knows_common,man_face_young_1, man_face_old_2],

## Ghealdan  
  ["ghealdan_recruit","Ghealdan Recruit","Ghealdan Recruits",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_12,
   [itm_hatchet, itm_ghealdan_recruit_tunic, itm_wrapping_boots],
   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1, ghealdan_man_face_young, ghealdan_man_face_older],
  
  ["ghealdan_militia","Ghealdan Militia","Ghealdan Militia",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_12,
   [itm_one_handed_battle_axe_a, itm_ghealdan_shield_weak, itm_ghealdan_recruit_tunic, itm_footman_helmet, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2 ,wp_one_handed(100)|wp(70),knows_wot_infantry_2 ,ghealdan_man_face_young, ghealdan_man_face_older],
  
  ["ghealdan_axeman","Ghealdan Axeman","Ghealdan Axemen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_12,
   [itm_one_handed_battle_axe_b, itm_ghealdan_shield_normal, itm_ghealdan_army_armor, itm_leather_boots, itm_leather_gloves, itm_guard_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(120)|wp(80),knows_wot_infantry_3, ghealdan_man_face_young, ghealdan_man_face_older],
  
  ["ghealdan_bowman","Ghealdan Bowman","Ghealdan Bowmen",tf_guarantee_all,0,0,fac_kingdom_12,
   [itm_strong_bow, itm_arrows, itm_sword_secondary, itm_ghealdan_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_footman_helmet],
   def_attrib_wot_infantry_2 ,wp_archery(100)|wp_one_handed(90)|wp(80),knows_wot_archer_2, ghealdan_man_face_young, ghealdan_man_face_older],
  
  ["ghealdan_scout","Ghealdan Scout","Ghealdan Scouts",tf_guarantee_all_cavalry,0,0,fac_kingdom_12,
   [itm_one_handed_battle_axe_a, itm_ghealdan_shield_weak, itm_ghealdan_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_footman_helmet, itm_saddle_horse],
   def_attrib_wot_cavalry_2 ,wp_one_handed(105)|wp(75),knows_wot_cavalry_2, ghealdan_man_face_young, ghealdan_man_face_older],
  
  ["ghealdan_lancer","Ghealdan Lancer","Ghealdan Lancers",tf_guarantee_all_cavalry,0,0,fac_kingdom_12,
   [itm_lance, itm_sword_medieval_c_long, itm_ghealdan_shield_normal, itm_ghealdan_army_armor, itm_steel_greaves_wot, itm_leather_gloves, itm_guard_helmet, itm_courser, itm_hunter],
   def_attrib_wot_cavalry_3 ,wp_polearm(135)|wp_one_handed(110)|wp(85),knows_wot_cavalry_3 , ghealdan_man_face_young, ghealdan_man_face_older],

## Far Madding  
  ["far_madding_recruit","Far Madding Recruit","Far Madding Recruits",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_13,
   [itm_spear, itm_far_madding_recruit_tunic, itm_wrapping_boots],
   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1, far_madding_man_face_young, far_madding_man_face_older],
  
  ["far_madding_footman","Far Madding Street Guard","Far Madding Street Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_13,
   [itm_street_patrol_club, itm_far_madding_shield_weak, itm_far_madding_recruit_tunic, itm_leather_warrior_cap, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2 ,wp_one_handed(100)|wp(70),knows_wot_infantry_2 ,far_madding_man_face_young, far_madding_man_face_older],
  #
#  ["southlander_2_recruit_west","Southlander Alliance Recruit (West)","Southlander Alliance Recruits (West)",tf_guarantee_armor,0,0,fac_kingdom_3,
#   [itm_scythe,itm_hatchet,itm_stones,itm_leather_cap,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_wrapping_boots],
#   def_attrib|level(3),wp(65),knows_common,man_face_young_1, man_face_old_2],

## Tarabon  
  ["tarabon_recruit","Tarabon Recruit","Tarabon Recruits",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_14,
   [itm_staff, itm_tarabon_recruit_tunic, itm_nomad_boots],
   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1, tarabon_man_face_young, tarabon_man_face_older],
  
  ["tarabon_rabble","Tarabon Rabble","Tarabon Rabble",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_14,
   [itm_butchering_knife, itm_pitch_fork, itm_boar_spear, itm_pelt_coat, itm_sarranid_cloth_robe_b, itm_linen_tunic, itm_nomad_boots, itm_nomad_cap],
   def_attrib_wot_infantry_2 ,wp_polearm(90)|wp(70),knows_wot_infantry_2,tarabon_man_face_young, tarabon_man_face_older],
  
  ["tarabon_bowman","Tarabon Bowman","Tarabon Bowmen",tf_guarantee_all,0,0,fac_kingdom_14,
   [itm_strong_bow, itm_arrows, itm_sword_secondary, itm_tarabon_recruit_tunic, itm_nomad_boots, itm_leather_gloves, itm_sarranid_helmet1],
   def_attrib_wot_infantry_2 ,wp_archery(100)|wp_one_handed(90)|wp(80),knows_wot_archer_2, tarabon_man_face_young, tarabon_man_face_older],
  
  ["tarabon_scout","Tarabon Scout","Tarabon Scouts",tf_guarantee_all_cavalry,0,0,fac_kingdom_14,
   [itm_military_fork, itm_one_handed_battle_axe_a, itm_tarabon_shield_weak, itm_tarabon_recruit_tunic, itm_nomad_boots, itm_leather_gloves, itm_sarranid_helmet1, itm_saddle_horse],
   def_attrib_wot_cavalry_2 ,wp_polearm(105)|wp(75),knows_wot_cavalry_2, tarabon_man_face_young, tarabon_man_face_older],

## Amadicia  
  ["amadicia_recruit","Amadicia Recruit","Amadicia Recruits",tf_guarantee_all,0,0,fac_kingdom_15,
   [itm_spear, itm_amadicia_recruit_tunic, itm_wrapping_boots],
   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1, amadicia_man_face_young, amadicia_man_face_older],
  
  ["amadicia_militia","Amadicia Militia","Amadicia Militia",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_15,
   [itm_spear, itm_amadicia_shield_weak, itm_amadicia_recruit_tunic, itm_black_hood, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2 ,wp_polearm(100)|wp(70),knows_wot_infantry_2 ,amadicia_man_face_young, amadicia_man_face_older],
  
  ["amadicia_pikeman","Amadicia Pikeman","Amadicia Pikemen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_15,
   [itm_pike, itm_amadicia_army_armor ,itm_amadicia_shield_normal, itm_leather_boots, itm_leather_gloves, itm_segmented_helmet],
   def_attrib_wot_infantry_3 ,wp_polearm(120)|wp(80),knows_wot_infantry_3 ,amadicia_man_face_young, amadicia_man_face_older],
  
  ["amadicia_bowman","Amadicia Bowman","Amadicia Bowmen",tf_guarantee_all,0,0,fac_kingdom_15,
   [itm_short_bow, itm_arrows, itm_sword_secondary, itm_amadicia_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_black_hood],
   def_attrib_wot_infantry_2 ,wp_archery(100)|wp_one_handed(90)|wp(80),knows_wot_archer_2, amadicia_man_face_young, amadicia_man_face_older],

## Children of the Light  
  ["whitecloak_recruit","Whitecloak Recruit","Whitecloak Recruits",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_16,
   [itm_sword_medieval_a, itm_whitecloak_recruit_tunic, itm_segmented_helmet, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2 ,wp_one_handed(100)|wp(70),knows_wot_infantry_2 ,man_face_young_1, man_face_old_2],
  
  ["whitecloak_footman","Whitecloak Footman","Whitecloak Footmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_16,
   [itm_sword_medieval_b, itm_whitecloak_shield_weak, itm_whitecloak_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_segmented_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(120)|wp(80),knows_wot_infantry_3, man_face_young_1, man_face_old_2],
  
  ["whitecloak_swordsman","Whitecloak Swordsman","Whitecloak Swordsmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_16,
   [itm_sword_medieval_c_long, itm_whitecloak_shield_normal, itm_whitecloak_questioner_tabbard, itm_mail_chausses, itm_mail_mittens, itm_guard_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(135)|wp(100),knows_wot_infantry_3, man_face_young_1, man_face_old_2],
  
  ["whitecloak_bowman","Whitecloak Bowman","Whitecloak Bowmen",tf_guarantee_all,0,0,fac_kingdom_16,
   [itm_short_bow, itm_arrows, itm_sword_secondary, itm_whitecloak_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_segmented_helmet],
   def_attrib_wot_infantry_2 ,wp_archery(100)|wp_one_handed(90)|wp(80),knows_wot_archer_2, man_face_young_1, man_face_old_2],
  
  ["whitecloak_man_at_arms","Whitecloak Man at Arms","Whitecloak Man at Arms",tf_guarantee_all_cavalry,0,0,fac_kingdom_16,
   [itm_sword_medieval_c_long, itm_whitecloak_shield_normal, itm_whitecloak_questioner_tabbard, itm_mail_chausses, itm_mail_mittens, itm_guard_helmet, itm_courser, itm_hunter],
   def_attrib_wot_cavalry_3 ,wp_one_handed(140)|wp(100),knows_wot_cavalry_3 ,man_face_young_1, man_face_old_2],


# Borderlands
  
#  ["borderland_recruit","Borderland Recruit","Borderland Recruits",tf_guarantee_armor,0,0,fac_kingdom_4,
#   [itm_scythe,itm_hatchet,itm_stones,itm_leather_cap,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_wrapping_boots],
#   def_attrib|level(3),wp(65),knows_common,man_face_young_1, man_face_old_2],
  
#  ["borderland_recruit_east","Borderland Recruit (East)","Borderland Recruits (East)",tf_guarantee_armor,0,0,fac_kingdom_4,
#   [itm_scythe,itm_hatchet,itm_stones,itm_leather_cap,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_wrapping_boots],
#   def_attrib|level(4),wp(70),knows_common,man_face_young_1, man_face_old_2],
  
## Shienar
  ["shienar_recruit","Shienar Recruit","Shienar Recruits",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_17,
   [itm_hand_axe, itm_shienar_recruit_tunic, itm_leather_boots, itm_nordic_archer_helmet],
   def_attrib_wot_infantry_1 ,wp(75),knows_wot_infantry_1, shienar_man_face_young, shienar_man_face_older],
  
  ["shienar_militia","Shienar Militia","Shienar Militia",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_17,
   [itm_sword_medieval_b, itm_shienar_shield_weak, itm_shienar_leather_armor, itm_skullcap, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2 ,wp_one_handed(100)|wp(70),knows_wot_infantry_2 ,shienar_man_face_young, shienar_man_face_older],
  
  ["shienar_spearman","Shienar Spearman","Shienar Spearmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_17,
   [itm_war_spear, itm_shienar_shield_normal, itm_mail_shirt, itm_mail_chausses, itm_leather_gloves, itm_nordic_fighter_helmet],
   def_attrib_wot_infantry_3 ,wp_polearm(125)|wp(100),knows_wot_infantry_3, shienar_man_face_young, shienar_man_face_older],
  
  ["shienar_swordsman","Shienar Swordsman","Shienar Swordsmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_17,
   [itm_sword_medieval_d_long, itm_shienar_shield_strong, itm_banded_armor, itm_mail_chausses, itm_gauntlets, itm_nordic_warlord_helmet],
   def_attrib_wot_infantry_4 ,wp_one_handed(155)|wp(100),knows_wot_infantry_4, shienar_man_face_young, shienar_man_face_older],
  
  ["shienar_bowman","Shienar Bowman","Shienar Bowmen",tf_guarantee_all,0,0,fac_kingdom_17,
   [itm_strong_bow, itm_arrows, itm_sword_secondary, itm_shienar_leather_armor, itm_leather_boots, itm_leather_gloves, itm_skullcap],
   def_attrib_wot_infantry_3 ,wp_archery(130)|wp_one_handed(120)|wp(80),knows_wot_archer_3, shienar_man_face_young, shienar_man_face_older],
  
  ["shienar_light_cavalry","Shienar Light Cavalry","Shienar Light Cavalry",tf_guarantee_all_cavalry,0,0,fac_kingdom_17,
   [itm_sword_medieval_b, itm_shienar_shield_weak, itm_shienar_leather_armor, itm_leather_boots, itm_leather_gloves, itm_skullcap, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_one_handed(105)|wp(75),knows_wot_cavalry_2, shienar_man_face_young, shienar_man_face_older],
  
  ["shienar_lancer","Shienar Lancer","Shienar Lancers",tf_guarantee_all_cavalry,0,0,fac_kingdom_17,
   [itm_lance, itm_sword_medieval_c_long, itm_shienar_shield_normal, itm_banded_armor, itm_steel_greaves_wot, itm_gauntlets, itm_nordic_warlord_helmet, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_3 ,wp_polearm(135)|wp_one_handed(110)|wp(85),knows_wot_cavalry_3 , shienar_man_face_young, shienar_man_face_older],
  
  ["shienar_heavy_lancer","Shienar Heavy Lancer","Shienar Heavy Lancers",tf_guarantee_all_cavalry,0,0,fac_kingdom_17,
   [itm_heavy_lance, itm_sword_medieval_c_long, itm_shienar_shield_strong, itm_plate_armor, itm_steel_greaves_wot, itm_gauntlets, itm_great_helmet, itm_warhorse, itm_charger],
   def_attrib_wot_cavalry_4 ,wp_polearm(175)|wp_one_handed(150)|wp(85),knows_wot_cavalry_4 , shienar_man_face_young, shienar_man_face_older],

## Arafel  
  ["arafel_recruit","Arafel Recruit","Arafel Recruits",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_18,
   [itm_mace_1, itm_arafel_recruit_tunic, itm_leather_boots, itm_footman_helmet],
   def_attrib_wot_infantry_1 ,wp(75),knows_wot_infantry_1, arafel_man_face_young, arafel_man_face_older],
  
  ["arafel_militia","Arafel Militia","Arafel Militia",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_18,
   [itm_mace_2, itm_arafel_shield_weak, itm_arafel_army_armor, itm_mail_coif, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2 ,wp_one_handed(100)|wp(70),knows_wot_infantry_2 ,arafel_man_face_young, arafel_man_face_older],
  
  ["arafel_swordsman","Arafel Swordsman","Arafel Swordsmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_18,
   [itm_sword_viking_3, itm_arafel_shield_normal, itm_arafel_tabbard, itm_splinted_greaves_nospurs_wot, itm_mail_mittens, itm_guard_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(120)|wp(100),knows_wot_infantry_3, arafel_man_face_young, arafel_man_face_older],
  
  ["arafel_halberdier","Arafel Halberdier","Arafel Halberdiers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_18,
   [itm_halberd, itm_arafel_tabbard, itm_splinted_greaves_nospurs_wot, itm_mail_mittens, itm_guard_helmet],
   def_attrib_wot_infantry_4 ,wp_polearm(150)|wp(100),knows_wot_infantry_4, arafel_man_face_young, arafel_man_face_older],
  
  ["arafel_bowman","Arafel Bowman","Arafel Bowmen",tf_guarantee_all,0,0,fac_kingdom_18,
   [itm_strong_bow, itm_arrows, itm_sword_secondary, itm_arafel_army_armor, itm_mail_coif, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_3 ,wp_archery(130)|wp_one_handed(115)|wp(80),knows_wot_archer_3, arafel_man_face_young, arafel_man_face_older],
  
  ["arafel_man_at_arms","Arafel Man at Arms","Arafel Man at Arms",tf_guarantee_all_cavalry,0,0,fac_kingdom_18,
   [itm_mace_3, itm_arafel_shield_normal, itm_mamluke_mail, itm_mail_chausses, itm_leather_gloves, itm_segmented_helmet, itm_hunter],
   def_attrib_wot_cavalry_2 ,wp_one_handed(105)|wp(75),knows_wot_cavalry_2, arafel_man_face_young, arafel_man_face_older],
  #
#  ["borderland_recruit_west","Borderland Recruit (West)","Borderland Recruits (West)",tf_guarantee_armor,0,0,fac_kingdom_4,
#   [itm_scythe,itm_hatchet,itm_stones,itm_leather_cap,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_wrapping_boots],
#   def_attrib|level(4),wp(70),knows_common,man_face_young_1, man_face_old_2],

## Kandor  
  ["kandor_recruit","Kandor Recruit","Kandor Recruits",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_19,
   [itm_fighting_axe, itm_kandor_shield_weak, itm_kandor_recruit_tunic, itm_hide_boots, itm_vaegir_fur_cap],
   def_attrib_wot_infantry_1 ,wp(75),knows_wot_infantry_1, kandor_man_face_young, kandor_man_face_older],
  
  ["kandor_militia","Kandor Militia","Kandor Militia",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_19,
   [itm_one_handed_war_axe_b, itm_kandor_shield_normal, itm_kandor_leather_armor, itm_vaegir_fur_helmet, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2 ,wp_one_handed(100)|wp(70),knows_wot_infantry_2 ,kandor_man_face_young, kandor_man_face_older],
  
  ["kandor_axeman","Kandor Axeman","Kandor Axemen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_19,
   [itm_one_handed_battle_axe_c, itm_kandor_shield_strong, itm_kandor_surcoat, itm_mail_chausses, itm_mail_mittens, itm_vaegir_lamellar_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(120)|wp(100),knows_wot_infantry_3, kandor_man_face_young, kandor_man_face_older],
  
  ["kandor_berserker","Kandor Berserker","Kandor Berserkers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_19,
   [itm_long_axe_b, itm_coat_of_plates, itm_plate_boots, itm_gauntlets, itm_visored_sallet],
   def_attrib_wot_infantry_4 ,wp_two_handed(150)|wp(100),knows_wot_infantry_4, kandor_man_face_young, kandor_man_face_older],
  
  ["kandor_bowman","Kandor Bowman","Kandor Bowmen",tf_guarantee_all,0,0,fac_kingdom_19,
   [itm_nomad_bow, itm_arrows, itm_sword_secondary, itm_kandor_leather_armor, itm_vaegir_fur_helmet, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_3 ,wp_archery(130)|wp_one_handed(125)|wp(80),knows_wot_archer_3, kandor_man_face_young, kandor_man_face_older],
  
  ["kandor_man_at_arms","Kandor Man at Arms","Kandor Man at Arms",tf_guarantee_all_cavalry,0,0,fac_kingdom_19,
   [itm_one_handed_battle_axe_b, itm_kandor_shield_normal, itm_kandor_army_armor, itm_splinted_leather_greaves, itm_leather_gloves, itm_vaegir_spiked_helmet, itm_hunter],
   def_attrib_wot_cavalry_2 ,wp_one_handed(105)|wp(75),knows_wot_cavalry_2, kandor_man_face_young, kandor_man_face_older],

## Saldaea  
  ["saldaea_recruit","Saldaea Recruit","Saldaea Recruits",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_20,
   [itm_sword_khergit_1, itm_saldaea_recruit_tunic, itm_hide_boots, itm_leather_steppe_cap_b],
   def_attrib_wot_infantry_1 ,wp(75),knows_wot_infantry_1, saldaea_man_face_young, saldaea_man_face_older],
  
  ["saldaea_militia","Saldaea Militia","Saldaea Militia",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_20,
   [itm_sword_khergit_2, itm_saldaea_shield_normal, itm_saldaea_warrior_outfit, itm_nomad_cap_b, itm_hunter_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2 ,wp_one_handed(100)|wp(70),knows_wot_infantry_2 ,saldaea_man_face_young, saldaea_man_face_older],
  
  ["saldaea_swordsman","Saldaea Swordsman","Saldaea Swordsmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_20,
   [itm_sword_khergit_3, itm_saldaea_shield_strong, itm_saldaea_army_armor, itm_leather_boots, itm_leather_gloves, itm_leather_steppe_cap_c],
   def_attrib_wot_infantry_3 ,wp_one_handed(120)|wp(100),knows_wot_infantry_3, saldaea_man_face_young, saldaea_man_face_older],
  
  ["saldaea_bowman","Saldaea Bowman","Saldaea Bowmen",tf_guarantee_all,0,0,fac_kingdom_20,
   [itm_nomad_bow, itm_arrows, itm_sword_secondary, itm_saldaea_warrior_outfit, itm_nomad_cap_b, itm_hunter_boots, itm_leather_gloves],
   def_attrib_wot_infantry_3 ,wp_archery(130)|wp_one_handed(120)|wp(80),knows_wot_archer_3, saldaea_man_face_young, saldaea_man_face_older],
  
  ["saldaea_cavalry","Saldaea Cavalry","Saldaea Cavalry",tf_guarantee_all_cavalry,0,0,fac_kingdom_20,
   [itm_sword_khergit_1, itm_saldaea_shield_weak, itm_saldaea_warrior_outfit, itm_nomad_cap_b, itm_hunter_boots, itm_leather_gloves, itm_steppe_horse],
   def_attrib_wot_cavalry_2 ,wp_one_handed(105)|wp(75),knows_wot_cavalry_2, saldaea_man_face_young, saldaea_man_face_older],
  
  ["saldaea_light_cavalry","Saldaea Light Cavalry","Saldaea Light Cavalry",tf_guarantee_all_cavalry,0,0,fac_kingdom_20,
   [itm_sword_khergit_2, itm_saldaea_shield_normal, itm_khergit_elite_armor, itm_khergit_war_helmet, itm_khergit_leather_boots, itm_scale_gauntlets, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_one_handed(130)|wp(100),knows_wot_cavalry_3, saldaea_man_face_young, saldaea_man_face_older],
  
  ["saldaea_elite_light_cavalry","Saldaea Elite Light Cavalry","Saldaea Elite Light Cavalry",tf_guarantee_all_cavalry,0,0,fac_kingdom_20,
   [itm_sword_khergit_3, itm_saldaea_shield_strong, itm_heavy_lamellar_armor_wot, itm_khergit_cavalry_helmet, itm_splinted_greaves, itm_lamellar_gauntlets, itm_saldaea_warhorse],
   def_attrib_wot_cavalry_4 ,wp_one_handed(155)|wp(100),knows_wot_cavalry_4, saldaea_man_face_young, saldaea_man_face_older],
  
  ["saldaea_skirmisher","Saldaea Skirmisher","Saldaea Skirmishers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_20,
   [itm_khergit_bow, itm_arrows, itm_sword_secondary, itm_khergit_elite_armor, itm_khergit_war_helmet, itm_khergit_leather_boots, itm_scale_gauntlets, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_archery(165)|wp_one_handed(120)|wp(85),knows_wot_horse_archer_3 ,saldaea_man_face_young, saldaea_man_face_older],


# White Tower
  
#    ["sedai_recruit","Sedai Recruit","Sedai Recruits",tf_guarantee_armor,0,0,fac_kingdom_5,
#   [itm_hatchet,itm_pickaxe,itm_club,itm_stones,itm_tab_shield_heater_a,itm_leather_cap,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_nomad_boots,itm_wrapping_boots],
#   def_attrib|level(2),wp(60),knows_common,tar_valon_man_face_younger, tar_valon_man_face_old],
  
  ["sedai_recruit_channeler","Sedai Recruit (Channeler)","Sedai Recruits (Channeler)",tf_female|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo,itm_channeler_dagger,itm_woolen_dress,itm_wrapping_boots],
   def_attrib|level(3),wp_firearm(65)|wp(60),knows_common|knows_power_draw_1|knows_fire_1|knows_earth_1|knows_spirit_1|knows_water_3|knows_air_1,tar_valon_woman_face_younger, mayene_woman_face_middle],
  
  ["novice_social","Novice (Social)","Novices (Social)",tf_female|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_novice_dress, itm_novice_accepted_damane_shoes], # , itm_wig_brown_ponytail
   def_attrib|level(5),wp_firearm(100)|wp_one_handed(90)|wp(70),knows_common|knows_power_draw_2|knows_fire_4|knows_earth_1|knows_spirit_3|knows_water_4|knows_air_4,tar_valon_woman_face_younger, tear_woman_face_middle],
  
  ["accepted_medical","Accepted (Medical)","Accepted (Medical)",tf_female|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_accepted_dress, itm_novice_accepted_damane_shoes], # , itm_wig_blond_longer
   def_attrib|level(10),wp_firearm(120)|wp_one_handed(110)|wp(75),knows_common|knows_power_draw_3|knows_fire_4|knows_earth_2|knows_spirit_4|knows_water_5|knows_air_5,tar_valon_woman_face_younger, far_madding_woman_face_middle],
  
  ["aes_sedai_yellow","Aes Sedai Yellow","Aes Sedai Yellows",tf_female|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_yellow_dress, itm_aes_sedai_yellow_shoes], # , itm_wig_black_long
   def_attrib|level(15),wp_firearm(175)|wp_one_handed(110)|wp(80),knows_common|knows_power_draw_4|knows_fire_5|knows_earth_4|knows_spirit_5|knows_water_6|knows_air_6,tar_valon_woman_face_younger, illian_woman_face_middle],
  
  ["accepted_academic","Accepted (Academic)","Accepted (Academic)",tf_female|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_accepted_dress, itm_novice_accepted_damane_shoes], # , itm_wig_brown_longer
   def_attrib|level(10),wp_firearm(120)|wp_one_handed(110)|wp(75),knows_common|knows_power_draw_3|knows_fire_4|knows_earth_2|knows_spirit_4|knows_water_5|knows_air_5,tar_valon_woman_face_young, murandy_woman_face_middle],
  
  ["aes_sedai_brown","Aes Sedai Brown","Aes Sedai Browns",tf_female|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_brown_dress, itm_aes_sedai_brown_shoes], # , itm_wig_red_bun
   def_attrib|level(15),wp_firearm(175)|wp_one_handed(110)|wp(80),knows_common|knows_power_draw_4|knows_fire_5|knows_earth_4|knows_spirit_5|knows_water_6|knows_air_6,tar_valon_woman_face_young, altara_woman_face_old],
  
  ["aes_sedai_white","Aes Sedai White","Aes Sedai Whites",tf_female|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_white_dress, itm_aes_sedai_white_shoes], # , itm_wig_black_long
   def_attrib|level(15),wp_firearm(175)|wp_one_handed(110)|wp(80),knows_common|knows_power_draw_4|knows_fire_5|knows_earth_4|knows_spirit_5|knows_water_6|knows_air_6,tar_valon_woman_face_young, ghealdan_woman_face_old],
  
  ["novice_civil","Novice (Civil)","Novices (Civil)",tf_female|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_novice_dress, itm_novice_accepted_damane_shoes], # , itm_wig_blond_ponytail
   def_attrib|level(5),wp_firearm(100)|wp_one_handed(90)|wp(70),knows_common|knows_power_draw_2|knows_fire_4|knows_earth_1|knows_spirit_3|knows_water_4|knows_air_4,tar_valon_woman_face_younger, amadicia_woman_face_young],
  
  ["accepted_political","Accepted (Political)","Accepted (Political)",tf_female|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_accepted_dress, itm_novice_accepted_damane_shoes], # , itm_wig_brown_braid
   def_attrib|level(10),wp_firearm(120)|wp_one_handed(110)|wp(75),knows_common|knows_power_draw_3|knows_fire_4|knows_earth_2|knows_spirit_4|knows_water_5|knows_air_5,tar_valon_woman_face_young, tarabon_woman_face_middle],
  
  ["aes_sedai_blue","Aes Sedai Blue","Aes Sedai Blues",tf_female|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_blue_dress, itm_aes_sedai_blue_shoes], # , itm_wig_blond_braid
   def_attrib|level(15),wp_firearm(175)|wp_one_handed(110)|wp(80),knows_common|knows_power_draw_4|knows_fire_5|knows_earth_4|knows_spirit_5|knows_water_6|knows_air_6,tar_valon_woman_face_young, arad_doman_woman_face_old],
  
  ["aes_sedai_grey","Aes Sedai Grey","Aes Sedai Greys",tf_female|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_grey_dress, itm_aes_sedai_grey_shoes], # , itm_wig_red_braid
   def_attrib|level(15),wp_firearm(175)|wp_one_handed(110)|wp(80),knows_common|knows_power_draw_4|knows_fire_5|knows_earth_4|knows_spirit_5|knows_water_6|knows_air_6,tar_valon_woman_face_young, saldaea_woman_face_old],
  
  ["accepted_military","Accepted (Military)","Accepted (Military)",tf_female|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_accepted_dress, itm_novice_accepted_damane_shoes], # , itm_wig_red_braid
   def_attrib|level(10),wp_firearm(120)|wp_one_handed(110)|wp(75),knows_common|knows_power_draw_3|knows_fire_4|knows_earth_2|knows_spirit_4|knows_water_5|knows_air_5,tar_valon_woman_face_young, kandor_woman_face_middle],
  
  ["aes_sedai_red","Aes Sedai Red","Aes Sedai Reds",tf_female|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_red_dress, itm_aes_sedai_red_shoes], # , itm_wig_brown_bun
   def_attrib|level(15),wp_firearm(175)|wp_one_handed(110)|wp(80),knows_common|knows_power_draw_4|knows_fire_5|knows_earth_4|knows_spirit_6|knows_water_6|knows_air_6,tar_valon_woman_face_young, arafel_woman_face_old],
  
  ["aes_sedai_green","Aes Sedai Green","Aes Sedai Greens",tf_female|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_green_dress, itm_aes_sedai_green_shoes], # , itm_wig_red_long
   def_attrib|level(15),wp_firearm(175)|wp_one_handed(110)|wp(80),knows_common|knows_power_draw_4|knows_fire_5|knows_earth_6|knows_spirit_5|knows_water_6|knows_air_6,tar_valon_woman_face_young, shienar_woman_face_old],
  
  ["sedai_recruit_soldier","Sedai Recruit (Soldier)","Sedai Recruits (Soldier)",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_21,
   [itm_club,itm_staff,itm_padded_cloth,itm_leather_cap,itm_leather_boots],
   def_attrib|level(4),wp(60),knows_common,tar_valon_man_face_young, tar_valon_man_face_old],
  
  ["tar_valon_street_patrol","Tar Valon Street Patrol","Tar Valon Street Patrols",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_21,
   [itm_street_patrol_club, itm_white_tower_patrol_tunic, itm_norman_helmet, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_1 ,wp_one_handed(100)|wp(70),knows_wot_infantry_1 ,tar_valon_man_face_young, tar_valon_man_face_old],
  
  ["tower_guard_infantry","Tower Guard Infantry","Tower Guard Infantry",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_21,
   [itm_spiked_mace, itm_steel_buckler2, itm_white_tower_guard_armor, itm_segmented_helmet, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2,wp_one_handed(125)|wp(90),knows_wot_infantry_2,tar_valon_man_face_young, tar_valon_man_face_old],
  
  ["warder_trainee","Warder Trainee","Warder Trainees",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_21,
   [itm_sword_viking_2_small, itm_arena_tunic_white, itm_norman_helmet, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_1,wp_one_handed(100)|wp(70),knows_wot_infantry_1,tar_valon_man_face_young, tar_valon_man_face_old],


# Aiel Nation

#  ["aiel_recruit","Aiel Recruit","Aiel Recruits",tf_guarantee_armor,0,0,fac_kingdom_6,
#   [itm_aiel_knife, itm_shoufa_grey, itm_cadinsor_grey ,itm_cadinsor_boots_grey],
#   def_attrib|level(3),wp(70),knows_common, aiel_1_man_face_younger, aiel_2_man_face_old],
  
  ["aiel_recruit_channeler","Aiel Recruit (Channeler)","Aiel Recruits (Channeler)",tf_female|tf_guarantee_all,0,0,fac_kingdom_22,
   [itm_power_player, itm_power_ammo,itm_channeler_dagger, itm_wise_one_dress, itm_cadinsor_boots],
   def_attrib|level(5),wp_firearm(80)|wp(75),knows_common|knows_power_draw_2|knows_fire_1|knows_earth_1|knows_spirit_3|knows_water_4|knows_air_1, aiel_1_woman_face_younger, aiel_2_woman_face_middle],
  
  ["wise_one_apprentice","Wise One Apprentice","Wise One Apprentices",tf_female|tf_guarantee_all,0,0,fac_kingdom_22,
   [itm_power_player, itm_power_ammo, itm_wise_one_dress, itm_cadinsor_boots],
  def_attrib|level(10),wp_firearm(120)|wp_one_handed(110)|wp(75),knows_common|knows_power_draw_3|knows_fire_4|knows_earth_2|knows_spirit_4|knows_water_4|knows_air_2, aiel_1_woman_face_younger, aiel_2_woman_face_middle],
  
  ["wise_one","Wise One","Wise Ones",tf_female|tf_guarantee_all,0,0,fac_kingdom_22,
   [itm_power_player, itm_power_ammo, itm_wise_one_dress_with_shawl, itm_cadinsor_boots],
   def_attrib|level(16),wp_firearm(150)|wp_one_handed(110)|wp(80),knows_common|knows_power_draw_4|knows_fire_6|knows_earth_4|knows_spirit_6|knows_water_5|knows_air_5, aiel_1_woman_face_young, aiel_2_woman_face_old],
  
  ["aiel_recruit_soldier","Aiel Recruit (Soldier)","Aiel Recruits (Soldier)",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_22,
   [itm_aiel_spear, itm_cadinsor_grey, itm_shoufa_grey, itm_cadinsor_boots_grey],
   def_attrib|level(5),wp(80),knows_common, aiel_1_man_face_younger, aiel_2_man_face_old],
  
  ["aiel_recruit_lithe","Aiel Recruit (Lithe)","Aiel Recruits (Lithe)",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_22,
   [itm_aiel_spear, itm_hide_buckler_weak, itm_cadinsor_grey, itm_shoufa_grey, itm_cadinsor_boots_grey],
   def_attrib_wot_super_infantry_2 ,wp_polearm(110)|wp(70),knows_wot_super_infantry_2 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  
  ["aiel_raider","Aiel Raider","Aiel Raiders",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_22,
   [itm_aiel_spear, itm_hide_buckler_normal, itm_cadinsor_green, itm_shoufa_green, itm_cadinsor_boots_green],
   def_attrib_wot_super_infantry_3 ,wp_polearm(145)|wp(90),knows_wot_super_infantry_3 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  
  ["aiel_recruit_athletic","Aiel Recruit (Athletic)","Aiel Recruits (Athletic)",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_22,
   [itm_aiel_spear, itm_cadinsor_grey, itm_shoufa_grey, itm_cadinsor_boots_grey],
   def_attrib_wot_super_infantry_2 ,wp_polearm(115)|wp(70),knows_wot_super_infantry_2 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  
  ["aiel_runner","Aiel Runner","Aiel Runners",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_22,
   [itm_aiel_spear, itm_cadinsor_green, itm_shoufa_green, itm_cadinsor_boots_green],
   def_attrib_wot_super_infantry_3 ,wp_polearm(145)|wp(90),knows_wot_super_infantry_3 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  
  ["aiel_scout","Aiel Scout","Aiel Scouts",tf_guarantee_all,0,0,fac_kingdom_22,
   [itm_nomad_bow, itm_arrows, itm_aiel_spear, itm_cadinsor_green, itm_shoufa_green, itm_cadinsor_boots_green],
   def_attrib_wot_super_infantry_3 ,wp_archery(145)|wp_polearm(130)|wp(90),knows_wot_super_infantry_3 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  
  ["aiel_recruit_bulky","Aiel Recruit (Bulky)","Aiel Recruits (Bulky)",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_22,
   [itm_aiel_spear, itm_hide_buckler_weak, itm_cadinsor_grey, itm_shoufa_grey, itm_cadinsor_boots_grey],
   def_attrib_wot_super_infantry_3 ,wp_polearm(125)|wp(70),knows_wot_super_infantry_3 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  
  ["aiel_enforcer","Aiel Enforcer","Aiel Enforcers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_22,
   [itm_aiel_spear, itm_hide_buckler_normal, itm_cadinsor_green, itm_shoufa_green, itm_cadinsor_boots_green],
   def_attrib_wot_super_infantry_4 ,wp_polearm(165)|wp(120),knows_wot_super_infantry_4 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  
  ["aiel_recruit_warrior","Aiel Recruit (Warrior)","Aiel Recruits (Warrior)",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_22,
   [itm_aiel_spear, itm_hide_buckler_weak, itm_cadinsor_grey, itm_shoufa_grey, itm_cadinsor_boots_grey],
   def_attrib_wot_super_infantry_3 ,wp_polearm(125)|wp(70),knows_wot_super_infantry_3 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  
  ["aiel_brute","Aiel Brute","Aiel Brutes",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_22,
   [itm_aiel_spear, itm_aiel_knife, itm_cadinsor_green, itm_shoufa_green, itm_cadinsor_boots_green],
   def_attrib_wot_super_infantry_4 ,wp_polearm(165)|wp_one_handed(145)|wp(120),knows_wot_super_infantry_4 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  
  ["aiel_grappler","Aiel Grappler","Aiel Grapplers",tf_guarantee_all,0,0,fac_kingdom_22,
   [itm_nomad_bow, itm_arrows, itm_aiel_knife, itm_cadinsor_green, itm_shoufa_green, itm_cadinsor_boots_green],
   def_attrib_wot_super_infantry_4 ,wp_archery(165)|wp_one_handed(145)|wp(120),knows_wot_super_infantry_4 ,aiel_1_man_face_younger, aiel_2_man_face_old],


# Seanchan Empire
  
#  ["seanchan_recruit","Seanchan Recruit","Seanchan Recruits",tf_guarantee_armor,0,0,fac_kingdom_7,
#   [itm_scythe,itm_hatchet,itm_stones,itm_leather_cap,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_wrapping_boots],
#   def_attrib|level(3),wp(65),knows_common,man_face_young_1, man_face_old_2],
  
  ["seanchan_recruit_channeler","Seanchan Recruit (Channeler)","Seanchan Recruits (Channeler)",tf_female|tf_guarantee_all,0,0,fac_kingdom_23,
   [itm_channeler_dagger,itm_woolen_dress,itm_damane_boots],
   def_attrib|level(3),wp(60),knows_common,seanchan_1_woman_face_younger, seanchan_2_woman_face_middle],
  
  ["suldam","Sul'dam","Sul'dam",tf_female|tf_guarantee_all,0,0,fac_kingdom_23,
   [itm_suldam_dagger, itm_suldam_dress, itm_suldam_boots],
   def_attrib_wot_infantry_2,wp_one_handed(125)|wp(90),knows_wot_infantry_2,seanchan_1_woman_face_younger, seanchan_2_woman_face_old],
  
#  ["seanchan_recruit_soldier","Seanchan Recruit (Soldier)","Seanchan Recruits (Soldier)",tf_guarantee_all,0,0,fac_kingdom_7,
#   [itm_staff, itm_blue_gambeson, itm_leather_boots],
#   def_attrib|level(4),wp(70),knows_common,seanchan_1_man_face_young, seanchan_2_man_face_older],
  
  ["seanchan_armsman","Seanchan Armsman","Seanchan Armsmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_23,
   [itm_seanchan_straight_sword, itm_blue_gambeson, itm_leather_warrior_cap, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_1,wp_one_handed(85)|wp(70),knows_wot_infantry_1, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  
  ["seanchan_footman","Seanchan Footman","Seanchan Footmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_23,
   [itm_seanchan_straight_sword, itm_seanchan_low_armor, itm_seanchan_low_helmet, itm_seanchan_low_boots, itm_seanchan_low_gloves],
   def_attrib_wot_infantry_2,wp_one_handed(100)|wp(90),knows_wot_infantry_2, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  
  ["seanchan_swordsman","Seanchan Swordsman","Seanchan Swordsmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_23,
   [itm_seanchan_sword, itm_seanchan_middle_armor, itm_seanchan_middle_helmet, itm_seanchan_middle_boots, itm_seanchan_middle_gloves],
   def_attrib_wot_infantry_3,wp_two_handed(130)|wp(100),knows_wot_infantry_3, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  
  ["seanchan_blademaster","Seanchan Blademaster","Seanchan Blademasters",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_23,
   [itm_seanchan_large_sword, itm_seanchan_high_armor, itm_seanchan_high_helmet, itm_seanchan_high_boots, itm_seanchan_high_gloves],
   def_attrib_wot_infantry_4,wp_two_handed(150)|wp(120),knows_wot_infantry_4, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  
  ["seanchan_pikeman","Seanchan Pikeman","Seanchan Pikemen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_23,
   [itm_pike, itm_seanchan_middle_armor, itm_seanchan_middle_helmet, itm_seanchan_middle_boots, itm_seanchan_middle_gloves],
   def_attrib_wot_infantry_3,wp_polearm(130)|wp(100),knows_wot_infantry_3, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  
  ["seanchan_bowman","Seanchan Archer","Seanchan Archers",tf_guarantee_all,0,0,fac_kingdom_23,
   [itm_strong_bow, itm_arrows, itm_seanchan_straight_sword, itm_seanchan_low_armor, itm_seanchan_low_helmet, itm_seanchan_low_boots, itm_seanchan_low_gloves],
   def_attrib_wot_infantry_2,wp_archery(105)|wp_one_handed(100)|wp(90),knows_wot_archer_2, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  
  ["seanchan_scout","Seanchan Scout","Seanchan Scouts",tf_guarantee_all_cavalry,0,0,fac_kingdom_23,
   [itm_seanchan_straight_sword, itm_blue_gambeson, itm_leather_warrior_cap, itm_leather_boots, itm_leather_gloves, itm_saddle_horse],
   def_attrib_wot_cavalry_2,wp_one_handed(95)|wp(70),knows_wot_cavalry_2, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  
  ["seanchan_man_at_arms","Seanchan Man at Arms","Seanchan Men at Arms",tf_guarantee_all_cavalry,0,0,fac_kingdom_23,
   [itm_seanchan_straight_sword, itm_seanchan_low_armor, itm_seanchan_low_helmet, itm_seanchan_low_boots, itm_seanchan_low_gloves, itm_arabian_horse_a],
   def_attrib_wot_cavalry_3,wp_one_handed(125)|wp(90),knows_wot_cavalry_3, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  
  ["seanchan_lancer","Seanchan Lancer","Seanchan Lancers",tf_guarantee_all_cavalry,0,0,fac_kingdom_23,
   [itm_lance, itm_seanchan_straight_sword, itm_seanchan_middle_armor, itm_seanchan_middle_helmet, itm_seanchan_middle_boots, itm_seanchan_middle_gloves, itm_arabian_horse_b],
   def_attrib_wot_cavalry_4,wp_polearm(145)|wp(100),knows_wot_cavalry_4, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  
#  ["seanchan_conquered_ally","Seanchan Conquered Ally","Seanchan Conquered Allies",tf_guarantee_armor,0,0,fac_kingdom_7,
#   [itm_scythe,itm_hatchet,itm_stones,itm_leather_cap,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_wrapping_boots],
#   def_attrib|level(3),wp(65),knows_common,man_face_young_1, man_face_old_2],
  
  ["seanchan_tarabon_ally","Seanchan Tarabon Ally","Seanchan Tarabon Allies",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_23,
   [itm_staff, itm_tarabon_recruit_tunic, itm_nomad_boots],
   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1, tarabon_man_face_young, tarabon_man_face_older],
  
#  ["seanchan_conquered_ally_middle","Seanchan Conquered Ally (Middle)","Seanchan Conquered Allies (Middle)",tf_guarantee_armor,0,0,fac_kingdom_7,
#   [itm_scythe,itm_hatchet,itm_stones,itm_leather_cap,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_wrapping_boots],
#   def_attrib|level(3),wp(70),knows_common,man_face_young_1, man_face_old_2],
  
  ["seanchan_amadicia_ally","Seanchan Amadicia Ally","Seanchan Amadicia Allies",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_23,
   [itm_spear, itm_amadicia_recruit_tunic, itm_wrapping_boots],
   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1, amadicia_man_face_young, amadicia_man_face_older],
  
  ["seanchan_altara_ally","Seanchan Altara Ally","Seanchan Altara Allies",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_23,
   [itm_cleaver, itm_altara_recruit_armor, itm_altara_green_boots],
   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1, altara_man_face_young, altara_man_face_older],


# Shadowspawn
  
#  ["shadowspawn_recruit","Shadowspawn Recruit","Shadowspawn Recruits",tf_guarantee_armor,0,0,fac_kingdom_8,
#   [itm_scythe,itm_hatchet,itm_stones,itm_leather_cap,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_wrapping_boots],
#   def_attrib|level(3),wp(65),knows_common,man_face_young_1, man_face_old_2],
  
  ["shadowspawn_recruit_creature","Shadowspawn Recruit (Creature)","Shadowspawn Recruits (Creature)",tf_trolloc|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_24,
   [itm_hatchet,itm_stones,itm_trolloc_hawk_helmet, itm_trolloc_weak_armor, itm_black_mail_gauntlets, itm_black_leather_boots],
   def_attrib|level(3),wp(65),knows_common,man_face_young_1, man_face_old_2],
  
  ["trolloc_grunt","Trolloc Grunt","Trolloc Grunts",tf_trolloc|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_24,
   [itm_military_fork,itm_trolloc_hawk_helmet, itm_trolloc_weak_armor, itm_black_mail_gauntlets, itm_black_leather_boots],
    def_attrib_wot_super_infantry_2 ,wp_polearm(110)|wp(70),knows_wot_super_infantry_2,man_face_young_1, man_face_old_2],
  
  ["trolloc_hewer","Trolloc Hewer","Trolloc Hewers",tf_trolloc|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_24,
   [itm_two_handed_axe,itm_trolloc_goat_helmet, itm_trolloc_normal_armor, itm_black_mail_gauntlets, itm_black_leather_boots],
    def_attrib_wot_super_infantry_3 ,wp_two_handed(145)|wp(110),knows_wot_super_infantry_3,man_face_young_1, man_face_old_2],
  
  ["trolloc_berserker","Trolloc Berserker","Trolloc Berserker",tf_trolloc|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_24,
   [itm_trolloc_mace,itm_trolloc_goat_helmet, itm_trolloc_normal_armor, itm_black_mail_gauntlets, itm_black_leather_boots],
    def_attrib_wot_super_infantry_4 ,wp_two_handed(190)|wp(140),knows_wot_super_infantry_4,man_face_young_1, man_face_old_2],
  
  ["trolloc_clan_chief","Trolloc Clan Chief","Trolloc Clan Chiefs",tf_trolloc|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_24,
   [itm_great_long_bardiche,itm_trolloc_wolf_helmet, itm_trolloc_strong_armor, itm_black_mail_gauntlets, itm_black_leather_boots],
    def_attrib_wot_super_infantry_5 ,wp_polearm(250)|wp(200),knows_wot_super_infantry_5,man_face_young_1, man_face_old_2],
  
  ["trolloc_archer","Trolloc Archer","Trolloc Archers",tf_trolloc|tf_guarantee_all,0,0,fac_kingdom_24,
   [itm_war_bow,itm_arrows, itm_sword_secondary, itm_trolloc_hawk_helmet, itm_trolloc_weak_armor, itm_black_mail_gauntlets, itm_black_leather_boots],
    def_attrib_wot_super_infantry_2 ,wp_archery(110)|wp_one_handed(100)|wp(70),knows_wot_super_infantry_2,man_face_young_1, man_face_old_2],
  
  ["trolloc_stalker","Trolloc Stalker","Trolloc Stalkers",tf_trolloc|tf_guarantee_all,0,0,fac_kingdom_24,
   [itm_strong_bow,itm_arrows,itm_arrows, itm_sword_secondary, itm_trolloc_goat_helmet, itm_trolloc_weak_armor, itm_black_mail_gauntlets, itm_black_leather_boots],
    def_attrib_wot_super_infantry_4 ,wp_archery(175)|wp_one_handed(145)|wp(70),knows_wot_super_infantry_4,man_face_young_1, man_face_old_2],
  
#  ["shadowspawn_recruit_human","Shadowspawn Recruit (Human)","Shadowspawn Recruits (Human)",tf_guarantee_all,0,0,fac_kingdom_8,
#   [itm_falchion, itm_skullcap, itm_darkfriend_tunic, itm_leather_gloves, itm_leather_boots],
#   def_attrib|level(3),wp(65),knows_common,man_face_young_1, man_face_old_2],
  
  ["darkfriend_channeler","Darkfriend Channeler","Darkfriend Channelers",tf_guarantee_all,0,0,fac_kingdom_24,
   [itm_power_player, itm_power_ammo, itm_sword_secondary, itm_darkfriend_tunic, itm_leather_boots],
   def_attrib_wot_infantry_1,wp_firearm(105)|wp_one_handed(100)|wp(75),knows_wot_infantry_1|knows_power_draw_2|knows_fire_4|knows_earth_3|knows_spirit_3|knows_water_4|knows_air_1,man_face_young_1, man_face_old_2],

  ["darkfriend_wilder","Darkfriend Wilder","Darkfriend Wilders",tf_guarantee_all,0,0,fac_kingdom_24,
   [itm_power_player, itm_power_ammo, itm_darkfriend_tunic, itm_leather_boots],
   def_attrib|level(15),wp_firearm(175)|wp_one_handed(110)|wp(80),knows_common|knows_power_draw_3|knows_fire_6|knows_earth_6|knows_spirit_4|knows_water_4|knows_air_3,man_face_young_1, man_face_old_2],

  ["darkfriend_channeler_female","Darkfriend Channeler","Darkfriend Channelers",tf_female|tf_guarantee_all,0,0,fac_kingdom_24,
   [itm_power_player, itm_power_ammo, itm_channeler_dagger, itm_woolen_dress, itm_leather_boots],
   def_attrib_wot_infantry_1,wp_firearm(105)|wp_one_handed(100)|wp(75),knows_wot_infantry_1|knows_power_draw_2|knows_fire_2|knows_earth_1|knows_spirit_3|knows_water_4|knows_air_3,woman_face_1, woman_face_2],

  ["aes_sedai_black","Aes Sedai Black","Aes Sedai Blacks",tf_female|tf_guarantee_all,0,0,fac_kingdom_24,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_black_ajah_dress, itm_aes_sedai_black_ajah_shoes], # , itm_wig_brown_bun
   def_attrib|level(15),wp_firearm(175)|wp_one_handed(110)|wp(80),knows_common|knows_power_draw_2|knows_fire_5|knows_earth_3|knows_spirit_5|knows_water_6|knows_air_6,woman_face_1, woman_face_2],
  
  ["darkfriend_initiate","Darkfriend Initiate","Darkfriend Initiates",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_24,
   [itm_mace_3, itm_darkfriend_shield_weak, itm_darkfriend_tunic, itm_skullcap, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2,wp_one_handed(100)|wp(90),knows_wot_infantry_2, man_face_young_1, man_face_old_2],
  
  ["darkfriend_murderer","Darkfriend Murderer","Darkfriend Murderers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_24,
   [itm_sword_viking_3, itm_darkfriend_shield_normal, itm_darkfriend_armor, itm_leather_boots, itm_mail_mittens, itm_guard_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(120)|wp(100),knows_wot_infantry_3, man_face_young_1, man_face_old_2],
  
  ["darkfriend_ambusher","Darkfriend Ambushers","Darkfriend Ambushers",tf_guarantee_all_cavalry,0,0,fac_kingdom_24,
   [itm_sword_viking_3, itm_darkfriend_shield_normal, itm_darkfriend_armor, itm_leather_boots, itm_mail_mittens, itm_guard_helmet, itm_saddle_horse],
   def_attrib_wot_cavalry_2 ,wp_one_handed(105)|wp(75),knows_wot_cavalry_2, man_face_young_1, man_face_old_2],

##################
## Shara
##################

    ["shara_recruit","Shara Recruit","Shara Recruits",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_25,
   [itm_sword_medieval_a, itm_shara_recruit_scout_armor, itm_sarranid_boots_b],
   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1 ,man_face_young_1, man_face_old_2],

    ["shara_armsman","Shara Armsman","Shara Armsmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_25,
   [itm_red_arm_club, itm_shara_armsman_armor, itm_black_leather_boots, itm_leather_gloves, itm_black_turban],
   def_attrib_wot_infantry_2 ,wp_one_handed(110)|wp(75),knows_wot_infantry_2 ,man_face_young_1, man_face_old_2],

    ["shara_town_guard","Shara Town Guard","Shara Town Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_25,
   [itm_war_spear, itm_sword_medieval_b, itm_shara_town_guard_armor, itm_black_leather_boots, itm_scale_gauntlets, itm_black_turban_helmet2],
   def_attrib_wot_infantry_3 ,wp_polearm(125)|wp(80),knows_wot_infantry_3 ,man_face_young_1, man_face_old_2],

  ["shara_border_guard","Shara Border Guard","Shara Border Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_25,
   [itm_halberd, itm_sword_medieval_b, itm_shara_border_guard_armor, itm_splinted_greaves_nospurs_wot, itm_scale_gauntlets, itm_vaegir_spiked_helmet],
   def_attrib_wot_infantry_4 ,wp_polearm(135)|wp(90),knows_wot_infantry_4, man_face_young_1, man_face_old_2],

  ["shara_swordsman","Shara Swordsman","Shara Swordsmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_25,
   [itm_sword_medieval_c_long, itm_dec_steel_shield, itm_shara_border_guard_armor, itm_splinted_greaves_nospurs_wot, itm_scale_gauntlets, itm_vaegir_spiked_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(120)|wp(80),knows_wot_infantry_3, man_face_young_1, man_face_old_2],

  ["shara_bowman","Shara Bowman","Shara Bowmen",tf_guarantee_all,0,0,fac_kingdom_25,
   [itm_strong_bow, itm_arrows, itm_sword_secondary, itm_shara_bowman_armor, itm_sarranid_boots_b, itm_leather_gloves, itm_black_turban_helmet],
   def_attrib_wot_infantry_3 ,wp_archery(100)|wp_one_handed(90)|wp(80),knows_wot_archer_3, man_face_young_1, man_face_old_2],

  ["shara_scout","Shara Scout","Shara Scouts",tf_guarantee_all_cavalry,0,0,fac_kingdom_25,
   [itm_war_spear, itm_sword_medieval_a, itm_shara_recruit_scout_armor, itm_leather_boots, itm_leather_gloves, itm_black_turban, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_polearm(110)|wp_one_handed(100)|wp(75),knows_wot_cavalry_2, man_face_young_1, man_face_old_2],
  
  ["shara_man_at_arms","Shara Man at Arms","Shara Man at Arms",tf_guarantee_all_cavalry,0,0,fac_kingdom_25,
   [itm_sword_medieval_c_long, itm_brass_shield, itm_shara_mid_cavalry_armor, itm_brass_boots, itm_scale_gauntlets, itm_helmet5_brass, itm_hunter, itm_warhorse, itm_camel],
   def_attrib_wot_cavalry_3 ,wp_one_handed(135)|wp(110),knows_wot_cavalry_3 ,man_face_young_1, man_face_old_2],

  ["ayyad_villager","Ayyad Villager","Ayyad Villagers",tf_female|tf_guarantee_all,0,0,fac_kingdom_25,
   [itm_power_player, itm_power_ammo, itm_ayyad_villager_tunic, itm_sarranid_boots_b],
  def_attrib|level(10),wp_firearm(120)|wp_one_handed(110)|wp(75),knows_common|knows_power_draw_2|knows_fire_4|knows_earth_1|knows_spirit_3|knows_water_4|knows_air_3, woman_face_1, woman_face_2],
  
  ["ayyad_village_leader","Ayyad Village Leader","Ayyad Village Leaders",tf_female|tf_guarantee_all,0,0,fac_kingdom_25,
   [itm_power_player, itm_power_ammo, itm_ayyad_village_leader_tunic, itm_sarranid_boots_b],
   def_attrib|level(16),wp_firearm(150)|wp_one_handed(110)|wp(80),knows_common|knows_power_draw_3|knows_fire_5|knows_earth_2|knows_spirit_5|knows_water_5|knows_air_4, woman_face_1, woman_face_2],
  

#############
## Sea Folk
#############

    ["sea_folk_recruit","Sea Folk Recruit","Sea Folk Recruits",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_26,
   [itm_hand_axe],
   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1 ,seanchan_2_man_face_younger, seanchan_2_man_face_old],

    ["sea_folk_bilge_hand","Sea Folk Bilge Hand","Sea Folk Bilge Hands",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_26,
   [itm_one_handed_war_axe_b, itm_sea_folk_tunic],
   def_attrib_wot_infantry_2 ,wp_one_handed(110)|wp(75),knows_wot_infantry_2 ,seanchan_2_man_face_younger, seanchan_2_man_face_old],

    ["sea_folk_deck_hand","Sea Folk Deck Hand","Sea Folk Deck Hands",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_26,
   [itm_scimitar, itm_sea_folk_padded_armor, itm_spiked_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(125)|wp(80),knows_wot_infantry_3 ,seanchan_2_man_face_younger, seanchan_2_man_face_old],

  ["sea_folk_boatswain","Sea Folk Boatswain","Sea Folk Boatswains",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_26,
   [itm_scimitar_b, itm_wooden_round_shield, itm_sea_folk_padded_armor, itm_leather_gloves, itm_vaegir_spiked_helmet],
   def_attrib_wot_infantry_4 ,wp_one_handed(135)|wp(90),knows_wot_infantry_4, seanchan_2_man_face_younger, seanchan_2_man_face_old],

  ["sea_folk_dogwatcher","Sea Folk Dogwatcher","Sea Folk Dogwatchers",tf_guarantee_all,0,0,fac_kingdom_26,
   [itm_strong_bow, itm_arrows, itm_sword_secondary, itm_sea_folk_tunic, itm_spiked_helmet],
   def_attrib_wot_infantry_3 ,wp_archery(100)|wp_one_handed(90)|wp(80),knows_wot_archer_3, seanchan_2_man_face_younger, seanchan_2_man_face_old],

    ["sea_folk_weatherly","Sea Folk Weatherly","Sea Folk Weatherlies",tf_female|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_26,
   [itm_spear, itm_sea_folk_female_tunic],
   def_attrib_wot_infantry_2 ,wp_polearm(110)|wp(75),knows_wot_infantry_2 ,seanchan_2_woman_face_younger, seanchan_2_woman_face_old],

    ["sea_folk_quarterling","Sea Folk Quarterling","Sea Folk Quarterlings",tf_female|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_26,
   [itm_war_spear, itm_sea_folk_female_tunic_2 ,itm_wooden_round_shield],
   def_attrib_wot_infantry_3 ,wp_polearm(125)|wp(80),knows_wot_infantry_3 ,seanchan_2_woman_face_younger, seanchan_2_woman_face_old],

  ["sea_folk_sailmistress","Sea Folk Sailmistress","Sea Folk Sailmistresses",tf_female|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_26,
   [itm_scimitar_b, itm_sea_folk_female_tunic_2, itm_leather_gloves, itm_spiked_helmet],
   def_attrib_wot_infantry_4 ,wp_one_handed(135)|wp(90),knows_wot_infantry_4, seanchan_2_woman_face_younger, seanchan_2_woman_face_old],

  ["sea_folk_recruit_channeler","Sea Folk Recruit (Channeler)","Sea Folk Recruits (Channeler)",tf_female|tf_guarantee_all,0,0,fac_kingdom_26,
   [itm_power_player, itm_power_ammo, itm_sea_folk_female_tunic],
  def_attrib|level(10),wp_firearm(120)|wp_one_handed(110)|wp(75),knows_common|knows_power_draw_2|knows_fire_3|knows_earth_1|knows_spirit_3|knows_water_5|knows_air_4, seanchan_2_woman_face_younger, seanchan_2_woman_face_old],
  
  ["sea_folk_pupil","Sea Folk Pupil","Sea Folk Pupils",tf_female|tf_guarantee_all,0,0,fac_kingdom_26,
   [itm_power_player, itm_power_ammo, itm_sea_folk_female_tunic_2],
   def_attrib|level(16),wp_firearm(150)|wp_one_handed(110)|wp(80),knows_common|knows_power_draw_3|knows_fire_4|knows_earth_2|knows_spirit_5|knows_water_6|knows_air_5, seanchan_2_woman_face_younger, seanchan_2_woman_face_old],  
  

#####################
## Land of Madmen
#####################

    ["madmen_recruit","Madmen Recruit","Madmen Recruits",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_27,
   [itm_cudgel, itm_madmen_paint_2, itm_madmen_paint_1],
   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1 ,man_face_young_1, man_face_old_2],

    ["madmen_wanderer","Madmen Wanderer","Madmen Wanderers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_27,
   [itm_war_spear, itm_madmen_paint_3, itm_madmen_paint_2, itm_hide_boots],
   def_attrib_wot_infantry_2 ,wp_polearm(110)|wp(75),knows_wot_infantry_2 ,man_face_young_1, man_face_old_2],

    ["madmen_villager","Madmen Villager","Madmen Villagers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_27,
   [itm_hammer, itm_nomad_vest, itm_hide_boots, itm_steppe_cap],
   def_attrib_wot_infantry_3 ,wp_one_handed(125)|wp(80),knows_wot_infantry_3 ,man_face_young_1, man_face_old_2],

  ["madmen_clansman","Madmen Clansman","Madmen Clansmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_27,
   [itm_long_hafted_knobbed_mace, itm_long_hafted_spiked_mace, itm_madmen_rawhide_coat, itm_hide_boots, itm_nomad_cap, itm_leather_gloves],
   def_attrib_wot_infantry_4 ,wp_polearm(135)|wp(90),knows_wot_infantry_4, man_face_young_1, man_face_old_2],

  ["madmen_looter","Madmen Looter","Madmen Looters",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_27,
   [itm_one_handed_battle_axe_b, itm_madmen_rawhide_coat, itm_hide_boots, itm_nomad_cap, itm_leather_gloves],
   def_attrib_wot_infantry_3 ,wp_one_handed(120)|wp(80),knows_wot_infantry_3, man_face_young_1, man_face_old_2],

  ["madmen_hunter","Madmen Hunter","Madmen Hunters",tf_guarantee_all,0,0,fac_kingdom_27,
   [itm_throwing_spears, itm_throwing_spears, itm_one_handed_battle_axe_a, itm_pelt_coat, itm_hunter_boots, itm_nomad_cap_b],
   def_attrib_wot_infantry_2 ,wp_throwing(75)|wp_one_handed(70)|wp(60),knows_wot_archer_2, man_face_young_1, man_face_old_2],  

  ["madmen_ambusher","Madmen Ambusher","Madmen Ambushers",tf_guarantee_all,0,0,fac_kingdom_27,
   [itm_strong_bow, itm_arrows, itm_one_handed_battle_axe_a, itm_ragged_outfit, itm_hunter_boots, itm_leather_steppe_cap_a],
   def_attrib_wot_infantry_3 ,wp_archery(100)|wp_one_handed(90)|wp(80),knows_wot_archer_3, man_face_young_1, man_face_old_2],

  ["madmen_horse_tamer","Madmen Horse Tamer","Madmen Horse Tamers",tf_guarantee_all_cavalry,0,0,fac_kingdom_27,
   [itm_war_spear, itm_one_handed_battle_axe_a, itm_pelt_coat, itm_hunter_boots, itm_nomad_cap_b, itm_steppe_horse],
   def_attrib_wot_cavalry_2 ,wp_polearm(110)|wp_one_handed(100)|wp(75),knows_wot_cavalry_2, man_face_young_1, man_face_old_2],
  
  ["madmen_slave_catcher","Madmen Slave Catcher","Madmen Slave Catchers",tf_guarantee_all_cavalry,0,0,fac_kingdom_27,
   [itm_long_hafted_knobbed_mace, itm_one_handed_battle_axe_a, itm_ragged_outfit, itm_hunter_boots, itm_leather_steppe_cap_a, itm_arabian_horse_a],
   def_attrib_wot_cavalry_3 ,wp_polearm(135)|wp_one_handed(110)|wp(85),knows_wot_cavalry_3 ,man_face_young_1, man_face_old_2],

    ["madmen_air_shifter","Madman Air Shifter","Madmen Air Shifters",tf_guarantee_all,0,0,fac_kingdom_27,
   [itm_power_player, itm_power_ammo, itm_one_handed_battle_axe_a, itm_madmen_paint_4, itm_hide_boots],
   def_attrib_wot_infantry_1,wp_firearm(105)|wp_one_handed(100)|wp(75),knows_wot_infantry_1|knows_power_draw_2|knows_fire_3|knows_earth_3|knows_spirit_3|knows_water_4|knows_air_3,man_face_young_1, man_face_old_2],
  
    ["madmen_fire_tamer","Madmen Fire Tamer","Madmen Fire Tamers",tf_guarantee_all,0,0,fac_kingdom_27,
   [itm_power_player, itm_power_ammo, itm_one_handed_battle_axe_a, itm_ragged_outfit, itm_hide_boots],
   def_attrib_wot_infantry_2,wp_firearm(130)|wp_one_handed(110)|wp(80),knows_wot_infantry_2|knows_power_draw_3|knows_fire_6|knows_earth_6|knows_spirit_4|knows_water_4|knows_air_5,man_face_young_1, man_face_old_2],  

  
##################
## Toman Head
##################

    ["toman_head_recruit","Toman Head Recruit","Toman Head Recruits",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_28,
   [itm_sword_medieval_a, itm_toman_head_recruit_tunic, itm_wrapping_boots],
   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1 ,arad_doman_man_face_younger, tarabon_man_face_old],

    ["toman_head_footman","Toman Head Footman","Toman Head Footmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_28,
   [itm_red_arm_club, itm_toman_head_army_armor, itm_toman_head_shield_normal, itm_leather_boots, itm_leather_gloves, itm_nordic_archer_helmet],
   def_attrib_wot_infantry_2 ,wp_one_handed(110)|wp(75),knows_wot_infantry_2 ,arad_doman_man_face_younger, tarabon_man_face_old],  


  

#  ["draghkar","Draghkar","Draghkar",tf_guarantee_armor,0,0,fac_kingdom_1,
#   [itm_scythe,itm_hatchet,itm_pickaxe,itm_club,itm_stones,itm_tab_shield_heater_a,itm_leather_cap,itm_felt_hat,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_nomad_boots,itm_wrapping_boots],
#   def_attrib|level(5),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],


##########################################
##### End WoT Faction Troops (Upgradeable)
##########################################


############################################################################################################
###################################################################### Non-upgrading troops begin
############################################################################################################


##########################################
##### WoT Faction Troops (Non-Upgradeable)
##########################################

# Legion of the Dragon #
    ["ashaman_veteran","Asha'man Veteran","Asha'man Veterans",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_power_player, itm_power_ammo, itm_ashaman_coat, itm_black_leather_boots, itm_saddle_horse],
   def_attrib_wot_infantry_3,wp_firearm(200)|wp_one_handed(150)|wp(125),knows_wot_horse_archer_3|knows_power_draw_5|knows_fire_7|knows_earth_7|knows_spirit_6|knows_water_5|knows_air_5,man_face_young_1, man_face_old_2],
  
    ["legion_blademaster","Legion Blademaster","Legion Blademasters",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_great_sword, itm_legion_plate, itm_shynbaulds_wot, itm_mail_gauntlets_wot, itm_andoran_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(180)|wp(100),knows_wot_infantry_4 ,man_face_young_1, man_face_old_2],
  
    ["legion_bannerman","Legion Bannerman","Legion Bannermen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_ashwood_pike, itm_legion_plate, itm_shynbaulds_wot, itm_mail_gauntlets_wot, itm_andoran_helmet],
   def_attrib_wot_infantry_4 ,wp_polearm(180)|wp(100),knows_wot_infantry_4 ,man_face_young_1, man_face_old_2],
  
    ["legion_heavy_crossbowman","Legion Heavy Crossbowman","Legion Heavy Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_heavy_crossbow, itm_steel_bolts, itm_sword_secondary, itm_legion_shield_normal, itm_legion_army_armor, itm_leather_boots, itm_leather_gloves, itm_nordic_helmet],
   def_attrib_wot_infantry_3 ,wp_crossbow(150)|wp_one_handed(110)|wp(85),knows_wot_archer_3 ,man_face_young_1, man_face_old_2],
  
    ["legion_heavy_lancer","Legion Heavy Lancer","Legion Heavy Lancers",tf_guarantee_all_cavalry,0,0,fac_kingdom_1,
   [itm_heavy_lance, itm_sword_medieval_c_long, itm_legion_shield_strong, itm_legion_plate, itm_steel_greaves_wot, itm_gauntlets, itm_andoran_helmet, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_3 ,wp_polearm(150)|wp_one_handed(140)|wp(100),knows_wot_cavalry_3 ,man_face_young_1, man_face_old_2],
  
    ["legion_captain","Legion Captain","Legion Captains",tf_guarantee_all_cavalry,0,0,fac_kingdom_1,
   [itm_great_sword, itm_legion_shield_strong, itm_legion_plate, itm_steel_greaves_wot, itm_gauntlets, itm_andoran_helmet, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_4 ,wp_two_handed(175)|wp_one_handed(150)|wp(100),knows_wot_cavalry_4 ,man_face_young_1, man_face_old_2],

    ["ashaman_soldier_warder","Asha'man Soldier","Asha'man Soldiers",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_power_player, itm_power_ammo, itm_sword_secondary, itm_ashaman_soldier_coat, itm_black_leather_boots],
   def_attrib_wot_infantry_1,wp_firearm(105)|wp_one_handed(100)|wp(75),knows_wot_infantry_1|knows_power_draw_2|knows_fire_4|knows_earth_2|knows_spirit_3|knows_water_4|knows_air_2,murandy_man_face_young, altara_man_face_older],

    ["ashaman_dedicated_warder","Asha'man Dedicated","Asha'man Dedicated",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_power_player, itm_power_ammo, itm_ashaman_dedicated_coat, itm_black_leather_boots],
   def_attrib_wot_infantry_2,wp_firearm(130)|wp_one_handed(110)|wp(80),knows_wot_infantry_2|knows_power_draw_3|knows_fire_5|knows_earth_6|knows_spirit_5|knows_water_4|knows_air_4,ghealdan_man_face_younger, amadicia_man_face_older],
  
    ["ashaman_warder","Asha'man","Asha'man",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_power_player, itm_power_ammo, itm_ashaman_coat, itm_black_leather_boots, itm_saddle_horse],
   def_attrib_wot_infantry_2,wp_firearm(175)|wp_one_handed(110)|wp(90),knows_wot_horse_archer_2|knows_power_draw_4|knows_fire_7|knows_earth_6|knows_spirit_6|knows_water_5|knows_air_4,tarabon_man_face_younger, arad_doman_man_face_older],  
  #Other
  ["legion_messenger","Legion Messenger","Legion Messengers",tf_guarantee_all_cavalry,0,0,fac_kingdom_1,
   [itm_spiked_mace, itm_legion_shield_normal, itm_sword_viking_3, itm_legion_army_armor, itm_leather_boots, itm_leather_gloves, itm_nordic_helmet, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_polearm(120)|wp_one_handed(120)|wp(85),knows_wot_cavalry_2 ,man_face_young_1, man_face_old_2],

  ["legion_deserter","Legion Deserter","Legion Deserters",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_sword_medieval_b, itm_legion_army_armor, itm_legion_shield_weak, itm_leather_boots, itm_leather_gloves, itm_nordic_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(125)|wp(80),knows_wot_infantry_3 ,man_face_young_1, man_face_old_2],

  ["legion_prison_guard","Prison Guard","Prison Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_great_sword, itm_legion_plate, itm_shynbaulds_wot, itm_mail_gauntlets_wot, itm_andoran_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(180)|wp(100),knows_wot_infantry_4 ,man_face_young_1, man_face_old_2],
  
  ["legion_castle_guard","Castle Guard","Castle Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
   [itm_great_sword, itm_legion_plate, itm_shynbaulds_wot, itm_mail_gauntlets_wot, itm_andoran_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(180)|wp(100),knows_wot_infantry_4 ,man_face_young_1, man_face_old_2],

## Band of the Red Hand  
    ["red_hand_bannerman","Red Hand Bannerman","Red Hand Bannermen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
   [itm_ashwood_pike, itm_red_hand_plate, itm_red_hand_greaves, itm_red_hand_plate_gauntlets, itm_red_hand_kettle_helm],
   def_attrib_wot_infantry_4 ,wp_polearm(180)|wp(100),knows_wot_infantry_4 ,man_face_young_1, man_face_old_2],
  
    ["red_hand_swordsman","Red Hand Swordsman","Red Hand Swordsmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
   [itm_sword_viking_3, itm_red_hand_shield_strong, itm_red_hand_plate, itm_red_hand_greaves, itm_red_hand_plate_gauntlets, itm_red_hand_kettle_helm],
   def_attrib_wot_infantry_4 ,wp_one_handed(180)|wp(100),knows_wot_infantry_4 ,man_face_young_1, man_face_old_2],
  
    ["red_hand_fast_crossbowman","Red Hand Fast Crossbowman","Red Hand Fast Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_red_hand_fast_crossbow, itm_steel_bolts, itm_steel_bolts, itm_sword_secondary, itm_red_hand_plate, itm_red_hand_greaves, itm_red_hand_plate_gauntlets, itm_red_hand_kettle_helm],
   def_attrib_wot_infantry_4 ,wp_crossbow(175)|wp_one_handed(150)|wp(85),knows_wot_archer_4 ,man_face_young_1, man_face_old_2],
  
    ["red_hand_lancer","Red Hand Lancer","Red Hand Lancers",tf_guarantee_all_cavalry,0,0,fac_kingdom_2,
   [itm_heavy_lance, itm_sword_medieval_c_long, itm_red_hand_shield_strong, itm_red_hand_plate, itm_red_hand_greaves, itm_red_hand_plate_gauntlets, itm_red_hand_kettle_helm, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_3 ,wp_polearm(150)|wp_one_handed(140)|wp(100),knows_wot_cavalry_3 ,man_face_young_1, man_face_old_2],
  
    ["red_hand_captain","Red Hand Captain","Red Hand Captains",tf_guarantee_all_cavalry,0,0,fac_kingdom_2,
   [itm_great_sword, itm_red_hand_shield_strong, itm_red_hand_plate, itm_red_hand_greaves, itm_red_hand_plate_gauntlets, itm_red_hand_kettle_helm, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_4 ,wp_two_handed(175)|wp_one_handed(150)|wp(100),knows_wot_cavalry_4 ,man_face_young_1, man_face_old_2],
  
    ["red_hand_skirmisher","Red Hand Skirmisher","Red Hand Skirmishers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_khergit_bow, itm_arrows, itm_sword_secondary, itm_red_hand_tunic, itm_leather_boots, itm_leather_gloves, itm_red_hand_bell_helm, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_archery(120)|wp_one_handed(110)|wp(85),knows_wot_horse_archer_3 ,man_face_young_1, man_face_old_2],
  #Other
    ["red_hand_messenger","Red Hand Messenger","Red Hand Messengers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_khergit_bow, itm_arrows, itm_sword_secondary, itm_red_hand_tunic, itm_leather_boots, itm_leather_gloves, itm_red_hand_bell_helm, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_archery(120)|wp_one_handed(110)|wp(85),knows_wot_horse_archer_3 ,man_face_young_1, man_face_old_2],

    ["red_hand_deserter","Red Hand Deserter","Red Hand Deserters",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
   [itm_sword_medieval_a, itm_red_hand_tunic, itm_wrapping_boots],
   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1 ,man_face_young_1, man_face_old_2],

    ["red_hand_prison_guard","Prison Guard","Prison Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
   [itm_ashwood_pike, itm_red_hand_plate, itm_red_hand_greaves, itm_red_hand_plate_gauntlets, itm_red_hand_kettle_helm],
   def_attrib_wot_infantry_4 ,wp_polearm(180)|wp(100),knows_wot_infantry_4 ,man_face_young_1, man_face_old_2],
  
    ["red_hand_castle_guard","Castle Guard","Castle Guards",tf_guarantee_all_cavalry,0,0,fac_kingdom_2,
   [itm_great_sword, itm_red_hand_shield_strong, itm_red_hand_plate, itm_red_hand_greaves, itm_red_hand_plate_gauntlets, itm_red_hand_kettle_helm, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_4 ,wp_two_handed(175)|wp_one_handed(150)|wp(100),knows_wot_cavalry_4 ,man_face_young_1, man_face_old_2],
  
## Two Rivers  
    ["two_rivers_halberdier","Two Rivers Halberdier","Two Rivers Halberdiers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
   [itm_halberd, itm_two_rivers_armor, itm_leather_boots, itm_leather_gloves, itm_segmented_helmet],
   def_attrib_wot_infantry_3 ,wp_polearm(115)|wp(85),knows_wot_infantry_3 ,andor_man_face_younger, andor_man_face_older],
  
    ["two_rivers_scout","Two Rivers Scout","Two Rivers Scouts",tf_guarantee_all_cavalry,0,0,fac_kingdom_3,
   [itm_spear, itm_sword_medieval_a, itm_ragged_outfit, itm_leather_jerkin, itm_leather_boots, itm_leather_gloves, itm_leather_cap, itm_segmented_helmet, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_polearm(125)|wp(80),knows_wot_cavalry_2, andor_man_face_younger, andor_man_face_older],
  
    ["two_rivers_marksman","Two Rivers Marksman","Two Rivers Marksmen",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_two_rivers_long_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_sword_secondary, itm_two_rivers_armor, itm_leather_boots, itm_leather_gloves, itm_segmented_helmet],
   def_attrib_wot_infantry_5 ,wp_archery(175)|wp_one_handed(145)|wp(125),knows_wot_archer_5 ,andor_man_face_younger, andor_man_face_older],
  #Other
    ["two_rivers_messenger","Two Rivers Messenger","Two Rivers Messengers",tf_guarantee_all_cavalry,0,0,fac_kingdom_3,
   [itm_spear, itm_ragged_outfit, itm_leather_jerkin, itm_leather_boots, itm_leather_gloves, itm_leather_cap, itm_segmented_helmet, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_polearm(125)|wp(80),knows_wot_cavalry_2, andor_man_face_younger, andor_man_face_older],

    ["two_rivers_deserter","Two Rivers Deserter","Two Rivers Deserters",tf_guarantee_all_cavalry,0,0,fac_kingdom_3,
   [itm_spear, itm_ragged_outfit, itm_leather_jerkin, itm_leather_boots, itm_leather_gloves, itm_leather_cap, itm_segmented_helmet, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_polearm(125)|wp(80),knows_wot_cavalry_2, andor_man_face_younger, andor_man_face_older],

    ["two_rivers_prison_guard","Prison Guard","Prison Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
   [itm_halberd, itm_two_rivers_armor, itm_leather_boots, itm_leather_gloves, itm_segmented_helmet],
   def_attrib_wot_infantry_3 ,wp_polearm(115)|wp(85),knows_wot_infantry_3 ,andor_man_face_younger, andor_man_face_older],
  
    ["two_rivers_castle_guard","Castle Guard","Castle Guards",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_two_rivers_long_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_sword_secondary, itm_two_rivers_armor, itm_leather_boots, itm_leather_gloves, itm_segmented_helmet],
   def_attrib_wot_infantry_5 ,wp_archery(175)|wp_one_handed(145)|wp(125),knows_wot_archer_5 ,andor_man_face_younger, andor_man_face_older],


# Southlander Coalition (1)

## Mayene
  ["mayene_swordsman","Mayene Swordsman","Mayene Swordsmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_4,
   [itm_mayene_sword, itm_mayene_shield_strong, itm_mayene_army_armor, itm_leather_boots, itm_leather_gloves, itm_kettle_hat_wot],
   def_attrib_wot_infantry_3 ,wp_one_handed(150)|wp(100),knows_wot_infantry_3 ,mayene_man_face_young, mayene_man_face_older],
  
  ["mayene_bowman","Mayene Bowman","Mayene Bowmen",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_short_bow, itm_arrows, itm_sword_secondary, itm_mayene_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_leather_cap],
   def_attrib_wot_infantry_2 ,wp_archery(90)|wp_one_handed(85)|wp(80),knows_wot_archer_2 ,mayene_man_face_young, mayene_man_face_older],
  
  ["mayene_royal_guard","Mayene Winged Guard","Mayene Winged Guards",tf_guarantee_all_cavalry,0,0,fac_kingdom_4,
   [itm_heavy_lance, itm_sword_medieval_c_long, itm_mayene_plate, itm_mayene_greaves, itm_mayene_gauntlets_red, itm_mayene_winged_guard_helmet, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_4 ,wp_polearm(140)|wp_one_handed(130)|wp(100),knows_wot_cavalry_4 ,mayene_man_face_young, mayene_man_face_older],
  #Other
  ["mayene_messenger","Mayene Messenger","Mayene Messengers",tf_guarantee_all_cavalry,0,0,fac_kingdom_4,
   [itm_heavy_lance, itm_mayene_plate, itm_mayene_greaves, itm_mayene_gauntlets_red, itm_mayene_winged_guard_helmet, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_4 ,wp_polearm(140)|wp_one_handed(130)|wp(100),knows_wot_cavalry_4 ,mayene_man_face_young, mayene_man_face_older],

  ["mayene_deserter","Mayene Deserter","Mayene Deserters",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_short_bow, itm_arrows, itm_sword_secondary, itm_mayene_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_leather_cap],
   def_attrib_wot_infantry_2 ,wp_archery(90)|wp_one_handed(85)|wp(80),knows_wot_archer_2 ,mayene_man_face_young, mayene_man_face_older],

  ["mayene_prison_guard","Prison Guard","Prison Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_4,
   [itm_mayene_sword, itm_mayene_shield_strong, itm_mayene_army_armor, itm_leather_boots, itm_leather_gloves, itm_kettle_hat_wot],
   def_attrib_wot_infantry_3 ,wp_one_handed(150)|wp(100),knows_wot_infantry_3 ,mayene_man_face_young, mayene_man_face_older],
  
  ["mayene_castle_guard","Castle Guard","Castle Guards",tf_guarantee_all_cavalry,0,0,fac_kingdom_4,
   [itm_heavy_lance, itm_mayene_plate, itm_mayene_greaves, itm_mayene_gauntlets_red, itm_mayene_winged_guard_helmet, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_4 ,wp_polearm(140)|wp_one_handed(130)|wp(100),knows_wot_cavalry_4 ,mayene_man_face_young, mayene_man_face_older],


## Cairhien  
  ["cairhien_bannerman","Cairhien Bannerman","Cairhien Bannermen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_5,
   [itm_ashwood_pike, itm_cairhien_plate, itm_shynbaulds_wot, itm_gauntlets, itm_cairhien_helmet],
   def_attrib_wot_infantry_4 ,wp_polearm(180)|wp(100),knows_wot_infantry_4 ,cairhien_man_face_young, cairhien_man_face_older],
  
  ["cairhien_crossbowman","Cairhien Crossbowman","Cairhien Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_crossbow, itm_bolts, itm_sword_secondary, itm_cairhien_shield_normal, itm_cairhien_army_armor, itm_leather_boots, itm_leather_gloves, itm_bascinet],
   def_attrib_wot_infantry_3 ,wp_crossbow(125)|wp_one_handed(110)|wp(85),knows_wot_archer_3 ,cairhien_man_face_young, cairhien_man_face_older],
  
  ["cairhien_light_cavalry","Cairhien Light Cavalry","Cairhien Light Cavalry",tf_guarantee_all_cavalry,0,0,fac_kingdom_5,
   [itm_sword_medieval_b, itm_cairhien_shield_normal, itm_cairhien_army_armor, itm_leather_boots, itm_leather_gloves, itm_bascinet, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_one_handed(120)|wp(85),knows_wot_cavalry_3 ,cairhien_man_face_young, cairhien_man_face_older],
  
  ["cairhien_lancer","Cairhien Lancer","Cairhien Lancers",tf_guarantee_all_cavalry,0,0,fac_kingdom_5,
   [itm_heavy_lance, itm_sword_medieval_c_long, itm_cairhien_shield_strong, itm_cairhien_plate, itm_shynbaulds_wot, itm_gauntlets, itm_cairhien_helmet, itm_courser, itm_hunter],
   def_attrib_wot_cavalry_3 ,wp_polearm(150)|wp_one_handed(140)|wp(100),knows_wot_cavalry_3 ,cairhien_man_face_young, cairhien_man_face_older],
  #Other
  ["cairhien_messenger","Cairhien Messenger","Cairhien Messengers",tf_guarantee_all_cavalry,0,0,fac_kingdom_5,
   [itm_sword_medieval_b, itm_cairhien_shield_normal, itm_cairhien_army_armor, itm_leather_boots, itm_leather_gloves, itm_bascinet, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_one_handed(120)|wp(85),knows_wot_cavalry_3 ,cairhien_man_face_young, cairhien_man_face_older],

  ["cairhien_deserter","Cairhien Deserter","Cairhien Deserters",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_crossbow, itm_bolts, itm_sword_secondary, itm_cairhien_shield_normal, itm_cairhien_army_armor, itm_leather_boots, itm_leather_gloves, itm_bascinet],
   def_attrib_wot_infantry_3 ,wp_crossbow(125)|wp_one_handed(110)|wp(85),knows_wot_archer_3 ,cairhien_man_face_young, cairhien_man_face_older],

  ["cairhien_prison_guard","Prison Guard","Prison Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_5,
   [itm_ashwood_pike, itm_cairhien_plate, itm_shynbaulds_wot, itm_gauntlets, itm_cairhien_helmet],
   def_attrib_wot_infantry_4 ,wp_polearm(180)|wp(100),knows_wot_infantry_4 ,cairhien_man_face_young, cairhien_man_face_older],
  
  ["cairhien_castle_guard","Castle Guard","Castle Guards",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_crossbow, itm_bolts, itm_sword_secondary, itm_cairhien_shield_normal, itm_cairhien_army_armor, itm_leather_boots, itm_leather_gloves, itm_bascinet],
   def_attrib_wot_infantry_3 ,wp_crossbow(125)|wp_one_handed(110)|wp(85),knows_wot_archer_3 ,cairhien_man_face_young, cairhien_man_face_older],


## Illian
  ["illian_companion_captain","Illian Companion Captian","Illian Companion Captians",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_6,
   [itm_two_handed_cleaver, itm_illian_companion_captain_surcoat, itm_mail_chausses, itm_scale_gauntlets, itm_illian_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(180)|wp(125),knows_wot_infantry_4, illian_man_face_young, illian_man_face_older],
  
  ["illian_marksman","Illian Marksman","Illian Marksmen",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_heavy_crossbow, itm_steel_bolts, itm_sword_secondary, itm_illian_army_armor, itm_leather_boots, itm_leather_gloves, itm_khergit_war_helmet],
   def_attrib_wot_infantry_4 ,wp_crossbow(145)|wp_one_handed(110)|wp(100),knows_wot_archer_4, illian_man_face_young, illian_man_face_older],
  
  ["illian_man_at_arms","Illian Man at Arms","Illian Man at Arms",tf_guarantee_all_cavalry,0,0,fac_kingdom_6,
   [itm_spiked_mace, itm_illian_shield_normal, itm_illian_army_armor, itm_leather_boots, itm_leather_gloves, itm_khergit_war_helmet, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_one_handed(120)|wp(85),knows_wot_cavalry_2, illian_man_face_young, illian_man_face_older],
  #Other
  ["illian_messenger","Illian Messenger","Illian Messengers",tf_guarantee_all_cavalry,0,0,fac_kingdom_6,
   [itm_spiked_mace, itm_illian_shield_normal, itm_illian_army_armor, itm_leather_boots, itm_leather_gloves, itm_khergit_war_helmet, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_one_handed(120)|wp(85),knows_wot_cavalry_2, illian_man_face_young, illian_man_face_older],

  ["illian_deserter","Illian Deserter","Illian Deserters",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_6,
   [itm_illian_seax, itm_illian_shield_weak, itm_illian_recruit_tunic, itm_leather_boots, itm_skullcap],
   def_attrib_wot_infantry_2 ,wp_one_handed(90)|wp(70),knows_wot_infantry_2, illian_man_face_young, illian_man_face_older],

  ["illian_prison_guard","Prison Guard","Prison Guards",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_heavy_crossbow, itm_steel_bolts, itm_sword_secondary, itm_illian_army_armor, itm_leather_boots, itm_leather_gloves, itm_khergit_war_helmet],
   def_attrib_wot_infantry_4 ,wp_crossbow(145)|wp_one_handed(110)|wp(100),knows_wot_archer_4, illian_man_face_young, illian_man_face_older],
  
  ["illian_castle_guard","Castle Guard","Castle Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_6,
   [itm_two_handed_cleaver, itm_illian_companion_captain_surcoat, itm_mail_chausses, itm_scale_gauntlets, itm_illian_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(180)|wp(125),knows_wot_infantry_4, illian_man_face_young, illian_man_face_older],


## Murandy  
  ["murandy_berserker","Murandy Berserker","Murandy Berserkers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_7,
   [itm_warhammer, itm_murandy_elite_armor, itm_mail_chausses, itm_mail_mittens, itm_nordic_huscarl_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(185)|wp(125),knows_wot_infantry_4, murandy_man_face_young, murandy_man_face_older],
  
  ["murandy_marksman","Murandy Marksman","Murandy Marksmen",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_war_bow, itm_bodkin_arrows, itm_sword_secondary, itm_murandy_leather_armor, itm_leather_boots, itm_leather_gloves, itm_nordic_fighter_helmet],
   def_attrib_wot_infantry_4 ,wp_archery(140)|wp_one_handed(110)|wp(100),knows_wot_archer_4, murandy_man_face_young, murandy_man_face_older],
  
  ["murandy_captain","Murandy Captain","Murandy Captains",tf_guarantee_all_cavalry,0,0,fac_kingdom_7,
   [itm_heavy_lance, itm_sword_medieval_c_long, itm_murandy_shield_strong, itm_murandy_elite_armor, itm_mail_mittens, itm_mail_chausses, itm_nordic_huscarl_helmet, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_3 ,wp_polearm(145)|wp_one_handed(120)|wp(100),knows_wot_cavalry_3 ,murandy_man_face_young, murandy_man_face_older],
  #Other
  ["murandy_messenger","Murandy Messenger","Murandy Messengers",tf_guarantee_all_cavalry,0,0,fac_kingdom_7,
   [itm_hammer, itm_murandy_shield_weak, itm_murandy_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_leather_warrior_cap, itm_steppe_horse],
   def_attrib_wot_cavalry_1 ,wp_one_handed(100)|wp(70),knows_wot_cavalry_1, murandy_man_face_young, murandy_man_face_older],

  ["murandy_deserter","Murandy Deserter","Murandy Deserters",tf_guarantee_all_cavalry,0,0,fac_kingdom_7,
   [itm_hammer, itm_murandy_shield_weak, itm_murandy_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_leather_warrior_cap, itm_steppe_horse],
   def_attrib_wot_cavalry_1 ,wp_one_handed(100)|wp(70),knows_wot_cavalry_1, murandy_man_face_young, murandy_man_face_older],

  ["murandy_prison_guard","Prison Guard","Prison Guards",tf_guarantee_all_cavalry,0,0,fac_kingdom_7,
   [itm_heavy_lance, itm_murandy_shield_strong, itm_murandy_elite_armor, itm_mail_mittens, itm_mail_chausses, itm_nordic_huscarl_helmet, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_3 ,wp_polearm(145)|wp_one_handed(120)|wp(100),knows_wot_cavalry_3 ,murandy_man_face_young, murandy_man_face_older],
  
  ["murandy_castle_guard","Castle Guard","Castle Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_7,
   [itm_warhammer, itm_murandy_elite_armor, itm_mail_chausses, itm_mail_mittens, itm_nordic_huscarl_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(185)|wp(125),knows_wot_infantry_4, murandy_man_face_young, murandy_man_face_older],


## Altara
  ["altara_royal_guard","Altara Royal Guard","Altara Royal Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_8,
   [itm_altara_royal_guard_halberd, itm_altara_royal_guard_armor, itm_altara_royal_guard_boots, itm_scale_gauntlets, itm_altara_royal_guard_helmet],
   def_attrib_wot_infantry_4 ,wp_polearm(180)|wp(125),knows_wot_infantry_4, altara_man_face_young, altara_man_face_older],
  
  ["altara_knife_thrower","Altara Knife Thrower","Altara Knife Throwers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_8,
   [itm_throwing_knives, itm_scimitar, itm_altara_army_armor, itm_altara_green_boots, itm_leather_gloves, itm_vaegir_spiked_helmet],
   def_attrib_wot_infantry_3 ,wp_throwing(110)|wp_one_handed(105)|wp(95),knows_wot_thrower_3 ,altara_man_face_young, altara_man_face_older],
  
  ["altara_man_at_arms","Altara Man at Arms","Altara Man at Arms",tf_guarantee_all_cavalry,0,0,fac_kingdom_8,
   [itm_sarranid_cavalry_sword, itm_altara_shield_strong, itm_altara_army_armor, itm_leather_gloves, itm_altara_green_boots, itm_vaegir_spiked_helmet, itm_courser, itm_hunter],
   def_attrib_wot_cavalry_3 ,wp_one_handed(135)|wp(100),knows_wot_cavalry_3 ,altara_man_face_young, altara_man_face_older],
   
  ["altara_skirmisher","Altara Skirmisher","Altara Skirmishers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_khergit_bow, itm_arrows, itm_sword_secondary, itm_altara_army_armor, itm_altara_green_boots, itm_leather_gloves, itm_vaegir_spiked_helmet, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_archery(120)|wp_one_handed(110)|wp(85),knows_wot_horse_archer_2 ,altara_man_face_young, altara_man_face_older],
  #Other
  ["altara_messenger","Altara Messenger","Altara Messengers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_khergit_bow, itm_arrows, itm_sword_secondary, itm_altara_army_armor, itm_altara_green_boots, itm_leather_gloves, itm_vaegir_spiked_helmet, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_archery(120)|wp_one_handed(110)|wp(85),knows_wot_horse_archer_2 ,altara_man_face_young, altara_man_face_older],

  ["altara_deserter","Altara Deserter","Altara Deserters",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_8,
   [itm_throwing_knives, itm_scimitar, itm_altara_army_armor, itm_altara_green_boots, itm_leather_gloves, itm_vaegir_spiked_helmet],
   def_attrib_wot_infantry_3 ,wp_throwing(110)|wp_one_handed(105)|wp(95),knows_wot_thrower_3 ,altara_man_face_young, altara_man_face_older],

  ["altara_prison_guard","Prison Guard","Prison Guards",tf_guarantee_all_cavalry,0,0,fac_kingdom_8,
   [itm_sarranid_cavalry_sword, itm_altara_shield_strong, itm_altara_army_armor, itm_leather_gloves, itm_altara_green_boots, itm_vaegir_spiked_helmet, itm_courser, itm_hunter],
   def_attrib_wot_cavalry_3 ,wp_one_handed(135)|wp(100),knows_wot_cavalry_3 ,altara_man_face_young, altara_man_face_older],
  
  ["altara_castle_guard","Castle Guard","Castle Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_8,
   [itm_altara_royal_guard_halberd, itm_altara_royal_guard_armor, itm_altara_royal_guard_boots, itm_scale_gauntlets, itm_altara_royal_guard_helmet],
   def_attrib_wot_infantry_4 ,wp_polearm(180)|wp(125),knows_wot_infantry_4, altara_man_face_young, altara_man_face_older],


## Arad Doman
  ["arad_doman_long_swordsman","Arad Doman Long Swordsman","Arad Doman Long Swordsmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_9,
   [itm_sword_medieval_d_long, itm_arad_doman_shield_strong, itm_arad_doman_elite_armor, itm_splinted_greaves, itm_gauntlets, itm_nasal_helmet],
   def_attrib_wot_infantry_4 ,wp_one_handed(150)|wp(100),knows_wot_infantry_4, arad_doman_man_face_young, arad_doman_man_face_older],
  
  ["arad_doman_bowman","Arad Doman Bowman","Arad Doman Bowmen",tf_guarantee_all,0,0,fac_kingdom_9,
   [itm_short_bow, itm_arrows, itm_sword_secondary, itm_arad_doman_army_armor, itm_light_leather_boots, itm_leather_gloves, itm_nordic_archer_helmet],
   def_attrib_wot_infantry_2 ,wp_archery(90)|wp_one_handed(85)|wp(80),knows_wot_archer_2 ,arad_doman_man_face_young, arad_doman_man_face_older],
  
  ["arad_doman_man_at_arms","Arad Doman Man at Arms","Arad Doman Man at Arms",tf_guarantee_all_cavalry,0,0,fac_kingdom_9,
   [itm_sword_medieval_c_long, itm_arad_doman_shield_normal, itm_arad_doman_army_armor, itm_light_leather_boots, itm_leather_gloves, itm_nordic_archer_helmet, itm_courser, itm_hunter],
   def_attrib_wot_cavalry_3 ,wp_one_handed(135)|wp(100),knows_wot_cavalry_3 ,arad_doman_man_face_young, arad_doman_man_face_older],
#Other
  ["arad_doman_messenger","Arad Doman Messenger","Arad Doman Messengers",tf_guarantee_all_cavalry,0,0,fac_kingdom_9,
   [itm_sword_medieval_c_long, itm_arad_doman_shield_normal, itm_arad_doman_army_armor, itm_light_leather_boots, itm_leather_gloves, itm_nordic_archer_helmet, itm_courser, itm_hunter],
   def_attrib_wot_cavalry_3 ,wp_one_handed(135)|wp(100),knows_wot_cavalry_3 ,arad_doman_man_face_young, arad_doman_man_face_older],
  
  ["arad_doman_deserter","Arad Doman Deserter","Arad Doman Deserters",tf_guarantee_all,0,0,fac_kingdom_9,
   [itm_short_bow, itm_arrows, itm_sword_secondary, itm_arad_doman_army_armor, itm_light_leather_boots, itm_leather_gloves, itm_nordic_archer_helmet],
   def_attrib_wot_infantry_2 ,wp_archery(90)|wp_one_handed(85)|wp(80),knows_wot_archer_2 ,arad_doman_man_face_young, arad_doman_man_face_older],
  
  ["arad_doman_prison_guard","Prison Guard","Prison Guards",tf_guarantee_all_cavalry,0,0,fac_kingdom_9,
   [itm_sword_medieval_c_long, itm_arad_doman_shield_normal, itm_arad_doman_army_armor, itm_light_leather_boots, itm_leather_gloves, itm_nordic_archer_helmet, itm_courser, itm_hunter],
   def_attrib_wot_cavalry_3 ,wp_one_handed(135)|wp(100),knows_wot_cavalry_3 ,arad_doman_man_face_young, arad_doman_man_face_older],
  
  ["arad_doman_castle_guard","Castle Guard","Castle Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_9,
   [itm_sword_medieval_d_long, itm_arad_doman_shield_strong, itm_arad_doman_elite_armor, itm_splinted_greaves, itm_gauntlets, itm_nasal_helmet],
   def_attrib_wot_infantry_4 ,wp_one_handed(150)|wp(100),knows_wot_infantry_4, arad_doman_man_face_young, arad_doman_man_face_older],


# Southlander Alliance (2)

## Tear
  ["tear_blademaster","Tear Blademaster","Tear Blademasters",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_10,
   [itm_flamberge, itm_tear_gilded_plate, itm_shynbaulds_wot, itm_mail_gauntlets_wot, itm_tear_elite_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(180)|wp(100),knows_wot_infantry_4 ,tear_man_face_young, tear_man_face_old],
  
  ["tear_defender_captain","Tear Defender Captain","Tear Defender Captains",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_10,
   [itm_awlpike, itm_tear_defender_captain_armor, itm_black_greaves, itm_tear_defender_gauntlets, itm_tear_defender_helmet],
   def_attrib_wot_infantry_5 ,wp_polearm(175)|wp(150),knows_wot_infantry_5, tear_man_face_young, tear_man_face_old],
  
  ["tear_crossbowman","Tear Crossbowman","Tear Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_10,
   [itm_crossbow, itm_bolts, itm_sword_secondary, itm_tear_shield_normal, itm_tear_plate, itm_splinted_greaves_nospurs_wot, itm_leather_gloves, itm_tear_helmet],
   def_attrib_wot_infantry_3 ,wp_crossbow(125)|wp_one_handed(110)|wp(85),knows_wot_archer_3 ,tear_man_face_young, tear_man_face_old],
  
  ["tear_light_cavalry","Tear Light Cavalry","Tear Light Cavalry",tf_guarantee_all_cavalry,0,0,fac_kingdom_10,
   [itm_sword_medieval_b, itm_tear_shield_normal, itm_tear_plate, itm_splinted_greaves_spurs_wot, itm_leather_gloves, itm_tear_helmet, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_one_handed(115)|wp(85),knows_wot_cavalry_3 ,tear_man_face_young, tear_man_face_old],
   
  ["tear_heavy_lancer","Tear Heavy Lancer","Tear Heavy Lancers",tf_guarantee_all_cavalry,0,0,fac_kingdom_10,
   [itm_heavy_lance, itm_sword_medieval_c_long, itm_tear_shield_strong, itm_tear_gilded_plate, itm_gauntlets, itm_shynbaulds_wot, itm_tear_elite_helmet, itm_warhorse, itm_charger],
   def_attrib_wot_cavalry_4 ,wp_polearm(155)|wp_one_handed(120)|wp(100),knows_wot_cavalry_4 ,tear_man_face_young, tear_man_face_old],
#Other
  ["tear_messenger","Tear Messenger","Tear Messengers",tf_guarantee_all_cavalry,0,0,fac_kingdom_10,
   [itm_sword_medieval_b, itm_tear_shield_normal, itm_tear_plate, itm_splinted_greaves_spurs_wot, itm_leather_gloves, itm_tear_helmet, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_one_handed(115)|wp(85),knows_wot_cavalry_3 ,tear_man_face_young, tear_man_face_old],
  
  ["tear_deserter","Tear Deserter","Tear Deserters",tf_guarantee_all,0,0,fac_kingdom_10,
   [itm_crossbow, itm_bolts, itm_sword_secondary, itm_tear_shield_normal, itm_tear_plate, itm_splinted_greaves_nospurs_wot, itm_leather_gloves, itm_tear_helmet],
   def_attrib_wot_infantry_3 ,wp_crossbow(125)|wp_one_handed(110)|wp(85),knows_wot_archer_3 ,tear_man_face_young, tear_man_face_old],
  
  ["tear_prison_guard","Prison Guard","Prison Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_10,
   [itm_flamberge, itm_tear_gilded_plate, itm_shynbaulds_wot, itm_mail_gauntlets_wot, itm_tear_elite_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(180)|wp(100),knows_wot_infantry_4 ,tear_man_face_young, tear_man_face_old],
  
  ["tear_castle_guard","Castle Guard","Castle Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_10,
   [itm_awlpike, itm_tear_defender_captain_armor, itm_black_greaves, itm_tear_defender_gauntlets, itm_tear_defender_helmet],
   def_attrib_wot_infantry_5 ,wp_polearm(175)|wp(150),knows_wot_infantry_5, tear_man_face_young, tear_man_face_old],


## Andor
  ["andor_blademaster","Andor Blademaster","Andor Blademasters",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_11,
   [itm_sword_two_handed_a, itm_andor_plate, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_andoran_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(180)|wp(100),knows_wot_infantry_4 ,andor_man_face_young, andor_man_face_older],
  
  ["andor_halberdier","Andor Halberdier","Andor Halberdiers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_11,
   [itm_halberd, itm_andor_plate, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_andoran_helmet],
   def_attrib_wot_infantry_4 ,wp_polearm(180)|wp(100),knows_wot_infantry_4 ,andor_man_face_young, andor_man_face_older],
  
  ["andor_crossbowman","Andor Crossbowman","Andor Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_11,
   [itm_crossbow, itm_bolts, itm_sword_secondary, itm_andor_shield_normal, itm_andor_army_armor, itm_leather_boots, itm_leather_gloves, itm_nordic_helmet],
   def_attrib_wot_infantry_3 ,wp_crossbow(125)|wp_one_handed(110)|wp(85),knows_wot_archer_3 ,andor_man_face_young, andor_man_face_older],
  
  ["andor_man_at_arms","Andor Man at Arms","Andor Man at Arms",tf_guarantee_all_cavalry,0,0,fac_kingdom_11,
   [itm_one_handed_war_axe_b, itm_andor_shield_normal, itm_andor_army_armor, itm_leather_boots, itm_leather_gloves, itm_nordic_helmet, itm_courser, itm_hunter],
   def_attrib_wot_cavalry_3 ,wp_one_handed(120)|wp(85),knows_wot_cavalry_3 ,andor_man_face_young, andor_man_face_older],
  
  ["andor_bannerman","Andor Bannerman","Andor Bannermen",tf_guarantee_all_cavalry,0,0,fac_kingdom_11,
   [itm_heavy_lance, itm_sword_medieval_c_long, itm_andor_shield_strong, itm_andor_queens_guard_armor, itm_steel_greaves_wot, itm_wisby_gauntlets_red_wot, itm_sugarloaf_wot, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_4 ,wp_polearm(165)|wp_one_handed(120)|wp(85),knows_wot_cavalry_4 ,andor_man_face_young, andor_man_face_older],
#Other
  ["andor_messenger","Andor Messenger","Andor Messengers",tf_guarantee_all_cavalry,0,0,fac_kingdom_11,
   [itm_one_handed_war_axe_b, itm_andor_shield_normal, itm_andor_army_armor, itm_leather_boots, itm_leather_gloves, itm_nordic_helmet, itm_courser, itm_hunter],
   def_attrib_wot_cavalry_3 ,wp_one_handed(120)|wp(85),knows_wot_cavalry_3 ,andor_man_face_young, andor_man_face_older],
  
  ["andor_deserter","Andor Deserter","Andor Deserters",tf_guarantee_all_cavalry,0,0,fac_kingdom_11,
   [itm_one_handed_war_axe_b, itm_andor_shield_normal, itm_andor_army_armor, itm_leather_boots, itm_leather_gloves, itm_nordic_helmet, itm_courser, itm_hunter],
   def_attrib_wot_cavalry_3 ,wp_one_handed(120)|wp(85),knows_wot_cavalry_3 ,andor_man_face_young, andor_man_face_older],
  
  ["andor_prison_guard","Prison Guard","Prison Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_11,
   [itm_halberd, itm_andor_plate, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_andoran_helmet],
   def_attrib_wot_infantry_4 ,wp_polearm(180)|wp(100),knows_wot_infantry_4 ,andor_man_face_young, andor_man_face_older],
  
  ["andor_castle_guard","Castle Guard","Castle Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_11,
   [itm_sword_two_handed_a, itm_andor_plate, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_andoran_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(180)|wp(100),knows_wot_infantry_4 ,andor_man_face_young, andor_man_face_older],


## Ghealdan
  ["ghealdan_heavy_axeman","Ghealdan Heavy Axeman","Ghealdan Heavy Axemen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_12,
   [itm_long_axe_b, itm_ghealdan_plate, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_bascinet_2],
   def_attrib_wot_infantry_4 ,wp_two_handed(175)|wp(100),knows_wot_infantry_4 ,ghealdan_man_face_young, ghealdan_man_face_older],
  
  ["ghealdan_marksman","Ghealdan Marksman","Ghealdan Marksmen",tf_guarantee_all,0,0,fac_kingdom_12,
   [itm_war_bow, itm_bodkin_arrows, itm_sword_secondary, itm_ghealdan_army_armor, itm_leather_boots, itm_leather_gloves, itm_guard_helmet],
   def_attrib_wot_infantry_3 ,wp_archery(135)|wp_one_handed(110)|wp(95),knows_wot_archer_3, ghealdan_man_face_young, ghealdan_man_face_older],
  
  ["ghealdan_man_at_arms","Ghealdan Man at Arms","Ghealdan Man at Arms",tf_guarantee_all_cavalry,0,0,fac_kingdom_12,
   [itm_one_handed_battle_axe_b, itm_ghealdan_shield_normal, itm_ghealdan_army_armor, itm_leather_boots, itm_leather_gloves, itm_guard_helmet, itm_courser, itm_hunter],
   def_attrib_wot_cavalry_3 ,wp_one_handed(120)|wp(85),knows_wot_cavalry_3 ,ghealdan_man_face_young, ghealdan_man_face_older],
  
  ["ghealdan_royal_guard","Ghealdan Royal Guard","Ghealdan Royal Guards",tf_guarantee_all_cavalry,0,0,fac_kingdom_12,
   [itm_heavy_lance, itm_sword_medieval_c_long, itm_ghealdan_shield_strong, itm_ghealdan_plate, itm_steel_greaves_wot, itm_gauntlets, itm_bascinet_2, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_4 ,wp_polearm(165)|wp_one_handed(120)|wp(85),knows_wot_cavalry_4 ,ghealdan_man_face_young, ghealdan_man_face_older],
#Other
  ["ghealdan_messenger","Ghealdan Messenger","Ghealdan Messengers",tf_guarantee_all_cavalry,0,0,fac_kingdom_12,
   [itm_one_handed_battle_axe_b, itm_ghealdan_shield_normal, itm_ghealdan_army_armor, itm_leather_boots, itm_leather_gloves, itm_guard_helmet, itm_courser, itm_hunter],
   def_attrib_wot_cavalry_3 ,wp_one_handed(120)|wp(85),knows_wot_cavalry_3 ,ghealdan_man_face_young, ghealdan_man_face_older],
  
  ["ghealdan_deserter","Ghealdan Deserter","Ghealdan Deserters",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_12,
   [itm_one_handed_battle_axe_a, itm_ghealdan_shield_weak, itm_ghealdan_recruit_tunic, itm_footman_helmet, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2 ,wp_one_handed(100)|wp(70),knows_wot_infantry_2 ,ghealdan_man_face_young, ghealdan_man_face_older],
  
  ["ghealdan_prison_guard","Prison Guard","Prison Guards",tf_guarantee_all,0,0,fac_kingdom_12,
   [itm_war_bow, itm_bodkin_arrows, itm_sword_secondary, itm_ghealdan_army_armor, itm_leather_boots, itm_leather_gloves, itm_guard_helmet],
   def_attrib_wot_infantry_3 ,wp_archery(135)|wp_one_handed(110)|wp(95),knows_wot_archer_3, ghealdan_man_face_young, ghealdan_man_face_older],
  
  ["ghealdan_castle_guard","Castle Guard","Castle Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_12,
   [itm_long_axe_b, itm_ghealdan_plate, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_bascinet_2],
   def_attrib_wot_infantry_4 ,wp_two_handed(175)|wp(100),knows_wot_infantry_4 ,ghealdan_man_face_young, ghealdan_man_face_older],


## Far Madding
  ["far_madding_city_guard","Far Madding City Guard","Far Madding City Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_13,
   [itm_war_spear, itm_sword_medieval_c_long, itm_far_madding_shield_normal, itm_far_madding_armor, itm_mail_chausses, itm_leather_gloves, itm_bascinet_3],
   def_attrib_wot_infantry_3 ,wp_polearm(150)|wp(100),knows_wot_infantry_3 ,far_madding_man_face_young, far_madding_man_face_older],
  
  ["far_madding_crossbowman","Far Madding Crossbowman","Far Madding Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_13,
   [itm_crossbow, itm_bolts, itm_sword_secondary, itm_far_madding_shield_normal, itm_far_madding_armor, itm_mail_chausses, itm_leather_gloves, itm_bascinet_3],
   def_attrib_wot_infantry_3 ,wp_crossbow(125)|wp_one_handed(110)|wp(85),knows_wot_archer_3 ,far_madding_man_face_young, far_madding_man_face_older],
  #Other
  ["far_madding_messenger","Far Madding Messenger","Far Madding Messengers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_13,
   [itm_street_patrol_club, itm_far_madding_shield_weak, itm_far_madding_recruit_tunic, itm_leather_warrior_cap, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2 ,wp_one_handed(100)|wp(70),knows_wot_infantry_2 ,far_madding_man_face_young, far_madding_man_face_older],  
  
  ["far_madding_deserter","Far Madding Deserter","Far Madding Deserters",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_13,
   [itm_spear, itm_far_madding_recruit_tunic, itm_wrapping_boots],
   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1, far_madding_man_face_young, far_madding_man_face_older],
  
  ["far_madding_prison_guard","Prison Guard","Prison Guards",tf_guarantee_all,0,0,fac_kingdom_13,
   [itm_crossbow, itm_bolts, itm_sword_secondary, itm_far_madding_shield_normal, itm_far_madding_armor, itm_mail_chausses, itm_leather_gloves, itm_bascinet_3],
   def_attrib_wot_infantry_3 ,wp_crossbow(125)|wp_one_handed(110)|wp(85),knows_wot_archer_3 ,far_madding_man_face_young, far_madding_man_face_older],
  
  ["far_madding_castle_guard","Castle Guard","Castle Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_13,
   [itm_war_spear, itm_far_madding_shield_normal, itm_far_madding_armor, itm_mail_chausses, itm_leather_gloves, itm_bascinet_3],
   def_attrib_wot_infantry_3 ,wp_polearm(150)|wp(100),knows_wot_infantry_3 ,far_madding_man_face_young, far_madding_man_face_older],


## Tarabon
  ["tarabon_spearman","Tarabon Spearman","Tarabon Spearmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_14,
   [itm_war_spear, itm_tarabon_shield_normal, itm_tarabon_army_armor, itm_leather_boots, itm_leather_gloves, itm_vaegir_war_helmet],
   def_attrib_wot_infantry_3 ,wp_polearm(150)|wp(100),knows_wot_infantry_3 ,tarabon_man_face_young, tarabon_man_face_older],
  
  ["tarabon_marksman","Tarabon Marksman","Tarabon Marksmen",tf_guarantee_all,0,0,fac_kingdom_14,
   [itm_war_bow, itm_bodkin_arrows, itm_sword_secondary, itm_tarabon_army_armor, itm_leather_boots, itm_leather_gloves, itm_vaegir_war_helmet],
   def_attrib_wot_infantry_4 ,wp_archery(155)|wp_one_handed(125)|wp(105),knows_wot_archer_4, tarabon_man_face_young, tarabon_man_face_older],
  
  ["tarabon_lancer","Tarabon Lancer","Tarabon Lancers",tf_guarantee_all_cavalry,0,0,fac_kingdom_14,
   [itm_lance, itm_sword_medieval_c_long, itm_tarabon_shield_strong, itm_tarabon_elite_armor, itm_sarranid_boots_d, itm_scale_gauntlets, itm_sarranid_veiled_helmet, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_3 ,wp_polearm(150)|wp_one_handed(140)|wp(100),knows_wot_cavalry_3 ,tarabon_man_face_young, tarabon_man_face_older],
  
  ["tarabon_skirmisher","Tarabon Skirmisher","Tarabon Skirmishers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_14,
   [itm_khergit_bow, itm_arrows, itm_sword_secondary, itm_tarabon_elite_armor, itm_sarranid_boots_d, itm_leather_gloves, itm_sarranid_veiled_helmet, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_archery(145)|wp_one_handed(115)|wp(85),knows_wot_horse_archer_3 ,tarabon_man_face_young, tarabon_man_face_older],
  #Other
  ["tarabon_messenger","Tarabon Messenger","Tarabon Messengers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_14,
   [itm_khergit_bow, itm_arrows, itm_sword_secondary, itm_tarabon_elite_armor, itm_sarranid_boots_d, itm_leather_gloves, itm_sarranid_veiled_helmet, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_archery(145)|wp_one_handed(115)|wp(85),knows_wot_horse_archer_3 ,tarabon_man_face_young, tarabon_man_face_older], 
  
  ["tarabon_deserter","Tarabon Deserter","Tarabon Deserters",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_14,
   [itm_war_spear, itm_tarabon_shield_normal, itm_tarabon_army_armor, itm_leather_boots, itm_leather_gloves, itm_vaegir_war_helmet],
   def_attrib_wot_infantry_3 ,wp_polearm(150)|wp(100),knows_wot_infantry_3 ,tarabon_man_face_young, tarabon_man_face_older],
  
  ["tarabon_prison_guard","Prison Guard","Prison Guards",tf_guarantee_all,0,0,fac_kingdom_14,
   [itm_war_bow, itm_bodkin_arrows, itm_sword_secondary, itm_tarabon_army_armor, itm_leather_boots, itm_leather_gloves, itm_vaegir_war_helmet],
   def_attrib_wot_infantry_4 ,wp_archery(155)|wp_one_handed(125)|wp(105),knows_wot_archer_4, tarabon_man_face_young, tarabon_man_face_older],
  
  ["tarabon_castle_guard","Castle Guard","Castle Guards",tf_guarantee_all_cavalry,0,0,fac_kingdom_14,
   [itm_lance, itm_tarabon_shield_strong, itm_tarabon_elite_armor, itm_sarranid_boots_d, itm_scale_gauntlets, itm_sarranid_veiled_helmet, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_3 ,wp_polearm(150)|wp_one_handed(140)|wp(100),knows_wot_cavalry_3 ,tarabon_man_face_young, tarabon_man_face_older],


## Amadicia
  ["amadicia_captain","Amadicia Captain","Amadicia Captains",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_15,
   [itm_ashwood_pike, itm_amadicia_shield_strong, itm_amadicia_elite_armor, itm_shynbaulds_wot, itm_gauntlets, itm_flat_topped_helmet],
   def_attrib_wot_infantry_4 ,wp_polearm(180)|wp(100),knows_wot_infantry_4 ,amadicia_man_face_young, amadicia_man_face_older],
  
 ["amadicia_skirmisher","Amadicia Skirmisher","Amadicia Skirmishers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_15,
   [itm_khergit_bow, itm_arrows, itm_sword_secondary, itm_amadicia_army_armor, itm_leather_boots, itm_leather_gloves, itm_segmented_helmet, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_archery(150)|wp_one_handed(115)|wp(85),knows_wot_horse_archer_3 ,amadicia_man_face_young, amadicia_man_face_older],
  #Other
 ["amadicia_messenger","Amadicia Messenger","Amadicia Messengers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_15,
   [itm_khergit_bow, itm_arrows, itm_sword_secondary, itm_amadicia_army_armor, itm_leather_boots, itm_leather_gloves, itm_segmented_helmet, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_archery(150)|wp_one_handed(115)|wp(85),knows_wot_horse_archer_3 ,amadicia_man_face_young, amadicia_man_face_older],
  
  ["amadicia_deserter","Amadicia Deserter","Amadicia Deserters",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_15,
   [itm_spear, itm_amadicia_shield_weak, itm_amadicia_recruit_tunic, itm_black_hood, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2 ,wp_polearm(100)|wp(70),knows_wot_infantry_2 ,amadicia_man_face_young, amadicia_man_face_older],
  
  ["amadicia_prison_guard","Prison Guard","Prison Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_15,
   [itm_ashwood_pike, itm_amadicia_shield_strong, itm_amadicia_elite_armor, itm_shynbaulds_wot, itm_gauntlets, itm_flat_topped_helmet],
   def_attrib_wot_infantry_4 ,wp_polearm(180)|wp(100),knows_wot_infantry_4 ,amadicia_man_face_young, amadicia_man_face_older],
  
 ["amadicia_castle_guard","Castle Guard","Castle Guards",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_15,
   [itm_khergit_bow, itm_arrows, itm_sword_secondary, itm_amadicia_army_armor, itm_leather_boots, itm_leather_gloves, itm_segmented_helmet, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_archery(150)|wp_one_handed(115)|wp(85),knows_wot_horse_archer_3 ,amadicia_man_face_young, amadicia_man_face_older],


## Children of the Light
  ["whitecloak_captain","Whitecloak Captain","Whitecloak Captains",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_16,
   [itm_great_sword, itm_whitecloak_tabbard, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_whitecloak_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(175)|wp(100),knows_wot_infantry_4 ,man_face_young_1, man_face_old_2],

  ["whitecloak_crossbowman","Whitecloak Crossbowman","Whitecloak Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_16,
   [itm_crossbow, itm_bolts, itm_sword_secondary, itm_whitecloak_tabbard, itm_mail_chausses, itm_leather_gloves, itm_guard_helmet],
   def_attrib_wot_infantry_3 ,wp_crossbow(125)|wp_one_handed(110)|wp(85),knows_wot_archer_3 ,man_face_young_1, man_face_old_2],
  
  ["whitecloak_lancer","Whitecloak Lancer","Whitecloak Lancer",tf_guarantee_all_cavalry,0,0,fac_kingdom_16,
   [itm_heavy_lance, itm_sword_medieval_c_long, itm_whitecloak_shield_strong, itm_whitecloak_tabbard, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_whitecloak_helmet, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_4 ,wp_polearm(165)|wp_one_handed(140)|wp(100),knows_wot_cavalry_4 ,man_face_young_1, man_face_old_2],
  #Other
  ["whitecloak_messenger","Whitecloak Messenger","Whitecloak Messenger",tf_guarantee_all_cavalry,0,0,fac_kingdom_16,
   [itm_heavy_lance, itm_whitecloak_shield_strong, itm_whitecloak_tabbard, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_whitecloak_helmet, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_4 ,wp_polearm(165)|wp_one_handed(140)|wp(100),knows_wot_cavalry_4 ,man_face_young_1, man_face_old_2],
  
  ["whitecloak_deserter","Whitecloak Deserter","Whitecloak Deserters",tf_guarantee_all,0,0,fac_kingdom_16,
   [itm_crossbow, itm_bolts, itm_sword_secondary, itm_whitecloak_tabbard, itm_mail_chausses, itm_leather_gloves, itm_guard_helmet],
   def_attrib_wot_infantry_3 ,wp_crossbow(125)|wp_one_handed(110)|wp(85),knows_wot_archer_3 ,man_face_young_1, man_face_old_2],
  
  ["whitecloak_prison_guard","Prison Guard","Prison Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_16,
   [itm_sword_medieval_c_long, itm_whitecloak_shield_normal, itm_whitecloak_questioner_tabbard, itm_mail_chausses, itm_mail_mittens, itm_guard_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(135)|wp(100),knows_wot_infantry_3, man_face_young_1, man_face_old_2],
  
  ["whitecloak_castle_guard","Castle Guard","Castle Guard",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_16,
   [itm_great_sword, itm_whitecloak_tabbard, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_whitecloak_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(175)|wp(100),knows_wot_infantry_4 ,man_face_young_1, man_face_old_2],


# Borderlands

## Shienar
  ["shienar_pikeman","Shienar Pikeman","Shienar Pikemen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_17,
   [itm_ashwood_pike, itm_shienar_shield_strong, itm_banded_armor, itm_mail_chausses, itm_gauntlets, itm_nordic_warlord_helmet],
   def_attrib_wot_infantry_4 ,wp_polearm(155)|wp(100),knows_wot_infantry_4, shienar_man_face_young, shienar_man_face_older],
  
  ["shienar_blademaster","Shienar Blademaster","Shienar Blademasters",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_17,
   [itm_great_sword, itm_plate_armor, itm_steel_greaves_wot, itm_gauntlets, itm_great_helmet],
   def_attrib_wot_infantry_5 ,wp_two_handed(190)|wp(150),knows_wot_infantry_5, shienar_man_face_young, shienar_man_face_older],
  
  ["shienar_marksman","Shienar Marksman","Shienar Marksmen",tf_guarantee_all,0,0,fac_kingdom_17,
   [itm_war_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_sword_secondary, itm_mail_shirt, itm_mail_chausses, itm_leather_gloves, itm_nordic_fighter_helmet],
   def_attrib_wot_infantry_4 ,wp_archery(165)|wp_one_handed(140)|wp(120),knows_wot_archer_4, shienar_man_face_young, shienar_man_face_older],
  
  ["shienar_crossbowman","Shienar Crossbowman","Shienar Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_17,
   [itm_crossbow, itm_bolts, itm_sword_secondary, itm_shienar_shield_weak, itm_mail_shirt, itm_mail_chausses, itm_leather_gloves, itm_nordic_fighter_helmet],
   def_attrib_wot_infantry_4 ,wp_crossbow(165)|wp_one_handed(135)|wp(120),knows_wot_archer_4, shienar_man_face_young, shienar_man_face_older],
  
  ["shienar_captain","Shienar Captain","Shienar Captains",tf_guarantee_all_cavalry,0,0,fac_kingdom_17,
   [itm_heavy_lance, itm_sword_medieval_c_long, itm_shienar_shield_strong, itm_shienar_captain_armor, itm_steel_greaves_wot, itm_shienar_captain_gauntlets, itm_winged_great_helmet, itm_heavy_charger],
   def_attrib_wot_cavalry_5 ,wp_polearm(210)|wp_one_handed(175)|wp(150),knows_wot_cavalry_5 , shienar_man_face_young, shienar_man_face_older],
  #Other
  ["shienar_messenger","Shienar Messenger","Shienar Messengers",tf_guarantee_all_cavalry,0,0,fac_kingdom_17,
   [itm_sword_medieval_b, itm_shienar_shield_weak, itm_shienar_leather_armor, itm_leather_boots, itm_leather_gloves, itm_skullcap, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_one_handed(105)|wp(75),knows_wot_cavalry_2, shienar_man_face_young, shienar_man_face_older],  
  
  ["shienar_deserter","Shienar Deserter","Shienar Deserters",tf_guarantee_all,0,0,fac_kingdom_17,
   [itm_strong_bow, itm_arrows, itm_sword_secondary, itm_shienar_leather_armor, itm_leather_boots, itm_leather_gloves, itm_skullcap],
   def_attrib_wot_infantry_3 ,wp_archery(130)|wp_one_handed(120)|wp(80),knows_wot_archer_3, shienar_man_face_young, shienar_man_face_older],
  
  ["shienar_prison_guard","Prison Guard","Prison Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_17,
   [itm_ashwood_pike, itm_shienar_shield_strong, itm_banded_armor, itm_mail_chausses, itm_gauntlets, itm_nordic_warlord_helmet],
   def_attrib_wot_infantry_4 ,wp_polearm(155)|wp(100),knows_wot_infantry_4, shienar_man_face_young, shienar_man_face_older],
  
  ["shienar_castle_guard","Castle Guard","Castle Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_17,
   [itm_great_sword, itm_plate_armor, itm_steel_greaves_wot, itm_gauntlets, itm_great_helmet],
   def_attrib_wot_infantry_5 ,wp_two_handed(190)|wp(150),knows_wot_infantry_5, shienar_man_face_young, shienar_man_face_older],


## Arafel
  ["arafel_blademaster","Arafel Blademaster","Arafel Blademasters",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_18,
   [itm_sword_of_war, itm_arafel_mail_and_plate, itm_steel_greaves_wot, itm_gauntlets, itm_oniontop_bascinet_wot],
   def_attrib_wot_infantry_4 ,wp_two_handed(180)|wp(150),knows_wot_infantry_4, arafel_man_face_young, arafel_man_face_older],
  
  ["arafel_bannerman","Arafel Bannerman","Arafel Bannermen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_18,
   [itm_poleaxe, itm_arafel_mail_and_plate, itm_steel_greaves_wot, itm_gauntlets, itm_oniontop_bascinet_wot],
   def_attrib_wot_infantry_5 ,wp_polearm(195)|wp(150),knows_wot_infantry_5, arafel_man_face_young, arafel_man_face_older],
  
  ["arafel_marksman","Arafel Marksman","Arafel Marksmen",tf_guarantee_all,0,0,fac_kingdom_18,
   [itm_war_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_sword_secondary, itm_mamluke_mail, itm_mail_chausses, itm_leather_gloves, itm_segmented_helmet],
   def_attrib_wot_infantry_4 ,wp_archery(165)|wp_one_handed(140)|wp(120),knows_wot_archer_4, arafel_man_face_young, arafel_man_face_older],
  
  ["arafel_lancer","Arafel Lancer","Arafel Lancers",tf_guarantee_all_cavalry,0,0,fac_kingdom_18,
   [itm_lance, itm_sword_medieval_c_long, itm_arafel_shield_strong, itm_arafel_tabbard, itm_splinted_greaves_spurs_wot, itm_mail_mittens, itm_guard_helmet, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_4 ,wp_polearm(150)|wp(75),knows_wot_cavalry_4, arafel_man_face_young, arafel_man_face_older],
  
  ["arafel_skirmisher","Arafel Skirmisher","Arafel Skirmishers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_18,
   [itm_khergit_bow, itm_arrows, itm_sword_secondary, itm_mamluke_mail, itm_mail_chausses, itm_leather_gloves, itm_segmented_helmet, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_archery(165)|wp_one_handed(120)|wp(85),knows_wot_horse_archer_3 ,arafel_man_face_young, arafel_man_face_older],
  #Other
  ["arafel_messenger","Arafel Messenger","Arafel Messengers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_18,
   [itm_khergit_bow, itm_arrows, itm_sword_secondary, itm_mamluke_mail, itm_mail_chausses, itm_leather_gloves, itm_segmented_helmet, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_archery(165)|wp_one_handed(120)|wp(85),knows_wot_horse_archer_3 ,arafel_man_face_young, arafel_man_face_older],  
  
  ["arafel_deserter","Arafel Deserter","Arafel Deserters",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_18,
   [itm_mace_1, itm_arafel_recruit_tunic, itm_leather_boots, itm_footman_helmet],
   def_attrib_wot_infantry_1 ,wp(75),knows_wot_infantry_1, arafel_man_face_young, arafel_man_face_older],
  
  ["arafel_prison_guard","Prison Guard","Prison Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_18,
   [itm_sword_of_war, itm_arafel_mail_and_plate, itm_steel_greaves_wot, itm_gauntlets, itm_oniontop_bascinet_wot],
   def_attrib_wot_infantry_4 ,wp_two_handed(180)|wp(150),knows_wot_infantry_4, arafel_man_face_young, arafel_man_face_older],
  
  ["arafel_castle_guard","Castle Guard","Castle Guards",tf_guarantee_all,0,0,fac_kingdom_18,
   [itm_war_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_sword_secondary, itm_mamluke_mail, itm_mail_chausses, itm_leather_gloves, itm_segmented_helmet],
   def_attrib_wot_infantry_4 ,wp_archery(165)|wp_one_handed(140)|wp(120),knows_wot_archer_4, arafel_man_face_young, arafel_man_face_older],


## Kandor
  ["kandor_captain","Kandor Captain","Kandor Captains",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_19,
   [itm_long_axe_c, itm_coat_of_plates, itm_plate_boots, itm_gauntlets, itm_kandor_visored_sallet],
   def_attrib_wot_infantry_5 ,wp_two_handed(180)|wp(150),knows_wot_infantry_5, kandor_man_face_young, kandor_man_face_older],
  
  ["kandor_maceman","Kandor Maceman","Kandor Macemen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_19,
   [itm_kandor_long_mace,itm_kandor_surcoat, itm_mail_chausses, itm_mail_mittens, itm_vaegir_lamellar_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(150)|wp(100),knows_wot_infantry_4, kandor_man_face_young, kandor_man_face_older],
  
  ["kandor_crossbowman","Kandor Crossbowman","Kandor Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_19,
   [itm_crossbow, itm_bolts, itm_sword_secondary, itm_kandor_shield_weak, itm_kandor_leather_armor, itm_vaegir_fur_helmet, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_4 ,wp_crossbow(165)|wp_one_handed(130)|wp(120),knows_wot_archer_4, kandor_man_face_young, kandor_man_face_older],
  
  ["kandor_heavy_horseman","Kandor Heavy Horseman","Kandor Heavy Horsemen",tf_guarantee_all_cavalry,0,0,fac_kingdom_19,
   [itm_one_handed_battle_axe_c, itm_kandor_shield_strong, itm_kandor_surcoat, itm_mail_chausses, itm_mail_mittens, itm_vaegir_lamellar_helmet, itm_warhorse, itm_charger],
   def_attrib_wot_cavalry_4 ,wp_one_handed(165)|wp(125),knows_wot_cavalry_4, kandor_man_face_young, kandor_man_face_older],
  
  ["kandor_skirmisher","Kandor Skirmisher","Kandor Skirmishers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_19,
   [itm_khergit_bow, itm_arrows, itm_sword_secondary, itm_kandor_army_armor, itm_splinted_leather_greaves, itm_leather_gloves, itm_vaegir_spiked_helmet, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_archery(165)|wp_one_handed(120)|wp(85),knows_wot_horse_archer_3 ,kandor_man_face_young, kandor_man_face_older],
  #Other
  ["kandor_messenger","Kandor Messenger","Kandor Messengers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_19,
   [itm_khergit_bow, itm_arrows, itm_sword_secondary, itm_kandor_army_armor, itm_splinted_leather_greaves, itm_leather_gloves, itm_vaegir_spiked_helmet, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_archery(165)|wp_one_handed(120)|wp(85),knows_wot_horse_archer_3 ,kandor_man_face_young, kandor_man_face_older],
  
  ["kandor_deserter","Kandor Deserter","Kandor Deserters",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_19,
   [itm_kandor_long_mace,itm_kandor_surcoat, itm_mail_chausses, itm_mail_mittens, itm_vaegir_lamellar_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(150)|wp(100),knows_wot_infantry_4, kandor_man_face_young, kandor_man_face_older],
  
  ["kandor_prison_guard","Prison Guard","Prison Guards",tf_guarantee_all_cavalry,0,0,fac_kingdom_19,
   [itm_one_handed_battle_axe_c, itm_kandor_shield_strong, itm_kandor_surcoat, itm_mail_chausses, itm_mail_mittens, itm_vaegir_lamellar_helmet, itm_warhorse, itm_charger],
   def_attrib_wot_cavalry_4 ,wp_one_handed(165)|wp(125),knows_wot_cavalry_4, kandor_man_face_young, kandor_man_face_older],
  
  ["kandor_castle_guard","Castle Guard","Castle Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_19,
   [itm_long_axe_c, itm_coat_of_plates, itm_plate_boots, itm_gauntlets, itm_kandor_visored_sallet],
   def_attrib_wot_infantry_5 ,wp_two_handed(180)|wp(150),knows_wot_infantry_5, kandor_man_face_young, kandor_man_face_older],


## Saldaea
  ["saldaea_bannerman","Saldaea Bannerman","Saldaea Bannermen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_20,
   [itm_khergit_sword_two_handed_b, itm_heavy_lamellar_armor_wot, itm_khergit_cavalry_helmet, itm_splinted_greaves, itm_lamellar_gauntlets],
   def_attrib_wot_infantry_4 ,wp_two_handed(165)|wp(100),knows_wot_infantry_4, saldaea_man_face_young, saldaea_man_face_older],
  
  ["saldaea_halberdier","Saldaea Halberdier","Saldaea Halberdiers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_20,
   [itm_poleaxe, itm_saldaea_army_armor, itm_leather_boots, itm_leather_gloves, itm_leather_steppe_cap_c],
   def_attrib_wot_infantry_4 ,wp_polearm(155)|wp(120),knows_wot_infantry_4, saldaea_man_face_young, saldaea_man_face_older],
  
  ["saldaea_marksman","Saldaea Marksman","Saldaea Marksmen",tf_guarantee_all,0,0,fac_kingdom_20,
   [itm_war_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_sword_secondary, itm_saldaea_army_armor, itm_leather_boots, itm_leather_gloves, itm_leather_steppe_cap_c],
   def_attrib_wot_infantry_4 ,wp_archery(165)|wp_one_handed(150)|wp(120),knows_wot_archer_4, saldaea_man_face_young, saldaea_man_face_older],
  
  ["saldaea_quartermaster","Saldaea Squad Leader","Saldaea Squad Leaders",tf_guarantee_all_cavalry,0,0,fac_kingdom_20,
   [itm_sword_khergit_4, itm_saldaea_shield_strong, itm_vaegir_elite_armor, itm_khergit_guard_helmet, itm_splinted_greaves, itm_lamellar_gauntlets, itm_saldaea_charger],
   def_attrib_wot_cavalry_5 ,wp_one_handed(180)|wp(125),knows_wot_cavalry_5, saldaea_man_face_young, saldaea_man_face_older],
  
  ["saldaea_elite_skirmisher","Saldaea Elite Skirmisher","Saldaea Elite Skirmishers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_20,
   [itm_khergit_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_sword_secondary, itm_heavy_lamellar_armor_wot, itm_khergit_cavalry_helmet, itm_splinted_greaves, itm_lamellar_gauntlets, itm_saldaea_warhorse],
   def_attrib_wot_cavalry_4 ,wp_archery(180)|wp_one_handed(150)|wp(85),knows_wot_horse_archer_4 ,saldaea_man_face_young, saldaea_man_face_older],
#Other
  ["saldaea_messenger","Saldaea Messenger","Saldaea Messengers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_20,
   [itm_khergit_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_sword_secondary, itm_heavy_lamellar_armor_wot, itm_khergit_cavalry_helmet, itm_splinted_greaves, itm_lamellar_gauntlets, itm_saldaea_warhorse],
   def_attrib_wot_cavalry_4 ,wp_archery(180)|wp_one_handed(150)|wp(85),knows_wot_horse_archer_4 ,saldaea_man_face_young, saldaea_man_face_older],
  
  ["saldaea_deserter","Saldaea Deserter","Saldaea Deserters",tf_guarantee_all,0,0,fac_kingdom_20,
   [itm_war_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_sword_secondary, itm_saldaea_army_armor, itm_leather_boots, itm_leather_gloves, itm_leather_steppe_cap_c],
   def_attrib_wot_infantry_4 ,wp_archery(165)|wp_one_handed(150)|wp(120),knows_wot_archer_4, saldaea_man_face_young, saldaea_man_face_older],
  
  ["saldaea_prison_guard","Prison Guard","Prison Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_20,
   [itm_poleaxe, itm_saldaea_army_armor, itm_leather_boots, itm_leather_gloves, itm_leather_steppe_cap_c],
   def_attrib_wot_infantry_4 ,wp_polearm(155)|wp(120),knows_wot_infantry_4, saldaea_man_face_young, saldaea_man_face_older],
  
  ["saldaea_castle_guard","Castle Guard","Castle Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_20,
   [itm_khergit_sword_two_handed_b, itm_heavy_lamellar_armor_wot, itm_khergit_cavalry_helmet, itm_splinted_greaves, itm_lamellar_gauntlets],
   def_attrib_wot_infantry_4 ,wp_two_handed(165)|wp(100),knows_wot_infantry_4, saldaea_man_face_young, saldaea_man_face_older],


# White Tower
  
  ["aes_sedai_yellow_veteran","Aes Sedai Yellow Veteran","Aes Sedai Yellow Veterans",tf_female|tf_mounted|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_yellow_dress, itm_veteran_aes_sedai_yellow_shoes, itm_courser], # , itm_wig_black_bun
   def_attrib|level(20),wp_firearm(195)|wp_one_handed(110)|wp(90),knows_common|knows_power_draw_5|knows_riding_2|knows_fire_6|knows_earth_5|knows_spirit_6|knows_water_7|knows_air_7,tar_valon_woman_face_middle, cairhien_woman_face_older],
  
  ["aes_sedai_brown_veteran","Aes Sedai Brown Veteran","Aes Sedai Brown Veterans",tf_female|tf_mounted|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_brown_dress, itm_veteran_aes_sedai_brown_shoes, itm_courser], # , itm_wig_brown_bun
   def_attrib|level(20),wp_firearm(195)|wp_one_handed(110)|wp(90),knows_common|knows_power_draw_5|knows_riding_2|knows_fire_6|knows_earth_5|knows_spirit_6|knows_water_7|knows_air_7,tar_valon_woman_face_middle, andor_woman_face_older],
  
  ["aes_sedai_white_veteran","Aes Sedai White Veteran","Aes Sedai White Veterans",tf_female|tf_mounted|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_white_dress, itm_veteran_aes_sedai_white_shoes, itm_courser], # , itm_wig_red_bun
   def_attrib|level(20),wp_firearm(195)|wp_one_handed(110)|wp(90),knows_common|knows_power_draw_5|knows_riding_2|knows_fire_6|knows_earth_5|knows_spirit_6|knows_water_7|knows_air_7,tar_valon_woman_face_middle, aiel_1_woman_face_older],
  
  ["aes_sedai_blue_veteran","Aes Sedai Blue Veteran","Aes Sedai Blue Veterans",tf_female|tf_mounted|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_blue_dress, itm_veteran_aes_sedai_blue_shoes, itm_courser], # , itm_wig_white_longer
   def_attrib|level(20),wp_firearm(195)|wp_one_handed(110)|wp(90),knows_common|knows_power_draw_5|knows_riding_2|knows_fire_6|knows_earth_5|knows_spirit_6|knows_water_7|knows_air_7,tar_valon_woman_face_middle, aiel_2_woman_face_older],
  
  ["aes_sedai_grey_veteran","Aes Sedai Grey Veteran","Aes Sedai Grey Veteran",tf_female|tf_mounted|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_grey_dress, itm_veteran_aes_sedai_grey_shoes, itm_courser], # , itm_wig_white_bun
   def_attrib|level(20),wp_firearm(195)|wp_one_handed(110)|wp(90),knows_common|knows_power_draw_5|knows_riding_2|knows_fire_6|knows_earth_5|knows_spirit_6|knows_water_7|knows_air_7,tar_valon_woman_face_middle, seanchan_1_woman_face_older],
  
  ["aes_sedai_red_veteran","Aes Sedai Red Veteran","Aes Sedai Red Veteran",tf_female|tf_mounted|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_red_dress, itm_veteran_aes_sedai_red_shoes, itm_courser], # , itm_wig_brown_short
   def_attrib|level(20),wp_firearm(195)|wp_one_handed(110)|wp(90),knows_common|knows_power_draw_5|knows_riding_2|knows_fire_6|knows_earth_5|knows_spirit_7|knows_water_7|knows_air_7,tar_valon_woman_face_middle, seanchan_2_woman_face_older],
  
  ["aes_sedai_green_veteran","Aes Sedai Green Veteran","Aes Sedai Green Veterans",tf_female|tf_mounted|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_green_dress, itm_veteran_aes_sedai_green_shoes, itm_courser], # , itm_wig_red_long
   def_attrib|level(20),wp_firearm(195)|wp_one_handed(110)|wp(90),knows_common|knows_power_draw_5|knows_riding_2|knows_fire_6|knows_earth_6|knows_spirit_6|knows_water_7|knows_air_7,tar_valon_woman_face_middle, saldaea_woman_face_older],
  
  ["tower_guard_captain","Tower Guard Captain","Tower Guard Captains",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_21,
   [itm_great_sword, itm_sword_viking_2_small, itm_white_tower_captain_armor, itm_guard_helmet, itm_splinted_leather_greaves, itm_leather_gloves],
   def_attrib_wot_infantry_3,wp_one_handed(150)|wp(100),knows_wot_infantry_3,tar_valon_man_face_middle, tar_valon_man_face_older],

  ["tower_guard_crossbowman","Tower Guard Crossbowman","Tower Guard Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_crossbow, itm_bolts, itm_sword_medieval_a, itm_white_tower_guard_armor, itm_segmented_helmet, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2 ,wp_crossbow(125)|wp_one_handed(110)|wp(90),knows_wot_archer_2 ,tar_valon_man_face_young, tar_valon_man_face_old],
  
  ["youngling_infantry","Youngling Infantry","Youngling Infantry",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_21,
   [itm_sword_viking_3_small, itm_trainee_gambeson, itm_segmented_helmet, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2 ,wp_one_handed(125)|wp(90),knows_wot_infantry_2 ,tar_valon_man_face_younger, tar_valon_man_face_young],
  
  ["warder","Warder","Warders",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_21,
   [itm_great_sword, itm_flamberge, itm_bastard_sword_b, itm_sword_medieval_c_small, itm_mayene_sword, itm_sarranid_elite_armor, itm_lamellar_vest, itm_scale_armor, itm_vaegir_war_helmet, itm_vaegir_lamellar_helmet, itm_splinted_leather_greaves, itm_scale_gauntlets],
   def_attrib_wot_infantry_4 ,wp_two_handed(150)|wp(90),knows_wot_infantry_4 ,tar_valon_man_face_young, andor_man_face_old],
  
  ["warder_veteran","Warder Veteran","Warder Veterans",tf_guarantee_all_cavalry,0,0,fac_kingdom_21,
   [itm_great_sword, itm_sword_viking_2_small, itm_flamberge, itm_khergit_sword_two_handed_b, itm_large_heron_mark_blade, itm_heron_mark_blade, itm_khergit_elite_armor, itm_banded_armor, itm_vaegir_elite_armor, itm_khergit_guard_helmet, itm_vaegir_war_helmet, itm_splinted_greaves, itm_lamellar_gauntlets,itm_hunter],
   def_attrib_wot_cavalry_4 ,wp_one_handed(150)|wp_two_handed(175)|wp(100),knows_wot_cavalry_4 ,tar_valon_man_face_middle, shienar_man_face_older],

  ["youngling_cavalry","Youngling Cavalry","Youngling Cavalry",tf_guarantee_all_cavalry,0,0,fac_kingdom_21,
   [itm_lance, itm_sword_viking_3_small, itm_trainee_gambeson, itm_segmented_helmet, itm_leather_boots, itm_leather_gloves,itm_courser],
   def_attrib_wot_cavalry_2,wp_one_handed(115)|wp_polearm(125)|wp(90),knows_wot_cavalry_2,tar_valon_man_face_younger, tar_valon_man_face_young],

  ["aes_sedai_yellow_warder","Aes Sedai Yellow","Aes Sedai Yellows",tf_female|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_yellow_dress, itm_aes_sedai_yellow_shoes], # , itm_wig_black_long
   def_attrib|level(15),wp_firearm(175)|wp_one_handed(110)|wp(80),knows_common|knows_power_draw_4|knows_fire_5|knows_earth_4|knows_spirit_5|knows_water_6|knows_air_6,tar_valon_woman_face_younger, illian_woman_face_middle],
    
  ["aes_sedai_brown_warder","Aes Sedai Brown","Aes Sedai Browns",tf_female|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_brown_dress, itm_aes_sedai_brown_shoes], # , itm_wig_red_bun
   def_attrib|level(15),wp_firearm(175)|wp_one_handed(110)|wp(80),knows_common|knows_power_draw_4|knows_fire_5|knows_earth_4|knows_spirit_5|knows_water_6|knows_air_6,tar_valon_woman_face_young, altara_woman_face_old],
  
  ["aes_sedai_white_warder","Aes Sedai White","Aes Sedai Whites",tf_female|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_white_dress, itm_aes_sedai_white_shoes], # , itm_wig_black_long
   def_attrib|level(15),wp_firearm(175)|wp_one_handed(110)|wp(80),knows_common|knows_power_draw_4|knows_fire_5|knows_earth_4|knows_spirit_5|knows_water_6|knows_air_6,tar_valon_woman_face_young, ghealdan_woman_face_old],
    
  ["aes_sedai_blue_warder","Aes Sedai Blue","Aes Sedai Blues",tf_female|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_blue_dress, itm_aes_sedai_blue_shoes], # , itm_wig_blond_braid
   def_attrib|level(15),wp_firearm(175)|wp_one_handed(110)|wp(80),knows_common|knows_power_draw_4|knows_fire_5|knows_earth_4|knows_spirit_5|knows_water_6|knows_air_6,tar_valon_woman_face_young, arad_doman_woman_face_old],
  
  ["aes_sedai_grey_warder","Aes Sedai Grey","Aes Sedai Greys",tf_female|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_grey_dress, itm_aes_sedai_grey_shoes], # , itm_wig_red_braid
   def_attrib|level(15),wp_firearm(175)|wp_one_handed(110)|wp(80),knows_common|knows_power_draw_4|knows_fire_5|knows_earth_4|knows_spirit_5|knows_water_6|knows_air_6,tar_valon_woman_face_young, saldaea_woman_face_old],
    
  ["aes_sedai_red_warder","Aes Sedai Red","Aes Sedai Reds",tf_female|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_red_dress, itm_aes_sedai_red_shoes], # , itm_wig_brown_bun
   def_attrib|level(15),wp_firearm(175)|wp_one_handed(110)|wp(80),knows_common|knows_power_draw_4|knows_fire_5|knows_earth_4|knows_spirit_6|knows_water_6|knows_air_6,tar_valon_woman_face_young, arafel_woman_face_old],
  
  ["aes_sedai_green_warder","Aes Sedai Green","Aes Sedai Greens",tf_female|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_green_dress, itm_aes_sedai_green_shoes], # , itm_wig_red_long
   def_attrib|level(15),wp_firearm(175)|wp_one_handed(110)|wp(80),knows_common|knows_power_draw_4|knows_fire_5|knows_earth_6|knows_spirit_5|knows_water_6|knows_air_6,tar_valon_woman_face_young, shienar_woman_face_old],

  ["aes_sedai_yellow_veteran_warder","Aes Sedai Yellow Veteran","Aes Sedai Yellow Veterans",tf_female|tf_mounted|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_yellow_dress, itm_veteran_aes_sedai_yellow_shoes, itm_courser], # , itm_wig_black_bun
   def_attrib|level(20),wp_firearm(195)|wp_one_handed(110)|wp(90),knows_common|knows_power_draw_5|knows_riding_2|knows_fire_6|knows_earth_5|knows_spirit_6|knows_water_7|knows_air_7,tar_valon_woman_face_middle, cairhien_woman_face_older],
  
  ["aes_sedai_brown_veteran_warder","Aes Sedai Brown Veteran","Aes Sedai Brown Veterans",tf_female|tf_mounted|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_brown_dress, itm_veteran_aes_sedai_brown_shoes, itm_courser], # , itm_wig_brown_bun
   def_attrib|level(20),wp_firearm(195)|wp_one_handed(110)|wp(90),knows_common|knows_power_draw_5|knows_riding_2|knows_fire_6|knows_earth_5|knows_spirit_6|knows_water_7|knows_air_7,tar_valon_woman_face_middle, andor_woman_face_older],
  
  ["aes_sedai_white_veteran_warder","Aes Sedai White Veteran","Aes Sedai White Veterans",tf_female|tf_mounted|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_white_dress, itm_veteran_aes_sedai_white_shoes, itm_courser], # , itm_wig_red_bun
   def_attrib|level(20),wp_firearm(195)|wp_one_handed(110)|wp(90),knows_common|knows_power_draw_5|knows_riding_2|knows_fire_6|knows_earth_5|knows_spirit_6|knows_water_7|knows_air_7,tar_valon_woman_face_middle, aiel_1_woman_face_older],
  
  ["aes_sedai_blue_veteran_warder","Aes Sedai Blue Veteran","Aes Sedai Blue Veterans",tf_female|tf_mounted|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_blue_dress, itm_veteran_aes_sedai_blue_shoes, itm_courser], # , itm_wig_white_longer
   def_attrib|level(20),wp_firearm(195)|wp_one_handed(110)|wp(90),knows_common|knows_power_draw_5|knows_riding_2|knows_fire_6|knows_earth_5|knows_spirit_6|knows_water_7|knows_air_7,tar_valon_woman_face_middle, aiel_2_woman_face_older],
  
  ["aes_sedai_grey_veteran_warder","Aes Sedai Grey Veteran","Aes Sedai Grey Veteran",tf_female|tf_mounted|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_grey_dress, itm_veteran_aes_sedai_grey_shoes, itm_courser], # , itm_wig_white_bun
   def_attrib|level(20),wp_firearm(195)|wp_one_handed(110)|wp(90),knows_common|knows_power_draw_5|knows_riding_2|knows_fire_6|knows_earth_5|knows_spirit_6|knows_water_7|knows_air_7,tar_valon_woman_face_middle, seanchan_1_woman_face_older],
  
  ["aes_sedai_red_veteran_warder","Aes Sedai Red Veteran","Aes Sedai Red Veteran",tf_female|tf_mounted|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_red_dress, itm_veteran_aes_sedai_red_shoes, itm_courser], # , itm_wig_brown_short
   def_attrib|level(20),wp_firearm(195)|wp_one_handed(110)|wp(90),knows_common|knows_power_draw_5|knows_riding_2|knows_fire_6|knows_earth_5|knows_spirit_7|knows_water_7|knows_air_7,tar_valon_woman_face_middle, seanchan_2_woman_face_older],
  
  ["aes_sedai_green_veteran_warder","Aes Sedai Green Veteran","Aes Sedai Green Veterans",tf_female|tf_mounted|tf_guarantee_all,0,0,fac_kingdom_21,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_green_dress, itm_veteran_aes_sedai_green_shoes, itm_courser], # , itm_wig_red_long
   def_attrib|level(20),wp_firearm(195)|wp_one_handed(110)|wp(90),knows_common|knows_power_draw_5|knows_riding_2|knows_fire_6|knows_earth_6|knows_spirit_6|knows_water_7|knows_air_7,tar_valon_woman_face_middle, saldaea_woman_face_older],
#Other
  ["sedai_messenger","White Tower Messenger","White Tower Messengers",tf_guarantee_all_cavalry,0,0,fac_kingdom_21,
   [itm_lance, itm_sword_viking_3_small, itm_white_tower_guard_armor, itm_segmented_helmet, itm_leather_boots, itm_leather_gloves,itm_courser],
   def_attrib_wot_cavalry_2,wp_one_handed(115)|wp_polearm(125)|wp(90),knows_wot_cavalry_2,tar_valon_man_face_younger, tar_valon_man_face_young],
  
  ["sedai_deserter","White Tower Deserter","White Tower Deserters",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_21,
   [itm_sword_viking_3_small, itm_trainee_gambeson, itm_segmented_helmet, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_3 ,wp_one_handed(125)|wp(90),knows_wot_infantry_3 ,tar_valon_man_face_younger, tar_valon_man_face_young],
  
  ["sedai_prison_guard","Prison Guard","Prison Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_21,
   [itm_great_sword, itm_sword_viking_2_small, itm_white_tower_captain_armor, itm_guard_helmet, itm_splinted_leather_greaves, itm_leather_gloves],
   def_attrib_wot_infantry_4 ,wp_one_handed(150)|wp(100),knows_wot_infantry_4 ,tar_valon_man_face_middle, tar_valon_man_face_older],

  ["sedai_castle_guard","Castle Guard","Castle Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_21,
   [itm_great_sword, itm_sword_viking_2_small, itm_white_tower_captain_armor, itm_guard_helmet, itm_splinted_leather_greaves, itm_leather_gloves],
   def_attrib_wot_infantry_4 ,wp_one_handed(150)|wp(100),knows_wot_infantry_4 ,tar_valon_man_face_middle, tar_valon_man_face_older],


# Aiel Nation

  ["wise_one_dream_walker","Wise One Dream Walker","Wise One Dream Walkers",tf_female|tf_guarantee_all,0,0,fac_kingdom_22,
   [itm_power_player, itm_power_ammo, itm_wise_one_dress_with_shawl, itm_cadinsor_boots],
   def_attrib|level(20),wp_firearm(195)|wp_one_handed(125)|wp(90),knows_common|knows_power_draw_5|knows_fire_7|knows_earth_5|knows_spirit_7|knows_water_6|knows_air_7, aiel_1_woman_face_middle, aiel_2_woman_face_older],
  
  ["knife_hand","Knife Hand","Knife Hands",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_22,
   [itm_aiel_knife, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_4 ,wp_one_handed(185)|wp(120),knows_wot_super_infantry_4 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  
  ["night_spear","Night Spear","Night Spears",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_22,
   [itm_aiel_spear, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_4 ,wp_polearm(190)|wp(120),knows_wot_super_infantry_4 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  
  ["dawn_runner","Dawn Runner","Dawn Runners",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_22,
   [itm_aiel_spear, itm_aiel_knife, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_4 ,wp_polearm(190)|wp_one_handed(140)|wp(120),knows_wot_super_infantry_4 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  
  ["mountain_dancer","Mountain Dancer","Mountain Dancers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_22,
   [itm_aiel_spear, itm_hide_buckler_strong, itm_aiel_knife, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_4 ,wp_polearm(190)|wp_one_handed(140)|wp(120),knows_wot_super_infantry_4 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  
  ["maiden_of_the_spear","Maiden of the Spear","Maidens of the Spear",tf_female|tf_guarantee_all,0,0,fac_kingdom_22,
   [itm_khergit_bow, itm_arrows, itm_arrows, itm_aiel_knife, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_4 ,wp_archery(190)|wp_one_handed(140)|wp(120),knows_wot_super_infantry_4 ,aiel_1_woman_face_younger, aiel_2_woman_face_old],
  
  ["water_seeker","Water Seeker","Water Seekers",tf_guarantee_all,0,0,fac_kingdom_22,
   [itm_khergit_bow, itm_arrows, itm_arrows, itm_aiel_spear, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_4 ,wp_archery(190)|wp_polearm(140)|wp(120),knows_wot_super_infantry_4 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  
  ["stone_dog","Stone Dog","Stone Dogs",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_22,
   [itm_javelin, itm_aiel_spear, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_5 ,wp_throwing(190)|wp_polearm(175)|wp(120),knows_wot_super_infantry_5 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  
  ["red_shield","Red Shield","Red Shields",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_22,
   [itm_aiel_spear, itm_hide_buckler_strong, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_5 ,wp_polearm(190)|wp(120),knows_wot_super_infantry_5 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  
  ["brother_of_the_eagle","Brother of the Eagle","Brothers of the Eagle",tf_guarantee_all,0,0,fac_kingdom_22,
   [itm_khergit_bow, itm_arrows, itm_arrows, itm_aiel_knife, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_5 ,wp_archery(195)|wp_one_handed(160)|wp(130),knows_wot_super_infantry_5 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  
  ["brotherless","Brotherless","Brotherless",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_22,
   [itm_aiel_spear, itm_hide_buckler_strong, itm_aiel_knife, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_5 ,wp_polearm(200)|wp_one_handed(160)|wp(130),knows_wot_super_infantry_5 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  
  ["black_eye","Black Eye","Black Eyes",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_22,
   [itm_javelin, itm_aiel_spear, itm_hide_buckler_strong, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_5 ,wp_throwing(185)|wp_polearm(160)|wp(130),knows_wot_super_infantry_5 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  
  ["true_blood","True Blood","True Bloods",tf_guarantee_all,0,0,fac_kingdom_22,
   [itm_khergit_bow, itm_arrows, itm_arrows, itm_aiel_spear, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_5 ,wp_archery(195)|wp_polearm(160)|wp(130),knows_wot_super_infantry_5 ,aiel_1_man_face_younger, aiel_2_man_face_old],
#Other
  ["aiel_messenger","Aiel Messenger","Aiel Messengers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_22,
   [itm_aiel_spear, itm_aiel_knife, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_4 ,wp_polearm(190)|wp_one_handed(140)|wp(120),knows_wot_super_infantry_4 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  
  ["aiel_deserter","Aiel Deserter","Aiel Deserters",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_22,
   [itm_aiel_spear, itm_hide_buckler_strong, itm_aiel_knife, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_5 ,wp_polearm(200)|wp_one_handed(160)|wp(130),knows_wot_super_infantry_5 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  
  ["aiel_prison_guard","Prison Guard","Prison Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_22,
   [itm_aiel_spear, itm_hide_buckler_strong, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_5 ,wp_polearm(190)|wp(120),knows_wot_super_infantry_5 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  
  ["aiel_castle_guard","Castle Guard","Castle Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_22,
   [itm_aiel_spear, itm_hide_buckler_strong, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_5 ,wp_polearm(190)|wp(120),knows_wot_super_infantry_5 ,aiel_1_man_face_younger, aiel_2_man_face_old],


# Seanchan Empire
  
  ["der_suldam","Der Sul'dam","Der Sul'dam",tf_female|tf_guarantee_all,0,0,fac_kingdom_23,
   [itm_der_suldam_dagger, itm_suldam_dress, itm_suldam_boots],
   def_attrib_wot_infantry_3,wp_one_handed(135)|wp(90),knows_wot_infantry_3,seanchan_1_woman_face_younger, seanchan_2_woman_face_older],
  
  ["damane","Damane","Damane",tf_female|tf_guarantee_all,0,0,fac_kingdom_23,
   [itm_power_player, itm_power_ammo, itm_damane_dress, itm_damane_boots],
   def_attrib|level(18),wp_firearm(175)|wp_one_handed(110)|wp(90),knows_common|knows_power_draw_3|knows_fire_5|knows_earth_4|knows_spirit_5|knows_water_5|knows_air_6, seanchan_1_woman_face_younger, seanchan_2_woman_face_older],

  ["damane_veteran","Damane Veteran","Damane Veterans",tf_female|tf_guarantee_all,0,0,fac_kingdom_23,
   [itm_power_player, itm_power_ammo, itm_damane_dress, itm_damane_boots],
   def_attrib|level(18),wp_firearm(195)|wp_one_handed(110)|wp(90),knows_common|knows_power_draw_5|knows_fire_7|knows_earth_6|knows_spirit_7|knows_water_7|knows_air_7, seanchan_1_woman_face_younger, seanchan_2_woman_face_older],
  
  ["seanchan_deathwatch_guard","Seanchan Deathwatch Guard","Seanchan Deathwatch Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_23,
   [itm_seanchan_large_sword, itm_deathwatch_guard_armor, itm_deathwatch_guard_helmet, itm_deathwatch_guard_boots, itm_deathwatch_guard_gloves],
   def_attrib_wot_infantry_5,wp_two_handed(200)|wp(175),knows_wot_infantry_5, seanchan_1_man_face_middle, seanchan_2_man_face_older],
  
  ["seanchan_halberdier","Seanchan Halberdier","Seanchan Halberdiers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_23,
   [itm_hafted_blade_a, itm_seanchan_high_armor, itm_seanchan_high_helmet, itm_seanchan_high_boots, itm_seanchan_high_gloves],
   def_attrib_wot_infantry_4,wp_polearm(150)|wp(120),knows_wot_infantry_4, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  
  ["seanchan_marksman","Seanchan Marksman","Seanchan Marksmen",tf_guarantee_all,0,0,fac_kingdom_23,
   [itm_war_bow, itm_arrows, itm_arrows, itm_seanchan_sword, itm_seanchan_middle_armor, itm_seanchan_middle_helmet, itm_seanchan_middle_boots, itm_seanchan_middle_gloves],
   def_attrib_wot_infantry_4,wp_archery(165)|wp_two_handed(130)|wp(100),knows_wot_infantry_4, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  
  ["seanchan_crossbowman","Seanchan Crossbowman","Seanchan Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_23,
   [itm_crossbow, itm_bolts, itm_seanchan_straight_sword, itm_seanchan_low_armor, itm_seanchan_low_helmet, itm_seanchan_low_boots, itm_seanchan_low_gloves],
   def_attrib_wot_infantry_3,wp_crossbow(135)|wp_one_handed(110)|wp(90),knows_wot_archer_3, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  
#  ["seanchan_morat_torm","Seanchan Morat'Torm","Seanchan Morat'Torm",tf_guarantee_armor,0,0,fac_kingdom_7,
#   [itm_scythe,itm_hatchet,itm_pickaxe,itm_club,itm_stones,itm_tab_shield_heater_a,itm_leather_cap,itm_felt_hat,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_nomad_boots,itm_wrapping_boots],
#   def_attrib|level(1),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
  
  ["seanchan_captain","Seanchan Captain","Seanchan Captains",tf_guarantee_all_cavalry,0,0,fac_kingdom_23,
   [itm_glaive, itm_seanchan_high_armor, itm_seanchan_high_helmet, itm_seanchan_high_boots, itm_seanchan_high_gloves, itm_hunter],
   def_attrib_wot_cavalry_5,wp_polearm(190)|wp(145),knows_wot_cavalry_5, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  
  ["seanchan_skirmisher","Seanchan Skirmisher","Seanchan Skirmishers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_23,
   [itm_khergit_bow, itm_arrows, itm_seanchan_straight_sword, itm_seanchan_middle_armor, itm_seanchan_middle_helmet, itm_seanchan_middle_boots, itm_seanchan_middle_gloves, itm_courser],
   def_attrib_wot_cavalry_4 ,wp_archery(180)|wp_one_handed(150)|wp(85),knows_wot_horse_archer_4, seanchan_1_man_face_younger, seanchan_2_man_face_older],  
#Other
  ["seanchan_messenger","Seanchan Messenger","Seanchan Messengers",tf_guarantee_all_cavalry,0,0,fac_kingdom_23,
   [itm_seanchan_straight_sword, itm_seanchan_low_armor, itm_seanchan_low_helmet, itm_seanchan_low_boots, itm_seanchan_low_gloves, itm_arabian_horse_a],
   def_attrib_wot_cavalry_3,wp_one_handed(125)|wp(90),knows_wot_cavalry_3, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  
  ["seanchan_deserter","Seanchan Deserter","Seanchan Deserters",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_23,
   [itm_seanchan_straight_sword, itm_seanchan_low_armor, itm_seanchan_low_helmet, itm_seanchan_low_boots, itm_seanchan_low_gloves],
   def_attrib_wot_infantry_2,wp_one_handed(100)|wp(90),knows_wot_infantry_2, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  
  ["seanchan_prison_guard","Prison Guard","Prison Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_23,
   [itm_seanchan_large_sword, itm_deathwatch_guard_armor, itm_deathwatch_guard_helmet, itm_deathwatch_guard_boots, itm_deathwatch_guard_gloves],
   def_attrib_wot_infantry_5,wp_two_handed(200)|wp(175),knows_wot_infantry_5, seanchan_1_man_face_middle, seanchan_2_man_face_older],
  
  ["seanchan_castle_guard","Castle Guard","Castle Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_23,
   [itm_hafted_blade_a, itm_seanchan_high_armor, itm_seanchan_high_helmet, itm_seanchan_high_boots, itm_seanchan_high_gloves],
   def_attrib_wot_infantry_4,wp_polearm(150)|wp(120),knows_wot_infantry_4, seanchan_1_man_face_younger, seanchan_2_man_face_older],


# Shadowspawn
  
  ["myrddraal","Myrddraal","Myddraal",tf_myrddraal|tf_guarantee_all_cavalry,0,0,fac_kingdom_24,
   [itm_myrddraal_blade,itm_myrddraal_hood_helmet, itm_myrddraal_armor, itm_black_mail_gauntlets, itm_black_leather_boots, itm_myrddraal_horse],
    def_attrib_wot_cavalry_5 ,wp_two_handed(225)|wp(200),knows_wot_cavalry_5,man_face_young_1, man_face_old_2],
  
  ["draghkar","Draghkar","Draghkar",tf_myrddraal|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_24,
   [itm_draghkar_dagger, itm_draghkar_tunic, itm_draghkar_helmet, itm_black_leather_boots, itm_draghkar_gloves],
   str_10|agi_7|int_5|cha_5|level(20),wp_one_handed(100)|wp(90),knows_wot_infantry_2, man_face_young_1, man_face_old_2],
  
  ["dreadlord","Dreadlord","Dreadlords",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_24,
   [itm_power_player, itm_power_ammo, itm_dreadlord_coat, itm_black_leather_boots, itm_saddle_horse],
   def_attrib_wot_infantry_3,wp_firearm(225)|wp_one_handed(150)|wp(125),knows_wot_horse_archer_3|knows_power_draw_5|knows_fire_6|knows_earth_6|knows_spirit_7|knows_water_5|knows_air_5,man_face_young_1, man_face_old_2],
  
  ["darkfriend_assassin","Darkfriend Assassin","Darkfriend Assassins",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_24,
   [itm_great_sword, itm_darkfriend_plate, itm_black_leather_boots, itm_black_mail_gauntlets, itm_bascinet_3],
   def_attrib_wot_infantry_4 ,wp_two_handed(155)|wp(100),knows_wot_infantry_4, man_face_young_1, man_face_old_2],
  
  ["darkfriend_leader","Darkfriend Leader","Darkfriend Leader",tf_guarantee_all_cavalry,0,0,fac_kingdom_24,
   [itm_heavy_lance, itm_sword_medieval_c_long, itm_darkfriend_shield_strong, itm_darkfriend_plate, itm_black_leather_boots, itm_black_mail_gauntlets, itm_bascinet_3, itm_hunter],
   def_attrib_wot_cavalry_4 ,wp_polearm(160)|wp(115),knows_wot_cavalry_4, man_face_young_1, man_face_old_2],
  
  ["darkfriend_marksman","Darkfriend Marksman","Darkfriend Marksmen",tf_guarantee_all,0,0,fac_kingdom_24,
   [itm_strong_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_sword_secondary, itm_darkfriend_armor, itm_leather_boots, itm_mail_mittens, itm_guard_helmet],
   def_attrib_wot_infantry_3 ,wp_archery(140)|wp_one_handed(130)|wp(120),knows_wot_archer_3, man_face_young_1, man_face_old_2],
#Other
  ["shadowspawn_messenger","Shadowspawn Messenger","Shadowspawn Messengers",tf_guarantee_all_cavalry,0,0,fac_kingdom_24,
   [itm_sword_viking_3, itm_darkfriend_shield_normal, itm_darkfriend_armor, itm_leather_boots, itm_mail_mittens, itm_guard_helmet, itm_saddle_horse],
   def_attrib_wot_cavalry_2 ,wp_one_handed(105)|wp(75),knows_wot_cavalry_2, man_face_young_1, man_face_old_2],
  
  ["shadowspawn_deserter","Shadowspawn Deserter","Shadowspawn Deserters",tf_trolloc|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_24,
   [itm_military_fork,itm_trolloc_hawk_helmet, itm_trolloc_weak_armor, itm_black_mail_gauntlets, itm_black_leather_boots],
    def_attrib_wot_super_infantry_2 ,wp_polearm(110)|wp(70),knows_wot_super_infantry_2,man_face_young_1, man_face_old_2],
  
  ["shadowspawn_prison_guard","Prison Guard","Prison Guards",tf_trolloc|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_24,
   [itm_great_long_bardiche,itm_trolloc_wolf_helmet, itm_trolloc_strong_armor, itm_black_mail_gauntlets, itm_black_leather_boots],
    def_attrib_wot_super_infantry_5 ,wp_polearm(250)|wp(200),knows_wot_super_infantry_5,man_face_young_1, man_face_old_2],
  
  ["shadowspawn_castle_guard","Castle Guard","Castle Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_24,
   [itm_great_sword, itm_darkfriend_plate, itm_black_leather_boots, itm_black_mail_gauntlets, itm_bascinet_3],
   def_attrib_wot_infantry_4 ,wp_two_handed(155)|wp(100),knows_wot_infantry_4, man_face_young_1, man_face_old_2],

############
## Shara
############

  ["shara_defender","Shara Defender","Shara Defenders",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_25,
   [itm_awlpike, itm_sword_secondary, itm_shara_elite_armor, itm_black_greaves, itm_wisby_gauntlets_black_wot, itm_noken_helmet],
   def_attrib_wot_infantry_5 ,wp_polearm(175)|wp(150),knows_wot_infantry_5, man_face_young_1, man_face_old_2],

  ["shara_captain","Shara Captain","Shara Captains",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_25,
   [itm_khergit_sword_two_handed_b, itm_shara_elite_armor, itm_black_greaves, itm_wisby_gauntlets_black_wot, itm_noken_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(180)|wp(100),knows_wot_infantry_4 ,man_face_young_1, man_face_old_2],

  ["shara_marksman","Shara Marksman","Shara Marksmen",tf_guarantee_all,0,0,fac_kingdom_25,
   [itm_war_bow, itm_bodkin_arrows, itm_sword_secondary, itm_shara_marksman_armor, itm_leather_boots, itm_helmet2_brass],
   def_attrib_wot_infantry_4 ,wp_archery(155)|wp_one_handed(125)|wp(105),knows_wot_archer_4, man_face_young_1, man_face_old_2],

  ["shara_crossbowman","Shara Crossbowman","Shara Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_25,
   [itm_crossbow, itm_bolts, itm_sword_secondary, itm_brass_shield, itm_shara_crossbowman_armor, itm_brass_boots, itm_lamellar_gauntlets, itm_helmet5_brass],
   def_attrib_wot_infantry_3 ,wp_crossbow(125)|wp_one_handed(110)|wp(85),knows_wot_archer_3 ,man_face_young_1, man_face_old_2],

  ["shara_shbo_guardsman","Shara Sh'bo Guardsman","Shara Sh'bo Guarsman",tf_guarantee_all_cavalry,0,0,fac_kingdom_25,
   [itm_heavy_lance, itm_sword_khergit_3, itm_brass_shield_elite, itm_sword_khergit_3, itm_shara_shbo_guardsman_armor, itm_lamellar_gauntlets, itm_brass_boots, itm_brass_veil_helm, itm_lord_warhorse_8],
   def_attrib_wot_cavalry_4 ,wp_polearm(170)|wp_one_handed(145)|wp(100),knows_wot_cavalry_4 ,man_face_young_1, man_face_old_2],

  ["shara_skirmisher","Shara Skirmisher","Shara Skirmishers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_25,
   [itm_khergit_bow, itm_arrows, itm_sword_secondary, itm_shara_mid_cavalry_armor, itm_brass_boots, itm_scale_gauntlets, itm_helmet5_brass, itm_hunter, itm_camel],
   def_attrib_wot_cavalry_3 ,wp_archery(145)|wp_one_handed(115)|wp(85),knows_wot_horse_archer_3 ,man_face_young_1, man_face_old_2],

  ["ayyad_counsel_member","Ayyad Counsel Member","Ayyad Counsel Members",tf_female|tf_guarantee_all,0,0,fac_kingdom_25,
   [itm_power_player, itm_power_ammo, itm_ayyad_counsel_member_tunic, itm_sarranid_boots_b],
   def_attrib|level(20),wp_firearm(185)|wp_one_handed(125)|wp(90),knows_common|knows_power_draw_4|knows_fire_6|knows_earth_3|knows_spirit_7|knows_water_6|knows_air_6, woman_face_1, woman_face_2],
  # Other
  ["shara_messenger","Shara Messenger","Shara Messengers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_25,
   [itm_khergit_bow, itm_arrows, itm_sword_secondary, itm_shara_mid_cavalry_armor, itm_brass_boots, itm_scale_gauntlets, itm_helmet5_brass, itm_hunter, itm_camel],
   def_attrib_wot_cavalry_3 ,wp_archery(145)|wp_one_handed(115)|wp(85),knows_wot_horse_archer_3 ,man_face_young_1, man_face_old_2],

  ["shara_deserter","Shara Deserter","Shara Deserters",tf_guarantee_all,0,0,fac_kingdom_25,
   [itm_crossbow, itm_bolts, itm_sword_secondary, itm_brass_shield, itm_shara_crossbowman_armor, itm_brass_boots, itm_lamellar_gauntlets, itm_helmet5_brass],
   def_attrib_wot_infantry_3 ,wp_crossbow(125)|wp_one_handed(110)|wp(85),knows_wot_archer_3 ,man_face_young_1, man_face_old_2],

  ["shara_prison_guard","Prison Guard","Prison Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_25,
   [itm_heavy_lance, itm_brass_shield_elite, itm_sword_khergit_3, itm_shara_shbo_guardsman_armor, itm_lamellar_gauntlets, itm_brass_boots, itm_brass_veil_helm, itm_lord_warhorse_8],
   def_attrib_wot_cavalry_4 ,wp_polearm(170)|wp_one_handed(145)|wp(100),knows_wot_cavalry_4 ,man_face_young_1, man_face_old_2],

  ["shara_castle_guard","Castle Guard","Castle Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_25,
   [itm_khergit_sword_two_handed_b, itm_shara_elite_armor, itm_black_greaves, itm_wisby_gauntlets_black_wot, itm_noken_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(180)|wp(100),knows_wot_infantry_4 ,man_face_young_1, man_face_old_2],


##############
## Sea Folk
##############

  ["sea_folk_cargomaster","Sea Folk Cargomaster","Sea Folk Cargomasters",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_26,
   [itm_khergit_sword_two_handed_b, itm_sea_folk_elite_armor, itm_leather_gloves, itm_sea_folk_elite_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(180)|wp(100),knows_wot_infantry_4 ,seanchan_2_man_face_young, seanchan_2_man_face_old],

  ["sea_folk_deck_defender","Sea Folk Deck Defenders","Sea Folk Deck Defenders",tf_guarantee_all,0,0,fac_kingdom_26,
   [itm_war_bow, itm_bodkin_arrows, itm_sword_secondary, itm_sea_folk_padded_armor, itm_leather_gloves, itm_vaegir_spiked_helmet],
   def_attrib_wot_infantry_4 ,wp_archery(155)|wp_one_handed(125)|wp(105),knows_wot_archer_4, seanchan_2_man_face_young, seanchan_2_man_face_old],

  ["sea_folk_wavemistress","Sea Folk Wavemistress","Sea Folk Wavemistresses",tf_female|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_26,
   [itm_scimitar_b, itm_sea_folk_female_armor, itm_leather_covered_round_shield, itm_leather_gloves, itm_vaegir_spiked_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(180)|wp(100),knows_wot_infantry_4 ,seanchan_2_woman_face_young, seanchan_2_woman_face_old],  
  
  ["sea_folk_windfinder","Sea Folk Windfinder","Sea Folk Windfinders",tf_female|tf_guarantee_all,0,0,fac_kingdom_26,
   [itm_power_player, itm_power_ammo, itm_sea_folk_female_armor],
   def_attrib|level(20),wp_firearm(185)|wp_one_handed(125)|wp(90),knows_common|knows_power_draw_4|knows_fire_5|knows_earth_4|knows_spirit_6|knows_water_7|knows_air_7, seanchan_2_woman_face_young, seanchan_2_woman_face_old],
  # Other
    ["sea_folk_messenger","Sea Folk Messenger","Sea Folk Messengers",tf_female|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_26,
   [itm_spear, itm_sea_folk_female_tunic],
   def_attrib_wot_infantry_2 ,wp_polearm(110)|wp(75),knows_wot_infantry_2 ,seanchan_2_woman_face_younger, seanchan_2_woman_face_old],  

  ["sea_folk_deserter","Sea Folk Deserter","Sea Folk Deserters",tf_guarantee_all,0,0,fac_kingdom_26,
   [itm_strong_bow, itm_arrows, itm_sword_secondary, itm_sea_folk_padded_armor, itm_spiked_helmet],
   def_attrib_wot_infantry_3 ,wp_archery(100)|wp_one_handed(90)|wp(80),knows_wot_archer_3, seanchan_2_man_face_younger, seanchan_2_man_face_old],

  ["sea_folk_prison_guard","Prison Guard","Prison Guards",tf_female|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_26,
   [itm_scimitar_b, itm_sea_folk_female_armor, itm_leather_covered_round_shield, itm_leather_gloves, itm_vaegir_spiked_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(180)|wp(100),knows_wot_infantry_4 ,seanchan_2_woman_face_young, seanchan_2_woman_face_old],  

  ["sea_folk_castle_guard","Castle Guard","Castle Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_26,
   [itm_khergit_sword_two_handed_b, itm_sea_folk_elite_armor, itm_leather_gloves, itm_sea_folk_elite_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(180)|wp(100),knows_wot_infantry_4 ,seanchan_2_man_face_young, seanchan_2_man_face_old],


####################
## Land of Madmen
####################

  ["madmen_chieftan","Madmen Chieftan","Madman Chieftans",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_27,
   [itm_great_long_bardiche, itm_hammer, itm_lamellar_vest_khergit, itm_leather_boots, itm_leather_gloves, itm_khergit_war_helmet],
   def_attrib_wot_infantry_5 ,wp_polearm(185)|wp(150),knows_wot_infantry_5, man_face_young_1, man_face_old_2],

  ["madmen_pillager","Madmen Pillager","Madmen Pillagers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_27,
   [itm_one_handed_battle_axe_b, itm_leather_covered_round_shield, itm_lamellar_vest_khergit, itm_leather_boots, itm_leather_gloves, itm_khergit_war_helmet],
   def_attrib_wot_infantry_4 ,wp_one_handed(180)|wp(100),knows_wot_infantry_4 ,man_face_young_1, man_face_old_2],

  ["madmen_assassin","Madmen Assassin","Madmen Assassins",tf_guarantee_all,0,0,fac_kingdom_27,
   [itm_war_bow, itm_bodkin_arrows, itm_one_handed_war_axe_b, itm_tribal_warrior_outfit, itm_hide_boots, itm_leather_gloves, itm_leather_steppe_cap_b],
   def_attrib_wot_infantry_4 ,wp_archery(155)|wp_one_handed(125)|wp(105),knows_wot_archer_4, man_face_young_1, man_face_old_2],

  ["madmen_thunderhoof","Madmen Thunderhoof","Madmen Thunderhooves",tf_guarantee_all_cavalry,0,0,fac_kingdom_27,
   [itm_lance, itm_sword_medieval_b, itm_one_handed_war_axe_b, itm_leather_covered_round_shield, itm_tribal_warrior_outfit, itm_hide_boots, itm_leather_gloves, itm_leather_steppe_cap_b, itm_hunter],
   def_attrib_wot_cavalry_4 ,wp_polearm(155)|wp_one_handed(120)|wp(100),knows_wot_cavalry_4 ,man_face_young_1, man_face_old_2],

  ["madmen_plains_rider","Madmen Plains Rider","Madmen Plains Riders",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_27,
   [itm_khergit_bow, itm_arrows, itm_one_handed_war_axe_b, itm_ragged_outfit, itm_hide_boots, itm_leather_gloves, itm_steppe_horse],
   def_attrib_wot_cavalry_3 ,wp_archery(145)|wp_one_handed(115)|wp(85),knows_wot_horse_archer_3 ,man_face_young_1, man_face_old_2],

    ["madmen_storm_caller","Madmen Storm Caller","Madmen Storm Callers",tf_guarantee_all,0,0,fac_kingdom_27,
   [itm_power_player, itm_power_ammo, itm_one_handed_war_axe_b, itm_lamellar_vest_khergit, itm_leather_boots, itm_leather_gloves, itm_khergit_war_helmet],
   def_attrib_wot_infantry_2,wp_firearm(185)|wp_one_handed(110)|wp(90),knows_wot_infantry_2|knows_power_draw_4|knows_fire_7|knows_earth_6|knows_spirit_5|knows_water_7|knows_air_6,man_face_young_1, man_face_old_2],
  # Other
  ["madmen_messenger","Madmen Messenger","Madmen Messengers",tf_guarantee_all_cavalry,0,0,fac_kingdom_27,
   [itm_lance, itm_one_handed_war_axe_b, itm_leather_covered_round_shield, itm_tribal_warrior_outfit, itm_hide_boots, itm_leather_gloves, itm_leather_steppe_cap_b, itm_hunter],
   def_attrib_wot_cavalry_4 ,wp_polearm(155)|wp_one_handed(120)|wp(100),knows_wot_cavalry_4 ,man_face_young_1, man_face_old_2],

  ["madmen_deserter","Madmen Deserter","Madmen Deserters",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_27,
   [itm_war_spear, itm_madmen_paint_3, itm_madmen_paint_2, itm_hide_boots],
   def_attrib_wot_infantry_2 ,wp_polearm(110)|wp(75),knows_wot_infantry_2 ,man_face_young_1, man_face_old_2],

  ["madmen_prison_guard","Prison Guard","Prison Guards",tf_guarantee_all,0,0,fac_kingdom_27,
   [itm_war_bow, itm_bodkin_arrows, itm_one_handed_war_axe_b, itm_tribal_warrior_outfit, itm_hide_boots, itm_leather_gloves, itm_leather_steppe_cap_b],
   def_attrib_wot_infantry_4 ,wp_archery(155)|wp_one_handed(125)|wp(105),knows_wot_archer_4, man_face_young_1, man_face_old_2],

  ["madmen_castle_guard","Castle Guard","Castle Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_27,
   [itm_great_long_bardiche, itm_hammer, itm_lamellar_vest_khergit, itm_leather_boots, itm_leather_gloves, itm_khergit_war_helmet],
   def_attrib_wot_infantry_5 ,wp_polearm(185)|wp(150),knows_wot_infantry_5, man_face_young_1, man_face_old_2],

  
##################
## Toman Head
##################

  ["toman_head_city_guard","Toman Head City Guard","Toman Head City Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_28,
   [itm_halberd, itm_sword_medieval_a, itm_toman_head_mail_and_plate, itm_mail_chausses, itm_leather_gloves, itm_nasal_helmet],
   def_attrib_wot_infantry_3 ,wp_polearm(150)|wp(100),knows_wot_infantry_3 ,arad_doman_man_face_younger, tarabon_man_face_old],
  
  ["toman_head_bowman","Toman Head Bowman","Toman Head Bowmen",tf_guarantee_all,0,0,fac_kingdom_28,
   [itm_strong_bow, itm_arrows, itm_sword_secondary, itm_toman_head_shield_weak, itm_toman_head_army_armor, itm_leather_boots, itm_leather_gloves, itm_nordic_archer_helmet],
   def_attrib_wot_infantry_3 ,wp_archery(125)|wp_one_handed(110)|wp(85),knows_wot_archer_3 ,arad_doman_man_face_younger, tarabon_man_face_old],

    ["toman_head_scout","Toman Head Scout","Toman Head Scouts",tf_guarantee_all_cavalry,0,0,fac_kingdom_28,
   [itm_war_spear, itm_sword_medieval_c, itm_toman_head_shield_weak, itm_toman_head_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_leather_cap, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_polearm(125)|wp(80),knows_wot_cavalry_2, arad_doman_man_face_younger, tarabon_man_face_old],
  # Other
    ["toman_head_messenger","Toman Head Messenger","Toman Head Messengers",tf_guarantee_all_cavalry,0,0,fac_kingdom_28,
   [itm_war_spear, itm_sword_medieval_c, itm_toman_head_shield_weak, itm_toman_head_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_leather_cap, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_polearm(125)|wp(80),knows_wot_cavalry_2, arad_doman_man_face_younger, tarabon_man_face_old],

    ["toman_head_deserter","Toman Head Deserter","Toman Head Deserters",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_28,
   [itm_sword_medieval_a, itm_toman_head_recruit_tunic, itm_wrapping_boots],
   def_attrib_wot_infantry_1 ,wp(65),knows_wot_infantry_1 ,arad_doman_man_face_younger, tarabon_man_face_old],

  ["toman_head_prison_guard","Prison Guard","Prison Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_28,
   [itm_red_arm_club, itm_toman_head_army_armor, itm_toman_head_shield_normal, itm_leather_boots, itm_leather_gloves, itm_nordic_archer_helmet],
   def_attrib_wot_infantry_2 ,wp_one_handed(110)|wp(75),knows_wot_infantry_2 ,arad_doman_man_face_younger, tarabon_man_face_old],  
  
  ["toman_head_castle_guard","Castle Guard","Castle Guards",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_28,
   [itm_halberd, itm_sword_medieval_a, itm_toman_head_mail_and_plate, itm_mail_chausses, itm_leather_gloves, itm_nasal_helmet],
   def_attrib_wot_infantry_3 ,wp_polearm(150)|wp(100),knows_wot_infantry_3 ,arad_doman_man_face_younger, tarabon_man_face_old],


   
  
  

#  ["draghkar","Draghkar","Draghkar",tf_guarantee_armor,0,0,fac_kingdom_1,
#   [itm_scythe,itm_hatchet,itm_pickaxe,itm_club,itm_stones,itm_tab_shield_heater_a,itm_leather_cap,itm_felt_hat,itm_felt_hat,
#    itm_shirt,itm_coarse_tunic,itm_leather_apron,itm_nomad_boots,itm_wrapping_boots],
#   def_attrib|level(5),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],



##############################################
##### End WoT Faction Troops (Non-Upgradeable)
##############################################
  
  

### other native troops that may or may not need to upgrade (commented out their upgrade for TGS)  

# Modified for TGS
  ["looter","Bandit","Bandits",tf_guarantee_armor,0,0,fac_outlaws,
   [itm_stones,itm_hatchet,itm_club,itm_butchering_knife,itm_falchion, itm_rawhide_coat,itm_nomad_armor,itm_nomad_armor,itm_woolen_cap,itm_woolen_cap,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(20),knows_common,bandit_face1, bandit_face2],
  ["bandit","Bandit","Bandits",tf_guarantee_armor,0,0,fac_outlaws,
   [itm_arrows,itm_spiked_mace,itm_sword_viking_1,itm_short_bow,itm_falchion,itm_nordic_shield,itm_rawhide_coat,itm_leather_cap,itm_leather_jerkin,itm_nomad_armor,itm_nomad_boots,itm_wrapping_boots,itm_saddle_horse],
   def_attrib|level(10),wp(60),knows_common|knows_power_draw_1,bandit_face1, bandit_face2],
  ["brigand","Brigand","Brigands",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_outlaws,
   [itm_arrows,itm_spiked_mace,itm_sword_viking_1,itm_falchion,itm_wooden_shield,itm_hide_covered_round_shield,itm_long_bow,itm_leather_cap,itm_leather_jerkin,itm_nomad_boots,itm_saddle_horse],
   def_attrib|level(16),wp(90),knows_common|knows_power_draw_3,bandit_face1, bandit_face2],
  ["mountain_bandit","Bandit","Bandits",tf_guarantee_armor|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_arrows,itm_sword_viking_1,itm_spear,itm_winged_mace,itm_maul,itm_falchion,itm_short_bow,itm_javelin,itm_fur_covered_shield,itm_hide_covered_round_shield,
    itm_felt_hat,itm_head_wrappings,itm_skullcap,itm_ragged_outfit,itm_rawhide_coat,itm_leather_armor,itm_hide_boots,itm_nomad_boots,itm_wooden_shield,itm_nordic_shield],
   def_attrib|level(11),wp(90),knows_common|knows_power_draw_2,rhodok_face_young_1, rhodok_face_old_2],
  ["forest_bandit","Forest Raider","Forest Raiders",tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_boots,0,0,fac_outlaws,
   [itm_arrows,itm_axe,itm_hatchet,itm_quarter_staff,itm_short_bow,itm_hunting_bow,
    itm_common_hood,itm_black_hood,itm_shirt,itm_padded_leather,itm_leather_jerkin,itm_ragged_outfit,itm_hide_boots,itm_leather_boots],
   def_attrib|level(11),wp(90),knows_common|knows_power_draw_3,swadian_face_young_1, swadian_face_old_2],
  ["sea_raider","Coastal Raider","Coastal Raiders",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_shield,0,0,fac_outlaws,
   [itm_arrows,itm_sword_viking_1,itm_sword_viking_2,itm_fighting_axe,itm_battle_axe,itm_spear,itm_nordic_shield,itm_nordic_shield,itm_nordic_shield,itm_wooden_shield,itm_long_bow,itm_javelin,itm_throwing_axes,
    itm_nordic_helmet,itm_nordic_helmet,itm_nasal_helmet,itm_nomad_vest,itm_byrnie,itm_mail_shirt,itm_leather_boots, itm_nomad_boots],
   def_attrib|level(16),wp(110),knows_ironflesh_2|knows_power_strike_2|knows_power_draw_3|knows_power_throw_2|knows_riding_1|knows_athletics_2,nord_face_young_1, nord_face_old_2],
  ["steppe_bandit","Steppe Bandit","Steppe Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_guarantee_ranged|tf_mounted,0,0,fac_outlaws,
   [itm_arrows,itm_sword_khergit_1,itm_winged_mace,itm_spear, itm_light_lance,itm_nomad_bow,itm_nomad_bow,itm_short_bow,itm_jarid,itm_leather_steppe_cap_a,itm_leather_steppe_cap_b,itm_nomad_cap,itm_nomad_cap_b,itm_khergit_armor,itm_steppe_armor,itm_leather_vest,itm_hide_boots,itm_nomad_boots,itm_leather_covered_round_shield,itm_leather_covered_round_shield,itm_saddle_horse,itm_steppe_horse,itm_steppe_horse],
   def_attrib|level(12),wp(100),knows_riding_4|knows_horse_archery_3|knows_power_draw_3,khergit_face_young_1, khergit_face_old_2],
  ["taiga_bandit","Taiga Bandit","Taiga Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged,0,0,fac_outlaws,
   [itm_arrows,itm_sword_khergit_1,itm_winged_mace,itm_spear, itm_light_lance,itm_nomad_bow,itm_nomad_bow,itm_short_bow,itm_jarid,itm_javelin,itm_vaegir_fur_cap,itm_leather_steppe_cap_c,itm_nomad_armor,itm_leather_jerkin,itm_hide_boots,itm_nomad_boots,itm_leather_covered_round_shield,itm_leather_covered_round_shield],
   def_attrib|level(15),wp(110),knows_common|knows_power_draw_4|knows_power_throw_3,vaegir_face_young_1, vaegir_face_old_2],
  ["desert_bandit","Desert Bandit","Desert Bandits",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse|tf_mounted,0,0,fac_outlaws,
   [itm_arrows,itm_arabian_sword_a,itm_winged_mace,itm_spear, itm_light_lance,itm_jarid,itm_nomad_bow,itm_short_bow,itm_jarid,itm_sarranid_cloth_robe, itm_sarranid_cloth_robe, itm_skirmisher_armor, itm_desert_turban, itm_turban,itm_leather_steppe_cap_b,itm_leather_covered_round_shield,itm_leather_covered_round_shield,itm_saddle_horse,itm_arabian_horse_a],
   def_attrib|level(12),wp(100),knows_riding_4|knows_horse_archery_3|knows_power_draw_3,khergit_face_young_1, khergit_face_old_2],
# End modified for TGS
  ### added for TGS
  ["arad_doman_rabble_bandit","Arad Doman Rabble","Arad Doman Rabble",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
   [itm_butchering_knife, itm_pitch_fork, itm_boar_spear, itm_pelt_coat, itm_sarranid_cloth_robe, itm_linen_tunic, itm_wrapping_boots, itm_steppe_cap],
   def_attrib_wot_infantry_2 ,wp_one_handed(90)|wp(70),knows_wot_infantry_2,arad_doman_man_face_young, arad_doman_man_face_older],
  ["aiel_raider_bandit","Aiel Raider","Aiel Raiders",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_6,
   [itm_aiel_spear, itm_hide_buckler_normal, itm_cadinsor_green, itm_shoufa_green, itm_cadinsor_boots_green],
   def_attrib_wot_super_infantry_3 ,wp_polearm(145)|wp(90),knows_wot_super_infantry_3 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  ["trolloc_grunt_bandit","Trolloc Grunt","Trolloc Grunts",tf_trolloc|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_8,
   [itm_military_fork,itm_trolloc_hawk_helmet, itm_trolloc_weak_armor, itm_black_mail_gauntlets, itm_black_leather_boots],
    def_attrib_wot_super_infantry_2 ,wp_polearm(110)|wp(70),knows_wot_super_infantry_2,man_face_young_1, man_face_old_2],
  ### end added for TGS
  
  ["black_khergit_horseman","Black Khergit Horseman","Black Khergit Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
   [itm_arrows,itm_sword_khergit_2,itm_scimitar,itm_scimitar,itm_winged_mace,itm_spear,itm_lance,itm_khergit_bow,itm_khergit_bow,itm_nomad_bow,itm_nomad_bow,itm_steppe_cap,itm_nomad_cap,itm_khergit_war_helmet,itm_khergit_war_helmet,itm_mail_hauberk,itm_lamellar_armor,itm_hide_boots,itm_plate_covered_round_shield,itm_plate_covered_round_shield,itm_saddle_horse,itm_steppe_horse],
   def_attrib|level(21),wp(100),knows_riding_3|knows_ironflesh_3|knows_horse_archery_3|knows_power_draw_3,khergit_face_young_1, khergit_face_old_2],

  ["manhunter","Manhunter","Manhunters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_manhunters,
   [itm_mace_3,itm_winged_mace,itm_nasal_helmet,itm_padded_cloth,itm_aketon_green,itm_aketon_green,itm_wooden_shield,itm_nomad_boots,itm_wrapping_boots,itm_sumpter_horse],
   def_attrib|level(10),wp(50),knows_common,bandit_face1, bandit_face2],
##  ["deserter","Deserter","Deserters",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_swadian_deserters,
##   [itm_arrows,itm_spear,itm_fighting_pick,itm_short_bow,itm_sword,itm_voulge,itm_nordic_shield,itm_round_shield,itm_kettle_hat,itm_leather_cap,itm_padded_cloth,itm_leather_armor,itm_scale_armor,itm_saddle_horse],
##   def_attrib|level(12),wp(60),knows_common,bandit_face1, bandit_face2],

#fac_slavers
##  ["slave_keeper","Slave Keeper","Slave Keepers",tf_guarantee_armor ,0,0,fac_slavers,
##   [itm_cudgel,itm_club,itm_woolen_cap,itm_rawhide_coat,itm_coarse_tunic,itm_nomad_armor,itm_nordic_shield,itm_nomad_boots,itm_wrapping_boots,itm_sumpter_horse],
##   def_attrib|level(10),wp(60),knows_common,bandit_face1, bandit_face2],
  ["slave_driver","Slave Driver","Slave Drivers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse ,0,0,fac_slavers,
   [itm_club_with_spike_head,itm_segmented_helmet,itm_tribal_warrior_outfit,itm_nordic_shield,itm_leather_boots,itm_leather_gloves,itm_khergit_leather_boots,itm_steppe_horse],
   def_attrib|level(14),wp(80),knows_common,bandit_face1, bandit_face2],
  ["slave_hunter","Slave Hunter","Slave Hunters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield ,0,0,fac_slavers,
   [itm_winged_mace,itm_maul,itm_kettle_hat,itm_mail_shirt,itm_tab_shield_round_c,itm_leather_boots,itm_leather_gloves,itm_courser],
   def_attrib|level(18),wp(90),knows_common,bandit_face1, bandit_face2],
  ["slave_crusher","Slave Crusher","Slave Crushers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield ,0,0,fac_slavers,
   [itm_sledgehammer,itm_spiked_mace,itm_mail_hauberk,itm_bascinet_2,itm_bascinet_3,itm_mail_mittens,itm_tab_shield_round_d,itm_mail_chausses,itm_splinted_leather_greaves,itm_hunter],
   def_attrib|level(22),wp(110),knows_common|knows_riding_4|knows_power_strike_3,bandit_face1, bandit_face2],
  ["slaver_chief","Slaver Chief","Slaver Chiefs",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_slavers,
   [itm_military_hammer,itm_warhammer,itm_brigandine_red,itm_steel_shield,itm_scale_gauntlets,itm_mail_mittens,itm_guard_helmet,itm_plate_boots,itm_mail_boots,itm_warhorse],
   def_attrib|level(26),wp(130),knows_common|knows_riding_4|knows_power_strike_5,bandit_face1, bandit_face2],

#Rhodok tribal, Hunter, warrior, veteran, warchief






#  ["undead_walker","undead_walker","undead_walkers",tf_undead|tf_allways_fall_dead,0,0,fac_undeads,
#   [], 
#   def_attrib|level(3),wp(60),knows_common,undead_face1, undead_face2],
#  ["undead_horseman","undead_horseman","undead_horsemen",tf_undead|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse,0,0,fac_undeads,
#   [], 
#   def_attrib|level(19),wp(100),knows_common,undead_face1, undead_face2],
#  ["undead_nomad","undead_nomad","undead_nomads",tf_undead|tf_allways_fall_dead|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
#   [], 
#   def_attrib|level(21),wp(100),knows_common|knows_riding_4,khergit_face1, khergit_face2],
#  ["undead","undead","undead",tf_undead|tf_allways_fall_dead,0,0,fac_undeads,
#   [], 
#   def_attrib|level(3),wp(60),knows_common,undead_face1, undead_face2],
#  ["hell_knight","hell_knight","hell_knights",tf_undead|tf_allways_fall_dead|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_undeads,
#   [], 
#   def_attrib|level(23),wp(100),knows_common|knows_riding_3,undead_face1, undead_face2],



  ["follower_woman","Camp Follower","Camp Follower",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_bolts,itm_light_crossbow,itm_short_bow,itm_crossbow,itm_nordic_shield,itm_hide_covered_round_shield,itm_hatchet,itm_hand_axe,itm_voulge,itm_fighting_pick,itm_club,itm_dress,itm_woolen_dress, itm_skullcap, itm_wrapping_boots],
   def_attrib|level(5),wp(70),knows_common,refugee_face1,refugee_face2],
  ["hunter_woman","Huntress","Huntresses",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_bolts,itm_arrows,itm_light_crossbow,itm_short_bow,itm_crossbow,itm_nordic_shield,itm_hide_covered_round_shield,itm_hatchet,itm_hand_axe,itm_voulge,itm_fighting_pick,itm_club,itm_dress,itm_leather_jerkin, itm_skullcap, itm_wrapping_boots],
   def_attrib|level(10),wp(85),knows_common|knows_power_strike_1,refugee_face1,refugee_face2],

  # modified for TGS
  ["fighter_woman","Cha Faile Swordswoman","Cha Faile Swordswomen",tf_female|tf_guarantee_all_wo_ranged,0,0,fac_commoners,
   [itm_sword_medieval_b,itm_fur_covered_shield,itm_nordic_shield,itm_leather_jerkin,itm_leather_vest, itm_leather_boots, itm_leather_gloves],
   def_attrib|level(16),wp(100),knows_common|knows_riding_3|knows_athletics_2|knows_ironflesh_1,refugee_face1,refugee_face2],
  ["sword_sister","Hunter for the Horn","Hunters for the Horn",tf_female|tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_shield|tf_guarantee_horse,0,0,fac_commoners,
   [itm_sword_medieval_b,itm_sword_khergit_3,itm_plate_covered_round_shield,itm_tab_shield_small_round_c,itm_plate_armor,itm_coat_of_plates,itm_mail_chausses,itm_iron_greaves,itm_guard_helmet,itm_helmet_with_neckguard,itm_courser,itm_leather_gloves],
   def_attrib|level(20),wp_one_handed(150)|wp(140),knows_common|knows_riding_5|knows_athletics_3|knows_ironflesh_2|knows_shield_2,refugee_face1,refugee_face2],
  # end modified for TGS
  ### added for TGS
  ["village_wisdom","Village Wisdom","Village Wisdoms",tf_female|tf_guarantee_all,0,0,fac_commoners,
   [itm_power_player,itm_power_ammo,itm_cudgel,itm_dress,itm_woolen_dress, itm_wrapping_boots],
   def_attrib|level(10),wp_firearm(120)|wp_one_handed(110)|wp(75),knows_common|knows_power_draw_3|knows_fire_4|knows_earth_2|knows_spirit_4|knows_water_5|knows_air_5,refugee_face1,refugee_face2],
  ["kinswoman","Kinswoman","Kinswomen",tf_female|tf_guarantee_all,0,0,fac_commoners,
   [itm_power_player,itm_power_ammo,itm_dagger,itm_blue_dress, itm_dress,itm_peasant_dress,itm_woolen_dress, itm_woolen_hose],
   def_attrib|level(15),wp_firearm(150)|wp_one_handed(125)|wp(100),knows_common|knows_power_draw_4|knows_fire_5|knows_earth_4|knows_spirit_5|knows_water_6|knows_air_6,refugee_face1,refugee_face2],
  ### end added for TGS

  ["refugee","Refugee","Refugees",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_knife,itm_pitch_fork,itm_sickle,itm_hatchet,itm_club,itm_dress,itm_robe,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
   def_attrib|level(1),wp(45),knows_common,refugee_face1,refugee_face2],
  ["peasant_woman","Peasant Woman","Peasant Women",tf_female|tf_guarantee_armor,0,0,fac_commoners,
   [itm_knife,itm_pitch_fork,itm_sickle,itm_hatchet,itm_club,itm_dress,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
   def_attrib|level(1),wp(40),knows_common,refugee_face1,refugee_face2],

 
  ["caravan_master","Caravan Master","Caravan Masters",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_commoners,
   [itm_sword_medieval_c,itm_fur_coat,itm_hide_boots,itm_saddle_horse,
    itm_saddle_horse,itm_saddle_horse,itm_saddle_horse,
    itm_leather_jacket, itm_leather_cap],
   def_attrib|level(9),wp(100),knows_common|knows_riding_4|knows_ironflesh_3,mercenary_face_1, mercenary_face_2],

  ["kidnapped_girl","Kidnapped Girl","Kidnapped Girls",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners,
   [itm_dress,itm_leather_boots],
   def_attrib|level(2),wp(50),knows_common|knows_riding_2,woman_face_1, woman_face_2],


#This troop is the troop marked as soldiers_end and town_walkers_begin
 ["town_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic, itm_linen_tunic,itm_fur_coat, itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_arena_tunic_white, itm_leather_apron, itm_shirt, itm_arena_tunic_green, itm_arena_tunic_blue, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_young_1, man_face_old_2],
 ["town_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["khergit_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_sarranid_felt_hat,itm_turban,itm_wrapping_boots,itm_khergit_leather_boots,itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b],
   def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
 ["khergit_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
 ["sarranid_townsman","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
   [itm_sarranid_felt_hat,itm_turban,itm_wrapping_boots,itm_sarranid_boots_a,itm_sarranid_cloth_robe, itm_sarranid_cloth_robe_b],
   def_attrib|level(4),wp(60),knows_common,swadian_face_younger_1, swadian_face_middle_2],
 ["sarranid_townswoman","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_sarranid_common_dress, itm_sarranid_common_dress_b,itm_woolen_hose,itm_sarranid_boots_a, itm_sarranid_felt_head_cloth, itm_sarranid_felt_head_cloth_b],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
  
#This troop is the troop marked as town_walkers_end and village_walkers_begin
 ["village_walker_1","Villager","Villagers",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic, itm_linen_tunic, itm_coarse_tunic, itm_leather_vest, itm_leather_apron, itm_shirt, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_younger_1, man_face_older_2],
 ["village_walker_2","Villager","Villagers",tf_female|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],

#This troop is the troop marked as village_walkers_end and spy_walkers_begin
 ["spy_walker_1","Townsman","Townsmen",tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_short_tunic, itm_linen_tunic, itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_robe, itm_leather_apron, itm_shirt, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_hide_boots, itm_ankle_boots, itm_leather_boots, itm_fur_hat, itm_leather_cap, itm_straw_hat, itm_felt_hat],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_old_2],
 ["spy_walker_2","Townswoman","Townswomen",tf_female|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_commoners,
   [itm_blue_dress, itm_dress, itm_woolen_dress, itm_peasant_dress, itm_woolen_hose, itm_blue_hose, itm_wimple_a, itm_wimple_with_veil, itm_female_hood],
   def_attrib|level(2),wp(40),knows_common,woman_face_1,woman_face_2],
# Ryan END

#This troop is the troop marked as spy_walkers_end
# Zendar
  ["tournament_master","Tournament Master","Tournament Master",tf_hero, scn_zendar_center|entry(1),reserved,  fac_commoners,[itm_nomad_armor,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],
  ["trainer","Trainer","Trainer",tf_hero, scn_zendar_center|entry(2),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x00000000000430c701ea98836781647f],
  ["Constable_Hareck","Constable Hareck","Constable Hareck",tf_hero, scn_zendar_center|entry(5),reserved,  fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x00000000000c41c001fb15234eb6dd3f],

# Ryan BEGIN
  ["Ramun_the_slave_trader","Ramun, the slave trader","Ramun, the slave trader",tf_hero, no_scene,reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x0000000fd5105592385281c55b8e44eb00000000001d9b220000000000000000],

  ["guide","Quick Jimmy","Quick Jimmy",tf_hero, no_scene,0,  fac_commoners,[itm_coarse_tunic,itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c318301f24e38a36e38e3],
# Ryan END

  ["Xerina","Xerina","Xerina",tf_hero|tf_female, scn_the_happy_boar|entry(5),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|str_15|agi_15|level(39),wp(312),knows_power_strike_5|knows_ironflesh_5|knows_riding_6|knows_power_draw_4|knows_athletics_8|knows_shield_3,0x00000001ac0820074920561d0b51e6ed00000000001d40ed0000000000000000],
  ["Dranton","Dranton","Dranton",tf_hero, scn_the_happy_boar|entry(2),reserved,  fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|str_15|agi_14|level(42),wp(324),knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_3,0x0000000a460c3002470c50f3502879f800000000001ce0a00000000000000000],
  ["Kradus","Kradus","Kradus",tf_hero, scn_the_happy_boar|entry(3),reserved,  fac_commoners,[itm_padded_leather,itm_hide_boots],def_attrib|str_15|agi_14|level(43),wp(270),knows_power_strike_5|knows_ironflesh_7|knows_riding_4|knows_power_draw_4|knows_athletics_4|knows_shield_3,0x0000000f5b1052c61ce1a9521db1375200000000001ed31b0000000000000000],


#Tutorial
  ["tutorial_trainer","Training Ground Master","Training Ground Master",tf_hero, 0, 0, fac_commoners,[itm_robe,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common,0x000000000008414401e28f534c8a2d09],
  ["tutorial_student_1","{!}tutorial_student_1","{!}tutorial_student_1",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_sword, itm_practice_shield, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_2","{!}tutorial_student_2","{!}tutorial_student_2",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_sword, itm_practice_shield, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_3","{!}tutorial_student_3","{!}tutorial_student_3",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_staff, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],
  ["tutorial_student_4","{!}tutorial_student_4","{!}tutorial_student_4",tf_guarantee_boots|tf_guarantee_armor, 0, 0, fac_neutral,
   [itm_practice_staff, itm_leather_jerkin,itm_padded_leather,itm_leather_armor,itm_ankle_boots,itm_padded_coif,itm_footman_helmet],
   def_attrib|level(2),wp(20),knows_common, swadian_face_young_1, swadian_face_old_2],

#Sargoth
  #halkard, hardawk. lord_taucard lord_caupard. lord_paugard

#Salt mine
  ["Galeas","Galeas","Galeas",tf_hero, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,0x000000000004718201c073191a9bb10c],

#Dhorak keep

  ["farmer_from_bandit_village","Farmer","Farmers",tf_guarantee_armor,no_scene,reserved,fac_commoners,
   [itm_linen_tunic,itm_coarse_tunic,itm_shirt,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_older_2],

  ["trainer_1","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_1|entry(6),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000d0d1030c74ae8d661b651c6840000000000000e220000000000000000],
  ["trainer_2","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_2|entry(6),reserved,  fac_commoners,[itm_nomad_vest,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e5a04360428ec253846640b5d0000000000000ee80000000000000000],
  ["trainer_3","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_3|entry(6),reserved,  fac_commoners,[itm_padded_leather,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e4a0445822ca1a11ab1e9eaea0000000000000f510000000000000000],
  ["trainer_4","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_4|entry(6),reserved,  fac_commoners,[itm_leather_jerkin,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e600452c32ef8e5bb92cf1c970000000000000fc20000000000000000],
  ["trainer_5","Trainer","Trainer",tf_hero, scn_training_ground_ranged_melee_5|entry(6),reserved,  fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(2),wp(20),knows_common,0x0000000e77082000150049a34c42ec960000000000000e080000000000000000],

# Ransom brokers.
  ["ransom_broker_1","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_2","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_3","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_4","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_short_tunic,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_5","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_6","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_blue_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_7","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_red_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_8","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_9","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["ransom_broker_10","Ransom_Broker","Ransom_Broker",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern traveler.
  ["tavern_traveler_1","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_2","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_3","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_vest,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_4","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_blue_gambeson,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_5","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_short_tunic,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_6","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_7","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_8","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_tabard,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_9","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_traveler_10","Traveller","Traveller",tf_hero|tf_randomize_face, 0, reserved, fac_commoners,[itm_leather_jacket,itm_hide_boots],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],

# Tavern traveler.
  ["tavern_bookseller_1","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots,
               itm_book_tactics, itm_book_persuasion, itm_book_wound_treatment_reference, itm_book_leadership, 
               itm_book_intelligence, itm_book_training_reference, itm_book_surgery_reference],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],
  ["tavern_bookseller_2","Book_Merchant","Book_Merchant",tf_hero|tf_is_merchant|tf_randomize_face, 0, reserved, fac_commoners,[itm_fur_coat,itm_hide_boots,
               itm_book_wound_treatment_reference, itm_book_leadership, itm_book_intelligence, itm_book_trade, 
               itm_book_engineering, itm_book_weapon_mastery],def_attrib|level(5),wp(20),knows_common,merchant_face_1, merchant_face_2],

# Tavern minstrel.
  ["tavern_minstrel_1","Wandering Minstrel","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_leather_jacket, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #lute
  ["tavern_minstrel_2","Wandering Bard","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_tunic_with_green_cape, itm_hide_boots, itm_lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2],  #early harp/lyre
  ["tavern_minstrel_3","Wandering Ashik","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_nomad_robe, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #lute/oud or rebab
  ["tavern_minstrel_4","Wandering Skald","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_fur_coat, itm_hide_boots, itm_lyre],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #No instrument or lyre
  ["tavern_minstrel_5","Wandering Troubadour","Minstrel",tf_hero|tf_randomize_face|tf_guarantee_shield|tf_guarantee_armor|tf_guarantee_boots, 0, reserved, fac_commoners,[itm_short_tunic, itm_hide_boots, itm_lute],def_attrib|level(5),wp(20),knows_common,merchant_face_1,merchant_face_2], #Lute or Byzantine/Occitan lyra
  
#NPC system changes begin
#Companions
  ["kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  "kingdom_heroes_including_player_begin",  tf_hero, 0,reserved,  fac_kingdom_1,[],          lord_attrib,wp(220),knows_lord_1, 0x000000000010918a01f248377289467d],

########### Channelers ############
  
  # Female Village Wisdom
  ["npc1","Seinen","Seinen",tf_hero|tf_female|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_power_player, itm_power_ammo, itm_quarter_staff, itm_woolen_dress, itm_woolen_hose],
   str_8|agi_7|int_12|cha_7|level(4),wp_polearm(65)|wp_firearm(35)|wp(27),
   knows_power_strike_1|knows_athletics_2|knows_wound_treatment_2|knows_surgery_3|knows_first_aid_2|knows_leadership_2|knows_power_draw_2|knows_fire_2|knows_earth_1|knows_spirit_3|knows_water_4|knows_air_2, #skills 2/3 player at that level
   0x0000000d25002001696289574da93b2200000000001ca3480000000000000000],
  
  # Male Rogue Channeler
  ["npc2","Darlaan","Darlaan", tf_hero|tf_unmoveable_in_party_window, 0,reserved, fac_commoners,[itm_power_player, itm_power_ammo, itm_one_handed_war_axe_b, itm_kandor_shield_weak, itm_leather_jerkin, itm_leather_boots, itm_saddle_horse],
   str_8|agi_7|int_13|cha_6|level(5),wp_firearm(47)|wp_one_handed(75)|wp(40),knows_warrior_npc|
   knows_wound_treatment_1|knows_first_aid_1|knows_leadership_1|knows_shield_2|knows_power_draw_2|knows_fire_3|knows_earth_2|knows_spirit_3|knows_water_4|knows_air_2,
   0x00000004b21002d1389b3352d8b22b1a00000000001dd6cb0000000000000000],
  
  # Female Black Ajah
  ["npc3","Cetaleen","Cetaleen",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved, fac_commoners,[itm_power_player, itm_power_ammo, itm_dagger, itm_aes_sedai_grey_dress, itm_aes_sedai_grey_shoes, itm_lady_dress_blue, itm_woolen_hose, itm_courser],
   str_5|agi_7|int_14|cha_11|level(2),wp_firearm(65)|wp(30),
   knows_wound_treatment_2|knows_trade_1|knows_first_aid_3|knows_surgery_2|knows_riding_3|knows_persuasion_3|knows_leadership_3|knows_power_draw_2|knows_fire_4|knows_earth_2|knows_spirit_4|knows_water_4|knows_air_3,
   0x00000005b904300438e148bb5d8522d300000000001dc4530000000000000000],

  # Male Asha'man
  ["npc4","Jayn","Jayn",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_power_player, itm_power_ammo, itm_sword_medieval_a, itm_cairhien_shield_weak, itm_ashaman_soldier_coat, itm_black_leather_boots],
   str_10|agi_9|int_13|cha_10|level(8),wp_one_handed(95)|wp_firearm(63)|wp(50),knows_warrior_npc|
   knows_weapon_master_2|knows_power_strike_2|knows_riding_2|knows_athletics_2|knows_power_throw_2|knows_first_aid_1|knows_surgery_1|knows_tactics_2|knows_leadership_2|knows_persuasion_1|knows_power_draw_2|knows_fire_5|knows_earth_3|knows_spirit_3|knows_water_4|knows_air_2,
   0x00000004130041534955d1b35c8ce6d200000000001ce3230000000000000000],

  # Female Liberated Damane
  ["npc5","Zonnein","Zonnein",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_power_player, itm_power_ammo, itm_dagger, itm_peasant_dress,itm_woolen_hose],
   str_9|agi_9|int_12|cha_7|level(5),wp_firearm(72)|wp(35),
   knows_riding_1|knows_power_strike_1|knows_athletics_2|knows_wound_treatment_1|knows_surgery_1|knows_first_aid_1|knows_power_draw_3|knows_fire_4|knows_earth_2|knows_spirit_4|knows_water_4|knows_air_2,
   0x000000058b001003396bb2b6e26dbb6500000000001f56e40000000000000000],

  # Female Windfinder
  ["npc6","Eldriva","Eldriva",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_power_player, itm_power_ammo, itm_scimitar, itm_archers_vest, itm_peasant_dress],
   str_8|agi_12|int_10|cha_5|level(4),wp_one_handed(80)|wp_firearm(49),
   knows_weapon_master_1|knows_power_strike_1|knows_athletics_3|knows_trainer_1|knows_leadership_1|knows_spotting_1|knows_trade_3|knows_power_draw_2|knows_fire_4|knows_earth_1|knows_spirit_3|knows_water_4|knows_air_3,
  0x0000000222104003430b75a9265358de00000000001cdb230000000000000000],

########### Non-Channelers ############
  
  # Male Ogier
  ["npc7","Haludar","Haludar",tf_ogier_male|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_long_axe, itm_tribal_warrior_outfit, itm_hunter_boots],
   str_12|agi_6|int_13|cha_8|level(10),wp_two_handed(75)|wp(50),knows_tracker_npc|
   knows_wound_treatment_1|knows_persuasion_1|knows_engineer_2,
   0x000000060b1045c45f3ffd68fc98d8a300000000001eb97f0000000000000000],

  # Male Darkfriend
  ["npc8","Peluir","Peluir",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_padded_leather, itm_leather_boots, itm_butchering_knife, itm_short_bow, itm_arrows, itm_military_cleaver_b, itm_saddle_horse],
   str_11|agi_10|int_9|cha_6|level(7),wp_one_handed(80)|wp(70),knows_warrior_npc|
   knows_power_draw_2|knows_looting_1|knows_prisoner_management_2|knows_spotting_1|knows_pathfinding_1|knows_tracking_1|knows_leadership_2|knows_tactics_1,
   0x000000060010541046de6a7aec6e4d9c000000000015c4e40000000000000000],

  # Male Two Rivers Archer
  ["npc9","Celin","Celin",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_spear, itm_long_bow, itm_bodkin_arrows, itm_leather_jerkin, itm_leather_cap, itm_leather_boots],
   str_9|agi_12|int_7|cha_8|level(5),wp_archery(100)|wp_polearm(70)|wp(50),knows_tracker_npc|knows_warrior_npc|
   knows_athletics_3|knows_pathfinding_2|knows_spotting_2|knows_tracking_3|knows_tactics_1|knows_power_strike_1|knows_power_draw_3,
   0x000000061f08518f24924f26ed76d56b00000000001cab590000000000000000],

  # Female Illian Smuggler
  ["npc10","Maigue","Maigue",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_cudgel, itm_leather_vest],
   str_8|agi_14|int_13|cha_11|level(4),wp_one_handed(70)|wp(60),
   knows_weapon_master_1|knows_tactics_1|knows_leadership_1|knows_power_strike_1|knows_athletics_2|knows_looting_4|knows_inventory_management_3|knows_prisoner_management_1|knows_trade_3|knows_persuasion_2|knows_spotting_1|knows_pathfinding_2,
   0x000000073a08000255a42de74d6e489800000000001db2aa0000000000000000],

  # Male Cairhien University Student
  ["npc11","Aloien","Aloien",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_dagger, itm_linen_tunic, itm_woolen_hose],
   str_8|agi_8|int_15|cha_11|level(2),wp_one_handed(40)|wp(30),
   knows_trainer_1|knows_tactics_1|knows_engineer_5|knows_trade_1|knows_inventory_management_2,
   0x0000000af900139338cb5488dc9948de00000000001ed4cd0000000000000000],

  # Female Gleeman
  ["npc12","Lalea","Lalea",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_pilgrim_disguise,itm_nomad_boots, itm_throwing_knives],
   str_8|agi_7|int_13|cha_14|level(4),wp_throwing(65)|wp(45),knows_merchant_npc|
   knows_ironflesh_1|knows_power_throw_3|knows_wound_treatment_1|knows_athletics_1|knows_persuasion_3|knows_leadership_2,
   0x00000001ee0c00064f1d99c95552672b00000000001e47140000000000000000],

  # Male Borderland Soldier
  ["npc13","Lasan","Lasan",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_trolloc_mace, itm_lance, itm_studded_leather_coat, itm_leather_boots, itm_leather_gloves, itm_skullcap, itm_hunter],
   str_14|agi_11|int_10|cha_8|level(10),wp_polearm(110)|wp_one_handed(100)|wp(80),knows_warrior_npc|
   knows_riding_3|knows_leadership_2|knows_athletics_2|knows_ironflesh_2|knows_power_strike_2|knows_weapon_master_3|knows_spotting_1|knows_pathfinding_1|knows_tracking_1|knows_first_aid_1|knows_wound_treatment_1,
   0x0000000dbf00434b4ab3aa691b524c6100000000001e2b6e0000000000000000],

  # Female Aiel Maiden of the Spear
  ["npc14","Nienlea","Nienlea",tf_female|tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_aiel_spear, itm_nomad_bow, itm_arrows, itm_cadinsor_green, itm_cadinsor_boots_green, itm_shoufa_green],
   str_10|agi_15|int_10|cha_8|level(5),wp_polearm(100)|wp_archery(90)|wp(60),knows_warrior_npc|
   knows_spotting_3|knows_pathfinding_3|knows_tracking_3|knows_weapon_master_2|knows_power_strike_2|knows_power_draw_1|knows_looting_2|knows_athletics_5|knows_wound_treatment_1,
   0x0000000080100007352455cd0c51495500000000001e48660000000000000000],

  # Male Seanchan Farmer
  ["npc15","Sedrar","Sedrar",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_spear, itm_butchering_knife, itm_leather_apron, itm_leather_boots],
   str_11|agi_10|int_8|cha_8|level(7),wp_polearm(85)|wp(55),
   knows_wound_treatment_1|knows_engineer_2|knows_trade_4|knows_tracking_1|knows_spotting_1|knows_pathfinding_1|knows_power_strike_1|knows_ironflesh_2|knows_inventory_management_2,
   0x00000008880c758736fa95349e59b93100000000001ddaa10000000000000000],

  # Male Hunter for the Horn
  ["npc16","Hammaeus","Hammaeus",tf_hero|tf_unmoveable_in_party_window, 0, reserved,  fac_commoners,[itm_sword_khergit_1, itm_nomad_bow, itm_arrows, itm_nomad_armor, itm_nomad_boots, itm_steppe_horse],
   str_7|agi_11|int_8|cha_7|level(5),wp_archery(100)|wp_one_handed(90)|wp(80),knows_tracker_npc|
   knows_horse_archery_3|knows_riding_3|knows_wound_treatment_2|knows_trade_1|knows_inventory_management_1|knows_athletics_2|knows_power_strike_1,
   0x00000005090c050d54ed90b9257666d900000000001dd4ca0000000000000000],
  
#NPC system changes end

## Kingdom Leaders

#governers olgrel rasevas                                                                        Horse          Bodywear                Footwear_in                     Footwear_out                    Armor                       Weapon                  Shield                  Headwear
  ["kingdom_1_lord",  "The Dragon Reborn Rand al'Thor",  "Rand",  tf_hero, 0,reserved,  fac_kingdom_1,[itm_lord_warhorse_5, itm_rich_outfit, itm_leather_boots, itm_shynbaulds_wot, itm_legion_plate, itm_gauntlets, itm_power_player, itm_power_ammo], knight_attrib_5,wp_firearm(350)|wp_one_handed(300)|wp(200),knight_skills_5|knows_trainer_7|knows_power_draw_10|knows_fire_10|knows_earth_10|knows_spirit_10|knows_water_10|knows_air_10, 0x000000000b042004492371a51c71b8e400000000001dc6e40000000000000000],
  ["kingdom_2_lord",  "Matrim Cauthon", "Mat", tf_hero, 0, reserved,  fac_kingdom_2, [itm_hunter, itm_mats_hat, itm_red_hand_plate, itm_red_hand_greaves, itm_leather_gloves, itm_ashandarei], knight_attrib_5,wp_polearm(330)|wp(250),knight_skills_5|knows_trainer_7, 0x000000003d04100448dc92392471c91c00000000001d47250000000000000000],
  ["kingdom_3_lord",  "Perrin Aybara", "Perrin", tf_hero, 0, reserved,  fac_kingdom_3, [itm_hunter, itm_two_rivers_armor, itm_leather_boots, itm_leather_gloves, itm_warhammer], knight_attrib_5,wp_two_handed(300)|wp(250),knight_skills_5|knows_trainer_4, 0x0000000837041181596d91b96c72bb2400000000001ec7550000000000000000],

  ["kingdom_4_lord",  "Berelain sur Paendrag Paeron", "Berelain", tf_hero|tf_female, 0, reserved,  fac_kingdom_4, [itm_courser, itm_sarranid_lady_dress_b, itm_woolen_hose, itm_sword_medieval_b_small], knight_attrib_2,wp_one_handed(165)|wp(160),knight_skills_2|knows_trainer_5, 0x000000003f001001469992289184a69200000000001cb6cb0000000000000000],
  ["kingdom_5_lord",  "Lord Semaradrid Maravin",  "Semaradrid",  tf_hero, 0,reserved,  fac_kingdom_5,[itm_lord_warhorse_2, itm_courtly_outfit, itm_leather_boots, itm_shynbaulds_wot, itm_cairhien_plate, itm_gauntlets, itm_great_sword, itm_cairhien_helmet], knight_attrib_5,wp_two_handed(250)|wp(220),knight_skills_5|knows_trainer_4, 0x0000000de7045003371b72371c8db8d400000000001db8e30000000000000000],
  ["kingdom_6_lord",  "King Mattin Stepaneos", "Mattin", tf_hero, 0, reserved,  fac_kingdom_6, [itm_hunter, itm_illian_companion_captain_surcoat, itm_mail_chausses, itm_scale_gauntlets, itm_illian_helmet, itm_two_handed_cleaver], knight_attrib_4,wp_two_handed(220)|wp(130),knight_skills_4|knows_trainer_3, illian_man_face_old],
  ["kingdom_7_lord",  "King Roedran Almaric do Arreloa a'Naloy", "Roedran", tf_hero, 0, reserved,  fac_kingdom_7, [itm_charger, itm_murandy_elite_armor, itm_mail_chausses, itm_mail_mittens, itm_nordic_huscarl_helmet, itm_military_hammer, itm_murandy_shield_strong],   knight_attrib_3,wp_one_handed(220)|wp(130),knight_skills_3|knows_trainer_3, murandy_man_face_old],
  ["kingdom_8_lord",  "King Beslan Mitsobar", "Beslan", tf_hero, 0, reserved,  fac_kingdom_8, [itm_arabian_horse_b, itm_altara_royal_guard_armor, itm_altara_royal_guard_boots, itm_scale_gauntlets, itm_altara_royal_guard_helmet, itm_khergit_sword_two_handed_a], knight_attrib_4,wp_two_handed(245)|wp(160),knight_skills_4|knows_trainer_4, altara_man_face_young],
  ["kingdom_9_lord",  "King Alsalam Saeed Almadar", "Alsalam", tf_hero, 0, reserved,  fac_kingdom_9, [itm_lord_warhorse_6, itm_arad_doman_elite_armor, itm_splinted_greaves, itm_gauntlets, itm_nasal_helmet, itm_sword_medieval_d_long, itm_arad_doman_shield_strong], knight_attrib_3,wp_one_handed(235)|wp(220),knight_skills_3|knows_trainer_5, arad_doman_man_face_older],

  ["kingdom_10_lord", "King Darlin Sisnera", "Darlin", tf_hero, 0, reserved,  fac_kingdom_10, [itm_lord_warhorse_6, itm_tear_gilded_plate, itm_shynbaulds_wot, itm_gauntlets, itm_tear_elite_helmet, itm_sword_two_handed_b], knight_attrib_5,wp_two_handed(250)|wp(160),knight_skills_5|knows_trainer_7, tear_man_face_young],
  ["kingdom_11_lord", "Queen Elayne Trakand",  "Elayne",  tf_hero|tf_female, 0,reserved,  fac_kingdom_11,[itm_courser, itm_lady_dress_ruby, itm_woolen_hose, itm_novice_accepted_damane_shoes, itm_green_dress, itm_power_player, itm_power_ammo], knight_attrib_4,wp_firearm(275)|wp_one_handed(225)|wp(220),knight_skills_4|knows_trainer_6|knows_power_draw_8|knows_fire_7|knows_earth_7|knows_spirit_9|knows_water_8|knows_air_8, 0x00000002010c000138d4c5339a063ad300000000001ed2d30000000000000000],
  ["kingdom_12_lord", "Queen Alliandre Maritha Kigarin", "Alliandre", tf_hero|tf_female, 0, reserved,  fac_kingdom_12, [itm_courser, itm_sarranid_lady_dress_b, itm_woolen_hose, itm_sword_medieval_b_small], knight_attrib_2,wp_one_handed(165)|wp(160),knight_skills_2|knows_trainer_3, ghealdan_woman_face_middle],
  ["kingdom_13_lord", "First Counsel Aleis Barsalla", "Aleis", tf_hero|tf_female, 0, reserved,  fac_kingdom_13, [itm_courser, itm_green_dress, itm_woolen_hose, itm_sword_medieval_b_small], knight_attrib_2,wp_one_handed(165)|wp(160),knight_skills_2|knows_trainer_3, far_madding_woman_face_old],
  ["kingdom_14_lord", "Panarch Amathera Aelfdene Casmir Lounault", "Amathera", tf_hero|tf_female, 0, reserved,  fac_kingdom_14, [itm_courser, itm_khergit_lady_dress, itm_woolen_hose, itm_sword_medieval_b_small], knight_attrib_2,wp_one_handed(165)|wp(160),knight_skills_2|knows_trainer_3, tarabon_woman_face_middle],
  ["kingdom_15_lord", "King Ailron", "Ailron", tf_hero, 0, reserved,  fac_kingdom_15, [itm_charger, itm_amadicia_elite_armor, itm_shynbaulds_wot, itm_gauntlets, itm_flat_topped_helmet, itm_great_sword], knight_attrib_4,wp_two_handed(260)|wp(225),knight_skills_4|knows_trainer_4, amadicia_man_face_old],
  ["kingdom_16_lord", "Lord Captain Commander Galad Damodred", "Galad", tf_hero, 0, reserved,  fac_kingdom_16, [itm_charger, itm_whitecloak_tabbard, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_whitecloak_helmet, itm_great_sword], knight_attrib_5,wp_two_handed(310)|wp(250),knight_skills_5|knows_trainer_4, 0x00000001aa08200316dacdcc9d7188ec00000000001db7240000000000000000],

  ["kingdom_17_lord", "King Easar Togita", "Easar", tf_hero, 0, reserved,  fac_kingdom_17, [itm_heavy_charger, itm_shienar_captain_armor, itm_steel_greaves_wot, itm_shienar_captain_gauntlets, itm_winged_great_helmet, itm_sword_of_war], knight_attrib_5,wp_two_handed(275)|wp(200),knight_skills_5|knows_trainer_5, shienar_man_face_older],
  ["kingdom_18_lord", "King Paitar Neramovni Nachiman", "Paitar", tf_hero, 0, reserved,  fac_kingdom_18, [itm_charger, itm_arafel_mail_and_plate, itm_steel_greaves_wot, itm_gauntlets, itm_oniontop_bascinet_wot, itm_sword_of_war], knight_attrib_5,wp_two_handed(250)|wp(200),knight_skills_5|knows_trainer_5, arafel_man_face_older],
  ["kingdom_19_lord", "Queen Ethenielle Cosaru Noramaga", "Ethenielle", tf_hero|tf_female, 0, reserved,  fac_kingdom_19, [itm_charger, itm_brown_dress, itm_woolen_hose, itm_one_handed_battle_axe_b], knight_attrib_3,wp_one_handed(200)|wp(160),knight_skills_3|knows_trainer_4, kandor_woman_face_middle],
  ["kingdom_20_lord", "Queen Tenobia si Bashere Kazadi", "Tenobia", tf_hero|tf_female, 0, reserved,  fac_kingdom_20, [itm_lord_warhorse_1, itm_khergit_lady_dress_b, itm_woolen_hose, itm_arabian_sword_b], knight_attrib_3,wp_one_handed(200)|wp(160),knight_skills_3|knows_trainer_4, saldaea_woman_face_young],

  ["kingdom_21_lord",  "Amyrlin Seat Egwene al'Vere",  "Egwene",  tf_hero|tf_female, 0,reserved,  fac_kingdom_21,[itm_hunter, itm_lady_dress_green, itm_woolen_hose, itm_novice_accepted_damane_shoes, itm_red_dress, itm_power_player, itm_power_ammo], knight_attrib_4,wp_firearm(275)|wp_one_handed(225)|wp(220),knight_skills_4|knows_trainer_5|knows_power_draw_8|knows_fire_7|knows_earth_8|knows_spirit_9|knows_water_8|knows_air_8, 0x000000002308200344da719494adc89a00000000001d33130000000000000000],
  ["kingdom_22_lord",  "Clan Chief Rhuarc",  "Rhuarc",  tf_hero, 0,reserved,  fac_kingdom_22,[itm_cadinsor, itm_cadinsor_boots, itm_shoufa, itm_aiel_spear, itm_hide_buckler_strong], knight_attrib_5,wp_polearm(325)|wp(300),knight_skills_5|knows_trainer_5, 0x0000000db304100536d38db6e46dcae500000000001e492b0000000000000000],
  ["kingdom_23_lord",  "Empress Fortuona Athaem Devi Paendrig",  "Fortuona",  tf_hero|tf_female, 0,reserved,  fac_kingdom_23,[itm_lord_warhorse_7, itm_sarranid_lady_dress, itm_novice_accepted_damane_shoes, itm_seanchan_sword], knight_attrib_4,wp_two_handed(260)|wp(250),knight_skills_4|knows_trainer_5, 0x00000000050c40003325c5331dc8b5a300000000001e44a40000000000000000],
  ["kingdom_24_lord",  "Shaidar Haran",  "Shaidar Haran",  tf_hero, 0,reserved,  fac_kingdom_24,[itm_myrddraal_horse, itm_myrddraal_armor, itm_black_leather_boots, itm_myrddraal_hood_helmet, itm_black_mail_gauntlets, itm_myrddraal_blade], knight_attrib_5,wp_two_handed(325)|wp(300),knight_skills_5|knows_trainer_5, 0x000000033604400933a5d2329c72461600000000001cc7230000000000000000],

  ["kingdom_25_lord",  "Sh'botay Shaofan",  "Shofan",  tf_hero, 0,reserved,  fac_kingdom_25,[itm_lord_warhorse_8, itm_khergit_sword_two_handed_b, itm_shara_shbo_guardsman_armor, itm_lamellar_gauntlets, itm_brass_boots, itm_brass_veil_helm], knight_attrib_5,wp_two_handed(300)|wp(300),knight_skills_5|knows_trainer_5, seanchan_2_man_face_middle],
  ["kingdom_26_lord",  "Mistress of the Ships Zaida din Parede Blackwing",  "Zaida",  tf_hero|tf_female, 0,reserved,  fac_kingdom_26,[itm_scimitar_b, itm_sea_folk_female_armor, itm_leather_covered_round_shield, itm_leather_gloves], knight_attrib_5,wp_one_handed(275)|wp(300),knight_skills_5|knows_trainer_5, seanchan_2_woman_face_middle],
  ["kingdom_27_lord",  "High Chief Pergath",  "Pergath",  tf_hero, 0,reserved,  fac_kingdom_27,[itm_hunter, itm_great_long_bardiche, itm_hammer, itm_lamellar_vest_khergit, itm_leather_boots, itm_leather_gloves, itm_khergit_war_helmet], knight_attrib_5,wp_polearm(325)|wp(300),knight_skills_5|knows_trainer_5, kandor_man_face_older],
  ["kingdom_28_lord",  "First Watcher Baladum",  "Baladum",  tf_hero, 0,reserved,  fac_kingdom_28,[itm_charger, itm_great_sword, itm_toman_head_mail_and_plate, itm_mail_chausses, itm_leather_gloves, itm_nasal_helmet], knight_attrib_5,wp_two_handed(310)|wp(300),knight_skills_5|knows_trainer_5, arad_doman_man_face_old],
  
# V: New faces for Rand, Semaradrid, Lan, Rhuarc


#    Imbrea   Belinda Ruby Qaelmas Rose    Willow 
#  Alin  Ganzo            Zelka Rabugti
#  Qlurzach Ruhbus Givea_alsev  Belanz        Bendina  
# Dunga        Agatha     Dibus Crahask
  
#                                                                               Horse                   Bodywear                Armor                               Footwear_in                 Footwear_out                        Headwear                    Weapon               Shield
  #Swadian civilian clothes: itm_courtly_outfit itm_gambeson itm_blue_gambeson itm_red_gambeson itm_nobleman_outfit itm_rich_outfit itm_short_tunic itm_tabard
  #Older knights with higher skills moved to top


# Legion of the Dragon
  ["knight_1_1", "Damer Flinn", "Flinn", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter, itm_ashaman_coat, itm_black_leather_boots, itm_power_player, itm_power_ammo], knight_attrib_4,wp_firearm(325)|wp_one_handed(220)|wp(200),knight_skills_4|knows_trainer_3|knows_power_draw_9|knows_fire_9|knows_earth_9|knows_spirit_10|knows_water_9|knows_air_9, 0x0000000edc08314026a272a7624f522100000000001e491d0000000000000000],
  ["knight_1_2", "Logain Ablar", "Logain", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter, itm_ashaman_coat, itm_black_leather_boots, itm_power_player, itm_power_ammo], knight_attrib_4,wp_firearm(325)|wp_one_handed(220)|wp(200),knight_skills_4|knows_trainer_3|knows_power_draw_10|knows_fire_10|knows_earth_10|knows_spirit_9|knows_water_9|knows_air_9, 0x00000005b104410924dc7238e3725b2d00000000001da9220000000000000000],
  ["knight_1_3", "Jahar Narishma", "Narishma", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter, itm_ashaman_coat, itm_black_leather_boots, itm_power_player, itm_power_ammo], knight_attrib_4,wp_firearm(325)|wp_one_handed(220)|wp(200),knight_skills_4|knows_trainer_3|knows_power_draw_9|knows_fire_10|knows_earth_9|knows_spirit_9|knows_water_9|knows_air_9, far_madding_man_face_younger],
  ["knight_1_4", "Elmindreda Farshaw", "Min", tf_hero|tf_female, 0, reserved,  fac_kingdom_1, [itm_hunter, itm_brown_dress, itm_leather_boots, itm_aiel_knife, itm_throwing_knives], knight_attrib_2,wp_throwing(200)|wp_one_handed(150)|wp(130),knight_skills_1, 0x000000006100100748e191b69b8db65900000000001db89b0000000000000000],
  ["knight_1_5", "Donalo Sandomere", "Donalo", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter, itm_ashaman_coat, itm_black_leather_boots, itm_power_player, itm_power_ammo], knight_attrib_4,wp_firearm(250)|wp_one_handed(220)|wp(200),knight_skills_4|knows_trainer_3|knows_power_draw_7|knows_fire_8|knows_earth_8|knows_spirit_7|knows_water_7|knows_air_7, tear_man_face_middle],
  ["knight_1_6", "Fager Neald", "Neald", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter, itm_ashaman_coat, itm_black_leather_boots, itm_power_player, itm_power_ammo], knight_attrib_4,wp_firearm(250)|wp_one_handed(220)|wp(200),knight_skills_4|knows_trainer_3|knows_power_draw_8|knows_fire_8|knows_earth_7|knows_spirit_7|knows_water_7|knows_air_7, murandy_man_face_middle],
  ["knight_1_7", "Jur Grady", "Grady", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter, itm_ashaman_coat, itm_black_leather_boots, itm_power_player, itm_power_ammo], knight_attrib_4,wp_firearm(250)|wp_one_handed(220)|wp(200),knight_skills_4|knows_trainer_3|knows_power_draw_8|knows_fire_7|knows_earth_8|knows_spirit_8|knows_water_7|knows_air_7, andor_man_face_middle],


# Band of the Red Hand
  ["knight_2_1", "Lord Talmanes Delovinde", "Talmanes", tf_hero, 0, reserved,  fac_kingdom_2, [itm_charger, itm_red_hand_plate, itm_red_hand_greaves, itm_red_hand_plate_gauntlets, itm_red_hand_kettle_helm, itm_great_sword],   knight_attrib_3,wp_two_handed(250)|wp(130),knight_skills_3|knows_trainer_3, 0x00000009a50435d4491c7236db52472500000000001d27220000000000000000], 
  ["knight_2_2", "Daerid Ondin", "Daerid", tf_hero, 0, reserved,  fac_kingdom_2, [itm_charger, itm_red_hand_plate, itm_red_hand_greaves, itm_red_hand_plate_gauntlets, itm_red_hand_kettle_helm, itm_great_sword],   knight_attrib_3,wp_two_handed(250)|wp(130),knight_skills_3|knows_trainer_3, cairhien_man_face_old],
  ["knight_2_3", "Harnan", "Harnan", tf_hero, 0, reserved,  fac_kingdom_2, [itm_charger, itm_red_hand_plate, itm_red_hand_greaves, itm_red_hand_plate_gauntlets, itm_red_hand_kettle_helm, itm_great_sword],   knight_attrib_3,wp_two_handed(250)|wp(130),knight_skills_3|knows_trainer_3, illian_man_face_middle],
  ["knight_2_4", "Chel Vanin", "Chel Vanin", tf_hero, 0, reserved,  fac_kingdom_2, [itm_charger, itm_red_hand_plate, itm_red_hand_greaves, itm_red_hand_plate_gauntlets, itm_red_hand_kettle_helm, itm_great_sword],   knight_attrib_3|knows_trainer_4,wp_two_handed(250)|wp(130),knight_skills_3|knows_trainer_3, 0x0000000bfc04425348e45236e3d24b2400000000001f375b0000000000000000],
  ["knight_2_5", "Macoll", "Macoll", tf_hero, 0, reserved,  fac_kingdom_2, [itm_charger, itm_red_hand_plate, itm_red_hand_greaves, itm_red_hand_plate_gauntlets, itm_red_hand_kettle_helm, itm_great_sword],   knight_attrib_3|knows_trainer_4,wp_two_handed(250)|wp(130),knight_skills_3|knows_trainer_3, arad_doman_man_face_middle],

  
# Two Rivers  
  ["knight_3_1", "Tam al'Thor", "Tam", tf_hero, 0, reserved,  fac_kingdom_3, [itm_hunter, itm_two_rivers_armor, itm_leather_boots, itm_leather_gloves, itm_two_rivers_long_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_large_heron_mark_blade], knight_attrib_4,wp_archery(320)|wp_two_handed(300)|wp(250),knight_skills_4|knows_trainer_4, 0x0000000ebf04614436d39596a4924aed00000000001dab1a0000000000000000],
  ["knight_3_2", "Brandelwyn al'Vere", "Bran", tf_hero, 0, reserved,  fac_kingdom_3, [itm_hunter, itm_two_rivers_armor, itm_leather_boots, itm_segmented_helmet, itm_leather_gloves, itm_halberd], knight_attrib_3,wp_polearm(220)|wp(200),knight_skills_3|knows_trainer_4, 0x0000000efc0411524b1c7236e3d24b2400000000001f49230000000000000000],
  ["knight_3_3", "Abell Cauthon", "Abell", tf_hero, 0, reserved,  fac_kingdom_3, [itm_hunter, itm_two_rivers_armor, itm_leather_boots, itm_leather_gloves, itm_two_rivers_long_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_large_heron_mark_blade], knight_attrib_4,wp_archery(320)|wp_two_handed(300)|wp(250),knight_skills_4|knows_trainer_4, andor_man_face_old],
  ["knight_3_4", "Ban al'Seen", "Ban", tf_hero, 0, reserved,  fac_kingdom_3, [itm_hunter, itm_two_rivers_armor, itm_leather_boots, itm_segmented_helmet, itm_leather_gloves, itm_halberd], knight_attrib_3,wp_polearm(220)|wp(200),knight_skills_3|knows_trainer_4, andor_man_face_young],
  ["knight_3_5", "Elyas Machera", "Elyas", tf_hero, 0, reserved,  fac_kingdom_3, [itm_pelt_coat, itm_hide_boots, itm_leather_gloves, itm_aiel_knife], knight_attrib_5,wp_one_handed(275)|wp(240),knight_skills_5|knows_trainer_5, 0x0000000d870861c738db71c924cdcb2400000000001f49230000000000000000],

# V: New faces for Mat, Perrin, Elyas, Tam, Talmanes, Logain, Bran, Vanin, Min (also fixed name)

  
#  ["knight_1_21", "Lord Swadian 21", "knight_1_7", tf_hero, 0, reserved,  fac_kingdom_1, [itm_saddle_horse,      itm_ragged_outfit,      itm_heraldic_mail_with_surcoat,           itm_nomad_boots,            itm_splinted_greaves,                itm_great_helmet, itm_gauntlets,           itm_sword_medieval_c,   itm_sword_two_handed_a,   itm_tab_shield_heater_cav_a],   knight_attrib_2,wp(150),knight_skills_2, 0x0000000c4d0840d24a9b2ab4ac2a332400000000001d34db0000000000000000, swadian_face_young_2],
 # ["knight_1_22", "Lord Swadian 22", "knight_1_8", tf_hero, 0, reserved,  fac_kingdom_1, [itm_saddle_horse,      itm_short_tunic,       itm_heraldic_mail_with_surcoat,           itm_leather_boots,          itm_mail_chausses,                   itm_winged_great_helmet, itm_gauntlets,       itm_bastard_sword_a,  itm_sword_two_handed_a,  itm_tab_shield_heater_d],    knight_attrib_3,wp(180),knight_skills_3|knows_trainer_4, 0x0000000c370c1194546469ca6c4e450e00000000001ebac40000000000000000, swadian_face_older_2],
#  ["knight_1_23", "Lord Swadian 23", "knight_1_9", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter,            itm_rich_outfit,        itm_mail_hauberk,                   itm_woolen_hose,            itm_mail_chausses,                   itm_guard_helmet, itm_gauntlets,         itm_sword_medieval_c,    itm_tab_shield_heater_d],      knight_attrib_4,wp(200),knight_skills_4|knows_trainer_6, 0x0000000c0c1064864ba34e2ae291992b00000000001da8720000000000000000, swadian_face_older_2],
#  ["knight_1_24", "Lord Swadian 24", "knight_1_0", tf_hero, 0, reserved,  fac_kingdom_1, [itm_hunter,            itm_tabard,      itm_heraldic_mail_with_surcoat,               itm_leather_boots,          itm_mail_boots,                      itm_winged_great_helmet, itm_gauntlets, itm_bastard_sword_b, itm_sword_two_handed_b,  itm_tab_shield_heater_cav_b], knight_attrib_5,wp(240),knight_skills_5|knows_trainer_5, 0x0000000c0a08038736db74c6a396a8e500000000001db8eb0000000000000000, swadian_face_older_2],

  
#Southland Coalition (Mayene, Cairhien, Illian, Murandy, Altara, Arad Doman)
  
# Mayene
  ["knight_4_1", "Captain Bertain Gallenne", "Bertain", tf_hero, 0, reserved,  fac_kingdom_4, [itm_lord_warhorse_2, itm_mayene_plate, itm_mayene_greaves, itm_mayene_gauntlets_red, itm_mayene_winged_guard_helmet, itm_sword_of_war], knight_attrib_4,wp_two_handed(245)|wp(220),knight_skills_4|knows_trainer_3, mayene_man_face_old],
  ["knight_4_2", "Captain Havien Nurelle", "Havien", tf_hero, 0, reserved,  fac_kingdom_4, [itm_lord_warhorse_2, itm_mayene_plate, itm_mayene_greaves, itm_mayene_gauntlets_red, itm_mayene_winged_guard_helmet, itm_sword_of_war], knight_attrib_4,wp_two_handed(245)|wp(220),knight_skills_4|knows_trainer_3, mayene_man_face_young],


# Cairhien
  ["knight_5_1", "Lord Dalthanes Annallin", "Dalthanes", tf_hero, 0, reserved,  fac_kingdom_5, [itm_lord_warhorse_2, itm_cairhien_plate, itm_shynbaulds_wot, itm_gauntlets, itm_cairhien_helmet, itm_great_sword], knight_attrib_3,wp_two_handed(200)|wp(170),knight_skills_3|knows_trainer_4, cairhien_man_face_middle],
  ["knight_5_2", "Lord Barmanes Nolaisen", "Barmanes", tf_hero, 0, reserved,  fac_kingdom_5, [itm_lord_warhorse_2, itm_cairhien_plate, itm_shynbaulds_wot, itm_gauntlets, itm_cairhien_helmet, itm_great_sword], knight_attrib_3,wp_two_handed(200)|wp(170),knight_skills_3|knows_trainer_4, cairhien_man_face_old],
  ["knight_5_3", "Lord Dobraine Taborwin", "Dobraine", tf_hero, 0, reserved,  fac_kingdom_5, [itm_lord_warhorse_2, itm_cairhien_plate, itm_shynbaulds_wot, itm_gauntlets, itm_cairhien_helmet, itm_great_sword], knight_attrib_4,wp_two_handed(210)|wp(170),knight_skills_4|knows_trainer_4, cairhien_man_face_older],
  ["knight_5_4", "Lady Selande Darengil", "Selande", tf_hero|tf_female, 0, reserved,  fac_kingdom_5, [itm_courser, itm_lady_dress_blue, itm_woolen_hose, itm_sword_medieval_b_small], knight_attrib_2,wp_one_handed(165)|wp(160),knight_skills_2|knows_trainer_3, cairhien_woman_face_younger],
  ["knight_5_5", "Lady Caraline Damodred", "Caraline", tf_hero|tf_female, 0, reserved,  fac_kingdom_5, [itm_courser, itm_lady_dress_blue, itm_woolen_hose, itm_sword_medieval_b_small], knight_attrib_2,wp_one_handed(165)|wp(160),knight_skills_2|knows_trainer_3, cairhien_woman_face_young],
  ["knight_5_6", "Lady Alil Riatin", "Alil", tf_hero|tf_female, 0, reserved,  fac_kingdom_5, [itm_courser, itm_lady_dress_blue, itm_woolen_hose, itm_sword_medieval_b_small], knight_attrib_2,wp_one_handed(165)|wp(160),knight_skills_2|knows_trainer_3, cairhien_woman_face_younger],
  ["knight_5_7", "Lord Bertome Saighan", "Bertome", tf_hero, 0, reserved,  fac_kingdom_5, [itm_lord_warhorse_2, itm_cairhien_plate, itm_shynbaulds_wot, itm_gauntlets, itm_cairhien_helmet, itm_great_sword], knight_attrib_3,wp_two_handed(200)|wp(170),knight_skills_3|knows_trainer_4, cairhien_man_face_older],


# Illian
  ["knight_6_1", "Lord Jeordwyn Semaris", "Jeordwyn", tf_hero, 0, reserved,  fac_kingdom_6, [itm_hunter, itm_illian_companion_captain_surcoat, itm_mail_chausses, itm_scale_gauntlets, itm_illian_helmet, itm_two_handed_cleaver], knight_attrib_4,wp_two_handed(220)|wp(130),knight_skills_4|knows_trainer_3, illian_man_face_middle],
  ["knight_6_2", "Lord Lidrin", "Lidrin", tf_hero, 0, reserved,  fac_kingdom_6, [itm_hunter, itm_illian_companion_captain_surcoat, itm_mail_chausses, itm_scale_gauntlets, itm_illian_helmet, itm_two_handed_cleaver], knight_attrib_4,wp_two_handed(220)|wp(130),knight_skills_4|knows_trainer_3, illian_man_face_older],
  ["knight_6_3", "Lord Spiron Narettin", "Spiron", tf_hero, 0, reserved,  fac_kingdom_6, [itm_hunter, itm_illian_companion_captain_surcoat, itm_mail_chausses, itm_scale_gauntlets, itm_illian_helmet, itm_two_handed_cleaver], knight_attrib_4,wp_two_handed(220)|wp(130),knight_skills_4|knows_trainer_3, illian_man_face_young],
  ["knight_6_4", "Lord Vivian", "Vivian", tf_hero, 0, reserved,  fac_kingdom_6, [itm_hunter, itm_illian_companion_captain_surcoat, itm_mail_chausses, itm_scale_gauntlets, itm_illian_helmet, itm_two_handed_cleaver], knight_attrib_4,wp_two_handed(220)|wp(130),knight_skills_4|knows_trainer_3, illian_man_face_middle],
  ["knight_6_5", "Lord Gregorin den Lushenos", "Gregorin", tf_hero, 0, reserved,  fac_kingdom_6, [itm_hunter, itm_illian_companion_captain_surcoat, itm_mail_chausses, itm_scale_gauntlets, itm_illian_helmet, itm_two_handed_cleaver], knight_attrib_3,wp_two_handed(220)|wp(130),knight_skills_3|knows_trainer_3, illian_man_face_older],
  ["knight_6_6", "Lord Kiril Drapeneos", "Kiril", tf_hero, 0, reserved,  fac_kingdom_6, [itm_hunter, itm_illian_companion_captain_surcoat, itm_mail_chausses, itm_scale_gauntlets, itm_illian_helmet, itm_two_handed_cleaver], knight_attrib_3,wp_two_handed(220)|wp(130),knight_skills_3|knows_trainer_3, illian_man_face_old],
  ["knight_6_7", "Lord Ballin Elamri", "Ballin", tf_hero, 0, reserved,  fac_kingdom_6, [itm_hunter, itm_illian_companion_captain_surcoat, itm_mail_chausses, itm_scale_gauntlets, itm_illian_helmet, itm_two_handed_cleaver], knight_attrib_3,wp_two_handed(200)|wp(170),knight_skills_3|knows_trainer_3, cairhien_man_face_younger],

  
# Murandy
  ["knight_7_1", "Lady Segan do Avharin a'Roos", "Segan", tf_hero|tf_female, 0, reserved,  fac_kingdom_7, [itm_courser, itm_brown_dress, itm_woolen_hose, itm_spiked_mace, itm_murandy_shield_normal], knight_attrib_2,wp_one_handed(160)|wp(150),knight_skills_2|knows_trainer_4, murandy_woman_face_middle],
  ["knight_7_2", "Lord Paitr do Fearna a'Conn", "Paitr", tf_hero, 0, reserved,  fac_kingdom_7, [itm_charger, itm_murandy_elite_armor, itm_mail_chausses, itm_mail_mittens, itm_nordic_huscarl_helmet, itm_military_hammer, itm_murandy_shield_strong],   knight_attrib_3,wp_one_handed(220)|wp(130),knight_skills_3|knows_trainer_3, murandy_man_face_middle],
  ["knight_7_3", "Lord Sedrin do Meri a'Conlin", "Sedrin", tf_hero, 0, reserved,  fac_kingdom_7, [itm_charger, itm_murandy_elite_armor, itm_mail_chausses, itm_mail_mittens, itm_nordic_huscarl_helmet, itm_military_hammer, itm_murandy_shield_strong],   knight_attrib_3,wp_one_handed(220)|wp(130),knight_skills_3|knows_trainer_3, murandy_man_face_young],
  ["knight_7_4", "Lord Donel do Morny a'Lordeine", "Donel", tf_hero, 0, reserved,  fac_kingdom_7, [itm_charger, itm_murandy_elite_armor, itm_mail_chausses, itm_mail_mittens, itm_nordic_huscarl_helmet, itm_military_hammer, itm_murandy_shield_strong],   knight_attrib_3,wp_one_handed(220)|wp(130),knight_skills_3|knows_trainer_3, murandy_man_face_older],
  ["knight_7_5", "Lady Cian do Mehon a'Macansa", "Cian", tf_hero|tf_female, 0, reserved,  fac_kingdom_7, [itm_courser, itm_brown_dress, itm_woolen_hose, itm_spiked_mace, itm_murandy_shield_normal], knight_attrib_2,wp_one_handed(160)|wp(150),knight_skills_2|knows_trainer_4, murandy_woman_face_middle],
  ["knight_7_6", "Lord Conran do Dantin a'Moredar", "Conran", tf_hero, 0, reserved,  fac_kingdom_7, [itm_charger, itm_murandy_elite_armor, itm_mail_chausses, itm_mail_mittens, itm_nordic_huscarl_helmet, itm_military_hammer, itm_murandy_shield_strong],   knight_attrib_2,wp_one_handed(220)|wp(130),knight_skills_2|knows_trainer_3, murandy_man_face_young],
  ["knight_7_7", "Lady Corele do Arman a'Llys", "Corele", tf_hero|tf_female, 0, reserved,  fac_kingdom_7, [itm_courser, itm_brown_dress, itm_woolen_hose, itm_spiked_mace, itm_murandy_shield_normal], knight_attrib_2,wp_one_handed(160)|wp(150),knight_skills_2|knows_trainer_4, murandy_woman_face_younger],


# Altara
  ["knight_8_1", "Lord Nathin Sarmain Vendare", "Nathin", tf_hero, 0, reserved,  fac_kingdom_8, [itm_arabian_horse_b, itm_altara_royal_guard_armor, itm_altara_royal_guard_boots, itm_scale_gauntlets, itm_altara_royal_guard_helmet, itm_khergit_sword_two_handed_a], knight_attrib_4,wp_two_handed(245)|wp(160),knight_skills_4|knows_trainer_4, altara_man_face_middle],
  ["knight_8_2", "Lord Malalin", "Malalin", tf_hero, 0, reserved,  fac_kingdom_8, [itm_arabian_horse_b, itm_altara_royal_guard_armor, itm_altara_royal_guard_boots, itm_scale_gauntlets, itm_altara_royal_guard_helmet, itm_khergit_sword_two_handed_a], knight_attrib_4,wp_two_handed(245)|wp(160),knight_skills_4|knows_trainer_4, altara_man_face_middle],
  ["knight_8_3", "Lady Aethelaine", "Aethelaine", tf_hero|tf_female, 0, reserved,  fac_kingdom_8, [itm_courser, itm_sarranid_lady_dress_b, itm_woolen_hose, itm_sarranid_cavalry_sword], knight_attrib_2,wp_one_handed(165)|wp(160),knight_skills_2|knows_trainer_3, altara_woman_face_middle],
  ["knight_8_4", "Lord Entin Contar", "Entin", tf_hero, 0, reserved,  fac_kingdom_8, [itm_arabian_horse_b, itm_altara_royal_guard_armor, itm_altara_royal_guard_boots, itm_scale_gauntlets, itm_altara_royal_guard_helmet, itm_khergit_sword_two_handed_a], knight_attrib_3,wp_two_handed(205)|wp(160),knight_skills_3|knows_trainer_4, altara_man_face_older],
  ["knight_8_5", "Lady Glydis Contar", "Glydis", tf_hero|tf_female, 0, reserved,  fac_kingdom_8, [itm_courser, itm_sarranid_lady_dress_b, itm_woolen_hose, itm_sarranid_cavalry_sword], knight_attrib_2,wp_one_handed(165)|wp(160),knight_skills_2|knows_trainer_3, altara_woman_face_old],
  ["knight_8_6", "Lord Brand Llewys", "Brand", tf_hero, 0, reserved,  fac_kingdom_8, [itm_arabian_horse_b, itm_altara_royal_guard_armor, itm_altara_royal_guard_boots, itm_scale_gauntlets, itm_altara_royal_guard_helmet, itm_khergit_sword_two_handed_a], knight_attrib_3,wp_two_handed(205)|wp(160),knight_skills_3|knows_trainer_4, altara_man_face_younger],
  ["knight_8_7", "Lady Alania Llewys", "Alania", tf_hero|tf_female, 0, reserved,  fac_kingdom_8, [itm_courser, itm_sarranid_lady_dress_b, itm_woolen_hose, itm_sarranid_cavalry_sword], knight_attrib_2,wp_one_handed(165)|wp(160),knight_skills_2|knows_trainer_3, altara_woman_face_younger],


# Arad Doman  
  ["knight_9_1", "Lord Rodel Ituralde", "Rodel", tf_hero, 0, reserved,  fac_kingdom_9, [itm_lord_warhorse_6, itm_arad_doman_elite_armor, itm_splinted_greaves, itm_gauntlets, itm_nasal_helmet, itm_large_heron_mark_blade], knight_attrib_5,wp_two_handed(275)|wp(250),knight_skills_5|knows_trainer_5, arad_doman_man_face_old],
  ["knight_9_2", "Lady Alamindra Cutren", "Almindra", tf_hero|tf_female, 0, reserved,  fac_kingdom_9, [itm_courser, itm_khergit_lady_dress, itm_woolen_hose, itm_sword_medieval_b_small], knight_attrib_2,wp_one_handed(165)|wp(160),knight_skills_2|knows_trainer_3, arad_doman_woman_face_old],
  ["knight_9_3", "Lord Callswell", "Callswell", tf_hero, 0, reserved,  fac_kingdom_9, [itm_lord_warhorse_6, itm_arad_doman_elite_armor, itm_splinted_greaves, itm_gauntlets, itm_nasal_helmet, itm_sword_medieval_d_long, itm_arad_doman_shield_strong], knight_attrib_3,wp_one_handed(235)|wp(220),knight_skills_3|knows_trainer_4, arad_doman_man_face_younger],
  ["knight_9_4", "Lord Tellaen", "Tellaen", tf_hero, 0, reserved,  fac_kingdom_9, [itm_lord_warhorse_6, itm_arad_doman_elite_armor, itm_splinted_greaves, itm_gauntlets, itm_nasal_helmet, itm_sword_medieval_d_long, itm_arad_doman_shield_strong], knight_attrib_3,wp_one_handed(235)|wp(220),knight_skills_3|knows_trainer_4, arad_doman_woman_face_young],

# V: New face for Berelain


#Southland Alliance (Tarabon, Far Madding, Andor, Amadicia, Ghealdan, Tear)

# Tear
  ["knight_10_1", "High Lord Torean Andiama", "Torean", tf_hero, 0, reserved,  fac_kingdom_10, [itm_lord_warhorse_6, itm_tear_gilded_plate, itm_shynbaulds_wot, itm_gauntlets, itm_tear_elite_helmet, itm_sword_two_handed_b], knight_attrib_4,wp_two_handed(210)|wp(160),knight_skills_4|knows_trainer_5, tear_man_face_old],
  ["knight_10_2", "High Lord Hearne", "Hearne", tf_hero, 0, reserved,  fac_kingdom_10, [itm_lord_warhorse_6, itm_tear_gilded_plate, itm_shynbaulds_wot, itm_gauntlets, itm_tear_elite_helmet, itm_sword_two_handed_b], knight_attrib_4,wp_two_handed(210)|wp(160),knight_skills_4|knows_trainer_5, tear_man_face_middle],
  ["knight_10_3", "High Lord Sunamon Haellin", "Sunamon", tf_hero, 0, reserved,  fac_kingdom_10, [itm_lord_warhorse_6, itm_tear_gilded_plate, itm_shynbaulds_wot, itm_gauntlets, itm_tear_elite_helmet, itm_sword_two_handed_b], knight_attrib_4,wp_two_handed(210)|wp(160),knight_skills_4|knows_trainer_5, tear_man_face_older],
  ["knight_10_4", "High Lord Tedosian", "Tedosian", tf_hero, 0, reserved,  fac_kingdom_10, [itm_lord_warhorse_6, itm_tear_gilded_plate, itm_shynbaulds_wot, itm_gauntlets, itm_tear_elite_helmet, itm_sword_two_handed_b], knight_attrib_4,wp_two_handed(210)|wp(160),knight_skills_4|knows_trainer_5, tear_man_face_middle],
  ["knight_10_5", "Lord Estean Andiama", "Estean", tf_hero, 0, reserved,  fac_kingdom_10, [itm_lord_warhorse_6, itm_tear_gilded_plate, itm_shynbaulds_wot, itm_gauntlets, itm_tear_elite_helmet, itm_sword_two_handed_b], knight_attrib_4,wp_two_handed(210)|wp(160),knight_skills_4|knows_trainer_5, tear_man_face_younger],
  ["knight_10_6", "High Lord Tolmeran", "Tolmeran", tf_hero, 0, reserved,  fac_kingdom_10, [itm_lord_warhorse_6, itm_tear_gilded_plate, itm_shynbaulds_wot, itm_gauntlets, itm_tear_elite_helmet, itm_sword_two_handed_b], knight_attrib_4,wp_two_handed(210)|wp(160),knight_skills_4|knows_trainer_5, tear_man_face_young],
  ["knight_10_7", "Lord Carlomin", "Carlomin", tf_hero, 0, reserved,  fac_kingdom_10, [itm_lord_warhorse_6, itm_tear_gilded_plate, itm_shynbaulds_wot, itm_gauntlets, itm_tear_elite_helmet, itm_sword_two_handed_b], knight_attrib_4,wp_two_handed(210)|wp(160),knight_skills_4|knows_trainer_5, tear_man_face_old],
  ["knight_10_8", "High Lord Aracome", "Aracome", tf_hero, 0, reserved,  fac_kingdom_10, [itm_lord_warhorse_6, itm_tear_gilded_plate, itm_shynbaulds_wot, itm_gauntlets, itm_tear_elite_helmet, itm_sword_two_handed_b], knight_attrib_4,wp_two_handed(210)|wp(160),knight_skills_4|knows_trainer_5, tear_man_face_middle],


# Andor
  ["knight_11_1", "Captain General Birgitte 'Silverbow' Trahelion", "Birgitte", tf_hero|tf_female, 0, reserved,  fac_kingdom_11, [itm_lord_warhorse_4, itm_andor_plate, itm_leather_boots, itm_leather_gloves, itm_war_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_sword_medieval_b_small], knight_attrib_4,wp_archery(325)|wp_one_handed(250)|wp(160),knight_skills_4|knows_trainer_4, 0x0000000000000006471a6e36d26926db00000000001d36d30000000000000000],
  ["knight_11_2", "Captain Charlz Guybon", "Charlz", tf_hero, 0, reserved,  fac_kingdom_11, [itm_lord_warhorse_4, itm_andor_plate, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_andoran_helmet, itm_great_sword], knight_attrib_4,wp_two_handed(250)|wp(190),knight_skills_4|knows_trainer_4, andor_man_face_young],
  ["knight_11_3", "Lord Gawyn Trakand", "Gawyn", tf_hero, 0, reserved,  fac_kingdom_11, [itm_lord_warhorse_4, itm_andor_plate, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_andoran_helmet, itm_great_sword], knight_attrib_5,wp_two_handed(295)|wp(190),knight_skills_5|knows_trainer_5, 0x000000018a04100137245646d1b598cd00000000001dcae60000000000000000],
  ["knight_11_4", "Lady Ellorien Traemane", "Ellorien", tf_hero|tf_female, 0, reserved,  fac_kingdom_11, [itm_courser, itm_lady_dress_ruby, itm_woolen_hose, itm_sword_medieval_b_small], knight_attrib_2,wp_one_handed(165)|wp(160),knight_skills_2|knows_trainer_3, andor_woman_face_middle],
  ["knight_11_5", "Lady Dyelin Taravin", "Dyelin", tf_hero|tf_female, 0, reserved,  fac_kingdom_11, [itm_courser, itm_lady_dress_ruby, itm_woolen_hose, itm_sword_medieval_b_small], knight_attrib_2,wp_one_handed(165)|wp(160),knight_skills_2|knows_trainer_3, andor_woman_face_old],
  ["knight_11_6", "Guardsman Martyn Tallanvor", "Martyn", tf_hero, 0, reserved,  fac_kingdom_11, [itm_lord_warhorse_4, itm_andor_plate, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_andoran_helmet, itm_great_sword], knight_attrib_4,wp_two_handed(250)|wp(190),knight_skills_4|knows_trainer_4, andor_man_face_young],
  ["knight_11_7", "Lord Eram Talkend", "Eram", tf_hero, 0, reserved,  fac_kingdom_11, [itm_lord_warhorse_4, itm_andor_plate, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_andoran_helmet, itm_great_sword], knight_attrib_4,wp_two_handed(250)|wp(190),knight_skills_4|knows_trainer_4, andor_man_face_middle],
  ["knight_11_8", "Lord Jarid Sarand", "Jarid", tf_hero, 0, reserved,  fac_kingdom_11, [itm_lord_warhorse_4, itm_andor_plate, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_andoran_helmet, itm_great_sword], knight_attrib_4,wp_two_handed(250)|wp(190),knight_skills_4|knows_trainer_4, andor_man_face_middle],
  ["knight_11_9", "Lord Hanselle Renshar", "Hanselle", tf_hero, 0, reserved,  fac_kingdom_11, [itm_lord_warhorse_4, itm_andor_plate, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_andoran_helmet, itm_great_sword], knight_attrib_3,wp_two_handed(225)|wp(190),knight_skills_3|knows_trainer_4, andor_man_face_younger],
  ["knight_11_10", "Lord Aubrem Pensenor", "Aubrem", tf_hero, 0, reserved,  fac_kingdom_11, [itm_lord_warhorse_4, itm_andor_plate, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_andoran_helmet, itm_great_sword], knight_attrib_3,wp_two_handed(250)|wp(190),knight_skills_3|knows_trainer_4, andor_man_face_middle],
  ["knight_11_11", "Lord Luan Norwelyn", "Luan", tf_hero, 0, reserved,  fac_kingdom_11, [itm_lord_warhorse_4, itm_andor_plate, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_andoran_helmet, itm_great_sword], knight_attrib_4,wp_two_handed(250)|wp(190),knight_skills_4|knows_trainer_4, andor_man_face_old],


# Ghealdan
  ["knight_12_1", "First Captain Gerard Arganda", "Gerard", tf_hero, 0, reserved,  fac_kingdom_12, [itm_charger, itm_ghealdan_plate, itm_steel_greaves_wot, itm_gauntlets, itm_bascinet_2, itm_long_axe_b], knight_attrib_4,wp_two_handed(260)|wp(225),knight_skills_4|knows_trainer_4, ghealdan_man_face_old],
  ["knight_12_2", "Lord Kireyin", "Kireyin", tf_hero, 0, reserved,  fac_kingdom_12, [itm_charger, itm_ghealdan_plate, itm_steel_greaves_wot, itm_gauntlets, itm_bascinet_2, itm_long_axe_b], knight_attrib_4,wp_two_handed(260)|wp(225),knight_skills_4|knows_trainer_4, ghealdan_man_face_middle],
  ["knight_12_3", "Lord Javin Abrenda", "Javin", tf_hero, 0, reserved,  fac_kingdom_12, [itm_charger, itm_ghealdan_plate, itm_steel_greaves_wot, itm_gauntlets, itm_bascinet_2, itm_long_axe_b], knight_attrib_4,wp_two_handed(250)|wp(190),knight_skills_4|knows_trainer_4, ghealdan_man_face_old],
  ["knight_12_4", "Lady Marelle Abrenda", "Marelle", tf_hero|tf_female, 0, reserved,  fac_kingdom_12, [itm_courser, itm_lady_dress_ruby, itm_woolen_hose, itm_sword_medieval_b_small], knight_attrib_2,wp_one_handed(165)|wp(160),knight_skills_2|knows_trainer_3, ghealdan_woman_face_old],


# Far Madding
  ["knight_13_1", "Counsel Narvais Maslin", "Narvais", tf_hero|tf_female, 0, reserved,  fac_kingdom_13, [itm_courser, itm_red_dress, itm_woolen_hose, itm_sword_medieval_b_small], knight_attrib_2,wp_one_handed(165)|wp(160),knight_skills_2|knows_trainer_3, far_madding_woman_face_young],
  ["knight_13_2", "Counsel Cumere Powys", "Cumere", tf_hero|tf_female, 0, reserved,  fac_kingdom_13, [itm_courser, itm_brown_dress, itm_woolen_hose, itm_sword_medieval_b_small], knight_attrib_2,wp_one_handed(165)|wp(160),knight_skills_2|knows_trainer_3, far_madding_woman_face_middle],


# Tarabon
  ["knight_14_1", "Lord Brys", "Brys", tf_hero, 0, reserved,  fac_kingdom_14, [itm_lord_warhorse_2, itm_tarabon_elite_armor, itm_sarranid_boots_d, itm_scale_gauntlets, itm_sarranid_veiled_helmet, itm_great_sword], knight_attrib_4,wp_two_handed(260)|wp(225),knight_skills_4|knows_trainer_4, tarabon_man_face_old],
  ["knight_14_2", "Lord Tanric Gelbin", "Tanric", tf_hero, 0, reserved,  fac_kingdom_14, [itm_lord_warhorse_2, itm_tarabon_elite_armor, itm_sarranid_boots_d, itm_scale_gauntlets, itm_sarranid_veiled_helmet, itm_great_sword], knight_attrib_4,wp_two_handed(260)|wp(225),knight_skills_4|knows_trainer_4, tarabon_man_face_young],
  ["knight_14_3", "Lord Cendrid Halfin", "Centrid", tf_hero, 0, reserved,  fac_kingdom_14, [itm_lord_warhorse_2, itm_tarabon_elite_armor, itm_sarranid_boots_d, itm_scale_gauntlets, itm_sarranid_veiled_helmet, itm_great_sword], knight_attrib_4,wp_two_handed(260)|wp(225),knight_skills_4|knows_trainer_4, tarabon_man_face_middle],


# Amadicia
  ["knight_15_1", "Lord Belaron Setaine", "Belaron", tf_hero, 0, reserved,  fac_kingdom_15, [itm_charger, itm_amadicia_elite_armor, itm_shynbaulds_wot, itm_gauntlets, itm_flat_topped_helmet, itm_great_sword], knight_attrib_4,wp_two_handed(260)|wp(225),knight_skills_4|knows_trainer_4, amadicia_man_face_middle],
  ["knight_15_2", "Lady Tamina Setaine", "Tamina", tf_hero|tf_female, 0, reserved,  fac_kingdom_15, [itm_courser, itm_lady_dress_green, itm_woolen_hose, itm_sword_medieval_b_small], knight_attrib_2,wp_one_handed(165)|wp(160),knight_skills_2|knows_trainer_3, amadicia_woman_face_middle],
  ["knight_15_3", "Lord Allan Renar", "Allan", tf_hero, 0, reserved,  fac_kingdom_15, [itm_charger, itm_amadicia_elite_armor, itm_shynbaulds_wot, itm_gauntlets, itm_flat_topped_helmet, itm_great_sword], knight_attrib_4,wp_two_handed(260)|wp(225),knight_skills_4|knows_trainer_4, amadicia_man_face_young],


# Children of the Light
  ["knight_16_1", "High Inquisitor Rhadam Asunawa", "Asunawa", tf_hero, 0, reserved,  fac_kingdom_16, [itm_charger, itm_whitecloak_inquisitor_tabbard, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_whitecloak_helmet, itm_great_sword], knight_attrib_3,wp_two_handed(250)|wp(200),knight_skills_3|knows_trainer_4, amadicia_man_face_older],
  ["knight_16_2", "Captain Dain Bornhald", "Dain", tf_hero, 0, reserved,  fac_kingdom_16, [itm_charger, itm_whitecloak_tabbard, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_whitecloak_helmet, itm_great_sword], knight_attrib_4,wp_two_handed(260)|wp(225),knight_skills_4|knows_trainer_4, amadicia_man_face_young],
  ["knight_16_3", "Child Jaret Byar", "Jaret", tf_hero, 0, reserved,  fac_kingdom_16, [itm_charger, itm_whitecloak_tabbard, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_whitecloak_helmet, itm_great_sword], knight_attrib_4,wp_two_handed(260)|wp(225),knight_skills_4|knows_trainer_4, amadicia_man_face_middle],

# V: New face for Birgitte


#Borderlands (Malkier, Shienar, Arafel, Kandor, Saldaea)

# Shienar
  ["knight_17_1", "Lord Agelmar Jagad", "Agelmar", tf_hero, 0, reserved,  fac_kingdom_17, [itm_heavy_charger, itm_shienar_captain_armor, itm_steel_greaves_wot, itm_shienar_captain_gauntlets, itm_winged_great_helmet, itm_sword_of_war], knight_attrib_5,wp_two_handed(275)|wp(200),knight_skills_5|knows_trainer_5, shienar_man_face_old],
  ["knight_17_2", "Lord Kayen Yokata", "Kayen", tf_hero, 0, reserved,  fac_kingdom_17, [itm_heavy_charger, itm_shienar_captain_armor, itm_steel_greaves_wot, itm_shienar_captain_gauntlets, itm_winged_great_helmet, itm_sword_of_war], knight_attrib_5,wp_two_handed(275)|wp(200),knight_skills_5|knows_trainer_5, shienar_man_face_middle],
  ["knight_17_3", "Lord Ingtar Shinowa", "Ingtar", tf_hero, 0, reserved,  fac_kingdom_17, [itm_heavy_charger, itm_shienar_captain_armor, itm_steel_greaves_wot, itm_shienar_captain_gauntlets, itm_winged_great_helmet, itm_sword_of_war], knight_attrib_5,wp_two_handed(275)|wp(200),knight_skills_5|knows_trainer_5, shienar_man_face_young],
  ["knight_17_4", "Hurin", "Hurin", tf_hero, 0, reserved,  fac_kingdom_17, [itm_heavy_charger, itm_shienar_captain_armor, itm_steel_greaves_wot, itm_shienar_captain_gauntlets, itm_winged_great_helmet, itm_sword_of_war], knight_attrib_4,wp_two_handed(250)|wp(200),knight_skills_4|knows_trainer_5, shienar_man_face_middle],
  ["knight_17_5", "Uno Nomesta", "Uno", tf_hero, 0, reserved,  fac_kingdom_17, [itm_heavy_charger, itm_shienar_captain_armor, itm_steel_greaves_wot, itm_shienar_captain_gauntlets, itm_winged_great_helmet, itm_sword_of_war], knight_attrib_5,wp_two_handed(275)|wp(200),knight_skills_5|knows_trainer_5, shienar_man_face_old],


# Arafel
  ["knight_18_1", "Lord Ishigari Terasian", "Ishigari", tf_hero, 0, reserved,  fac_kingdom_18, [itm_charger, itm_arafel_mail_and_plate, itm_steel_greaves_wot, itm_gauntlets, itm_oniontop_bascinet_wot, itm_sword_of_war], knight_attrib_5,wp_two_handed(250)|wp(200),knight_skills_5|knows_trainer_5, arafel_man_face_middle],
  ["knight_18_2", "Lord Kyril Shianri", "Kyril", tf_hero, 0, reserved,  fac_kingdom_18, [itm_charger, itm_arafel_mail_and_plate, itm_steel_greaves_wot, itm_gauntlets, itm_oniontop_bascinet_wot, itm_sword_of_war], knight_attrib_5,wp_two_handed(250)|wp(200),knight_skills_5|knows_trainer_5, arafel_man_face_young],
  ["knight_18_3", "Lord Temaril", "Temaril", tf_hero, 0, reserved,  fac_kingdom_18, [itm_charger, itm_arafel_mail_and_plate, itm_steel_greaves_wot, itm_gauntlets, itm_oniontop_bascinet_wot, itm_sword_of_war], knight_attrib_4,wp_two_handed(250)|wp(200),knight_skills_4|knows_trainer_5, arafel_man_face_middle],


# Kandor
  ["knight_19_1", "Lord Baldhere", "Baldhere", tf_hero, 0, reserved,  fac_kingdom_19, [itm_charger, itm_coat_of_plates, itm_plate_boots, itm_gauntlets, itm_kandor_visored_sallet, itm_long_axe_c], knight_attrib_5,wp_two_handed(250)|wp(200),knight_skills_5|knows_trainer_4, kandor_man_face_old],
  ["knight_19_2", "Lady Serailla", "Serailla", tf_hero|tf_female, 0, reserved,  fac_kingdom_19, [itm_charger, itm_green_dress, itm_woolen_hose, itm_one_handed_battle_axe_b], knight_attrib_3,wp_one_handed(200)|wp(160),knight_skills_3|knows_trainer_4, kandor_woman_face_old],
  ["knight_19_3", "Lady Nazelle", "Nazelle", tf_hero|tf_female, 0, reserved,  fac_kingdom_19, [itm_charger, itm_red_dress, itm_woolen_hose, itm_one_handed_battle_axe_b], knight_attrib_3,wp_one_handed(200)|wp(160),knight_skills_3|knows_trainer_4, kandor_woman_face_young],
  ["knight_19_4", "Lord Antol", "Antol", tf_hero, 0, reserved,  fac_kingdom_19, [itm_charger, itm_coat_of_plates, itm_plate_boots, itm_gauntlets, itm_kandor_visored_sallet, itm_long_axe_c], knight_attrib_5,wp_two_handed(250)|wp(200),knight_skills_5|knows_trainer_4, kandor_man_face_young],
  ["knight_19_5", "Lord Ismic", "Ismic", tf_hero, 0, reserved,  fac_kingdom_19, [itm_charger, itm_coat_of_plates, itm_plate_boots, itm_gauntlets, itm_kandor_visored_sallet, itm_long_axe_c], knight_attrib_5,wp_two_handed(250)|wp(200),knight_skills_5|knows_trainer_4, kandor_man_face_young],


# Saldaea
  ["knight_20_1", "Lord Davram Bashere", "Davram", tf_hero, 0, reserved,  fac_kingdom_20, [itm_lord_warhorse_1, itm_vaegir_elite_armor, itm_splinted_greaves, itm_khergit_guard_helmet, itm_lamellar_gauntlets, itm_khergit_sword_two_handed_b], knight_attrib_5,wp_two_handed(300)|wp(250),knight_skills_5|knows_trainer_4, saldaea_man_face_old],  
  ["knight_20_2", "Lord Maedin Bashere", "Maedin", tf_hero, 0, reserved,  fac_kingdom_20, [itm_lord_warhorse_1, itm_vaegir_elite_armor, itm_splinted_greaves, itm_khergit_guard_helmet, itm_lamellar_gauntlets, itm_khergit_sword_two_handed_b], knight_attrib_5,wp_two_handed(275)|wp(250),knight_skills_5|knows_trainer_4, saldaea_man_face_older],
  ["knight_20_3", "Lord Kalyan Ramsin", "Kalyan", tf_hero, 0, reserved,  fac_kingdom_20, [itm_lord_warhorse_1, itm_vaegir_elite_armor, itm_splinted_greaves, itm_khergit_guard_helmet, itm_lamellar_gauntlets, itm_khergit_sword_two_handed_b], knight_attrib_5,wp_two_handed(275)|wp(250),knight_skills_5|knows_trainer_4, saldaea_man_face_middle],
  ["knight_20_4", "Tumad Ahzkan", "Tumad", tf_hero, 0, reserved,  fac_kingdom_20, [itm_lord_warhorse_1, itm_vaegir_elite_armor, itm_splinted_greaves, itm_khergit_guard_helmet, itm_lamellar_gauntlets, itm_khergit_sword_two_handed_b], knight_attrib_5,wp_two_handed(275)|wp(250),knight_skills_5|knows_trainer_4, saldaea_man_face_young],


# White Tower
  ["knight_21_1", "Keeper of the Chronicles Silviana Sedai", "Silviana", tf_hero|tf_female, 0, reserved,  fac_kingdom_21, [itm_hunter, itm_aes_sedai_red_dress, itm_veteran_aes_sedai_red_shoes, itm_power_player, itm_power_ammo], knight_attrib_3,wp_firearm(220)|wp_one_handed(175)|wp(130),knight_skills_3|knows_trainer_4|knows_power_draw_7|knows_fire_7|knows_earth_7|knows_spirit_8|knows_water_8|knows_air_8, tar_valon_woman_face_middle],
  ["knight_21_2", "Lord Gareth Bryne", "Gareth", tf_hero, 0, reserved,  fac_kingdom_21, [itm_charger, itm_white_tower_captain_armor, itm_splinted_leather_greaves, itm_leather_gloves, itm_guard_helmet, itm_great_sword], knight_attrib_4,wp_two_handed(250)|wp(200),knight_skills_4|knows_trainer_5, andor_man_face_old],
  ["knight_21_3", "al'Lan Mandragoran",  "Lan",  tf_hero, 0,reserved,  fac_kingdom_21,[itm_heavy_charger, itm_nobleman_outfit, itm_leather_boots, itm_steel_greaves_wot, itm_shienar_captain_armor, itm_shienar_captain_gauntlets, itm_seanchan_large_sword, itm_winged_great_helmet], knight_attrib_5,wp_two_handed(325)|wp(300),knight_skills_5|knows_trainer_4, 0x0000000da704414724d38e371c6dc8e500000000001e58eb0000000000000000],
  ["knight_21_4", "Guard Captain Jimar Chubain", "Chubain", tf_hero, 0, reserved,  fac_kingdom_21, [itm_charger, itm_white_tower_captain_armor, itm_splinted_leather_greaves, itm_leather_gloves, itm_guard_helmet, itm_great_sword], knight_attrib_4,wp_two_handed(250)|wp(200),knight_skills_4|knows_trainer_5, tar_valon_man_face_old],
  ["knight_21_5", "Cadsuane Sedai", "Cadsuane", tf_hero|tf_female, 0, reserved,  fac_kingdom_21, [itm_hunter, itm_aes_sedai_green_dress, itm_veteran_aes_sedai_green_shoes, itm_power_player, itm_power_ammo], knight_attrib_3,wp_firearm(250)|wp_one_handed(175)|wp(130),knight_skills_3|knows_trainer_4|knows_power_draw_8|knows_fire_8|knows_earth_8|knows_spirit_9|knows_water_8|knows_air_8, far_madding_woman_face_older],
  ["knight_21_6", "Nynaeve Sedai", "Nynaeve", tf_hero|tf_female, 0, reserved,  fac_kingdom_21, [itm_hunter, itm_aes_sedai_yellow_dress, itm_veteran_aes_sedai_yellow_shoes, itm_power_player, itm_power_ammo], knight_attrib_3,wp_firearm(310)|wp_one_handed(175)|wp(130),knight_skills_3|knows_trainer_4|knows_power_draw_9|knows_fire_9|knows_earth_8|knows_spirit_10|knows_water_10|knows_air_10, andor_woman_face_young],
  ["knight_21_7", "Siuan Sedai", "Siuan", tf_hero|tf_female, 0, reserved,  fac_kingdom_21, [itm_hunter, itm_aes_sedai_blue_dress, itm_veteran_aes_sedai_blue_shoes, itm_power_player, itm_power_ammo], knight_attrib_3,wp_firearm(195)|wp_one_handed(175)|wp(130),knight_skills_3|knows_trainer_4|knows_power_draw_7|knows_fire_7|knows_earth_7|knows_spirit_7|knows_water_7|knows_air_7, tear_woman_face_young],
  ["knight_21_8", "Leana Sedai", "Leana", tf_hero|tf_female, 0, reserved,  fac_kingdom_21, [itm_hunter, itm_aes_sedai_green_dress, itm_veteran_aes_sedai_green_shoes, itm_power_player, itm_power_ammo], knight_attrib_3,wp_firearm(195)|wp_one_handed(175)|wp(130),knight_skills_3|knows_trainer_4|knows_power_draw_7|knows_fire_7|knows_earth_7|knows_spirit_7|knows_water_7|knows_air_7, 0x00000002870800054f1c8ed924a1ad1300000000001eb8e30000000000000000],
  ["knight_21_9", "Lelaine Sedai", "Lelaine", tf_hero|tf_female, 0, reserved,  fac_kingdom_21, [itm_hunter, itm_aes_sedai_blue_dress, itm_veteran_aes_sedai_blue_shoes, itm_power_player, itm_power_ammo], knight_attrib_3,wp_firearm(210)|wp_one_handed(175)|wp(130),knight_skills_3|knows_trainer_4|knows_power_draw_8|knows_fire_7|knows_earth_7|knows_spirit_8|knows_water_8|knows_air_7, tar_valon_woman_face_young],
  ["knight_21_10", "Romanda Sedai", "Romanda", tf_hero|tf_female, 0, reserved,  fac_kingdom_21, [itm_hunter, itm_aes_sedai_yellow_dress, itm_veteran_aes_sedai_yellow_shoes, itm_power_player, itm_power_ammo], knight_attrib_3,wp_firearm(210)|wp_one_handed(175)|wp(130),knight_skills_3|knows_trainer_4|knows_power_draw_8|knows_fire_7|knows_earth_7|knows_spirit_8|knows_water_7|knows_air_8, far_madding_woman_face_old],

#  ["knight_21_11", "Pevara Sedai", "Pevara", tf_hero|tf_female, 0, reserved,  fac_kingdom_21, [itm_hunter, itm_aes_sedai_red_dress, itm_veteran_aes_sedai_red_shoes, itm_power_female_good_ranged, itm_power_ammo], knight_attrib_3,wp_firearm(225)|wp_one_handed(175)|wp(130),knight_skills_3|knows_trainer_4, kandor_woman_face_old],
#  ["knight_21_12", "Yukiri Sedai", "Yukiri", tf_hero|tf_female, 0, reserved,  fac_kingdom_21, [itm_hunter, itm_aes_sedai_grey_dress, itm_veteran_aes_sedai_grey_shoes, itm_power_female_good_ranged, itm_power_ammo], knight_attrib_3,wp_firearm(225)|wp_one_handed(175)|wp(130),knight_skills_3|knows_trainer_4, arafel_woman_face_middle],
#  ["knight_21_13", "Saerin Sedai", "Saerin", tf_hero|tf_female, 0, reserved,  fac_kingdom_21, [itm_hunter, itm_aes_sedai_brown_dress, itm_veteran_aes_sedai_brown_shoes, itm_power_female_good_ranged, itm_power_ammo], knight_attrib_3,wp_firearm(225)|wp_one_handed(175)|wp(130),knight_skills_3|knows_trainer_4, altara_woman_face_middle],
#  ["knight_21_14", "Doesine Sedai", "Doesine", tf_hero|tf_female, 0, reserved,  fac_kingdom_21, [itm_hunter, itm_aes_sedai_yellow_dress, itm_veteran_aes_sedai_yellow_shoes, itm_power_female_good_ranged, itm_power_ammo], knight_attrib_3,wp_firearm(225)|wp_one_handed(175)|wp(130),knight_skills_3|knows_trainer_4, cairhien_woman_face_old],
#  ["knight_21_15", "Seaine Sedai", "Seaine", tf_hero|tf_female, 0, reserved,  fac_kingdom_21, [itm_hunter, itm_aes_sedai_white_dress, itm_veteran_aes_sedai_white_shoes, itm_power_female_good_ranged, itm_power_ammo], knight_attrib_3,wp_firearm(225)|wp_one_handed(175)|wp(130),knight_skills_3|knows_trainer_4, murandy_woman_face_middle],
#  ["knight_21_16", "Myrelle Sedai", "Myrelle", tf_hero|tf_female, 0, reserved,  fac_kingdom_21, [itm_hunter, itm_aes_sedai_green_dress, itm_veteran_aes_sedai_green_shoes, itm_power_female_good_ranged, itm_power_ammo], knight_attrib_3,wp_firearm(225)|wp_one_handed(175)|wp(130),knight_skills_3|knows_trainer_4, altara_woman_face_young],
#  ["knight_21_17", "Kiruna Sedai", "Kiruna", tf_hero|tf_female, 0, reserved,  fac_kingdom_21, [itm_hunter, itm_aes_sedai_green_dress, itm_veteran_aes_sedai_green_shoes, itm_power_female_good_ranged, itm_power_ammo], knight_attrib_3,wp_firearm(225)|wp_one_handed(175)|wp(130),knight_skills_3|knows_trainer_4, arafel_woman_face_middle],
#  ["knight_21_18", "Bera Sedai", "Bera", tf_hero|tf_female, 0, reserved,  fac_kingdom_21, [itm_hunter, itm_aes_sedai_green_dress, itm_veteran_aes_sedai_green_shoes, itm_power_female_good_ranged, itm_power_ammo], knight_attrib_3,wp_firearm(225)|wp_one_handed(175)|wp(130),knight_skills_3|knows_trainer_4, andor_woman_face_middle],
#  ["knight_21_19", "Tiana Sedai", "Tiana", tf_hero|tf_female, 0, reserved,  fac_kingdom_21, [itm_hunter, itm_aes_sedai_grey_dress, itm_veteran_aes_sedai_grey_shoes, itm_power_female_good_ranged, itm_power_ammo], knight_attrib_3,wp_firearm(225)|wp_one_handed(175)|wp(130),knight_skills_3|knows_trainer_4, tear_woman_face_middle],
#  ["knight_21_20", "Takima Sedai", "Takima", tf_hero|tf_female, 0, reserved,  fac_kingdom_21, [itm_hunter, itm_aes_sedai_brown_dress, itm_veteran_aes_sedai_brown_shoes, itm_power_female_good_ranged, itm_power_ammo], knight_attrib_3,wp_firearm(225)|wp_one_handed(175)|wp(130),knight_skills_3|knows_trainer_4, saldaea_woman_face_young],
#  ["knight_21_21", "Masuri Sedai", "Masuri", tf_hero|tf_female, 0, reserved,  fac_kingdom_21, [itm_hunter, itm_aes_sedai_brown_dress, itm_veteran_aes_sedai_brown_shoes, itm_power_female_good_ranged, itm_power_ammo], knight_attrib_3,wp_firearm(225)|wp_one_handed(175)|wp(130),knight_skills_3|knows_trainer_4, ghealdan_woman_face_middle],


# Aiel Nation
  ["knight_22_1", "Clan Chief Han", "Han", tf_hero, 0, reserved,  fac_kingdom_22, [itm_cadinsor, itm_cadinsor_boots, itm_shoufa, itm_aiel_spear, itm_hide_buckler_strong], knight_attrib_5,wp_polearm(275)|wp(200),knight_skills_5|knows_trainer_5, aiel_2_man_face_old],
  ["knight_22_2", "Clan Chief Dhearic", "Dhearic", tf_hero, 0, reserved,  fac_kingdom_22, [itm_cadinsor, itm_cadinsor_boots, itm_shoufa, itm_aiel_spear, itm_hide_buckler_strong], knight_attrib_5,wp_polearm(275)|wp(200),knight_skills_5|knows_trainer_5, aiel_1_man_face_old],
  ["knight_22_3", "Clan Chief Timolan", "Timolan", tf_hero, 0, reserved,  fac_kingdom_22, [itm_cadinsor, itm_cadinsor_boots, itm_shoufa, itm_aiel_spear, itm_hide_buckler_strong], knight_attrib_5,wp_polearm(275)|wp(200),knight_skills_5|knows_trainer_5, aiel_2_man_face_middle],
  ["knight_22_4", "Clan Chief Bruan", "Bruan", tf_hero, 0, reserved,  fac_kingdom_22, [itm_cadinsor, itm_cadinsor_boots, itm_shoufa, itm_aiel_spear, itm_hide_buckler_strong], knight_attrib_5,wp_polearm(275)|wp(200),knight_skills_5|knows_trainer_5, aiel_1_man_face_middle],
  ["knight_22_5", "Clan Chief Indirian", "Indirian", tf_hero, 0, reserved,  fac_kingdom_22, [itm_cadinsor, itm_cadinsor_boots, itm_shoufa, itm_aiel_spear, itm_hide_buckler_strong], knight_attrib_5,wp_polearm(275)|wp(200),knight_skills_5|knows_trainer_5, aiel_2_man_face_older],
  ["knight_22_6", "Clan Chief Bael", "Bael", tf_hero, 0, reserved,  fac_kingdom_22, [itm_cadinsor, itm_cadinsor_boots, itm_shoufa, itm_aiel_spear, itm_hide_buckler_strong], knight_attrib_5,wp_polearm(275)|wp(200),knight_skills_5|knows_trainer_5, aiel_1_man_face_older],
  ["knight_22_7", "Clan Chief Mandelain", "Mandelain", tf_hero, 0, reserved,  fac_kingdom_22, [itm_cadinsor, itm_cadinsor_boots, itm_shoufa, itm_aiel_spear, itm_hide_buckler_strong], knight_attrib_5,wp_polearm(275)|wp(200),knight_skills_5|knows_trainer_5, aiel_2_man_face_old],
  ["knight_22_8", "Clan Chief Erim", "Erim", tf_hero, 0, reserved,  fac_kingdom_22, [itm_cadinsor, itm_cadinsor_boots, itm_shoufa, itm_aiel_spear, itm_hide_buckler_strong], knight_attrib_5,wp_polearm(275)|wp(200),knight_skills_5|knows_trainer_5, aiel_1_man_face_old],
  ["knight_22_9", "Clan Chief Jheran", "Jheran", tf_hero, 0, reserved,  fac_kingdom_22, [itm_cadinsor, itm_cadinsor_boots, itm_shoufa, itm_aiel_spear, itm_hide_buckler_strong], knight_attrib_5,wp_polearm(275)|wp(200),knight_skills_5|knows_trainer_5, aiel_2_man_face_young],
  ["knight_22_10", "Clan Chief Janwin", "Janwin", tf_hero, 0, reserved,  fac_kingdom_22, [itm_cadinsor, itm_cadinsor_boots, itm_shoufa, itm_aiel_spear, itm_hide_buckler_strong], knight_attrib_5,wp_polearm(275)|wp(200),knight_skills_5|knows_trainer_5, aiel_1_man_face_young],
  ["knight_22_11", "Nandera", "Nandera", tf_hero|tf_female, 0, reserved,  fac_kingdom_22, [itm_cadinsor, itm_cadinsor_boots, itm_shoufa, itm_aiel_spear, itm_hide_buckler_strong], knight_attrib_5,wp_polearm(275)|wp(200),knight_skills_5|knows_trainer_5, aiel_2_woman_face_middle],
  ["knight_22_12", "Wise One Sorilea", "Sorilea", tf_hero|tf_female, 0, reserved,  fac_kingdom_22, [itm_wise_one_dress_with_shawl, itm_cadinsor_boots, itm_power_player, itm_power_ammo], knight_attrib_3,wp_firearm(185)|wp_one_handed(175)|wp(130),knight_skills_3|knows_trainer_4|knows_power_draw_7|knows_fire_7|knows_earth_7|knows_spirit_7|knows_water_7|knows_air_7, aiel_1_woman_face_older],
  ["knight_22_13", "Wise One Amys", "Amys", tf_hero|tf_female, 0, reserved,  fac_kingdom_22, [itm_wise_one_dress_with_shawl, itm_cadinsor_boots, itm_power_player, itm_power_ammo], knight_attrib_3,wp_firearm(210)|wp_one_handed(200)|wp(130),knight_skills_3|knows_trainer_4|knows_power_draw_7|knows_fire_7|knows_earth_7|knows_spirit_9|knows_water_8|knows_air_7, aiel_1_woman_face_old],
  ["knight_22_14", "Bain", "Bain", tf_hero|tf_female, 0, reserved,  fac_kingdom_22, [itm_cadinsor, itm_cadinsor_boots, itm_shoufa, itm_aiel_spear, itm_hide_buckler_strong], knight_attrib_5,wp_polearm(275)|wp(200),knight_skills_5|knows_trainer_5, aiel_2_woman_face_younger],
  ["knight_22_15", "Wise One Melaine", "Melaine", tf_hero|tf_female, 0, reserved,  fac_kingdom_22, [itm_wise_one_dress_with_shawl, itm_cadinsor_boots, itm_power_player, itm_power_ammo], knight_attrib_3,wp_firearm(210)|wp_one_handed(200)|wp(130),knight_skills_3|knows_trainer_4|knows_power_draw_7|knows_fire_7|knows_earth_7|knows_spirit_9|knows_water_7|knows_air_8, aiel_2_woman_face_young],
  ["knight_22_16", "Wise One Bair", "Bair", tf_hero|tf_female, 0, reserved,  fac_kingdom_22, [itm_wise_one_dress_with_shawl, itm_cadinsor_boots, itm_aiel_knife], knight_attrib_3,wp_one_handed(200)|wp(130),knight_skills_3|knows_trainer_4, aiel_2_woman_face_older],
  ["knight_22_17", "Gaul", "Gaul", tf_hero, 0, reserved,  fac_kingdom_22, [itm_cadinsor, itm_cadinsor_boots, itm_shoufa, itm_aiel_spear, itm_hide_buckler_strong], knight_attrib_5,wp_polearm(300)|wp(200),knight_skills_5|knows_trainer_5, aiel_2_man_face_younger],
  ["knight_22_18", "Aviendha", "Aviendha", tf_hero|tf_female, 0, reserved,  fac_kingdom_22, [itm_wise_one_dress_with_shawl, itm_cadinsor_boots, itm_power_player, itm_power_ammo], knight_attrib_4,wp_firearm(280)|wp_one_handed(200)|wp(130),knight_skills_4|knows_trainer_4|knows_power_draw_8|knows_fire_8|knows_earth_8|knows_spirit_9|knows_water_9|knows_air_8, aiel_1_woman_face_younger],
  ["knight_22_19", "Heirn", "Heirn", tf_hero, 0, reserved,  fac_kingdom_22, [itm_cadinsor, itm_cadinsor_boots, itm_shoufa, itm_aiel_spear, itm_hide_buckler_strong], knight_attrib_5,wp_polearm(275)|wp(200),knight_skills_5|knows_trainer_5, aiel_1_man_face_old],
  ["knight_22_20", "Sulin", "Sulin", tf_hero|tf_female, 0, reserved,  fac_kingdom_22, [itm_cadinsor, itm_cadinsor_boots, itm_shoufa, itm_aiel_spear, itm_hide_buckler_strong], knight_attrib_5,wp_polearm(275)|wp(200),knight_skills_5|knows_trainer_5, aiel_1_woman_face_older],


# Seanchan Empire
  ["knight_23_1", "Captain-General Lunal Galgan", "Galgan", tf_hero, 0, reserved,  fac_kingdom_23, [itm_arabian_horse_b, itm_seanchan_high_armor, itm_seanchan_high_boots, itm_seanchan_high_gloves, itm_seanchan_high_helmet, itm_seanchan_large_sword], knight_attrib_5,wp_two_handed(275)|wp(230),knight_skills_5|knows_trainer_5, seanchan_1_man_face_older],
  ["knight_23_2", "Banner-General Furyk Karede", "Karede", tf_hero, 0, reserved,  fac_kingdom_23, [itm_arabian_horse_b, itm_deathwatch_guard_armor, itm_deathwatch_guard_helmet, itm_deathwatch_guard_boots, itm_deathwatch_guard_gloves, itm_seanchan_large_sword], knight_attrib_5,wp_two_handed(300)|wp(230),knight_skills_5|knows_trainer_4, seanchan_1_man_face_old],
  ["knight_23_3", "Lieutenant-General Tylee Khirgan", "Tylee", tf_hero|tf_female, 0, reserved,  fac_kingdom_23, [itm_arabian_horse_b, itm_seanchan_high_armor, itm_seanchan_high_boots, itm_seanchan_high_gloves, itm_seanchan_high_helmet, itm_seanchan_large_sword], knight_attrib_4,wp_two_handed(255)|wp(230),knight_skills_4|knows_trainer_4, seanchan_1_woman_face_middle],
  ["knight_23_4", "Banner-General Gamel Loune", "Gamel", tf_hero, 0, reserved,  fac_kingdom_23, [itm_arabian_horse_b, itm_seanchan_high_armor, itm_seanchan_high_boots, itm_seanchan_high_gloves, itm_seanchan_high_helmet, itm_seanchan_large_sword], knight_attrib_5,wp_two_handed(275)|wp(230),knight_skills_5|knows_trainer_4, seanchan_2_man_face_old],
  ["knight_23_5", "Banner-General Mikhel Najirah", "Mikhel", tf_hero, 0, reserved,  fac_kingdom_23, [itm_arabian_horse_b, itm_seanchan_high_armor, itm_seanchan_high_boots, itm_seanchan_high_gloves, itm_seanchan_high_helmet, itm_seanchan_large_sword], knight_attrib_5,wp_two_handed(275)|wp(230),knight_skills_5|knows_trainer_4, seanchan_2_man_face_middle],
  ["knight_23_6", "Der-Suldam Lisaine Jarath", "Lisaine", tf_hero|tf_female, 0, reserved,  fac_kingdom_23, [itm_arabian_horse_a, itm_suldam_dress, itm_suldam_boots, itm_der_suldam_dagger], knight_attrib_3,wp_one_handed(200)|wp(130),knight_skills_3|knows_trainer_3, seanchan_2_woman_face_middle],
  ["knight_23_7", "Banner-General Efraim Yamada", "Efraim", tf_hero, 0, reserved,  fac_kingdom_23, [itm_arabian_horse_b, itm_seanchan_high_armor, itm_seanchan_high_boots, itm_seanchan_high_gloves, itm_seanchan_high_helmet, itm_seanchan_large_sword], knight_attrib_5,wp_two_handed(275)|wp(230),knight_skills_5|knows_trainer_4, seanchan_1_man_face_middle],
  ["knight_23_8", "Lieutenant-General Abaldar Yulan", "Abaldar", tf_hero, 0, reserved,  fac_kingdom_23, [itm_arabian_horse_b, itm_seanchan_high_armor, itm_seanchan_high_boots, itm_seanchan_high_gloves, itm_seanchan_high_helmet, itm_seanchan_large_sword], knight_attrib_4,wp_two_handed(255)|wp(230),knight_skills_4|knows_trainer_4, seanchan_2_man_face_older],
  ["knight_23_9", "Captain Jadranka", "Jadranka", tf_hero, 0, reserved,  fac_kingdom_23, [itm_arabian_horse_b, itm_seanchan_high_armor, itm_seanchan_high_boots, itm_seanchan_high_gloves, itm_seanchan_high_helmet, itm_seanchan_large_sword], knight_attrib_4,wp_two_handed(250)|wp(230),knight_skills_3|knows_trainer_4, seanchan_1_man_face_middle],
  ["knight_23_10", "Lieutenant Gueye Arabah", "Gueye", tf_hero, 0, reserved,  fac_kingdom_23, [itm_arabian_horse_b, itm_seanchan_high_armor, itm_seanchan_high_boots, itm_seanchan_high_gloves, itm_seanchan_high_helmet, itm_seanchan_large_sword], knight_attrib_3,wp_two_handed(250)|wp(230),knight_skills_3|knows_trainer_3, seanchan_2_man_face_middle],
  ["knight_23_11", "Captain Assid Bakuun", "Assid", tf_hero, 0, reserved,  fac_kingdom_23, [itm_arabian_horse_b, itm_seanchan_high_armor, itm_seanchan_high_boots, itm_seanchan_high_gloves, itm_seanchan_high_helmet, itm_seanchan_large_sword], knight_attrib_4,wp_two_handed(250)|wp(230),knight_skills_3|knows_trainer_4, seanchan_1_man_face_young],
  ["knight_23_12", "Captain Blasic Faloun", "Blasic", tf_hero, 0, reserved,  fac_kingdom_23, [itm_arabian_horse_b, itm_seanchan_high_armor, itm_seanchan_high_boots, itm_seanchan_high_gloves, itm_seanchan_high_helmet, itm_seanchan_large_sword], knight_attrib_4,wp_two_handed(250)|wp(230),knight_skills_3|knows_trainer_4, seanchan_2_man_face_young],
  ["knight_23_13", "Captain Musenge", "Musenge", tf_hero, 0, reserved,  fac_kingdom_23, [itm_arabian_horse_b, itm_seanchan_high_armor, itm_seanchan_high_boots, itm_seanchan_high_gloves, itm_seanchan_high_helmet, itm_seanchan_large_sword], knight_attrib_4,wp_two_handed(250)|wp(230),knight_skills_3|knows_trainer_4, seanchan_1_man_face_younger],
  ["knight_23_14", "Captain Bakayar Mishima", "Mishima", tf_hero, 0, reserved,  fac_kingdom_23, [itm_arabian_horse_b, itm_seanchan_high_armor, itm_seanchan_high_boots, itm_seanchan_high_gloves, itm_seanchan_high_helmet, itm_seanchan_large_sword], knight_attrib_4,wp_two_handed(250)|wp(230),knight_skills_3|knows_trainer_4, seanchan_2_man_face_younger],
  ["knight_23_15", "Lord Faverde Nothish", "Faverde", tf_hero, 0, reserved,  fac_kingdom_23, [itm_arabian_horse_a, itm_seanchan_middle_armor, itm_seanchan_middle_boots, itm_seanchan_middle_gloves, itm_seanchan_middle_helmet, itm_seanchan_large_sword], knight_attrib_3,wp_two_handed(250)|wp(230),knight_skills_3|knows_trainer_3, seanchan_2_man_face_middle],
  ["knight_23_16", "Lord Amenar Shumada", "Amenar", tf_hero, 0, reserved,  fac_kingdom_23, [itm_arabian_horse_a, itm_seanchan_middle_armor, itm_seanchan_middle_boots, itm_seanchan_middle_gloves, itm_seanchan_middle_helmet, itm_seanchan_large_sword], knight_attrib_3,wp_two_handed(250)|wp(230),knight_skills_3|knows_trainer_3, seanchan_1_man_face_older],
  ["knight_23_17", "Captain Egeanin Tamarath", "Egeanin", tf_hero|tf_female, 0, reserved,  fac_kingdom_23, [itm_arabian_horse_b, itm_seanchan_high_armor, itm_seanchan_high_boots, itm_seanchan_high_gloves, itm_seanchan_high_helmet, itm_seanchan_large_sword], knight_attrib_4,wp_two_handed(250)|wp(230),knight_skills_3|knows_trainer_4, seanchan_1_woman_face_middle],
  ["knight_23_18", "Hand Yuril", "Yuril", tf_hero, 0, reserved,  fac_kingdom_23, [itm_arabian_horse_a, itm_seanchan_middle_armor, itm_seanchan_middle_boots, itm_seanchan_middle_gloves, itm_seanchan_middle_helmet, itm_seanchan_large_sword], knight_attrib_3,wp_two_handed(250)|wp(230),knight_skills_3|knows_trainer_3, seanchan_1_man_face_young],
  ["knight_23_19", "Voice Selucia", "Selucia", tf_hero|tf_female, 0, reserved,  fac_kingdom_23, [itm_arabian_horse_a, itm_sarranid_lady_dress, itm_suldam_boots, itm_aiel_knife], knight_attrib_3,wp_one_handed(200)|wp(130),knight_skills_3|knows_trainer_4, seanchan_1_woman_face_young],
  ["knight_23_20", "Sul'dam Malahavana", "Malahavana", tf_hero|tf_female, 0, reserved,  fac_kingdom_23, [itm_arabian_horse_a, itm_suldam_dress, itm_suldam_boots, itm_suldam_dagger], knight_attrib_3,wp_one_handed(200)|wp(130),knight_skills_3|knows_trainer_3, seanchan_1_woman_face_old],


#Shadowspawn
  ["knight_24_1", "Moridin", "Moridin", tf_hero, 0, reserved,  fac_kingdom_24, [itm_myrddraal_horse, itm_dreadlord_coat, itm_black_leather_boots, itm_power_player, itm_power_ammo], knight_attrib_5,wp_firearm(350)|wp_one_handed(300)|wp(200),knight_skills_5|knows_trainer_5|knows_power_draw_10|knows_fire_10|knows_earth_10|knows_spirit_10|knows_water_10|knows_air_10, 0x000000033604400933a5d2329c72461600000000001cc7230000000000000000],
  ["knight_24_2", "Demandred", "Demandred", tf_hero, 0, reserved,  fac_kingdom_24, [itm_myrddraal_horse, itm_dreadlord_coat, itm_black_leather_boots, itm_power_player, itm_power_ammo], knight_attrib_5,wp_firearm(340)|wp_one_handed(300)|wp(200),knight_skills_5|knows_trainer_5|knows_power_draw_10|knows_fire_10|knows_earth_10|knows_spirit_10|knows_water_9|knows_air_9, far_madding_man_face_middle],
  ["knight_24_3", "Moghedien", "Moghedien", tf_hero|tf_female, 0, reserved,  fac_kingdom_24, [itm_hunter, itm_sarranid_common_dress, itm_aes_sedai_black_ajah_shoes, itm_power_player, itm_power_ammo], knight_attrib_4,wp_firearm(290)|wp_one_handed(175)|wp(130),knight_skills_4|knows_trainer_4|knows_power_draw_9|knows_fire_8|knows_earth_8|knows_spirit_10|knows_water_9|knows_air_8, tear_woman_face_middle],
  ["knight_24_4", "Mesaana", "Mesaana", tf_hero|tf_female, 0, reserved,  fac_kingdom_24, [itm_courser, itm_sarranid_lady_dress, itm_aes_sedai_black_ajah_shoes, itm_power_player, itm_power_ammo], knight_attrib_4,wp_firearm(300)|wp_one_handed(175)|wp(130),knight_skills_4|knows_trainer_5|knows_power_draw_9|knows_fire_8|knows_earth_8|knows_spirit_9|knows_water_9|knows_air_10, tar_valon_woman_face_middle],
  ["knight_24_5", "Graendal", "Graendal", tf_hero|tf_female, 0, reserved,  fac_kingdom_24, [itm_courser, itm_khergit_lady_dress, itm_aes_sedai_black_ajah_shoes, itm_power_player, itm_power_ammo], knight_attrib_4,wp_firearm(330)|wp_one_handed(175)|wp(130),knight_skills_4|knows_trainer_5|knows_power_draw_10|knows_fire_9|knows_earth_9|knows_spirit_10|knows_water_10|knows_air_10, arad_doman_woman_face_middle],
  ["knight_24_6", "Cyndane", "Cyndane", tf_hero|tf_female, 0, reserved,  fac_kingdom_24, [itm_hunter, itm_red_dress, itm_aes_sedai_black_ajah_shoes, itm_power_player, itm_power_ammo], knight_attrib_4,wp_firearm(340)|wp_one_handed(175)|wp(130),knight_skills_4|knows_trainer_5|knows_power_draw_10|knows_fire_9|knows_earth_9|knows_spirit_10|knows_water_9|knows_air_10, kandor_woman_face_middle],
  ["knight_24_7", "Alviarin Freidhen", "Alviarin", tf_hero|tf_female, 0, reserved,  fac_kingdom_24, [itm_saddle_horse, itm_aes_sedai_black_ajah_dress, itm_aes_sedai_black_ajah_shoes, itm_power_player, itm_power_ammo], knight_attrib_3,wp_firearm(205)|wp_one_handed(200)|wp(160),knight_skills_3|knows_trainer_3|knows_power_draw_8|knows_fire_7|knows_earth_7|knows_spirit_8|knows_water_7|knows_air_8, tear_woman_face_old],
  ["knight_24_8", "Katerine Alruddin", "Katerine", tf_hero|tf_female, 0, reserved,  fac_kingdom_24, [itm_saddle_horse, itm_aes_sedai_black_ajah_dress, itm_aes_sedai_black_ajah_shoes, itm_power_player, itm_power_ammo], knight_attrib_3,wp_firearm(205)|wp_one_handed(200)|wp(160),knight_skills_3|knows_trainer_3|knows_power_draw_8|knows_fire_7|knows_earth_7|knows_spirit_8|knows_water_8|knows_air_7, tarabon_woman_face_middle],
  ["knight_24_9", "Delana Mosalaine", "Delana", tf_hero|tf_female, 0, reserved,  fac_kingdom_24, [itm_saddle_horse, itm_aes_sedai_black_ajah_dress, itm_aes_sedai_black_ajah_shoes, itm_power_player, itm_power_ammo], knight_attrib_3,wp_firearm(195)|wp_one_handed(200)|wp(160),knight_skills_3|knows_trainer_3|knows_power_draw_7|knows_fire_7|knows_earth_7|knows_spirit_7|knows_water_7|knows_air_8, shienar_woman_face_old],
  ["knight_24_10", "Chesmal Emry", "Chesmal", tf_hero|tf_female, 0, reserved,  fac_kingdom_24, [itm_saddle_horse, itm_aes_sedai_black_ajah_dress, itm_aes_sedai_black_ajah_shoes, itm_power_player, itm_power_ammo], knight_attrib_3,wp_firearm(195)|wp_one_handed(200)|wp(160),knight_skills_3|knows_trainer_3|knows_power_draw_7|knows_fire_7|knows_earth_7|knows_spirit_8|knows_water_7|knows_air_7, ghealdan_woman_face_middle],
  ["knight_24_11", "Rianna Andomeran", "Rianna", tf_hero|tf_female, 0, reserved,  fac_kingdom_24, [itm_saddle_horse, itm_aes_sedai_black_ajah_dress, itm_aes_sedai_black_ajah_shoes, itm_power_player, itm_power_ammo], knight_attrib_3,wp_firearm(195)|wp_one_handed(200)|wp(160),knight_skills_3|knows_trainer_3|knows_power_draw_7|knows_fire_7|knows_earth_7|knows_spirit_7|knows_water_8|knows_air_7, kandor_woman_face_old],
  ["knight_24_12", "Falion Bhoda", "Falion", tf_hero|tf_female, 0, reserved,  fac_kingdom_24, [itm_saddle_horse, itm_aes_sedai_black_ajah_dress, itm_aes_sedai_black_ajah_shoes, itm_power_player, itm_power_ammo], knight_attrib_3,wp_firearm(195)|wp_one_handed(200)|wp(160),knight_skills_3|knows_trainer_3|knows_power_draw_7|knows_fire_7|knows_earth_7|knows_spirit_8|knows_water_7|knows_air_7, kandor_woman_face_middle],
  ["knight_24_13", "Marillin Gemalphin", "Marillin", tf_hero|tf_female, 0, reserved,  fac_kingdom_24, [itm_saddle_horse, itm_aes_sedai_black_ajah_dress, itm_aes_sedai_black_ajah_shoes, itm_power_player, itm_power_ammo], knight_attrib_3,wp_firearm(195)|wp_one_handed(200)|wp(160),knight_skills_3|knows_trainer_3|knows_power_draw_7|knows_fire_7|knows_earth_7|knows_spirit_7|knows_water_7|knows_air_8, andor_woman_face_old],
  ["knight_24_14", "Temaile Kinderode", "Temaile", tf_hero|tf_female, 0, reserved,  fac_kingdom_24, [itm_saddle_horse, itm_aes_sedai_black_ajah_dress, itm_aes_sedai_black_ajah_shoes, itm_power_player, itm_power_ammo], knight_attrib_3,wp_firearm(195)|wp_one_handed(200)|wp(160),knight_skills_3|knows_trainer_3|knows_power_draw_7|knows_fire_7|knows_earth_7|knows_spirit_7|knows_water_8|knows_air_7, cairhien_woman_face_middle],
  ["knight_24_15", "Mili Skane", "Mili", tf_hero|tf_female, 0, reserved,  fac_kingdom_24, [itm_brown_dress, itm_woolen_hose, itm_illian_seax], knight_attrib_3,wp_one_handed(200)|wp(130),knight_skills_3|knows_trainer_4, andor_woman_face_younger],
  ["knight_24_16", "Daved Hanlon", "Daved", tf_hero, 0, reserved,  fac_kingdom_24, [itm_lord_warhorse_4, itm_andor_plate, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_andoran_helmet, itm_great_sword], knight_attrib_4,wp_two_handed(250)|wp(190),knight_skills_4|knows_trainer_4, amadicia_man_face_young],
  ["knight_24_17", "K'vor'chag Vlja Djevik", "K'vor'chag", tf_hero, 0, reserved,  fac_kingdom_24, [itm_trolloc_strong_armor, itm_black_leather_boots, itm_black_mail_gauntlets, itm_trolloc_goat_helmet, itm_great_long_bardiche], knight_attrib_5,wp_polearm(300)|wp(200),knight_skills_5|knows_trainer_5, 0x000000033604400933a5d2329c72461600000000001cc7230000000000000000],
  ["knight_24_18", "Old Cully", "Old Cully", tf_hero, 0, reserved,  fac_kingdom_24, [itm_charger, itm_murandy_elite_armor, itm_mail_chausses, itm_mail_mittens, itm_nordic_huscarl_helmet, itm_military_hammer, itm_murandy_shield_strong], knight_attrib_2,wp_one_handed(220)|wp(130),knight_skills_2|knows_trainer_3, altara_man_face_older],
  ["knight_24_19", "High Lord Weiramon Saniago", "Weiramon", tf_hero, 0, reserved,  fac_kingdom_24, [itm_lord_warhorse_6, itm_tear_gilded_plate, itm_shynbaulds_wot, itm_gauntlets, itm_tear_elite_helmet, itm_sword_two_handed_b], knight_attrib_4,wp_two_handed(210)|wp(160),knight_skills_4|knows_trainer_5, tear_man_face_old],
  ["knight_24_20", "Lady Anaiyella Narencelona", "Anaiyella", tf_hero|tf_female, 0, reserved,  fac_kingdom_24, [itm_hunter, itm_sarranid_common_dress, itm_aes_sedai_black_ajah_shoes, itm_illian_seax], knight_attrib_3,wp_one_handed(200)|wp(130),knight_skills_3|knows_trainer_4, saldaea_woman_face_older],


# Shara (10)
  ["knight_25_1", "Sh'boan Chiape", "Chiape", tf_hero|tf_female, 0, reserved,  fac_kingdom_25, [itm_arabian_horse_b, itm_sword_khergit_3, itm_ayyad_counsel_member_tunic, itm_sarranid_boots_b], knight_attrib_5,wp_one_handed(275)|wp(230),knight_skills_5|knows_trainer_5, seanchan_2_woman_face_young],
  ["knight_25_2", "Counsellor Sharipe", "Sharipe", tf_hero|tf_female, 0, reserved,  fac_kingdom_25, [itm_arabian_horse_b, itm_power_player, itm_power_ammo, itm_ayyad_counsel_member_tunic, itm_sarranid_boots_b], knight_attrib_5,wp_firearm(205)|wp(230),knight_skills_5|knows_trainer_5|knows_power_draw_8|knows_fire_7|knows_earth_7|knows_spirit_8|knows_water_8|knows_air_8, seanchan_1_woman_face_older],
  ["knight_25_3", "Counsellor Tanule", "Tanule", tf_hero|tf_female, 0, reserved,  fac_kingdom_25, [itm_arabian_horse_b, itm_power_player, itm_power_ammo, itm_ayyad_counsel_member_tunic, itm_sarranid_boots_b], knight_attrib_5,wp_firearm(195)|wp(230),knight_skills_5|knows_trainer_5|knows_power_draw_7|knows_fire_7|knows_earth_7|knows_spirit_8|knows_water_7|knows_air_8, seanchan_1_woman_face_middle],
  ["knight_25_4", "Counsellor Bahryma", "Bahryma", tf_hero|tf_female, 0, reserved,  fac_kingdom_25, [itm_arabian_horse_b, itm_power_player, itm_power_ammo, itm_ayyad_counsel_member_tunic, itm_sarranid_boots_b], knight_attrib_5,wp_firearm(195)|wp(230),knight_skills_5|knows_trainer_5|knows_power_draw_7|knows_fire_7|knows_earth_7|knows_spirit_7|knows_water_8|knows_air_7, seanchan_2_woman_face_older],
  ["knight_25_5", "Lord Alamar", "Alamar", tf_hero, 0, reserved,  fac_kingdom_25, [itm_lord_warhorse_8, itm_khergit_sword_two_handed_b, itm_shara_shbo_guardsman_armor, itm_lamellar_gauntlets, itm_brass_boots, itm_brass_veil_helm], knight_attrib_5,wp_two_handed(275)|wp(230),knight_skills_5|knows_trainer_5, seanchan_1_man_face_older],
  ["knight_25_6", "Lord Dentan", "Dentan", tf_hero, 0, reserved,  fac_kingdom_25, [itm_lord_warhorse_8, itm_khergit_sword_two_handed_b, itm_shara_shbo_guardsman_armor, itm_lamellar_gauntlets, itm_brass_boots, itm_brass_veil_helm], knight_attrib_5,wp_two_handed(270)|wp(230),knight_skills_5|knows_trainer_5, seanchan_1_man_face_middle],
  ["knight_25_7", "Lord Rym", "Rym", tf_hero, 0, reserved,  fac_kingdom_25, [itm_lord_warhorse_8, itm_khergit_sword_two_handed_b, itm_shara_shbo_guardsman_armor, itm_lamellar_gauntlets, itm_brass_boots, itm_brass_veil_helm], knight_attrib_5,wp_two_handed(265)|wp(230),knight_skills_5|knows_trainer_5, seanchan_1_man_face_younger],
  ["knight_25_8", "Lord Ebal", "Ebal", tf_hero, 0, reserved,  fac_kingdom_25, [itm_lord_warhorse_8, itm_khergit_sword_two_handed_b, itm_shara_shbo_guardsman_armor, itm_lamellar_gauntlets, itm_brass_boots, itm_brass_veil_helm], knight_attrib_5,wp_two_handed(260)|wp(230),knight_skills_5|knows_trainer_5, seanchan_2_man_face_older],
  ["knight_25_9", "Lord Seerah", "Seerah", tf_hero, 0, reserved,  fac_kingdom_25, [itm_lord_warhorse_8, itm_khergit_sword_two_handed_b, itm_shara_shbo_guardsman_armor, itm_lamellar_gauntlets, itm_brass_boots, itm_brass_veil_helm], knight_attrib_5,wp_two_handed(270)|wp(230),knight_skills_5|knows_trainer_5, seanchan_2_man_face_middle],
  ["knight_25_10", "Lord Muntid", "Muntid", tf_hero, 0, reserved,  fac_kingdom_25, [itm_lord_warhorse_8, itm_khergit_sword_two_handed_b, itm_shara_shbo_guardsman_armor, itm_lamellar_gauntlets, itm_brass_boots, itm_brass_veil_helm], knight_attrib_5,wp_two_handed(275)|wp(230),knight_skills_5|knows_trainer_5, seanchan_2_man_face_younger],


# Sea Folk (10)  itm_scimitar_b, itm_sea_folk_female_armor, itm_leather_covered_round_shield, itm_leather_gloves
  ["knight_26_1", "Wavemistress Harine din Togara Two Winds", "Harine", tf_hero|tf_female, 0, reserved,  fac_kingdom_26, [itm_scimitar_b, itm_sea_folk_female_armor, itm_leather_covered_round_shield, itm_leather_gloves], knight_attrib_5,wp_one_handed(250)|wp(230),knight_skills_5|knows_trainer_5, seanchan_2_woman_face_old],
  ["knight_26_2", "Wavemistress Malin din Toral Breaking Wave", "Malin", tf_hero|tf_female, 0, reserved,  fac_kingdom_26, [itm_scimitar_b, itm_sea_folk_female_armor, itm_leather_covered_round_shield, itm_leather_gloves], knight_attrib_5,wp_one_handed(265)|wp(230),knight_skills_5|knows_trainer_5, seanchan_2_woman_face_older],
  ["knight_26_3", "Master of the Blades Amel", "Amel", tf_hero, 0, reserved,  fac_kingdom_26, [itm_khergit_sword_two_handed_b, itm_sea_folk_elite_armor, itm_leather_gloves, itm_sea_folk_elite_helmet], knight_attrib_5,wp_two_handed(275)|wp(230),knight_skills_5|knows_trainer_5, seanchan_2_man_face_old],
  ["knight_26_4", "Sailmistress Cemeille din Selaan Long Eyes", "Cemeille", tf_hero|tf_female, 0, reserved,  fac_kingdom_26, [itm_scimitar_b, itm_sea_folk_female_armor, itm_leather_covered_round_shield, itm_leather_gloves], knight_attrib_5,wp_one_handed(275)|wp(230),knight_skills_5|knows_trainer_5, seanchan_2_woman_face_young],
  ["knight_26_5", "Windfinder Shalon din Togara Morning Tide", "Shalon", tf_hero|tf_female, 0, reserved,  fac_kingdom_26, [itm_power_player, itm_power_ammo, itm_sea_folk_female_armor], knight_attrib_5,wp_firearm(205)|wp(230),knight_skills_5|knows_trainer_5|knows_power_draw_8|knows_fire_7|knows_earth_7|knows_spirit_8|knows_water_9|knows_air_8, seanchan_2_woman_face_middle],
  ["knight_26_6", "Swordmaster Moad", "Moad", tf_hero, 0, reserved,  fac_kingdom_26, [itm_khergit_sword_two_handed_b, itm_sea_folk_elite_armor, itm_leather_gloves, itm_sea_folk_elite_helmet], knight_attrib_5,wp_two_handed(285)|wp(230),knight_skills_5|knows_trainer_5, seanchan_2_man_face_young],
  ["knight_26_7", "Cargo Master Toram", "Toram", tf_hero, 0, reserved,  fac_kingdom_26, [itm_khergit_sword_two_handed_b, itm_sea_folk_elite_armor, itm_leather_gloves, itm_sea_folk_elite_helmet], knight_attrib_5,wp_two_handed(280)|wp(230),knight_skills_5|knows_trainer_5, seanchan_2_man_face_middle],
  ["knight_26_8", "Sailmistress Milis din Shalada Three Stars", "Milis", tf_hero|tf_female, 0, reserved,  fac_kingdom_26, [itm_scimitar_b, itm_sea_folk_female_armor, itm_leather_covered_round_shield, itm_leather_gloves], knight_attrib_5,wp_one_handed(275)|wp(230),knight_skills_5|knows_trainer_5, seanchan_2_woman_face_young],
  ["knight_26_9", "Windfinder Renaile din Calon Blue Star", "Renaile", tf_hero|tf_female, 0, reserved,  fac_kingdom_26, [itm_power_player, itm_power_ammo, itm_sea_folk_female_armor], knight_attrib_5,wp_firearm(195)|wp(230),knight_skills_5|knows_trainer_5|knows_power_draw_7|knows_fire_7|knows_earth_7|knows_spirit_8|knows_water_7|knows_air_8, seanchan_2_woman_face_younger],
  ["knight_26_10", "Windfinder Caire din Gelyn Running Wave", "Caire", tf_hero|tf_female, 0, reserved,  fac_kingdom_26, [itm_power_player, itm_power_ammo, itm_sea_folk_female_armor], knight_attrib_5,wp_firearm(195)|wp(230),knight_skills_5|knows_trainer_5|knows_power_draw_7|knows_fire_7|knows_earth_7|knows_spirit_8|knows_water_8|knows_air_7, seanchan_2_woman_face_young],


# Island of Madmen (10)
  ["knight_27_1", "Chief Berend", "Berend", tf_hero, 0, reserved,  fac_kingdom_27, [itm_hunter, itm_great_long_bardiche, itm_hammer, itm_lamellar_vest_khergit, itm_leather_boots, itm_leather_gloves, itm_khergit_war_helmet], knight_attrib_5,wp_polearm(250)|wp(230),knight_skills_5|knows_trainer_5, shienar_man_face_middle, kandor_man_face_older],
  ["knight_27_2", "Chief Detlef", "Detlef", tf_hero, 0, reserved,  fac_kingdom_27, [itm_hunter, itm_great_long_bardiche, itm_hammer, itm_lamellar_vest_khergit, itm_leather_boots, itm_leather_gloves, itm_khergit_war_helmet], knight_attrib_5,wp_polearm(250)|wp(230),knight_skills_5|knows_trainer_5, shienar_man_face_middle, kandor_man_face_older],
  ["knight_27_3", "Chief Emeric", "Emeric", tf_hero, 0, reserved,  fac_kingdom_27, [itm_hunter, itm_great_long_bardiche, itm_hammer, itm_lamellar_vest_khergit, itm_leather_boots, itm_leather_gloves, itm_khergit_war_helmet], knight_attrib_5,wp_polearm(250)|wp(230),knight_skills_5|knows_trainer_5, shienar_man_face_middle, kandor_man_face_older],
  ["knight_27_4", "Chief Hraban", "Hraban", tf_hero, 0, reserved,  fac_kingdom_27, [itm_hunter, itm_great_long_bardiche, itm_hammer, itm_lamellar_vest_khergit, itm_leather_boots, itm_leather_gloves, itm_khergit_war_helmet], knight_attrib_5,wp_polearm(250)|wp(230),knight_skills_5|knows_trainer_5, shienar_man_face_middle, kandor_man_face_older],
  ["knight_27_5", "Chief Jakobi", "Jakob", tf_hero, 0, reserved,  fac_kingdom_27, [itm_hunter, itm_great_long_bardiche, itm_hammer, itm_lamellar_vest_khergit, itm_leather_boots, itm_leather_gloves, itm_khergit_war_helmet], knight_attrib_5,wp_polearm(250)|wp(230),knight_skills_5|knows_trainer_5, shienar_man_face_middle, kandor_man_face_older],
  ["knight_27_6", "Chief Kayetan", "Harine", tf_hero, 0, reserved,  fac_kingdom_27, [itm_hunter, itm_one_handed_battle_axe_b, itm_leather_covered_round_shield, itm_lamellar_vest_khergit, itm_leather_boots, itm_leather_gloves, itm_khergit_war_helmet], knight_attrib_5,wp_polearm(250)|wp(230),knight_skills_5|knows_trainer_5, shienar_man_face_middle, kandor_man_face_older],
  ["knight_27_7", "Chief Merten", "Merten", tf_hero, 0, reserved,  fac_kingdom_27, [itm_hunter, itm_one_handed_battle_axe_b, itm_leather_covered_round_shield, itm_lamellar_vest_khergit, itm_leather_boots, itm_leather_gloves, itm_khergit_war_helmet], knight_attrib_5,wp_polearm(250)|wp(230),knight_skills_5|knows_trainer_5, shienar_man_face_middle, kandor_man_face_older],
  ["knight_27_8", "Chief Rikert", "Rikert", tf_hero, 0, reserved,  fac_kingdom_27, [itm_hunter, itm_one_handed_battle_axe_b, itm_leather_covered_round_shield, itm_lamellar_vest_khergit, itm_leather_boots, itm_leather_gloves, itm_khergit_war_helmet], knight_attrib_5,wp_polearm(250)|wp(230),knight_skills_5|knows_trainer_5, shienar_man_face_middle, kandor_man_face_older],
  ["knight_27_9", "Chief Sikke", "Sikke", tf_hero, 0, reserved,  fac_kingdom_27, [itm_hunter, itm_one_handed_battle_axe_b, itm_leather_covered_round_shield, itm_lamellar_vest_khergit, itm_leather_boots, itm_leather_gloves, itm_khergit_war_helmet], knight_attrib_5,wp_polearm(250)|wp(230),knight_skills_5|knows_trainer_5, shienar_man_face_middle, kandor_man_face_older],
  ["knight_27_10", "Chief Wotan", "Wotan", tf_hero, 0, reserved,  fac_kingdom_27, [itm_hunter, itm_one_handed_battle_axe_b, itm_leather_covered_round_shield, itm_lamellar_vest_khergit, itm_leather_boots, itm_leather_gloves, itm_khergit_war_helmet], knight_attrib_5,wp_polearm(250)|wp(230),knight_skills_5|knows_trainer_5, shienar_man_face_middle, kandor_man_face_older],


# Toman Head (3)  itm_charger, itm_great_sword, itm_toman_head_mail_and_plate, itm_mail_chausses, itm_leather_gloves, itm_nasal_helmet
  
  ["knight_28_1", "Second Watcher Shibaul", "Shibaul", tf_hero, 0, reserved,  fac_kingdom_28, [itm_charger, itm_great_sword, itm_toman_head_mail_and_plate, itm_mail_chausses, itm_leather_gloves, itm_nasal_helmet], knight_attrib_5,wp_two_handed(250)|wp(230),knight_skills_5|knows_trainer_5, arad_doman_man_face_young, tarabon_man_face_old],
  ["knight_28_2", "Governor Terulam", "Terulam", tf_hero, 0, reserved,  fac_kingdom_28, [itm_charger, itm_great_sword, itm_toman_head_mail_and_plate, itm_mail_chausses, itm_leather_gloves, itm_nasal_helmet], knight_attrib_5,wp_two_handed(250)|wp(230),knight_skills_5|knows_trainer_5, arad_doman_man_face_young, tarabon_man_face_old],
  ["knight_28_3", "Lord Hartzul", "Hartzul", tf_hero, 0, reserved,  fac_kingdom_28, [itm_charger, itm_great_sword, itm_toman_head_mail_and_plate, itm_mail_chausses, itm_leather_gloves, itm_nasal_helmet], knight_attrib_5,wp_two_handed(250)|wp(230),knight_skills_5|knows_trainer_5, arad_doman_man_face_young, tarabon_man_face_old],


  
# V: New names for generics and unknowns

## TGS: mat: Pretenders Begin

# complete  
  ["kingdom_1_pretender",  "Mazrim Taim",       "Taim",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_1,[itm_hunter, itm_ashaman_coat, itm_black_leather_boots, itm_power_player, itm_power_ammo], knight_attrib_4,wp_firearm(325)|wp_one_handed(220)|wp(200),knight_skills_4|knows_trainer_3|knows_power_draw_9|knows_fire_10|knows_earth_10|knows_spirit_9|knows_water_9|knows_air_9, saldaea_man_face_middle],
  
  ["kingdom_2_pretender",  "Kingdom_2",       "Kingdom",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_2,[itm_linen_shirt, itm_leather_boots], knight_attrib_4,wp_firearm(250)|wp_one_handed(220)|wp(200),knight_skills_4|knows_trainer_3, saldaea_man_face_middle],
  ["kingdom_3_pretender",  "Kingdom_3",       "Kingdom",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_3,[itm_linen_shirt, itm_leather_boots], knight_attrib_4,wp_firearm(250)|wp_one_handed(220)|wp(200),knight_skills_4|knows_trainer_3, saldaea_man_face_middle],
  ["kingdom_4_pretender",  "Kingdom_4",       "Kingdom",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_4,[itm_linen_shirt, itm_leather_boots], knight_attrib_4,wp_firearm(250)|wp_one_handed(220)|wp(200),knight_skills_4|knows_trainer_3, saldaea_man_face_middle],

# complete
  ["kingdom_5_pretender",  "Lady Colavere", "Colavere",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_5,[itm_courser, itm_lady_dress_blue, itm_woolen_hose, itm_sword_medieval_b_small], knight_attrib_2,wp_one_handed(165)|wp(160),knight_skills_2|knows_trainer_3, cairhien_woman_face_old],

  ["kingdom_6_pretender",  "Kingdom_6",       "Kingdom",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_6,[itm_linen_shirt, itm_leather_boots], knight_attrib_4,wp_firearm(250)|wp_one_handed(220)|wp(200),knight_skills_4|knows_trainer_3, saldaea_man_face_middle],
  ["kingdom_7_pretender",  "Kingdom_7",       "Kingdom",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_7,[itm_linen_shirt, itm_leather_boots], knight_attrib_4,wp_firearm(250)|wp_one_handed(220)|wp(200),knight_skills_4|knows_trainer_3, saldaea_man_face_middle],
  ["kingdom_8_pretender",  "Kingdom_8",       "Kingdom",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_8,[itm_linen_shirt, itm_leather_boots], knight_attrib_4,wp_firearm(250)|wp_one_handed(220)|wp(200),knight_skills_4|knows_trainer_3, saldaea_man_face_middle],
  ["kingdom_9_pretender",  "Kingdom_9",       "Kingdom",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_9,[itm_linen_shirt, itm_leather_boots], knight_attrib_4,wp_firearm(250)|wp_one_handed(220)|wp(200),knight_skills_4|knows_trainer_3, saldaea_man_face_middle],
  ["kingdom_10_pretender",  "Kingdom_10",       "Kingdom",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_10,[itm_linen_shirt, itm_leather_boots], knight_attrib_4,wp_firearm(250)|wp_one_handed(220)|wp(200),knight_skills_4|knows_trainer_3, saldaea_man_face_middle],

# complete
  ["kingdom_11_pretender",  "Lady Arymilla",    "Arymilla",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_11,[itm_courser, itm_lady_dress_ruby, itm_woolen_hose, itm_sword_medieval_b_small], knight_attrib_2,wp_one_handed(165)|wp(160),knight_skills_2|knows_trainer_3, andor_woman_face_young],

  ["kingdom_12_pretender",  "Kingdom_12",       "Kingdom",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_12,[itm_linen_shirt, itm_leather_boots], knight_attrib_4,wp_firearm(250)|wp_one_handed(220)|wp(200),knight_skills_4|knows_trainer_3, saldaea_man_face_middle],
  ["kingdom_13_pretender",  "Kingdom_13",       "Kingdom",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_13,[itm_linen_shirt, itm_leather_boots], knight_attrib_4,wp_firearm(250)|wp_one_handed(220)|wp(200),knight_skills_4|knows_trainer_3, saldaea_man_face_middle],
  ["kingdom_14_pretender",  "Kingdom_14",       "Kingdom",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_14,[itm_linen_shirt, itm_leather_boots], knight_attrib_4,wp_firearm(250)|wp_one_handed(220)|wp(200),knight_skills_4|knows_trainer_3, saldaea_man_face_middle],
  ["kingdom_15_pretender",  "Kingdom_15",       "Kingdom",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_15,[itm_linen_shirt, itm_leather_boots], knight_attrib_4,wp_firearm(250)|wp_one_handed(220)|wp(200),knight_skills_4|knows_trainer_3, saldaea_man_face_middle],
  ["kingdom_16_pretender",  "Kingdom_16",       "Kingdom",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_16,[itm_linen_shirt, itm_leather_boots], knight_attrib_4,wp_firearm(250)|wp_one_handed(220)|wp(200),knight_skills_4|knows_trainer_3, saldaea_man_face_middle],

# complete
  ["kingdom_17_pretender",  "Isam",   "Isam",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_17,[itm_heavy_charger, itm_nobleman_outfit, itm_leather_boots, itm_steel_greaves_wot, itm_shienar_captain_armor, itm_shienar_captain_gauntlets, itm_seanchan_large_sword, itm_winged_great_helmet], knight_attrib_5,wp_two_handed(325)|wp(300),knight_skills_5|knows_trainer_4, 0x0000000b2c04500348628a4b5b72259400000000001e453a0000000000000000],

  ["kingdom_18_pretender",  "Kingdom_18",       "Kingdom",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_18,[itm_linen_shirt, itm_leather_boots], knight_attrib_4,wp_firearm(250)|wp_one_handed(220)|wp(200),knight_skills_4|knows_trainer_3, saldaea_man_face_middle],
  ["kingdom_19_pretender",  "Kingdom_19",       "Kingdom",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_19,[itm_linen_shirt, itm_leather_boots], knight_attrib_4,wp_firearm(250)|wp_one_handed(220)|wp(200),knight_skills_4|knows_trainer_3, saldaea_man_face_middle],
  ["kingdom_20_pretender",  "Kingdom_20",       "Kingdom",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_20,[itm_linen_shirt, itm_leather_boots], knight_attrib_4,wp_firearm(250)|wp_one_handed(220)|wp(200),knight_skills_4|knows_trainer_3, saldaea_man_face_middle],

# complete
  ["kingdom_21_pretender",  "Elaida do Avriny a'Roihan",  "Elaida",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_21,[itm_hunter, itm_aes_sedai_red_dress, itm_veteran_aes_sedai_red_shoes, itm_power_player, itm_power_ammo], knight_attrib_3,wp_firearm(210)|wp_one_handed(175)|wp(130),knight_skills_3|knows_trainer_4|knows_power_draw_8|knows_fire_7|knows_earth_7|knows_spirit_8|knows_water_7|knows_air_8, tar_valon_woman_face_middle],
# complete
  ["kingdom_22_pretender",  "Sevanna",       "Sevanna",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_22,[itm_wise_one_dress_with_shawl, itm_cadinsor_boots, itm_aiel_knife], knight_attrib_3,wp_one_handed(200)|wp(130),knight_skills_3|knows_trainer_4, aiel_2_woman_face_young],
#complete
  ["kingdom_23_pretender",  "High Lady Suroth",       "Suroth",  tf_hero|tf_female|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_23,[itm_arabian_horse_a, itm_sarranid_lady_dress, itm_suldam_boots, itm_aiel_knife], knight_attrib_3,wp_one_handed(200)|wp(130),knight_skills_3|knows_trainer_4, seanchan_1_woman_face_old],
#complete
  ["kingdom_24_pretender",  "Padan Fain",       "Padan Fain",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_24,[itm_saddle_horse, itm_nobleman_outfit, itm_leather_boots, itm_leather_gloves, itm_padan_fain_dagger], lord_attrib,wp(220),knows_lord_1, murandy_man_face_middle],

  ["kingdom_25_pretender",  "Kingdom_25",       "Kingdom",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_25,[itm_linen_shirt, itm_leather_boots], knight_attrib_4,wp_firearm(250)|wp_one_handed(220)|wp(200),knight_skills_4|knows_trainer_3, saldaea_man_face_middle],
  ["kingdom_26_pretender",  "Kingdom_26",       "Kingdom",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_26,[itm_linen_shirt, itm_leather_boots], knight_attrib_4,wp_firearm(250)|wp_one_handed(220)|wp(200),knight_skills_4|knows_trainer_3, saldaea_man_face_middle],
  ["kingdom_27_pretender",  "Kingdom_27",       "Kingdom",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_27,[itm_linen_shirt, itm_leather_boots], knight_attrib_4,wp_firearm(250)|wp_one_handed(220)|wp(200),knight_skills_4|knows_trainer_3, saldaea_man_face_middle],
  ["kingdom_28_pretender",  "Kingdom_28",       "Kingdom",  tf_hero|tf_unmoveable_in_party_window, 0,reserved,  fac_kingdom_28,[itm_linen_shirt, itm_leather_boots], knight_attrib_4,wp_firearm(250)|wp_one_handed(220)|wp(200),knight_skills_4|knows_trainer_3, saldaea_man_face_middle],

## TGS: mat: Pretenders end

##  ["kingdom_1_lord_a", "Kingdom 1 Lord A", "Kingdom 1 Lord A", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_b", "Kingdom 1 Lord B", "Kingdom 1 Lord B", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_c", "Kingdom 1 Lord C", "Kingdom 1 Lord C", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_d", "Kingdom 1 Lord D", "Kingdom 1 Lord D", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_e", "Kingdom 1 Lord E", "Kingdom 1 Lord E", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_f", "Kingdom 1 Lord F", "Kingdom 1 Lord F", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_g", "Kingdom 1 Lord G", "Kingdom 1 Lord G", tf_hero, 0,reserved,  fac_kingdom_1,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_h", "Kingdom 1 Lord H", "Kingdom 1 Lord H", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_i", "Kingdom 1 Lord I", "Kingdom 1 Lord I", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_j", "Kingdom 1 Lord J", "Kingdom 1 Lord J", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_k", "Kingdom 1 Lord K", "Kingdom 1 Lord K", tf_hero, 0,reserved,  fac_kingdom_2,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_l", "Kingdom 1 Lord L", "Kingdom 1 Lord L", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_m", "Kingdom 1 Lord M", "Kingdom 1 Lord M", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],
##  ["kingdom_1_lord_n", "Kingdom 1 Lord N", "Kingdom 1 Lord N", tf_hero, 0,reserved,  fac_kingdom_3,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x00000000000c710201fa51b7286db721],



#  ["town_1_ruler_a", "King Harlaus",  "King Harlaus",  tf_hero, scn_town_1_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_courtly_outfit,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000010908101e36db44b75b6dd],
#  ["town_2_ruler_a", "Duke Taugard",  "Duke Taugard",  tf_hero, scn_town_2_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_courtly_outfit,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000000310401e06db86375f6da],
#  ["town_3_ruler_a", "Count Grimar",  "Count Grimar",  tf_hero, scn_town_3_castle|entry(9),reserved, fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000004430301e46136eb75bc0a],
#  ["town_4_ruler_a", "Count Haxalye", "Count Haxalye", tf_hero, scn_town_4_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000010918701e77136e905bc0e
#  ["town_5_ruler_a", "Count Belicha", "Count Belicha", tf_hero, scn_town_5_castle|entry(9),reserved, fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000421c801e7713729c5b8ce],
#  ["town_6_ruler_a", "Count Nourbis", "Count Nourbis", tf_hero, scn_town_6_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000c640501e371b72bcdb724],
#  ["town_7_ruler_a", "Count Rhudolg", "Count Rhudolg", tf_hero, scn_town_7_castle|entry(9),reserved,  fac_swadians,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000c710201fa51b7286db721],
 
#  ["town_8_ruler_b", "King Yaroglek", "King_yaroglek", tf_hero, scn_town_8_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000000128801f294ca6d66d555],
#  ["town_9_ruler_b", "Count Aolbrug", "Count_Aolbrug", tf_hero, scn_town_9_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000004234401f26a271c8d38ea],
#  ["town_10_ruler_b","Count Rasevas", "Count_Rasevas", tf_hero, scn_town_10_castle|entry(9),reserved, fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000001032c201f38e269372471c],
#  ["town_11_ruler_b","Count Leomir",  "Count_Leomir",  tf_hero, scn_town_11_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000c538001f55148936d3895],
#  ["town_12_ruler_b","Count Haelbrad","Count_Haelbrad",tf_hero, scn_town_12_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x00000000000410c701f38598ac8aaaab],
#  ["town_13_ruler_b","Count Mira",    "Count_Mira",    tf_hero, scn_town_13_castle|entry(9),reserved, fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000004204401f390c515555594],
#  ["town_14_ruler_b","Count Camechaw","Count_Camechaw",tf_hero, scn_town_14_castle|entry(9),reserved,  fac_vaegirs,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],

##  ["kingdom_2_lord_a", "Kingdom 2 Lord A", "Kingdom 2 Lord A", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_b", "Kingdom 2 Lord B", "Kingdom 2 Lord B", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_c", "Kingdom 2 Lord C", "Kingdom 2 Lord C", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_d", "Kingdom 2 Lord D", "Kingdom 2 Lord D", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_e", "Kingdom 2 Lord E", "Kingdom 2 Lord E", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_f", "Kingdom 2 Lord F", "Kingdom 2 Lord F", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_g", "Kingdom 2 Lord G", "Kingdom 2 Lord G", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_h", "Kingdom 2 Lord H", "Kingdom 2 Lord H", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_i", "Kingdom 2 Lord I", "Kingdom 2 Lord I", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_j", "Kingdom 2 Lord J", "Kingdom 2 Lord J", tf_hero, 0,reserved,  fac_kingdom_11,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_k", "Kingdom 2 Lord K", "Kingdom 2 Lord K", tf_hero, 0,reserved,  fac_kingdom_10,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_l", "Kingdom 2 Lord L", "Kingdom 2 Lord L", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_m", "Kingdom 2 Lord M", "Kingdom 2 Lord M", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],
##  ["kingdom_2_lord_n", "Kingdom 2 Lord N", "Kingdom 2 Lord N", tf_hero, 0,reserved,  fac_kingdom_12,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots,itm_coat_of_plates],lord_attrib|level(38),wp(220),knows_common, 0x000000000008318101f390c515555594],



#Royal family members

  ["knight_1_1_wife","Error - knight_1_1_wife should not appear in game","knight_1_1_wife",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_commoners, [itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],

  #Legion of the Dragon "spouses" - eight mothers, eight daughters, four sisters

# Legion of the Dragon
  ["kingdom_1_lady_1","Lady Katunia Flinn","Katunia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_brown_dress,itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_1_lady_2","Lady Emrumeidha Flinn","Emrumeidha",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_brown_dress,itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_1_lady_3","Lady Sereldia Ablar","Sereldia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [       itm_brown_dress,itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_1_lady_4","Lady Junitha Sandomere","Junitha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [        itm_brown_dress,itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],  
  ["kingdom_1_lady_5","Lady Masivin Neald","Masivin",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [     itm_brown_dress,itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_1_lady_6","Sora Grady","Sora",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_brown_dress,itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_1_lady_7","Lady Malaileei Grady","Malaileei",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_brown_dress,itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],


# Band of the Red Hand
  ["kingdom_2_lady_1","Lady Katia Ondin","Katia",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_brown_dress,itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_2_lady_2","Lady Lakimanen Ondin","Lakimanen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [       itm_brown_dress,itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_2_lady_3","Lady Tabaen Vanin","Tabaen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_brown_dress,itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_2_lady_4","Lady Elludia","Elludia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_brown_dress,itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_2_lady_5","Lady Ailavia","Ailavia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_brown_dress,itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],


# Two Rivers  
  ["kingdom_3_lady_1","Natti Cauthon","Natti",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [          itm_brown_dress,itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_3_lady_2","Bodewhin Cauthon","Bode",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [       itm_brown_dress,itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_3_lady_3","Eldrin Cauthon","Eldrin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [       itm_brown_dress,itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_3_lady_4","Marin al'Vere","Marin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_3_lady_5","Lady Feluva al'Seen","Feluva",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],

  # V: New ladies

  
  #Southland Coalition "spouses"

# Mayene
  ["kingdom_4_lady_1","Lady Drina Gallenne","Drina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_green_dress,itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_4_lady_2","Lady Oseanida","Oseanida",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [itm_green_dress,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],


# Cairhien
  ["kingdom_5_lady_1","Lady Tibal Maravin","Tibal",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_brown_dress,itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_5_lady_2","Lady Faerin Maravin","Faerin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [    itm_brown_dress,itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_5_lady_3","Lady Pelaeka Taborwin","Pelaeka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [     itm_brown_dress,itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_5_lady_4","Lady Eldrendrei","Eldrendrei",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_brown_dress,itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_5_lady_5","Lady Nesille","Nesille",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [       itm_brown_dress,itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_5_lady_6","Lady Vemia","Vemia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_brown_dress,itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_5_lady_7","Lady Mordanainen","Mordanainen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [  itm_brown_dress,itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],


# Illian
  ["kingdom_6_lady_1","Lady Seomis Stepanos","Seomis",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [   itm_green_dress,itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_6_lady_2","Lady Tabath Drapeneos","Tabath",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [     itm_green_dress,itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_6_lady_3","Lady Aisha Elamri","Aisha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [     itm_green_dress,itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_6_lady_4","Lady Tesladayamei","Tesladayamei",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [  itm_green_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_6_lady_5","Lady Moirilin","Moirilin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6,  [     itm_green_dress, itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_6_lady_6","Lady Ciliin","Ciliin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [     itm_green_dress, itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_6_lady_7","Lady Faolalien","Faolalien",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_6, [   itm_green_dress,  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],


# Murandy
  ["kingdom_7_lady_1","Lady Haris do Cian a'Macansa","Haris",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,  [   itm_green_dress, itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_7_lady_2","Lady Sucildey","Sucildey",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,  [   itm_green_dress, itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_7_lady_3","Lady Tesiven","Tesiven",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [     itm_green_dress, itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_7_lady_4","Lady Cavaenicei","Cavaenicei",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [    itm_green_dress, itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_7_lady_5","Lady Alomei","Alomei",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,  [   itm_green_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_7_lady_6","Lady Masiy","Masiy",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7,  [  itm_green_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_7_lady_7","Lady Emrulei","Emrulei",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_7, [  itm_green_dress,  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],


# Altara
  ["kingdom_8_lady_1","Lady Vayen Contar","Vayen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [   itm_red_dress ,  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_8_lady_2","Lady Lana Vendare","Lana",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [    itm_red_dress ,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_8_lady_3","Lady Sulen","Sulen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [ itm_red_dress ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_8_lady_4","Lady Jeonien","Jeonien",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [itm_green_dress,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
  ["kingdom_8_lady_5","Lady Deindryllade","Deindryllade",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [    itm_red_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_8_lady_6","Lady Cemiei","Cemiei",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8, [   itm_red_dress ,  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_8_lady_7","Lady Nareslyia","Nareslyia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_8,  [  itm_red_dress ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],


# Arad Doman
  ["kingdom_9_lady_1","Lady Nesha Ituralde","Nesha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [      itm_green_dress, itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
  ["kingdom_9_lady_2","Lady Tamsin Ituralde","Tamsin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9,  [   itm_green_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
  ["kingdom_9_lady_3","Lady Joaka Callswell","Joaka",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [     itm_green_dress,  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
  ["kingdom_9_lady_4","Lady Masahe","Masahe",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_9, [      itm_green_dress, itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],

  
#  ["kingdom_2_lady_14","Lady Tenica","Tenica",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],
#  ["kingdom_2_lady_15","Lady Leluve","Leluve",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000007080004782a6cc4ecae4d1e00000000001eb6e30000000000000000],
#  ["kingdom_2_lady_16","Lady Ispas","Ispas",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2,  [       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054008200638db99d89eccbd3500000000001ec91d0000000000000000],
#  ["kingdom_2_lady_17","Lady Eldrasen","Eldrasen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007c0101002588caf17142ab93d00000000001ddfa40000000000000000],
#  ["kingdom_2_lady_18","Lady Elleinen","Elleinen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_2, [  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008c00c20032aa5ae36b4259b9300000000001da6a50000000000000000],


#Southland Alliance "Spouses"

# Tear
  ["kingdom_10_lady_1","Lady Tuan Andiama","Tuan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_10_lady_2","Lady Ceen","Ceen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
  ["kingdom_10_lady_3","Lady Pendhren","Pendhren",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
  ["kingdom_10_lady_4","Lady Elolinday","Elolinday",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001ad003001628c54b05d2e48b200000000001d56e60000000000000000],
  ["kingdom_10_lady_5","Lady Beldien", "Beldien",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001a700300265cb6db15d6db6da00000000001f82180000000000000000],
  ["kingdom_10_lady_6","Lady Nicollienin","Nicollienin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_10_lady_7","Lady Darla","Darla",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_10_lady_8","Lady Myretin","Myretin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_10,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],


# Andor
  ["kingdom_11_lady_1","Lady Ayasu Traemaene","Ayasu",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11,  [    itm_red_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["kingdom_11_lady_2","Lady Ravina Sarand","Ravina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_11_lady_3","Lady Ruha Pensenor","Ruha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_11_lady_4","Lady Elenia Sarand","Elenia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11,  [    itm_brown_dress,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_11_lady_5","Lady Chedina","Chedina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11,  [    itm_brown_dress,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_11_lady_6","Lady Lareme","Lareme",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_11_lady_7","Lady Faridia","Faridia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001940c3006019c925165d1129b00000000001d13240000000000000000],
  ["kingdom_11_lady_8","Lady Payara","Payara",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
  ["kingdom_11_lady_9","Lady Mollei","Mollei",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000019b083005389591941379b8d100000000001e63150000000000000000],
  ["kingdom_11_lady_10","Lady Konellein","Konellein",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["kingdom_11_lady_11","Lady Tamrevin","Tamrevin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_11, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],


# Ghealdan
  ["kingdom_12_lady_1","Lady Mahraz","Mahraz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [itm_red_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
  ["kingdom_12_lady_2","Lady Ayasu","Ayasu",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12,  [    itm_red_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["kingdom_12_lady_3","Lady Ravin","Ravin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],
  ["kingdom_12_lady_4","Lady Ruha","Ruha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_12, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],


# Far Madding
  ["kingdom_13_lady_1","Lady Borge Barsalla","Borge",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_13, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
  ["kingdom_13_lady_2","Lady Mahraz Maslin","Mahraz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_13, [itm_red_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],


# Tarabon  
  ["kingdom_14_lady_1","Lady Kefra","Kefra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
  ["kingdom_14_lady_2","Lady Nirvaz","Nirvaz",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001940c3006019c925165d1129b00000000001d13240000000000000000],
  ["kingdom_14_lady_3","Lady Dulua","Dulua",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_14, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],


# Amadicia
  ["kingdom_15_lady_1","Lady Selika","Selika",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_15,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000019b083005389591941379b8d100000000001e63150000000000000000],
  ["kingdom_15_lady_2","Lady Thalatha","Thalatha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_15,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
  ["kingdom_15_lady_3","Lady Yasreen","Yasreen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_15, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000056e082002471c91c8aa2a130b00000000001d48a40000000000000000],


# Children of the Light
  ["kingdom_16_lady_1","Lady Nadha","Nadha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_16, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
  ["kingdom_16_lady_2","Lady Zenur","Zenur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_16,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_2],
  ["kingdom_16_lady_3","Lady Arjis","Zenur",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_16,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001ad003001628c54b05d2e48b200000000001d56e60000000000000000],


#  ["kingdom_3_lady_17","Lady Atjahan", "Atjahan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001a700300265cb6db15d6db6da00000000001f82180000000000000000],
#  ["kingdom_3_lady_18","Lady Qutala","Qutala",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],
#  ["kingdom_3_lady_19","Lady Hindal","Hindal",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000320c30023ce23a145a8f27a300000000001ea6dc0000000000000000],
#  ["kingdom_3_lady_20","Lady Mechet","Mechet",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3,  [    itm_brown_dress ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000002a0c200348a28f2a54aa391c00000000001e46d10000000000000000],
#  ["kingdom_3_lady_21","Lady Borge","Borge",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_brown_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, khergit_woman_face_1],
#  ["kingdom_3_lady_22","Lady Tuan","Tuan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_3, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000008ec0820062ce4d246b38e632e00000000001d52910000000000000000],

  

#Borderlands "spouses"

# Shienar
  ["kingdom_17_lady_1","Lady Eir","Eir",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_17,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_17_lady_2","Lady Lutamae","Lutamae",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_17,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_17_lady_3","Lady Ingunn","Ingunn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_17, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_17_lady_4","Lady Kaeteli","Kaeteli",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_17, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_17_lady_5","Lady Aesa","Aesa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_17, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],


# Arafel
  ["kingdom_18_lady_1","Lady Kawisu Terasian","Kawisu",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_18, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],
  ["kingdom_18_lady_2","Lady Intowa Terasian","Intowa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_18,  [    itm_peasant_dress, itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_18_lady_3","Lady Bryn Shianri","Bryn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_18, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],


# Kandor
  ["kingdom_19_lady_1","Lady Jarene Noramaga","Jarene",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_19, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_19_lady_2","Lady Lellallei","Lellallei",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_19, [      itm_court_dress ,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_19_lady_3","Lady Pellein","Pellein",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_19,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
  ["kingdom_19_lady_4","Lady Pascha","Pascha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_19,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
  ["kingdom_19_lady_5","Lady Rialla","Rialla",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_19,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],


# Saldaea
  ["kingdom_20_lady_1","Lady Deira ni'Ghaline t'Bashere","Deira",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_20, [    itm_green_dress,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_20_lady_2","Lady Faile ni Bashere t'Aybara","Faile",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_20,  [    itm_green_dress,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_20_lady_3","Lady Faluanen","Faluanen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_20, [      itm_court_dress ,  itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054b100003274d65d2d239eb1300000000001d49080000000000000000],
  ["kingdom_20_lady_4","Lady Tematia","Tematia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_20, [      itm_court_dress ,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000058610000664d3693664f0c54b00000000001d332d0000000000000000],


#  ["kingdom_4_lady_8","Lady Thera","Thera",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],
#  ["kingdom_4_lady_15","Lady Eilif","Eilif",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000469a4d5cda4b1349c00000000001cd6600000000000000000],
#  ["kingdom_4_lady_16","Lady Doinen","Doinen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_4,  [    itm_peasant_dress,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000000021564d196e2aa279400000000001dc4ed0000000000000000],

# end TGS changes

# White Tower "Spouses"
  
  ["kingdom_21_lady_1","Lady Brina Chubain","Brina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_21, [      itm_lady_dress_green,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_21_lady_2","Lady Aliena","Aliena",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_21, [      itm_lady_dress_green,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
  ["kingdom_21_lady_3","Lady Aneth","Aneth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_21,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_21_lady_4","Lady Reada","Reada",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_21,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
# changed names for ladies 5 through 20 for TGS
  ["kingdom_21_lady_5","Lady Saraten","Saraten",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_21, [      itm_lady_dress_green,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_21_lady_6","Lady Baotheia","Baotheia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_21, [itm_lady_dress_green,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000bf0400035913aa236b4d975a00000000001eb69c0000000000000000],
  ["kingdom_21_lady_7","Lady Eleandra","Eleandra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_21,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
  ["kingdom_21_lady_8","Lady Meraced","Meraced",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_21,  [ itm_lady_dress_ruby ,     itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
  ["kingdom_21_lady_9","Lady Adelisa","Adelisa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_21, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
  ["kingdom_21_lady_10","Lady Calantina","Calantina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_21, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],


#  ["kingdom_5_lady_11","Lady Forbesa","Forbesa",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
#  ["kingdom_5_lady_12","Lady Claudora","Claudora",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
#  ["kingdom_5_lady_13","Lady Anais","Anais",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
#  ["kingdom_5_lady_14","Lady Miraeia","Miraeia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
#  ["kingdom_5_lady_15","Lady Agasia","Agasia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
#  ["kingdom_5_lady_16","Lady Geneiava","Geneiava",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],
#  ["kingdom_5_lady_17","Lady Gwenael","Gwenael",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000007e900200416ed96e88b8d595a00000000001cb8ac0000000000000000],
#  ["kingdom_5_lady_18","Lady Ysueth","Ysueth",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5, [      itm_lady_dress_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057008200222d432cf6d4a2ae300000000001d37a10000000000000000],
#  ["kingdom_5_lady_19","Lady Ellian","Ellian",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000001b9002002364dd8aa5475d76400000000001db8d30000000000000000],
#  ["kingdom_5_lady_20","Lady Timethi","Timethi",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_5,  [ itm_lady_dress_ruby ,  itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000057a0000014123dae69e8e48e200000000001e08db0000000000000000],

# end TGS changes
  
# Aiel Nation "Spouses"
  
  ["kingdom_22_lady_1","Jaihlle","Jaihlle",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22, [itm_wise_one_dress,        itm_cadinsor_boots],     def_attrib|level(2),wp(50),knows_common, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_22_lady_2","Thanaikha","Thanaikha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22, [itm_wise_one_dress,      itm_cadinsor_boots],     def_attrib|level(2),wp(50),knows_common, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_22_lady_3","Sulaha","Sulaha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22,  [itm_wise_one_dress,       itm_cadinsor_boots], def_attrib|level(2),wp(50),knows_common, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_22_lady_4","Sevotanra","Sevotanra",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22,  [itm_wise_one_dress,       itm_cadinsor_boots], def_attrib|level(2),wp(50),knows_common, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_22_lady_5","Wise One Bawthan","Bawthan",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22, [itm_wise_one_dress_with_shawl,      itm_cadinsor_boots],     def_attrib|level(2),wp(50),knows_common, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_22_lady_6","Wise One Mahayl","Mahayl",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22, [itm_wise_one_dress_with_shawl,      itm_cadinsor_boots],     def_attrib|level(2),wp(50),knows_common,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_22_lady_7","Wise One Isna","Isna",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22, [itm_wise_one_dress_with_shawl,      itm_cadinsor_boots],     def_attrib|level(2),wp(50),knows_common, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_22_lady_8","Roofmistress Lian","Lian",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22, [itm_wise_one_dress_with_shawl,        itm_cadinsor_boots],     def_attrib|level(2),wp(50),knows_common, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_22_lady_9","Wise One Ifar","Ifar",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22, [itm_wise_one_dress_with_shawl,      itm_cadinsor_boots],     def_attrib|level(2),wp(50),knows_common, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_22_lady_10","Roofmistress Yasmin","Yasmin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22, [itm_wise_one_dress,       itm_cadinsor_boots],     def_attrib|level(2),wp(50),knows_common,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_22_lady_11","Roofmistress Dula","Dula",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22, [itm_wise_one_dress,      itm_cadinsor_boots],     def_attrib|level(2),wp(50),knows_common, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_22_lady_12","Niella","Niella",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22, [itm_wise_one_dress,       itm_cadinsor_boots],     def_attrib|level(2),wp(50),knows_common,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_22_lady_13","Wise One Luqa","Luqa",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22, [itm_wise_one_dress_with_shawl,     itm_cadinsor_boots],     def_attrib|level(2),wp(50),knows_common, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_22_lady_14","Wise One Zandina","Zandina",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22, [itm_wise_one_dress_with_shawl,      itm_cadinsor_boots],     def_attrib|level(2),wp(50),knows_common, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_22_lady_15","Apprentice Lulya","Lulya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22, [itm_wise_one_dress,       itm_cadinsor_boots],     def_attrib|level(2),wp(50),knows_common, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_22_lady_16","Apprentice Zahara","Zahara",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22, [itm_wise_one_dress,      itm_cadinsor_boots],     def_attrib|level(2),wp(50),knows_common, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_22_lady_17","Apprentice Safiya","Safiya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22, [itm_wise_one_dress,      itm_cadinsor_boots],     def_attrib|level(2),wp(50),knows_common, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_22_lady_18","Naenr","Naenr",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22, [itm_wise_one_dress,      itm_cadinsor_boots],     def_attrib|level(2),wp(50),knows_common, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_22_lady_19","Wise One Jair","Jair",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22, [itm_wise_one_dress,      itm_cadinsor_boots],     def_attrib|level(2),wp(50),knows_common, swadian_woman_face_1],
  ["kingdom_22_lady_20","Domann","Domann",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_22, [itm_wise_one_dress,      itm_cadinsor_boots],     def_attrib|level(2),wp(50),knows_common, swadian_woman_face_2],

# V: FIXME: Get rid of riding and head dresses etc

# Seanchan Empire "Spouses"
  
  ["kingdom_23_lady_1","Lady Essin Loune","Essin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23, [itm_sarranid_lady_dress,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_23_lady_2","Lady Forsal Najirah","Forsal",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_23_lady_3","Lady Busein Najirah","Busein",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_23_lady_4","Lady Darsaen Faloun","Laer",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_23_lady_5","Lady Femela Faloun","Paen",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_23_lady_6","Lady Eluvine Nothish","Eldrig",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_23_lady_7","Lady Yin Shumada","Yin",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_23_lady_8","Lady Larlona","Larlona",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23, [itm_sarranid_lady_dress_b,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_23_lady_9","Lady Tauavyn","Tauavyn",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_23_lady_10","Lady Mulada","Mulada",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23, [itm_sarranid_lady_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_23_lady_11","Lady Tarela","Tarela",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_23_lady_12","Lady Anbara","Anbara",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23, [itm_sarranid_lady_dress_b,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_23_lady_13","Lady Egannoth","Egannoth",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23, [itm_sarranid_lady_dress_b,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_23_lady_14","Lady Bealgwia","Bealgwia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_23_lady_15","Lady Lulya","Lulya",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23, [itm_sarranid_lady_dress_b,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_23_lady_16","Lady Dairsia","Dairsia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_23_lady_17","Lady Moreri","Moreri",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_23_lady_18","Lady Rinas","Rinas",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_23_lady_19","Lady Abanine","Abanine",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_23_lady_20","Lady Zathela","Zathela",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_23, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],


# Shadowspawn "Spouses"
  
  ["kingdom_24_lady_1","Lady Eldrene","Eldrene",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_24, [itm_sarranid_lady_dress,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  ["kingdom_24_lady_2","Lady Tianua","Tianua",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_24, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000054f08100232636aa90d6e194b00000000001e43130000000000000000],
  ["kingdom_24_lady_3","Lady Bany","Bany",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_24,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000018f0410064854c742db74b52200000000001d448b0000000000000000],
  ["kingdom_24_lady_4","Lady Emruia","Emruia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_24,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000204200629b131e90d6a8ae400000000001e28dd0000000000000000],
  ["kingdom_24_lady_5","Lady Fiena","Fiena",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_24, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_24_lady_6","Lady Kanice","Kanice",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_24, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000000d0820011693b142ca6a271a00000000001db6920000000000000000],
  ["kingdom_24_lady_7","Lady Isna","Isna",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_24, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_24_lady_8","Lady Siyafan","Siyafan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_24, [itm_sarranid_lady_dress_b,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000001900000542ac4e76d5d0d35300000000001e26a40000000000000000],
  ["kingdom_24_lady_9","Lady Tilinen","Tilinen",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_24, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_24_lady_10","Lady Vaiven","Vaiven",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_24, [itm_sarranid_lady_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   0x000000003a00200646a129464baaa6db00000000001de7a00000000000000000],
  ["kingdom_24_lady_11","Lady Ailile","Ailile",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_24, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_24_lady_12","Lady Miinen","Miinen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_24, [itm_sarranid_lady_dress_b,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,  0x000000003f04100148d245d6526d456b00000000001e3b350000000000000000],
  ["kingdom_24_lady_13","Lady Semenei","Semenei",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_24, [itm_sarranid_lady_dress_b,     itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_24_lady_14","Lady Sherata","Sherata",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_24, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003a0c3003358a56d51c8e399400000000000944dc0000000000000000],
  ["kingdom_24_lady_15","Lady Fodaren","Fodaren",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_24, [itm_sarranid_lady_dress_b,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_24_lady_16","Lady Myrdea","Myrdea",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_24, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000003b080003531e8932e432bb5a000000000008db6a0000000000000000],
  ["kingdom_24_lady_17","Lady Gaiyaia","Gaiyaia",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_24, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x00000000000c000446e4b4c2cc5234d200000000001ea3120000000000000000],
  ["kingdom_24_lady_18","Lady Baredray","Baredray",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_24, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x0000000000083006465800000901161200000000001e38cc0000000000000000],
  ["kingdom_24_lady_19","Lady Pusanin","Pusanin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_24, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1],
  ["kingdom_24_lady_20","Lady Sheriaen","Sheriaen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_24, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_2],


# Shara "Spouses"
  
  ["kingdom_25_lady_1","Lady Adibah","Adibah",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_25, [itm_sarranid_lady_dress,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, woman_face_1, woman_face_2],
  ["kingdom_25_lady_2","Lady Fareeha","Fareeha",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_25, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, woman_face_1, woman_face_2],
  ["kingdom_25_lady_3","Lady Mahasen","Mahasen",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_25,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, woman_face_1, woman_face_2],
  ["kingdom_25_lady_4","Lady Rashidah","Rashidah",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_25,  [itm_sarranid_lady_dress,       itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, woman_face_1, woman_face_2],
  ["kingdom_25_lady_5","Lady Shimah","Shimah",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_25, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, woman_face_1, woman_face_2],
  ["kingdom_25_lady_6","Lady Kamila","Kamila",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_25, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   woman_face_1, woman_face_2],
  ["kingdom_25_lady_7","Lady Duriyah","Duriyah",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_25, [itm_sarranid_lady_dress,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_25_lady_8","Lady Zahrah","Zahrah",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_25, [itm_sarranid_lady_dress_b,        itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, woman_face_1, woman_face_2],
  ["kingdom_25_lady_9","Lady Nadia","Nadia",tf_hero|tf_randomize_face|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_25, [itm_sarranid_lady_dress_b,      itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, swadian_woman_face_1, swadian_woman_face_2],
  ["kingdom_25_lady_10","Lady Thara","Thara",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_25, [itm_sarranid_lady_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2,   woman_face_1, woman_face_2],


# Sea Folk "Spouses"

  ["kingdom_26_lady_1","Talaan din Gelyn","Talaan",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_26, [itm_sea_folk_female_tunic],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, seanchan_2_woman_face_younger, seanchan_2_woman_face_old],
  ["kingdom_26_lady_2","Ehvon","Ehvon",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_26, [itm_sea_folk_female_tunic],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, seanchan_2_woman_face_younger, seanchan_2_woman_face_old],
  ["kingdom_26_lady_3","Jadein","Jadein",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_26, [itm_sea_folk_female_tunic],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, seanchan_2_woman_face_younger, seanchan_2_woman_face_old],
  ["kingdom_26_lady_4","Coine de Jubai Wild Winds","Coine",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_26, [itm_sea_folk_female_tunic],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, seanchan_2_woman_face_younger, seanchan_2_woman_face_old],
  ["kingdom_26_lady_5","Kurin","Kurin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_26, [itm_sea_folk_female_tunic],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, seanchan_2_woman_face_younger, seanchan_2_woman_face_old],
  ["kingdom_26_lady_6","Naime","Naime",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_26, [itm_sea_folk_female_tunic_2],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, seanchan_2_woman_face_younger, seanchan_2_woman_face_old],
  ["kingdom_26_lady_7","Rysael","Rysael",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_26, [itm_sea_folk_female_tunic_2],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, seanchan_2_woman_face_younger, seanchan_2_woman_face_old],
  ["kingdom_26_lady_8","Senine","Senine",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_26, [itm_sea_folk_female_tunic_2],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, seanchan_2_woman_face_younger, seanchan_2_woman_face_old],
  ["kingdom_26_lady_9","Serile","Serile",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_26, [itm_sea_folk_female_tunic_2],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, seanchan_2_woman_face_younger, seanchan_2_woman_face_old],
  ["kingdom_26_lady_10","Turane","Turane",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_26, [itm_sea_folk_female_tunic_2],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, seanchan_2_woman_face_younger, seanchan_2_woman_face_old],
  

# Island of Madmen "Spouses"

  ["kingdom_27_lady_1","Amalie","Amalie",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_27, [itm_khergit_lady_dress_b],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, woman_face_1, woman_face_2],
  ["kingdom_27_lady_2","Bruna","Bruna",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_27, [itm_khergit_lady_dress_b],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, woman_face_1, woman_face_2],
  ["kingdom_27_lady_3","Gerde","Gerde",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_27, [itm_khergit_lady_dress_b],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, woman_face_1, woman_face_2],
  ["kingdom_27_lady_4","Hedda","Hedda",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_27, [itm_khergit_lady_dress_b],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, woman_face_1, woman_face_2],
  ["kingdom_27_lady_5","Ilse","Ilse",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_27, [itm_khergit_lady_dress_b],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, woman_face_1, woman_face_2],
  ["kingdom_27_lady_6","Katrin","Katrin",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_27, [itm_khergit_lady_dress_b],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, woman_face_1, woman_face_2],
  ["kingdom_27_lady_7","Madde","Madde",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_27, [itm_khergit_lady_dress_b],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, woman_face_1, woman_face_2],
  ["kingdom_27_lady_8","Nadja","Nadja",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_27, [itm_khergit_lady_dress_b],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, woman_face_1, woman_face_2],
  ["kingdom_27_lady_9","Senta","Senta",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_27, [itm_khergit_lady_dress_b],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, woman_face_1, woman_face_2],
  ["kingdom_27_lady_10","Verena","Verena",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_27, [itm_khergit_lady_dress_b],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, woman_face_1, woman_face_2],


# Toman Head "Spouses"

  ["kingdom_28_lady_1","Lady Sharine","Sharine",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_28, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, arad_doman_woman_face_middle, tarabon_woman_face_old],
  ["kingdom_28_lady_2","Lady Jesslyn","Jesslyn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_28, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, arad_doman_woman_face_young, tarabon_woman_face_middle],
  ["kingdom_28_lady_3","Lady Karyn","Karyn",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_28, [      itm_green_dress,       itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, arad_doman_woman_face_middle, tarabon_woman_face_old],
  


################## Ladies End ####################  

  
#  ["kingdom_11_lord_daughter","kingdom_11_lord_daughter","kingdom_11_lord_daughter",tf_hero|tf_female,0,reserved,fac_kingdom_10,  [ itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008300701c08d34a450ce43],
#  ["kingdom_13_lord_daughter","kingdom_13_lord_daughter","kingdom_13_lord_daughter",tf_hero|tf_female,0,reserved,fac_kingdom_10,  [ itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008000401db10a45b41d6d8],
##  ["kingdom_1_lady_a","kingdom_1_lady_a","kingdom_1_lady_a",tf_hero|tf_female,0,reserved,fac_kingdom_1, [   itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],
##  ["kingdom_1_lady_b","kingdom_1_lady_b","kingdom_1_lady_b",tf_hero|tf_female,0,reserved,fac_kingdom_1, [   itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000101c3ae68e0e944ac],
##  ["kingdom_2_lady_a","Kingdom 2 Lady a","Kingdom 2 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_2, [               itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008100501d8ad93708e4694],
##  ["kingdom_2_lady_b","Kingdom 2 Lady b","Kingdom 2 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_2, [               itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000004000401d8ad93708e4694],
##  ["kingdom_3_lady_a","Kingdom 3 Lady a","Kingdom 3 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_3, [               itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500301d8ad93708e4694],
##
##  ["kingdom_3_lady_b","Kingdom 3 Lady b","Kingdom 3 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_3,  [                         itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000000100601d8b08d76d14a24],
##  ["kingdom_4_lady_a","Kingdom 4 Lady a","Kingdom 4 Lady a",tf_hero|tf_female,0,reserved,fac_kingdom_4,  [                         itm_lady_dress_green,   itm_turret_hat_green,   itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000010500601d8ad93708e4694],
##  ["kingdom_4_lady_b","Kingdom 4 Lady b","Kingdom 4 Lady b",tf_hero|tf_female,0,reserved,fac_kingdom_4,  [                         itm_lady_dress_blue ,   itm_turret_hat_blue,    itm_leather_boots], def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000000008500201d8ad93708e4694],

  ["heroes_end", "{!}heroes end", "{!}heroes end", tf_hero, 0,reserved,  fac_neutral,[itm_saddle_horse,itm_leather_jacket,itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, 0x000000000008318101f390c515555594],
#Merchants                                                                              AT                      SILAH                   ZIRH                        BOT                         Head_wear
##  ["merchant_1", "merchant_1_F", "merchant_1_F",tf_hero|tf_female,  0,0, fac_kingdom_1,[itm_courser,            itm_fighting_axe,       itm_leather_jerkin,         itm_leather_boots,          itm_straw_hat],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008200201e54c137a940c91],
##  ["merchant_2", "merchant_2", "merchant_2", tf_hero,               0,0, fac_kingdom_2,[itm_saddle_horse,       itm_arming_sword,       itm_light_leather,          itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000000601db6db6db6db6db],
##  ["merchant_3", "merchant_3", "merchant_3", tf_hero,               0,0, fac_kingdom_3,[itm_courser,            itm_nordic_sword,       itm_leather_jerkin,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008100701db6db6db6db6db],
##  ["merchant_4", "merchant_4_F", "merchant_4_F",tf_hero|tf_female,  0,0, fac_kingdom_4,[itm_saddle_horse,       itm_falchion,           itm_light_leather,          itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401e54c137a945c91],
##  ["merchant_5", "merchant_5", "merchant_5", tf_hero,               0,0, fac_kingdom_5,[itm_saddle_horse,       itm_sword,              itm_ragged_outfit,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008038001e54c135a945c91],
##  ["merchant_6", "merchant_6", "merchant_6", tf_hero,               0,0, fac_kingdom_1,[itm_saddle_horse,      itm_scimitar,           itm_leather_jerkin,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000000248e01e54c1b5a945c91],
##  ["merchant_7", "merchant_7_F", "merchant_7_F",tf_hero|tf_female,  0,0, fac_kingdom_2,[itm_hunter,            itm_arming_sword,       itm_padded_leather,         itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004200601c98ad39c97557a],
##  ["merchant_8", "merchant_8", "merchant_8", tf_hero,               0,0, fac_kingdom_3,[itm_saddle_horse,      itm_nordic_sword,       itm_light_leather,          itm_leather_boots,          itm_woolen_hood],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001095ce01d6aad3a497557a],
##  ["merchant_9", "merchant_9", "merchant_9", tf_hero,               0,0, fac_kingdom_4,[itm_saddle_horse,      itm_sword,              itm_padded_leather,         itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010519601ec26ae99898697],
##  ["merchant_10","merchant_10","merchant_10",tf_hero,               0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,      itm_light_leather,          itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000884c401f6837d3294e28a],
##  ["merchant_11","merchant_11","merchant_11",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_leather_jacket,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c450501e289dd2c692694],
##  ["merchant_12","merchant_12","merchant_12",tf_hero,               0,0, fac_merchants,[itm_hunter,             itm_falchion,           itm_leather_jerkin,         itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c660a01e5af3cb2763401],
##  ["merchant_13","merchant_13","merchant_13",tf_hero,               0,0, fac_merchants,[itm_sumpter_horse,      itm_nordic_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000001001d601ec912a89e4d534],
##  ["merchant_14","merchant_14","merchant_14",tf_hero,               0,0, fac_merchants,[itm_courser,            itm_bastard_sword,      itm_light_leather,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000004335601ea2c04a8b6a394],
##  ["merchant_15","merchant_15","merchant_15",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_padded_leather,         itm_woolen_hose,            itm_fur_hat],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008358e01dbf27b6436089d],
##  ["merchant_16","merchant_16_F","merchant_16_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_hunter,             itm_bastard_sword,      itm_light_leather,          itm_hide_boots,                             ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x00000000000c300101db0b9921494add],
##  ["merchant_17","merchant_17","merchant_17",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_sword,              itm_leather_jacket,         itm_blue_hose,                              ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008740f01e945c360976a0a],
##  ["merchant_18","merchant_18","merchant_18",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_nordic_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008020c01fc2db3b4c97685],
##  ["merchant_19","merchant_19","merchant_19",tf_hero,               0,0, fac_merchants,[itm_saddle_horse,       itm_falchion,           itm_leather_jerkin,         itm_woolen_hose,                            ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000008118301f02af91892725b],
##  ["merchant_20","merchant_20_F","merchant_20_F",tf_hero|tf_female, 0,0, fac_merchants,[itm_courser,            itm_arming_sword,       itm_padded_leather,         itm_leather_boots,                          ],              def_attrib|level(15),wp(100),knows_inventory_management_10, 0x000000000010500401f6837d27688212],

  
#Seneschals
  ["town_1_seneschal", "{!}Town 1 Seneschal", "{!}Town 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_2_seneschal", "{!}Town 2 Seneschal", "{!}Town 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["town_3_seneschal", "{!}Town 3 Seneschal", "{!}Town 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["town_4_seneschal", "{!}Town 4 Seneschal", "{!}Town 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["town_5_seneschal", "{!}Town 5 Seneschal", "{!}Town 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000000249101e7898999ac54c6],
  ["town_6_seneschal", "{!}Town 6 Seneschal", "{!}Town 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["town_7_seneschal", "{!}Town 7 Seneschal", "{!}Town7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000000018101f9487aa831dce4],
  ["town_8_seneschal", "{!}Town 8 Seneschal", "{!}Town 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["town_9_seneschal", "{!}Town 9 Seneschal", "{!}Town 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["town_10_seneschal", "{!}Town 10 Seneschal", "{!}Town 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000010230c01ef41badb50465e],
  ["town_11_seneschal", "{!}Town 11 Seneschal", "{!}Town 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["town_12_seneschal", "{!}Town 12 Seneschal", "{!}Town 12 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["town_13_seneschal", "{!}Town 13 Seneschal", "{!}Town 13 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["town_14_seneschal", "{!}Town 14 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_15_seneschal", "{!}Town 15 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_16_seneschal", "{!}Town 16 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_17_seneschal", "{!}Town17 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_18_seneschal", "{!}Town 18 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_19_seneschal", "{!}Town 19 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_20_seneschal", "{!}Town 20 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_21_seneschal", "{!}Town 21 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_22_seneschal", "{!}Town 22 Seneschal", "{!}Town 14 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
## TGS: mat: Added for new Towns
  ["town_23_seneschal", "{!}Town 23 Seneschal", "{!}Town 23 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["town_24_seneschal", "{!}Town 24 Seneschal", "{!}Town 24 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["town_25_seneschal", "{!}Town 25 Seneschal", "{!}Town 25 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["town_26_seneschal", "{!}Town 26 Seneschal", "{!}Town 26 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["town_27_seneschal", "{!}Town 27 Seneschal", "{!}Town 27 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000000249101e7898999ac54c6],
  ["town_28_seneschal", "{!}Town 28 Seneschal", "{!}Town 28 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["town_29_seneschal", "{!}Town 29 Seneschal", "{!}Town 29 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000000018101f9487aa831dce4],
  ["town_30_seneschal", "{!}Town 30 Seneschal", "{!}Town 30 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["town_31_seneschal", "{!}Town 31 Seneschal", "{!}Town 31 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["town_32_seneschal", "{!}Town 32 Seneschal", "{!}Town 32 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000010230c01ef41badb50465e],
  ["town_33_seneschal", "{!}Town 33 Seneschal", "{!}Town 33 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["town_34_seneschal", "{!}Town 34 Seneschal", "{!}Town 34 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["town_35_seneschal", "{!}Town 35 Seneschal", "{!}Town 35 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["town_36_seneschal", "{!}Town 36 Seneschal", "{!}Town 36 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_37_seneschal", "{!}Town 37 Seneschal", "{!}Town 37 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
  ["town_38_seneschal", "{!}Town 38 Seneschal", "{!}Town 38 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000000004728b01c293c694944b05],
## TGS: mat: End

  ["castle_1_seneschal", "{!}Castle 1 Seneschal", "{!}Castle 1 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["castle_2_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_3_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_4_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_5_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_6_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_7_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_8_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_9_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_10_seneschal", "{!}Castle 10 Seneschal", "{!}Castle 10 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_11_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_12_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_13_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_14_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_15_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_16_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_17_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_18_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_19_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_20_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_21_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_22_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_23_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_24_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_25_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_26_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_27_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_28_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_29_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_30_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_31_seneschal", "{!}Castle 11 Seneschal", "{!}Castle 11 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_32_seneschal", "{!}Castle 2 Seneschal", "{!}Castle 2 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_33_seneschal", "{!}Castle 3 Seneschal", "{!}Castle 3 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_34_seneschal", "{!}Castle 4 Seneschal", "{!}Castle 4 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_35_seneschal", "{!}Castle 5 Seneschal", "{!}Castle 5 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_36_seneschal", "{!}Castle 6 Seneschal", "{!}Castle 6 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_37_seneschal", "{!}Castle 7 Seneschal", "{!}Castle 7 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_38_seneschal", "{!}Castle 8 Seneschal", "{!}Castle 8 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_39_seneschal", "{!}Castle 9 Seneschal", "{!}Castle 9 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_40_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_41_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_42_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_43_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_44_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_45_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_46_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_47_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_48_seneschal", "{!}Castle 20 Seneschal", "{!}Castle 20 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
## TGS: mat: Added for new Castles
  ["castle_49_seneschal", "{!}Castle 49 Seneschal", "{!}Castle 49 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x000000000010360b01cef8b57553d34e],
  ["castle_50_seneschal", "{!}Castle 50 Seneschal", "{!}Castle 50 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_51_seneschal", "{!}Castle 51 Seneschal", "{!}Castle 51 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_52_seneschal", "{!}Castle 52 Seneschal", "{!}Castle 52 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_53_seneschal", "{!}Castle 53 Seneschal", "{!}Castle 53 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_54_seneschal", "{!}Castle 54 Seneschal", "{!}Castle 54 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_55_seneschal", "{!}Castle 55 Seneschal", "{!}Castle 55 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_56_seneschal", "{!}Castle 56 Seneschal", "{!}Castle 56 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_57_seneschal", "{!}Castle 57 Seneschal", "{!}Castle 57 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_58_seneschal", "{!}Castle 58 Seneschal", "{!}Castle 58 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_59_seneschal", "{!}Castle 59 Seneschal", "{!}Castle 59 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_60_seneschal", "{!}Castle 60 Seneschal", "{!}Castle 60 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_nomad_armor,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000008061301fb89acfb95332f],
  ["castle_61_seneschal", "{!}Castle 61 Seneschal", "{!}Castle 61 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008548e01d952a9b25d6d5a],
  ["castle_62_seneschal", "{!}Castle 62 Seneschal", "{!}Castle 62 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_linen_tunic,           itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000004715201ea236c60a2bcae],
  ["castle_63_seneschal", "{!}Castle 63 Seneschal", "{!}Castle 63 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jerkin,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c500e01dbb2115a55f3cd],
  ["castle_64_seneschal", "{!}Castle 64 Seneschal", "{!}Castle 64 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_coarse_tunic,          itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000000000c03cc01cc34a9a467fdfd],
  ["castle_65_seneschal", "{!}Castle 65 Seneschal", "{!}Castle 65 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_blue_gambeson,         itm_blue_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000c13ce01dc4723ab936c82],
  ["castle_66_seneschal", "{!}Castle 66 Seneschal", "{!}Castle 66 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,        itm_hide_boots],    def_attrib|level(2),wp(20),knows_common, 0x00000000000c218501ef4f5d2ccb0026],
  ["castle_67_seneschal", "{!}Castle 67 Seneschal", "{!}Castle 67 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_leather_jacket,        itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000000008035201e6eebaf3f3eb2b],
  ["castle_68_seneschal", "{!}Castle 68 Seneschal", "{!}Castle 68 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_69_seneschal", "{!}Castle 69 Seneschal", "{!}Castle 69 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
  ["castle_70_seneschal", "{!}Castle 70 Seneschal", "{!}Castle 70 Seneschal", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[itm_padded_leather,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000000000440c601e1cd45cfb38550],
## TGS: mat: End


#Arena Masters
  ["town_1_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_1_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_2_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_2_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_3_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_3_arena|entry(52),reserved,   fac_commoners,[itm_nomad_armor,       itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_4_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_4_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_5_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_5_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_6_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_6_arena|entry(52),reserved,   fac_commoners,[itm_leather_jerkin,    itm_leather_boots], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_7_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_7_arena|entry(52),reserved,   fac_commoners,[itm_padded_leather,    itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_8_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_8_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_9_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_9_arena|entry(52),reserved,   fac_commoners,[itm_padded_leather,    itm_leather_boots], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_10_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_10_arena|entry(52),reserved,  fac_commoners,[itm_nomad_armor,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_11_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_11_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_12_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_12_arena|entry(52),reserved,  fac_commoners,[itm_leather_jerkin,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_13_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_13_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic,      itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_14_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_14_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_15_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_15_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_16_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_16_arena|entry(52),reserved,  fac_commoners,[itm_fur_coat,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_17_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_17_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_18_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_18_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_19_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_19_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_20_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_20_arena|entry(52),reserved,  fac_commoners,[itm_fur_coat,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_21_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_21_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_22_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_22_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
## TGS: mat: Added for new Towns
  ["town_23_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_23_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_24_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_24_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_25_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_25_arena|entry(52),reserved,   fac_commoners,[itm_nomad_armor,       itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_26_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_26_arena|entry(52),reserved,   fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_27_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_27_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_28_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_28_arena|entry(52),reserved,   fac_commoners,[itm_leather_jerkin,    itm_leather_boots], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_29_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_29_arena|entry(52),reserved,   fac_commoners,[itm_padded_leather,    itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_30_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_30_arena|entry(52),reserved,   fac_commoners,[itm_linen_tunic,       itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_31_arena_master", "Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_31_arena|entry(52),reserved,   fac_commoners,[itm_padded_leather,    itm_leather_boots], def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_32_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_32_arena|entry(52),reserved,  fac_commoners,[itm_nomad_armor,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_33_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_33_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic,      itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_34_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_34_arena|entry(52),reserved,  fac_commoners,[itm_leather_jerkin,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_35_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_35_arena|entry(52),reserved,  fac_commoners,[itm_coarse_tunic,      itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_36_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_36_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_37_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_37_arena|entry(52),reserved,  fac_commoners,[itm_padded_leather,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
  ["town_38_arena_master","Tournament Master","{!}Tournament Master",tf_hero|tf_randomize_face, scn_town_38_arena|entry(52),reserved,  fac_commoners,[itm_fur_coat,    itm_hide_boots],    def_attrib|level(2),wp(20),knows_common,man_face_middle_1, man_face_older_2],
## TGS: mat: End


# Underground 

##  ["town_1_crook","Town 1 Crook","Town 1 Crook",tf_hero,                0,0, fac_neutral,[itm_linen_tunic,        itm_leather_boots       ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004428401f46e44a27144e3],
##  ["town_2_crook","Town 2 Crook","Town 2 Crook",tf_hero|tf_female,      0,0, fac_neutral,[itm_lady_dress_ruby,    itm_turret_hat_ruby     ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x000000000004300101c36db6db6db6db],
##  ["town_3_crook","Town 3 Crook","Town 3 Crook",tf_hero,                0,0, fac_neutral,[itm_leather_apron,      itm_hide_boots          ],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c530701f17944a25164e1],
##  ["town_4_crook","Town 4 Crook","Town 4 Crook",tf_hero,                0,0, fac_neutral,[itm_coarse_tunic,       itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c840501f36db6db7134db],
##  ["town_5_crook","Town 5 Crook","Town 5 Crook",tf_hero,                0,0, fac_neutral,[itm_red_gambeson,       itm_blue_hose           ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c000601f36db6db7134db],
##  ["town_6_crook","Town 6 Crook","Town 6 Crook",tf_hero,                0,0, fac_neutral,[itm_coarse_tunic,       itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c10c801db6db6dd7598aa],
##  ["town_7_crook","Town 7 Crook","Town 7 Crook",tf_hero|tf_female,      0,0, fac_neutral,[itm_woolen_dress,       itm_woolen_hood         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010214101de2f64db6db58d],
##  
##  ["town_8_crook","Town 8 Crook","Town 8 Crook",tf_hero,                0,0, fac_neutral,[itm_leather_jacket,     itm_leather_boots       ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000010318401c96db4db6db58d],
##  ["town_9_crook","Town 9 Crook","Town 9 Crook",tf_hero,                0,0, fac_neutral,[itm_linen_tunic,        itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008520501f16db4db6db58d],
##  ["town_10_crook","Town 10 Crook","Town 10 Crook",tf_hero,             0,0, fac_neutral,[itm_coarse_tunic,      itm_nomad_boots         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008600701f35144db6db8a2],
##  ["town_11_crook","Town 11 Crook","Town 11 Crook",tf_hero|tf_female,   0,0, fac_neutral,[itm_blue_dress,        itm_wimple_with_veil    ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x000000000008408101f386c4db4dd514],
##  ["town_12_crook","Town 12 Crook","Town 12 Crook",tf_hero,             0,0, fac_neutral,[itm_coarse_tunic,      itm_hide_boots          ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000870c501f386c4f34dbaa1],
##  ["town_13_crook","Town 13 Crook","Town 13 Crook",tf_hero,             0,0, fac_neutral,[itm_blue_gambeson,     itm_nomad_boots         ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000000c114901f245caf34dbaa1],
##  ["town_14_crook","Town 14 Crook","Town 14 Crook",tf_hero|tf_female,   0,0, fac_neutral,[itm_woolen_dress,      itm_turret_hat_ruby     ],def_attrib|level(5),wp(20),knows_inventory_management_10, 0x00000000001021c001f545a49b6eb2bc],

# Armor Merchants
  #arena_masters_end = zendar_armorer

  ["town_1_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,           itm_leather_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_2_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,          itm_straw_hat       ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_3_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_red,        itm_hide_boots      ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_4_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_red_gambeson,         itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_5_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_6_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_7_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,       itm_blue_hose       ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_8_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_leather,       itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_9_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_10_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_11_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_12_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_red_gambeson,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_13_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_14_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,         itm_headcloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_15_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_16_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_17_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_18_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,         itm_headcloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_19_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_20_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_21_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_22_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_sarranid_common_dress,         itm_sarranid_head_cloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
## TGS: mat: Added for new Towns
  ["town_23_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,           itm_leather_boots   ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_24_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,          itm_straw_hat       ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_25_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_red,        itm_hide_boots      ],def_attrib|level(2),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_26_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_red_gambeson,         itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_27_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_28_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,       itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_29_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,       itm_blue_hose       ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_30_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_padded_leather,       itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_31_armorer","Armorer",  "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_32_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_33_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_34_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_red_gambeson,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_35_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,       itm_hide_boots      ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_36_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,         itm_headcloth       ],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_37_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_blue_gambeson,        itm_leather_boots   ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_38_armorer","Armorer", "{!}Armorer",  tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,         itm_nomad_boots     ],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
## TGS: mat: End

# Weapon merchants

  ["town_1_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots,itm_straw_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_2_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,     itm_nomad_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_3_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,   itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_4_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,            itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_5_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,   itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_6_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_7_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,            itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_8_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,     itm_wrapping_boots,itm_straw_hat],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_9_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,   itm_leather_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_10_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_11_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_woolen_hose],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_12_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_13_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_red,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_14_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_blue,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_15_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_woolen_hose],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_16_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_17_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_green,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_18_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_19_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_20_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_21_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_green,     itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_22_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_sarranid_boots_a],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
## TGS: mat: Added for new Towns
  ["town_23_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots,itm_straw_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_24_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,     itm_nomad_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_25_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_fur_coat,   itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_26_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,            itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_27_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,   itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_28_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,      itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_29_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,            itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_30_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|tf_female|tf_is_merchant, 0, 0, fac_commoners,[itm_woolen_dress,     itm_wrapping_boots,itm_straw_hat],def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_31_weaponsmith", "Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jerkin,   itm_leather_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_32_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_linen_tunic,     itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_33_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_woolen_hose],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_34_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_35_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_red,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_36_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_arena_tunic_blue,     itm_wrapping_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_37_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_leather_jacket,  itm_woolen_hose],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
  ["town_38_weaponsmith","Weaponsmith","{!}Weaponsmith",tf_hero|tf_randomize_face|          tf_is_merchant, 0, 0, fac_commoners,[itm_shirt,           itm_hide_boots],def_attrib|level(5),wp(20),knows_inventory_management_10, mercenary_face_1, mercenary_face_2],
## TGS: mat: End

#Tavern keepers

  ["town_1_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_1_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_2_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_2_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_3_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_3_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_4_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_4_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_5_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_5_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_6_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_6_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_7_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_7_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_leather_boots,      itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_8_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_8_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,      itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_9_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_9_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_10_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_10_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_11_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_11_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_12_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_12_tavern|entry(9),0,  fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_13_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_13_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_14_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_14_tavern|entry(9),0,  fac_commoners,[itm_shirt,               itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_15_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_15_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_16_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_16_tavern|entry(9),0,  fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_17_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_17_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_18_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_18_tavern|entry(9),0,  fac_commoners,[itm_shirt,               itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_19_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_19_tavern|entry(9),0,  fac_commoners,[itm_sarranid_dress_a,        itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_20_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_20_tavern|entry(9),0,  fac_commoners,[itm_sarranid_cloth_robe,       itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_21_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_21_tavern|entry(9),0,  fac_commoners,[itm_sarranid_common_dress,        itm_sarranid_boots_a,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_22_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_22_tavern|entry(9),0,  fac_commoners,[itm_sarranid_cloth_robe_b,               itm_sarranid_boots_a],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
## TGS: mat: Added for new Towns
  ["town_23_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_23_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_wrapping_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_24_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_24_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_25_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_25_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_26_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_26_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_27_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_27_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_28_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_28_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_29_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_29_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_leather_boots,      itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_30_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_30_tavern|entry(9),0,   fac_commoners,[itm_leather_apron,      itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_31_tavernkeeper", "Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_31_tavern|entry(9),0,   fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_32_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_32_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_33_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_33_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_34_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_34_tavern|entry(9),0,  fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_35_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_35_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_hide_boots,     itm_headcloth],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_36_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_36_tavern|entry(9),0,  fac_commoners,[itm_shirt,               itm_leather_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
  ["town_37_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face|tf_female, scn_town_37_tavern|entry(9),0,  fac_commoners,[itm_woolen_dress,        itm_nomad_boots],def_attrib|level(2),wp(20),knows_common, woman_face_1, woman_face_2],
  ["town_38_tavernkeeper","Tavern_Keeper","{!}Tavern_Keeper",tf_hero|tf_randomize_face,           scn_town_38_tavern|entry(9),0,  fac_commoners,[itm_leather_apron,       itm_hide_boots],def_attrib|level(2),wp(20),knows_common, mercenary_face_1, mercenary_face_2],
## TGS: mat: End

#Goods Merchants

  ["town_1_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_1_store|entry(9),0, fac_commoners,     [itm_coarse_tunic,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_2_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_2_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_3_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_3_store|entry(9),0, fac_commoners,     [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_4_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_4_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_5_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_5_store|entry(9),0, fac_commoners,     [itm_nomad_armor,   itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_6_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_6_store|entry(9),0, fac_commoners,     [itm_woolen_dress,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_7_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_7_store|entry(9),0, fac_commoners,     [itm_leather_jerkin,itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_8_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_8_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_9_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_9_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_10_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_10_store|entry(9),0, fac_commoners,    [itm_leather_jerkin,itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_11_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_11_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_12_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_12_store|entry(9),0, fac_commoners,    [itm_woolen_dress,  itm_leather_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_13_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_13_store|entry(9),0, fac_commoners,    [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_14_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_14_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_15_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_15_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_16_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_16_store|entry(9),0, fac_commoners,    [itm_woolen_dress,  itm_leather_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_17_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_17_store|entry(9),0, fac_commoners,    [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_18_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_18_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_19_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_19_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_20_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_20_store|entry(9),0, fac_commoners,    [itm_sarranid_common_dress_b,  itm_sarranid_boots_a, itm_sarranid_felt_head_cloth_b  ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_21_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_21_store|entry(9),0, fac_commoners,    [itm_sarranid_dress_a,         itm_sarranid_boots_a,  itm_sarranid_felt_head_cloth  ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_22_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_22_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
## TGS: mat: Added for new Towns
  ["town_23_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_23_store|entry(9),0, fac_commoners,     [itm_coarse_tunic,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_24_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_24_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_25_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_25_store|entry(9),0, fac_commoners,     [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_26_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_26_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_27_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_27_store|entry(9),0, fac_commoners,     [itm_nomad_armor,   itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_28_merchant", "Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_28_store|entry(9),0, fac_commoners,     [itm_woolen_dress,  itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_29_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_29_store|entry(9),0, fac_commoners,     [itm_leather_jerkin,itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_30_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_30_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_31_merchant", "Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_31_store|entry(9),0, fac_commoners,     [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_32_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_32_store|entry(9),0, fac_commoners,    [itm_leather_jerkin,itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_33_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_33_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_34_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_34_store|entry(9),0, fac_commoners,    [itm_woolen_dress,  itm_leather_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_35_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_35_store|entry(9),0, fac_commoners,    [itm_dress,         itm_leather_boots,  itm_straw_hat   ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_36_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_36_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_37_merchant","Merchant","{!}Merchant",          tf_hero|tf_randomize_face|tf_is_merchant, scn_town_37_store|entry(9),0, fac_commoners,    [itm_leather_apron, itm_leather_boots                   ],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_38_merchant","Merchant","{!}Merchant",tf_female|tf_hero|tf_randomize_face|tf_is_merchant, scn_town_38_store|entry(9),0, fac_commoners,    [itm_woolen_dress,  itm_leather_boots,  itm_female_hood ],def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
## TGS: mat: End

  ["salt_mine_merchant","Barezan","Barezan",                tf_hero|tf_is_merchant, scn_salt_mine|entry(1),0, fac_commoners,        [itm_leather_apron, itm_leather_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, 0x00000000000c528601ea69b6e46dbdb6],

# Horse Merchants

  ["town_1_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_blue_dress,           itm_blue_hose,      itm_female_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_2_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_3_horse_merchant","Horse Merchant","{!}Town 3 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_nomad_armor,          itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_4_horse_merchant","Horse Merchant","{!}Town 4 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_jerkin,       itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_5_horse_merchant","Horse Merchant","{!}Town 5 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_dress,                itm_woolen_hose,    itm_woolen_hood],   def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_6_horse_merchant","Horse Merchant","{!}Town 6 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_7_horse_merchant","Horse Merchant","{!}Town 7 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_8_horse_merchant","Horse Merchant","{!}Town 8 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_9_horse_merchant","Horse Merchant","{!}Town 9 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_jerkin,       itm_woolen_hose],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_10_horse_merchant","Horse Merchant","{!}Town 10 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_blue_dress,          itm_blue_hose,      itm_straw_hat],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_11_horse_merchant","Horse Merchant","{!}Town 11 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_12_horse_merchant","Horse Merchant","{!}Town 12 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket,      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_13_horse_merchant","Horse Merchant","{!}Town 13 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,        itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_14_horse_merchant","Horse Merchant","{!}Town 14 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_peasant_dress,       itm_blue_hose,      itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_15_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_16_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket,      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_17_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,        itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_18_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_peasant_dress,       itm_blue_hose,      itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_19_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_sarranid_boots_a],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_20_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_sarranid_cloth_robe,      itm_sarranid_boots_a],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_21_horse_merchant","Horse Merchant","{!}Town 17 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_sarranid_cloth_robe_b,        itm_sarranid_boots_a],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_22_horse_merchant","Horse Merchant","{!}Town 18 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_sarranid_common_dress_b,       itm_blue_hose,      itm_sarranid_felt_head_cloth_b],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
## TGS: mat: Added for new Towns
  ["town_23_horse_merchant","Horse Merchant","{!}Town 1 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_blue_dress,           itm_blue_hose,      itm_female_hood],   def_attrib|level(2),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_24_horse_merchant","Horse Merchant","{!}Town 2 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_linen_tunic,          itm_nomad_boots,],                      def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_25_horse_merchant","Horse Merchant","{!}Town 3 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_nomad_armor,          itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_26_horse_merchant","Horse Merchant","{!}Town 4 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_jerkin,       itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_27_horse_merchant","Horse Merchant","{!}Town 5 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,    0, 0, fac_commoners,[itm_dress,                itm_woolen_hose,    itm_woolen_hood],   def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_28_horse_merchant","Horse Merchant","{!}Town 6 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_29_horse_merchant","Horse Merchant","{!}Town 7 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_30_horse_merchant","Horse Merchant","{!}Town 8 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_coarse_tunic,         itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_31_horse_merchant","Horse Merchant","{!}Town 9 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,              0, 0, fac_commoners,[itm_leather_jerkin,       itm_woolen_hose],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_32_horse_merchant","Horse Merchant","{!}Town 10 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_blue_dress,          itm_blue_hose,      itm_straw_hat],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_33_horse_merchant","Horse Merchant","{!}Town 11 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_34_horse_merchant","Horse Merchant","{!}Town 12 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket,      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_35_horse_merchant","Horse Merchant","{!}Town 13 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_coarse_tunic,        itm_nomad_boots],                       def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_36_horse_merchant","Horse Merchant","{!}Town 14 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant|tf_female,  0, 0, fac_commoners,[itm_peasant_dress,       itm_blue_hose,      itm_headcloth],     def_attrib|level(5),wp(20),knows_inventory_management_10, woman_face_1, woman_face_2],
  ["town_37_horse_merchant","Horse Merchant","{!}Town 15 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_nomad_armor,         itm_leather_boots],                     def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
  ["town_38_horse_merchant","Horse Merchant","{!}Town 16 Horse Merchant",tf_hero|tf_randomize_face|tf_is_merchant,            0, 0, fac_commoners,[itm_leather_jacket,      itm_hide_boots],                        def_attrib|level(5),wp(20),knows_inventory_management_10, man_face_young_1, man_face_older_2],
## TGS: mat: End

#Town Mayors    #itm_courtly_outfit itm_gambeson itm_blue_gambeson itm_red_gambeson itm_nobleman_outfit itm_rich_outfit
  ["town_1_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["town_2_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_gambeson,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_3_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_blue_gambeson,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_4_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_fur_coat,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_5_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_nobleman_outfit,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_6_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_7_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_rich_outfit,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_8_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_9_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_10_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_11_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_12_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_red_gambeson,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_13_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_nobleman_outfit,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_14_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_15_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_16_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_fur_coat,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_17_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_nobleman_outfit,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_18_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_19_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,     itm_sarranid_boots_a],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_20_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,       itm_sarranid_boots_a], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_21_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,    itm_sarranid_boots_a],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_22_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_sarranid_boots_a],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
## TGS: mat: Added for new Towns
  ["town_23_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, man_face_middle_1, mercenary_face_2],
  ["town_24_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_gambeson,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_25_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_blue_gambeson,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_26_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_fur_coat,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_27_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_nobleman_outfit,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_28_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_29_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_rich_outfit,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_30_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_red_gambeson,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_31_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[     itm_courtly_outfit,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_32_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_33_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_34_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_red_gambeson,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_35_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_nobleman_outfit,    itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_36_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_blue_gambeson,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_37_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_leather_jacket,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
  ["town_38_mayor", "Guild_Master", "{!}Guild_Master", tf_hero|tf_randomize_face, 0,reserved,  fac_neutral,[ itm_fur_coat,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common,  man_face_middle_1, mercenary_face_2],
## TGS: mat: End

#Village stores
  ["village_1_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_2_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_3_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_4_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_5_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_6_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_7_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_8_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_9_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,         man_face_old_1, man_face_older_2],
  ["village_10_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_11_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_12_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_13_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_14_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_15_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_16_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_17_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_18_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_19_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots, itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_20_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_21_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_22_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_23_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_24_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_25_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_26_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_27_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_28_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_29_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_30_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_31_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_32_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_33_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_34_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_35_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_36_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_37_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_38_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_39_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_40_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_41_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_42_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_43_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_44_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_45_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_46_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_47_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_48_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_49_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_50_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_51_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_52_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_53_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_54_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_55_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_56_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_57_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_58_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_59_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_60_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_61_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_62_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_63_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_64_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_65_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_66_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_67_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_68_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_69_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_70_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_71_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_72_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_73_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_74_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_75_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_76_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_77_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_78_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_79_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_80_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_81_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_82_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_83_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_84_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_85_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_86_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_87_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_88_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_89_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_90_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_91_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_92_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_93_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_94_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_95_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_96_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_97_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_98_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_99_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_100_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_101_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_102_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_103_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_104_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_105_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_106_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_107_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_108_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_109_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_sarranid_cloth_robe_b, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_110_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
## TGS: mat: Added for new Villages
  ["village_111_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_112_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_113_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_114_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_115_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_116_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_117_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_118_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_119_elder", "Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,         man_face_old_1, man_face_older_2],
  ["village_120_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_121_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_122_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_123_eder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_124_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_125_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_126_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_127_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_128_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_129_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots, itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_130_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_leather_warrior_cap],def_attrib|level(2),wp(20),knows_inventory_management_10, man_face_old_1, man_face_older_2],
  ["village_131_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_132_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_133_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,            man_face_old_1, man_face_older_2],
  ["village_134_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_135_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_fur_coat, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                      man_face_old_1, man_face_older_2],
  ["village_136_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_137_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_wrapping_boots, itm_felt_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,        man_face_old_1, man_face_older_2],
  ["village_138_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_139_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_140_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_141_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_142_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_143_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots, itm_leather_cap],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_144_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots,itm_fur_hat],def_attrib|level(2),wp(20),knows_inventory_management_10,             man_face_old_1, man_face_older_2],
  ["village_145_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_146_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_147_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_148_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_hide_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                          man_face_old_1, man_face_older_2],
  ["village_149_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
  ["village_150_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_robe, itm_wrapping_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                              man_face_old_1, man_face_older_2],
  ["village_151_elder","Village_Elder", "{!}village_1_elder",tf_hero|tf_randomize_face|tf_is_merchant, 0,0, fac_commoners,[itm_coarse_tunic, itm_nomad_boots],def_attrib|level(2),wp(20),knows_inventory_management_10,                         man_face_old_1, man_face_older_2],
## TGS: mat: End

# Place extra merchants before this point
  ["merchants_end","merchants_end","merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],

  #Used for player enterprises
## Corrected for TGS
  ["town_1_master_craftsman", "{!}Town 1 Craftsman", "{!}Town 1 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_2_master_craftsman", "{!}Town 2 Craftsman", "{!}Town 2 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x0000000f010811c92d3295e46a96c72300000000001f5a980000000000000000],
  ["town_3_master_craftsman", "{!}Town 3 Craftsman", "{!}Town 3 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000001b083203151d2ad5648e52b400000000001b172e0000000000000000],
  ["town_4_master_craftsman", "{!}Town 4 Craftsman", "{!}Town 4 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000001a10114f091b2c259cd4c92300000000000228dd0000000000000000],
  ["town_5_master_craftsman", "{!}Town 5 Craftsman", "{!}Town 5 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000d1044c578598cd92b5256db00000000001f23340000000000000000],
  ["town_6_master_craftsman", "{!}Town 6 Craftsman", "{!}Town 6 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000001f046285493eaf1b048abcdb00000000001a8aad0000000000000000],
  ["town_7_master_craftsman", "{!}Town 7 Craftsman", "{!}Town 7 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000002b0052c34c549225619356d400000000001cc6e60000000000000000],
  ["town_8_master_craftsman", "{!}Town 8 Craftsman", "{!}Town 8 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x0000000fdb0c20465b6e51e8a12c82d400000000001e148c0000000000000000],
  ["town_9_master_craftsman", "{!}Town 9 Craftsman", "{!}Town 9 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009f7005246071db236e296a45300000000001a8b0a0000000000000000],
  ["town_10_master_craftsman", "{!}Town 10 Craftsman", "{!}Town 10 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000009f71012c2456a921aa379321a000000000012c6d90000000000000000],
  ["town_11_master_craftsman", "{!}Town 11 Craftsman", "{!}Town 11 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000009f308514428db71b9ad70b72400000000001dc9140000000000000000],
  ["town_12_master_craftsman", "{!}Town 12 Craftsman", "{!}Town 12 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009e90825863853a5b91cd71a5b00000000000598db0000000000000000],
  ["town_13_master_craftsman", "{!}Town 13 Craftsman", "{!}Town 13 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000009fa0c708f274c8eb4c64e271300000000001eb69a0000000000000000],
  ["town_14_master_craftsman", "{!}Town 14 Craftsman", "{!}Town 14 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007590c3206155c8b475a4e439a00000000001f489a0000000000000000],
  ["town_15_master_craftsman", "{!}Town 15 Craftsman", "{!}Town 14 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007440022d04b2c6cb7d3723d5a00000000001dc90a0000000000000000],
  ["town_16_master_craftsman", "{!}Town 16 Craftsman", "{!}Town 14 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007680c3586054b8e372e4db65c00000000001db7230000000000000000],
  ["town_17_master_craftsman", "{!}Town 17 Craftsman", "{!}Town 14 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x0000000766046186591b564cec85d2e200000000001e4cea0000000000000000],
  ["town_18_master_craftsman", "{!}Town 18 Craftsman", "{!}Town 14 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x0000000e7e0075523a6aa9b6da61e8dd00000000001d96d30000000000000000],
  ["town_19_master_craftsman", "{!}Town 19 Craftsman", "{!}Town 14 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000002408314852a432e88aaa42e100000000001e284e0000000000000000],
  ["town_20_master_craftsman", "{!}Town 20 Craftsman", "{!}Town 14 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe_b,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000001104449136e44cbd1c9352bc000000000005e8d10000000000000000],
  ["town_21_master_craftsman", "{!}Town 21 Craftsman", "{!}Town 14 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000000131032d3351c6e43226ec96c000000000005b5240000000000000000],
  ["town_22_master_craftsman", "{!}Town 22 Craftsman", "{!}Town 14 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_sarranid_cloth_robe_b,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000000200c658a5723b1a3148dc455000000000015ab920000000000000000],
## End
## TGS: mat: Added for new Towns
  ["town_23_master_craftsman", "{!}Town 23 Craftsman", "{!}Town 23 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000003a0c629346edb2335a82b6e300000000000d634a0000000000000000],
  ["town_24_master_craftsman", "{!}Town 24 Craftsman", "{!}Town 24 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_padded_leather,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x0000000f010811c92d3295e46a96c72300000000001f5a980000000000000000],
  ["town_25_master_craftsman", "{!}Town 25 Craftsman", "{!}Town 25 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x000000001b083203151d2ad5648e52b400000000001b172e0000000000000000],
  ["town_26_master_craftsman", "{!}Town 26 Craftsman", "{!}Town 26 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x000000001a10114f091b2c259cd4c92300000000000228dd0000000000000000],
  ["town_27_master_craftsman", "{!}Town 27 Craftsman", "{!}Town 27 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000000d1044c578598cd92b5256db00000000001f23340000000000000000],
  ["town_28_master_craftsman", "{!}Town 28 Craftsman", "{!}Town 28 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x000000001f046285493eaf1b048abcdb00000000001a8aad0000000000000000],
  ["town_29_master_craftsman", "{!}Town 29 Craftsman", "{!}Town 29 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x000000002b0052c34c549225619356d400000000001cc6e60000000000000000],
  ["town_30_master_craftsman", "{!}Town 30 Craftsman", "{!}Town 30 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_leather_apron,       itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x0000000fdb0c20465b6e51e8a12c82d400000000001e148c0000000000000000],
  ["town_31_master_craftsman", "{!}Town 31 Craftsman", "{!}Town 31 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[     itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009f7005246071db236e296a45300000000001a8b0a0000000000000000],
  ["town_32_master_craftsman", "{!}Town 32 Craftsman", "{!}Town 32 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000009f71012c2456a921aa379321a000000000012c6d90000000000000000],
  ["town_33_master_craftsman", "{!}Town 33 Craftsman", "{!}Town 33 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,     itm_nomad_boots],   def_attrib|level(2),wp(20),knows_common, 0x00000009f308514428db71b9ad70b72400000000001dc9140000000000000000],
  ["town_34_master_craftsman", "{!}Town 34 Seneschal", "{!}Town 34 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_coarse_tunic,       itm_leather_boots], def_attrib|level(2),wp(20),knows_common, 0x00000009e90825863853a5b91cd71a5b00000000000598db0000000000000000],
  ["town_35_master_craftsman", "{!}Town 35 Seneschal", "{!}Town 35 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_jerkin,     itm_woolen_hose],   def_attrib|level(2),wp(20),knows_common, 0x00000009fa0c708f274c8eb4c64e271300000000001eb69a0000000000000000],
  ["town_36_master_craftsman", "{!}Town 36 Seneschal", "{!}Town 36 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007590c3206155c8b475a4e439a00000000001f489a0000000000000000],
  ["town_37_master_craftsman", "{!}Town 37 Seneschal", "{!}Town 37 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007440022d04b2c6cb7d3723d5a00000000001dc90a0000000000000000],
  ["town_38_master_craftsman", "{!}Town 38 Seneschal", "{!}Town 38 Craftsman", tf_hero|tf_is_merchant, 0,reserved,  fac_neutral,[ itm_leather_apron,      itm_blue_hose],     def_attrib|level(2),wp(20),knows_common, 0x00000007680c3586054b8e372e4db65c00000000001db7230000000000000000],
## TGS: mat: End
  
  
# Chests
  ["zendar_chest","{!}Zendar Chest","{!}Zendar Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,
   [],def_attrib|level(18),wp(60),knows_common, 0],
  ["tutorial_chest_1","{!}Melee Weapons Chest","{!}Melee Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_sword, itm_tutorial_axe, itm_tutorial_spear, itm_tutorial_club, itm_tutorial_battle_axe],def_attrib|level(18),wp(60),knows_common, 0],
  ["tutorial_chest_2","{!}Ranged Weapons Chest","{!}Ranged Weapons Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_tutorial_short_bow, itm_tutorial_arrows, itm_tutorial_crossbow, itm_tutorial_bolts, itm_tutorial_throwing_daggers],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_1","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_strange_armor,itm_strange_short_sword],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_2","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_strange_boots,itm_strange_sword],def_attrib|level(18),wp(60),knows_common, 0],
  ["bonus_chest_3","{!}Bonus Chest","{!}Bonus Chest",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[itm_strange_helmet,itm_strange_great_sword],def_attrib|level(18),wp(60),knows_common, 0],

  ["household_possessions","{!}household_possessions","{!}household_possessions",tf_hero|tf_inactive|tf_is_merchant, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_inventory_management_10, 0],  
  
# These are used as arrays in the scripts.
  ["temp_array_a","{!}temp_array_a","{!}temp_array_a",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_b","{!}temp_array_b","{!}temp_array_b",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],
  ["temp_array_c","{!}temp_array_c","{!}temp_array_c",tf_hero|tf_inactive, 0,reserved,  fac_neutral,[],def_attrib|level(18),wp(60),knows_common, 0],

  ["stack_selection_amounts","{!}stack_selection_amounts","{!}stack_selection_amounts",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["stack_selection_ids","{!}stack_selection_ids","{!}stack_selection_ids",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["notification_menu_types","{!}notification_menu_types","{!}notification_menu_types",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["notification_menu_var1","{!}notification_menu_var1","{!}notification_menu_var1",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],
  ["notification_menu_var2","{!}notification_menu_var2","{!}notification_menu_var2",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["banner_background_color_array","{!}banner_background_color_array","{!}banner_background_color_array",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

  ["multiplayer_data","{!}multiplayer_data","{!}multiplayer_data",tf_hero|tf_inactive,0,reserved,fac_neutral,[],def_attrib,0,knows_common,0],

##  ["black_khergit_guard","Black Khergit Guard","Black Khergit Guard",tf_mounted|tf_guarantee_ranged|tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_helmet|tf_guarantee_armor|tf_guarantee_horse,0,0,fac_black_khergits,
##   [itm_arrows,itm_nomad_sabre,itm_scimitar,itm_winged_mace,itm_lance,itm_khergit_bow,itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_guard_boots,itm_khergit_guard_armor,itm_nomad_shield,itm_steppe_horse,itm_warhorse],
##   def_attrib|level(28),wp(140),knows_riding_6|knows_ironflesh_4|knows_horse_archery_6|knows_power_draw_6,khergit_face1, khergit_face2],


# Add Extra Quest NPCs below this point  

  ["local_merchant","Local Merchant","Local Merchants",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["tax_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
  ["trainee_peasant","Peasant","Peasants",tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
  ["fugitive","Nervous Man","Nervous Men",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_medieval_b, itm_throwing_daggers],
   def_attrib|str_24|agi_25|level(26),wp(180),knows_common|knows_power_throw_6|knows_power_strike_6|knows_ironflesh_9,man_face_middle_1, man_face_old_2],
   
  ["belligerent_drunk","Belligerent Drunk","Belligerent Drunks",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   def_attrib|str_20|agi_8|level(15),wp(120),knows_common|knows_power_strike_2|knows_ironflesh_9,    bandit_face1, bandit_face2],

  ["hired_assassin","Hired Assassin","Hired Assassin",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners, #they look like belligerent drunks
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   def_attrib|str_20|agi_16|level(20),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_3,    bandit_face1, bandit_face2],

  ["fight_promoter","Rough-Looking Character","Rough-Looking Character",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_commoners,
   [itm_short_tunic,itm_linen_tunic,itm_coarse_tunic, itm_tabard, itm_leather_vest, itm_woolen_hose, itm_nomad_boots, itm_blue_hose, itm_wrapping_boots, itm_fur_hat, itm_leather_cap, itm_sword_viking_1],
   def_attrib|str_20|agi_16|level(20),wp(180),knows_common|knows_power_strike_5|knows_ironflesh_3,    bandit_face1, bandit_face2],

   
   
  ["spy","Ordinary Townsman","Ordinary Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
   [itm_sword_viking_1,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves],
   def_attrib|agi_11|level(20),wp(130),knows_common,man_face_middle_1, man_face_older_2],
   
  ["spy_partner","Unremarkable Townsman","Unremarkable Townsmen", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
   [itm_sword_medieval_b,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves],
   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],

   ["nurse_for_lady","Nurse","Nurse",tf_female|tf_guarantee_armor,0,reserved,fac_commoners,
   [itm_robe, itm_black_hood, itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,woman_face_1, woman_face_2],   
   ["temporary_minister","Minister","Minister",tf_guarantee_armor|tf_guarantee_boots,0,reserved,fac_commoners,
   [itm_rich_outfit, itm_wrapping_boots],
   def_attrib|level(4),wp(60),knows_common,man_face_middle_1, man_face_older_2],   
   
   
##  ["conspirator","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [itm_sword,itm_leather_jerkin,itm_leather_boots,itm_hunter,itm_leather_gloves],
##   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],
##  ["conspirator_leader","Conspirator","Conspirators", tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse,0,0,fac_neutral,
##   [itm_sword,itm_leather_jerkin,itm_leather_boots,itm_hunter,itm_leather_gloves],
##   def_attrib|agi_11|level(10),wp(130),knows_common,vaegir_face1, vaegir_face2],
##  ["peasant_rebel","Peasant Rebel","Peasant Rebels",tf_guarantee_armor,0,reserved,fac_peasant_rebels,
##   [itm_cleaver,itm_knife,itm_pitch_fork,itm_sickle,itm_club,itm_stones,itm_leather_cap,itm_felt_hat,itm_felt_hat,itm_linen_tunic,itm_coarse_tunic,itm_nomad_boots,itm_wrapping_boots],
##   def_attrib|level(4),wp(60),knows_common,vaegir_face1, vaegir_face2],
##  ["noble_refugee","Noble Refugee","Noble Refugees",tf_guarantee_boots|tf_guarantee_armor,0,0,fac_noble_refugees,
##   [itm_sword,itm_leather_jacket,itm_hide_boots, itm_saddle_horse, itm_leather_jacket, itm_leather_cap],
##   def_attrib|level(9),wp(100),knows_common,swadian_face1, swadian_face2],
##  ["noble_refugee_woman","Noble Refugee Woman","Noble Refugee Women",tf_female|tf_guarantee_armor|tf_guarantee_boots,0,0,fac_noble_refugees,
##   [itm_knife,itm_dagger,itm_hunting_crossbow,itm_dress,itm_robe,itm_woolen_dress, itm_headcloth, itm_woolen_hood, itm_wrapping_boots],
##   def_attrib|level(3),wp(45),knows_common,refugee_face1,refugee_face2],


  ["quick_battle_6_player", "{!}quick_battle_6_player", "{!}quick_battle_6_player", tf_hero, 0, reserved,  fac_player_faction, [itm_padded_cloth,itm_nomad_boots, itm_splinted_leather_greaves, itm_skullcap, itm_sword_medieval_b,  itm_crossbow, itm_bolts, itm_plate_covered_round_shield],    knight_attrib_1,wp(130),knight_skills_1, 0x000000000008010b01f041a9249f65fd],

#Multiplayer ai troops (modified for TGS)
#  ["swadian_crossbowman_multiplayer_ai","Swadian Crossbowman","Swadian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
#   [itm_bolts,itm_crossbow,itm_sword_medieval_a,itm_tab_shield_heater_b,
#    itm_leather_jerkin,itm_leather_armor,itm_ankle_boots,itm_footman_helmet],
#   def_attrib|level(19),wp_melee(90)|wp_crossbow(100),knows_common|knows_ironflesh_4|knows_athletics_6|knows_shield_5|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
    ["swadian_crossbowman_multiplayer_ai","Ashaman Soldier","Ashaman Soldiers",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_power_player, itm_power_ammo, itm_sword_secondary, itm_ashaman_soldier_coat, itm_black_leather_boots],
   def_attrib_wot_infantry_1,wp_firearm(105)|wp_one_handed(100)|wp(75),knows_wot_infantry_1|knows_power_draw_2,murandy_man_face_young, altara_man_face_older],
    ["ashaman_dedicated_multi","Ashaman Dedicated","Ashaman Dedicated",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_power_player, itm_power_ammo, itm_sword_secondary, itm_ashaman_dedicated_coat, itm_black_leather_boots],
   def_attrib_wot_infantry_2,wp_firearm(130)|wp_one_handed(110)|wp(80),knows_wot_infantry_2|knows_power_draw_3,ghealdan_man_face_younger, amadicia_man_face_older],
    ["ashaman_multi","Ashaman","Ashaman",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_power_player, itm_power_ammo, itm_ashaman_coat, itm_black_leather_boots, itm_saddle_horse],
   def_attrib_wot_infantry_2,wp_firearm(165)|wp_one_handed(110)|wp(90),knows_wot_infantry_2|knows_power_draw_4,tarabon_man_face_younger, arad_doman_man_face_older],
  ["ashaman_veteran_multi","Ashaman Veteran","Ashaman Veterans",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_power_player, itm_power_ammo, itm_ashaman_coat, itm_black_leather_boots, itm_saddle_horse],
   def_attrib_wot_infantry_3,wp_firearm(200)|wp_one_handed(150)|wp(125),knows_wot_infantry_3|knows_power_draw_5,man_face_young_1, man_face_old_2],
  
    ["legion_crossbowman_multi","Legion Crossbowman","Legion Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_crossbow, itm_bolts, itm_sword_secondary, itm_legion_army_tunic, itm_leather_boots, itm_leather_gloves, itm_skullcap],
   def_attrib_wot_infantry_2 ,wp_crossbow(100)|wp_one_handed(90)|wp(70),knows_wot_archer_2 ,man_face_young_1, man_face_old_2],
  ["legion_heavy_crossbowman_multi","Legion Heavy Crossbowman","Legion Heavy Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_heavy_crossbow, itm_steel_bolts, itm_sword_secondary, itm_legion_shield_normal, itm_legion_army_armor, itm_leather_boots, itm_leather_gloves, itm_nordic_helmet],
   def_attrib_wot_infantry_3 ,wp_crossbow(150)|wp_one_handed(110)|wp(85),knows_wot_archer_3 ,man_face_young_1, man_face_old_2],
  
    ["red_hand_crossbowman_multi","Red Hand Crossbowman","Red Hand Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_crossbow, itm_bolts, itm_sword_secondary, itm_red_hand_tunic, itm_leather_boots, itm_leather_gloves, itm_red_hand_bell_helm],
   def_attrib_wot_infantry_2 ,wp_crossbow(100)|wp_one_handed(90)|wp(70),knows_wot_archer_2 ,man_face_young_1, man_face_old_2],
  ["red_hand_fast_crossbowman_multi","Red Hand Fast Crossbowman","Red Hand Fast Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_red_hand_fast_crossbow, itm_steel_bolts, itm_steel_bolts, itm_sword_secondary, itm_red_hand_plate, itm_red_hand_greaves, itm_red_hand_plate_gauntlets, itm_red_hand_kettle_helm],
   def_attrib_wot_infantry_4 ,wp_crossbow(175)|wp_one_handed(150)|wp(85),knows_wot_archer_4 ,man_face_young_1, man_face_old_2],
  
    ["two_rivers_longbowman_multi","Two Rivers Longbowman","Two Rivers Longbowmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_long_bow, itm_arrows, itm_sword_secondary, itm_ragged_outfit, itm_leather_jerkin, itm_leather_boots, itm_leather_gloves, itm_leather_cap, itm_segmented_helmet],
   def_attrib_wot_infantry_4 ,wp_archery(125)|wp_one_handed(110)|wp(100),knows_wot_archer_4 ,andor_man_face_younger, andor_man_face_older],
  ["two_rivers_marksman_multi","Two Rivers Marksman","Two Rivers Marksmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_two_rivers_long_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_sword_secondary, itm_two_rivers_armor, itm_leather_boots, itm_leather_gloves, itm_segmented_helmet],
   def_attrib_wot_infantry_5 ,wp_archery(175)|wp_one_handed(145)|wp(125),knows_wot_archer_5 ,andor_man_face_younger, andor_man_face_older],

#  ["swadian_infantry_multiplayer_ai","Swadian Infantry","Swadian Infantry",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
#   [itm_pike,itm_bastard_sword_a,itm_tab_shield_heater_c,
#    itm_studded_leather_coat,itm_ankle_boots,itm_flat_topped_helmet],
#   def_attrib|level(19),wp_melee(105),knows_common|knows_ironflesh_5|knows_shield_4|knows_power_strike_5|knows_athletics_4,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_infantry_multiplayer_ai","Legion Footman","Legion Footmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_sword_medieval_b, itm_legion_shield_weak, itm_legion_army_tunic, itm_leather_boots, itm_leather_gloves, itm_skullcap],
   def_attrib_wot_infantry_2 ,wp_one_handed(90)|wp(70),knows_wot_infantry_2 ,man_face_young_1, man_face_old_2],
    ["legion_infantry_multi","Legion Infantry","Legion Infantry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_hammer, itm_legion_army_tunic, itm_legion_shield_normal, itm_leather_boots, itm_leather_gloves, itm_nordic_helmet],
   def_attrib_wot_infantry_2 ,wp_one_handed(110)|wp(75),knows_wot_infantry_2 ,man_face_young_1, man_face_old_2],
    ["legion_swordsman_multi","Legion Swordsman","Legion Swordsmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_sword_medieval_b, itm_legion_army_armor, itm_legion_shield_strong, itm_leather_boots, itm_leather_gloves, itm_nordic_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(125)|wp(80),knows_wot_infantry_3 ,man_face_young_1, man_face_old_2],
  ["legion_blademaster_multi","Legion Blademaster","Legion Blademasters",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_great_sword, itm_legion_plate, itm_shynbaulds_wot, itm_mail_gauntlets_wot, itm_andoran_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(180)|wp(100),knows_wot_infantry_4 ,man_face_young_1, man_face_old_2],
    ["legion_pikeman_multi","Legion Pikeman","Legion Pikemen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_pike, itm_legion_army_armor,itm_legion_shield_strong, itm_leather_boots, itm_leather_gloves, itm_nordic_helmet],
   def_attrib_wot_infantry_3 ,wp_polearm(125)|wp(80),knows_wot_infantry_3 ,man_face_young_1, man_face_old_2],
  ["legion_bannerman_multi","Legion Bannerman","Legion Bannermen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_ashwood_pike, itm_legion_plate, itm_shynbaulds_wot, itm_mail_gauntlets_wot, itm_andoran_helmet],
   def_attrib_wot_infantry_4 ,wp_polearm(180)|wp(100),knows_wot_infantry_4 ,man_face_young_1, man_face_old_2],

  ["red_hand_infantry_multi","Red Hand Redarm","Red Hand Redarms",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_red_arm_club, itm_red_arm_tunic, itm_red_hand_shield_weak, itm_leather_boots, itm_leather_gloves, itm_red_hand_bell_helm],
   def_attrib_wot_infantry_2 ,wp_one_handed(110)|wp(75),knows_wot_infantry_2 ,man_face_young_1, man_face_old_2],
    ["red_hand_pikeman_multi","Red Hand Pikeman","Red Hand Pikemen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_pike, itm_red_hand_tunic,itm_red_hand_shield_normal, itm_leather_boots, itm_leather_gloves, itm_red_hand_bell_helm],
   def_attrib_wot_infantry_3 ,wp_polearm(125)|wp(80),knows_wot_infantry_3 ,man_face_young_1, man_face_old_2],
  ["red_hand_bannerman_multi","Red Hand Bannerman","Red Hand Bannermen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_ashwood_pike, itm_red_hand_plate, itm_red_hand_greaves, itm_red_hand_plate_gauntlets, itm_red_hand_kettle_helm],
   def_attrib_wot_infantry_4 ,wp_polearm(180)|wp(100),knows_wot_infantry_4 ,man_face_young_1, man_face_old_2],
  ["red_hand_swordsman_multi","Red Hand Swordsman","Red Hand Swordsmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_sword_viking_3, itm_red_hand_shield_strong, itm_red_hand_plate, itm_red_hand_greaves, itm_red_hand_plate_gauntlets, itm_red_hand_kettle_helm],
   def_attrib_wot_infantry_4 ,wp_one_handed(180)|wp(100),knows_wot_infantry_4 ,man_face_young_1, man_face_old_2],
  
  ["two_rivers_farmer_multi","Two Rivers Farmer","Two Rivers Farmers",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_hatchet, itm_scythe, itm_leather_apron, itm_ragged_outfit, itm_leather_cap, itm_felt_hat, itm_leather_boots],
   def_attrib_wot_infantry_1 ,wp(75),knows_wot_infantry_1, andor_man_face_younger, andor_man_face_older],
  ["two_rivers_spearman_multi","Two Rivers Spearman","Two Rivers Spearmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_spear, itm_ragged_outfit, itm_leather_jerkin, itm_leather_boots, itm_leather_gloves, itm_leather_cap, itm_segmented_helmet],
   def_attrib_wot_infantry_2 ,wp_polearm(125)|wp(80),knows_wot_infantry_2, andor_man_face_younger, andor_man_face_older],
  ["two_rivers_halberdier_multi","Two Rivers Halberdier","Two Rivers Halberdiers",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_halberd, itm_two_rivers_armor, itm_leather_boots, itm_leather_gloves, itm_segmented_helmet],
   def_attrib_wot_infantry_3 ,wp_polearm(115)|wp(85),knows_wot_infantry_3 ,andor_man_face_younger, andor_man_face_older],


#  ["swadian_man_at_arms_multiplayer_ai","Swadian Man at Arms","Swadian Men at Arms",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_1,
#   [itm_lance,itm_bastard_sword_a,itm_tab_shield_heater_cav_a,
#    itm_mail_with_surcoat,itm_hide_boots,itm_norman_helmet,itm_hunter],
#   def_attrib|level(19),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_4|knows_shield_4|knows_power_strike_4|knows_athletics_1,swadian_face_young_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer_ai","Legion Cavalry","Legion Cavalry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_war_spear, itm_sword_medieval_a, itm_legion_army_tunic, itm_leather_boots, itm_leather_gloves, itm_skullcap, itm_saddle_horse],
   def_attrib_wot_cavalry_1 ,wp_polearm(100)|wp_one_handed(95)|wp(70),knows_wot_cavalry_1 ,man_face_young_1, man_face_old_2],
    ["legion_lancer_multi","Legion Lancer","Legion Lancers",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_lance, itm_legion_shield_normal, itm_legion_army_armor, itm_leather_boots, itm_leather_gloves, itm_nordic_helmet, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_polearm(120)|wp_one_handed(110)|wp(85),knows_wot_cavalry_2 ,man_face_young_1, man_face_old_2],
  ["legion_heavy_lancer_multi","Legion Heavy Lancer","Legion Heavy Lancers",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_heavy_lance, itm_legion_shield_strong, itm_legion_plate, itm_steel_greaves_wot, itm_gauntlets, itm_andoran_helmet, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_3 ,wp_polearm(150)|wp_one_handed(140)|wp(100),knows_wot_cavalry_3 ,man_face_young_1, man_face_old_2],
    ["legion_man_at_arms_multi","Legion Man at Arms","Legion Man at Arms",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_spiked_mace, itm_legion_shield_normal, itm_sword_viking_3, itm_legion_army_armor, itm_leather_boots, itm_leather_gloves, itm_nordic_helmet, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_polearm(120)|wp_one_handed(120)|wp(85),knows_wot_cavalry_2 ,man_face_young_1, man_face_old_2],
   ["legion_captain_multi","Legion Captain","Legion Captains",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_great_sword, itm_legion_shield_strong, itm_legion_plate, itm_steel_greaves_wot, itm_gauntlets, itm_andoran_helmet, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_4 ,wp_two_handed(175)|wp_one_handed(150)|wp(100),knows_wot_cavalry_4 ,man_face_young_1, man_face_old_2],
  
  ["red_hand_man_at_arms_multi","Red Hand Man at Arms","Red Hand Man at Arms",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_red_arm_hammer, itm_red_hand_shield_weak, itm_sword_viking_3, itm_red_arm_tunic, itm_leather_boots, itm_leather_gloves, itm_red_hand_bell_helm, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_polearm(120)|wp_one_handed(120)|wp(85),knows_wot_cavalry_2 ,man_face_young_1, man_face_old_2],
  ["red_hand_lancer_multi","Red Hand Lancer","Red Hand Lancers",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_heavy_lance, itm_red_hand_shield_strong, itm_red_hand_plate, itm_red_hand_greaves, itm_red_hand_plate_gauntlets, itm_red_hand_kettle_helm, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_3 ,wp_polearm(150)|wp_one_handed(140)|wp(100),knows_wot_cavalry_3 ,man_face_young_1, man_face_old_2],
    ["red_hand_light_cavalry_multi","Red Hand Light Cavalry","Red Hand Light Cavalry",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_war_spear, itm_red_hand_shield_normal, itm_red_hand_tunic, itm_leather_boots, itm_leather_gloves, itm_red_hand_bell_helm, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_polearm(120)|wp_one_handed(110)|wp(85),knows_wot_cavalry_2 ,man_face_young_1, man_face_old_2],
  ["red_hand_captain_multi","Red Hand Captain","Red Hand Captains",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_great_sword, itm_red_hand_shield_strong, itm_red_hand_plate, itm_red_hand_greaves, itm_red_hand_plate_gauntlets, itm_red_hand_kettle_helm, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_4 ,wp_two_handed(175)|wp_one_handed(150)|wp(100),knows_wot_cavalry_4 ,man_face_young_1, man_face_old_2],
    ["red_hand_skirmisher_multi","Red Hand Skirmisher","Red Hand Skirmishers",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_khergit_bow, itm_arrows, itm_sword_secondary, itm_red_hand_tunic, itm_leather_boots, itm_leather_gloves, itm_red_hand_bell_helm, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_archery(120)|wp_one_handed(110)|wp(85),knows_wot_horse_archer_3 ,man_face_young_1, man_face_old_2],
  
    ["two_rivers_scout_multi","Two Rivers Scout","Two Rivers Scouts",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_spear, itm_ragged_outfit, itm_leather_jerkin, itm_leather_boots, itm_leather_gloves, itm_leather_cap, itm_segmented_helmet, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_polearm(125)|wp(80),knows_wot_cavalry_2, andor_man_face_younger, andor_man_face_older],

  #################
#  ["vaegir_archer_multiplayer_ai","Vaegir Archer","Vaegir Archers",tf_guarantee_all,0,0,fac_kingdom_2,
#   [itm_arrows,itm_scimitar,itm_nomad_bow,
#    itm_leather_vest,itm_nomad_boots,itm_spiked_helmet,itm_nomad_cap],
#   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_4|knows_power_draw_5|knows_athletics_6|knows_shield_2,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_archer_multiplayer_ai","Mayene Bowman","Mayene Bowmen",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_short_bow, itm_arrows, itm_sword_secondary, itm_mayene_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_leather_cap],
   def_attrib_wot_infantry_2 ,wp_archery(90)|wp_one_handed(85)|wp(80),knows_wot_archer_2 ,mayene_man_face_young, mayene_man_face_older],

  ["cairhien_crossbowman_multi","Cairhien Crossbowman","Cairhien Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_crossbow, itm_bolts, itm_sword_secondary, itm_cairhien_shield_normal, itm_cairhien_army_armor, itm_leather_boots, itm_leather_gloves, itm_bascinet],
   def_attrib_wot_infantry_3 ,wp_crossbow(125)|wp_one_handed(110)|wp(85),knows_wot_archer_3 ,cairhien_man_face_young, cairhien_man_face_older],
  
  ["illian_bowman_multi","Illian Bowman","Illian Bowmen",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_short_bow, itm_arrows, itm_sword_secondary, itm_illian_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_skullcap],
   def_attrib_wot_infantry_2 ,wp_archery(90)|wp_one_handed(85)|wp(80),knows_wot_archer_2, illian_man_face_young, illian_man_face_older],
  ["illian_crossbowman_multi","Illian Crossbowman","Illian Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_crossbow, itm_bolts, itm_sword_secondary, itm_illian_army_armor, itm_leather_boots, itm_leather_gloves, itm_khergit_war_helmet],
   def_attrib_wot_infantry_3 ,wp_crossbow(110)|wp_one_handed(100)|wp(80),knows_wot_archer_3, illian_man_face_young, illian_man_face_older],
  ["illian_marksman_multi","Illian Marksman","Illian Marksmen",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_heavy_crossbow, itm_steel_bolts, itm_sword_secondary, itm_illian_army_armor, itm_leather_boots, itm_leather_gloves, itm_khergit_war_helmet],
   def_attrib_wot_infantry_4 ,wp_crossbow(145)|wp_one_handed(110)|wp(100),knows_wot_archer_4, illian_man_face_young, illian_man_face_older],

  ["murandy_bowman_multi","Murandy Bowman","Murandy Bowmen",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_nomad_bow, itm_arrows, itm_sword_secondary, itm_murandy_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_leather_warrior_cap],
   def_attrib_wot_infantry_3 ,wp_archery(100)|wp_one_handed(90)|wp(80),knows_wot_archer_3, murandy_man_face_young, murandy_man_face_older],
  ["murandy_marksman_multi","Murandy Marksman","Murandy Marksmen",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_war_bow, itm_bodkin_arrows, itm_sword_secondary, itm_murandy_leather_armor, itm_leather_boots, itm_leather_gloves, itm_nordic_fighter_helmet],
   def_attrib_wot_infantry_4 ,wp_archery(140)|wp_one_handed(110)|wp(100),knows_wot_archer_4, murandy_man_face_young, murandy_man_face_older],

  ["altara_knife_thrower_multi","Altara Knife Thrower","Altara Knife Throwers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_throwing_knives, itm_scimitar, itm_altara_army_armor, itm_altara_green_boots, itm_leather_gloves, itm_vaegir_spiked_helmet],
   def_attrib_wot_infantry_3 ,wp_throwing(110)|wp_one_handed(105)|wp(95),knows_wot_thrower_3 ,altara_man_face_young, altara_man_face_older],
  
  ["arad_doman_bowman_multi","Arad Doman Bowman","Arad Doman Bowmen",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_short_bow, itm_arrows, itm_sword_secondary, itm_arad_doman_army_armor, itm_light_leather_boots, itm_leather_gloves, itm_nordic_archer_helmet],
   def_attrib_wot_infantry_2 ,wp_archery(90)|wp_one_handed(85)|wp(80),knows_wot_archer_2 ,arad_doman_man_face_young, arad_doman_man_face_older],

  
#  ["vaegir_spearman_multiplayer_ai","Vaegir Spearman","Vaegir Spearmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
#   [itm_padded_leather,itm_nomad_boots,itm_spiked_helmet,itm_nomad_cap, itm_spear, itm_tab_shield_kite_b, itm_mace_1, itm_javelin],
#   def_attrib|str_12|level(19),wp_melee(90),knows_ironflesh_4|knows_athletics_6|knows_power_throw_3|knows_power_strike_3|knows_shield_2,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_spearman_multiplayer_ai","Mayene Militia","Mayene Militia",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_fighting_pick, itm_mayene_shield_weak, itm_mayene_recruit_tunic, itm_leather_boots, itm_leather_cap],
   def_attrib_wot_infantry_2 ,wp_one_handed(90)|wp(70),knows_wot_infantry_2 ,mayene_man_face_young, mayene_man_face_older],
  ["mayene_swordsman_multi","Mayene Swordsman","Mayene Swordsmen",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_mayene_sword, itm_mayene_shield_strong, itm_mayene_army_armor, itm_leather_boots, itm_leather_gloves, itm_kettle_hat_wot],
   def_attrib_wot_infantry_3 ,wp_one_handed(150)|wp(100),knows_wot_infantry_3 ,mayene_man_face_young, mayene_man_face_older],
  
  ["cairhien_militia_multi","Cairhien Militia","Cairhien Militia",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_sword_medieval_b, itm_cairhien_shield_weak, itm_cairhien_recruit_tunic, itm_leather_boots, itm_leather_cap],
   def_attrib_wot_infantry_2 ,wp_one_handed(90)|wp(70),knows_wot_infantry_2 ,cairhien_man_face_young, cairhien_man_face_older],
  ["cairhien_pikeman_multi","Cairhien Pikeman","Cairhien Pikemen",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_pike, itm_cairhien_army_armor ,itm_cairhien_shield_normal, itm_leather_boots, itm_leather_gloves, itm_bascinet],
   def_attrib_wot_infantry_3 ,wp_polearm(120)|wp(80),knows_wot_infantry_3 ,cairhien_man_face_young, cairhien_man_face_older],
  ["cairhien_bannerman_multi","Cairhien Bannerman","Cairhien Bannermen",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_ashwood_pike, itm_cairhien_plate, itm_shynbaulds_wot, itm_gauntlets, itm_cairhien_helmet],
   def_attrib_wot_infantry_4 ,wp_polearm(180)|wp(100),knows_wot_infantry_4 ,cairhien_man_face_young, cairhien_man_face_older],
  
  ["illian_militia_multi","Illian Militia","Illian Militia",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_illian_seax, itm_illian_shield_weak, itm_illian_recruit_tunic, itm_leather_boots, itm_skullcap],
   def_attrib_wot_infantry_2 ,wp_one_handed(90)|wp(70),knows_wot_infantry_2, illian_man_face_young, illian_man_face_older],
  ["illian_swordsman_multi","Illian Swordsman","Illian Swordsmen",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_sword_medieval_b, itm_illian_army_armor, itm_illian_shield_normal, itm_leather_boots, itm_leather_gloves, itm_khergit_war_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(120)|wp(80),knows_wot_infantry_3, illian_man_face_young, illian_man_face_older],
  ["illian_companion_multi","Illian Companion","Illian Companions",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_military_cleaver_b, itm_illian_companion_surcoat, itm_illian_shield_strong, itm_mail_chausses, itm_leather_gloves, itm_bascinet_3],
   def_attrib_wot_infantry_4 ,wp_one_handed(145)|wp(100),knows_wot_infantry_4, illian_man_face_young, illian_man_face_older],
  ["illian_companion_captain_multi","Illian Companion Captian","Illian Companion Captians",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_two_handed_cleaver, itm_illian_companion_captain_surcoat, itm_mail_chausses, itm_scale_gauntlets, itm_illian_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(180)|wp(125),knows_wot_infantry_4, illian_man_face_young, illian_man_face_older],
  
  ["murandy_militia_multi","Murandy Militia","Murandy Militia",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_fighting_pick, itm_murandy_shield_weak, itm_murandy_recruit_tunic, itm_leather_boots, itm_leather_warrior_cap],
   def_attrib_wot_infantry_2 ,wp_one_handed(90)|wp(70),knows_wot_infantry_2, murandy_man_face_young, murandy_man_face_older],
  ["murandy_maceman_multi","Murandy Maceman","Murandy Macemen",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_maul, itm_murandy_leather_armor, itm_leather_boots, itm_leather_gloves, itm_nordic_fighter_helmet],
   def_attrib_wot_infantry_3 ,wp_two_handed(120)|wp(80),knows_wot_infantry_3, murandy_man_face_young, murandy_man_face_older],
  ["murandy_berserker_multi","Murandy Berserker","Murandy Berserkers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_warhammer, itm_murandy_elite_armor, itm_mail_chausses, itm_mail_mittens, itm_nordic_huscarl_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(185)|wp(125),knows_wot_infantry_4, murandy_man_face_young, murandy_man_face_older],
  
  ["altara_dueler_multi","Altara Dueler","Altara Duelers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_dagger, itm_altara_recruit_armor, itm_altara_green_boots, itm_spiked_helmet],
   def_attrib_wot_infantry_2 ,wp_one_handed(90)|wp(70),knows_wot_infantry_2, altara_man_face_young, altara_man_face_older],
  ["altara_swordsman_multi","Altara Swordsman","Altara Swordsmen",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_scimitar_b, itm_altara_shield_normal, itm_altara_army_armor, itm_altara_green_boots, itm_leather_gloves, itm_vaegir_spiked_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(120)|wp(80),knows_wot_infantry_3, altara_man_face_young, altara_man_face_older],
  ["altara_royal_guard_multi","Altara Royal Guard","Altara Royal Guards",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_altara_royal_guard_halberd, itm_altara_royal_guard_armor, itm_altara_royal_guard_boots, itm_scale_gauntlets, itm_altara_royal_guard_helmet],
   def_attrib_wot_infantry_4 ,wp_polearm(180)|wp(125),knows_wot_infantry_4, altara_man_face_young, altara_man_face_older],
  
  ["arad_doman_rabble_multi","Arad Doman Rabble","Arad Doman Rabble",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_butchering_knife, itm_pitch_fork, itm_boar_spear, itm_pelt_coat, itm_sarranid_cloth_robe, itm_linen_tunic, itm_wrapping_boots, itm_steppe_cap],
   def_attrib_wot_infantry_2 ,wp_one_handed(90)|wp(70),knows_wot_infantry_2,arad_doman_man_face_young, arad_doman_man_face_older],
  ["arad_doman_swordsman_multi","Arad Doman Swordsman","Arad Doman Swordsmen",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_sword_viking_3, itm_arad_doman_shield_normal, itm_arad_doman_army_armor, itm_light_leather_boots, itm_leather_gloves, itm_nordic_archer_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(120)|wp(80),knows_wot_infantry_3, arad_doman_man_face_young, arad_doman_man_face_older],
  ["arad_doman_long_swordsman_multi","Arad Doman Long Swordsman","Arad Doman Long Swordsmen",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_sword_medieval_d_long, itm_arad_doman_shield_strong, itm_arad_doman_elite_armor, itm_splinted_greaves, itm_gauntlets, itm_nasal_helmet],
   def_attrib_wot_infantry_4 ,wp_one_handed(150)|wp(100),knows_wot_infantry_4, arad_doman_man_face_young, arad_doman_man_face_older],


#  ["vaegir_horseman_multiplayer_ai","Vaegir Horseman","Vaegir Horsemen",tf_mounted|tf_guarantee_all_wo_ranged,0,0,fac_kingdom_2,
#   [itm_battle_axe,itm_scimitar,itm_lance,itm_tab_shield_kite_cav_a,
#     itm_studded_leather_coat,itm_lamellar_vest,itm_nomad_boots,itm_spiked_helmet,itm_saddle_horse],
#   def_attrib|level(19),wp(100),knows_riding_4|knows_ironflesh_4|knows_power_strike_4|knows_shield_3,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayer_ai","Mayene Man at Arms","Mayene Man at Arms",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_mayene_sword, itm_mayene_shield_weak, itm_mayene_army_armor, itm_leather_boots, itm_leather_gloves, itm_kettle_hat_wot, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_polearm(120)|wp_one_handed(120)|wp(85),knows_wot_cavalry_2 ,mayene_man_face_young, mayene_man_face_older],
  ["mayene_lancer_multi","Mayene Lancer","Mayene Lancers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_lance, itm_mayene_shield_normal, itm_mayene_army_armor, itm_leather_boots, itm_leather_gloves, itm_kettle_hat_wot, itm_courser, itm_hunter],
   def_attrib_wot_cavalry_3 ,wp_polearm(150)|wp_one_handed(120)|wp(85),knows_wot_cavalry_3 ,mayene_man_face_young, mayene_man_face_older],
  ["mayene_royal_guard_multi","Mayene Winged Guard","Mayene Winged Guards",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_heavy_lance, itm_mayene_plate, itm_mayene_greaves, itm_mayene_gauntlets_red, itm_mayene_winged_guard_helmet, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_4 ,wp_polearm(140)|wp_one_handed(130)|wp(100),knows_wot_cavalry_4 ,mayene_man_face_young, mayene_man_face_older],

  ["cairhien_man_at_arms_multi","Cairhien Man at Arms","Cairhien Man at Arms",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_fighting_axe, itm_cairhien_shield_normal, itm_cairhien_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_bascinet, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_one_handed(120)|wp(85),knows_wot_cavalry_2 ,cairhien_man_face_young, cairhien_man_face_older],
  ["cairhien_light_cavalry_multi","Cairhien Light Cavalry","Cairhien Light Cavalry",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_sword_medieval_b, itm_cairhien_shield_normal, itm_cairhien_army_armor, itm_leather_boots, itm_leather_gloves, itm_bascinet, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_one_handed(120)|wp(85),knows_wot_cavalry_3 ,cairhien_man_face_young, cairhien_man_face_older],
  ["cairhien_lancer_multi","Cairhien Lancer","Cairhien Lancers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_heavy_lance, itm_cairhien_shield_strong, itm_cairhien_plate, itm_shynbaulds_wot, itm_gauntlets, itm_cairhien_helmet, itm_courser, itm_hunter],
   def_attrib_wot_cavalry_3 ,wp_polearm(150)|wp_one_handed(140)|wp(100),knows_wot_cavalry_3 ,cairhien_man_face_young, cairhien_man_face_older],

  ["illian_scout_multi","Illian Scout","Illian Scouts",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_war_spear, itm_sword_medieval_a, itm_illian_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_skullcap, itm_saddle_horse],
   def_attrib_wot_cavalry_1 ,wp_polearm(100)|wp_one_handed(95)|wp(70),knows_wot_cavalry_1, illian_man_face_young, illian_man_face_older],
  ["illian_man_at_arms_multi","Illian Man at Arms","Illian Man at Arms",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_spiked_mace, itm_illian_shield_normal, itm_illian_army_armor, itm_leather_boots, itm_leather_gloves, itm_khergit_war_helmet, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_one_handed(120)|wp(85),knows_wot_cavalry_2, illian_man_face_young, illian_man_face_older],

  ["murandy_scout_multi","Murandy Scout","Murandy Scouts",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_hammer, itm_murandy_shield_weak, itm_murandy_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_leather_warrior_cap, itm_steppe_horse],
   def_attrib_wot_cavalry_1 ,wp_one_handed(100)|wp(70),knows_wot_cavalry_1, murandy_man_face_young, murandy_man_face_older],
  ["murandy_lancer_multi","Murandy Lancer","Murandy Lancers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_lance, itm_murandy_shield_normal, itm_murandy_leather_armor, itm_leather_boots, itm_leather_gloves, itm_nordic_fighter_helmet, itm_courser, itm_hunter],
   def_attrib_wot_cavalry_2 ,wp_polearm(120)|wp_one_handed(110)|wp(85),knows_wot_cavalry_2 ,murandy_man_face_young, murandy_man_face_older],
  ["murandy_captain_multi","Murandy Captain","Murandy Captains",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_heavy_lance, itm_murandy_shield_strong, itm_murandy_elite_armor, itm_mail_mittens, itm_mail_chausses, itm_nordic_huscarl_helmet, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_3 ,wp_polearm(145)|wp_one_handed(120)|wp(100),knows_wot_cavalry_3 ,murandy_man_face_young, murandy_man_face_older],

  ["altara_scout_multi","Altara Scout","Altara Scouts",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_war_spear, itm_sword_medieval_a, itm_altara_shield_weak, itm_altara_recruit_armor, itm_altara_green_boots, itm_leather_gloves, itm_spiked_helmet, itm_saddle_horse],
   def_attrib_wot_cavalry_1 ,wp_polearm(100)|wp_one_handed(95)|wp(70),knows_wot_cavalry_1, altara_man_face_young, altara_man_face_older],
  ["altara_man_at_arms_multi","Altara Man at Arms","Altara Man at Arms",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_sarranid_cavalry_sword, itm_altara_shield_strong, itm_altara_army_armor, itm_leather_gloves, itm_altara_green_boots, itm_vaegir_spiked_helmet, itm_courser, itm_hunter],
   def_attrib_wot_cavalry_3 ,wp_one_handed(135)|wp(100),knows_wot_cavalry_3 ,altara_man_face_young, altara_man_face_older],
  ["altara_skirmisher_multi","Altara Skirmisher","Altara Skirmishers",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_khergit_bow, itm_arrows, itm_sword_secondary, itm_altara_army_armor, itm_altara_green_boots, itm_leather_gloves, itm_vaegir_spiked_helmet, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_archery(120)|wp_one_handed(110)|wp(85),knows_wot_horse_archer_2 ,altara_man_face_young, altara_man_face_older],

  ["arad_doman_scout_multi","Arad Doman Scout","Arad Doman Scouts",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_war_spear, itm_sword_medieval_a, itm_arad_doman_shield_weak, itm_arad_doman_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_steppe_cap, itm_saddle_horse],
   def_attrib_wot_cavalry_1 ,wp_polearm(100)|wp_one_handed(95)|wp(70),knows_wot_cavalry_1, arad_doman_man_face_young, arad_doman_man_face_older],
   ["arad_doman_man_at_arms_multi","Arad Doman Man at Arms","Arad Doman Man at Arms",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_sword_medieval_c_long, itm_arad_doman_shield_normal, itm_arad_doman_army_armor, itm_light_leather_boots, itm_leather_gloves, itm_nordic_archer_helmet, itm_courser, itm_hunter],
   def_attrib_wot_cavalry_3 ,wp_one_handed(135)|wp(100),knows_wot_cavalry_3 ,arad_doman_man_face_young, arad_doman_man_face_older],


  #################
#  ["khergit_dismounted_lancer_multiplayer_ai","Khergit Dismounted Lancer","Khergit Dismounted Lancer",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
#   [itm_sword_khergit_4,itm_spiked_mace,itm_one_handed_war_axe_b,itm_one_handed_war_axe_a,itm_hafted_blade_a,itm_hafted_blade_b,itm_heavy_lance,itm_lance,
#    itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_war_helmet,itm_lamellar_vest_khergit,itm_lamellar_armor,itm_khergit_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves,itm_mail_mittens,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,itm_courser],
#   def_attrib|level(23),wp(150),knows_riding_7|knows_power_strike_5|knows_power_draw_2|knows_power_throw_2|knows_ironflesh_5|knows_horse_archery_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_dismounted_lancer_multiplayer_ai","Tear Town Watch","Tear Town Watch",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_street_patrol_club, itm_tear_recruit_tunic, itm_arming_cap, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_1 ,wp_one_handed(100)|wp(70),knows_wot_infantry_1 ,tear_man_face_young, tear_man_face_old],
  ["tear_swordsman_multi","Tear Swordsman","Tear Swordsmen",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_medieval_c_long, itm_tear_shield_normal, itm_tear_plate, itm_splinted_greaves_nospurs_wot, itm_leather_gloves, itm_tear_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(120)|wp(80),knows_wot_infantry_3, tear_man_face_young, tear_man_face_old],
  ["tear_defender_multi","Tear Defender","Tear Defenders",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_war_spear, itm_tear_defender_armor, itm_black_leather_boots, itm_tear_defender_gauntlets, itm_tear_defender_helmet],
   def_attrib_wot_infantry_4 ,wp_polearm(135)|wp(90),knows_wot_infantry_4, tear_man_face_young, tear_man_face_old],
  ["tear_blademaster_multi","Tear Blademaster","Tear Blademasters",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_flamberge, itm_tear_gilded_plate, itm_shynbaulds_wot, itm_mail_gauntlets_wot, itm_tear_elite_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(180)|wp(100),knows_wot_infantry_4 ,tear_man_face_young, tear_man_face_old],
  ["tear_defender_captain_multi","Tear Defender Captain","Tear Defender Captains",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_awlpike, itm_tear_defender_captain_armor, itm_black_greaves, itm_tear_defender_gauntlets, itm_tear_defender_helmet],
   def_attrib_wot_infantry_5 ,wp_polearm(175)|wp(150),knows_wot_infantry_5, tear_man_face_young, tear_man_face_old],

  ["andor_militia_multi","Andor Militia","Andor Militia",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_falchion, itm_andor_shield_weak, itm_andor_recruit_tunic, itm_skullcap, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2 ,wp_one_handed(100)|wp(70),knows_wot_infantry_2 ,andor_man_face_young, andor_man_face_older],
  ["andor_swordsman_multi","Andor Swordsman","Andor Swordsmen",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_viking_3, itm_andor_shield_normal, itm_andor_army_armor, itm_leather_boots, itm_leather_gloves, itm_nordic_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(120)|wp(80),knows_wot_infantry_3, andor_man_face_young, andor_man_face_older],
  ["andor_blademaster_multi","Andor Blademaster","Andor Blademasters",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_two_handed_a, itm_andor_plate, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_andoran_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(180)|wp(100),knows_wot_infantry_4 ,andor_man_face_young, andor_man_face_older],
  ["andor_halberdier_multi","Andor Halberdier","Andor Halberdiers",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_halberd, itm_andor_plate, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_andoran_helmet],
   def_attrib_wot_infantry_4 ,wp_polearm(180)|wp(100),knows_wot_infantry_4 ,andor_man_face_young, andor_man_face_older],

  ["ghealdan_militia_multi","Ghealdan Militia","Ghealdan Militia",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_one_handed_battle_axe_a, itm_ghealdan_shield_weak, itm_ghealdan_recruit_tunic, itm_footman_helmet, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2 ,wp_one_handed(100)|wp(70),knows_wot_infantry_2 ,ghealdan_man_face_young, ghealdan_man_face_older],
  ["ghealdan_axeman_multi","Ghealdan Axeman","Ghealdan Axemen",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_one_handed_battle_axe_b, itm_ghealdan_shield_normal, itm_ghealdan_army_armor, itm_leather_boots, itm_leather_gloves, itm_guard_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(120)|wp(80),knows_wot_infantry_3, ghealdan_man_face_young, ghealdan_man_face_older],
  ["ghealdan_heavy_axeman_multi","Ghealdan Heavy Axeman","Ghealdan Heavy Axemen",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_long_axe_b, itm_ghealdan_plate, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_bascinet_2],
   def_attrib_wot_infantry_4 ,wp_two_handed(175)|wp(100),knows_wot_infantry_4 ,ghealdan_man_face_young, ghealdan_man_face_older],

  ["far_madding_footman_multi","Far Madding Street Guard","Far Madding Street Guards",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_street_patrol_club, itm_far_madding_shield_weak, itm_far_madding_recruit_tunic, itm_leather_warrior_cap, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2 ,wp_one_handed(100)|wp(70),knows_wot_infantry_2 ,far_madding_man_face_young, far_madding_man_face_older],
  ["far_madding_city_guard_multi","Far Madding City Guard","Far Madding City Guards",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_war_spear, itm_far_madding_shield_normal, itm_far_madding_armor, itm_mail_chausses, itm_leather_gloves, itm_bascinet_3],
   def_attrib_wot_infantry_3 ,wp_polearm(150)|wp(100),knows_wot_infantry_3 ,far_madding_man_face_young, far_madding_man_face_older],

  ["tarabon_rabble_multi","Tarabon Rabble","Tarabon Rabble",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_butchering_knife, itm_pitch_fork, itm_boar_spear, itm_pelt_coat, itm_sarranid_cloth_robe_b, itm_linen_tunic, itm_nomad_boots, itm_nomad_cap],
   def_attrib_wot_infantry_2 ,wp_one_handed(90)|wp(70),knows_wot_infantry_2,tarabon_man_face_young, tarabon_man_face_older],
  ["tarabon_spearman_multi","Tarabon Spearman","Tarabon Spearmen",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_war_spear, itm_tarabon_shield_normal, itm_tarabon_army_armor, itm_leather_boots, itm_leather_gloves, itm_vaegir_war_helmet],
   def_attrib_wot_infantry_3 ,wp_polearm(150)|wp(100),knows_wot_infantry_3 ,tarabon_man_face_young, tarabon_man_face_older],

  ["amadicia_militia_multi","Amadicia Militia","Amadicia Militia",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_spear, itm_amadicia_shield_weak, itm_amadicia_recruit_tunic, itm_black_hood, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2 ,wp_polearm(100)|wp(70),knows_wot_infantry_2 ,amadicia_man_face_young, amadicia_man_face_older],
  ["amadicia_pikeman_multi","Amadicia Pikeman","Amadicia Pikemen",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_pike, itm_amadicia_army_armor ,itm_amadicia_shield_normal, itm_leather_boots, itm_leather_gloves, itm_segmented_helmet],
   def_attrib_wot_infantry_3 ,wp_polearm(120)|wp(80),knows_wot_infantry_3 ,amadicia_man_face_young, amadicia_man_face_older],
  ["whitecloak_footman_multi","Whitecloak Footman","Whitecloak Footmen",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_medieval_b, itm_whitecloak_shield_weak, itm_whitecloak_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_segmented_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(120)|wp(80),knows_wot_infantry_3, man_face_young_1, man_face_old_2],
  ["whitecloak_swordsman_multi","Whitecloak Swordsman","Whitecloak Swordsmen",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_medieval_c_long, itm_whitecloak_shield_normal, itm_whitecloak_questioner_tabbard, itm_mail_chausses, itm_mail_mittens, itm_guard_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(135)|wp(100),knows_wot_infantry_3, man_face_young_1, man_face_old_2],
  ["amadicia_captain_multi","Amadicia Captain","Amadicia Captains",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_ashwood_pike, itm_amadicia_shield_strong, itm_amadicia_elite_armor, itm_shynbaulds_wot, itm_gauntlets, itm_flat_topped_helmet],
   def_attrib_wot_infantry_4 ,wp_polearm(180)|wp(100),knows_wot_infantry_4 ,amadicia_man_face_young, amadicia_man_face_older],
  ["whitecloak_captain_multi","Whitecloak Captain","Whitecloak Captains",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_great_sword, itm_whitecloak_tabbard, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_whitecloak_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(175)|wp(100),knows_wot_infantry_4 ,man_face_young_1, man_face_old_2],

#  ["khergit_veteran_horse_archer_multiplayer_ai","Khergit Horse Archer","Khergit Horse Archers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
#   [itm_sword_khergit_3,itm_khergit_bow,itm_khergit_arrows,itm_tab_shield_small_round_b,
#    itm_khergit_cavalry_helmet,itm_tribal_warrior_outfit,itm_khergit_leather_boots,itm_steppe_horse],
#   def_attrib|level(21),wp(90)|wp_archery(150),knows_riding_6|knows_power_draw_5|knows_shield_2|knows_horse_archery_5,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_veteran_horse_archer_multiplayer_ai","Tear Bowman","Tear Bowmen",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_strong_bow, itm_arrows, itm_sword_secondary, itm_tear_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_arming_cap],
   def_attrib_wot_infantry_3 ,wp_archery(100)|wp_one_handed(90)|wp(80),knows_wot_archer_3, tear_man_face_young, tear_man_face_old],
  ["tear_crossbowman_multi","Tear Crossbowman","Tear Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_crossbow, itm_bolts, itm_sword_secondary, itm_tear_shield_normal, itm_tear_plate, itm_splinted_greaves_nospurs_wot, itm_leather_gloves, itm_tear_helmet],
   def_attrib_wot_infantry_3 ,wp_crossbow(125)|wp_one_handed(110)|wp(85),knows_wot_archer_3 ,tear_man_face_young, tear_man_face_old],

  ["andor_bowman_multi","Andor Bowman","Andor Bowmen",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_strong_bow, itm_arrows, itm_sword_secondary, itm_andor_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_skullcap],
   def_attrib_wot_infantry_3 ,wp_archery(100)|wp_one_handed(90)|wp(80),knows_wot_archer_3, andor_man_face_young, andor_man_face_older],
  ["andor_crossbowman_multi","Andor Crossbowman","Andor Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_crossbow, itm_bolts, itm_sword_secondary, itm_andor_shield_normal, itm_andor_army_armor, itm_leather_boots, itm_leather_gloves, itm_nordic_helmet],
   def_attrib_wot_infantry_3 ,wp_crossbow(125)|wp_one_handed(110)|wp(85),knows_wot_archer_3 ,andor_man_face_young, andor_man_face_older],
  
  ["ghealdan_bowman_multi","Ghealdan Bowman","Ghealdan Bowmen",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_strong_bow, itm_arrows, itm_sword_secondary, itm_ghealdan_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_footman_helmet],
   def_attrib_wot_infantry_2 ,wp_archery(100)|wp_one_handed(90)|wp(80),knows_wot_archer_2, ghealdan_man_face_young, ghealdan_man_face_older],
  ["ghealdan_marksman_multi","Ghealdan Marksman","Ghealdan Marksmen",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_war_bow, itm_bodkin_arrows, itm_sword_secondary, itm_ghealdan_army_armor, itm_leather_boots, itm_leather_gloves, itm_guard_helmet],
   def_attrib_wot_infantry_3 ,wp_archery(135)|wp_one_handed(110)|wp(95),knows_wot_archer_3, ghealdan_man_face_young, ghealdan_man_face_older],

  ["far_madding_crossbowman_multi","Far Madding Crossbowman","Far Madding Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_crossbow, itm_bolts, itm_sword_secondary, itm_far_madding_shield_normal, itm_far_madding_armor, itm_mail_chausses, itm_leather_gloves, itm_bascinet_3],
   def_attrib_wot_infantry_3 ,wp_crossbow(125)|wp_one_handed(110)|wp(85),knows_wot_archer_3 ,far_madding_man_face_young, far_madding_man_face_older],
  
  ["tarabon_bowman_multi","Tarabon Bowman","Tarabon Bowmen",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_strong_bow, itm_arrows, itm_sword_secondary, itm_tarabon_recruit_tunic, itm_nomad_boots, itm_leather_gloves, itm_sarranid_helmet1],
   def_attrib_wot_infantry_2 ,wp_archery(100)|wp_one_handed(90)|wp(80),knows_wot_archer_2, tarabon_man_face_young, tarabon_man_face_older],
  ["tarabon_marksman_multi","Tarabon Marksman","Tarabon Marksmen",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_war_bow, itm_bodkin_arrows, itm_sword_secondary, itm_tarabon_army_armor, itm_leather_boots, itm_leather_gloves, itm_vaegir_war_helmet],
   def_attrib_wot_infantry_4 ,wp_archery(155)|wp_one_handed(125)|wp(105),knows_wot_archer_4, tarabon_man_face_young, tarabon_man_face_older],
  
  ["amadicia_bowman_multi","Amadicia Bowman","Amadicia Bowmen",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_short_bow, itm_arrows, itm_sword_secondary, itm_amadicia_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_black_hood],
   def_attrib_wot_infantry_2 ,wp_archery(100)|wp_one_handed(90)|wp(80),knows_wot_archer_2, amadicia_man_face_young, amadicia_man_face_older],
  ["whitecloak_bowman_multi","Whitecloak Bowman","Whitecloak Bowmen",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_short_bow, itm_arrows, itm_sword_secondary, itm_whitecloak_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_segmented_helmet],
   def_attrib_wot_infantry_2 ,wp_archery(100)|wp_one_handed(90)|wp(80),knows_wot_archer_2, man_face_young_1, man_face_old_2],
  ["whitecloak_crossbowman_multi","Whitecloak Crossbowman","Whitecloak Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_crossbow, itm_bolts, itm_sword_secondary, itm_whitecloak_tabbard, itm_mail_chausses, itm_leather_gloves, itm_guard_helmet],
   def_attrib_wot_infantry_3 ,wp_crossbow(125)|wp_one_handed(110)|wp(85),knows_wot_archer_3 ,man_face_young_1, man_face_old_2],
  

#  ["khergit_lancer_multiplayer_ai","Khergit Lancer","Khergit Lancers",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_3,
#   [itm_sword_khergit_4,itm_spiked_mace,itm_one_handed_war_axe_b,itm_one_handed_war_axe_a,itm_hafted_blade_a,itm_hafted_blade_b,itm_heavy_lance,itm_lance,
#    itm_khergit_guard_helmet,itm_khergit_cavalry_helmet,itm_khergit_war_helmet,itm_lamellar_vest_khergit,itm_lamellar_armor,itm_khergit_leather_boots,itm_splinted_leather_greaves,itm_leather_gloves,itm_mail_mittens,itm_scale_gauntlets,itm_tab_shield_small_round_b,itm_tab_shield_small_round_c,itm_courser],
#   def_attrib|level(23),wp(150),knows_riding_7|knows_power_strike_5|knows_power_draw_2|knows_power_throw_2|knows_ironflesh_5|knows_horse_archery_1,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer_multiplayer_ai","Tear Scout","Tear Scouts",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_war_spear, itm_sword_medieval_a, itm_tear_shield_weak, itm_tear_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_arming_cap, itm_saddle_horse, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_polearm(110)|wp_one_handed(100)|wp(75),knows_wot_cavalry_2, tear_man_face_young, tear_man_face_old],
  ["tear_lancer_multi","Tear Lancer","Tear Lancers",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_lance, itm_tear_shield_normal, itm_tear_plate, itm_splinted_greaves_spurs_wot, itm_leather_gloves, itm_tear_helmet, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_3 ,wp_polearm(135)|wp_one_handed(110)|wp(85),knows_wot_cavalry_3 ,tear_man_face_young, tear_man_face_old],
  ["tear_light_cavalry_multi","Tear Light Cavalry","Tear Light Cavalry",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_medieval_b, itm_tear_shield_normal, itm_tear_plate, itm_splinted_greaves_spurs_wot, itm_leather_gloves, itm_tear_helmet, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_one_handed(115)|wp(85),knows_wot_cavalry_3 ,tear_man_face_young, tear_man_face_old],
  ["tear_heavy_lancer_multi","Tear Heavy Lancer","Tear Heavy Lancers",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_heavy_lance, itm_tear_shield_strong, itm_tear_gilded_plate, itm_gauntlets, itm_shynbaulds_wot, itm_tear_elite_helmet, itm_warhorse, itm_charger],
   def_attrib_wot_cavalry_4 ,wp_polearm(155)|wp_one_handed(120)|wp(100),knows_wot_cavalry_4 ,tear_man_face_young, tear_man_face_old],

  ["andor_scout_multi","Andor Scout","Andor Scouts",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_medieval_a, itm_andor_shield_weak, itm_andor_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_skullcap, itm_saddle_horse],
   def_attrib_wot_cavalry_2 ,wp_one_handed(105)|wp(75),knows_wot_cavalry_2, andor_man_face_young, andor_man_face_older],
  ["andor_lancer_multi","Andor Lancer","Andor Lancers",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_lance, itm_andor_shield_normal, itm_andor_plate, itm_steel_greaves_wot, itm_leather_gloves, itm_andoran_helmet, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_polearm(135)|wp_one_handed(110)|wp(85),knows_wot_cavalry_3 ,andor_man_face_young, andor_man_face_older],
  ["andor_queens_guard_multi","Andor Queen's Guard","Andor Queen's Guards",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_lance, itm_andor_shield_strong, itm_andor_queens_guard_armor, itm_steel_greaves_wot, itm_wisby_gauntlets_red_wot, itm_andoran_helmet, itm_courser, itm_hunter],
   def_attrib_wot_cavalry_4 ,wp_polearm(150)|wp_one_handed(120)|wp(85),knows_wot_cavalry_4 ,andor_man_face_young, andor_man_face_older],
  ["andor_man_at_arms_multi","Andor Man at Arms","Andor Man at Arms",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_one_handed_war_axe_b, itm_andor_shield_normal, itm_andor_army_armor, itm_leather_boots, itm_leather_gloves, itm_nordic_helmet, itm_courser, itm_hunter],
   def_attrib_wot_cavalry_3 ,wp_one_handed(120)|wp(85),knows_wot_cavalry_3 ,andor_man_face_young, andor_man_face_older],
  ["andor_bannerman_multi","Andor Bannerman","Andor Bannermen",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_heavy_lance, itm_andor_shield_strong, itm_andor_queens_guard_armor, itm_steel_greaves_wot, itm_wisby_gauntlets_red_wot, itm_sugarloaf_wot, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_4 ,wp_polearm(165)|wp_one_handed(120)|wp(85),knows_wot_cavalry_4 ,andor_man_face_young, andor_man_face_older],

  ["ghealdan_scout_multi","Ghealdan Scout","Ghealdan Scouts",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_one_handed_battle_axe_a, itm_ghealdan_shield_weak, itm_ghealdan_recruit_tunic, itm_leather_boots, itm_leather_gloves, itm_footman_helmet, itm_saddle_horse],
   def_attrib_wot_cavalry_2 ,wp_one_handed(105)|wp(75),knows_wot_cavalry_2, ghealdan_man_face_young, ghealdan_man_face_older],
  ["ghealdan_lancer_multi","Ghealdan Lancer","Ghealdan Lancers",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_lance, itm_ghealdan_shield_normal, itm_ghealdan_army_armor, itm_steel_greaves_wot, itm_leather_gloves, itm_guard_helmet, itm_courser, itm_hunter],
   def_attrib_wot_cavalry_3 ,wp_polearm(135)|wp_one_handed(110)|wp(85),knows_wot_cavalry_3 , ghealdan_man_face_young, ghealdan_man_face_older],
  ["ghealdan_man_at_arms_multi","Ghealdan Man at Arms","Ghealdan Man at Arms",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_one_handed_battle_axe_b, itm_ghealdan_shield_normal, itm_ghealdan_army_armor, itm_leather_boots, itm_leather_gloves, itm_guard_helmet, itm_courser, itm_hunter],
   def_attrib_wot_cavalry_3 ,wp_one_handed(120)|wp(85),knows_wot_cavalry_3 ,ghealdan_man_face_young, ghealdan_man_face_older],
  ["ghealdan_royal_guard_multi","Ghealdan Royal Guard","Ghealdan Royal Guards",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_heavy_lance, itm_ghealdan_shield_strong, itm_ghealdan_plate, itm_steel_greaves_wot, itm_gauntlets, itm_bascinet_2, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_4 ,wp_polearm(165)|wp_one_handed(120)|wp(85),knows_wot_cavalry_4 ,ghealdan_man_face_young, ghealdan_man_face_older],
  
  ["tarabon_scout_multi","Tarabon Scout","Tarabon Scouts",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_military_fork, itm_tarabon_shield_weak, itm_tarabon_recruit_tunic, itm_nomad_boots, itm_leather_gloves, itm_sarranid_helmet1, itm_saddle_horse],
   def_attrib_wot_cavalry_2 ,wp_polearm(105)|wp(75),knows_wot_cavalry_2, tarabon_man_face_young, tarabon_man_face_older],
  ["tarabon_lancer_multi","Tarabon Lancer","Tarabon Lancers",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_lance, itm_tarabon_shield_strong, itm_tarabon_elite_armor, itm_sarranid_boots_d, itm_scale_gauntlets, itm_sarranid_veiled_helmet, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_3 ,wp_polearm(150)|wp_one_handed(140)|wp(100),knows_wot_cavalry_3 ,tarabon_man_face_young, tarabon_man_face_older],
  ["tarabon_skirmisher_multi","Tarabon Skirmisher","Tarabon Skirmishers",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_khergit_bow, itm_arrows, itm_sword_secondary, itm_tarabon_elite_armor, itm_sarranid_boots_d, itm_leather_gloves, itm_sarranid_veiled_helmet, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_archery(145)|wp_one_handed(115)|wp(85),knows_wot_horse_archer_3 ,tarabon_man_face_young, tarabon_man_face_older],

  ["whitecloak_man_at_arms_multi","Whitecloak Man at Arms","Whitecloak Man at Arms",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_medieval_c_long, itm_whitecloak_shield_normal, itm_whitecloak_questioner_tabbard, itm_mail_chausses, itm_mail_mittens, itm_guard_helmet, itm_courser, itm_hunter],
   def_attrib_wot_cavalry_3 ,wp_one_handed(140)|wp(100),knows_wot_cavalry_3 ,man_face_young_1, man_face_old_2],
   ["amadicia_skirmisher_multi","Amadicia Skirmisher","Amadicia Skirmishers",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_khergit_bow, itm_arrows, itm_sword_secondary, itm_amadicia_army_armor, itm_leather_boots, itm_leather_gloves, itm_segmented_helmet, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_archery(150)|wp_one_handed(115)|wp(85),knows_wot_horse_archer_3 ,amadicia_man_face_young, amadicia_man_face_older],
  ["whitecloak_lancer_multi","Whitecloak Lancer","Whitecloak Lancer",tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_heavy_lance, itm_whitecloak_shield_strong, itm_whitecloak_tabbard, itm_steel_greaves_wot, itm_mail_gauntlets_wot, itm_whitecloak_helmet, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_4 ,wp_polearm(165)|wp_one_handed(140)|wp(100),knows_wot_cavalry_4 ,man_face_young_1, man_face_old_2],


  ################
#  ["nord_veteran_multiplayer_ai","Nord Footman","Nord Footmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_4,
#   [itm_sword_viking_2,itm_one_handed_battle_axe_b,itm_two_handed_axe,itm_tab_shield_round_d,itm_throwing_axes,
#    itm_nordic_helmet,itm_nordic_fighter_helmet,itm_mail_hauberk,itm_splinted_leather_greaves,itm_leather_boots,itm_leather_gloves],
#   def_attrib|level(19),wp(130),knows_ironflesh_3|knows_power_strike_5|knows_power_throw_3|knows_athletics_5|knows_shield_3,nord_face_young_1, nord_face_older_2],
  ["nord_veteran_multiplayer_ai","Shienar Militia","Shienar Militia",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_sword_medieval_b, itm_shienar_shield_weak, itm_shienar_leather_armor, itm_skullcap, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2 ,wp_one_handed(100)|wp(70),knows_wot_infantry_2 ,shienar_man_face_young, shienar_man_face_older],
  ["shienar_spearman_multi","Shienar Spearman","Shienar Spearmen",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_war_spear, itm_shienar_shield_normal, itm_mail_shirt, itm_mail_chausses, itm_leather_gloves, itm_nordic_fighter_helmet],
   def_attrib_wot_infantry_3 ,wp_polearm(125)|wp(100),knows_wot_infantry_3, shienar_man_face_young, shienar_man_face_older],
  ["shienar_swordsman_multi","Shienar Swordsman","Shienar Swordsmen",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_sword_medieval_d_long, itm_shienar_shield_strong, itm_banded_armor, itm_mail_chausses, itm_gauntlets, itm_nordic_warlord_helmet],
   def_attrib_wot_infantry_4 ,wp_one_handed(155)|wp(100),knows_wot_infantry_4, shienar_man_face_young, shienar_man_face_older],
  ["shienar_pikeman_multi","Shienar Pikeman","Shienar Pikemen",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_ashwood_pike, itm_shienar_shield_strong, itm_banded_armor, itm_mail_chausses, itm_gauntlets, itm_nordic_warlord_helmet],
   def_attrib_wot_infantry_4 ,wp_polearm(155)|wp(100),knows_wot_infantry_4, shienar_man_face_young, shienar_man_face_older],
  ["shienar_blademaster_multi","Shienar Blademaster","Shienar Blademasters",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_great_sword, itm_plate_armor, itm_steel_greaves_wot, itm_gauntlets, itm_great_helmet],
   def_attrib_wot_infantry_5 ,wp_two_handed(190)|wp(150),knows_wot_infantry_5, shienar_man_face_young, shienar_man_face_older],

  ["arafel_militia_multi","Arafel Militia","Arafel Militia",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_mace_2, itm_arafel_shield_weak, itm_arafel_army_armor, itm_mail_coif, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2 ,wp_one_handed(100)|wp(70),knows_wot_infantry_2 ,arafel_man_face_young, arafel_man_face_older],
  ["arafel_swordsman_multi","Arafel Swordsman","Arafel Swordsmen",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_sword_viking_3, itm_arafel_shield_normal, itm_arafel_tabbard, itm_splinted_greaves_nospurs_wot, itm_mail_mittens, itm_guard_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(120)|wp(100),knows_wot_infantry_3, arafel_man_face_young, arafel_man_face_older],
  ["arafel_halberdier_multi","Arafel Halberdier","Arafel Halberdiers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_halberd, itm_arafel_tabbard, itm_splinted_greaves_nospurs_wot, itm_mail_mittens, itm_guard_helmet],
   def_attrib_wot_infantry_4 ,wp_polearm(150)|wp(100),knows_wot_infantry_4, arafel_man_face_young, arafel_man_face_older],
  ["arafel_blademaster_multi","Arafel Blademaster","Arafel Blademasters",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_sword_of_war, itm_arafel_mail_and_plate, itm_steel_greaves_wot, itm_gauntlets, itm_oniontop_bascinet_wot],
   def_attrib_wot_infantry_4 ,wp_two_handed(180)|wp(150),knows_wot_infantry_4, arafel_man_face_young, arafel_man_face_older],
  ["arafel_bannerman_multi","Arafel Bannerman","Arafel Bannermen",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_poleaxe, itm_arafel_mail_and_plate, itm_steel_greaves_wot, itm_gauntlets, itm_oniontop_bascinet_wot],
   def_attrib_wot_infantry_5 ,wp_polearm(195)|wp(150),knows_wot_infantry_5, arafel_man_face_young, arafel_man_face_older],

  ["kandor_militia_multi","Kandor Militia","Kandor Militia",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_one_handed_war_axe_b, itm_kandor_shield_normal, itm_kandor_leather_armor, itm_vaegir_fur_helmet, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2 ,wp_one_handed(100)|wp(70),knows_wot_infantry_2 ,kandor_man_face_young, kandor_man_face_older],
  ["kandor_axeman_multi","Kandor Axeman","Kandor Axemen",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_one_handed_battle_axe_c, itm_kandor_shield_strong, itm_kandor_surcoat, itm_mail_chausses, itm_mail_mittens, itm_vaegir_lamellar_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(120)|wp(100),knows_wot_infantry_3, kandor_man_face_young, kandor_man_face_older],
  ["kandor_berserker_multi","Kandor Berserker","Kandor Berserkers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_long_axe_b, itm_coat_of_plates, itm_plate_boots, itm_gauntlets, itm_visored_sallet],
   def_attrib_wot_infantry_4 ,wp_two_handed(150)|wp(100),knows_wot_infantry_4, kandor_man_face_young, kandor_man_face_older],
  ["kandor_captain_multi","Kandor Captain","Kandor Captains",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_long_axe_c, itm_coat_of_plates, itm_plate_boots, itm_gauntlets, itm_kandor_visored_sallet],
   def_attrib_wot_infantry_5 ,wp_two_handed(180)|wp(150),knows_wot_infantry_5, kandor_man_face_young, kandor_man_face_older],
  ["kandor_maceman_multi","Kandor Maceman","Kandor Macemen",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_kandor_long_mace,itm_kandor_surcoat, itm_mail_chausses, itm_mail_mittens, itm_vaegir_lamellar_helmet],
   def_attrib_wot_infantry_4 ,wp_two_handed(150)|wp(100),knows_wot_infantry_4, kandor_man_face_young, kandor_man_face_older],

  ["saldaea_militia_multi","Saldaea Militia","Saldaea Militia",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_sword_khergit_2, itm_saldaea_shield_normal, itm_saldaea_warrior_outfit, itm_nomad_cap_b, itm_hunter_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2 ,wp_one_handed(100)|wp(70),knows_wot_infantry_2 ,saldaea_man_face_young, saldaea_man_face_older],
  ["saldaea_swordsman_multi","Saldaea Swordsman","Saldaea Swordsmen",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_sword_khergit_3, itm_saldaea_shield_strong, itm_saldaea_army_armor, itm_leather_boots, itm_leather_gloves, itm_leather_steppe_cap_c],
   def_attrib_wot_infantry_3 ,wp_one_handed(120)|wp(100),knows_wot_infantry_3, saldaea_man_face_young, saldaea_man_face_older],
  ["saldaea_bannerman_multi","Saldaea Bannerman","Saldaea Bannermen",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_khergit_sword_two_handed_b, itm_heavy_lamellar_armor_wot, itm_khergit_cavalry_helmet, itm_splinted_greaves, itm_lamellar_gauntlets],
   def_attrib_wot_infantry_4 ,wp_two_handed(165)|wp(100),knows_wot_infantry_4, saldaea_man_face_young, saldaea_man_face_older],
  ["saldaea_halberdier_multi","Saldaea Halberdier","Saldaea Halberdiers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_poleaxe, itm_saldaea_army_armor, itm_leather_boots, itm_leather_gloves, itm_leather_steppe_cap_c],
   def_attrib_wot_infantry_4 ,wp_polearm(155)|wp(120),knows_wot_infantry_4, saldaea_man_face_young, saldaea_man_face_older],

#  ["nord_scout_multiplayer_ai","Nord Scout","Nord Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
#   [itm_javelin,itm_sword_viking_1,itm_two_handed_axe,itm_spear,itm_tab_shield_round_a,
#    itm_skullcap,itm_nordic_archer_helmet,itm_leather_jerkin,itm_leather_boots,itm_saddle_horse],
#   def_attrib|level(19),wp(100),knows_riding_5|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3,nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayer_ai","Shienar Light Cavalry","Shienar Light Cavalry",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_sword_medieval_b, itm_shienar_shield_weak, itm_shienar_leather_armor, itm_leather_boots, itm_leather_gloves, itm_skullcap, itm_courser],
   def_attrib_wot_cavalry_2 ,wp_one_handed(105)|wp(75),knows_wot_cavalry_2, shienar_man_face_young, shienar_man_face_older],
  ["shienar_lancer_multi","Shienar Lancer","Shienar Lancers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_lance, itm_shienar_shield_normal, itm_banded_armor, itm_steel_greaves_wot, itm_gauntlets, itm_nordic_warlord_helmet, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_3 ,wp_polearm(135)|wp_one_handed(110)|wp(85),knows_wot_cavalry_3 , shienar_man_face_young, shienar_man_face_older],
  ["shienar_heavy_lancer_multi","Shienar Heavy Lancer","Shienar Heavy Lancers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_heavy_lance, itm_shienar_shield_strong, itm_plate_armor, itm_steel_greaves_wot, itm_gauntlets, itm_great_helmet, itm_warhorse, itm_charger],
   def_attrib_wot_cavalry_4 ,wp_polearm(175)|wp_one_handed(150)|wp(85),knows_wot_cavalry_4 , shienar_man_face_young, shienar_man_face_older],
  ["shienar_captain_multi","Shienar Captain","Shienar Captains",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_heavy_lance, itm_shienar_shield_strong, itm_shienar_captain_armor, itm_steel_greaves_wot, itm_shienar_captain_gauntlets, itm_winged_great_helmet, itm_heavy_charger],
   def_attrib_wot_cavalry_5 ,wp_polearm(210)|wp_one_handed(175)|wp(150),knows_wot_cavalry_5 , shienar_man_face_young, shienar_man_face_older],
  
  ["arafel_man_at_arms_multi","Arafel Man at Arms","Arafel Man at Arms",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_mace_3, itm_shienar_shield_normal, itm_mamluke_mail, itm_mail_chausses, itm_leather_gloves, itm_segmented_helmet, itm_hunter],
   def_attrib_wot_cavalry_2 ,wp_one_handed(105)|wp(75),knows_wot_cavalry_2, arafel_man_face_young, arafel_man_face_older],
  ["arafel_lancer_multi","Arafel Lancer","Arafel Lancers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_lance, itm_arafel_shield_strong, itm_arafel_tabbard, itm_splinted_greaves_spurs_wot, itm_mail_mittens, itm_guard_helmet, itm_hunter, itm_warhorse],
   def_attrib_wot_cavalry_4 ,wp_polearm(150)|wp(75),knows_wot_cavalry_4, arafel_man_face_young, arafel_man_face_older],
  ["arafel_skirmisher_multi","Arafel Skirmisher","Arafel Skirmishers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_khergit_bow, itm_arrows, itm_sword_secondary, itm_mamluke_mail, itm_mail_chausses, itm_leather_gloves, itm_segmented_helmet, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_archery(165)|wp_one_handed(120)|wp(85),knows_wot_horse_archer_3 ,arafel_man_face_young, arafel_man_face_older],
  
  ["kandor_man_at_arms_multi","Kandor Man at Arms","Kandor Man at Arms",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_one_handed_battle_axe_b, itm_kandor_shield_normal, itm_kandor_army_armor, itm_splinted_leather_greaves, itm_leather_gloves, itm_vaegir_spiked_helmet, itm_hunter],
   def_attrib_wot_cavalry_2 ,wp_one_handed(105)|wp(75),knows_wot_cavalry_2, kandor_man_face_young, kandor_man_face_older],
  ["kandor_heavy_horseman_multi","Kandor Heavy Horseman","Kandor Heavy Horsemen",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_one_handed_battle_axe_c, itm_kandor_shield_strong, itm_kandor_surcoat, itm_mail_chausses, itm_mail_mittens, itm_vaegir_lamellar_helmet, itm_warhorse, itm_charger],
   def_attrib_wot_cavalry_4 ,wp_one_handed(165)|wp(125),knows_wot_cavalry_4, kandor_man_face_young, kandor_man_face_older],
  ["kandor_skirmisher_multi","Kandor Skirmisher","Kandor Skirmishers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_khergit_bow, itm_arrows, itm_sword_secondary, itm_kandor_army_armor, itm_splinted_leather_greaves, itm_leather_gloves, itm_vaegir_spiked_helmet, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_archery(165)|wp_one_handed(120)|wp(85),knows_wot_horse_archer_3 ,kandor_man_face_young, kandor_man_face_older],
  
  ["saldaea_cavalry_multi","Saldaea Cavalry","Saldaea Cavalry",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_sword_khergit_1, itm_saldaea_shield_weak, itm_saldaea_warrior_outfit, itm_nomad_cap_b, itm_hunter_boots, itm_leather_gloves, itm_steppe_horse],
   def_attrib_wot_cavalry_2 ,wp_one_handed(105)|wp(75),knows_wot_cavalry_2, saldaea_man_face_young, saldaea_man_face_older],
  ["saldaea_light_cavalry_multi","Saldaea Light Cavalry","Saldaea Light Cavalry",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_sword_khergit_2, itm_saldaea_shield_normal, itm_khergit_elite_armor, itm_khergit_war_helmet, itm_khergit_leather_boots, itm_scale_gauntlets, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_one_handed(130)|wp(100),knows_wot_cavalry_3, saldaea_man_face_young, saldaea_man_face_older],
  ["saldaea_elite_light_cavalry_multi","Saldaea Elite Light Cavalry","Draghkar",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_sword_khergit_3, itm_saldaea_shield_strong, itm_heavy_lamellar_armor_wot, itm_khergit_cavalry_helmet, itm_splinted_greaves, itm_lamellar_gauntlets, itm_saldaea_warhorse],
   def_attrib_wot_cavalry_4 ,wp_one_handed(155)|wp(100),knows_wot_cavalry_4, saldaea_man_face_young, saldaea_man_face_older],
  ["saldaea_skirmisher_multi","Saldaea Skirmisher","Saldaea Skirmishers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_khergit_bow, itm_arrows, itm_sword_secondary, itm_khergit_elite_armor, itm_khergit_war_helmet, itm_khergit_leather_boots, itm_scale_gauntlets, itm_courser],
   def_attrib_wot_cavalry_3 ,wp_archery(165)|wp_one_handed(120)|wp(85),knows_wot_horse_archer_3 ,saldaea_man_face_young, saldaea_man_face_older],
  ["saldaea_quartermaster_multi","Saldaea Squad Leader","Saldaea Squad Leaders",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_sword_khergit_4, itm_saldaea_shield_strong, itm_vaegir_elite_armor, itm_khergit_guard_helmet, itm_splinted_greaves, itm_lamellar_gauntlets, itm_saldaea_charger],
   def_attrib_wot_cavalry_5 ,wp_one_handed(180)|wp(125),knows_wot_cavalry_5, saldaea_man_face_young, saldaea_man_face_older],
  ["saldaea_elite_skirmisher_multi","Saldaea Elite Skirmisher","Saldaea Elite Skirmishers",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_khergit_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_sword_secondary, itm_heavy_lamellar_armor_wot, itm_khergit_cavalry_helmet, itm_splinted_greaves, itm_lamellar_gauntlets, itm_saldaea_warhorse],
   def_attrib_wot_cavalry_4 ,wp_archery(180)|wp_one_handed(150)|wp(85),knows_wot_horse_archer_4 ,saldaea_man_face_young, saldaea_man_face_older],

#  ["nord_archer_multiplayer_ai","Nord Archer","Nord Archers",tf_guarantee_all,0,0,fac_kingdom_4,
#   [itm_arrows,itm_two_handed_axe,itm_sword_viking_2,itm_short_bow,
#    itm_leather_jerkin,itm_blue_tunic,itm_leather_boots,itm_nasal_helmet,itm_leather_cap],
#   def_attrib|str_11|level(19),wp_melee(80)|wp_archery(110),knows_ironflesh_4|knows_power_strike_2|knows_shield_1|knows_power_draw_5|knows_athletics_6,nord_face_young_1, nord_face_old_2],
  ["nord_archer_multiplayer_ai","Shienar Bowman","Shienar Bowmen",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_strong_bow, itm_arrows, itm_sword_secondary, itm_shienar_leather_armor, itm_leather_boots, itm_leather_gloves, itm_skullcap],
   def_attrib_wot_infantry_3 ,wp_archery(130)|wp_one_handed(120)|wp(80),knows_wot_archer_3, shienar_man_face_young, shienar_man_face_older],
  ["shienar_marksman_multi","Shienar Marksman","Shienar Marksmen",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_war_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_sword_secondary, itm_mail_shirt, itm_mail_chausses, itm_leather_gloves, itm_nordic_fighter_helmet],
   def_attrib_wot_infantry_4 ,wp_archery(165)|wp_one_handed(140)|wp(120),knows_wot_archer_4, shienar_man_face_young, shienar_man_face_older],
  ["shienar_crossbowman_multi","Shienar Crossbowman","Shienar Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_crossbow, itm_bolts, itm_sword_secondary, itm_shienar_shield_weak, itm_mail_shirt, itm_mail_chausses, itm_leather_gloves, itm_nordic_fighter_helmet],
   def_attrib_wot_infantry_4 ,wp_crossbow(165)|wp_one_handed(135)|wp(120),knows_wot_archer_4, shienar_man_face_young, shienar_man_face_older],

  ["arafel_bowman_multi","Arafel Bowman","Arafel Bowmen",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_strong_bow, itm_arrows, itm_sword_secondary, itm_arafel_army_armor, itm_mail_coif, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_3 ,wp_archery(130)|wp_one_handed(115)|wp(80),knows_wot_archer_3, arafel_man_face_young, arafel_man_face_older],
  ["arafel_marksman_multi","Arafel Marksman","Arafel Marksmen",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_war_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_sword_secondary, itm_mamluke_mail, itm_mail_chausses, itm_leather_gloves, itm_segmented_helmet],
   def_attrib_wot_infantry_4 ,wp_archery(165)|wp_one_handed(140)|wp(120),knows_wot_archer_4, arafel_man_face_young, arafel_man_face_older],

  ["kandor_bowman_multi","Kandor Bowman","Kandor Bowmen",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_nomad_bow, itm_arrows, itm_sword_secondary, itm_kandor_leather_armor, itm_vaegir_fur_helmet, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_3 ,wp_archery(130)|wp_one_handed(125)|wp(80),knows_wot_archer_3, kandor_man_face_young, kandor_man_face_older],
   ["kandor_crossbowman_multi","Kandor Crossbowman","Kandor Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_crossbow, itm_bolts, itm_sword_secondary, itm_kandor_shield_weak, itm_kandor_leather_armor, itm_vaegir_fur_helmet, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_4 ,wp_crossbow(165)|wp_one_handed(130)|wp(120),knows_wot_archer_4, kandor_man_face_young, kandor_man_face_older],

  ["saldaea_bowman_multi","Saldaea Bowman","Saldaea Bowmen",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_nomad_bow, itm_arrows, itm_sword_secondary, itm_saldaea_warrior_outfit, itm_nomad_cap_b, itm_hunter_boots, itm_leather_gloves],
   def_attrib_wot_infantry_3 ,wp_archery(130)|wp_one_handed(120)|wp(80),knows_wot_archer_3, saldaea_man_face_young, saldaea_man_face_older],
  ["saldaea_marksman_multi","Saldaea Marksman","Saldaea Marksmen",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_war_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_sword_secondary, itm_saldaea_army_armor, itm_leather_boots, itm_leather_gloves, itm_leather_steppe_cap_c],
   def_attrib_wot_infantry_4 ,wp_archery(165)|wp_one_handed(150)|wp(120),knows_wot_archer_4, saldaea_man_face_young, saldaea_man_face_older],

  #################
#  ["rhodok_veteran_crossbowman_multiplayer_ai","Rhodok Crossbowman","Rhodok Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
#   [itm_fighting_pick,itm_club_with_spike_head,itm_maul,itm_tab_shield_pavise_c,itm_heavy_crossbow,itm_bolts,
#    itm_leather_cap,itm_padded_leather,itm_nomad_boots],
#   def_attrib|level(19),wp_melee(100)|wp_crossbow(120),knows_common|knows_ironflesh_4|knows_shield_5|knows_power_strike_3|knows_athletics_6,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_veteran_crossbowman_multiplayer_ai","Novice","Novices",tf_female|tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_power_player, itm_power_ammo, itm_channeler_dagger, itm_novice_dress, itm_novice_accepted_damane_shoes], # , itm_wig_brown_ponytail
   def_attrib|level(5),wp_firearm(100)|wp_one_handed(90)|wp(70),knows_common|knows_power_draw_2,tar_valon_woman_face_younger, tear_woman_face_middle],
  ["accepted_medical_multi","Accepted","Accepted",tf_female|tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_power_player, itm_power_ammo, itm_accepted_dress, itm_novice_accepted_damane_shoes], # , itm_wig_blond_longer
   def_attrib|level(10),wp_firearm(120)|wp_one_handed(110)|wp(75),knows_common|knows_power_draw_2,tar_valon_woman_face_younger, far_madding_woman_face_middle],
  ["aes_sedai_white_multi","Aes Sedai White","Aes Sedai Whites",tf_female|tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_white_dress, itm_aes_sedai_white_shoes], # , itm_wig_black_long
   def_attrib|level(15),wp_firearm(150)|wp_one_handed(110)|wp(80),knows_common|knows_power_draw_3,tar_valon_woman_face_young, ghealdan_woman_face_old],
  ["aes_sedai_grey_multi","Aes Sedai Grey","Aes Sedai Greys",tf_female|tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_grey_dress, itm_aes_sedai_grey_shoes], # , itm_wig_red_braid
   def_attrib|level(15),wp_firearm(150)|wp_one_handed(110)|wp(80),knows_common|knows_power_draw_3,tar_valon_woman_face_young, saldaea_woman_face_old],
  ["aes_sedai_red_multi","Aes Sedai Red","Aes Sedai Reds",tf_female|tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_red_dress, itm_aes_sedai_red_shoes], # , itm_wig_brown_bun
   def_attrib|level(15),wp_firearm(150)|wp_one_handed(110)|wp(80),knows_common|knows_power_draw_3,tar_valon_woman_face_young, arafel_woman_face_old],
  ["tower_guard_crossbowman_multi","Tower Guard Crossbowman","Tower Guard Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_crossbow, itm_bolts, itm_sword_medieval_a, itm_white_tower_guard_armor, itm_segmented_helmet, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2 ,wp_crossbow(125)|wp_one_handed(110)|wp(90),knows_wot_archer_2 ,tar_valon_man_face_young, tar_valon_man_face_old],

#  ["rhodok_veteran_spearman_multiplayer_ai","Rhodok Spearman","Rhodok Spearmen",tf_guarantee_all_wo_ranged,0,0,fac_kingdom_5,
#   [itm_ashwood_pike,itm_war_spear,itm_pike,itm_club_with_spike_head,itm_sledgehammer,itm_tab_shield_pavise_c,itm_sword_medieval_a,
#    itm_leather_cap,itm_byrnie,itm_ragged_outfit,itm_nomad_boots],
#   def_attrib|level(19),wp(115),knows_common|knows_ironflesh_5|knows_shield_3|knows_power_strike_4|knows_athletics_3,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_veteran_spearman_multiplayer_ai","Tar Valon Street Patrol","Tar Valon Street Patrols",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_street_patrol_club, itm_white_tower_patrol_tunic, itm_norman_helmet, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_1 ,wp_one_handed(100)|wp(70),knows_wot_infantry_1 ,tar_valon_man_face_young, tar_valon_man_face_old],
  ["tower_guard_infantry_multi","Tower Guard Infantry","Tower Guard Infantry",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_spiked_mace, itm_steel_buckler2, itm_white_tower_guard_armor, itm_segmented_helmet, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2,wp_one_handed(125)|wp(90),knows_wot_infantry_2,tar_valon_man_face_young, tar_valon_man_face_old],
  ["warder_trainee_multi","Warder Trainee","Warder Trainees",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_sword_viking_2_small, itm_arena_tunic_white, itm_norman_helmet, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_1,wp_one_handed(100)|wp(70),knows_wot_infantry_1,tar_valon_man_face_young, tar_valon_man_face_old],
  ["tower_guard_captain_multi","Tower Guard Captain","Tower Guard Captains",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_great_sword, itm_sword_viking_2_small, itm_white_tower_captain_armor, itm_guard_helmet, itm_splinted_leather_greaves, itm_leather_gloves],
   def_attrib_wot_infantry_3,wp_one_handed(150)|wp(100),knows_wot_infantry_3,tar_valon_man_face_middle, tar_valon_man_face_older],
  ["youngling_infantry_multi","Youngling Infantry","Youngling Infantry",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_sword_viking_3_small, itm_trainee_gambeson, itm_segmented_helmet, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2 ,wp_one_handed(125)|wp(90),knows_wot_infantry_2 ,tar_valon_man_face_younger, tar_valon_man_face_young],
  ["warder_multi","Warder","Warders",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_great_sword, itm_sarranid_elite_armor, itm_vaegir_war_helmet, itm_splinted_leather_greaves, itm_scale_gauntlets],
   def_attrib_wot_infantry_4 ,wp_two_handed(150)|wp(90),knows_wot_infantry_4 ,tar_valon_man_face_young, andor_man_face_old],
  
  
#  ["rhodok_scout_multiplayer_ai","Rhodok Scout","Rhodok Scouts",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_5,
   #TODO: Change weapons, copied from Nord Scout
#   [itm_javelin,itm_sword_viking_1,itm_two_handed_axe,itm_spear,itm_tab_shield_round_a,
#    itm_skullcap,itm_leather_jerkin,itm_leather_boots,itm_saddle_horse],
#   def_attrib|level(19),wp(100),knows_riding_5|knows_ironflesh_2|knows_power_strike_2|knows_shield_1|knows_horse_archery_2|knows_power_throw_3,rhodok_face_young_1, rhodok_face_older_2],
  ["rhodok_scout_multiplayer_ai","Aes Sedai Yellow Veteran","Aes Sedai Yellow Veterans",tf_female|tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_yellow_dress, itm_veteran_aes_sedai_yellow_shoes, itm_courser], # , itm_wig_black_bun
   def_attrib|level(20),wp_firearm(200)|wp_one_handed(110)|wp(90),knows_common|knows_power_draw_3|knows_riding_2,tar_valon_woman_face_middle, cairhien_woman_face_older],
  ["aes_sedai_brown_veteran_multi","Aes Sedai Brown Veteran","Aes Sedai Brown Veterans",tf_female|tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_brown_dress, itm_veteran_aes_sedai_brown_shoes, itm_courser], # , itm_wig_brown_bun
   def_attrib|level(20),wp_firearm(200)|wp_one_handed(110)|wp(90),knows_common|knows_power_draw_3|knows_riding_2,tar_valon_woman_face_middle, andor_woman_face_older],
  ["aes_sedai_blue_veteran_multi","Aes Sedai Blue Veteran","Aes Sedai Blue Veterans",tf_female|tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_blue_dress, itm_veteran_aes_sedai_blue_shoes, itm_courser], # , itm_wig_white_longer
   def_attrib|level(20),wp_firearm(200)|wp_one_handed(110)|wp(90),knows_common|knows_power_draw_3|knows_riding_2,tar_valon_woman_face_middle, aiel_2_woman_face_older],
  ["aes_sedai_green_veteran_multi","Aes Sedai Green Veteran","Aes Sedai Green Veterans",tf_female|tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_green_dress, itm_veteran_aes_sedai_green_shoes, itm_courser], # , itm_wig_red_long
   def_attrib|level(20),wp_firearm(200)|wp_one_handed(110)|wp(90),knows_common|knows_power_draw_3|knows_riding_2,tar_valon_woman_face_middle, saldaea_woman_face_older],
  ["warder_veteran_multi","Warder Veteran","Warder Veterans",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_great_sword, itm_sword_viking_2_small, itm_khergit_elite_armor, itm_khergit_guard_helmet, itm_splinted_greaves, itm_lamellar_gauntlets,itm_hunter],
   def_attrib_wot_cavalry_4 ,wp_one_handed(150)|wp_two_handed(175)|wp(100),knows_wot_cavalry_4 ,tar_valon_man_face_middle, shienar_man_face_older],
  ["youngling_cavalry_multi","Youngling Cavalry","Youngling Cavalry",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_lance, itm_sword_viking_3_small, itm_trainee_gambeson, itm_segmented_helmet, itm_leather_boots, itm_leather_gloves,itm_courser],
   def_attrib_wot_cavalry_2,wp_one_handed(115)|wp_polearm(125)|wp(90),knows_wot_cavalry_2,tar_valon_man_face_younger, tar_valon_man_face_young],


  #################
#  ["sarranid_infantry_multiplayer_ai","Sarranid Infantry","Sarranid Infantries",tf_guarantee_shield|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet,0,0,fac_kingdom_6,
#   [itm_sarranid_mail_shirt,itm_sarranid_horseman_helmet,itm_sarranid_boots_b,itm_sarranid_boots_c,itm_splinted_leather_greaves,itm_arabian_sword_b,itm_mace_3,itm_spear,itm_tab_shield_kite_c],
#   def_attrib|level(20),wp_melee(105),knows_common|knows_riding_3|knows_ironflesh_2|knows_shield_3,swadian_face_middle_1, swadian_face_old_2],
  ["sarranid_infantry_multiplayer_ai","Aiel Recruit (Lithe)","Aiel Recruits (Lithe)",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_aiel_spear, itm_hide_buckler_weak, itm_cadinsor_grey, itm_shoufa_grey, itm_cadinsor_boots_grey],
   def_attrib_wot_super_infantry_2 ,wp_polearm(110)|wp(70),knows_wot_super_infantry_2 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  ["aiel_raider_multi","Aiel Raider","Aiel Raiders",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_aiel_spear, itm_hide_buckler_normal, itm_cadinsor_green, itm_shoufa_green, itm_cadinsor_boots_green],
   def_attrib_wot_super_infantry_3 ,wp_polearm(145)|wp(90),knows_wot_super_infantry_3 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  ["aiel_recruit_athletic_multi","Aiel Recruit (Athletic)","Aiel Recruits (Athletic)",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_aiel_spear, itm_cadinsor_grey, itm_shoufa_grey, itm_cadinsor_boots_grey],
   def_attrib_wot_super_infantry_2 ,wp_polearm(115)|wp(70),knows_wot_super_infantry_2 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  ["aiel_runner_multi","Aiel Runner","Aiel Runners",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_aiel_spear, itm_cadinsor_green, itm_shoufa_green, itm_cadinsor_boots_green],
   def_attrib_wot_super_infantry_3 ,wp_polearm(145)|wp(90),knows_wot_super_infantry_3 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  ["aiel_recruit_bulky_multi","Aiel Recruit (Bulky)","Aiel Recruits (Bulky)",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_aiel_spear, itm_hide_buckler_weak, itm_cadinsor_grey, itm_shoufa_grey, itm_cadinsor_boots_grey],
   def_attrib_wot_super_infantry_3 ,wp_polearm(125)|wp(70),knows_wot_super_infantry_3 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  ["aiel_enforcer_multi","Aiel Enforcer","Aiel Enforcers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_aiel_spear, itm_hide_buckler_normal, itm_cadinsor_green, itm_shoufa_green, itm_cadinsor_boots_green],
   def_attrib_wot_super_infantry_4 ,wp_polearm(165)|wp(120),knows_wot_super_infantry_4 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  ["aiel_recruit_warrior_multi","Aiel Recruit (Warrior)","Aiel Recruits (Warrior)",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_aiel_spear, itm_hide_buckler_weak, itm_cadinsor_grey, itm_shoufa_grey, itm_cadinsor_boots_grey],
   def_attrib_wot_super_infantry_3 ,wp_polearm(125)|wp(70),knows_wot_super_infantry_3 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  ["aiel_brute_multi","Aiel Brute","Aiel Brutes",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_aiel_spear, itm_aiel_knife, itm_cadinsor_green, itm_shoufa_green, itm_cadinsor_boots_green],
   def_attrib_wot_super_infantry_4 ,wp_polearm(165)|wp_one_handed(145)|wp(120),knows_wot_super_infantry_4 ,aiel_1_man_face_younger, aiel_2_man_face_old],

#  ["sarranid_archer_multiplayer_ai","Sarranid Archer","Sarranid Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_6,
#   [itm_arrows,itm_nomad_bow,itm_arabian_sword_a,itm_archers_vest,itm_sarranid_boots_b,itm_sarranid_helmet1,itm_turban,itm_desert_turban],
#   def_attrib|level(19),wp_melee(90)|wp_archery(100),knows_common|knows_riding_2|knows_ironflesh_1,swadian_face_young_1, swadian_face_old_2],
  ["sarranid_archer_multiplayer_ai","Wise One Apprentice","Wise One Apprentices",tf_female|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_power_player, itm_power_ammo, itm_wise_one_dress, itm_cadinsor_boots],
  def_attrib|level(10),wp_firearm(120)|wp_one_handed(110)|wp(75),knows_common|knows_power_draw_2, aiel_1_woman_face_younger, aiel_2_woman_face_middle],
  ["wise_one_multi","Wise One","Wise Ones",tf_female|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_power_player, itm_power_ammo, itm_wise_one_dress_with_shawl, itm_cadinsor_boots],
   def_attrib|level(16),wp_firearm(150)|wp_one_handed(110)|wp(80),knows_common|knows_power_draw_3, aiel_1_woman_face_young, aiel_2_woman_face_old],
  ["aiel_scout_multi","Aiel Scout","Aiel Scouts",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_nomad_bow, itm_arrows, itm_aiel_spear, itm_cadinsor_green, itm_shoufa_green, itm_cadinsor_boots_green],
   def_attrib_wot_super_infantry_3 ,wp_archery(145)|wp_polearm(130)|wp(90),knows_wot_super_infantry_3 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  ["aiel_grappler_multi","Aiel Grappler","Aiel Grapplers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_nomad_bow, itm_arrows, itm_aiel_knife, itm_cadinsor_green, itm_shoufa_green, itm_cadinsor_boots_green],
   def_attrib_wot_super_infantry_4 ,wp_archery(165)|wp_one_handed(145)|wp(120),knows_wot_super_infantry_4 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  ["wise_one_dream_walker_multi","Wise One Dream Walker","Wise One Dream Walkers",tf_female|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_power_player, itm_power_ammo, itm_wise_one_dress_with_shawl, itm_cadinsor_boots],
   def_attrib|level(20),wp_firearm(200)|wp_one_handed(125)|wp(90),knows_common|knows_power_draw_3, aiel_1_woman_face_middle, aiel_2_woman_face_older],
  ["maiden_of_the_spear_multi","Maiden of the Spear","Maidens of the Spear",tf_female|tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_khergit_bow, itm_arrows, itm_arrows, itm_aiel_knife, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_4 ,wp_archery(190)|wp_one_handed(140)|wp(120),knows_wot_super_infantry_4 ,aiel_1_woman_face_younger, aiel_2_woman_face_old],
  ["water_seeker_multi","Water Seeker","Water Seekers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_khergit_bow, itm_arrows, itm_arrows, itm_aiel_spear, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_4 ,wp_archery(190)|wp_polearm(140)|wp(120),knows_wot_super_infantry_4 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  ["brother_of_the_eagle_multi","Brother of the Eagle","Brothers of the Eagle",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_khergit_bow, itm_arrows, itm_arrows, itm_aiel_knife, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_5 ,wp_archery(195)|wp_one_handed(160)|wp(130),knows_wot_super_infantry_5 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  ["true_blood_multi","True Blood","True Bloods",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_khergit_bow, itm_arrows, itm_arrows, itm_aiel_spear, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_5 ,wp_archery(195)|wp_polearm(160)|wp(130),knows_wot_super_infantry_5 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  
#  ["sarranid_horseman_multiplayer_ai","Sarranid Horseman","Sarranid Horsemen",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_6,
#   [itm_lance,itm_arabian_sword_b,itm_scimitar_b,itm_mace_4,itm_tab_shield_small_round_b,
#    itm_sarranid_mail_shirt,itm_sarranid_boots_b,itm_sarranid_boots_c,itm_sarranid_horseman_helmet,itm_courser,itm_hunter],
#   def_attrib|level(20),wp_melee(100),knows_common|knows_riding_4|knows_ironflesh_2|knows_shield_2|knows_power_strike_3,swadian_face_young_1, swadian_face_old_2],
  ["sarranid_horseman_multiplayer_ai","Knife Hand","Knife Hands",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_aiel_knife, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_4 ,wp_one_handed(185)|wp(120),knows_wot_super_infantry_4 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  ["night_spear_multi","Night Spear","Night Spears",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_aiel_spear, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_4 ,wp_polearm(190)|wp(120),knows_wot_super_infantry_4 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  ["dawn_runner_multi","Dawn Runner","Dawn Runners",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_aiel_spear, itm_aiel_knife, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_4 ,wp_polearm(190)|wp_one_handed(140)|wp(120),knows_wot_super_infantry_4 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  ["mountain_dancer_multi","Mountain Dancer","Mountain Dancers",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_aiel_spear, itm_hide_buckler_strong, itm_aiel_knife, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_4 ,wp_polearm(190)|wp_one_handed(140)|wp(120),knows_wot_super_infantry_4 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  ["stone_dog_multi","Stone Dog","Stone Dogs",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_javelin, itm_aiel_spear, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_5 ,wp_throwing(190)|wp_polearm(175)|wp(120),knows_wot_super_infantry_5 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  ["red_shield_multi","Red Shield","Red Shields",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_aiel_spear, itm_hide_buckler_strong, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_5 ,wp_polearm(190)|wp(120),knows_wot_super_infantry_5 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  ["brotherless_multi","Brotherless","Brotherless",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_aiel_spear, itm_hide_buckler_strong, itm_aiel_knife, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_5 ,wp_polearm(200)|wp_one_handed(160)|wp(130),knows_wot_super_infantry_5 ,aiel_1_man_face_younger, aiel_2_man_face_old],
  ["black_eye_multi","Black Eye","Black Eyes",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_javelin, itm_aiel_spear, itm_hide_buckler_strong, itm_cadinsor, itm_shoufa, itm_cadinsor_boots],
   def_attrib_wot_super_infantry_5 ,wp_throwing(185)|wp_polearm(160)|wp(130),knows_wot_super_infantry_5 ,aiel_1_man_face_younger, aiel_2_man_face_old],

  #######################
  ["seanchan_archer_multiplayer_ai","Sul'dam","Sul'dam",tf_female|tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_suldam_dagger, itm_suldam_dress, itm_suldam_boots],
   def_attrib_wot_infantry_2,wp_one_handed(125)|wp(90),knows_wot_infantry_2,seanchan_1_woman_face_younger, seanchan_2_woman_face_old],
  ["seanchan_bowman_multi","Seanchan Archer","Seanchan Archers",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_strong_bow, itm_arrows, itm_seanchan_straight_sword, itm_seanchan_low_armor, itm_seanchan_low_helmet, itm_seanchan_low_boots, itm_seanchan_low_gloves],
   def_attrib_wot_infantry_2,wp_archery(105)|wp_one_handed(100)|wp(90),knows_wot_archer_2, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  ["der_suldam_multi","Der Sul'dam","Der Sul'dam",tf_female|tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_der_suldam_dagger, itm_suldam_dress, itm_suldam_boots],
   def_attrib_wot_infantry_3,wp_one_handed(135)|wp(90),knows_wot_infantry_3,seanchan_1_woman_face_younger, seanchan_2_woman_face_older],
  ["damane_multi","Damane","Damane",tf_female|tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_power_player, itm_power_ammo, itm_damane_dress, itm_damane_boots],
   def_attrib|level(18),wp_firearm(190)|wp_one_handed(110)|wp(90),knows_common|knows_power_draw_3|knows_riding_2, seanchan_1_woman_face_younger, seanchan_2_woman_face_older],
  ["seanchan_marksman_multi","Seanchan Marksman","Seanchan Marksmen",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_war_bow, itm_arrows, itm_arrows, itm_seanchan_sword, itm_seanchan_middle_armor, itm_seanchan_middle_helmet, itm_seanchan_middle_boots, itm_seanchan_middle_gloves],
   def_attrib_wot_infantry_4,wp_archery(165)|wp_two_handed(130)|wp(100),knows_wot_infantry_4, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  ["seanchan_crossbowman_multi","Seanchan Crossbowman","Seanchan Crossbowmen",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_crossbow, itm_bolts, itm_seanchan_straight_sword, itm_seanchan_low_armor, itm_seanchan_low_helmet, itm_seanchan_low_boots, itm_seanchan_low_gloves],
   def_attrib_wot_infantry_3,wp_crossbow(135)|wp_one_handed(110)|wp(90),knows_wot_archer_3, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  
  ["seanchan_infantry_multiplayer_ai","Seanchan Armsman","Seanchan Armsmen",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_seanchan_straight_sword, itm_blue_gambeson, itm_leather_warrior_cap, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_1,wp_one_handed(85)|wp(70),knows_wot_infantry_1, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  ["seanchan_footman_multi","Seanchan Footman","Seanchan Footmen",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_seanchan_straight_sword, itm_seanchan_low_armor, itm_seanchan_low_helmet, itm_seanchan_low_boots, itm_seanchan_low_gloves],
   def_attrib_wot_infantry_2,wp_one_handed(100)|wp(90),knows_wot_infantry_2, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  ["seanchan_swordsman_multi","Seanchan Swordsman","Seanchan Swordsmen",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_seanchan_sword, itm_seanchan_middle_armor, itm_seanchan_middle_helmet, itm_seanchan_middle_boots, itm_seanchan_middle_gloves],
   def_attrib_wot_infantry_3,wp_two_handed(130)|wp(100),knows_wot_infantry_3, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  ["seanchan_blademaster_multi","Seanchan Blademaster","Seanchan Blademasters",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_seanchan_large_sword, itm_seanchan_high_armor, itm_seanchan_high_helmet, itm_seanchan_high_boots, itm_seanchan_high_gloves],
   def_attrib_wot_infantry_4,wp_two_handed(150)|wp(120),knows_wot_infantry_4, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  ["seanchan_pikeman_multi","Seanchan Pikeman","Seanchan Pikemen",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_pike, itm_seanchan_middle_armor, itm_seanchan_middle_helmet, itm_seanchan_middle_boots, itm_seanchan_middle_gloves],
   def_attrib_wot_infantry_3,wp_polearm(130)|wp(100),knows_wot_infantry_3, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  ["seanchan_deathwatch_guard_multi","Seanchan Deathwatch Guard","Seanchan Deathwatch Guards",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_seanchan_large_sword, itm_deathwatch_guard_armor, itm_deathwatch_guard_helmet, itm_deathwatch_guard_boots, itm_deathwatch_guard_gloves],
   def_attrib_wot_infantry_5,wp_two_handed(200)|wp(175),knows_wot_infantry_5, seanchan_1_man_face_middle, seanchan_2_man_face_older],
  ["seanchan_halberdier_multi","Seanchan Halberdier","Seanchan Halberdiers",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_hafted_blade_a, itm_seanchan_high_armor, itm_seanchan_high_helmet, itm_seanchan_high_boots, itm_seanchan_high_gloves],
   def_attrib_wot_infantry_4,wp_polearm(150)|wp(120),knows_wot_infantry_4, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  
  ["seanchan_horseman_multiplayer_ai","Seanchan Scout","Seanchan Scouts",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_seanchan_straight_sword, itm_blue_gambeson, itm_leather_warrior_cap, itm_leather_boots, itm_leather_gloves, itm_saddle_horse],
   def_attrib_wot_cavalry_2,wp_one_handed(95)|wp(70),knows_wot_cavalry_2, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  ["seanchan_man_at_arms_multi","Seanchan Man at Arms","Seanchan Men at Arms",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_seanchan_straight_sword, itm_seanchan_low_armor, itm_seanchan_low_helmet, itm_seanchan_low_boots, itm_seanchan_low_gloves, itm_arabian_horse_a],
   def_attrib_wot_cavalry_3,wp_one_handed(125)|wp(90),knows_wot_cavalry_3, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  ["seanchan_lancer_multi","Seanchan Lancer","Seanchan Lancers",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_lance, itm_seanchan_middle_armor, itm_seanchan_middle_helmet, itm_seanchan_middle_boots, itm_seanchan_middle_gloves, itm_arabian_horse_b],
   def_attrib_wot_cavalry_4,wp_polearm(145)|wp(100),knows_wot_cavalry_4, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  ["seanchan_captain_multi","Seanchan Captain","Seanchan Captains",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_glaive, itm_seanchan_high_armor, itm_seanchan_high_helmet, itm_seanchan_high_boots, itm_seanchan_high_gloves, itm_hunter],
   def_attrib_wot_cavalry_5,wp_polearm(190)|wp(145),knows_wot_cavalry_5, seanchan_1_man_face_younger, seanchan_2_man_face_older],
  ["seanchan_skirmisher_multi","Seanchan Skirmisher","Seanchan Skirmishers",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_khergit_bow, itm_arrows, itm_seanchan_straight_sword, itm_seanchan_middle_armor, itm_seanchan_middle_helmet, itm_seanchan_middle_boots, itm_seanchan_middle_gloves, itm_courser],
   def_attrib_wot_cavalry_4 ,wp_archery(180)|wp_one_handed(150)|wp(85),knows_wot_horse_archer_4, seanchan_1_man_face_younger, seanchan_2_man_face_older],


  ####################
  ["shadowspawn_infantry_multiplayer_ai","Trolloc Grunt","Trolloc Grunts",tf_trolloc|tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_military_fork,itm_trolloc_hawk_helmet, itm_trolloc_weak_armor, itm_black_mail_gauntlets, itm_black_leather_boots],
    def_attrib_wot_super_infantry_2 ,wp_polearm(110)|wp(70),knows_wot_super_infantry_2,man_face_young_1, man_face_old_2],
  ["trolloc_hewer_multi","Trolloc Hewer","Trolloc Hewers",tf_trolloc|tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_two_handed_axe,itm_trolloc_goat_helmet, itm_trolloc_normal_armor, itm_black_mail_gauntlets, itm_black_leather_boots],
    def_attrib_wot_super_infantry_3 ,wp_two_handed(145)|wp(110),knows_wot_super_infantry_3,man_face_young_1, man_face_old_2],
  ["trolloc_berserker_multi","Trolloc Berserker","Trolloc Berserker",tf_trolloc|tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_trolloc_mace,itm_trolloc_goat_helmet, itm_trolloc_normal_armor, itm_black_mail_gauntlets, itm_black_leather_boots],
    def_attrib_wot_super_infantry_4 ,wp_two_handed(190)|wp(140),knows_wot_super_infantry_4,man_face_young_1, man_face_old_2],
  ["trolloc_clan_chief_multi","Trolloc Clan Chief","Trolloc Clan Chiefs",tf_trolloc|tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_great_long_bardiche,itm_trolloc_wolf_helmet, itm_trolloc_strong_armor, itm_black_mail_gauntlets, itm_black_leather_boots],
    def_attrib_wot_super_infantry_5 ,wp_polearm(250)|wp(200),knows_wot_super_infantry_5,man_face_young_1, man_face_old_2],
  ["darkfriend_initiate_multi","Darkfriend Initiate","Darkfriends Initiates",tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_mace_3, itm_darkfriend_shield_weak, itm_darkfriend_tunic, itm_skullcap, itm_leather_boots, itm_leather_gloves],
   def_attrib_wot_infantry_2,wp_one_handed(100)|wp(90),knows_wot_infantry_2, man_face_young_1, man_face_old_2],
  ["darkfriend_murderer_multi","Darkfriend Murderer","Darkfriend Murderers",tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_sword_viking_3, itm_darkfriend_shield_normal, itm_darkfriend_armor, itm_leather_boots, itm_mail_mittens, itm_guard_helmet],
   def_attrib_wot_infantry_3 ,wp_one_handed(120)|wp(100),knows_wot_infantry_3, man_face_young_1, man_face_old_2],
  ["darkfriend_ambusher_multi","Darkfriend Ambushers","Darkfriend Ambushers",tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_sword_viking_3, itm_darkfriend_shield_normal, itm_darkfriend_armor, itm_leather_boots, itm_mail_mittens, itm_guard_helmet, itm_saddle_horse],
   def_attrib_wot_cavalry_2 ,wp_one_handed(105)|wp(75),knows_wot_cavalry_2, man_face_young_1, man_face_old_2],
  ["darkfriend_assassin_multi","Darkfriend Assassin","Darkfriend Assassins",tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_great_sword, itm_darkfriend_plate, itm_black_leather_boots, itm_black_mail_gauntlets, itm_bascinet_3],
   def_attrib_wot_infantry_4 ,wp_two_handed(155)|wp(100),knows_wot_infantry_4, man_face_young_1, man_face_old_2],
  
  ["shadowspawn_archer_multiplayer_ai","Trolloc Archer","Trolloc Archers",tf_trolloc|tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_war_bow,itm_arrows, itm_sword_secondary, itm_trolloc_hawk_helmet, itm_trolloc_weak_armor, itm_black_mail_gauntlets, itm_black_leather_boots],
    def_attrib_wot_super_infantry_2 ,wp_archery(110)|wp_one_handed(100)|wp(70),knows_wot_super_infantry_2,man_face_young_1, man_face_old_2],
  ["trolloc_stalker_multi","Trolloc Stalker","Trolloc Stalkers",tf_trolloc|tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_strong_bow,itm_arrows,itm_arrows, itm_sword_secondary, itm_trolloc_goat_helmet, itm_trolloc_weak_armor, itm_black_mail_gauntlets, itm_black_leather_boots],
    def_attrib_wot_super_infantry_4 ,wp_archery(175)|wp_one_handed(145)|wp(70),knows_wot_super_infantry_4,man_face_young_1, man_face_old_2],
  ["darkfriend_channeler_multi","Darkfriend Channeler","Darkfriend Channelers",tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_power_player, itm_power_ammo, itm_sword_secondary, itm_darkfriend_tunic, itm_leather_boots],
   def_attrib_wot_infantry_1,wp_firearm(105)|wp_one_handed(100)|wp(75),knows_wot_infantry_1|knows_power_draw_2,man_face_young_1, man_face_old_2],
  ["aes_sedai_black_multi","Aes Sedai Black","Aes Sedai Blacks",tf_female|tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_power_player, itm_power_ammo, itm_aes_sedai_black_ajah_dress, itm_aes_sedai_black_ajah_shoes], # , itm_wig_brown_bun
   def_attrib|level(15),wp_firearm(150)|wp_one_handed(110)|wp(80),knows_common|knows_power_draw_3,woman_face_1, woman_face_2],
  ["draghkar_multi","Draghkar","Draghkar",tf_myrddraal|tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_draghkar_dagger, itm_draghkar_tunic, itm_draghkar_helmet, itm_black_leather_boots, itm_draghkar_gloves],
   str_10|agi_7|int_5|cha_5|level(20),wp_one_handed(100)|wp(90),knows_wot_infantry_2, man_face_young_1, man_face_old_2],
  ["dreadlord_multi","Dreadlord","Dreadlords",tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_power_player, itm_power_ammo, itm_dreadlord_coat, itm_black_leather_boots, itm_saddle_horse],
   def_attrib_wot_infantry_3,wp_firearm(200)|wp_one_handed(150)|wp(125),knows_wot_infantry_3|knows_power_draw_5,man_face_young_1, man_face_old_2],
  ["darkfriend_marksman_multi","Darkfriend Marksman","Darkfriend Marksmen",tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_strong_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_sword_secondary, itm_darkfriend_armor, itm_leather_boots, itm_mail_mittens, itm_guard_helmet],
   def_attrib_wot_infantry_3 ,wp_archery(140)|wp_one_handed(130)|wp(120),knows_wot_archer_3, man_face_young_1, man_face_old_2],

  ["shadowspawn_horseman_multiplayer_ai","Myrddraal","Myddraal",tf_myrddraal|tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_myrddraal_blade,itm_myrddraal_hood_helmet, itm_myrddraal_armor, itm_black_mail_gauntlets, itm_black_leather_boots, itm_myrddraal_horse],
    def_attrib_wot_cavalry_5 ,wp_two_handed(225)|wp(200),knows_wot_cavalry_5,man_face_young_1, man_face_old_2],
  ["darkfriend_leader_multi","Darkfriend Leader","Darkfriend Leader",tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_heavy_lance, itm_darkfriend_shield_strong, itm_darkfriend_plate, itm_black_leather_boots, itm_black_mail_gauntlets, itm_bascinet_3, itm_hunter],
   def_attrib_wot_cavalry_4 ,wp_polearm(160)|wp(115),knows_wot_cavalry_4, man_face_young_1, man_face_old_2],
   
   
##############################
##############################
#Multiplayer troops (they must have the base items only, nothing else)
  ["swadian_crossbowman_multiplayer","Legion Armsman","Legion Armsmen",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_bolts,itm_crossbow,itm_sword_medieval_b_small,itm_legion_shield_weak,itm_legion_recruit_tunic,itm_wrapping_boots],
   def_attrib_multiplayer|level(20),wpex(150,140,140,100,160,100),knows_common|knows_ironflesh_4|knows_athletics_4|knows_shield_4|knows_power_strike_4|knows_power_draw_4|knows_riding_3,swadian_face_young_1, swadian_face_old_2],
  ["swadian_infantry_multiplayer","Red Hand Soldier","Red Hand Soldiers",tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_sword_medieval_a,itm_red_hand_shield_weak,itm_red_hand_tunic,itm_ankle_boots],
   def_attrib_multiplayer|level(20),wpex(160,160,125,100,160,100),knows_common|knows_ironflesh_5|knows_shield_4|knows_power_strike_4|knows_power_draw_4|knows_athletics_6|knows_riding_3|knows_horse_archery_4,swadian_face_middle_1, swadian_face_old_2],
  ["swadian_man_at_arms_multiplayer","Two Rivers Militia","Two Rivers Militia",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_spear,itm_long_bow,itm_arrows,
    itm_leather_apron,itm_ankle_boots,itm_felt_hat,itm_saddle_horse],
   def_attrib_multiplayer|level(20),wpex(140,135,150,200,125,100),knows_common|knows_riding_3|knows_ironflesh_3|knows_shield_2|knows_power_draw_8|knows_power_strike_3|knows_athletics_5,swadian_face_young_1, swadian_face_old_2],
  ["legion_ashaman_multiplayer","Asha'man","Asha'man",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
   [itm_power_player_multiplayer,itm_sword_medieval_a,
    itm_ashaman_soldier_coat, itm_black_leather_boots,itm_saddle_horse],
   def_attrib_multiplayer|level(20),wpex(140,135,150,135,125,100),knows_common|knows_riding_3|knows_ironflesh_4|knows_shield_2|knows_power_strike_3|knows_athletics_3,swadian_face_young_1, swadian_face_old_2],
    
#  ["swadian_mounted_crossbowman_multiplayer","Swadian Mounted Crossbowman","Swadian Mounted Crossbowmen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_1,
#   [itm_bolts,itm_light_crossbow,itm_tab_shield_heater_cav_a,itm_bastard_sword_a,
#    itm_red_shirt,itm_hide_boots,itm_saddle_horse],
#   def_attrib_multiplayer|level(20),wp_melee(100)|wp_crossbow(120),knows_common|knows_riding_4|knows_shield_3|knows_ironflesh_3|knows_horse_archery_2|knows_power_strike_3|knows_athletics_2|knows_shield_2,swadian_face_young_1, swadian_face_old_2],

############################
  ["vaegir_archer_multiplayer","Mayene Guardsman","Mayene Guardsmen",tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_light_lance,itm_mayene_shield_weak,itm_sword_medieval_a,
    itm_mayene_recruit_tunic,itm_wrapping_boots,itm_leather_cap,itm_saddle_horse],
   def_attrib_multiplayer|str_12|level(20),wpex(150,135,160,135,125,100),knows_ironflesh_5|knows_power_draw_4|knows_athletics_4|knows_shield_5|knows_riding_4|knows_power_strike_4,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_spearman_multiplayer","Cairhien Armsman","Cairhien Armsmen",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_ranged|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_spear, itm_cairhien_shield_weak, itm_cudgel,
    itm_cairhien_recruit_tunic,itm_wrapping_boots,itm_woolen_cap],
   def_attrib_multiplayer|str_12|level(20),wpex(145,130,165,125,135,100),knows_ironflesh_4|knows_shield_3|knows_power_draw_4|knows_power_strike_4|knows_athletics_5|knows_riding_3,vaegir_face_young_1, vaegir_face_older_2],
  ["vaegir_horseman_multiplayer","Illian Armsman","Illian Armsmen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_illian_seax,itm_illian_shield_weak,itm_short_bow,itm_arrows,
    itm_illian_recruit_tunic,itm_wrapping_boots],
   def_attrib_multiplayer|level(20),wpex(155,155,140,140,125,100),knows_riding_3|knows_ironflesh_4|knows_power_strike_5|knows_shield_5|knows_power_draw_4|knows_athletics_5,vaegir_face_young_1, vaegir_face_older_2],
  ["murandy_berserker_multiplayer","Murandy Berserker","Murandy Berserkers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_spiked_club,itm_murandy_shield_weak,itm_nomad_bow,itm_arrows,
    itm_murandy_recruit_tunic,itm_wrapping_boots,itm_steppe_horse],
   def_attrib_multiplayer|level(20),wpex(145,145,150,125,125,150),knows_riding_3|knows_ironflesh_4|knows_power_strike_4|knows_shield_5|knows_power_throw_4|knows_athletics_4|knows_horse_archery_4,vaegir_face_young_1, vaegir_face_older_2],
  ["altara_guardsman_multiplayer","Altara Guardsman","Altara Guardsmen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_dagger,itm_altara_shield_weak,itm_throwing_knives,
    itm_altara_recruit_armor,itm_altara_green_boots],
   def_attrib_multiplayer|level(20),wpex(150,160,145,145,125,100),knows_riding_3|knows_ironflesh_4|knows_power_strike_5|knows_shield_5|knows_power_draw_4|knows_athletics_5,vaegir_face_young_1, vaegir_face_older_2],
  ["arad_doman_mercenary_multiplayer","Arad Doman Mercenary","Arad Doman Mercenaries",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_2,
   [itm_sword_viking_2_small,itm_arad_doman_shield_weak,itm_spear,
    itm_arad_doman_recruit_tunic,itm_wrapping_boots],
   def_attrib_multiplayer|level(20),wpex(155,145,150,135,125,150),knows_riding_3|knows_ironflesh_4|knows_power_strike_4|knows_shield_5|knows_power_throw_4|knows_athletics_4,vaegir_face_young_1, vaegir_face_older_2],

#############################
  ["khergit_veteran_horse_archer_multiplayer","Tear Defender","Tear Defenders",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_light_lance,itm_sword_viking_2_small,itm_tear_shield_weak,
    itm_tear_recruit_tunic,itm_arming_cap,itm_wrapping_boots,itm_saddle_horse],
   def_attrib_multiplayer|level(20),wpex(150,150,155,135,140,125),knows_riding_5|knows_power_draw_4|knows_shield_4|knows_power_strike_4|knows_athletics_4|knows_ironflesh_4,khergit_face_middle_1, khergit_face_older_2],
  ["khergit_lancer_multiplayer","Andor Guardsman","Andor Guardsmen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_falchion,itm_andor_shield_weak,itm_hunting_crossbow,itm_bolts,
    itm_andor_recruit_tunic,itm_skullcap,itm_leather_boots],
   def_attrib_multiplayer|level(20),wpex(150,155,150,135,145,125),knows_riding_5|knows_ironflesh_5|knows_power_draw_4|knows_shield_3|knows_power_strike_5|knows_athletics_5,khergit_face_middle_1, khergit_face_older_2],
  ["ghealdan_armsman_multiplayer","Ghealdan Armsman","Ghealdan Armsmen",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_short_bow,itm_arrows,itm_ghealdan_shield_weak,itm_hatchet,
    itm_ghealdan_recruit_tunic,itm_wrapping_boots],
   def_attrib_multiplayer|level(20),wpex(145,160,150,150,135,125),knows_riding_4|knows_ironflesh_5|knows_power_draw_4|knows_shield_4|knows_power_strike_5|knows_athletics_5,khergit_face_middle_1, khergit_face_older_2],
  ["far_madding_guard_multiplayer","Far Madding Guard","Far Madding Guards",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_crossbow,itm_bolts,itm_far_madding_shield_weak,itm_spear,
    itm_far_madding_recruit_tunic,itm_wrapping_boots],
   def_attrib_multiplayer|level(20),wpex(150,125,155,125,150,125),knows_riding_2|knows_ironflesh_5|knows_power_draw_4|knows_shield_4|knows_power_strike_5|knows_athletics_5,khergit_face_middle_1, khergit_face_older_2],
  ["tarabon_mercenary_multiplayer","Tarabon Mercenary","Tarabon Mercenaries",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_staff,itm_short_bow,itm_arrows,itm_tarabon_shield_weak,
    itm_tarabon_recruit_tunic,itm_nomad_boots],
   def_attrib_multiplayer|level(20),wpex(140,125,150,145,130,125),knows_riding_4|knows_ironflesh_4|knows_power_draw_4|knows_shield_4|knows_power_strike_4|knows_athletics_4|knows_horse_archery_4,khergit_face_middle_1, khergit_face_older_2],
  ["amadicia_regular_multiplayer","Amadicia Regular","Amadicia Regulars",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_spear,itm_amadicia_shield_weak,itm_sword_viking_2_small,
    itm_amadicia_recruit_tunic,itm_wrapping_boots,itm_black_hood],
   def_attrib_multiplayer|level(20),wpex(140,130,160,145,130,125),knows_riding_4|knows_ironflesh_4|knows_power_draw_4|knows_shield_4|knows_power_strike_4|knows_athletics_4|knows_horse_archery_4,khergit_face_middle_1, khergit_face_older_2],
  ["whitecloak_initiate_multiplayer","Whitecloak Initiate","Whitecloak Initiates",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_3,
   [itm_sword_medieval_a,itm_whitecloak_shield_weak,itm_light_lance,
    itm_whitecloak_recruit_tunic,itm_leather_boots,itm_leather_gloves,itm_courser],
   def_attrib_multiplayer|level(20),wpex(150,145,155,125,145,125),knows_riding_5|knows_ironflesh_5|knows_power_draw_4|knows_shield_4|knows_power_strike_4|knows_athletics_5,khergit_face_middle_1, khergit_face_older_2],

############################# Borderlands
  ["nord_archer_multiplayer","Shienar Border Guard","Shienar Border Guards",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_light_lance,itm_sword_viking_2_small,itm_shienar_shield_weak,
    itm_shienar_recruit_tunic,itm_leather_boots,itm_nordic_archer_helmet,itm_courser],
   def_attrib_multiplayer|str_13|level(23),wpex(160,165,180,160,145,125),knows_ironflesh_7|knows_power_strike_7|knows_shield_5|knows_power_draw_5|knows_athletics_6|knows_riding_7,nord_face_young_1, nord_face_old_2],
  ["nord_veteran_multiplayer","Arafel Guardsman","Arafel Guardsmen",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_mace_1,itm_arafel_shield_weak,itm_short_bow,itm_arrows,
    itm_arafel_recruit_tunic,itm_leather_boots,itm_footman_helmet],
   def_attrib_multiplayer|level(22),wpex(155,165,175,155,125,100),knows_ironflesh_6|knows_power_strike_7|knows_power_draw_5|knows_athletics_6|knows_shield_7|knows_riding_5|knows_horse_archery_5,nord_face_young_1, nord_face_older_2],
  ["nord_scout_multiplayer","Kandor Berserker","Kandor Berserkers",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_fighting_axe,itm_kandor_shield_weak,itm_hunting_crossbow,itm_bolts,
    itm_kandor_recruit_tunic,itm_hide_boots],
   def_attrib_multiplayer|level(23),wpex(155,175,170,155,125,100),knows_riding_5|knows_ironflesh_8|knows_power_strike_7|knows_shield_7|knows_horse_archery_5|knows_power_draw_5|knows_athletics_6,vaegir_face_young_1, vaegir_face_older_2],
  ["saldaea_armsman_multiplayer","Saldaea Armsman","Saldaea Armsman",tf_guarantee_all,0,0,fac_kingdom_4,
   [itm_sword_khergit_1,itm_saldaea_shield_weak,itm_nomad_bow,itm_arrows,
    itm_saldaea_recruit_tunic,itm_hide_boots,itm_leather_steppe_cap_b,itm_steppe_horse],
   def_attrib_multiplayer|str_12|level(22),wpex(155,165,165,180,145,125),knows_ironflesh_6|knows_power_strike_7|knows_shield_5|knows_power_draw_6|knows_athletics_6|knows_riding_8|knows_horse_archery_7,nord_face_young_1, nord_face_old_2],

############################## White Tower
  ["rhodok_veteran_crossbowman_multiplayer","Tower Guard","Tower Guards",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_crossbow,itm_bolts,itm_club,
    itm_white_tower_patrol_tunic,itm_leather_boots],
   def_attrib_multiplayer|level(20),wpex(150,145,120,125,145,125),knows_common|knows_ironflesh_5|knows_shield_3|knows_power_strike_4|knows_athletics_5|knows_riding_2|knows_power_draw_4,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_sergeant_multiplayer","Aes Sedai","Aes Sedai",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_power_player_multiplayer,itm_dagger,itm_cudgel,
    itm_novice_dress,itm_novice_accepted_damane_shoes,itm_saddle_horse],
   def_attrib_multiplayer|level(20),wpex(140,100,140,120,100,110),knows_common|knows_ironflesh_3|knows_shield_3|knows_power_strike_3|knows_athletics_4|knows_riding_3,rhodok_face_middle_1, rhodok_face_older_2],
  ["rhodok_horseman_multiplayer","Warder","Warders",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_sword_medieval_c, itm_light_lance,itm_short_bow,itm_arrows,
    itm_green_tunic,itm_leather_boots,itm_saddle_horse,itm_leather_gloves],
   def_attrib_multiplayer|level(23),wpex(150,160,150,145,125,100),knows_riding_5|knows_ironflesh_6|knows_shield_4|knows_power_strike_6|knows_power_draw_5|knows_athletics_6,rhodok_face_middle_1, rhodok_face_older_2],
  ["youngling_multiplayer","Youngling","Younglings",tf_guarantee_all,0,0,fac_kingdom_5,
   [itm_sword_viking_2_small, itm_light_lance,itm_short_bow,itm_arrows,
    itm_arena_tunic_white,itm_leather_boots,itm_saddle_horse],
   def_attrib_multiplayer|level(20),wpex(135,150,140,145,125,100),knows_riding_4|knows_ironflesh_4|knows_shield_3|knows_power_strike_4|knows_power_draw_4|knows_athletics_4,rhodok_face_middle_1, rhodok_face_older_2],

############################## Aiel Nation
  ["sarranid_archer_multiplayer","Aiel Wise One","Aiel Wise Ones",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_power_player_multiplayer,itm_aiel_knife,
    itm_wise_one_dress, itm_cadinsor_boots],
   def_attrib_multiplayer|str_12|level(19),wpex(150,125,135,125,125,100),knows_ironflesh_5|knows_power_draw_5|knows_athletics_7|knows_power_strike_5,vaegir_face_young_1, vaegir_face_older_2],
  
  ["sarranid_footman_multiplayer","Aiel Warrior","Aiel Warriors",tf_guarantee_all,0,0,fac_kingdom_6,
   [itm_shortened_spear, itm_hide_buckler_weak, itm_nomad_bow,itm_arrows,
    itm_cadinsor_grey, itm_shoufa_grey,itm_cadinsor_boots_grey],
   def_attrib_multiplayer|str_20|agi_20|level(24),wpex(170,100,180,180,50,155),knows_ironflesh_8|knows_shield_7|knows_power_throw_7|knows_power_strike_8|knows_athletics_9|knows_power_draw_7,vaegir_face_young_1, vaegir_face_older_2],

#  ["sarranid_mamluke_multiplayer","Sarranid Mamluke","Sarranid Mamluke",tf_mounted|tf_guarantee_all,0,0,fac_kingdom_6,
#   [itm_arabian_sword_a,itm_lance,itm_tab_shield_small_round_a,
#    itm_sarranid_cloth_robe, itm_sarranid_boots_b,itm_saddle_horse],
#   def_attrib_multiplayer|level(19),wpe(110,90,60,110),knows_riding_5|knows_ironflesh_3|knows_power_strike_2|knows_shield_3|knows_power_throw_2,vaegir_face_young_1, vaegir_face_older_2],

  ########################### Seanchan Empire
  ["seanchan_suldam_multiplayer","Sul'dam","Sul'dam",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_suldam_dagger,
    itm_suldam_dress, itm_suldam_boots,itm_saddle_horse],
   def_attrib_multiplayer|str_12|level(19),wpex(150,125,125,125,125,100),knows_ironflesh_3|knows_athletics_4|knows_power_strike_2|knows_riding_2,vaegir_face_young_1, vaegir_face_older_2],
  ["seanchan_damane_multiplayer","Damane","Damane",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_power_player_multiplayer,itm_dagger,
    itm_damane_dress, itm_damane_boots],
   def_attrib_multiplayer|str_12|level(20),wpex(150,125,125,125,125,100),knows_ironflesh_3|knows_athletics_4|knows_power_strike_2|knows_riding_2|knows_power_draw_4,vaegir_face_young_1, vaegir_face_older_2],
  ["seanchan_footman_multiplayer","Seanchan Footman","Seanchan Footmen",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_seanchan_straight_sword,itm_short_bow,itm_arrows,itm_staff,
    itm_blue_gambeson, itm_leather_warrior_cap,itm_leather_boots,itm_leather_gloves],
   def_attrib_multiplayer|str_12|level(20),wpex(155,165,145,150,125,100),knows_ironflesh_7|knows_power_strike_6|knows_athletics_6|knows_power_draw_5|knows_riding_3,vaegir_face_young_1, vaegir_face_older_2],
  ["seanchan_cavalry_multiplayer","Seanchan Cavalry","Seanchan Cavalry",tf_guarantee_all,0,0,fac_kingdom_7,
   [itm_seanchan_straight_sword,itm_light_lance,
    itm_blue_gambeson, itm_leather_warrior_cap,itm_leather_boots,itm_leather_gloves,itm_saddle_horse],
   def_attrib_multiplayer|str_12|level(20),wpex(155,155,165,150,125,100),knows_ironflesh_7|knows_power_strike_6|knows_athletics_5|knows_power_draw_5|knows_riding_6|knows_horse_archery_5,vaegir_face_young_1, vaegir_face_older_2],

  ############################ Shadowspawn

  ["shadowspawn_channeler_multiplayer","Darkfriend Channeler","Darkfriend Channelers",tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_power_player_multiplayer,itm_dagger,
    itm_darkfriend_tunic,itm_leather_boots],
   def_attrib_multiplayer|str_12|level(20),wpex(155,120,120,150,125,100),knows_ironflesh_4|knows_power_strike_4|knows_athletics_4|knows_power_draw_3|knows_riding_3,vaegir_face_young_1, vaegir_face_older_2],
  ["shadowspawn_soldier_multiplayer","Darkfriend Soldier","Darkfriend Soldier",tf_guarantee_all,0,0,fac_kingdom_8,
   [itm_falchion,itm_darkfriend_shield_weak,itm_short_bow,itm_arrows,
    itm_darkfriend_tunic,itm_leather_boots],
   def_attrib_multiplayer|str_12|level(20),wpex(155,155,150,150,125,100),knows_ironflesh_5|knows_power_strike_5|knows_athletics_4|knows_power_draw_4|knows_riding_4|knows_shield_4,vaegir_face_young_1, vaegir_face_older_2],
  ["shadowspawn_myrddraal_multiplayer","Myrddraal","Myrddraal",tf_guarantee_all|tf_myrddraal,0,0,fac_kingdom_8,
   [itm_sword_viking_3,itm_hunting_crossbow,itm_bolts,
    itm_darkfriend_tunic,itm_black_leather_boots,itm_draghkar_gloves,itm_myrddraal_hood_helmet,itm_saddle_horse],
   def_attrib_multiplayer|str_12|agi_20|level(25),wpex(125,175,125,125,150,100),knows_ironflesh_7|knows_power_strike_7|knows_athletics_8|knows_power_draw_6|knows_riding_6|knows_horse_archery_4,vaegir_face_young_1, vaegir_face_older_2],
  ["shadowspawn_draghkar_multiplayer","Draghkar","Draghkar",tf_guarantee_all|tf_myrddraal,0,0,fac_kingdom_8,
   [itm_draghkar_dagger,
    itm_draghkar_tunic,itm_black_leather_boots,itm_draghkar_gloves,itm_draghkar_helmet],
   def_attrib_multiplayer|str_11|level(20),wpex(150,125,125,125,125,100),knows_ironflesh_4|knows_power_strike_3|knows_athletics_5|knows_riding_1,vaegir_face_young_1, vaegir_face_older_2],
  ["shadowspawn_trolloc_multiplayer","Trolloc","Trolloc",tf_guarantee_all|tf_trolloc,0,0,fac_kingdom_8,
   [itm_hatchet,itm_pitch_fork,itm_short_bow,itm_arrows,
    itm_trolloc_weak_armor,itm_black_leather_boots,itm_draghkar_gloves,itm_trolloc_hawk_helmet],
   def_attrib_multiplayer|str_20|agi_25|level(22),wpex(160,165,175,160,125,100),knows_ironflesh_7|knows_power_strike_8|knows_athletics_10|knows_power_draw_6,vaegir_face_young_1, vaegir_face_older_2],

  ["multiplayer_end","{!}multiplayer_end","{!}multiplayer_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

  #replacable troop, not used
  ["nurse","Nurse","{!}nurse",tf_hero|tf_female|tf_unmoveable_in_party_window,0,reserved,fac_kingdom_1, [      itm_lady_dress_ruby ,   itm_turret_hat_ruby,    itm_leather_boots],     def_attrib|level(2),wp(50),knows_common|knows_riding_2, 0x000000055910200107632d675a92b92d00000000001e45620000000000000000],
  #erase later added to avoid errors

#Player history array
  ["log_array_entry_type",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_entry_time",            "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_actor",                 "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object",         "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_lord",    "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_center_object_faction", "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object",          "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_troop_object_faction",  "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],
  ["log_array_faction_object",        "{!}Local Merchant","{!}Local Merchant",tf_guarantee_boots|tf_guarantee_armor, 0,0, fac_commoners,[itm_leather_apron,itm_leather_boots,itm_butchering_knife],def_attrib|level(5),wp(40),knows_power_strike_1, merchant_face_1, merchant_face_2],

# changed for TGS
  ["quick_battle_troop_1","The Dragon Reborn Rand al'Thor",  "Rand",  tf_hero, 0,0,  fac_kingdom_1,[itm_lord_warhorse_5, itm_rich_outfit, itm_leather_boots, itm_shynbaulds_wot, itm_legion_plate, itm_gauntlets, itm_power_player, itm_large_heron_mark_blade], knight_attrib_5,wpex(100,300,100,100,50,50)|wp_firearm(350),knight_skills_5|knows_trainer_5|knows_power_draw_10|knows_channeling_10|knows_fire_10|knows_earth_10|knows_spirit_10|knows_water_10|knows_air_10, 0x00000000990c1001271c8dc71a6d36d300000000001db70d0000000000000000],
  
  ["quick_battle_troop_2","al'Lan Mandragoran",  "Lan",  tf_hero, 0,0,  fac_kingdom_21,[itm_heavy_charger, itm_nobleman_outfit, itm_leather_boots, itm_steel_greaves_wot, itm_shienar_captain_armor, itm_shienar_captain_gauntlets, itm_winged_great_helmet, itm_seanchan_large_sword, itm_heavy_lance, itm_seanchan_straight_sword, itm_shienar_shield_strong], knight_attrib_5,wpex(250,325,250,150,150,150),knight_skills_5|knows_trainer_4, 0x0000000b2c04500348628a4b5b72259400000000001e453a0000000000000000],
  
  ["quick_battle_troop_3","Clan Chief Rhuarc",  "Rhuarc",  tf_hero, 0,0,  fac_kingdom_22,[itm_cadinsor, itm_cadinsor_boots, itm_shoufa, itm_aiel_spear, itm_aiel_knife, itm_javelin, itm_hide_buckler_strong], knight_attrib_5,wpex(250,100,300,100,100,200),knight_skills_5|knows_trainer_5|knows_athletics_9, 0x0000000dd90c100167f4ef4732ad475400000000001dc74c0000000000000000],
  
  ["quick_battle_troop_4","Shaidar Haran",  "Shaidar Haran",  tf_hero|tf_myrddraal, 0,0,  fac_kingdom_24,[itm_myrddraal_horse, itm_myrddraal_armor, itm_black_leather_boots, itm_myrddraal_hood_helmet, itm_black_mail_gauntlets, itm_myrddraal_blade], knight_attrib_5,wpex(150,300,100,250,100,100),knight_skills_5|knows_trainer_5|knows_athletics_7, 0x000000033604400933a5d2329c72461600000000001cc7230000000000000000],
  
  ["quick_battle_troop_5","Matrim Cauthon", "Mat", tf_hero, 0, 0,  fac_kingdom_2, [itm_hunter, itm_mats_hat, itm_red_hand_plate, itm_red_hand_greaves, itm_leather_gloves, itm_ashandarei, itm_throwing_knives, itm_throwing_knives], knight_attrib_5,wpex(150,150,350,150,100,200),knight_skills_5|knows_trainer_7, 0x000000003d04100448dc92392471c91c00000000001d47250000000000000000],
  
  ["quick_battle_troop_6","Perrin Aybara", "Perrin", tf_hero, 0, 0,  fac_kingdom_3, [itm_hunter, itm_two_rivers_armor, itm_leather_boots, itm_leather_gloves, itm_warhammer, itm_illian_seax], knight_attrib_5,wpex(250,300,150,100,100,100),knight_skills_5|knows_trainer_4, 0x00000002270022434795b6b9634f66ea00000000001e58d20000000000000000],

  ["quick_battle_troop_7","Tam al'Thor", "Tam", tf_hero, 0, 0,  fac_kingdom_3, [itm_hunter, itm_two_rivers_armor, itm_leather_boots, itm_leather_gloves, itm_two_rivers_long_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_seanchan_large_sword], knight_attrib_4,wpex(150,275,300,300,100,100),knight_skills_4|knows_trainer_4, andor_man_face_old],
  
  ["quick_battle_troop_8","Lord Davram Bashere", "Davram", tf_hero, 0, 0,  fac_kingdom_1, [itm_lord_warhorse_1, itm_vaegir_elite_armor, itm_splinted_greaves, itm_khergit_guard_helmet, itm_lamellar_gauntlets, itm_heavy_lance, itm_khergit_sword_two_handed_b, itm_sword_khergit_4, itm_saldaea_shield_strong], knight_attrib_5,wpex(250,275,250,300,100,100),knight_skills_5|knows_trainer_4, saldaea_man_face_old],
  
  ["quick_battle_troop_9","Nynaeve Sedai", "Nynaeve", tf_hero|tf_female, 0, 0,  fac_kingdom_21, [itm_hunter, itm_aes_sedai_yellow_dress, itm_veteran_aes_sedai_yellow_shoes, itm_power_player, itm_cudgel], knight_attrib_3,wpex(200,100,100,100,100,100)|wp_firearm(300),knight_skills_3|knows_trainer_4|knows_power_draw_9|knows_channeling_9|knows_fire_9|knows_earth_9|knows_spirit_10|knows_water_9|knows_air_9, andor_woman_face_young],
  
  ["quick_battle_troop_10","Captain General Birgitte Silverbow", "Birgitte", tf_hero|tf_female, 0, reserved,  fac_kingdom_11, [itm_lord_warhorse_4, itm_andor_plate, itm_leather_boots, itm_leather_gloves, itm_war_bow, itm_bodkin_arrows, itm_bodkin_arrows, itm_sword_medieval_b_small], knight_attrib_4,wpex(250,100,100,350,100,100),knight_skills_4|knows_trainer_4, 0x00000001800000024cccd288cc39a36e00000000001edd080000000000000000],
  
  ["quick_battle_troop_11","Banner-General Furyk Karede", "Karede", tf_hero, 0, reserved,  fac_kingdom_23, [itm_arabian_horse_b, itm_deathwatch_guard_armor, itm_deathwatch_guard_helmet, itm_deathwatch_guard_boots, itm_deathwatch_guard_gloves, itm_seanchan_large_sword, itm_heavy_lance], knight_attrib_5,wpex(150,275,275,100,100,100),knight_skills_5|knows_trainer_4, seanchan_1_man_face_old],

  ["quick_battle_troop_12","Trolloc Clan Chief", "Trolloc Clan Chief", tf_hero|tf_trolloc, 0, reserved,  fac_kingdom_24, [itm_trolloc_strong_armor, itm_black_leather_boots, itm_black_mail_gauntlets, itm_trolloc_goat_helmet, itm_great_long_bardiche, itm_street_patrol_club], knight_attrib_5,wpex(250,150,300,150,100,100),knight_skills_5|knows_trainer_5|knows_athletics_10, 0x000000033604400933a5d2329c72461600000000001cc7230000000000000000],

  ["quick_battle_troops_end","{!}quick_battle_troops_end","{!}quick_battle_troops_end", 0, 0, 0, fac_kingdom_5, [], 0, 0, 0, 0, 0],

  ["tutorial_fighter_1","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088c1073144252b1929a85569300000000000496a50000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_2","Novice Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x000000088b08049056ab56566135c46500000000001dda1b0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_3","Regular Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_nomad_boots],
   def_attrib|level(9),wp_melee(50),knows_athletics_1|knows_ironflesh_2|knows_shield_2,0x00000008bc00400654914a3b0d0de74d00000000001d584e0000000000000000, vaegir_face_older_2],
  ["tutorial_fighter_4","Veteran Fighter","Fighters",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|level(16),wp_melee(110),knows_athletics_1|knows_ironflesh_3|knows_power_strike_2|knows_shield_2,0x000000089910324a495175324949671800000000001cd8ab0000000000000000, vaegir_face_older_2],
  ["tutorial_archer_1","Archer","Archers",tf_guarantee_ranged|tf_guarantee_boots|tf_guarantee_armor,0,0,fac_kingdom_2,
   [itm_leather_jerkin,itm_leather_vest,itm_nomad_boots,itm_vaegir_spiked_helmet,itm_vaegir_fur_helmet,itm_vaegir_fur_cap,itm_nomad_cap],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,vaegir_face_young_1, vaegir_face_older_2],
  ["tutorial_master_archer","Archery Trainer","Archery Trainer",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea508540642f34d461d2d54a300000000001d5d9a0000000000000000, vaegir_face_older_2],
  ["tutorial_rider_1","Rider","{!}Vaegir Knights",tf_mounted|tf_guarantee_boots|tf_guarantee_gloves|tf_guarantee_armor|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,0,0,fac_kingdom_2,
   [itm_green_tunic,itm_hunter, itm_saddle_horse,itm_leather_gloves],
   def_attrib|level(24),wp(130),knows_riding_4|knows_shield_2|knows_ironflesh_3|knows_power_strike_2,vaegir_face_middle_1, vaegir_face_older_2],
  ["tutorial_rider_2","Horse archer","{!}Khergit Horse Archers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_ranged|tf_guarantee_horse,0,0,fac_kingdom_3,
   [itm_tribal_warrior_outfit,itm_nomad_robe,itm_hide_boots,itm_tab_shield_small_round_a,itm_steppe_horse],
   def_attrib|level(14),wp(80)|wp_archery(110),knows_riding_5|knows_power_draw_3|knows_ironflesh_1|knows_horse_archery_4|knows_power_throw_1,khergit_face_young_1, khergit_face_older_2],
  ["tutorial_master_horseman","Riding Trainer","Riding Trainer",tf_hero,0,0,fac_kingdom_2,
   [itm_leather_vest,itm_nomad_boots],
   def_attrib|str_12|level(19),wp_melee(70)|wp_archery(110),knows_ironflesh_1|knows_power_draw_2|knows_athletics_2|knows_power_throw_1,0x0000000ea0084140478a692894ba185500000000001d4af30000000000000000, vaegir_face_older_2],
   
##### merchants for the tutorial (modify for TGS)
   
  ["swadian_merchant", "Merchant of Bandar Eban", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_4, [itm_sword_two_handed_a, itm_courtly_outfit, itm_leather_boots], def_attrib|level(2),wp(20),knows_common, arad_doman_man_face_old, mercenary_face_2],
  ["vaegir_merchant", "Merchant of Tanchico", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_5, [itm_sword_two_handed_a, itm_nobleman_outfit, itm_woolen_hose], def_attrib|level(2),wp(20),knows_common, tarabon_man_face_middle, mercenary_face_2],
  ["khergit_merchant", "Merchant of Tear", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_1, [itm_sword_two_handed_a, itm_red_gambeson, itm_nomad_boots], def_attrib|level(2),wp(20),knows_common, tear_man_face_old, mercenary_face_2],
  ["nord_merchant", "Merchant of Cairhien", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_2, [itm_sword_two_handed_a, itm_red_gambeson, itm_nomad_boots], def_attrib|level(2),wp(20),knows_common, cairhien_man_face_middle, mercenary_face_2],
  ["rhodok_merchant", "Merchant of Lugard", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_3, [itm_sword_two_handed_a, itm_leather_jerkin, itm_blue_hose], def_attrib|level(2),wp(20),knows_common, murandy_man_face_old, mercenary_face_2],
  ["sarranid_merchant", "Merchant of Tar Valon", "{!}Prominent", tf_hero|tf_randomize_face, 0, reserved, fac_kingdom_6, [itm_sword_two_handed_a, itm_sarranid_cloth_robe, itm_sarranid_boots_a], def_attrib|level(2),wp(20),knows_common, tar_valon_man_face_middle, mercenary_face_2],       
  ["startup_merchants_end","startup_merchants_end","startup_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],
 
  ["sea_raider_leader","Sea Raider Captain","Sea Raiders",tf_hero|tf_guarantee_all_wo_ranged,0,0,fac_outlaws,
   [itm_arrows,itm_sword_viking_1,itm_sword_viking_2,itm_fighting_axe,itm_battle_axe,itm_spear,itm_nordic_shield,itm_nordic_shield,itm_nordic_shield,itm_wooden_shield,itm_long_bow,itm_javelin,itm_throwing_axes,
    itm_nordic_helmet,itm_nordic_helmet,itm_nasal_helmet,itm_mail_shirt,itm_byrnie,itm_mail_hauberk,itm_leather_boots, itm_nomad_boots],
   def_attrib|level(24),wp(110),knows_ironflesh_2|knows_power_strike_2|knows_power_draw_3|knows_power_throw_2|knows_riding_1|knows_athletics_2,nord_face_young_1, nord_face_old_2],

  ["looter_leader","Robber","Looters",tf_hero,0,0,fac_outlaws,
   [itm_hatchet,itm_club,itm_butchering_knife,itm_falchion,itm_rawhide_coat,itm_stones,itm_nomad_armor,itm_nomad_armor,itm_woolen_cap,itm_woolen_cap,itm_nomad_boots,itm_wrapping_boots],
   def_attrib|level(4),wp(20),knows_common,0x00000001b80032473ac49738206626b200000000001da7660000000000000000, bandit_face2],
   
  ["bandit_leaders_end","bandit_leaders_end","bandit_leaders_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],   
  
  ["relative_of_merchant", "Merchant's Brother", "{!}Prominent",tf_hero,0,0,fac_kingdom_2,
   [itm_linen_tunic,itm_nomad_boots],
   def_attrib|level(1),wp_melee(10),knows_athletics_1|knows_ironflesh_2|knows_shield_2, 0x00000000320410022d2595495491afa400000000001d9ae30000000000000000, mercenary_face_2],   
   
  ["relative_of_merchants_end","relative_of_merchants_end","relative_of_merchants_end",tf_hero, 0,0, fac_commoners,[],def_attrib|level(2),wp(20),knows_inventory_management_10,0],     
  ##diplomacy begin
  ["dplmc_chamberlain","Chamberlain Aubrey de Vere", "Chamberlains",tf_hero|tf_male,0,0,fac_commoners,[itm_tabard, itm_leather_boots], def_attrib|level(10), wp(40),knows_inventory_management_10,0x0000000dfc0c238838e571c8d469c91b00000000001e39230000000000000000],

  ["dplmc_constable","Constable Miles de Gloucester","Constables",tf_hero|tf_male,0,0,fac_commoners,[itm_dplmc_coat_of_plates_red_constable, itm_leather_boots],
   knight_attrib_4,wp_melee(200),knows_common|knows_shield_3|knows_ironflesh_3|knows_power_strike_4|knows_athletics_4,0x0000000b4b1015054b1b4d591cba28d300000000001e472b0000000000000000],

  ["dplmc_chancellor","Chancellor Herfast","Chancellors",tf_hero|tf_male,0,0,fac_commoners,[itm_nobleman_outfit, itm_leather_boots],def_attrib|level(10), wp(40),knows_inventory_management_10, 0x00000009a20c21cf491bad28a28628d400000000001e371a0000000000000000],

  ["dplmc_messenger","Messenger","Messengers",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,
   [itm_sword_medieval_a,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],
   def_attrib|agi_21|int_30|cha_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7,man_face_young_1,man_face_old_2],

  ["dplmc_scout","Scout","Scouts",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,
   [itm_sword_medieval_a,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],
   def_attrib|agi_21|int_30|cha_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7,man_face_young_1,man_face_old_2],

   
# recruiter kit begin 
  ["dplmc_recruiter","Recruiter","Recruiter",tf_mounted|tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_horse|tf_guarantee_ranged,0,0,fac_neutral,
   [itm_sword_medieval_a,itm_leather_jerkin,itm_leather_boots,itm_courser,itm_leather_gloves,itm_light_crossbow,itm_bolts],
   def_attrib|agi_21|int_30|cha_21|level(25),wp(130),knows_common|knows_riding_7|knows_horse_archery_5|knows_leadership_7,swadian_face_young_1, swadian_face_old_2],
# recruiter kit end
  ##diplomacy end
]


#Troop upgrade declarations

upgrade(troops,"farmer", "watchman")
upgrade(troops,"townsman","watchman")
upgrade2(troops,"watchman","caravan_guard","mercenary_crossbowman")
upgrade2(troops,"caravan_guard","mercenary_swordsman","mercenary_horseman")
upgrade(troops,"mercenary_swordsman","hired_blade")
upgrade(troops,"mercenary_horseman","mercenary_cavalry")

#########################################
#### commented out native upgrades for TGS mod

#upgrade(troops,"swadian_recruit","swadian_militia")
#upgrade2(troops,"swadian_militia","swadian_footman","swadian_skirmisher")
#upgrade2(troops,"swadian_footman","swadian_man_at_arms","swadian_infantry")
#upgrade(troops,"swadian_infantry","swadian_sergeant")
#upgrade(troops,"swadian_skirmisher","swadian_crossbowman")
#upgrade(troops,"swadian_crossbowman","swadian_sharpshooter")
#upgrade(troops,"swadian_man_at_arms","swadian_knight")

#upgrade(troops,"vaegir_recruit","vaegir_footman")
#upgrade2(troops,"vaegir_footman","vaegir_veteran","vaegir_skirmisher")
#upgrade(troops,"vaegir_skirmisher","vaegir_archer")
#upgrade(troops,"vaegir_archer","vaegir_marksman")
#upgrade2(troops,"vaegir_veteran","vaegir_horseman","vaegir_infantry")
#upgrade(troops,"vaegir_infantry","vaegir_guard")
#upgrade(troops,"vaegir_horseman","vaegir_knight")

#upgrade(troops,"khergit_tribesman","khergit_skirmisher")
#upgrade(troops,"khergit_skirmisher","khergit_horseman")
#upgrade2(troops,"khergit_horseman","khergit_lancer","khergit_horse_archer")
#upgrade(troops,"khergit_horse_archer","khergit_veteran_horse_archer")

#upgrade2(troops,"nord_recruit","nord_footman","nord_huntsman")
#upgrade(troops,"nord_footman","nord_trained_footman")
#upgrade(troops,"nord_trained_footman","nord_warrior")
#upgrade(troops,"nord_warrior","nord_veteran")
#upgrade(troops,"nord_veteran","nord_champion")
#upgrade(troops,"nord_huntsman","nord_archer")
#upgrade(troops,"nord_archer","nord_veteran_archer")

#upgrade2(troops,"rhodok_tribesman","rhodok_spearman","rhodok_crossbowman")
#upgrade(troops,"rhodok_spearman","rhodok_trained_spearman")
#upgrade(troops,"rhodok_trained_spearman","rhodok_veteran_spearman")
#upgrade(troops,"rhodok_veteran_spearman","rhodok_sergeant")
#upgrade(troops,"rhodok_crossbowman","rhodok_trained_crossbowman")
#upgrade(troops,"rhodok_trained_crossbowman","rhodok_veteran_crossbowman") #new 1.126
#upgrade(troops,"rhodok_veteran_crossbowman","rhodok_sharpshooter")

#upgrade(troops,"sarranid_recruit","sarranid_footman")
#upgrade2(troops,"sarranid_footman","sarranid_veteran_footman","sarranid_skirmisher")
#upgrade2(troops,"sarranid_veteran_footman","sarranid_horseman","sarranid_infantry")
#upgrade(troops,"sarranid_infantry","sarranid_guard")
#upgrade(troops,"sarranid_skirmisher","sarranid_archer")
#upgrade(troops,"sarranid_archer","sarranid_master_archer")
#upgrade(troops,"sarranid_horseman","sarranid_mamluke")

################################ end commented out native upgrades for TGS mod
#############################################

##############################
### other upgrade tree troops that I commented out for TGS (I moved their position below my own troops and it might have hurt their upgrade order, so I commented out their upgrade just in case.)

#upgrade2(troops,"looter","mountain_bandit", "forest_bandit")

  #new tree connections (commented out for TGS)
  #upgrade(troops,"mountain_bandit","rhodok_tribesman")
  #upgrade(troops,"forest_bandit","swadian_recruit")
  #upgrade(troops,"steppe_bandit","khergit_tribesman")
  #upgrade(troops,"taiga_bandit","vaegir_recruit")
  #upgrade(troops,"sea_raider","nord_recruit")
  #upgrade(troops,"desert_bandit","sarranid_recruit")
  #new tree connections ended (commented out for TGS)

#upgrade2(troops,"bandit","brigand","mercenary_swordsman")
#upgrade(troops,"manhunter","slave_driver")

  #upgrade(troops,"forest_bandit","mercenary_crossbowman")

#upgrade(troops,"slave_driver","slave_hunter")
#upgrade(troops,"slave_hunter","slave_crusher")
#upgrade(troops,"slave_crusher","slaver_chief")

upgrade(troops,"follower_woman","hunter_woman")
upgrade(troops,"hunter_woman","fighter_woman")

upgrade(troops,"fighter_woman","sword_sister")
upgrade(troops,"refugee","follower_woman")

## added for TGS
upgrade2(troops,"peasant_woman","follower_woman","village_wisdom")
upgrade(troops,"village_wisdom","kinswoman"),
## end added for TGS

### other upgrade tree troops that I commented out for TGS (I moved their position below my own troops and it might have hurt their upgrade order, so I commented out their upgrade just in case.)
##############################

#################################
##### TGS troop upgrades (starting with Swadian recruit to Legion recruit)
#################################

##### Legion of the Dragon

#upgrade2(troops,"legion_recruit","legion_recruit_channeler","legion_recruit_soldier")

#Legion Channelers
upgrade(troops,"legion_recruit_channeler","ashaman_soldier")
upgrade(troops,"ashaman_soldier","ashaman_dedicated")
upgrade(troops,"ashaman_dedicated","ashaman")
upgrade(troops,"ashaman","ashaman_veteran")

#upgrade2(troops,"legion_recruit_soldier","legion_recruit_army","legion_ally")

#Legion Army
upgrade2(troops,"legion_recruit_army","legion_footman","legion_cavalry")
upgrade2(troops,"legion_footman","legion_infantry","legion_crossbowman")
upgrade2(troops,"legion_infantry","legion_swordsman","legion_pikeman")
upgrade(troops,"legion_swordsman","legion_blademaster")
upgrade(troops,"legion_pikeman","legion_bannerman")
upgrade(troops,"legion_crossbowman","legion_heavy_crossbowman")
upgrade2(troops,"legion_cavalry","legion_lancer","legion_man_at_arms")
upgrade(troops,"legion_lancer","legion_heavy_lancer")
upgrade(troops,"legion_man_at_arms","legion_captain")

#upgrade2(troops,"legion_ally","legion_true_ally","legion_conquered_ally")

#upgrade2(troops,"legion_true_ally","legion_true_ally_mat","legion_true_ally_perrin")

#Legion True Ally (Mat)
#upgrade(troops,"legion_true_ally_mat","red_hand_recruit")
upgrade2(troops,"red_hand_recruit","red_hand_infantry","red_hand_man_at_arms")
upgrade2(troops,"red_hand_infantry","red_hand_pikeman","red_hand_crossbowman")
upgrade2(troops,"red_hand_pikeman","red_hand_bannerman","red_hand_swordsman")
upgrade(troops,"red_hand_crossbowman","red_hand_fast_crossbowman")
upgrade2(troops,"red_hand_man_at_arms","red_hand_light_cavalry","red_hand_skirmisher")
upgrade2(troops,"red_hand_light_cavalry","red_hand_lancer","red_hand_captain")

#Legion True Ally (Perrin)
#upgrade2(troops,"legion_true_ally_perrin","two_rivers_farmer","mayene_man_at_arms")  #will need to change to upgrade2... to add the Mayeners eventually.
upgrade2(troops,"two_rivers_farmer","two_rivers_spearman","two_rivers_longbowman")
upgrade2(troops,"two_rivers_spearman","two_rivers_halberdier","two_rivers_scout")
upgrade(troops,"two_rivers_longbowman","two_rivers_marksman")

#Legion Conquered Ally
#upgrade2(troops,"legion_conquered_ally","legion_north_east_ally","legion_south_east_ally")
#upgrade2(troops,"legion_north_east_ally","legion_cairhien_ally","legion_andor_ally")  #need to eventually add upgrades to Cairhien and Andor troop trees
#upgrade2(troops,"legion_south_east_ally","legion_tear_ally","legion_illian_ally")  #need to eventually add upgrades to Tear and Illain troop trees

upgrade2(troops,"legion_cairhien_ally","cairhien_pikeman","cairhien_lancer") #is it possible to make an upgrade3 that looks at a third input for whether or not the upgrade should be allowed?
upgrade2(troops,"legion_andor_ally","andor_swordsman","andor_man_at_arms")
upgrade2(troops,"legion_tear_ally","tear_bowman","tear_lancer")
upgrade2(troops,"legion_illian_ally","illian_crossbowman","illian_man_at_arms")


##### Southlanders Coalition (1)

#upgrade2(troops,"southlander_1_recruit","southlander_1_recruit_east_central","southlander_1_recruit_west")

#upgrade2(troops,"southlander_1_recruit_east_central","southlander_1_recruit_east","southlander_1_recruit_central")

#upgrade2(troops,"southlander_1_recruit_east","mayene_recruit","cairhien_recruit")
#Mayene
upgrade2(troops,"mayene_recruit","mayene_militia","mayene_man_at_arms")
upgrade2(troops,"mayene_militia","mayene_swordsman","mayene_bowman")
upgrade(troops,"mayene_man_at_arms","mayene_lancer")
upgrade(troops,"mayene_lancer","mayene_royal_guard")
#Cairhien
upgrade2(troops,"cairhien_recruit","cairhien_militia","cairhien_man_at_arms")
upgrade2(troops,"cairhien_militia","cairhien_pikeman","cairhien_crossbowman")
upgrade(troops,"cairhien_pikeman","cairhien_bannerman")
upgrade2(troops,"cairhien_man_at_arms","cairhien_light_cavalry","cairhien_lancer")

#upgrade2(troops,"southlander_1_recruit_central","illian_recruit","murandy_recruit")
#Illian
upgrade2(troops,"illian_recruit","illian_militia","illian_scout")
upgrade2(troops,"illian_militia","illian_swordsman","illian_bowman")
upgrade(troops,"illian_swordsman","illian_companion")
upgrade(troops,"illian_companion","illian_companion_captain")
upgrade(troops,"illian_bowman","illian_crossbowman")
upgrade(troops,"illian_crossbowman","illian_marksman")
upgrade(troops,"illian_scout","illian_man_at_arms")
#Murandy
upgrade2(troops,"murandy_recruit","murandy_militia","murandy_scout")
upgrade2(troops,"murandy_militia","murandy_maceman","murandy_bowman")
upgrade(troops,"murandy_maceman","murandy_berserker")
upgrade(troops,"murandy_bowman","murandy_marksman")
upgrade(troops,"murandy_scout","murandy_lancer")
upgrade(troops,"murandy_lancer","murandy_captain")

#upgrade2(troops,"southlander_1_recruit_west","altara_recruit","arad_doman_recruit")
#Altara
upgrade2(troops,"altara_recruit","altara_dueler","altara_scout")
upgrade2(troops,"altara_dueler","altara_swordsman","altara_knife_thrower")
upgrade(troops,"altara_swordsman","altara_royal_guard")
upgrade2(troops,"altara_scout","altara_man_at_arms","altara_skirmisher")
#Arad Doman
upgrade2(troops,"arad_doman_recruit","arad_doman_rabble","arad_doman_scout")
upgrade2(troops,"arad_doman_rabble","arad_doman_swordsman","arad_doman_bowman")
upgrade(troops,"arad_doman_swordsman","arad_doman_long_swordsman")
upgrade(troops,"arad_doman_scout","arad_doman_man_at_arms")


##### Southlanders Alliance (2)

#upgrade2(troops,"southlander_2_recruit","southlander_2_recruit_east_central","southlander_2_recruit_west")

#upgrade2(troops,"southlander_2_recruit_east_central","southlander_2_recruit_east","southlander_2_recruit_central")

#upgrade2(troops,"southlander_2_recruit_east","tear_recruit","andor_recruit")
#Tear
upgrade2(troops,"tear_recruit","tear_town_watch","tear_scout")
upgrade2(troops,"tear_town_watch","tear_swordsman","tear_bowman")
upgrade2(troops,"tear_swordsman","tear_blademaster","tear_defender")
upgrade(troops,"tear_defender","tear_defender_captain")
upgrade(troops,"tear_bowman","tear_crossbowman")
upgrade2(troops,"tear_scout","tear_light_cavalry","tear_lancer")
upgrade(troops,"tear_lancer","tear_heavy_lancer")
#Andor
upgrade2(troops,"andor_recruit","andor_militia","andor_scout")
upgrade2(troops,"andor_militia","andor_swordsman","andor_bowman")
upgrade2(troops,"andor_swordsman","andor_blademaster","andor_halberdier")
upgrade(troops,"andor_bowman","andor_crossbowman")
upgrade2(troops,"andor_scout","andor_man_at_arms","andor_lancer")
upgrade(troops,"andor_lancer","andor_queens_guard")
upgrade(troops,"andor_queens_guard","andor_bannerman")

#upgrade2(troops,"southlander_2_recruit_central","ghealdan_recruit","far_madding_recruit")
#Ghealdan
upgrade2(troops,"ghealdan_recruit","ghealdan_militia","ghealdan_scout")
upgrade2(troops,"ghealdan_militia","ghealdan_axeman","ghealdan_bowman")
upgrade(troops,"ghealdan_axeman","ghealdan_heavy_axeman")
upgrade(troops,"ghealdan_bowman","ghealdan_marksman")
upgrade2(troops,"ghealdan_scout","ghealdan_man_at_arms","ghealdan_lancer")
upgrade(troops,"ghealdan_lancer","ghealdan_royal_guard")
#Far Madding
upgrade2(troops,"far_madding_recruit","far_madding_footman","far_madding_crossbowman")
upgrade(troops,"far_madding_footman","far_madding_city_guard")

#upgrade2(troops,"southlander_2_recruit_west","tarabon_recruit","amadicia_recruit")
#Tarabon
upgrade2(troops,"tarabon_recruit","tarabon_rabble","tarabon_scout")
upgrade2(troops,"tarabon_rabble","tarabon_spearman","tarabon_bowman")
upgrade(troops,"tarabon_bowman","tarabon_marksman")
upgrade2(troops,"tarabon_scout","tarabon_lancer","tarabon_skirmisher")
#Amadicia
upgrade(troops,"amadicia_recruit","amadicia_militia")
upgrade2(troops,"amadicia_militia","amadicia_pikeman","amadicia_bowman")
upgrade(troops,"amadicia_pikeman","amadicia_captain")
upgrade(troops,"amadicia_bowman","amadicia_skirmisher")

upgrade2(troops,"whitecloak_recruit","whitecloak_footman","whitecloak_man_at_arms")
upgrade2(troops,"whitecloak_footman","whitecloak_swordsman","whitecloak_bowman")
upgrade(troops,"whitecloak_swordsman","whitecloak_captain")
upgrade(troops,"whitecloak_bowman","whitecloak_crossbowman")
upgrade(troops,"whitecloak_man_at_arms","whitecloak_lancer")


##### Borderlands

#upgrade2(troops,"borderland_recruit","borderland_recruit_east","borderland_recruit_west")

#upgrade2(troops,"borderland_recruit_east","shienar_recruit","arafel_recruit")
#Shienar
upgrade2(troops,"shienar_recruit","shienar_militia","shienar_light_cavalry")
upgrade2(troops,"shienar_militia","shienar_spearman","shienar_bowman")
upgrade2(troops,"shienar_spearman","shienar_pikeman","shienar_swordsman")
upgrade(troops,"shienar_swordsman","shienar_blademaster")
upgrade2(troops,"shienar_bowman","shienar_marksman","shienar_crossbowman")
upgrade(troops,"shienar_light_cavalry","shienar_lancer")
upgrade(troops,"shienar_lancer","shienar_heavy_lancer")
upgrade(troops,"shienar_heavy_lancer","shienar_captain")
#Arafel
upgrade2(troops,"arafel_recruit","arafel_militia","arafel_man_at_arms")
upgrade2(troops,"arafel_militia","arafel_swordsman","arafel_bowman")
upgrade2(troops,"arafel_swordsman","arafel_blademaster","arafel_halberdier")
upgrade(troops,"arafel_halberdier","arafel_bannerman")
upgrade(troops,"arafel_bowman","arafel_marksman")
upgrade2(troops,"arafel_man_at_arms","arafel_lancer","arafel_skirmisher")

#upgrade2(troops,"borderland_recruit_west","kandor_recruit","saldaea_recruit")
#Kandor
upgrade2(troops,"kandor_recruit","kandor_militia","kandor_man_at_arms")
upgrade2(troops,"kandor_militia","kandor_axeman","kandor_bowman")
upgrade2(troops,"kandor_axeman","kandor_berserker","kandor_maceman")
upgrade(troops,"kandor_berserker","kandor_captain")
upgrade(troops,"kandor_bowman","kandor_crossbowman")
upgrade2(troops,"kandor_man_at_arms","kandor_heavy_horseman","kandor_skirmisher")
#Saldaea
upgrade2(troops,"saldaea_recruit","saldaea_militia","saldaea_cavalry")
upgrade2(troops,"saldaea_militia","saldaea_swordsman","saldaea_bowman")
upgrade2(troops,"saldaea_swordsman","saldaea_bannerman","saldaea_halberdier")
upgrade(troops,"saldaea_bowman","saldaea_marksman")
upgrade2(troops,"saldaea_cavalry","saldaea_light_cavalry","saldaea_skirmisher")
upgrade(troops,"saldaea_light_cavalry","saldaea_elite_light_cavalry")
upgrade(troops,"saldaea_elite_light_cavalry","saldaea_quartermaster")
upgrade(troops,"saldaea_skirmisher","saldaea_elite_skirmisher")


##### White Tower

#upgrade2(troops,"sedai_recruit","sedai_recruit_channeler","sedai_recruit_soldier")

#Aes Sedai Channelers
upgrade2(troops,"sedai_recruit_channeler","novice_social","novice_civil")

upgrade2(troops,"novice_social","accepted_medical","accepted_academic")

upgrade(troops,"accepted_medical","aes_sedai_yellow")
upgrade(troops,"aes_sedai_yellow","aes_sedai_yellow_veteran")

upgrade2(troops,"accepted_academic","aes_sedai_brown","aes_sedai_white")
upgrade(troops,"aes_sedai_brown","aes_sedai_brown_veteran")
upgrade(troops,"aes_sedai_white","aes_sedai_white_veteran")

upgrade2(troops,"novice_civil","accepted_political","accepted_military")

upgrade2(troops,"accepted_political","aes_sedai_blue","aes_sedai_grey")
upgrade(troops,"aes_sedai_blue","aes_sedai_blue_veteran")
upgrade(troops,"aes_sedai_grey","aes_sedai_grey_veteran")

upgrade2(troops,"accepted_military","aes_sedai_red","aes_sedai_green")
upgrade(troops,"aes_sedai_red","aes_sedai_red_veteran")
upgrade(troops,"aes_sedai_green","aes_sedai_green_veteran")
#Aes Sedai Soldiers
upgrade2(troops,"sedai_recruit_soldier","tar_valon_street_patrol","warder_trainee")
upgrade2(troops,"tar_valon_street_patrol","tower_guard_infantry","tower_guard_crossbowman")
upgrade(troops,"tower_guard_infantry","tower_guard_captain")

upgrade2(troops,"warder_trainee","youngling_infantry","youngling_cavalry")
#At this time Warders are not upgradeable (they spawn with their Aes Sedai)


##### Aiel Nation

#upgrade2(troops, "aiel_recruit", "aiel_recruit_channeler", "aiel_recruit_soldier")
#Aiel Channlers
upgrade(troops, "aiel_recruit_channeler", "wise_one_apprentice")
upgrade(troops, "wise_one_apprentice", "wise_one")
upgrade(troops, "wise_one", "wise_one_dream_walker")
#Aiel Soldiers
upgrade2(troops, "aiel_recruit_soldier", "aiel_recruit_lithe", "aiel_recruit_bulky")

upgrade2(troops, "aiel_recruit_lithe", "aiel_raider", "aiel_recruit_athletic")
upgrade2(troops, "aiel_raider", "knife_hand", "night_spear")

upgrade2(troops, "aiel_recruit_athletic", "aiel_runner", "aiel_scout")
upgrade2(troops, "aiel_runner", "dawn_runner", "mountain_dancer")
upgrade2(troops, "aiel_scout", "maiden_of_the_spear", "water_seeker")

upgrade2(troops, "aiel_recruit_bulky", "aiel_enforcer", "aiel_recruit_warrior")
upgrade2(troops, "aiel_enforcer", "stone_dog", "red_shield")

upgrade2(troops, "aiel_recruit_warrior", "aiel_brute", "aiel_grappler")
upgrade2(troops, "aiel_brute", "brother_of_the_eagle", "brotherless")
upgrade2(troops, "aiel_grappler", "black_eye", "true_blood")


##### Seanchan

#upgrade2(troops, "seanchan_recruit", "seanchan_recruit_channeler", "seanchan_recruit_soldier")
#Channlers
upgrade(troops, "seanchan_recruit_channeler", "suldam")
upgrade(troops, "suldam", "der_suldam") # no upgrade path to damane because they will spawn with their sul'dam
upgrade(troops, "damane", "damane_veteran") # only upgrade within the damane class
#Soldiers
#upgrade2(troops, "seanchan_recruit_soldier", "seanchan_armsman", "seanchan_conquered_ally")

upgrade2(troops, "seanchan_armsman", "seanchan_footman", "seanchan_scout")

upgrade2(troops, "seanchan_footman", "seanchan_swordsman", "seanchan_bowman")
upgrade2(troops, "seanchan_swordsman", "seanchan_pikeman", "seanchan_blademaster")
upgrade(troops, "seanchan_blademaster", "seanchan_deathwatch_guard"),
upgrade(troops, "seanchan_pikeman", "seanchan_halberdier")
upgrade2(troops, "seanchan_bowman", "seanchan_marksman", "seanchan_crossbowman")

upgrade(troops, "seanchan_scout", "seanchan_man_at_arms") # seanchan_morat_torm
upgrade2(troops, "seanchan_man_at_arms", "seanchan_lancer", "seanchan_skirmisher")
upgrade(troops, "seanchan_lancer", "seanchan_captain")
#Conquered Allies
#upgrade2(troops, "seanchan_conquered_ally", "seanchan_tarabon_ally", "seanchan_conquered_ally_middle")
upgrade2(troops, "seanchan_tarabon_ally", "tarabon_bowman", "tarabon_scout")
#upgrade2(troops, "seanchan_conquered_ally_middle", "seanchan_amadicia_ally", "seanchan_altara_ally")
upgrade2(troops, "seanchan_amadicia_ally", "amadicia_pikeman", "whitecloak_man_at_arms")
upgrade2(troops, "seanchan_altara_ally", "altara_swordsman", "altara_knife_thrower")


##### Shadowspawn

#upgrade2(troops,"shadowspawn_recruit","shadowspawn_recruit_creature","shadowspawn_recruit_human")
#Creatures
upgrade(troops,"shadowspawn_recruit_creature","trolloc_grunt")
upgrade2(troops,"trolloc_grunt","trolloc_hewer","trolloc_archer")
upgrade(troops,"trolloc_hewer","trolloc_berserker")
upgrade(troops,"trolloc_berserker","trolloc_clan_chief")
upgrade(troops,"trolloc_clan_chief","myrddraal")
upgrade(troops,"trolloc_archer","trolloc_stalker")
upgrade(troops,"trolloc_stalker","draghkar")
#Darkfriends
#upgrade2(troops,"shadowspawn_recruit_human","darkfriend_channeler","darkfriend_initiate")
upgrade(troops,"darkfriend_channeler","darkfriend_wilder")
upgrade(troops,"darkfriend_wilder","dreadlord")
upgrade(troops,"darkfriend_channeler_female","aes_sedai_black")
upgrade2(troops,"darkfriend_initiate","darkfriend_murderer","darkfriend_ambusher")
upgrade(troops,"darkfriend_murderer","darkfriend_assassin")
upgrade2(troops,"darkfriend_ambusher","darkfriend_leader","darkfriend_marksman")


##### Shara

upgrade2(troops,"shara_recruit","shara_armsman","shara_scout"),
upgrade2(troops,"shara_armsman","shara_town_guard","shara_bowman"),
upgrade2(troops,"shara_town_guard","shara_border_guard","shara_swordsman"),
upgrade(troops,"shara_border_guard","shara_defender"),
upgrade(troops,"shara_swordsman","shara_captain"),
upgrade2(troops,"shara_bowman","shara_marksman","shara_crossbowman"),
upgrade2(troops,"shara_scout","shara_man_at_arms","shara_skirmisher"),
upgrade(troops,"shara_man_at_arms","shara_shbo_guardsman"),

upgrade(troops,"ayyad_villager","ayyad_village_leader"),
upgrade(troops,"ayyad_village_leader","ayyad_counsel_member"),


##### Sea Folk

upgrade2(troops,"sea_folk_recruit","sea_folk_bilge_hand","sea_folk_weatherly"),
upgrade2(troops,"sea_folk_bilge_hand","sea_folk_deck_hand","sea_folk_dogwatcher"),
upgrade(troops,"sea_folk_deck_hand","sea_folk_boatswain"),
upgrade(troops,"sea_folk_boatswain","sea_folk_cargomaster"),
upgrade(troops,"sea_folk_dogwatcher","sea_folk_deck_defender"),
upgrade(troops,"sea_folk_weatherly","sea_folk_quarterling"),
upgrade(troops,"sea_folk_quarterling","sea_folk_sailmistress"),
upgrade(troops,"sea_folk_sailmistress","sea_folk_wavemistress"),

upgrade(troops,"sea_folk_recruit_channeler","sea_folk_pupil"),
upgrade(troops,"sea_folk_pupil","sea_folk_windfinder"),


##### Land of Madmen

upgrade2(troops,"madmen_recruit","madmen_wanderer","madmen_horse_tamer"),
upgrade2(troops,"madmen_wanderer","madmen_villager","madmen_hunter"),
upgrade2(troops,"madmen_villager","madmen_clansman","madmen_looter"),
upgrade(troops,"madmen_clansman","madmen_chieftan"),
upgrade(troops,"madmen_looter","madmen_pillager"),
upgrade(troops,"madmen_hunter","madmen_ambusher"),
upgrade(troops,"madmen_ambusher","madmen_assassin"),
upgrade2(troops,"madmen_horse_tamer","madmen_slave_catcher","madmen_plains_rider"),
upgrade(troops,"madmen_slave_catcher","madmen_thunderhoof"),

upgrade(troops,"madmen_air_shifter","madmen_fire_tamer"),
upgrade(troops,"madmen_fire_tamer","madmen_storm_caller"),


##### Toman Head

upgrade2(troops,"toman_head_recruit","toman_head_footman","toman_head_scout"),
upgrade2(troops,"toman_head_footman","toman_head_city_guard","toman_head_bowman"),


#################################
##### End TGS troop upgrades
#################################

