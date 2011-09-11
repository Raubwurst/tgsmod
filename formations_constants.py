# Formations for Warband by Motomataru
# rel. 12/26/10

#Formation modes
formation_none	= 0
formation_default	= 1
formation_ranks	= 2
formation_shield	= 3
formation_wedge	= 4
formation_square	= 5

#Formation tweaks
formation_minimum_spacing	= 67
formation_start_spread_out	= 2
formation_min_foot_troops	= 12
formation_min_cavalry_troops	= 5
formation_autorotate_at_player	= 1
formation_native_ai_use_formation = 1
formation_delay_for_spawn	= .4

from module_constants import slot_town_rebellion_readiness, slot_town_arena_melee_mission_tpl

#Other constants (not tweaks)
Third_Max_Weapon_Length = 250 / 3
#slot_party_cabadrin_order_d0 = slot_town_arena_melee_mission_tpl #78
slot_party_gk_order          = 108 #slot_town_rebellion_readiness #77

###################################################################################
# AutoLoot: Modified Constants
# Most of these are slot definitions, make sure they do not clash with your mod's other slot usage
###################################################################################
# This is an item slot
# slot_item_difficulty = 5

# # Autoloot improved by rubik begin
# slot_item_weight                  = 6

# slot_item_cant_on_horseback       = 10
# slot_item_type_not_for_sell       = 11
# slot_item_modifier_multiplier     = 12

slot_item_needs_two_hands	= 41
slot_item_length	= 42
slot_item_speed	= 43
slot_item_thrust_damage	= 44
slot_item_swing_damage	= 45

slot_item_head_armor	= slot_item_needs_two_hands
slot_item_body_armor	= slot_item_thrust_damage
slot_item_leg_armor	= slot_item_swing_damage

slot_item_horse_speed	= slot_item_needs_two_hands
slot_item_horse_armor	= slot_item_thrust_damage
slot_item_horse_charge	= slot_item_swing_damage
# # Autoloot end


#slots used instead of more global variables
slot_team_faction                      = 0
slot_team_default_formation            = 1
slot_team_reinforcement_stage          = 2
#Reset with every call of Store_Battlegroup_Data
slot_team_size                         = 3
slot_team_adj_size                     = 4 #used in formAI
slot_team_level                        = 5
slot_team_num_infantry                 = 6
slot_team_num_archers                  = 7
slot_team_num_cavalry                  = 8
slot_team_percent_ranged_throw         = 9
slot_team_percent_cavalry_are_archers  = 10
slot_team_archers_have_ammo            = 11
slot_team_avg_x                        = 12 # **used instead of POS registers
slot_team_avg_y                        = 13 # **used instead of POS registers
slot_team_d0_size                      = 14 #plus 8 more for the other divisions
slot_team_d0_level                     = 23 #plus 8 more for the other divisions
slot_team_d0_weapon_length             = 32 #plus 8 more for the other divisions
slot_team_d0_x                         = 41 #plus 8 more for the other divisions **used instead of POS registers
slot_team_d0_y                         = 50 #plus 8 more for the other divisions **used instead of POS registers
#End Reset Group
slot_team_d0_type                      = 59 #plus 8 more for the other divisions
slot_team_d0_move_order                = 68 #plus 8 more for the other divisions
slot_team_d0_formation                 = 77 #plus 8 more for the other divisions
slot_team_d0_first_member              = 86 #plus 8 more for the other divisions
slot_team_d0_formation_x               = 95 #plus 8 more for the other divisions
slot_team_d0_formation_y               = 104 #plus 8 more for the other divisions
slot_team_d0_formation_zrot            = 113 #plus 8 more for the other divisions
slot_team_d0_formation_space           = 122 #plus 8 more for the other divisions

reset_team_stats_begin = slot_team_size  
reset_team_stats_end   = slot_team_d0_y + 8 + 1

#Slot Division Type definitions
sdt_infantry   = 0
sdt_archer     = 1
sdt_cavalry    = 2
sdt_polearm    = 3
sdt_skirmisher = 4
sdt_harcher    = 5
sdt_support    = 6
sdt_bodyguard  = 7
sdt_unknown    = -1

scratch_team   = 7


