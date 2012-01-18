Pre-Battle Orders & Deployment by Caba'drin
v0.91 beta - 21 Dec 2011

*Shield Bash added (hold block, hit attack)
*Mostly small bugfixes and code optimizations.
*PBOD code separated to a ModMerger "kit"


Version 0.90 - The Long Overdue Version

New Features:
*Animated, properly functioning, Spear Bracing (animations courtesy of
Papa Larazou)! Found under your Attack Order menu (default F7-F7).
To brace your own polearm, hit B by default.
*Fully Map-able Keys for new orders, spear bracing, and "whistle for horse"
in addition to the fully map-able keys for the Custom Camera from before
Access key configuration from the PBOD Preferences menu under Camp-Take an Action.
*New AI for using special attack orders (Spear Bracing, Skirmish mode,
and Volley Fire). Enable/Disable in PBOD Preferences. DEFAULTS OFF.
*New Troop Management Option: Split Troops into Multiple Divisions allows you
to split the same troop type into more than one division (so, say, you can have
half your Swadian knights in the cav division and the other half as a personal
bodyguard). Choose the % of every spawn that you want split to the 'secondary divison'
up to 50% of the troops of that type, and select the secondary division. This
setting is stored and used in all battles (but can be disabled in its screen,
while maintaining your settings). Manage this in your Camp->Take an Action
menu.
*New "in between" Battle AI--Native AI, but uses formations to carry them out
DEFAULTS to NATIVE AI (other options "Formations" and "Native AI w/Formations")
*Weather-based penalties to all troops' ranged weapon proficiencies. DEFAULTS ON.
*'Backspace Battle Menu' now includes new flags for every division, not
just 1-3 (Infantry, Archers, Cavalry)
*Preference screen now includes mouse-over option tips

Fixes/Updates:
*Updated to most recent 'dev' version of motomataru's formations
*AI fixes for players who change the division of troops, so the AI won't be
crippled by your assignments in the Party Window
*Bugfixes for pre-battle orders including formations (should stop divisions
running across the map right after spawn)
*Toned polearm damage tweak down; other small tweaks
*The new order display should disappear with a press of 'ESC' or 'F9'
*Updated to Warband v1.143; includes Caba's "fix" for lords of defeated 
factions, preventing them from respawning if their factions have no fiefs 
(reverting faction defeat behavior to v1.134 and before).


As always, you'll find all of these options in your 
Camp - Take an Action menu, under "PBOD Preferences."

---------------
Notes from Previous Versions

***v0.88***
*Chock-full of New In-Battle Features!!!
*New Order: Volley Fire
Order your archers/crossbowmen to fire in unison; archers 1 shot/3 seconds, 
crossbowmen 1 shot/5 seconds. Will override an active skirmish order.
*New Order: Brace Spears
*New Option: Dis/Enable AI to Brace Spears
This is only step one of my integaration/improvements on The Mercenary's
spear bracing kit. Ordering your troops to brace spears, or for the AI
to do so, has them cause extra damage to a charging horse when they are 
stationary. The script does well in indentifying appropriate targets (no 
strange deaths) but the animation yet needs serious work so it looks less 
like horses are dying from fright and more like they are impaled on a row 
of braced pikes. The player should press "B" to brace their polearm.
THIS DEFAULTS "OFF". (Disabled)
*New Option: Battle Continuation - Charge All on KO
Turning this on will give all of your units the "Charge" command when you 
transition to the DeathCam and battle continuation. It will also cancel 
any formation orders so those in formations can charge. With it off, your 
divisions will remain in the last orders they received before you were KO'd.
THIS DEFAULTS "OFF".
*New Option: Foot Archers without Ammo Division Reassignment
Similar to the de-horsed cavalry option, this option sets any archer 
who runs out of ammo to the division the player selects (the AI will get 
shifted to Infantry). It is coded to exclude siege defense situations, 
since archers in siege defenses get their ammo automatically refilled.
THIS DEFAULTS "DISABLED".
*New Orders: Formations
*New Option: Dis/Enable AI use of Formations
Motomataru's battlefield tactics/formations kit has been added, 
allowing the following formations to be ordered: Ranks, Shieldwall, 
Wedge, and Square. These orders are given the same way Native orders 
are given--to whatever groups are selected at that time. (If you've 
played a mod with moto's orders before, you'll notice a difference in
that you can give the orders to all 9 divisions, and specify which 
orders are given to what divisions.)

This includes motomataru's reworked AI that includes the use of 
formations by the AI. Turning this on will activate the new AI and 
formations for non-player teams. Turning it off will maintain Native AI behavior.
THIS DEFAULTS "OFF."

Formations have also been integrated into the Pre-Battle Order display,
so you can set up what formations troops should begin in prior to battle. 
(Note: cavalry-based divisions can only form "Wedges" and foot archer 
based divisions can only complete the "Ranks" order. There isn't any error 
checking in the Order screen; inappropriate orders will simply be 
ignored in battle.) 

**The battle order menus have been changed slightly. Formations has 
been added to F4. You give formation orders beginning with F4 and 
then F4 - F8 for the various formations. The "Skirmish" menu, F7, has 
been renamed the "Attack orders" menu. F4 ends any active special attack 
order (skirmish, volley, spear brace). F5 begins Skirmish mode, 
F6 begins Volley fire, and F7 begins spear bracing.

Oh, and you can whistle to get your horse back by pressing "M".



***v0.86***
*A handful of Bugfixes. No feature changes.

***v0.85***
*Battle Continuation with two DeathCam modes:
a mouse operated free-roving cam and 'follow' mode that can cycle 
through bots still alive. "END" toggles between modes and the mouse
buttons cycle forward (left) and backward (right) among agents. Arrow
keys move the cameras.
*A Custom 'Follow' camera mode for in-battle. Press "END" to toggle
between camera modes. **All camera keys can be adjusted within the PBOD
Mod Preferences option in the Camp Action Menu.
*Pre-Battle order availability in offensive sieges
*Order & Deployment option availability in battles within villages


***v0.8***

PBOD is now "Expanded", changing some battle behavior and adding
a set of orders to that which are available Natively.
Now, you troops can be instructed on exactly which weapon
type to wield, whether or not to use shields, and for ranged
troops whether they should engage in melee combat or not.
These are accessed similarly to Native orders in that you
press a 'F' function key that opens a display outlining
the various orders available and they are given to whichever
divisions are currently selected.

Weapon and shield use orders are cleared by using the Native
"Use Any Weapon" order, or F3-F4.

The new orders are given as follows:
F5 - Weapon Type orders
	F5 - One Handed Weapons
	F6 - Two Handed Weapons
	F7 - Polearms
	F8 - Ranged Weapons (Bows and Thrown)
F6 - Shield Use orders
	F5 - Use Shields (forced)
	F6 - No Shields (forced)
	F7 - Free (don't force either way/default)
F7 - Skirmish orders (only for ranged units)
	F5 - Avoid Melee
	F6 - Stand and Fight (default)

Pressing F9 will close the display for the orders if it
doesn't close on its own.

Further, a series of "Weapon Use Fixes" are included to help
the NPCs choose among their weaponry better in battles.
These can be individually disabled in your Camp Menu, by 
going to Camp Action, selecting PBOD Preferences and 
un-ticking the respective boxes.

-The Lancer fix forces any mounted unit with a lance to use
that weapon at the beginning of a battle. It also forces that
unit to use the lance when mounted and a reasonable distance from
the enemy. Once dismounted or surrounded, a lancer will draw
their non-lance weapon.

-Similarly, the Horse Archer fix forces any mounted unit
that is guaranteed a ranged weapon to use their horse-useable
bow or crossbow. (This will exclude Companions as they are not
marked as having a ranged weapon guaranteed.) They will be forced
to use their bow until they are out of arrows/bolts or dismounted.

-The Spear/Pike/Polearm fix affects foot soldiers who have
a polearm equipped, but do not have any ranged weapons (throwing
or bows/crossbows). They will use their polearm exclusively
until surrounded by enemies, when they will change to their
non-polearm sidearm.

As a player, giving weapon orders (Native "Hold Fire" and 
"Use Blunt Weapons" as well as the new weapon-type specific
orders) will override this behavior, meaning you needn't
fear your troops going against your commands.


***v0.83***

*Bodyguards will join your character in towns and villages
Your repute and leadership earn you the loyalty of your hero companions
to fill this job. You earn 1 bodyguard for each 400 points of renown
and 3 points of the Leadership skill. This defaults ON.

*Original M&B-style feature: De-horsed Cavalry are Re-assigned
You can choose to have de-horsed cavalry (any mounted unit, regardless
of division) be re-assigned to a division of your choosing upon
the death of their mount. This defaults OFF.

*Anti-Cavalry & Horse Trample buffs
Pikes and long spears now do much more damage against horses,
giving them a significant buff in their intended anti-cavalry role.
Similarly, horse bumps/charages are also buffed, depending on the
heaviness of the mount involved. Heavy cavalry charges can now be
quite devastating. Balancing comments welcome on the forum. 
These buffs are paired and default ON, just like the weapon use 
fixes. 