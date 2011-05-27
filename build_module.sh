#!/bin/sh
mv ./module_info.py ./module_info.py.bak
echo "export_dir = \"The Gathering Storm/\"" > ./module_info.py
mv ~/.wine/drive_c/Program\ Files\ \(x86\)/Steam/steamapps/common/mountblade\ warband/Modules/The\ Gathering\ Storm/ .
python2 process_init.py
python2 process_global_variables.py
python2 process_strings.py
python2 process_skills.py
python2 process_music.py
python2 process_animations.py
python2 process_meshes.py
python2 process_sounds.py
python2 process_skins.py
python2 process_map_icons.py
python2 process_factions.py
python2 process_items.py
python2 process_scenes.py
python2 process_troops.py
python2 process_particle_sys.py
python2 process_scene_props.py
python2 process_tableau_materials.py
python2 process_presentations.py
python2 process_party_tmps.py
python2 process_parties.py
python2 process_quests.py
python2 process_info_pages.py
python2 process_scripts.py
python2 process_mission_tmps.py
python2 process_game_menus.py
python2 process_simple_triggers.py
python2 process_dialogs.py
python2 process_global_variables_unused.py
python2 process_postfx.py
mv ./module_info.py.bak ./module_info.py
mv ./The\ Gathering\ Storm ~/.wine/drive_c/Program\ Files\ \(x86\)/Steam/steamapps/common/mountblade\ warband/Modules/
rm *.pyc
echo ''
echo '______________________________'
echo ''
echo 'Script processing has ended.'
read -sn 1 -p 'Press any key to exit. . .'
echo ''
exit
