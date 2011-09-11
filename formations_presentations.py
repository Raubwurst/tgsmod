# Formations AI for Warband by Motomataru
# rel. 12/26/10
# EDIT FOR ORDER DISPLAY 11/19/10 by Caba'drin

from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
import string

####################################################################################################################
#  Each presentation record contains the following fields:
#  1) Presentation id: used for referencing presentations in other files. The prefix prsnt_ is automatically added before each presentation id.
#  2) Presentation flags. See header_presentations.py for a list of available flags
#  3) Presentation background mesh: See module_meshes.py for a list of available background meshes
#  4) Triggers: Simple triggers that are associated with the presentation
####################################################################################################################

# the following code block is to be inserted into "battle" presentation's trigger for ti_on_presentation_event_state_change
# just before the line (call_script, "script_update_order_flags_on_map"),
code_block1=[
# formations by motomataru
		  (assign, ":fixed_point_multiplier", 1),
		  (convert_to_fixed_point, ":fixed_point_multiplier"),
		  (set_fixed_point_multiplier, 100),
		  (call_script, "script_team_get_position_of_enemies", pos60, "$fplayer_team_no", grc_everyone),
		  (copy_position, pos1, pos3),
		  (try_for_range, ":battle_group", 0, 9),
		    (class_is_listening_order, "$fplayer_team_no", ":battle_group"),
			(store_add, ":slot", slot_team_d0_size, ":battle_group"),
			(team_slot_ge, "$fplayer_team_no", ":slot", 1),
			(team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
			(store_add, ":slot", slot_team_d0_formation, ":battle_group"),
			(neg|team_slot_eq, "$fplayer_team_no", ":slot", formation_none),			
			(team_get_slot, ":fformation", "$fplayer_team_no", ":slot"),
			(store_add, ":slot", slot_team_d0_formation_space, ":battle_group"),
		    (team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
			
			(call_script, "script_point_y_toward_position", pos1, pos60),
			(call_script, "script_set_formation_position", "$fplayer_team_no", ":battle_group", pos1),
			(try_begin),
				(store_add, ":slot", slot_team_d0_type, ":battle_group"),
				(team_get_slot, ":sd_type", "$fplayer_team_no", ":slot"),
				(neq, ":sd_type", sdt_cavalry),
				(neq, ":sd_type", sdt_harcher),
				
				(call_script, "script_get_centering_amount", ":fformation", ":troop_count", ":div_spacing"),
				(try_begin),
					(this_or_next|eq, ":sd_type", sdt_archer),
					(eq, ":sd_type", sdt_skirmisher),
					(val_mul, reg0, -1),
					(assign, ":script", "script_form_archers"),
				(else_try),
					(assign, ":script", "script_form_infantry"),
				(try_end),
				(position_move_x, pos1, reg0),
			(else_try),
				(assign, ":script", "script_form_cavalry"),
			(try_end),
			(call_script, ":script", "$fplayer_team_no", "$fplayer_agent_no", ":battle_group", ":div_spacing", ":fformation"),		
		    (store_add, ":slot", slot_team_d0_move_order, ":battle_group"),
			(team_set_slot, "$fplayer_team_no", ":slot", mordr_hold),
          (try_end), #Battle Group Loop
		  (set_fixed_point_multiplier, ":fixed_point_multiplier"),
# end formations
          (call_script, "script_update_order_flags_on_map"),
]


def modmerge(var_set):
	try:
		from modmerger_options import module_sys_info
		version = module_sys_info["version"]
	except:
		version = 1127 # version not specified.  assume latest warband at this time

	try:
		var_name_1 = "presentations"
		orig_presentations = var_set[var_name_1]

		# START do your own stuff to do merging

		modmerge_formations_presentations(orig_presentations)

		# END do your own stuff
            
	except KeyError:
		errstring = "Variable set does not contain expected variable: \"%s\"." % var_name_1
		raise ValueError(errstring)



from util_common import *
from util_wrappers import *
from util_presentations import *

def modmerge_formations_presentations(orig_presentations):
   # add_objects(orig_presentations, formations_presentations, True)	#add_presentations doesn't work
	
    # inject code into battle presentation
    try:
        find_i = list_find_first_match_i( orig_presentations, "battle" )
        battlep = PresentationWrapper(orig_presentations[find_i])
        codeblock = battlep.FindTrigger(ti_on_presentation_event_state_change).GetOpBlock()
        pos = codeblock.FindLineMatching( (call_script, "script_update_order_flags_on_map") )
        codeblock.InsertBefore(pos, code_block1)			
    except:
        import sys
        print "Injecton 1 failed:", sys.exc_info()[1]
        raise
