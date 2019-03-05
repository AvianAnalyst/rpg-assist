# RPG ASSISTER
*(name is a WIP)*

A suite of programs to assist in tabletop rpgs. This includes:  
[***Character Creator***](#character-creator)  
[***Character Manager***](#character-manager)  
[***Notes Manager***](#notes-manager)  
[***Story Helper***](#story-helper)
[***Party Manager***](#party-manager)  
[***Reference Guide***](#reference-guide)  
[***Item Generator***](#item-generator)  
[***NPC Generator***](#npc-generator)  
[***Encounter Generator***](#encounter-generator)  
[***Combat Manager***](#combat-manager)  
[***Location Generator***](#location-generator)  
[***Dungeon Generator***](#dungeon-generator)  
[***Future Plans***](#future-plans)  
[***Credits***](#credits)  

## Character Creator
This will walk players through creating characters in supported rpgs, and export the character to the [character
management system](#character-manager).
##### Supported RPGS   
- numanera (WIP)
##### Planned support
- dnd5e
- pathfinder
- monster of the week
- feel free to add requests!
___
## Character Manager
This will manage a player's character throughout play. This includes:
- health tracking
- inventory tracking
- spell tracking
- leveling up
- status effects  
it will also allow rolling a specific skill by clicking on that skill. (or system equivalent functionality.)
___
## Notes Manager
A place to compile notes. For players this will be points of interest they've picked up from the GM, for the GM this 
should support story planning including tracking character and story arcs.  
This will also allow for session summaries.
___
## Story Helper
This will generate situationally aware prompts to assist players and gms when they encounter a creativity block for how 
introduce something, or play a situation. For Numanera, this will double as a weird generator.
___
## Party Manager  
This will allow a GM to hold a party of characters. It will be used in the [Encounter Generator](#encounter-generator)
___
## Reference Guide  
This will be more or less an encyclopedia for the various systems. It will be broken down into separate RPGS. Followed 
by relevant categories.
#### RPGs
- ##### Numanera (WIP)
  - Characters
    - Types
    - Descriptors
    - Foci
  - Bestiary
  - Tech
    - Cyphers
      - aeotic
      - occultic
    - Artifacts
    - Oddities
  - Rules
    - wip
- ##### DND5 (TODO)
- ##### Pathfinder (TODO)
- ##### Monster of the Week (TODO)
___
## Item Generator
This will hold a catalogue of items which the GM can then pull one from to give to players. Implementation will be 
vary slightly depending on system and type. 
- Numanera
  - Cyphers  
    > This will be implemented through a 'deck' of cyphers and will be drawn at random. They will be weighted so that 
    less drawn cards will be drawn more likely. You will be able to specify drawing an aeotic cypher, an occultic cypher 
    or just draw in general.
  - Artifacts
    > Artifacts will similarly be drawn from a 'deck' with same draw logic. 
  - Oddities
    > See above
- DND5
  - wip
___
## NPC Generator
This will generate NPC skeletons for the gm on domand when they need one. 
The skeleton might be broken up into system specifics, I'm not sure as of yet. Planned skeletons currently look like:
> Name  
  Species  
  Occupation  
  Motivation  
  One word personality type  
  Quirk  
  
You will also be able to set a custom skeleton to add personal  desired adjectives.
___
## Encounter Generator
This will generate beasts and other creatures for a gm to have their players fight. It will interface with the 
[Party Manager](#party-manager) to allow a gm to select a desired difficulty for the fight, and a location. The 
generator will do the rest. It will then export the fight into the [Combat Manager](#combat-manager)
___
## Combat Manager
The combat manager will allow for the gm entering custom fight parameters, or importing them. Either from the 
[Encounter Generator](#encounter-generator), manually selecting beasts/players/npcs, or an (undecided) import format.
___
## Location Generator
This will allow for quick generation of locations. This will potentially allow for different categories such as 
'starting off places' or ??? I don't know. If you have ideas, please send them to me!
- Location skeletons will look something like:
  > Adjective  
  Type  
  Location in world
 > Please send words to fill in each of those things, thank you!
___
## Dungeon Generator
I want this functionality, but I'm not sure how to present it yet. Potentially prints out a map for the GM with 
trap/treasure locations, possibly NPCs too.  
Planned features once networked include:
  - hidden areas based on player group and dm vs player
  - hidden items based on the same.
___
## Future Plans
Once I have this all working locally, I would like to implement some networking features.  
- v1 features 
  - character sheet synchronization.
    > - Player made changes reflect for the gm 
    > - Gms can remotely manage character sheets
- Potential v2 features 
  - Support distance games
    > - Game chat
    > - Audio/video calls
    > - Some form of play by post functionality (suggestions on how you'd like to see this implemented are welcome.) 
- Potential v3 features
  - The ability to post ads
    > - Gms searching for players
    > - Players that are searching for games.
___
## Credits
***Author:*** 
- Kylan Byrd  

***Feature Suggestions:***
- Amos - Suggested the [Location Generator](#location-generator).
  >Thank you, Amos!  
- Matt - Suggested the [Dungeon Generator](#dungeon-generator), session summary functionality in the 
[Notes Manager](#notes-manager), automatic player sorting of skill checks, recently viewed items in the 
[Reference Guide](@reference-guide) and the [Story Helper](#story-helper).
  > Thank you, Matt!
- Andi - Suggested the [Notes Manager](#notes-manager).
  > Thank you, Andi!
- Skye - Suggested adding Species and Occupation to the [NPC Generator](#npc-generator).
  > Thank you, Skye!
- Dominares - Suggested adding quirks to the [NPC Generator](#npc-generator). Their suggestions also gave me the idea 
for allowing custom NPC skeletons.
  > Thank you, Dominares! 
___
