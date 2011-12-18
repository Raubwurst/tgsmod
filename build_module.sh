#!/bin/sh
if [ -f ./module_info.py ] ; then
	echo "module_info exists, temporarily appending .bak"
	mv ./module_info.py ./module_info.py.bak
else
	echo "module_info does not exist, I will create it"
fi

echo "export_dir = \"The Gathering Storm/\"" > ./module_info.py

echo "moving module folder to build..."
mv ~/.wine/drive_c/Program\ Files\ \(x86\)/Mount\&Blade\ Warband/Modules/The\ Gathering\ Storm/ .

echo "copying resources..."

copydirs=( Data languages Music Resource SceneObj Sounds Textures )
for directory in ${copydirs[@]} ; do
	echo "copying $directory to target" 
	rsync -r --exclude=.svn ./$directory/ ./The\ Gathering\ Storm/$directory
done

echo "copying module.ini to target"
cp ./module.ini ./The\ Gathering\ Storm

echo "beginning build..."
echo "-------------------------------------------"
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
echo "-------------------------------------------"
echo "finished build"
if [ -f ./module_info.py.bak ] ; then
	echo "moving old module_info back"
	mv ./module_info.py.bak ./module_info.py 
fi
mv ./The\ Gathering\ Storm ~/.wine/drive_c/Program\ Files\ \(x86\)/Mount\&Blade\ Warband/Modules/
rm *.pyc
echo ''
echo '______________________________'
echo ''
echo 'Script processing has ended.'
read -sn 1 -p 'Press any key to exit. . .'
echo ''
exit
