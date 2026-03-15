# sakuraUnlocker
100% save game downloader for XBMC4Xbox/XBMC4Gamers, specifically for use in Insignia lobbies that require (or benefit from) 100% unlocked content. 

<p align="center">
  <img src="https://github.com/faithvoid/script.sakuraUnlocker/blob/main/icon.png?raw=true" alt="sakuraUnlocker"/>
</p>

# Installation:
- Download the latest release from the Releases section of this repository
- Extract the .zip and copy "script.program.sakuraUnlocker" to "Q:/home/addons/"
- In your XBMC flavour of choice, go into your addon settings, enable the script, and then run it.
- Select the game you'd like to download a save file for, and follow the on-screen instructions carefully.
- **This has the risk of overwriting data you care about, so PLEASE read every single option on screen, select "Yes" to back up your game's save folder when requested if you have anything in that game you don't want to lose, and don't button-mash through the prompts, as you might overwrite something. I take zero responsibility if you overwrite your game's existing save data because you didn't read these instructions.**
- ???
- Profit! You're now ready to hop on Insignia with the same loadouts/maps/etc as other users!

## TODO
- Implement Rocky5's save-game signing algorithm for games such as Forza Motorsport

## FAQ
- "Why?"

A lot of Xbox Live titles have progression-based rewards. This is fantastic in concept, but not everyone these days has the time to 100% a game just to be on the same level as everyone else online, and some games are fairly strict about everyone having the same things available, or some games, like Project Gotham Racing 2, simply just aren't as fun to play online when one or more players only have early-game content. 
- "Will you upload non-Insignia game saves here?"

Probably not. This is meant to specifically target Insignia-supported games and make setting them up as hassle-free as possible, as having minimal unlocks can either stop users from joining certain lobbies, or limit everyone's options in what they can do in said lobbies. For singleplayer, you should focus on actually playing those games and have fun! And if you REALLY don't want to finish those games yourself, GameFAQs has you covered with hundreds of 100% save files for basically every Xbox game under the sun.
- "Why isn't (insert Insignia game here) available?"

A handful of games require their save games to be signed with HDD keys, meaning you can't just download them directly without signing them with an external utility. These games are temporarily left out until Rocky5's save game hash algorithm is implemented.

## Credits
- Mobcat - TitleID database, used for converting titleIDs to game titles!
- Pacific Muscle crew - Inspiration for the utility (as we were discusisng ways to make joining PGR2 lobbies as simple as possible for newbies).
- Insignia Team - For giving me a reason to make a utility like this!
- BigBucks000100 - Thorough 100% savegame catalog from his "Xbox Save Installer" project, saved me an ungodly amount of work.
- Rocky5 - Save hash calculation algorithm
- FlatIcons - Pink padlock icon
