from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

default_kingdom_relations = [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.02),("forest_bandits", -0.02)]
factions = [
  ("no_faction","No Faction",0, 0.9, [], []),
  ("commoners","Commoners",0, 0.1,[("player_faction",0.1)], []),
  ("outlaws","Outlaws", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [], 0x888888),
# Factions before this point are hardwired into the game end their order should not be changed.

  ("neutral","Neutral",0, 0.1,[("player_faction",0.0)], [],0xFFFFFF),
  ("innocents","Innocents", ff_always_hide_label, 0.5,[("outlaws",-0.05)], []),
  ("merchants","Merchants", ff_always_hide_label, 0.5,[("outlaws",-0.5),], []),

  ("dark_knights","{!}Dark Knights", 0, 0.5,[("innocents",-0.9),("player_faction",-0.4)], []),

  ("culture_1",  "{!}culture_1", 0, 0.9, [], []),   # legion
  ("culture_2",  "{!}culture_2", 0, 0.9, [], []),   # band
  ("culture_3",  "{!}culture_3", 0, 0.9, [], []),   # two rivers
  ("culture_4",  "{!}culture_4", 0, 0.9, [], []),   # mayene
  ("culture_5",  "{!}culture_5", 0, 0.9, [], []),   # cairhien
  ("culture_6",  "{!}culture_6", 0, 0.9, [], []),   # illian
  #added for TGS
  ("culture_7",  "{!}culture_7", 0, 0.9, [], []),   # murandy
  ("culture_8",  "{!}culture_8", 0, 0.9, [], []),   # altara
  ("culture_9",  "{!}culture_9", 0, 0.9, [], []),   # arad doman
  ("culture_10",  "{!}culture_10", 0, 0.9, [], []), # tear
  ("culture_11",  "{!}culture_11", 0, 0.9, [], []), # andor
  ("culture_12",  "{!}culture_12", 0, 0.9, [], []), # ghealdan
  ("culture_13",  "{!}culture_13", 0, 0.9, [], []), # far madding
  ("culture_14",  "{!}culture_14", 0, 0.9, [], []), # tarabon
  ("culture_15",  "{!}culture_15", 0, 0.9, [], []), # amadicia
  ("culture_16",  "{!}culture_16", 0, 0.9, [], []), # whitecloaks
  ("culture_17",  "{!}culture_17", 0, 0.9, [], []), # shienar
  ("culture_18",  "{!}culture_18", 0, 0.9, [], []), # arafel
  ("culture_19",  "{!}culture_19", 0, 0.9, [], []), # kandor
  ("culture_20",  "{!}culture_20", 0, 0.9, [], []), # saldaea
  ("culture_21",  "{!}culture_21", 0, 0.9, [], []), # white tower
  ("culture_22",  "{!}culture_22", 0, 0.9, [], []), # aiel nation
  ("culture_23",  "{!}culture_23", 0, 0.9, [], []), # seanchan
  ("culture_24",  "{!}culture_24", 0, 0.9, [], []), # shadowspawn
  ("culture_25",  "{!}culture_25", 0, 0.9, [], []), # shara
  ("culture_26",  "{!}culture_26", 0, 0.9, [], []), # sea folk
  ("culture_27",  "{!}culture_27", 0, 0.9, [], []), # land of madmen
  ("culture_28",  "{!}culture_28", 0, 0.9, [], []), # almoth plain
  #end added for TGS  

#  ("swadian_caravans","Swadian Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),
#  ("vaegir_caravans","Vaegir Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),

  ("player_faction","Player Faction",0, 0.9, [], []),
  ("player_supporters_faction","Player's Supporters",0, 0.9, [("player_faction",1.00),("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.05)], [], 0xFF4433), #changed name so that can tell difference if shows up on map
  #edited for TGS
  ("kingdom_1",  "the Legion of the Dragon", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.05)], [], 0xFF6600),#Kingdom of Swadia 
  ("kingdom_2",  "the Band of the Red Hand",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.05)], [], 0x003300),#Kingdom of Vaegirs 
  ("kingdom_3",  "the Two Rivers", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.05)], [], 0x663300),#Khergit Khanate 
  ("kingdom_4",  "the City-State of Mayene",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.05)], [], 0xFF3366),#Kingdom of Nords 
  ("kingdom_5",  "the Nation of Cairhien",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.05)], [], 0x00248E),#Kingdom of Rhodoks 
  ("kingdom_6",  "the Nation of Illian",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.05)], [], 0xFFCC00),#Sarranid Sultanate 
  ("kingdom_7",  "the Nation of Murandy",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.05)], [], 0xFEBFBF),#New Faction
  ("kingdom_8",  "the Nation of Altara",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.5)], [], 0x660000),#New Faction
  ("kingdom_9",  "the Nation of Arad Doman",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.5)], [], 0x47006B),#New Faction
  ("kingdom_10",  "the Nation of Tear",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.5)], [], 0xCC0099),#New Faction
  ("kingdom_11",  "the Nation of Andor",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.5)], [], 0xFF0000),#New Faction
  ("kingdom_12",  "the Nation of Ghealdan",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.5)], [], 0x008E00),#New Faction
  ("kingdom_13",  "the City-State of Far Madding",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.5)], [], 0x24006B),#New Faction
  ("kingdom_14",  "the Nation of Tarabon",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.5)], [], 0x99FF00),#New Faction
  ("kingdom_15",  "the Nation of Amadicia",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.5)], [], 0x646060),#New Faction
  ("kingdom_16",  "the Children of the Light",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.5)], [], 0xFFFFFF),#New Faction
  ("kingdom_17",  "the Nation of Shienar",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.5)], [], 0x0033CC),#New Faction
  ("kingdom_18",  "the Nation of Arafel",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.5)], [], 0xFE80DF),#New Faction
  ("kingdom_19",  "the Nation of Kandor",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.5)], [], 0x6BB200),#New Faction
  ("kingdom_20",  "the Nation of Saldaea",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.5)], [], 0x009999),#New Faction
  ("kingdom_21",  "the White Tower",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.5)], [], 0x80FFFE),#New Faction
  ("kingdom_22",  "the Aiel Nation",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.5)], [], 0xFFFF66),#New Faction
  ("kingdom_23",  "the Seanchan Empire",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.5)], [], 0x660099),#New Faction
  ("kingdom_24",  "the Shadowspawn",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", 0.5)], [], 0x000000),#New Faction
  ("kingdom_25",  "the Nation of Shara",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.5)], [], 0x363333),#New Faction
  ("kingdom_26",  "the Sea Folk",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.5)], [], 0x007D47),#New Faction
  ("kingdom_27",  "the Land of Madmen",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.5)], [], 0x006B6B),#New Faction
  ("kingdom_28",  "the Land of Toman Head",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05), ("trollocs", -0.5)], [], 0x00CC00),#New Faction
  #end edited for TGS

##  ("kingdom_1_rebels",  "Swadian rebels", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_2_rebels",  "Vaegir rebels",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_3_rebels",  "Khergit rebels", 0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_4_rebels",  "Nord rebels",    0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),
##  ("kingdom_5_rebels",  "Rhodok rebels",  0, 0.9, [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.02),("mountain_bandits", -0.05),("forest_bandits", -0.05)], [], 0xCC2211),

  ("kingdoms_end","{!}kingdoms_end", 0, 0,[], []),

  ("robber_knights",  "{!}robber_knights", 0, 0.1, [], []),

  ("khergits","{!}Khergits", 0, 0.5,[("player_faction",0.0)], []),
  ("black_khergits","{!}Black Khergits", 0, 0.5,[("player_faction",-0.3),("kingdom_1",-0.02),("kingdom_2",-0.02)], []),

##  ("rebel_peasants","Rebel Peasants", 0, 0.5,[("vaegirs",-0.5),("player_faction",0.0)], []),

  #edited for TGS
  ("manhunters","Children of the Light", 0, 0.5,[("outlaws",-0.6),("player_faction",0.1)], []),#Manhunters
  #end edited for TGS
  ("deserters","Deserters", 0, 0.5,[("manhunters",-0.6),("merchants",-0.5),("player_faction",-0.1)], [], 0x888888),
  ("mountain_bandits","Mountain Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),
  ("forest_bandits","Forest Bandits", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15)], [], 0x888888),
  #new for TGS
  ("trollocs","Marauding Trollocs", 0, 0.5,[("commoners",-0.2),("merchants",-0.5),("manhunters",-0.6),("player_faction",-0.15), ("kingdom_24",0.5)], [], 0x000000),
  #end new for TGS

  ("undeads","{!}Undeads", max_player_rating(-30), 0.5,[("commoners",-0.7),("player_faction",-0.5)], []),
  ("slavers","{!}Slavers", 0, 0.1, [], []),
  ("peasant_rebels","{!}Peasant Rebels", 0, 1.0,[("noble_refugees",-1.0),("player_faction",-0.4)], []),
  ("noble_refugees","{!}Noble Refugees", 0, 0.5,[], []),
]

##diplomacy start+ Define these for convenience
dplmc_factions_begin = 1 #As mentioned in the notes above, this is hardcoded and shouldn't be altered.  Deliberately excludes "no faction".
dplmc_non_generic_factions_begin = [x[0] for x in enumerate(factions) if x[1][0] == "merchants"][0] + 1
dplmc_factions_end   = len(factions)
##diplomacy end+
