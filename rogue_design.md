This game-design content was captured from:
https://groups.google.com/g/rec.games.roguelike.angband/c/ijo3FdsuE0s


The Rational Design of a Roguelike.
37 views
Subscribe 
Graaagh the Mighty's profile photo
Graaagh the Mighty
unread,
Apr 30, 2001, 8:41:45 AM
to
Lots of postings here (and in rec.games.roguelike.adom as a matter of
fact) have illuminated a number of issues with current roguelikes. The
following chart illustrates these. The chart includes every RPG I've
played, with emphasis on CRPGs, particularly roguelikes, and
especially Angband variants, and a few I haven't but know something
about.
Key:
Lifesaving column:
T -- indicates survival tactics require teleportation capabilities and
massive detection capabilities.
(Undesirable because it is bad roleplay, removes some strategic
elements one could otherwise have, and virtually forces the use
of heavy-handed game mechanics around vaults, special levels,
&c -- also, the need for massive detection leads to the
availability of massive detection, which then erases the element
of surprise or at least vastly reduces it!).
S -- indicates survival tactics require speed. (Neutral but see
scumming.)
A -- indicates the game has an Amulet of Life-Saving, or similar.
(Neutral.)
AA -- indicates the game has an Amulet of Life-Saving or similar, and
this item is fairly important, if not absolutely essential.
(Undesirable, as making these too rare will make the game
unplayable; if it's not unplayable it's probably scummable making
invincible munchkins possible.)
N -- indicates nonpermanent death (generally accompanied by limiting
when/where you can save the game, so as to prevent both fux0ring
yourself by saving just before an unavoidable death and
munchkinism (save, try something dangerous, die, restore, repeat
until you don't die, ...)). (Note: Deaths that are nonpermanent
only with a special, consumable item (e.g. AoLS, blood of life
potion) do not count here; these earn the game an A and if these
are made crucial the game earns an AA.) (Neutral, but arguably
the resulting game is not a roguelike.)
I -- indicates temporary invulnerability is available in the game.
(Neutral, but undesirable if too common.)
II -- indicates use of invulnerability is necessary (at least, barring
exreeme luck) to win the game.
Items column:
I -- Easy to identify stuff/detect bad stuff/whatever, and necessary.
(Undesirable -- takes some of the fun out of the game!)
II -- Ditto, plus finding all special powers of artifacts and such.
(Undesirable.)
C -- Hard to identify stuff and easy to wind up with a
nearly-unplayable (or even actually unwinnable) game (or get
killed) due to cursed stuff or lost items. (Can be combined with
I or II; e.g. ADOM has CI because in the early game C holds true
and in the late game I holds true.
E -- Cursed stuff is not a threat, either because it is easily
detected and avoided, easily removed, or just not that bad.
(Mutually exclusive with C.) (Undesirable -- useless gameplay
elements are in general undesirable.)
R -- A weird and questionable mechanism is needed to access stuff
saved somewhere, some locations, or such in reasonable time (e.g.
*band's Word of Recall). (Undesirable -- bad role-play.)
Z -- Saved stuff is prone to destruction, or stuff can't be saved.
(Undesirable usually -- stuff is usually necessary -- symbol
omitted if saving stuff isn't vital or at least highly
desirable.)
Structure column:
T -- indicates themed areas, with certain monsters/items more likely,
and/or in-character drops for monsters. (Desirable. Games with
too little spatial structure, e.g. vanilla Angband, are less
interesting and must rely on temporal structure too heavily to
avoid actually being boring.)
B -- indicates "bad" quests (e.g. random monsters and other stuff that
doesn't make very much sense). (Undesirable: bad roleplay.)
Q -- indicates "good" quests (e.g. in theme for the game).
(End-of-game stuff does not count here; to earn a Q the game must
have quest elements throughought.) (Desirable: good roleplay and
creates an alternative source of character development milestones
that otherwise must come from scumming or pure luck.)
H -- indicates heavy-handed game mechanics are used. (Undesirable.)
HH -- indicates heavy-handed game mechanics are used extensively.
(Undesirable.)
L -- indicates that with increasing dungeon level (or a similar
metric, such as ADOM's "danger factor") stronger monsters and
items become more common. (Desirable: adds spatial and temporal
structure, making the game more interesting.)
LL -- indicates the same as L, but also the game is very linear -- no
real branching or exploring is possible.
V -- indicates vaults, special levels, and so forth are present in
some form. (Desirable: adds spatial structure.)
W -- indicates a wilderness. (Desirable.)
WW -- indicates an unrealistic wilderness: different game mechanics
from the dungeons or other weirdness. (Undesirable IMO.)
Cl -- Character gains levels as part of temporal structure. (Neutral.)
Cs -- Character skills are part of temporal structure. (Neutral.)
Ct -- Characters can alter their stats in-game as part of temporal
structure. (Neutral.)
R -- Game structure has random elements. (Desirable for replay value.)
RR -- Game structure has random elements in spades. (Desirable.)
E -- Game has secrets/Easter eggs. (Desirable.)
Blank -- Undesirable, because a decent RPG needs QL and at least one
of Cl, Cs, Ct for interesting structure -- Q to prevent
scumming from being the main basis for character development,
L to prevent either an unfair early game or munchkinish late
game, and Cl, Cs, or Ct for both.
Spoilers/documentation column:
N -- indicates that reading spoily information is pretty much
necessary to win the game. (Undesirable.)
S -- indicates that reading spoily information is discouraged.
(Neutral.)
D -- indicates that the game has documentation. (Desirable.)
DD -- indicates that the game has excellent documentation.
(Desirable.)
DDD -- indicates that the game has excellent documentation and
moreover this is presented "in-game" in role-played fashion to
the greatest extent possible -- i.e. the outside-the-game-world
manuals only explain getting started, character generation, the
program's interface, and other elements not themselves part of
the role playing proper. (Desirable -- "learn as you go along"
is very good role-playing so long as it isn't slow and
frustrating trial-and-error exclusively!)
C -- indicates that the game designers closed the source code.
(Undesirable.)
CC -- indicates that the game designers closed the source code and
added strict anti-cheating security mechanisms that make it hard
to experiment for knowledge gaining purposes and impact unfairly
legitimate users. (Undesirable.)
Fairness column:
U -- indicates that unfair (i.e. difficult to avoid *and* difficult to
recover from) events can occur in any stage of the game.
Unavoidable deaths are the most common unfair event.
(Undesirable.)
E -- indicates that unfair events are restricted to the
early game. (Undesirable, but less so.)
R -- indicates that unfair events are restricted to the early game
with exceptions, but the exceptions are quite rare.
(Undesirable.)
M -- indicates that munchkins can be created that are unstoppable.
Note that this can be combined with 'U', e.g. Pernangband,
where breeders can cause all kinds of unavoidable deaths to
many characters, but alchemists can become sickeningly
overpowered ubermunchkins. (Undesirable.)
Scumming column:
N -- indicates that the game designers responded to players abusing
scummable features (e.g. stat potions) by making the scumming
*necessary* (e.g. the leap in monster nastiness in Angband at
2000'). (Undesirable.)
T -- indicates that the game designers limited scumming by creating
time or progression limitations of some kind, e.g. finitely many
monsters/items generated whole game, time limit, move limit,
inability to save the game, or similar. (Undesirable.)
U -- indicates that the game designers used something really evil and
unfair to limit some form of scumming, making it exceedingly
dangerous, but with unfair side effects for "legit" characters.
(Undesirable.)
S -- indicates that the game designers limited scumming by rendering
it both unnecessary and either undesirable past a point or
impossible without using any of the above methods. (Desirable.)
M -- indicates that unlimited scumming can create munchkins.
Miscellaneous column:
T -- slow and tedious to start a new character. (Undesirable,
especially in combination with 'E' or 'U' in fairness column.)
R -- you have to be a rocket scientist to start a new character.
(Undesirable -- basicaly you'll be messing with zillions of
options and poring over documentation. Or dying a lot. Or both.)
S -- Starting a new character, it is well-nigh necessary to scum for
high starting stats or something similar. (Undesirable.)
SS -- The game actually has built-in features to assist in automated
scumming for high starting stats or whatever. (Undesirable.)
Z -- Endgame characters of the same race and class don't have much to
distinguish them. (Neutral or undesirable.)
P -- Polymorphing or other random and unpredictable elements make the
game chaotic and reduce its structure.
(Can be combined with Z, when endgame characters are all alike in
that they all polymorph a lot or whatever and play similarly
regardless.) (Undesirable.)
P* -- P, but limited to some race/class combinations (e.g. Zangband
chaos-warrior). (Neutral.)
F -- indicates that every class plays like a fighter, possibly with
spell support. (Undesirable: bad roleplay, *unless* the game only
has classes that should properly be warriors.)
G -- Game has a glut of artifacts. (Undesirable: artifacts should be
rare and special. It's bad role play otherwise.)
M -- Some minor task requires inordinate amounts of the player's
attention, e.g. avoiding starvation or repairing stat drains a
lot. (Undesirable, even if realistic, because *boring*.)
A -- Asymmetrical game mechanics or just plain asymmetrical powers
make monsters very different from the player in e.g. hit points.
(Necessary to some extent if the player is to survive, but
undesirable past a certain point.)
W -- Weird game mechanics. (Undesirable -- catch-all for weird,
unrealistic or bad roleplay game mechanics not covered above.)

All columns:
? -- indicates I don't know everything about this game in this
category. (What I do know will be indicated.)
<number> -- see footnote of corresponding number below table.

Note that this table doesn't discuss bugs or other issues that don't
stem fundamentally from the game's design! It also doesn't address
graphics, sound, performance, disk space, or other issues that are at
most tangential to *gameplay*.

Game |Life|Item|Structure |Docs |Fair|Scumming|Misc
Paper RPGs 1 ClCsCtR1 DD2 M1 T3 TRS2
Zelda III(4) N I TQLVWE5 SDDC S6 ZF7
FFMQ(8) N I TQLLWWClR DDC S9 ZFM10
*Nethack(11) A C? TQHLVClCtRR? ? U ? PW?
ADOM A ICZ TBQHHLVWWCl NSDDCC13 R TM12 FMW14
CsCtRRE14
Angband TSI IIER HLVClCtRR15 ND E16 NS17 RSSZFGA
W18
*Moria TSII IER? HLVClCtRR ND? U NS? TRSZFGAW?
*ZAngband TSI? IIER TBQHLVClCt ND? R NS17 TRSSP*FGA
RRWW W?19
*PernAngband TSAI IIER TBQHLVClCt ND? UM NUM20 TRSSP*FGA
RRWW W?
*SAngband TS IIER HLVCsCtRR? ND? E? NSM?21 TRSSZFGA
W22
*CthAngband TSI? IIER TBQHLVCsCtRR ND? R? NS17 TRSSZFGA
WW W?
OAngband TS IIER THLVClCtRR15 NDD/DDD23 E?24 S25 TSSZGW26
Half-Life(27) N I TQLLVWCsRE28 NDD/DDD29 U30 S6 ZFM31
Quake(27) NI I TQLLVWRE28 NDD R32 S6 ZF
Quake II(27) NI I TQLLVWRE28 NDD/DDD33 R32 S6 ZF

1. Depends heavily upon the DM. Nonetheless a little paper-and-pencil
hacking or a few lenient DMs will create munchkins.
2. Source code and spoiler concepts are largely not applicable; same
with the concept of endgame.
3. Finitely many items/monsters are generatable, usually; if infinite
wilderness encounters are possible, the DM will usually get fed up
and use heavy-handed game mechanics to stop players if they start
scumming them.
4. Non-roguelike console game -- you need Super Nintendo or an
emulator to play this one. Included for comparison. Not a roguelike
-- the game is close to continous in space and time.
5. A good game without character stats, levels, or skills --
acquisition of equipment and health boosts and completion of quests
gives it all the temporal structure it needs. No randomness though.
6. Monsters don't give XP (no character levels), and the only items
generatable in endless quantities (which happens to include money
and anything you can buy with it) are consumables you can only
carry finitely many of (healing potions, bombs, &c in Zelda,
ammo/weapons/quads in the first person shooters.)
7. There's really only one race and class: elf warrior-mage I'd call
it. A warrior with support from magical devices, including
artifacts.
8. Final Fantasy Mystic Quest, another console game, also not
roguelike (due to movement/combat game mechanics).
9. The game generates finitely many monsters and items, except
consumables.
10. Again only one race and class -- human warrior-mage this time,
with spellbooks as well as devices. A boring minor task: much of
the late game involves wading through zillions of monsters you
*must* fight but with the fights generally boring and all alike.
11. I have not played Nethack, but I do have a moderate amount of
information about it from reading and conversation. A similar
statement is true for each game whose name is preceded with a star
(*).
12. The "background corruption", quantum leap in same at game day 90,
and rarity of corruption-reversal methods, and to a lesser extent
character aging and rarity of aging-reversal methods, combine to
limit scumming. Nonetheless the most recent versions have several
massively abusable features that permit certain degrees of
munchkinism (e.g. infinite money, rapid "crowning", infinite food,
absurdly high stats).
13. Paranoid anti-cheating security measures make Windoze crashes a
more common cause of death for legit characters than Ancient
Dragons. The only defense is to *shudder* *whispering* back up
your savefiles *retch!*.
14. Avoiding starvation takes up major amounts of time and effort in
the early game. Also, the game treats shopkeepers and quest
uniques rather oddly. Strange hiding of quest locations, behavior
of quest uniques, exclusions of quests, and behavior of certain
game locations (pyramid and small-mouther cave especially) are
examples of seriously weird and often heavy-handed game mechanics.
15. "Skills" in this game are secondary stats by another name. They
don't get trained or improve with use really.
16. For versions earlier than 2.9.1 this is 'R' due to the "Morgoth
double-manastorm" bug fixed in version 2.9.1.
17. Stat potion scumming was made necessary; breeder scumming was made
unprofitable (breeders are not worth much xp).
18. Welcome to the game that actually provides built-in tools to scum
up high starting stats -- not one but *two* such tools to choose
from! Everyone melees like mad too, and artifacts are so common a
winner has usually seen fifty and sold twenty-five! Game mechanics
are massively asymmetrical due to years of monster hitpoint
inflation. And what kind of store system is that?! Geez.
19. The asymmetry gets really bad here, with monster hitpoint
inflation leading to monsters breathing for more damage when
attacking other monsters than when attacking the player. When
someone posted how they died to a chaos breath with over 700hps
because it happened to be targeted at a monster and not at them, I
knew then that this game is deeply flawed. (On top of that,
if two Zangband monsters fight and one summons cyberdemons at the
other, the demons appear around *the player*, but this is likely a
bug rather than poor design.)
20. The usual need for stat potion scumming in *bands; the infamous
"breeder mutation" antiscumming mechanic; and the notorious
alchemist munchkinism, all in one game!
21. The usual need for stat potion scumming; the usual deflated
breeder xp; and the infamous fenneling munchkinism.
22. The 'Z' here being one of the inevitable weaknesses of a pure
skill-based RPG.
23. In-game documentation of items, especially ego-items, and slowly
improving character knowledge of magic devices is very nice but
not a "full" DDD IMO. Two-and-a-half D's perhaps. :-)
24. Haven't played far enough to be sure there are no unfair
later-game instadeaths, but doubt there are any in 0.5.1b.
25. Here is where [O] really excels.
26. And here -- not everyone is a massive melee destruction machine
anymore! The inflation of monster hps is gone too.
27. For variety & comparison, a few first person shooters whose single
player mode has significant role-play elements are included.
28. Half-life monsters are smart and behave somewhat randomly. The
linearity is a weakness of nearly all FPS games in single-player
mode. It is actually at its least-worst in Half-Life and
registered Quake, as the former limits revisiting only a smidgen
(but is still linear at large scales) and the latter permits the
four major worlds to be completed in any order before tackling the
boss lair. The Cs for Half-Life is debatable; I put it here as the
player obtains a new capability in the late game -- the Long Jump
Module.
29. Half-life's story line establishes some needed information in-game
in an in-character way.
30. Not only is it possible to save just before an unavoidable death
(e.g. while falling into a bottomless pit), but the game requires
so much saving and restoring in some parts (mostly involving
bottomless pits or very difficult monsters) as to make this really
likely to happen eventually.
31. See above about trial-and-die jumping "challenges". Especially bad
in the late game (Xen).
32. You can save just before an unavoidable death here too, but it's
rare for this to happen.
33. The "mission status computer" is a nice in-character source of
information. There are a few other, much more minor role-play
sources of information.

As you can see from the above, nobody has yet created the Right Thing
in RPGs; it pretty much has to be a computer game (the potential
abuses of paper RPGs are basically unavoidable without introducing an
omniscient referee -- but that would have to be a computer). Most
non-roguelike CRPGs are too structured, whereas most roguelikes are
too unstructured. Then there's the dependence on being either a
walking tank (ADOM), having amulets of life-saving/potions of blood of
life (ADOM, Nethack, PernAngband), or massive detection
paranoia+teleportation capability (all *bands).

Let us now proceed to design the Right Thing in roguelikes. The above
table serves as a guide, allowing a simple statement of the goal; we
want the following:

Game |Life |Structure |Docs |Fair|Scumming|Misc
Perfection? S?A?N? TQLWClCsCtRRE S?DDD S Z?P*?

(Here, a ? following a symbol indicates that it is open to question
whether we include it or not -- we can probably make the Right Thing
either way. More than one solution, IOW. We could also make a CRPG
that is not a roguelike and get something Right I am sure.)

The following discussion is broken into sections related to the
columns of the tables above.

1. Lifesaving, cursed items, and spoilers.
First let's examine the trouble spots in existing CRPGs that have
permanent death.
Nethack is short, so it was reasonable for the creators to make
winning a matter of trial and error once one is skilled enough.
Skilled players don't avoid death all that much, they just restart a
new character. Unfortunately, short games have less structure and
replay value, and replay value generally can be created only by adding
zaniness, which might be fun but is not that good role-playing-wise.
Nethack, you'll notice, has no shortage of zaniness, from sink-kicking
and deadly sex to the Keystone Kops.
ADOM is longer but short enough that avoiding death in super-paranoid
fashion or with the aid of lifesaving devices is still not a major
concern. Trial-and-error is still significant to surviving and
winning, even for a veteran. IMO this is bad, since it makes the game
potentially very frustrating. Spoiler reading is frowned upon but
necessary too to maximize your odds in the trial-and-error.
Angband goes the other route. The game (and its variants) is (are) so
long that avoiding death is crucial. To win you really must make
yourself damn-near invulnerable, and the main means of doing so is to
always know what's coming (detection mania), always know whether you
can handle it (spoiler necessity), and always be able to escape if you
can't or things turn badly (teleportation).

All of these problems stem from one fact. If you die without
life-saving, the game is over; if amulets of life-saving or potions of
blood of life or potions of invulnerability are made too common, the
game is trivial.

There are exactly three potential solutions to this dilemma. Note that
no extant roguelike seems to use either, and the first person shooters
don't either, but some non-roguelike CRPGs do...
1. Death is non-permanent; that is, there is no way to "lose the
game"; nonetheless it invariably causes a setback of some kind.
There are two implementations in turn:
a. Death resets you to an earlier point in the game, a
"checkpoint", and these are at fixed locations. This carries two
more options:
i. Finitely many finite-use checkpoints (this also limits
scumming, as progress in scumming can't be saved more than
finitely many times, but it may have its own problems).
The longer the game, the more checkpoints there are; a
checkpoint should become newly accessible just before a
dangerous maneuver must be attempted. Problems: distribution
of checkpoints must be carefully tuned to make the game
playable but not frustrating nor too easy.
ii. Infinitely many checkpoints/reusable checkpoints, but not
too easily accessible -- e.g. you have to go to an inn in a
town to save the game. Note that the Zelda games go this
route -- going to sanctuary or entering a dungeon cause
checkpoint uses. IMO a good choice (randomness and
nonlinearity can still provide replay value even without a
way to "lose the game"; the inevitable setbacks give the
player a reason to fear death and prepare before tackling
difficult areas of the game, but also let them experiment a
bit and learn some stuff by trial and error).
b. Death sets you back a fixed amount, e.g. to however things were
five thousand moves or ten real-world minutes ago. The former
presents no gameplay difficulties, but both present technical
hurdles of a severe nature (how to store all the game state
going back that far?) and the latter is abusable in a turn-based
game (e.g. any roguelike): wait at prompt for ten minutes before
attacking that Dracolisk. If things go badly and You die. -more-
you resume just before the fight.
2. Death is permanent, but the game doesn't end just because the
player character dies. This requires a party of characters that can
continue while diminished -- the real problem with most roguelikes
isn't permanent death, but the combo of permanent death and "you
versus the world". Permanent death with parties raises questions:
* Are there multiple PCs? If there are, it must either be a
multiplayer real-time CRPG or a single-player turn-based CRPG!
Multiplayer requires real-time to stop one person taking a snack
break/toilet break/his last breath (for real) bringing the game
to a screeching halt (or worse, an unforeseeable and unavoidable
network error doing the same -- at least regularly
abusive/unplayable-with players can be banned). Real-time however
allows for all manner of unfair deaths unless you go with
non-permanent death, so the player can save the game just before
going AFK and recover from a poorly-timed sneeze. Thus we need
a single-player CRPG, which must be turn-based as controlling
multiple PCs in real-time is not IMO possible with any real
competence. Note that Mystic Quest has parties of 2 characters
at times, with optional manual or computer control of the second
(so they could be changed from NPC to PC and back!), and is
turn-based. (It also lacks permanent death.)
* Is it multi-player? The above argument shows that a multi-player
game will have problems if it has permanent death, or any kind of
permanent setbacks.
* What happens when someone dies?
a. We can allow the diminished party to continue and try for a
short-handed win. This is similar to the "multiple lives"
approach to making other lengthy/complex video games winnable,
but in-character for a CRPG unlike "multiple lives".
In this case you can still "lose the game". Death of a
character is much to be feared because a short-handed party
has a harder time winning. But prone to unfairness and
inflation of death-avoidance mechanisms.
b. If an NPC dies, the NPC is replaced (eventually) by one of
comparable power; PCs are irreplaceable. Loss of all the PCs
loses the game. More fair than the above but still prone to
same problems, just to a lesser extent.
c. NPCs are replaceable, and new PCs can be rolled up at certain
locations and journey to find the party or otherwise resume
the game, without the game restarting. This is fraught with
problems: the new PC will be considerably weaker than the rest
of the party. One elegant solution is to provide mechanisms to
build up replacement PCs before they resume where their
predecessors left off; this may require a way for the game to
generate infinitely many quests that aren't silly "kill xxx
monsters" type quests. But it can be done! This (2c) is a very
good choice, like 1aii.
* Is death occasionally reversible?
Unfairness potential and detection/teleportation inflation
potential in the above cases can be further reduced. For example,
if a party contains a couple of healer NPCs that have the power
to resurrect dead characters, a death is usually a minor setback
rather than a massive loss, but if a party loses/is separated
from one healer, it is vulnerable to losing both healers
permanently if the other dies or gets lost somehow. Losing both
healers renders the party vulnerable to being whittled away to
nothing, losing the game, before getting the opportunity to
obtain another healer. Healer PCs of course would only get
resurrection power late (maybe at the max clevel, often 50 in
RPGs, and in a rare spellbook -- perhaps an artifact spellbook a
quest must be solved to obtain).
* Is it possible to lose the game?
With a or b above loss of all the PCs loses the game. With c
above, loss of all the PCs in the party may lose the game, or we
can allow the game to continue with the setback that although the
completed parts of the game remain completed (e.g. quests
fulfilled, uniques dead), and somewhere the lost party may have
left its stuff, the new PC has to build up from level 1 again.
(At least some of the game world is explored now, and some
difficult parts perhaps completed.)
3. Death is non-permanent but there is still a way to lose the game.
The most obvious way to do this is to impose an (in-game) time
limit, but this is fraught with danger -- e.g. the game might
become unwinnable and then be saved in the unwinnable state.
This, on the whole, is not a very good choice.

1aii and 2c seem to have tied for the best solution to this issue. For
part of that roguelike flavor, we shall go with option 2c: there is a
party, including one or more PCs and zero or more NPCs, and the game
ends if you quit (including after a win) or the whole party is
destroyed (which is a loss if you didn't in fact win first). Moreover,
we shall (for simplicity's sake) limit to one PC in the party. If an
NPC dies the player can lead the party to a town, where another NPC
can be recruited (and there might be other circumstances where an NPC
replacement *might* be obtainable). If the PC dies, the game goes on
-- the player rolls up a new PC, who starts in some town in the same
game world with the game state continuing to evolve, and he may
recruit some NPCs and may manage to find (and perhaps join forces
with) the surviving NPCs from the previous attempt. In this way, the
game sort of goes on after a sort-of-loss, but perseverance should win
the game eventually.

Where do cursed items and spoilers come in?
1aii allows difficulty always detecting really troublesome cursed
items not to be a showstopper, as if worse comes to worst you can
restore a save game. However, the setback of being returned to a
checkpoint you hit some time ago creates a deterrent to responses like
"Oh, it's cursed, quick-load..." and encourages finding in-game
solutions to problems posed by cursed items. If it turns out to be a
real pain or "game-ender" you can still reload and accept the setback.
(Of course to prevent saving *with* the trouble item, either no cursed
item should be a showstopper or otherwise really evil, or any such
should prevent saving the game until it is removed!)
2c allows you to get killed with a cursed item (including because of
it) and go on with your game. The setbacks associated with death
discourage a response of "Oh, it's cursed, suicide..." and encourages
finding in-game solutions to problems posed by cursed items. If it
turns out to be a real pain or "game-ender" you can still suicide and
accept the setback. Meanwhile, with a character's death not being a
showstopper, we avoid making it necessary to read spoilers to win,
because you can afford to learn things the hard way, even while
preferring to avoid that. That, in turn, means items and (especially)
monsters can be learned about in a gradual, in-character fashion, from
lore (in writings or from NPCs) and experience (Ow! It breathes nether
for beaucoup damage!).

2. Items, items, items.

How do we make instant identify unnecessary, so people will actually
risk wielding that unidentified long sword? Simple -- cursed items
aren't a showstopper. How do we make cursed items a non-useless part
of the game? Simple -- cursed items are neither perfectly detectable
nor harmless.

Cursed items should cause a setback, without being a total
showstopper. The above solutions to death issues (e.g. making death
nonpermanent, or permanent but not a showstopper itself) solve this
for us.

3. Documentation and Character Knowledge. (We'll get to structure
eventually.)

Ideally, our game documents some basic, required knowledge of game
mechanics, some knowledge of the game software's interface, and a
getting started guide as "standard" documentation, but everything else
is learned in-game by in-character means, from what potions exist, to
what this potion does, to what this monster breathes. Preferably, some
understanding of races, classes, stats, levels, xp, interface, and
such is given out-of-band in a help file, and everything else *comes
through the character's senses* -- either because they see it or hear
it in the world's lore and legends or from experienced NPCs they chat
up, or because they witness or experience it directly. Even to the
point that discovering that that lizard is a different kind from this
one depends sometimes on the character observing them act differently
or hearing about it from an expert NPC on the local fauna -- there
should be lookalike monsters, perhaps significantly different in
danger level, as much as there are items. Moreover, the character
shouldn't be born knowing every creature name -- Angband characters
instinctively know the name of a Dracolisk, and many never live to see
their first (and a lot more never live to see their second ;-)) ...
this is unrealistic IMO. It should be "a big scaly lizard with smoking
nostrils" until the player learns the name from an NPC or bit of lore
or something. Similarly, why the hell do nearly all roguelike
characters know a magic wand from an inert stick? Shouldn't they have
to use some method for sensing enchantment or take it to an expert
appraiser of magical items to get it diagnosed and maybe identified?
Then there's the question of identify. Magical identification should
be rare and special. Finding things out by experimentation, from lore,
and from sensible game world mechanisms is preferable to hand-waving
like that. Our game won't have any scrolls of identify, nevermind
ADOM's blessed scrolls of identify. But it will have a bunch of
learnable, improvable appraising skills, and ways to generically
"detect enchantment" and such; and once something is known to be
magical it can be tried (potions and scrolls can be tried regardless).

4. Fairness.

Much less of an issue with nonshowstopping death. Nonetheless, every
situation the game throws at you should be beatable with a little
thought and the right equipment, *without* peeking at the spoilers.
This doesn't mean every battle can be won with good enough equipment
-- just that those that can't must be avoidable entirely. Also, the
player should be able to scr00w themselves only by being immensely
stupid, never by sheer bad luck or easy-to-make mistakes. Selling that
artifact needed to win the game is idiocy -- *if* the player has good
reason to believe *without reading a spoiler file* that the artifact
*is* needed to win the game. Making the game solvable by multiple
routes makes things interesting and replayable as well as reducing the
risk of the player getting stuck through no fault of his own.

5. Scumming/cheating.

The solution to scumming is, IMO, making it not worth bothering with,
but not by way of heavy handed game mechanics. PernAngband's breeder
mutation is a good example of a bad scumming solution. In this case,
it's not really heavy-handed, but it causes massive unfair collateral
damage to non-scumming players -- if a breeder takes over a level that
they weren't farming, just couldn't control, they can easily be
fux0red. Making it necessary (a'la Angband's stat gain) is bad IMO.

Our game will make scumming unprofitable as follows:
* Farming: If there are breeders, farming them will be unprofitable
because every time a breeder duplicates, its XP and inventory will
be divied up, the former evenly, between the daughters. Let 1 worm
become 1000, then kill the 1000, and you will get exactly what you
would have gotten by killing the 1 worm right away, but at more
effort and risk.
* Scumming monster generation: Each level will require a factor more
XP to reach than the previous, to a first approximation. And monster
generation in cleared areas will be slow. Thus one cannot accumulate
levels quickly this way except if the monsters are quite dangerous
in that area.
* Item/vault scumming, stairscumming: These only become an issue with
randomly recreated dungeons. Abuses of this sort are common in
*bands (which are balanced to take it into account, in turn making
it *necessary* which is *really* bad). ADOM has it to a lesser
extent; every ADOM character I've ever done well with has scummed
its "Infinite Dungeon" for spellbooks, equipment, money, and food
in the early game. (The presence of background corruption in the ID
and the 90 day quantum leap in background corruption do limit this,
but with moderate to heavy handed game mechanics, and collateral
damage to nonabusive players. Moreover the game is balanced to make
some scumming here well-nigh necessary too!)
Our game will have persistent dungeons exclusively.
* Stat scumming: Stat gains of a permanent, intrinsic nature will be
extremely rare. Our game will include mechanisms to limit random
generation of items to finitely many occurrences, in addition to the
usual only-one-of-each-artifact rule, so stat potions can be made
not only rare but even "limited-edition". The game (for structure
purposes, see below) will also allow campaign designers to
explicitly place items, so one can still put a few guaranteed stat
potions in the game. Same goes for stat training -- if you can train
strength by paying a certain NPC, it only works finitely many times,
only raising strength to around a certain limit; if you can train
strength by kicking doors down, you only get a few increases, it
takes more and more doors for each successive increase from this
source, and it no longer works past a certain point. You can only
get so strong from kicking doors.
* Skill scumming: Skill improvement can only be taken so far for each
situation that can raise it. E.g. you only get so good at
pickpocketing by picking the pockets of farmers -- you might need to
pick the pocket of an orc chieftain to train it further with
practise.
Tying skill increases to clevels will be done in our game -- also to
the "level" or "strength" of any opponents involved.
* Scumming skills for XP: disarming a level 1 trap will only give so
much XP; you need to disarm more difficult/dangerous traps to get
much XP, relatively speaking, at later levels, and to improve the
trap disarming skill as well. And so forth.
* Skills and stats alone will not an ubercharacter make. They'll just
help, significantly but not to the point of making scumming very
rewarding. The "natural" increases should do fine for a fun and
decently-paced but not frustrating game.
* If raising skills and stats is hard, how does the player deal with
situations where they can really use a higher value *now*? We'll
throw in potions to temporarily boost stats, and as skills will be
affected by stats (e.g. dex and int for trap disarming) this will
boost skills in time of need. Boosts will be cumulative in duration
only. Potions of boost foo will be relatively common and shallow;
potions of supercharge foo, which will last longer and have larger
effects, will be deep and rare.

Persistent dungeons introduces a potential problem: item and XP
starvation. The solution: Infinite dungeons, which are, however,
persistent. Disk space is not an issue: the player can never explore
more than a finite amount of it. Won't it be scummed? Getting new
stuff from infinite dungeons will mean a form of mining: the more
you've taken out, the deeper inside you must go to find the next nice
item. Of course, they'll tend to get nastier with depth, accompanied
by better items. But without "word of recall" or similar, it's a long
trek back to the surface with that dragon scale mail. The continuing,
but fairly slow, monster generation does the rest. This will occur
even where the player isn't -- if the player is absent from a level
for a short time, it continues evolving in detail by the usual
mechanism (beware -- that dragon might follow you up several flights
of stairs!); if the player is absent longer, it stops so evolving.
When the player approaches a level that stopped evolving, it is
modified and then resumes evolving. The modification works as follows:
* If the player has been gone less than xxx game time, some items are
removed (artifacts are preserved if removed) and some monsters, in
proportion to the amount of time the player was gone. Powerfully
good/bad items are more likely to be removed (cursed ones getting
stuck to some hapless monster in-game or getting destroyed because
they are hated, precious ones taken because they are so valuable) as
are ones that have been lying there a long time. OOD monsters are
more likely to be removed (returning to their native depths), as are
fast-moving ones (they get bored and leave sooner). Non-moving ones
will be removed with a lower probability (something has to have
killed them). Removed monsters have some probability of being
"killed" instead of just "disappearing", generating their drops. The
more time went by the more the drop so generated will be subjected
to the afore-mentioned treatment of items. Weaker monsters are more
likely to die this way.
* Past a certain elapsed time, the items and
monsters will simply be totally regenerated. One exception: unopened
vaults are preserved against this effect.
This gives the impression of the level "evolving" naturally in the
player's absence, for a fraction the CPU cost of actually evolving it.
And it gives another way for the player to get more kit when they need
to -- revisiting an area not visited for a lot of game time is a way
to find new stuff and monters. (Unlike infinite dungeons, though, it
won't produce more vaults. This is why existing vaults are preserved
if undisturbed by the player or by an NPC that is permitted to open
vaults.)

A realistic alternative for vaults is to give pre-existing vaults a
certain (low) probability of being opened and looted, but to also
allow for new vaults to occasionally appear -- someone must build the
damn things right or they'd all have been looted long ago! But this is
exceedingly rare. Other changes in the world and dungeons can be
treated similarly, e.g. a mine may after many moons be a bit more
extensively mined, a dungeon may have new rubble piles and new or
missing walls, and so forth. (Certain places would be immune to
change, particularly uniques.)

See the following section, which dovetails with these ideas.

We must also address the issue of player storage of items. Certain
(unique) places will be safe to store items without them randomly
vanishing over time. The player's home will be one of them -- it will
never move or change, always be accessible (not always conveniently),
and never be robbed. (You are lucky enough to have gotten it
wizard-locked for you.)

6. Structure.

The right balance between structure and randomness is tricky to get
sometimes. We will discuss this a bit, then describe a mechanism
likely to give good results.

Replay value really requires lots of randomness, and roguelikes
traditionally have lots of it. Structure, however, makes the game
interesting and gives players that sense of exploring a large, real,
and living world. Towards this end, we note two kinds of structure.

* Spatial structure: How complex is the world? How big? What physical
structures does it have? Our game will have a hierarchy: a landscape
with forests, deserts, lakes, rivers, mountains, and towns, with
buildings and dungeon entrances; dungeons with vaults, special
hidden rooms, corridors, deadly traps, hidden barracks and
storehouses; buildings with various rooms and passages; etc.
* Temporal structure: How long is the game? How does it progress?
What milestones can occur? Our game will have events both in the
world's history and in the player character's life. It will have
levels and the obtaining of power-ups. It will also have a living,
breathing history and economy and ecology, or at least a good
illusion of the same. Populations will vary in various chaotic ways
and the player will see some things eating or rotting the dead,
others preying upon the living, others eating the plants as
elsewhere new ones grow. Seasons will pass and with it the weather
and ambient life forms will vary. Some towns will grow prosperous,
others might be built, and some might die, in semi-random fashion,
but resembling reality -- the world will not be unchanging except
where the player is, or in merely small ways through regenerated
monsters, nor as randomly rearranging as Angband or ADOM's infinite
dungeon. Some facilities, of course, will always be available, and
some (unique) places will never move or change except in prescribed
ways, to avoid trapping the player or losing them their stuff in an
unfair way.
Permanent changes might happen. The player character lives in a
world where species sometimes go extinct, and new ones sometimes
appear; where wars are fought and kings die and heirs take the
throne. They may even witness both random and planned battles,
assassinations, coronations, funerals, weddings, and so on.

This game will use both randomness and planning -- it will have
planned events, guaranteed places and things, and random ones as well.
The planned things will ensure that the game is winnable; the random
ones will ensure that it is massively replayable. Moreover, randomness
and purpose will be *entwined*. Picture this: a forest stretches
endlessly to the world's east past a point. Inside of it, the player
eventually encounters a witches' hut. It is a unique place, but it is
a random one -- it could have been generated at any time in a forest
anywhere in the game, though once generated this one, like most,
happens to be permanent and unmoving. The witch, however, assigns the
player a quest, and gives them a silver key they can use to open a
previously impassable door in a familiar dungeon... Here we have some
entwining: the forest is always there, though its interior is random.
Other forests are random in every regard. The hut itself is random in
where it will appear, but planned in its layout and in that a certain
NPC is found within. The witch's black cat might be generated anywhere
nearby and wander anywhere nearby too, randomly, but will always be
found nearby or in the hut at any time. The keys will never be
randomly generated; one can only ever get one from the witch. The door
might also be randomly placed, but guaranteed; the only way to open it
is with the key. What's inside is presumably also partly random, but
with guaranteed elements.

Moreover, the game may be rendered capable of generating *random
uniques* -- random unique items (indestructible such being random
artifacts), random unique NPCs/monsters, and random unique places.
These may even be structured into random quests that are, nonetheless,
interesting role-play -- no "This level is guarded by 22 Greater Hell
Beasts" garbage here! There can even be an infinite number of these,
though there can only be so many at once, and random quests and other
major random elements might be generated in finite numbers per clev
(with this reset if the PC dies!) -- the world's long-term mutability
allows for these to quietly appear and disappear and new ones appear
(although places, NPCs, and other things important for random quests
will be "temporarily guaranteed" if the player has taken on the quest
and not completed it, unless there is an explicit time limit or other
failure condition of the quest and it is met. Then the uniques are up
for grabs by the game's reclamation services, to be replaced
eventually perhaps by new ones.

How does this work? A hierarchy of features. Features will be one of
two major classes of game object; the other will encompass items and
monsters. Features and item/monsters have specialized kinds
(subclasses) and some kinds are abstract; e.g. humanoid (abstract) ->
Orc (concrete) -> Orc Captain (concrete). Abstract ones can't be
generated unspecialized. Concrete ones can be. Moreover, any of these
is either unique or nonunique and either randomly placeable or not. If
orc captains are randomly placeable, then a "random orc" might be an
orc captain; otherwise it won't be. If Gorbag the Orc Captain is
unique, then he can't be generated somewhere when already generated
elsewhere, and can't be generated at all once killed. The generation
algorithm goes like this: a feature of class "world" is generated, and
allowed to have random properties. The "world" class's generation code
places a few guaranteed features and randomizes the surrounding
features. One of these perhaps is a town the player will start in --
guaranteed to exist, random in location. Near the town, a rock outcrop
is generated -- random place but always near the town. The rock
outcrop generates a cave entrance, which generates the cave, which
generates corridors and cavernous spaces twisting through rock, with
randomly placed items and monsters of a low level. Now the player can
always find some interesting stuff and xp in the early game. Features
within features. Somewhere else an orc citadel is generated. It has
certain construction, random and guaranteed places -- maybe a temple
or altar is always there and always in the center, and everywhere else
no altars are generated but any orcish building might be, but a
barracks, an ogre chieftain's fancy home, and a few other guaranteed
places are generated. The fancy home always generates an ogre
chieftain (maybe a specific unique one) and the town is always
populated with orcs and a few random animals they will tolerate in
their citadels.

Note that we don't want a random altar turning up in the citadel, or a
kobold or human. The orcs should be carrying orcish weapons, only
rarely (or never) other brands (more realistic if the odd orc has a
non-orcish item he found somewhere and liked). How is this done? Each
class also has a bunch of flags. These flags are implemented as a set
(unordered growable collection data type) of strings, probably with a
hash table as the underlying data structure. Flags affect placement in
"themed" settings. E.g. any item with "orcish" as one of the strings
in the set is a good choice in the orc citadel, and any with "never
orcish" will never be generated there (the rest are merely
improbable). Any item with "shiny" small enough might be especially
attractive to a "pack rat", which might tend to gather these on a
level and hoard them in a small spot it randomly designates, usually
in an obscure corner somewhere, and which it will go to and guard when
it smells an intruder approaching. Any item with "junk" won't be
generated in shops. The use of a set makes this scheme really
expandable -- you can add a new item and make packrats like it; you
can add a packrat and give all the appropriate items a "shiny" flag.
As for depths and rarities -- every place is generated at a certain
level. This level affects what is generated in it initially and with
the passage of time. Things become very rare out of depth, and
monsters cease appearing at all too far out of depth. This includes
place types (think of [O]'s interesting rooms, but nested and
complexified and made very general and flexible). Subclasses have a
frequency; non-abstract classes have an unspecialized frequency. The
odds of a random orc being an orc captain are proportional to the orc
captain's frequency; the odds of it being a plain orc are proportional
to the orc unspecialized frequency. This means adding new stuff won't
seriously unbalance things. Suppose we have:

Weapon
/ \
Bladed Polearm

with no other subclasses, and equal frequencies on Bladed and Polearm.
When told to "generate a random weapon" the game engine will make a
bladed one half the time and a polearm half the time. Add a new sword
type and bladed weapons don't become more common than polearms; they
remain equally common. (However, existing bladed weapon types may
become slightly rarer.) This scheme also allows any object generated
to have its rarity calculated on the fly -- when the game generates a
random "foo" it also computes the probability that a randomly
generated "foo" would be whatever it generated. That means you can
make a weapon shop that deals exclusively in rare weapons: the "weapon
rarity" of your weapon can be used to determine the odds of the
shopkeeper wanting it; store items can be generated and ones that
aren't unusual enough rejected and replaced. Stores and vaults of rare
items should be fun! A fine-grained quality scheme (say using the
value in one of the game's currencies) can be used to stock vaults
with good items, or make that nasty undead drop exclusively cursed
ones, with fine-grained control. Of course, the flags and the classes
themselves (plus object size and weight and other obvious observables)
allow themed placements and behaviors: shops full of weapons, random
weapons, packrats only liking shiny small things.
Ego items can be generated too -- even ego places and monsters. Add to
the above scheme the ability to tag an "egoizer" onto a class; this
specifies a procedure for specializing items of that class. Attach an
"of burning" egoizer to the weapon class and get maces of burning,
flails of burning, swords of burning ... of course, weapons have an
"un-egoized" frequency and egoizers have frequencies. Suppose we put
an acidproof armor egoizer in, but don't want rusty chain mails to be
acidproof. An egoizer can specify a flag that must be absent, and
rusty chain mails can be given an "acid-susceptible" flag. Moreover,
you can use this to combine specializers. Want rusty plate mail, rusty
ring mail, and so on? Add a "rusty" egoizer with "acid-susceptible"
flag, and put a "rustproof" flag on the "acidproof" egoizer, making
them mutually exclusive. Similarly, one could prevent weapons from
having both the fire and frost brands simultaneously in this way.
Of course, one could generate themed items with egoizers too -- armors
generated underwater might have to be either rusty or rustproof;
weapons generated in Hell might always be flame branded (but not
especially useful unless taken out of there, as the creatures there
would be flame-themed, and therefore presumably fire resistant!); and
so forth.

7. Miscellaneous items.
T -- slow and tedious to start a new character. (Undesirable,
especially in combination with 'E' or 'U' in fairness column.)
R -- you have to be a rocket scientist to start a new character.
(Undesirable -- basicaly you'll be messing with zillions of
options and poring over documentation. Or dying a lot. Or both.)
S -- Starting a new character, it is well-nigh necessary to scum for
high starting stats or something similar. (Undesirable.)
SS -- The game actually has built-in features to assist in automated
scumming for high starting stats or whatever. (Undesirable.)

Starting a new character will be easy and painless in our game. Pick
race, pick class, get char with random stats and decent capability to
play the game competently. Away you go!

Z -- Endgame characters of the same race and class don't have much to
distinguish them. (Neutral or undesirable.)

No problemo here. Not only might the endgame depend on the class and
race, but it might depend on player choices and random factors.
*Multiple endgames* might be possible! Random uniques will add another
random factor -- a random artifact might make one game very different
from another even with other things being equal.

P -- Polymorphing or other random and unpredictable elements make the
game chaotic and reduce its structure.
(Can be combined with Z, when endgame characters are all alike in
that they all polymorph a lot or whatever and play similarly
regardless.) (Undesirable.)
P* -- P, but limited to some race/class combinations (e.g. Zangband
chaos-warrior). (Neutral.)

Player polymorphing will probably not be a part of this game. If it
is, any involuntary polymorphing will be temporary, auto-reversing
after some time.

F -- indicates that every class plays like a fighter, possibly with
spell support. (Undesirable: bad roleplay, *unless* the game only
has classes that should properly be warriors.)

Pure spellcasters will be in this game. There will also be real rogues
-- they steal and set traps and pick pockets and don't kill all that
much. The more difficult the heist, the more XP they get.

G -- Game has a glut of artifacts. (Undesirable: artifacts should be
rare and special. It's bad role play otherwise.)

Artifacts will be rare and special. Even the infinite parade of random
ones a game can generate. There'll be an equilibrium with these being
reclaimed sometimes and being rare. Unlike fixed artifacts, random
ones that are reclaimed are gone forever, but a new random one can
replace it. Random artifact generation gets rarer the more exist in
the game unreclaimed, and slowly more common with time (well, someone
has to keep making the damn things right?). There *is* a limit to the
latter increase, however. (Imagine there is a slow-growing pool of
random artifacts, of which those extant in the actual recorded game
universe are only a portion. The game takes place in a finite part of
an infinite world after all.)

M -- Some minor task requires inordinate amounts of the player's
attention, e.g. avoiding starvation or repairing stat drains a
lot. (Undesirable, even if realistic, because *boring*.)

You can starve, die of thirst, fall asleep from fatigue, or run out of
consumables of other sorts. But anything necessary is easy to come by,
including safe places to sleep, and fatigue strikes infrequently --
more so with more constitution. All of these conditions give plenty of
warning too. If you take a hike of several game days' journey to a
town, you'll need to sleep somewhere on the way. But abandoned
buildings, caves, and such aren't that rare or dangerous -- at least
once cleaned of any dangerous denizens you find there at first.
Also, when you first feel fatigue, hunger, thirst, or whatever, it
will be a while before these get stronger and actually begin to affect
your abilities in a negative way.

Stat drains and such will usually slowly repair themselves. Quick
fixes will be needed only in dire circumstances, and potions of boost
stat will temporarily mask the effects of a drain during a crucial
battle.

It will take tens of minutes of real play to get hungry from full, and
half an hour to need sleep after resting.

A -- Asymmetrical game mechanics or just plain asymmetrical powers
make monsters very different from the player in e.g. hit points.
(Necessary to some extent if the player is to survive, but
undesirable past a certain point.)

The game mechanics will be entirely symmetrical. NPCs and PCs won't
follow different physics. The game remains playable because some of
the NPCs are on *your* side, and you (the actual player) is easily
more intelligent than that box on your desk. Get to a higher level
beating weaker monsters. Get an advantage in equipment. Find a
tactical advantage. Or just plain outsmart them. But don't expect pure
brute force to work too often or without penalty.

W -- Weird game mechanics. (Undesirable -- catch-all for weird,
unrealistic or bad roleplay game mechanics not covered above.)

Shops will be real. Shopkeepers will not be omniscient. That weapons
store owner in that early town knows a lot about local weapons and can
appraose them well, but he knows considerably less about the weapons
used in the land over yonder, or about that rare and well-crafted item
you found in the dungeon. With rare and exotic items, he can
nonetheless give a slightly useful guess as to its power or
wretchedness, and often a much better idea of who to see or where to
go to seek more information about it... Moreover, they won't see you
pick up an item if they don't have LOS when you take it. (That's why a
lot of the shops will have an open and roughly round shape, so the
shopkeeper has LOS to every item...) Hmm, maybe you can block the view
with an innocuously-acting NPC? Wait -- that farmer over there
browsing is now talking to the shopkeeper ... the shopkeeper is giving
him money?! The shopkeeper is shouting about thieves! Let's get the
hell out of here! Oh what's this -- the town is crawling with police!
We're doomed... NPCs will have societies, and communicate, so beware!
You can kill anyone (in theory) and do anything (in theory) but maybe
not with impunity. Stealth will be a rogue's best friend, lowering the
odds of an in-LOS theft being detected by whoever has LOS to it.

Recall won't exist. You'll have to walk, swim, fall, fly, hop, skip,
or jump somewhere, unless you can catch a ride...

Your backpack is real. It can hold a lot of things, especially smaller
things, but watch out! Too much weight can make the bottom fall out of
it. I'd be careful about fire too. At least it can't be stolen easily,
although its contents might be easier to pilfer.

Fortunately, you can get more backpacks, you can roll up a spare and
put it in your original, and you might be able to find high quality
ones...ones that are not flammable, or maybe even have magical
abilities...

Monsters will have drops and hoards that make sense. A killed dragon
turn magically into a hoard of treasure, but maybe there's some down
that passageway it was blocking. (Yes, item, monster, and dungeon
feature generation will work hand in hand.) A orc won't "hit you for
3d3 damage"; it will "slash you with its small sword for 3d3 damage".
Moreover, the small sword will be dropped upon its death. Did it do
less damage than you expected? Better be careful, that sword just
might be a cursed (3d3-1) sword. I'd appraise it before risking
wielding it. OTOH, if it did you 10 points of damage without a
critical hit, that sucker's just *gotta* have a plus to damage. Hope
you survived. So, what's this? From far off it looks like "a sword"
next to "a suit of armor that looks like it had a body inside"...up
close it's "a short sword" next to "a dead orc wearing armor". Search
the "dead orc wearing armor" and you discover "a suit of chain mail",
"a hunting knife (1d3) in a pocket", and -- woah -- "a tool belt" and
"a silver-tipped straight stick in a tool belt slot". Better take the
knife and stick -- the latter is quite likely a magic wand of some
kind. At least he didn't zap you with it!

Yes, they'll be able to use items, and pick them up. Fortunately for
you, low-level monsters will be as unlikely as low level players to
either a) find or b) be able to use high-level items. You won't start
the game and immediately get "You hear a strange 'ZAP'! The death eay
bounces. You die..." -- but a monster with an OOD item might be as
dangerous as an OOD monster...

Monsters will do some predictable things. A patrol at an orc supply
depot will be an orc. It will also be patrolling. It will patrol in a
predictable fashion, at least when not pursuing or fighting an
intruder; run far enough and he will return to the barracks and resume
his patrol rather than remain away from his post for too long. If it
is unbeatable in combat, the supply depot is not a lost cause. Maybe
you can slip inside when he reaches one end of his patrol path and is
too far from the door to see it clearly. Maybe he's out of LOS for a
moment along his path. Maybe you can distract him -- order one of the
NPCs to draw him off to the north, then the rest of you sneak inside
while he's chasing the NPC, but before he returns. You might also be
able to throw a rock, making him go where it lands -- maybe if you
throw it to the right place he'll be out of LOS of the entrance for
long enough. You might also wake up that sleeping fire beetle and run
down the corridor as it slowly trundles along behind you until it
smells the food in the depot and switches its focus to going toward
the food it smells. While the orc patrolman is fighting the beetle,
you can sneak in. Perhaps the beetle is easy for you to safely
approach or kill (because of fire resistance) but the orc is easy bait
for it and will die, leaving the depot unguarded. Probably several of
those will work. Of course, if you do kill the orc, you'll find he had
a weapon and armor, probably of predictable kinds, and maybe one or
two useful tools and some random valuables.

Monsters will also do some unpredictable things. If a long sword is
generated near the depot, the patrol orc is likely to be found
wielding that instead of his default short sword. You might even catch
him on the way back to patrolling from where he found it. The
patrolman might be generated with a wand of striking, out of depth, as
one of his random number of random tools, and then you had better be
careful if he is able to use it, but if he isn't, killing him is
likely to be rewarding. OTOH, if he doesn't know how to use it, he
might be willing to *sell* it to you in exchange for money or trade it
for an item he does know how to use... if he isn't hostile that is.
Perhaps he only gets hostile if a non-orc actually goes within a few
squares of the door, or if someone attacks him. So before doing
anything rash, look at him from close range (is he wearing an unusual
weapon? does he look like a tough orc or a weaker one? does he have
any unusual wands or other objects displayed on his person in tool
belts, say? Remember they might also conceal a weapon...) and try
talking...

8. Conclusion.

Above is a blueprint for making a roguelike game head and shoulders
above the rest. Not only that, in an object oriented language it
should be possible to design an *engine* into which the planned
species of monster and item and place and the limits and parameters
for constructing and deploying random ones can be plugged. The one
engine could easily support thousands of different variants, and
multiple "campaigns" for each variant (same "world" in some sense,
different quests/goal/new stuff/removed stuff...)
--
Bill Gates: "No computer will ever need more than 640K of RAM." -- 1980
"There's nobody getting rich writing software that I know of." -- 1980
"This antitrust thing will blow over." -- 1998
Combine neo, an underscore, and one thousand sixty-one to make my hotmail addy.

Matt Thrower's profile photo
Matt Thrower
unread,
Apr 30, 2001, 12:06:45 PM
to
I'm sorry to post such a short reply to what is evidently an eloquent and
carefully considered post, but it strikes me there is another solution to
the 'death' problem which I've often thought would be an interesting take on
Angband, almost like a 'semi-cheat' or possibly acceptable, if the culture
of Angband changes a bit.
This is to make death non-permanent, but to impose some kind of penalty on
the player which is catastrophic enough to serioulsy impact gameplay and
therefore make death very unpleasent but which is, unlitmately,
non-permanent, so that the character can carry on playing if they so wish.
It seems to me that an obvious way to achieve this in Angband would be to
have a dead character be stripped of all his/her equipment by Morgoths
minions and then dumped back into town which raises the following:
1) The character will recall do a depth at which he or she is suddenly going
to find it very hard to stay alive.
2) They will have to backpeddle quite a lot to seek out more equipment,
adding a large frustration level to the game, but not actually making the
character unplayable.
3) They will have lost all their artifacts, possibly permanantley (depending
on design) making the game that much harder to play, given that all the most
powerful items are artefacts, but not totally impossible.



Graaagh the Mighty's profile photo
Graaagh the Mighty
unread,
Apr 30, 2001, 12:15:31 PM
to
On Mon, 30 Apr 2001 17:06:45 +0100, "Matt Thrower"
<REMOVETHISSPAMPROTE...@cramersystems.com> sat on a
tribble, which squeaked:
>I'm sorry to post such a short reply to what is evidently an eloquent and
>carefully considered post, but it strikes me there is another solution to
>the 'death' problem which I've often thought would be an interesting take on
>Angband, almost like a 'semi-cheat' or possibly acceptable, if the culture
>of Angband changes a bit.
>
>This is to make death non-permanent, but to impose some kind of penalty on
>the player which is catastrophic enough to serioulsy impact gameplay and
>therefore make death very unpleasent but which is, unlitmately,
>non-permanent, so that the character can carry on playing if they so wish.

Non permanent death with associated setbacks other than having to
reload at the last "checkpoint"? hmm.

Let me try to guess. Massive perm stat drains? Raised recall depth?
Permanent level drains? Random lost items (including artifacts, but
preserved)? Same but without preserving artifacts? (Ouch!)

>It seems to me that an obvious way to achieve this in Angband would be to
>have a dead character be stripped of all his/her equipment by Morgoths
>minions and then dumped back into town which raises the following:
>1) The character will recall do a depth at which he or she is suddenly going
>to find it very hard to stay alive.
>2) They will have to backpeddle quite a lot to seek out more equipment,
>adding a large frustration level to the game, but not actually making the
>character unplayable.

Well, they'll actually re-dive from 50', without benefit of recall.
Losing the Phial will actually hurt the worst.

>3) They will have lost all their artifacts, possibly permanantley (depending
>on design) making the game that much harder to play, given that all the most
>powerful items are artefacts, but not totally impossible.

Preserve the light sources (at least the Phial), and (if found) One
Ring, Morgoth's crown, and Grond, even if you don't preserve the
others. A game with no Phial would be un-playable. And preserve any
light source or (God forbid) one ring or winner artifact that was
sold/lost *earlier* -- i.e. *all* of these can be found again whether
sold or lost.

Players who find the Arkenstone or (for some reason) *use* the Star
will probably give up permanently a home slot to the Phial, so they
have a decent light source and the handy activation until they find
the Arkenstone again.

Big Bad Joe's profile photo
Big Bad Joe
unread,
Apr 30, 2001, 12:30:09 PM
to
On Mon, 30 Apr 2001 12:41:45 GMT, inv...@erehwon.invalid (Graaagh the
Mighty) drank a fifth of Old Crow and wrote:
<all-time record-holding snippage>

Wow...a lot to think about here. There would be a lot of difficulties
involved in creating such a game; however, none would be insuperable.
And, if it was well-executed, it would be a spectacular roguelike.
Nice post, Graagh. Of course, it will be a long time, if ever, before
much of this comes to fruition, but there are a lot of good ideas
here.

Big Bad Joe

Chris Kern's profile photo
Chris Kern
unread,
Apr 30, 2001, 1:55:45 PM
to

Nice post. I especially like your object oriented language idea. I
have toyed with the idea (and am still considering it) of making an
Angband variant coded in Java. There are many advantages to this
approach which would lead to some of the things you stated here.
-Chris

Bahman Rabii's profile photo
Bahman Rabii
unread,
Apr 30, 2001, 8:03:38 AM
to
ke...@grinnell.edu (Chris Kern) writes:
The Java virtual machine is at least an order of magnitude slower than
I would want for a *band. I'm not a big fan of just-in-time-compilers
(jits), and that is less standard on the user end. True compilers for
java are not developed enough yet, IMO (give it a couple of years).

C++ is viable. The other option is to program in a proceedural
language with an object oriented mindset. We could certainly use more
of that, especially in the variants (mine included).

--
Bahman Rabii
bah...@topped-with-meat.com
http://www.consume.org/Oangband

LucFrench's profile photo
LucFrench
unread,
Apr 30, 2001, 3:27:12 PM
to
Or use a Python/C method.

C for the more important items (the RNG, and the more time intensive items),
and Python for the rest.

The resulting speed would be acceptable, as long as you're willing to write
from (mostly) scratch.

Thanks
Luc "Monty" French

Graaagh the Mighty's profile photo
Graaagh the Mighty
unread,
Apr 30, 2001, 3:32:06 PM
to
From the Rational Design article (note References: header), recall the
notes on quests, on avoiding weird and heavy-handed game mechanics,
and on the object generation system (designed for maximum flexibility
and extensibility).
How should quests be created?

A quest has four basic components, one optional.
1. The player character has an in-game method of *learning of* the
quest. Being asked to do something by an NPC is a common one.
Reading a history of the region and finding mention of a lost
treasure is a less common but plausible one that is equally good
role-play.
2. The quest has an *objective*. This can be expressed as a predicate:
if such and such is true in the game world the objective is met.
What has to be true is the *objective condition*, e.g. "Foo nasty
evil unique is dead" or "player inventory contains bar artifact".
The quest is *won* if the objective condition becomes true.
3. The quest has a *reward*. Completing the objective causes something
nice to happen instantaneously. Commonly, all that "something nice"
is is that it becomes possible for something else nice (the reward
proper) to occur at a later time, e.g. the obtaining of an
artifact. For a "find the lost trteasure" type quest, of course,
the artifact, hoard of gold, or whatever that forms the objective
*is* the reward.
4. The quest *may* have *failure conditions* -- if one becomes true
the quest is over, but the reward is not obtained.

The quest *state* has the following possible evolutions:
unknown
|
\|/
known, incomplete
/ \
|/_ _\|
completed failed

with the "failed" branch possible only for a quest with failure
conditions. The game, of course, can end with each possible quest in
any of these possible states.

(The above may seem bleeding obvious, but establishing the terminology
and stating it in those terms makes what follows clearer.)

Now, there is one immediate question with quests: how to deal with a
quest condition being true at the time the quest is learned of?
1. Player can be rewarded immediately. Makes sense for lost treasures
and others with "self-rewarding quest conditions" -- if the player
stumbles on it without learning of it, they have the reward all the
same. With other quests it's much trickier sometimes. Suppose foo
NPC unique asks you to kill bar NPC unique and offers ten thousand
gold pieces? Well, killing bar does get you bar's drop, but that's
not the real reward, just a side effect. It is implied that foo NPC
unique will give you the money when you have met the criterion. So
perhaps the player is handed the gold as soon as they next talk to
foo NPC unique. But what is foo NPC unique? Telepathic or
omniscient of something? Or just relying on the PC being honest?
The former is unrealistic and heavy-handed. The latter is fine
role-play, but then it's unrealistic and heavy-handed if the PC is
automatically honest and the player can't do something to "trick"
the NPC. If the player can lie to the NPC, the quest itself is
pointless. No, the only sane solution is for foo NPC unique to
require proof -- say bar NPC unique's severed head on a popsicle
stick. Now the problem arises: player kills bar *first*, then talks
to foo. Foo, of course, doesn't know bar is dead and assigns the
quest. The player, of course, didn't know at the time he killed bar
that bar's dead body would be useful, so he left it lying around.
Presumably, unique corpses are artifacts, at least if they are
important, so the corpse is still lying where it fell. The player
backtracks and returns with it and claims his reward -- tedious but
things work. Of course, the player might do something stupid and
destroy the body explicitly (if that can be done with artifacts),
sell it, lose track of where it was ... ouch. Of course, the player
upon searching the body might discover some clue that its head
might be of value, but that is veering dangerously close to weird
game mechanics territory, in the area of ever-so-convenient
coincidences (there is no *in-game* reason for bar to shave "keep
me" in his hair or something is there?)... It's worse if there's
*no* proof of quest completion, so one must be accompanied by foo
NPC unique when the condition is met in order to complete the
quest; "completing" it out of foo NPC unique's LOS or whatever
actually *fails* the quest. The player should not be able to kill
bar without first being forewarned of this. The forewarning must
come from *in-band* methods -- in-game that is -- not spoiler files
or the game's external documentation, too! And that leads naturally
to...
2. Player cannot complete the quest or fail it without having learned
of it first. Commonly this is done in crpg's in a heavy-handed
fashion, e.g. by "hiding" the entrance to a quest-related locale
until the player gets the quest. This is just plain bad role-play
however. As an example, in ADOM if you start and talk to an NPC
called the "tiny girl" that is always generated in a planned
location, a cave magically opens in the wilderness. Methinks if
this girl can magically open caves at long range she doesn't need
the lowly PC's help! Solution: the quest can't be finished either
way until you learn of it *because you can't do much with it
without learning of it in-game*. Hypothetical examples to fix the
afore-mentioned ADOM quest, some good, some bad:
* The cave's first two levels are always accessible. The way to the
third is blocked and you need a key to open it. The key is given
to you by the tiny girl and keys compatible with that door can
*only* come from the tiny girl. Of course she tells you of the
quest when giving you the key. For completeness, she won't give
you the key if the PC doesn't acknowledge the quest; the PC
doesn't acknowledge the quest if he doesn't hear it assigned; the
PC doesn't hear it assigned if deaf or whatever. And doesn't
acknowledge it if mute -- with some clue that you need to get
un-mute and talk to her again if this occurs.
This is good role-play and works well, although in this
particular example explaining the door and key convincingly turns
out to be a bit difficult given the background of the quest as it
actually is in the game. It does, however, give the general
idea.
* The cave is huge and the goal tiny, and there is no obvious
method to find the route to the goal. Trial-and-error is made
ineffective by the sheer size of the place. The tiny girl tells
you the route.
This suffers from 3 problems:
1. How the hell does she know the route? (In other similar quests
this might however be reasonable for the NPC to know -- as for
why, if they know, they don't go there themselves, maybe
because they don't have a Pointy Object and the skill to use
it, and the PC does?)
2. The route *will* wind up in a spoiler file somewhere and
someone *will* use this. Moreover, veterans will remember the
route and reuse it anyways. This isn't a role-play issue at
first glance, but it is when you realize the PC whose player
read the spoilers/is a veteran effectively *magically knows*
the route! Randomizing the route from one game to another
alleviates this difficulty.
3. Some scumming bastard *will* solve the quest by an exhaustive
search, however bleeding huge the place is. Even if it is
infinite: if the quest is to be fair the route must
nonetheless be finite and moreover, must have a length cap;
that restricts the scummer to a finite search area.
Randomizing the route doesn't solve this one. This isn't bad
role-play (leaving aside the suspicion that the PC searching
the area either was *really* lucky or *magically knew* there
was something good there) but it is going to cause problems
elsewhere with rewarding logic and associated role-play,
perhaps.
* The goal is unachievable without, say, fire resistance.
This is problematical. We have two possibilities:
* The NPC gives you something to wear that confers fire
resistance, or a decent supply of something that gives temp
fire resistance.
What if the player *already has* fire resistance? Unlike our
specially-made key it's presumably common in the game, even if
rare at that stage of the game, and the player *could* luck
into it randomly.
* Not only is fire resist not too hard to obtain by that point,
but the NPC doesn't *give* you fire resistance, she merely
*tells you* to use it. Firstly, there's the matter of
benefitting from a spoiler again, and the associated bad
role-play of magic knowledge. Secondly, there's the matter of
common sense -- even if she *doesn't* tell you, if you wander
in there and see half a dozen ancient red dragons you'll
probably run for the exit thinking *I'll just grab some fire
resistance and then come right back* -- that is, if you don't
already *have* the resistance.
* The goal doesn't exist until the quest is assigned, even though
the setting does.
It works, but it's very difficult to justify on role-playing
grounds. It smacks of "weird coincidences" in the game world, or
our lowly NPC-who-needs-the-PC's-help-desperately nonetheless
wielding powerful magic.

Another issue involves time-limited quests. More ADOM examples:
* Several quests are failed or change state if too much game time
elapses after they are assigned.
* Some quests can only be taken within certain clevel ranges, and fail
if the PC passes the upper end of the ranges without completing
them.

The former *usually* pose serious problems no matter how they are
handled. Two possibilities exist:
1. The quest fails at a fixed absolute time in the game universe.
This almost always falls flat: the player will not necessarily
learn of the quest before that time is reached, unless it is
ridiculously far in the future, in which case why bother with a
time limit? A quest shouldn't end (including by failure) before the
player character knows it exists. Otherwise the player proper
benefits massively from spoily info, which in turn translates into
bad role-play: magical knowledge or an improbable coincidence.
The sole exception seems to be if the quest is assigned *when the
character is created* -- e.g. the character creation creates a
history including how your father went off to some cavern and has
not returned for 8 days, and you have decided to foolishly go there
to look for him. Perhaps you'll find him alive if you find him soon
enough, dead otherwise (not as good an outcome). This is a quest,
and decent from a role-playing standpoint. It works because the
PC *is* guaranteed to learn of the quest by a certain game time --
time zero in fact.
2. The quest fails a fixed time after it is learned-of. This solves
the problem of failing it *before* learning of it, but creates a
new problem: What is the mechanism for failure? Basically, learning
of the quest has to have a plausible *in-game* mechanism for
causing that timer to start ticking. Two plausible examples show
that this *can* work, but not very readily:
a. An NPC decides to test you: you have xyz time to do
such-and-such and prove it; if you succeed he'll give you baz
reward.
Reasonable in role-play terms, and scavenger hunts are fun.
b. You stumble on a coven of witches and overhear one fretting
about their need to obtain bumbleberry roots before the Sabbath
in order to cast a beneficial spell. You happen to know of a
source for bumbleberry roots.
Reasonable save for one nit: odd coincidence their need for
roots in a few days coincides with your stumbling onto them.
This doesn't work as a planned quest for this reason, but it
does work as a random quest for the exact same reason -- a
random encounter that is improbable (in reality as well as in
game) but potentially rewarding. Note that this also naturally
gives an example of a quest with a reward unspecified until
completed -- you have no idea what the beneficial spell does,
exactly, or else it doesn't affect you personally, but it's
fair to guess they will repay you somehow if you unexpectedly
and generously save their necks. This one could also be useful
to shift alignment, if such a concept is in the game, towards
"good" or similar.
Quests limited based on player level are impossible to justify on
role-play grounds -- or at least ones where reaching a certain level
causes failure. (An NPC might have in-character reasons not to assign
a dangerous quest to a character they can reasonably (in-game)
perceive as not being advanced enough to survive the attempt, of
course. It still makes more sense in most cases for them to assign it,
but warn a player character that seems not advanced enough, and let
the player risk it then or wait at his own discretion. A test with a
time limit administered by that NPC being a major exception to this
last.)

Rewarding can be handled in two ways:
* The reward is a direct outcome of completing the quest -- that is,
it consists entirely of the guaranteed items, guaranteed xp, and so
forth you will definitely be able to get in the course of completing
the quest. E.g.:
Quest: find lost city with hoards of gold.
Reward: hoards of gold.
Quest: defeat evil king, restoring peace to the land,
thereby getting his valuable artifact crown, not to mention
winning the game.
Reward (in-game): crown.
Quest: find prosperous town to the east.
Reward: access to stores/services/helpful NPCs in prosperous town to
the east.
* The reward requires additional steps, e.g. proving to some NPC that
you killed foo, or giving him artifact bar.
In this case, there must be a reasonable in-character way for the
NPC to know whether or not you completed the quest. This mechanism
actually causes there to be *two* quests: the one the player
perceives and the one the computer actually implements.
Learning: Good wizard says "Kill the evil wizard and ye shall be
handsomely rewarded. But you have to prove to me you killed him to
claim yer reward. They do say the wand he carries is unique -- there
is none other like it!"
Quest (player viewpoint): Kill evil wizard.
Quest (computer viewpoint): Give evil wizard's artifact wand to
good wizard.
Reward: Large sums of moolah (or, if the player is capable of using
it, they can say to hell with the money
and keep the wand! This might count as
an evil/dishonest/chaotic act for
purposes of PC alignment, of course...)
Note that the quest assignment message gives the player viewpoint:
kill the wizard. It also hints strongly at the method of proof,
obviating the need for spoilers (except perhaps for the exceedingly
dense). Presumably the proof is real -- the evil wizard is proof
against the theft of the wand from his still-living person somehow.
An alternative formulation (but without the character development
choice) is for the wand to be (a subset of) the reward: either
just showing it to the good wizard is enough, or the good wizard
hands it back and says he doesn't want it, just needed to make sure
it was genuine.
Learning: NPC tells player to recover the Runestone.
Quest (player viewpoint): Get the Runestone.
Quest (computer viewpoint): Give the Runestone to NPC, or perhaps
just show it.
Reward: Something.
Learning: NPC tells the player to get the Orb of Water and place it
in the Temple's receptacle, so the rains come back.
Quest (player viewpoint): Get and place the Orb.
Quest (conputer viewpoint): Either the NPC sees the Orb in place or
learns it is there from trustworthy
sources, or it actually rains (implying
that the Orb was restored).
Reward: Whatever.
With that last one the difference between the viewpoints is rather
subtle. The computer sees some additional conditions, but these are
fulfilled automatically when or shortly after the player completes
the quest from his or her view point.
In any case, the additional conditions, if not automatic and
guaranteed, must (and even then usually are) be easy for the player
to glean by knowledge imparted in game plus common sense. In a
sense, the player knows that merely getting the runestone alone
doesn't quite cut it, or merely killing the evil wizard, but
nonetheless the rest is perceived as not really the main task of the
quest by the player, merely as a final step after the main task. The
concept of "main task" is of course a cognitive one that is
meaningless to the computer, however, which sees only the final
condition.

With all of this understood, it is easy for a human being to concoct
good quests of all kinds, all great role-play, in endless variety.
This leaves the matter of computer-generated random quests.

The obvious basic approach is to construct the quest from elements of
some kind, each chosen randomly, with a reasonably large number of
combinations.

The simplest method is to have a fixed set of possible random quests.
Of course, players will scum for them all, and even if infinitely many
random quests are possible players will scum them for kit, XP, to do
more than anyone else has reportedly done, and so forth. Limiting this
scumming is tricky. Limiting where the locations involved can be
generated helps -- only a certain subset may be generated in areas
easily and safely accessible in the early game, for example, so the
scumming is effectively limited by clevel. This also allows making
more dangerous ones appear over game time in a natural way. Another
option (which can actually be combined with the above) is to generate
them rarely, and only at certain minimum intervals. If the world is
fully generated from the game's start, of course, this won't work,
otherwise it can be managed. Yet another possible solution is to hide
them so the player must luck into them even after they are generated.
Making some only available at fixed distances into infinite areas will
make scumming these ones progressively more difficult over time; those
not found in such environments might be made finite in number and
distributed with clevs as above. Of course, any area can be forced to
only ever generate up to a fixed number of them even if a larger
subset is possible.

The above does have quests that are really fixed, just randomly
placeable and non-guaranteed. True random quests require truly
combining elements -- that is, the quests aren't atomic.

The simplest randomization is to randomize the names of uniques
involved, and possibly randomize their abilities (as well as have
random elements to the locations involved).

More complex randomization requires a notion of quest *elements* with
rules for combining them. A quest element, then, is a miniature quest
in itself, but implicit rather than explicit to the player, usually.
(It *can* take the form of an explicit quest that can only be learned
of while solving the parent quest, and whose reward is needed to
progress in the parent quest). The general system to use is this:

* An element has a goal that is a logical "or" of alternative winning
conditions.
* Decide a level for the quest. (This can be a parameter to the
generation routine.)
* Decide on quest goal element. Any items or monsters or places
involved should be at most slightly deeper than level, preferably at
or a bit deeper than level.
* Decide on prerequisite elements for each term in goal element's
"or": completing all of these elements allows the goal element to be
attempted by that route. Some prerequisite elements will be decided
randomly; others will be determined by the goal -- e.g. if the goal
involves killing a balor, and this is well-nigh impossible without
death ray resistance, and the latter is rare at the quest's level,
throw obtaining this in as a prerequisite.
* Decide on their prerequisite elements, and so forth.
* Ensure that for each element, for each "or" term with no
prerequisites the term requires *in-game* learning of the quest to
make it true, if such a requirement is needed for role-play
purposes.
* Ensure that for each element, for each "or" term with prerequisites,
the term requires completion of all of the prerequisites to make it
true.
* Compute a level for this quest based on the levels of any it
* Decide on a set of "optional" elements -- e.g. it can't be done
without facing an ancient red dragon, therefore fire resistance is
desirable (though not essential, else we'd make it a prerequisite),
and at this quest's level fire resistance is still rather rare (the
dragon being a bit deeper than that level -- quests should have some
extra oomph right?), so with a certain probability generate with the
quest an item with fire resistance.
* For each element decide how the prerequisites being met can lead to
the goal.
* Generate the locations involved.
* Use the locations and prerequisites to construct a description of
the quest for the player to get upon learning of it -- e.g.
"kill foo to get bar". Base it on the uppermost elements, especially
the goal element. Pick a mechanism for the player to learn of the
quest. Pick a reward mechanism compatible with the learning (e.g. if
the player reads of a treasure buried somewhere the reward mechanism
has to be automatic: the treasure; if the player asks an NPC a
"proof->get reward" mechanism is allowable, *if* the goal condition
can be amended to generate proof; etc.)

The elements should be chosen from a random set. Each element in the
set has certain "hooks": what to do, why, what it might do to the
description string, and so forth.

What Why String
Get bar <goal>
Kill foo It has a bar "Kill foo to get bar"
Open door To reach foo <none -- player will try door after failing
to find foo anywhere else in quest location>
Get key To open door <none -- player finding locked door will know
they need to find a key when it proves to be
unpickable!>

Note that this is generated *backwards* -- e.g. we first generated a
goal element (get bar), then out of all the possible sets of
prerequisites for "get bar" we chose "kill something for it", then of
all the possible sets of prerequisites (including none) we chose "open
door", and so on. Now let us further examine how this can be done
algorithmically.

We have an element object. It acts as a generic template or
constructor for elements of a certain kind. The above example may
result from:

<set of possible goal elements> contains GetObject() and
KillCreature().

GetObject()
parameters: <none>
initialization: generate random item X
sets of possible prerequisites:
{GetToLocation(X)}
{GetObjectOffCreature(X)}
{GetObjectGuardedByCreature(X)}
{BuyObject(X)...}
string: Get <X> <prerequisite string>.
returns: X
proofs: possession of X
GetObject(X)
parameters: an object X
initialization: <none>
sets of possible prerequisites:
{GetToLocation(X)}
{GetObjectOffCreature(X)}
{GetObjectGuardedByCreature(X)}
{BuyObject(X)...}
string: Get <X> <prerequisite string>.
returns: <nothing>
proofs: possession of X
KillCreature()
parameters: <none>
initialization: generate random creature X
sets of possible prerequisites:
{GetToLocation(X)}
{GetToLocation(Y) and GetItemNeededToKill(X)}
{SummonCreature(X)}...
string: Kill <X> <prerequisite string>.
returns: X
proofs: possession of some (preferably unique) item
generated on X; any side effects of X's death.
GetObjectGuardedByCreature(X)
parameters: an item X
initialization: generate random location L and place X in it;
place Y guarding X (e.g. L must contain a choke
point between all possible entrances and a subset of
L, X must be placed in that subset, and Y must be
placed in the choke point); choose L and Y in theme
for X.
sets of possible prerequisites:
{GetToLocation(L)}
string: guarded by <Y> <prerequisite string>
returns: X
proofs: possession of X
GetObjectOffCreature(X)
parameters: an item X
generation: generate random creature Y and place X on its person;
choose Y in theme for X.
sets of possible prerequisites:
{GetToLocation(Y)}
{GetToLocation(Y), GetItemNeededToKill(X)} ...
string: from <Y> <prerequisite string>.
returns: X
proofs: possession of X
GetToLocation(Y)
parameters: an item, creature, or location Y
initialization: if Y is not a location, generate a location L
containing Y, with L in theme for Y; otherwise
set L := Y.
sets of possible prerequisites:
{PassObstacleToReach(L)}
{LearnOf(L)}
string: get to L <prerequisite string> if Y == L; <parameter> from
<L> <prerequisite string> if Y is an item; otherwise
<parameter> in <L> <prerequisite string>. (example results:
get cloak of invisibility from cavern; get cloak of
invisibility from dwarf in cavern; kill dwarf in cavern; get
to cavern)
returns: Y
proofs: being in L
PassObstacleToReach(L)
parameters: a location L
initialization: generate a location M containing L with obstacles
on a set that acts as a noncontiguous chokepoint to
reach L from any entrance. Push M on a stack of
locations to place from quest construction engine.
Determine obstacles by way of prerequisite return
values and place them appropriately.
sets of possible prerequisites:
{PassObstacle() -- repeated for various obstacles generated within
M.}
string: <prerequisite strings listed using 'or'> -- e.g.
". You'll need the <foo> or the <bar>" and the like.
returns: L
proofs: being in L
PassObstacle()
parameters: <none>
initialization: <none>
sets of possible prerequisites:
{PassDoor()}
{PassFlames()}
{PassCompoundObstacle()}
-- repeated for other obstacle types.
string: <prerequisite string>
returns: <prerequisite return>
proofs: <prerequisite proofs>
PassDoor()
parameters: <none>
initialization: Generate a door X and a key Y. Make X unopenable
without Y.
sets of possible prerequisites:
{Get(Y)}
{LearnAndGet(Y)}
string: <Y> or nothing.
returns: X
proofs: X is unlocked
PassFlames()
parameters: <none>
initialization: Generate a flaming obstacle X and an object Y that
grants fire resistance; if fire resistance is common
by this stage skip generating Y. If protecting
equipment from fire is difficult at this
stage, possibly generate a means to get protection
for equipment as an option. Place this in an
unplaced location and push that on a stack of
locations to place from quest construction engine.
Make description incorporate a hint pointing the
player to that location.
sets of possible prerequisites:
{Get(Y)}
{LearnAndGet(Y)}
-- Omit any prerequisites if fire resistance is common by this
stage.
string: <Y> or nothing.
returns: X
proofs: player walked through X
PassCompoundObstacle():
parameters: <none>
initialization: call PassObstacle twice and construct a location L
with two exits (e.g. a corridor) and two sequential
choke points between them and an obstacle at each
choke point.
sets of possible prerequisites:
{PassObstacle() and PassObstacle()}
string: <prerequisite strings in "and" list> or nothing.
returns: L
proofs: <proof of prerequisite 1> and <proof of prerequisite 2>
LearnOf(L):
parameters: a location L
initialization: push L on a stack of locations to place from quest
construction engine.
sets of possible prerequisites:
<none>
string: <none>
returns: L
proofs: <none>
LearnAndGet(Y):
parameters: an item Y
initialization: push Y on a stack of items to get during quest
assignment.
sets of possible prerequisites:
<none>
string: <none>
returns: Y
proofs: possession of Y

Other suggested elements: give X to Y, place X at Y (to cause Z), ...
-- note that these have many interesting branches -- they require
getting X *and* finding Y.

Quest generation then works by picking a goal, doing it recursively,
and then examining the stacks of locations and items -- placing the
former and using the latter in generating the way to obtain the quest.
If the item stack happens to be non-empty and the goal condition has
proofs it can generate a post-quest reward whose condition is
generated using the goal condition proofs and the learning mechanism
(e.g. if it's an NPC they must be shown the proof to get the reward).

Randomly placeable planned items, monsters, or locations can be used
in random quests as important items; key items or monsters will
presumably be unique. Actually random items, monsters, and locations
can be used too -- including random artifacts and random unique
monsters.

Quest element selection should use levels/rarities as with item
selection; selection should be more likely to pick a prerequisite over
none (when the latter is an option) with increasing level of the
quest, so that more involved random quests increase in likelihood with
level.

The quest itself is placed by placing all of its locations (and
therefore creatures and items). With random quests the locations
should usually be generated clustered. Exceptions should be handled as
follows:
* The stack of locations generated is actually a stack of sets; each
set is placed as a grouping.
* Locations and other stuff is generated in the theme in context where
the questis generated.
* The exceptions occur if the random quest uses elements of a "travel
to" nature. These place their subsidiary locations in separate sets
and whereas these sets get themes assigned and the subsidiary
locations must be in theme for the containing set and so forth, a
new set can get any theme. Travelling elements should be relatively
improbable.
* If a travelling element is generated subsidiary to a travelling
element, the resulting set is regarded as subordinate to the prior
one's set. Top level travelling elements are regarded as subordinate
to the initial set (the goal set).
* The deepest nested set gets the quest discovery stuff placed in it,
and has level the quest level. Traversal of the set tree is then
done to set other levels: going up to a parent, the parent gets a
level comparable to or somewhat deeper than the child; going down to
a child the child gets a level comparable to or somewhat shallower
than the parent. Within a set, the direct member locations are
generated at the set's level, and nested locations may increase in
level gradually. The higher a set's level, the more the maximum and
average level displacements of any traversed-to set.
* The set with the quest discovery stuff gets its locations strewn
about wherever the quest itself is generated, in a chosen containing
location of level the quest's level (this location is what
*determined* the level at which to generate the quest). Each
additional set gets placed randomly anywhere in the world where that
is unexplored (and can thus get stuff placed in it) or long enough
unvisited to have changed radically. The set's theme and level
restricts its placement.
* The quest assignment involves a text string explaining the goal and
any significantly nonobvious requirements that aren't learned of
along the way. That string's construction pattern could be as
indicated above but will probably be more complex. Conversion of
locations to strings happens after all locations are placed, and
describes the location relative to either the quest discovery
location or (if one exists) a nearby prominent landmark the player
can't miss in his explorations (this *can* be randomly generated, if
it happens to be distinctive). Item descriptions involve giving
important items that must be described a distinctive flavor and
giving the flavor to the player, possibly along with a hint as to
what the item is or does (e.g. if it is an artifact and you get to
keep it/must use it). Monster descriptions similarly.
* The goal will have the highest level of any part of the quest. Any
post-quest reward should be generated at or slightly deeper than
that level.

Final notes:
Making an algorithm to decide if a randomly generated location is
distinctive and if so to generate a description, making an algorithm
to deal with quest assignment strings, making an algorithm to decide
whether an ancient red dragon placed at *this* level should cause fire
resistance to be a prerequisite, to be placed but not a prerequisite,
or not to be placed at all, making an algorithm to decide which
prerequisites to include in the quest assignment string, making an
system to decide which proofs are compatible with what possible
(random) assignment mechanisms for post-quest rewards and via what
testing mechanisms (NPC LOS? Side effects of action?), making an
algorithm to decide whether a quest is self-rewarding or not (and
force regeneration if there is no automatic "climactic" reward and no
post-quest reward is possible), making an algorithm to decide if the
quest set-up is likely to make the player do the quest automatically,
whether the existence and nature of the reward should be hinted at, or
whether the reward should be explicitly indicated as existing, and
similar such hairy tasks are left as exercises to the reader. <eg>

Graaagh the Mighty's profile photo
Graaagh the Mighty
unread,
Apr 30, 2001, 3:35:26 PM
to
On Mon, 30 Apr 2001 16:30:09 GMT, BigBadJ...@hotmail.com (Big Bad
Joe) sat on a tribble, which squeaked:
>On Mon, 30 Apr 2001 12:41:45 GMT, inv...@erehwon.invalid (Graaagh the
>Mighty) drank a fifth of Old Crow and wrote:
>
><all-time record-holding snippage>
>
>Wow...a lot to think about here. There would be a lot of difficulties
>involved in creating such a game; however, none would be insuperable.

Of course -- if they were I wouldn't have posted it. In fact
algorithms for some of this shit are evolving in my head right now,
and the rest I have a sketch of implementation ideas for -- enough to
convince me *I* can do it, which means probably that anyone can.

>And, if it was well-executed, it would be a spectacular roguelike.
>Nice post, Graagh. Of course, it will be a long time, if ever, before
>much of this comes to fruition, but there are a lot of good ideas
>here.

Working nonstop and without many unexpected hurdles or setbacks (e.g.
disk crashes *forks the evil eye at the RNG*) I could probably cobble
together the engine and a prototype very-simple test campaign in six
weeks.

However, sleep and food are basic necessities, so six weeks of nonstop
anything are impossible. :-)

Graaagh the Mighty's profile photo
Graaagh the Mighty
unread,
Apr 30, 2001, 3:38:29 PM
to
On Mon, 30 Apr 2001 17:55:45 GMT, ke...@grinnell.edu (Chris Kern) sat

on a tribble, which squeaked:
>


>Nice post. I especially like your object oriented language idea.

You probably can make a CRPG without using OO.
You probably cannot make a decent CRPG without using OO.
(Note that you can use C or <name structured language here> and still
be OO, if the language has a concept of function pointers *or*
self-modifying code can be written. [The latter can be used to make a
hack that acts like function pointers.])

>I have toyed with the idea (and am still considering it) of making an
>Angband variant coded in Java. There are many advantages to this
>approach which would lead to some of the things you stated here.

Java was my language of choice. I have a partially complete version of
the code to generate specialized random <foo>, but it has to be
heavily reworked and updated and I will probably just rewrite it. It
is, however, based on generic algorithms, allowing you to use the item
generation engine on items, monsters, features/locations, random quest
components (see new thread), etc.

Chris Kern's profile photo
Chris Kern
unread,
Apr 30, 2001, 4:38:18 PM
to
On 30 Apr 2001 05:03:38 -0700, Bahman Rabii
<bah...@unmaker.house-of-toast.com> posted the following:
>ke...@grinnell.edu (Chris Kern) writes:
>
>> Nice post. I especially like your object oriented language idea. I
>> have toyed with the idea (and am still considering it) of making an
>> Angband variant coded in Java. There are many advantages to this
>> approach which would lead to some of the things you stated here.
>
>The Java virtual machine is at least an order of magnitude slower than
>I would want for a *band.

This is somewhat ridiculous...I can't buy that the JVM runs ten times
slower than a C program.

> I'm not a big fan of just-in-time-compilers
>(jits), and that is less standard on the user end. True compilers for
>java are not developed enough yet, IMO (give it a couple of years).

It would take a couple of years to write this :)

You would need a decent system to run this proposed game because of
the complexity of each object (monsters having inventories, able to
drink potions, use wands, move up levels, etc.). In my experience a
non-graphical Java program runs fast enough. I would not propose that
Angband be rewritten in Java, just that some variant come out written
in Java.

>C++ is viable.

I don't like C++ much.

-Chris

Chris Kern's profile photo
Chris Kern
unread,
Apr 30, 2001, 4:40:17 PM
to
On Mon, 30 Apr 2001 19:38:29 GMT, inv...@erehwon.invalid (Graaagh the
Mighty) posted the following:
>On Mon, 30 Apr 2001 17:55:45 GMT, ke...@grinnell.edu (Chris Kern) sat
>on a tribble, which squeaked:
>
>>
>>Nice post. I especially like your object oriented language idea.
>
>You probably can make a CRPG without using OO.
>You probably cannot make a decent CRPG without using OO.

I don't think I would agree with this, OO is just a programming
paradigm.

But I do like the idea of making the monsters and players much more
alike. So you could find a monster on a level, talk it into joining
you, and then it could walk around killing things, gaining levels,
getting things, equipping and using them, etc. Most of the code that
worked for the player would also work for the monster.

I would try this more if it wasn't so time consuming :-)

-Chris

Graaagh the Mighty's profile photo
Graaagh the Mighty
unread,
Apr 30, 2001, 4:31:15 PM
to
On 30 Apr 2001 05:03:38 -0700, Bahman Rabii
<bah...@unmaker.house-of-toast.com> sat on a tribble, which squeaked:
>ke...@grinnell.edu (Chris Kern) writes:
>
>> Nice post. I especially like your object oriented language idea. I
>> have toyed with the idea (and am still considering it) of making an
>> Angband variant coded in Java. There are many advantages to this
>> approach which would lead to some of the things you stated here.
>
>The Java virtual machine is at least an order of magnitude slower than
>I would want for a *band.

I disagree. On any machine that runs Java at all (32 bit architecture
being a *bare* minimum, and possibly not sufficient in and of itself)
Java would run fast enough without any (JIT or otherwise) compiling
for a turn-based game. A few optimization tricks would be needed but I
have tons of these up my sleeve:

* The world is not generated all at once. It is, say, an infinite
cubical lattice divided into cubical domains in regular fashion --
e.g. at divisions of 256 individual lattice cells on each axis.
In making a hierarchy of locations, parent locations (e.g. forest,
the world itself, &c.) are generated -- they define themselves by
a function that efficiently tests whether a cell is a member.
(This allows infinite elements without needing infinite space.)
At game start the "world" location is generated and some
sub-locations are generated that are guaranteed, including the start
location. From then on, the domain containing the player and any
other domain the player is in some sensing range of is considered
"active" at any given time. When a domain becomes active, a test is
performed (and this can be made efficient) for whether it contains
ungenerated cells. If it does, the cells in it get generated. How?
See below:
-- Each domain has an address -- three coordinates in units of full
domains from the world origin coordinate.
-- Each location tracks which domains it touches, using a function
touchesDomain(), allowing efficient implementation for infinite
locations, similarly to the hinted-at-above containsCell().
-- Each location tracks child locations and for each domain it
touches that a child location touches, it tracks the domains.
Again a function is used: childTouchesDomain() takes a domain
address and child.
-- Each location tracks whether it has generated its children.
-- The world tracks whether it has generated each domain. This is
done by maintaining a list of domains every cell of which is
generated.
-- When a domain becomes active, if the domain is on that list,
nothing is generated.
-- If the domain is not on that list, a traversal of locations
occurs starting with the world. At each step the current domain
generates its children if it hasn't already, then checks which
children touch the target domain. This set is then traversed.
Depth-first traversal is used. Recursion backtracks whenever a
location is hit that is atomic (a single cell) and returns when
the depth-first traversal ends.
-- Upshot: every cell in an active domain is generated at that
point. That domain is added to the list.
-- The list of completed domains is maintained using a hash
table so membership tests are O(1) even when the list gets large.
-- Cells have content (air, wall, floor, maybe gas or fire...), a
floor (null, solid, dangerous, rubble), a pile of (possibly
dissimilar) items of limited volume, and an occupant (or none).
-- Cells generated at certain levels and in certain themes track
this.
-- Completed domains and all locations track time since last active.
Recently active ones have items and monsters partially
regenerated when reactivated. Less recently active ones may
receive minor structural changes. Long-inactive ones may receive
major structural changes, which means they may be taken off the
completed list and some of the locations touching them cleared
(i.e. the children are removed and whether it has generated
children is reset to "false"). This occurs as part of activating
the location, *before* any necessary generation and *before*
changing the last active timestamp. So a long inactive domain the
player approaches may:
* get taken off the completed list
* have some locations touching it cleared -- ones not touching
any active cells only, of course -- this is done by choosing a
cell not marked "never change" and going up the location
hierarchy to the highest one that can be cleared -- a location
can be cleared if it touches no active domain and either it
isn't marked "clear only when clearing parent" or the parent
can be cleared. (This lets an old orc citadel disappear without
allowing its chieftain's house to disappear under any other
circumstances, and so forth, properly applied.)
* have the locations regenerated
* get put on the completed list
* get marked recently active
This allows for a continuous world with some 3d elements while
keeping updating stuff manageable (only monsters/NPCs in active
domains actually act -- apparent change in remote domains is created
stochastically and cheaply when they are reactivated).
It also causes incremental generation of the world, generally only 1
domain at a time, and never more than 8 at a time. (Max player
perception radius must be at most domain size; domain size should
not be much larger than max player perception radius for
efficiency). The nesting of locations means the game has a
low-detail overview of the world, with more detail near the
player, still more still nearer, and full detail generated right
near the player.
Also, inactive domains are swapped out of memory when they are
inactivated (but once swapping out is triggered it occurs
asynchronously, since the I/O involved might be slow). This
avoids the memory requirement ever exceeding (8 domains)*(max number
of simultaneous PCs), although the disk space requirements are
larger.
Saved games can be kept reasonable by discarding the details of
domains that have been inactive long enough to be regenerated.
Moreover, memory can be saved at slight loss in efficiency by
keeping a list of inactive domains in a queue, pushing domains
on the top of the queue when they become inactive, popping domains
from the middle of the queue that become active, and periodically
polling the bottom of the queue for domains inactive long enough to
be regenerated -- these last are discarded completely from memory
then and there, and the queue re-polled in case the second-last (now
the last) is similarly old, until one isn't. The poll overhead is
low. Heck all of that is low overhead.
All times discussed are in-game time, not real-world time.
* Generating stuff randomly: it can be arranged so that only a
weighted random walk down the tree of classes occurs. This is
limited by the depth of nested classes. Egoizer generation and
subclass selection at each walk step involves iteration over
applicable egoizers or subclasses at that step. This means the worst
case generation is the max over all possible walks down the class
hierarchy of the sum over a walk of the size of the set of egoizers
plus the size of the set of subclasses at each node.
Optimizing the hierarchy to minimize this should be easy. Also
expected running time depends on rarities (or frequencies) at each
step. Making objects that are expensive to generate rare at a point
before the bulk of that expense occurs will help.
* If pauses to generate domains are noticeable, either because of
items or because of the generation itself, this can be remedied as
follows:
-- Any domain adjacent to an active domain is *pre-active*.
-- If a domain becomes pre-active that needs generating, start
generating it *asynchronously*.
-- If a domain becomes active that is not finished generating,
block until all such are generated.

There's plenty more where those came from.

>C++ is viable. The other option is to program in a proceedural
>language with an object oriented mindset. We could certainly use more
>of that, especially in the variants (mine included).

Java has a big advantage over C++ and any other "compiled into stone"
language, and I don't mean graphics.

Plug-ins.

Suppose you want to make a new campaign. It will probably include new
executable code. Lots of it.
C/C++ engine: Requires a recompile. (Or you have to mess around, both
in the engine and in the campaign code, with a scripting
language -- ugh.)
Java engine: Drop the class files in the class-path of the engine,
pass some kind of game-initialization class as a
parameter to the engine command-line (preferably
supplying a batch file and a shell script to launch your
variant on the common platforms -- DOS/Windows, Unix),
and it loads the proper class and uses it to generate the
in-game-objects hierarchy, including the object whose
code generates the world .........

Basically, Java is a ready-made and convenient solution to the
scripting-language system, if you view the VM as equivalent to the
script interpreter the first solution requires the engine use, and the
class files as the scripts.

Java makes it easy to bundle all the data in the game class file jar
too, using ListResourceBundle, with the added bonus of making it easy
to localize strings while you're at it (as those bundles can have
locale-specific specializations in Java, which are automatically used
in the appropriate locale -- the specializations do not duplicate the
whole general bundle, only specifying keys with values different from
the parent's value for that key, along with the different values).

Matthias Kurzke's profile photo
Matthias Kurzke
unread,
Apr 30, 2001, 7:14:02 PM
to
On Mon, 30 Apr 2001 12:41:45 GMT, inv...@erehwon.invalid (Graaagh the
Mighty) wrote:
>Lots of postings here (and in rec.games.roguelike.adom as a matter of
>fact) have illuminated a number of issues with current roguelikes. The
>following chart illustrates these. The chart includes every RPG I've
>played, with emphasis on CRPGs, particularly roguelikes, and
>especially Angband variants, and a few I haven't but know something
>about.
>

[*snip the explanations of the classification system*]

I take the liberty of taking this already slightly off-topic thread
(it would probably belong to r.g.r.development...) and adding some
comments about a classic single-player-controls-a-party CRPG.

Game |Life|Item|Structure |Docs |Fair|Scumming|Misc

Might&Magic4/5 TN II TQLVWClCsCtEH CD? AM?

This is a "classic" CRPG for me (as is The Bard's Tale) that mostly
lacks randomness. (you have a fixed map with fixed dungeons, and only
the usual "random encounters"). The story is rather linear but
exploring the map gives you some nice extras. Upon death of the whole
party (you control 6 adventurers, usually one or two fighter-type, one
rogue, one wizard, one or two healers/paladins etc.) you return to
town (IIRC). Death of one character is not permanent, they can be
resurrected at the cost of one permanent CON point (i.e. ideally you
avoid this to happen, especially since there is only a finite number
of stat potions in the game. Scumming for gold is possible, but not
necessary for winning the game -- it IS necessary only for maxing out
your abilities (level goes up when you have experience PLUS go to a
"training area", most of which are limited in level and cost lots of
money). Problem is, of course, it's too easy. Learn where the traps in
the dungeons are, learn the order in which to go to places, and with
the restore game feature you always win in a reasonable amount of
time, with no big replay value. Still, I enjoyed it.

[Sorry for the long description, but I felt this type of CRPGs was
missing in your list -- the ones with emphasis on "story" (although
this one's rather linear) and discovery. Maybe Zelda is actually
closest?]

>
>Game |Life |Structure |Docs |Fair|Scumming|Misc
>Perfection? S?A?N? TQLWClCsCtRRE S?DDD S Z?P*?
>
>(Here, a ? following a symbol indicates that it is open to question
>whether we include it or not -- we can probably make the Right Thing
>either way. More than one solution, IOW. We could also make a CRPG
>that is not a roguelike and get something Right I am sure.)
>

Something Right == A Really Good Game, if I understand you correctly.

>The following discussion is broken into sections related to the
>columns of the tables above.
>
>1. Lifesaving, cursed items, and spoilers.
>First let's examine the trouble spots in existing CRPGs that have
>permanent death.

[snip]


>
>All of these problems stem from one fact. If you die without
>life-saving, the game is over; if amulets of life-saving or potions of
>blood of life or potions of invulnerability are made too common, the
>game is trivial.
>
>There are exactly three potential solutions to this dilemma. Note that
>no extant roguelike seems to use either, and the first person shooters
>don't either, but some non-roguelike CRPGs do...

> ii. Infinitely many checkpoints/reusable checkpoints, but not
> too easily accessible -- e.g. you have to go to an inn in a
> town to save the game. Note that the Zelda games go this
> route -- going to sanctuary or entering a dungeon cause
> checkpoint uses. IMO a good choice (randomness and
> nonlinearity can still provide replay value even without a
> way to "lose the game"; the inevitable setbacks give the
> player a reason to fear death and prepare before tackling
> difficult areas of the game, but also let them experiment a
> bit and learn some stuff by trial and error).

This is good in games that have something to explore (Angband hasn't,
but Zangband's old fixed quests are something that makes me want to
use this kind of cheating death / going back to a checkpoint. Some of
the quests are easy if you're prepared right, and hard if you don't
know them -- and they're boring after a while, because if you die
often, you have to replay the same quests over and over. I don't
really want to see the Thieves quest ever again... )

>2. Death is permanent, but the game doesn't end just because the
> player character dies. This requires a party of characters that can
> continue while diminished -- the real problem with most roguelikes
> isn't permanent death, but the combo of permanent death and "you
> versus the world". Permanent death with parties raises questions:
> * Are there multiple PCs?

> * What happens when someone dies?

> c. NPCs are replaceable, and new PCs can be rolled up at certain
> locations and journey to find the party or otherwise resume
> the game, without the game restarting.

This was possible in the M&M games. (You could roll up new party
members at the Inns in the various towns (like in the Adventurer's
Guild in The Bard's Tale) and they had the problem of being much
weaker than your party members, at least at first. But probably random
wilderness encounters would be enough to get them up... equipment
provided by the other party members).

> * Is death occasionally reversible?

M&M allowed resurrection as a high-level cleric spell (also costing a
lot of gems) or in temples. You still had to get your reduced party
(with at least one member still alive / not turned to stone / turned
into a skeleton) back to the next good temple, which was nontrivial if
you were in the middle of a dungeon and hadn't taken the right
precautions. But it was too easy because it *also* allowed restores if
all died...

>
>1aii and 2c seem to have tied for the best solution to this issue. For
>part of that roguelike flavor, we shall go with option 2c: there is a
>party, including one or more PCs and zero or more NPCs, and the game
>ends if you quit (including after a win) or the whole party is
>destroyed (which is a loss if you didn't in fact win first). Moreover,
>we shall (for simplicity's sake) limit to one PC in the party. If an
>NPC dies the player can lead the party to a town, where another NPC
>can be recruited (and there might be other circumstances where an NPC
>replacement *might* be obtainable). If the PC dies, the game goes on
>-- the player rolls up a new PC, who starts in some town in the same
>game world with the game state continuing to evolve, and he may
>recruit some NPCs and may manage to find (and perhaps join forces
>with) the surviving NPCs from the previous attempt. In this way, the
>game sort of goes on after a sort-of-loss, but perseverance should win
>the game eventually.
>

What are the NPCs supposed to do? If I can only control the PC and the
NPCs are controlled by some kind of AI, what will they do? Will they
try to heal me/resurrect me? Will they take suggestions/commands from
me? (Making them essentially PCs). If they are "realistic", they
should try to recruit a new party member instead of the deceased PC
and go on win the game. (Say a party of Borgs :-) Or they might decide
not to go where you want to go... (without a "free will", they will
lack depth and essentially be like aimple pets).
If you can control the whole party, you usually have fighters,
wizards, clerics and everything you need at your disposal. This can
easily be too powerful, except in cases where there's more possible
abilities you could need than party members to have them.

You have to be careful about the "party" approach. It shouldn't ONLY
be there for an interpretation of non-permanent death...

>3. Documentation and Character Knowledge. (We'll get to structure
>eventually.)
>
>Ideally, our game documents some basic, required knowledge of game
>mechanics, some knowledge of the game software's interface, and a
>getting started guide as "standard" documentation, but everything else
>is learned in-game by in-character means, from what potions exist, to
>what this potion does, to what this monster breathes.

This is indeed desirable. Note that (a) Nethack is much like that, at
least if you play it without spoilers [but that is IMHO impossible
(maybe I'm just too stupid)] and (b) I started to play Moria/Angband
in that way -- with a bit of info in a help file, and finding out a
lot of other things by dying to Gravity Hounds/Azriel etc. Yes I did
savefile scum. No I don't anymore.

[snip]

>Then there's the question of identify. Magical identification should
>be rare and special. Finding things out by experimentation, from lore,
>and from sensible game world mechanisms is preferable to hand-waving
>like that. Our game won't have any scrolls of identify, nevermind
>ADOM's blessed scrolls of identify. But it will have a bunch of
>learnable, improvable appraising skills, and ways to generically
>"detect enchantment" and such; and once something is known to be
>magical it can be tried (potions and scrolls can be tried regardless).
>

This is very good, as long as trying out things always has a
reasonable risk/reward ratio (like IDing Wands in Angband -- if you
try out an unknown wand on a tough monster you're insane, but it's
usually not hard to find reasonable targets). There's even monsters
you can use to find out your resists in relatively safe ways, but the
cheapness of ID and *ID* in Angband makes that not necessary...

>6. Structure.
>
>The right balance between structure and randomness is tricky to get
>sometimes. We will discuss this a bit, then describe a mechanism
>likely to give good results.
>
>Replay value really requires lots of randomness, and roguelikes
>traditionally have lots of it. Structure, however, makes the game
>interesting and gives players that sense of exploring a large, real,
>and living world. Towards this end, we note two kinds of structure.
>

>Moreover, the game may be rendered capable of generating *random
>uniques* -- random unique items (indestructible such being random
>artifacts), random unique NPCs/monsters, and random unique places.
>These may even be structured into random quests that are, nonetheless,
>interesting role-play -- no "This level is guarded by 22 Greater Hell
>Beasts" garbage here!

Well, how should these be structured? There's not so many "generic"
ways to build up quests -- and "our village is in danger! please kill
all monsters of type X in area Y" or "wizard X needs artifact Y from
place Z. please bring it for us" is always only a finite number of
quest types. Plus it easily lacks the fine-tuning that would make a
good story (quests are not so great if there is no story associated to
them). Well... but it's probably worth a try IF these random quests
don't appear too often (say, have 30 quest type templates and have 10
random quests in a game of average length).

[snip snip snip -- really a LONG post Graagh...]


>7. Miscellaneous items.
>T -- slow and tedious to start a new character. (Undesirable,
> especially in combination with 'E' or 'U' in fairness column.)
>R -- you have to be a rocket scientist to start a new character.
> (Undesirable -- basicaly you'll be messing with zillions of
> options and poring over documentation. Or dying a lot. Or both.)
>S -- Starting a new character, it is well-nigh necessary to scum for
> high starting stats or something similar. (Undesirable.)
>SS -- The game actually has built-in features to assist in automated
> scumming for high starting stats or whatever. (Undesirable.)
>
>Starting a new character will be easy and painless in our game. Pick
>race, pick class, get char with random stats and decent capability to
>play the game competently. Away you go!
>

Well... removing the need for autoroll / point based stats in Angband
would be a good thing, I am sure... if decent random characters can
still be made.

>Z -- Endgame characters of the same race and class don't have much to
> distinguish them. (Neutral or undesirable.)
>
>No problemo here. Not only might the endgame depend on the class and
>race, but it might depend on player choices and random factors.
>*Multiple endgames* might be possible! Random uniques will add another
>random factor -- a random artifact might make one game very different
>from another even with other things being equal.
>

Angband endgame also depends on what artifacts you find, but
admittedly not enough so. JLE patch improves this.


>
>W -- Weird game mechanics. (Undesirable -- catch-all for weird,
> unrealistic or bad roleplay game mechanics not covered above.)
>
>Shops will be real. Shopkeepers will not be omniscient. That weapons
>store owner in that early town knows a lot about local weapons and can
>appraose them well, but he knows considerably less about the weapons
>used in the land over yonder, or about that rare and well-crafted item
>you found in the dungeon. With rare and exotic items, he can
>nonetheless give a slightly useful guess as to its power or
>wretchedness, and often a much better idea of who to see or where to
>go to seek more information about it... Moreover, they won't see you
>pick up an item if they don't have LOS when you take it. (That's why a
>lot of the shops will have an open and roughly round shape, so the
>shopkeeper has LOS to every item...)

Any convex shape will do :-)

[snip couple of other good ideas]

>8. Conclusion.
>
>Above is a blueprint for making a roguelike game head and shoulders
>above the rest. Not only that, in an object oriented language it
>should be possible to design an *engine* into which the planned
>species of monster and item and place and the limits and parameters
>for constructing and deploying random ones can be plugged. The one
>engine could easily support thousands of different variants, and
>multiple "campaigns" for each variant (same "world" in some sense,
>different quests/goal/new stuff/removed stuff...)

Some more general comments:

(A) Did you read the "Development" section of Roguelike News? If not,
you should...

(B) You could try to post this in r.g.r.development (maybe adding a
[LONG] in the title...) and I think you'll get some more feedback.

(C) How many man-years do you expect until this becomes a playable
game? ;-)

Good luck,

Matthias

Scott Baxter's profile photo
Scott Baxter
unread,
Apr 30, 2001, 7:17:38 PM
to
Chris Kern wrote:
>
> On 30 Apr 2001 05:03:38 -0700, Bahman Rabii
> <bah...@unmaker.house-of-toast.com> posted the following:
>
> >The Java virtual machine is at least an order of magnitude slower than
> >I would want for a *band.
>
> This is somewhat ridiculous...I can't buy that the JVM runs ten times
> slower than a C program.
Well, to be pedantic it's the program running on top of the JVM that you
need to compare. It depends on the JVM, the platform, and what exactly
the program is doing, but ten times slower than C isn't that bad as an
off-the-cuff estimate for processor-intensive apps (like game AI or
generating levels). Java works best for apps where the main slowdowns
are due to outside communication rather than instruction-crunching.

A Java roguelike would be cool to try (wasn't ADOM going to do this at
some point?), but I wouldn't expect it run as quickly as any *band.

--
Scott Baxter
"listen:there's a hell
of a good universe next door;let's go"
- e. e. cummings

Big Bad Joe's profile photo
Big Bad Joe
unread,
Apr 30, 2001, 11:07:17 PM
to
On Mon, 30 Apr 2001 20:38:18 GMT, ke...@grinnell.edu (Chris Kern) drank

a fifth of Old Crow and wrote:
>On 30 Apr 2001 05:03:38 -0700, Bahman Rabii
><bah...@unmaker.house-of-toast.com> posted the following:
>
>>ke...@grinnell.edu (Chris Kern) writes:
>>
>>> Nice post. I especially like your object oriented language idea. I
>>> have toyed with the idea (and am still considering it) of making an
>>> Angband variant coded in Java. There are many advantages to this
>>> approach which would lead to some of the things you stated here.
>>
>>The Java virtual machine is at least an order of magnitude slower than
>>I would want for a *band.
>
>This is somewhat ridiculous...I can't buy that the JVM runs ten times
>slower than a C program.
>

I actually DO believe this. A magazine ran a test (admittedly about 3
years ago) and found that Visual J++ ran over 30 (THIRTY!) times
slower than Visual C++ (I remember this because it stood out in my
mind as almost unbelievable). Visual Basic 5.0 ran like a dog,
too...about 5 times slower than Visual C++. Delphi did pretty well
though, and Object Pascal is (from what I hear) a better language than
C++ for most purposes. Angband in Delphi could work...

Big Bad Joe

Stig E. Sandoe's profile photo
Stig E. Sandoe
unread,
May 1, 2001, 5:52:52 AM
to
inv...@erehwon.invalid (Graaagh the Mighty) writes:
[...]

On Death:

> 1aii and 2c seem to have tied for the best solution to this issue. For
> part of that roguelike flavor, we shall go with option 2c: there is a
> party, including one or more PCs and zero or more NPCs, and the game
> ends if you quit (including after a win) or the whole party is
> destroyed (which is a loss if you didn't in fact win first). Moreover,
> we shall (for simplicity's sake) limit to one PC in the party. If an
> NPC dies the player can lead the party to a town, where another NPC
> can be recruited (and there might be other circumstances where an NPC
> replacement *might* be obtainable). If the PC dies, the game goes on
> -- the player rolls up a new PC, who starts in some town in the same
> game world with the game state continuing to evolve, and he may
> recruit some NPCs and may manage to find (and perhaps join forces
> with) the surviving NPCs from the previous attempt. In this way, the
> game sort of goes on after a sort-of-loss, but perseverance should win
> the game eventually.

How do you picture the game-mechanics of this party-model, would you
basically play one character, or cycle through them all as in [T]?
Please feel free to elaborate.

> Where do cursed items and spoilers come in?
> 1aii allows difficulty always detecting really troublesome cursed
> items not to be a showstopper, as if worse comes to worst you can
> restore a save game. However, the setback of being returned to a
> checkpoint you hit some time ago creates a deterrent to responses like
> "Oh, it's cursed, quick-load..." and encourages finding in-game
> solutions to problems posed by cursed items. If it turns out to be a
> real pain or "game-ender" you can still reload and accept the
> setback.

One could also have these saves as infrequently as every fifth
level-gain assuming an Angband-model. It would be easier to get a
*remove-curse* than lose the last 2.5 levels.

> 2. Items, items, items.
>
> How do we make instant identify unnecessary, so people will actually
> risk wielding that unidentified long sword? Simple -- cursed items
> aren't a showstopper. How do we make cursed items a non-useless part
> of the game? Simple -- cursed items are neither perfectly detectable
> nor harmless.
>
> Cursed items should cause a setback, without being a total
> showstopper. The above solutions to death issues (e.g. making death
> nonpermanent, or permanent but not a showstopper itself) solve this
> for us.

As has been suggested on this group earlier, making several objects a
mixed curse is a good idea. In most Angband-versions cursed items are
really worthless and can be tossed, and only a very few are
double-edged, e.g Calris. Make the cursed (and the good) items have
some cool features and some bad side-effects. Most artifacts probably
have quite a few eccentricities.

> 3. Documentation and Character Knowledge. (We'll get to structure
> eventually.)

[snip good ideas basically]

Maybe someone should give Clippy a new home in Angband? :-)

> 5. Scumming/cheating.
>
> The solution to scumming is, IMO, making it not worth bothering with,
> but not by way of heavy handed game mechanics.

FAQ:

Q: Why do you autoscum?
A: Because levels would be boring otherwise

Q: Why do you townscum?
A: It's silly that they have no arrows

Q: Why do you stairscum?
A: Because I can, and when climbing/diving fast it's easier to
stairscum than search yet another huge random level for some
stair. (mostly at low lvls)


Morale:
- Make levels more fun
- Use a persistent level above and below to avoid blatant scumming,
but make normal medieval easy-to-produce items in the shop _common_.


> Persistent dungeons introduces a potential problem: item and XP
> starvation. The solution: Infinite dungeons, which are, however,
> persistent. Disk space is not an issue: the player can never explore
> more than a finite amount of it. Won't it be scummed? Getting new
> stuff from infinite dungeons will mean a form of mining: the more
> you've taken out, the deeper inside you must go to find the next nice
> item.

Sounds like a fair idea.

> Your backpack is real. It can hold a lot of things, especially smaller
> things, but watch out! Too much weight can make the bottom fall out of
> it. I'd be careful about fire too. At least it can't be stolen easily,
> although its contents might be easier to pilfer.
>
> Fortunately, you can get more backpacks, you can roll up a spare and
> put it in your original, and you might be able to find high quality
> ones...ones that are not flammable, or maybe even have magical
> abilities...

Yes :-)

> 8. Conclusion.
>
> Above is a blueprint for making a roguelike game head and shoulders
> above the rest.

Don't be alarmed if someone borrows ideas from this article. I also
suggest that you repost it to rec.games.roguelike.development. And
yes, please post more well-written pieces like this.

> Not only that, in an object oriented language it
> should be possible to design an *engine* into which the planned
> species of monster and item and place and the limits and parameters
> for constructing and deploying random ones can be plugged.

Yes.

> The one
> engine could easily support thousands of different variants, and
> multiple "campaigns" for each variant (same "world" in some sense,
> different quests/goal/new stuff/removed stuff...)

You will need to add some constraint for such an engine, but such an
engine is the path chosen by Langband[*] which is written in an
object-oriented language. Currently I am working on the engine, and I
have a plugin which emulates Vanilla Angband. It will need some time
still for completion though.


[*] http://langband.sourceforge.net/


--
------------------------------------------------------------------
Stig Erik Sandoe st...@ii.uib.no http://www.ii.uib.no/~stig/

Braeus's profile photo
Braeus
unread,
May 1, 2001, 6:34:33 AM
to

"Graaagh the Mighty" <inv...@erehwon.invalid> wrote in message
news:3aedcb92....@news.primus.ca...

> On 30 Apr 2001 05:03:38 -0700, Bahman Rabii
> <bah...@unmaker.house-of-toast.com> sat on a tribble, which squeaked:
>
> >ke...@grinnell.edu (Chris Kern) writes:
> >
> >> Nice post. I especially like your object oriented language idea. I
> >> have toyed with the idea (and am still considering it) of making an
> >> Angband variant coded in Java. There are many advantages to this
> >> approach which would lead to some of the things you stated here.
> >
> >The Java virtual machine is at least an order of magnitude slower than
> >I would want for a *band.
>
> I disagree. On any machine that runs Java at all (32 bit architecture
> being a *bare* minimum, and possibly not sufficient in and of itself)
> Java would run fast enough without any (JIT or otherwise) compiling
> for a turn-based game. A few optimization tricks would be needed but I
> have tons of these up my sleeve:
> <SNIP!>
Java is evil. Python is not.

I think Python is the obvious choice for this.


-----= Posted via Newsfeeds.Com, Uncensored Usenet News =-----
http://www.newsfeeds.com - The #1 Newsgroup Service in the World!
-----== Over 80,000 Newsgroups - 16 Different Servers! =-----

James Andrewartha's profile photo
James Andrewartha
unread,
May 1, 2001, 8:58:30 AM
to
What about the system used by MAngband? When you die, you become a ghost, and
drop all your equipment. However, you can move though walls, and float up or
down between levels without stairs. When you go back to the town level, you
can restore yourself by going to the temple, but you lose half your XP. Note
that you can stay on the level and have someone else come down and get your
equipment for you and take it back to town, but this is not always possible
(possibly in the system Graaagh is describing, an NPC could do it). You can
also get your "spare" euqipment stored in your home, stored there for this
possibility.

However, this was introduced because [M] is multiplayer, and dying lots sucks
in that environment. IMHO, permanent death is an essential feature of any
roguelike (potions of invulnerability etc. excluded).

--
"There's nobody getting rich | TRS-80
writing software that I | Email: trs80(a)tartarus.uwa.edu.au
know of" - Bill Gates, 1980 | Web: http://trs80.ucc.asn.au/

David Thornley's profile photo
David Thornley
unread,
May 1, 2001, 12:22:30 PM
to
In article <3aed8d92$0$12248$ed9e...@reading.news.pipex.net>,

Matt Thrower <REMOVETHISSPAMPROTE...@cramersystems.com> wrote:
>
>This is to make death non-permanent, but to impose some kind of penalty on
>the player which is catastrophic enough to serioulsy impact gameplay and
>therefore make death very unpleasent but which is, unlitmately,
In Cthangband, if you have a lot of money (IIRC, something like
700,000 GP), you can have a magic shop do a Ritual of Recall for you.
If you are then killed, you instead appear in the shop fully healed,
naked, and broke. (The prudent will have extra kit in a house in
town, and likely stuff to sell.) To me, it feels too much like
cheating to make it worthwhile for me to do it. Other people may
feel differently. (Since it is a part of the game, it isn't
cheating, and should be used by anybody who wants to and has the
cash.)

--
David H. Thornley | If you want my opinion, ask.
da...@thornley.net | If you don't, flee.
http://www.thornley.net/~thornley/david/ | O-

David Thornley's profile photo
David Thornley
unread,
May 1, 2001, 12:26:52 PM
to
In article <3aeda6e6...@enews.newsguy.com>,
There is an Angband variant being coded in an object-oriented language.
I refer of course to Common Lisp and Langband. Unfortunately, good
Lisp compilers are more rare than good C compilers. CMUCL works
well on the more common versions of Unix, but the good compilers on
Windows and the Mac are fairly expensive and don't necessarily
include redistribution licenses.
Timo Pietilä's profile photo
Timo Pietilä
unread,
May 1, 2001, 5:49:35 PM
to
> Angband TSI IIER HLVClCtRR15 ND E16 NS17 RSSZFGA
> W18
Angband TSI IE TLVClCtRR SD R SM ZGA

I didn't get same result.

Timo Pietilä

--
A(2.9.2) C "Wanderer" DP L:17 DL:300' A-- R--- Sp w:LxBow(+4,+9)
A/Gu L/W/D H+ D c-- f PV+ s-(+) TT- d(+) P++ M+
C-- S+ I-(++) So+ B++ ac GHB- SQ RQ++ V+ F:Z Rod Stacking

William Tanksley's profile photo
William Tanksley
unread,
May 1, 2001, 6:47:16 PM
to
Check out the roguelike "UnReal World", based on Finnish myths. Very
impressive.

http://www.mo.himolde.no/~knan/roguelike/49.html
http://www.hut.fi/~eye/roguelike/misc.html

(That reminds me -- runeinga, please check out this and Ragnarok, on the
same page. Both are very nice, although neither one is directly what you
want. Ragnarok is now freeware.)

IMO, making shops "realistic" isn't as good an idea as it sounds, unless
you know EXACTLY how you intend to allow people to use the shops,
including all possible abuses. It's just too complicated; games shouldn't
have complication for its own sake.

>Matthias

--
-William "Billy" Tanksley

Joseph Oberlander's profile photo
Joseph Oberlander
unread,
May 1, 2001, 6:53:38 PM
to
> > T -- indicates survival tactics require teleportation capabilities and
> > massive detection capabilities.
> > (Undesirable because it is bad roleplay, removes some strategic
> > elements one could otherwise have, and virtually forces the use
> > of heavy-handed game mechanics around vaults, special levels,
> > &c -- also, the need for massive detection leads to the
> > availability of massive detection, which then erases the element
> > of surprise or at least vastly reduces it!).
Desireable. In RL, if I go to the wrong side of town and make trouble, I
will be in situations where I am way over my head. Retreat is an option,
and in Angband, nothing requires that you kill anything unless you decide
to wake it up/get to close or attack it.

> > I -- indicates temporary invulnerability is available in the game.
> > (Neutral, but undesirable if too common.)

GoI needs to be made to not work at all against H-H damage(magical attacks
and such are blocked)

> > R -- A weird and questionable mechanism is needed to access stuff
> > saved somewhere, some locations, or such in reasonable time (e.g.
> > *band's Word of Recall). (Undesirable -- bad role-play.)

I think this is great and necessarry.

> > T -- indicates themed areas, with certain monsters/items more likely,
> > and/or in-character drops for monsters. (Desirable. Games with
> > too little spatial structure, e.g. vanilla Angband, are less
> > interesting and must rely on temporal structure too heavily to
> > avoid actually being boring.)

Themed games can also be seen as a give-away/pattern game. Very easy to
slide down the slope to PSX type games where it is scripted.

> > B -- indicates "bad" quests (e.g. random monsters and other stuff that
> > doesn't make very much sense). (Undesirable: bad roleplay.)

Life is random. I personally LOVE random quests.

> > W -- indicates a wilderness. (Desirable.)

Fluff. Scummable. Not desireable as it detracts from the overall continuity.
(you can play Angband sans wilderness just fine)


> > E -- Game has secrets/Easter eggs. (Desirable.)

Nope. Very very undesireable. Playing too much Nintendo. What makes
Angband truly great is that there is no "powerup behind door 4 on level.."
nonsense.

> > DDD -- indicates that the game has excellent documentation and
> > moreover this is presented "in-game" in role-played fashion to
> > the greatest extent possible -- i.e. the outside-the-game-world
> > manuals only explain getting started, character generation, the
> > program's interface, and other elements not themselves part of
> > the role playing proper. (Desirable -- "learn as you go along"
> > is very good role-playing so long as it isn't slow and
> > frustrating trial-and-error exclusively!)

Again, too much gaming consoles. RTM, folks.

> > U -- indicates that unfair (i.e. difficult to avoid *and* difficult to
> > recover from) events can occur in any stage of the game.
> > Unavoidable deaths are the most common unfair event.
> > (Undesirable.)

Angband has none of these with the speed-fix-patch. Very fair and there
is *always* a way to get out of there or avoid a stupid situation like
casting Phase-Door near a half-empty vault of Dragons(DUH!)

> > Scumming column:
> > N -- indicates that the game designers responded to players abusing
> > scummable features (e.g. stat potions) by making the scumming
> > *necessary* (e.g. the leap in monster nastiness in Angband at
> > 2000'). (Undesirable.)

Scunning is not necessarry. IMan chracters can win, afterall.

> > T -- indicates that the game designers limited scumming by creating
> > time or progression limitations of some kind, e.g. finitely many
> > monsters/items generated whole game, time limit, move limit,
> > inability to save the game, or similar. (Undesirable.)
> > U -- indicates that the game designers used something really evil and
> > unfair to limit some form of scumming, making it exceedingly
> > dangerous, but with unfair side effects for "legit" characters.
> > (Undesirable.)
> > S -- indicates that the game designers limited scumming by rendering
> > it both unnecessary and either undesirable past a point or
> > impossible without using any of the above methods. (Desirable.)
> > M -- indicates that unlimited scumming can create munchkins.

My half-preserve model would fix almost all of this nonsense.

> > S -- Starting a new character, it is well-nigh necessary to scum for
> > high starting stats or something similar. (Undesirable.)

Point-based half-maximize(my idea) would fix this if combined with
3E norms for stat increases.(this REALLY should be done)

> > SS -- The game actually has built-in features to assist in automated
> > scumming for high starting stats or whatever. (Undesirable.)

Bye-bye with the above proposal. You have a finite amount of points
to allocate, and since things are rounded down(avg 10 - 60 points to
distribute+racial bonuses)), you will always be short as racial minimims
also have to be paid for out of that.

> > Z -- Endgame characters of the same race and class don't have much to
> > distinguish them. (Neutral or undesirable.)

Fixed with half-maximize.

> > F -- indicates that every class plays like a fighter, possibly with
> > spell support. (Undesirable: bad roleplay, *unless* the game only
> > has classes that should properly be warriors.)

Fixed by moving the last three 4th-book spells to a special book and
moving soe of the Raals spells to the 4th. Easy access at decent levels to
Raal's spells would solve most of the midgame power-crisis.

(the last 3 spells are to powerful, IMO, for the 4th book)

> > G -- Game has a glut of artifacts. (Undesirable: artifacts should be
> > rare and special. It's bad role play otherwise.)

Angband has a good balance, IMO. The random generation routine for them
though, needs to be SERIOUSLY rebalanced. Items should not have every
resist, for instance.

> > M -- Some minor task requires inordinate amounts of the player's
> > attention, e.g. avoiding starvation or repairing stat drains a
> > lot. (Undesirable, even if realistic, because *boring*.)

Add an amulet of Sustenance or make Hold Life stop you from needing food.

> > A -- Asymmetrical game mechanics or just plain asymmetrical powers
> > make monsters very different from the player in e.g. hit points.
> > (Necessary to some extent if the player is to survive, but
> > undesirable past a certain point.)

Like fixing the Draco-lich/lisk nonsence?
Dracolisk is a half-dragon half-basilisk! Super Umber-Hulks.

DracoLich is a Dragon that turned itself into a Lich!
Ouch-and-a-half! These things should be the most powerful
non unique dragon in the game, period, and very deep.
All dragon and Lich powers rolled into one.

Chris Kern's profile photo
Chris Kern
unread,
May 1, 2001, 8:15:48 PM
to
On Tue, 01 May 2001 15:53:38 -0700, Joseph Oberlander
<ober...@pacbell.net> posted the following:
>Fluff. Scummable.

There's nothing inherent in a wilderness idea that makes it fluff or
scummable. Just because Z's old wilderness was like that doesn't mean
it has to be that way.

>Again, too much gaming consoles. RTM, folks.

I think that you and Neo are talking somewhat at cross purposes. Neo
wants an RPG-oriented roguelike (which Angband is not really), but you
seem content with the tactical orientation of Angband as it is now.

>Scunning is not necessarry.

I disagree. If you have an extreme amount of patience this is true,
but for most people, you cannot get the equipment necessary to win the
game without some scumming.

> IMan chracters can win, afterall.

Not in V.

>Angband has a good balance, IMO.

The biggest problem with Angband's artifacts is that over half of them
are totally worthless.

> > A -- Asymmetrical game mechanics or just plain asymmetrical powers
> > make monsters very different from the player in e.g. hit points.
> > (Necessary to some extent if the player is to survive, but
> > undesirable past a certain point.)

>Like fixing the Draco-lich/lisk nonsence?
>Dracolisk is a half-dragon half-basilisk! Super Umber-Hulks.

>DracoLich is a Dragon that turned itself into a Lich!
> Ouch-and-a-half! These things should be the most powerful
> non unique dragon in the game, period, and very deep.
> All dragon and Lich powers rolled into one.

No, I think Neo meant that monsters can have tens of thousands of HP
whereas the player can only reach a little over 1000 (as an example).

-Chris

Joseph Oberlander's profile photo
Joseph Oberlander
unread,
May 1, 2001, 11:06:10 PM
to
Chris Kern wrote:
>
> On Tue, 01 May 2001 15:53:38 -0700, Joseph Oberlander
> <ober...@pacbell.net> posted the following:
>
> >Fluff. Scummable.
>
> There's nothing inherent in a wilderness idea that makes it fluff or
> scummable. Just because Z's old wilderness was like that doesn't mean
> it has to be that way.
Unless it is one huge map it is scummable by popping on and off the edges.
Arena levels also suffer from this to a certian extent.



> >Again, too much gaming consoles. RTM, folks.
>
> I think that you and Neo are talking somewhat at cross purposes. Neo
> wants an RPG-oriented roguelike (which Angband is not really), but you
> seem content with the tactical orientation of Angband as it is now.

Yes. It is wonderfully refreshing to have a game that is anything but
Zelda XVIII. Evidently he thinks it should be more like that.

> >Scumming is not necessarry.


>
> I disagree. If you have an extreme amount of patience this is true,
> but for most people, you cannot get the equipment necessary to win the
> game without some scumming.

Most of the items that you scum for can be easily dealt with by
making those properties part of certain artifacts.

> > IMan chracters can win, afterall.
>
> Not in V.

Absolutely. Been done. OTOH, I'm not Lev ;)



> >Angband has a good balance, IMO.
>
> The biggest problem with Angband's artifacts is that over half of them
> are totally worthless.

Overall it does far far better than anything else on the market, IMO.



> > > A -- Asymmetrical game mechanics or just plain asymmetrical powers
> > > make monsters very different from the player in e.g. hit points.
> > > (Necessary to some extent if the player is to survive, but
> > > undesirable past a certain point.)
>
> >Like fixing the Draco-lich/lisk nonsence?
> >Dracolisk is a half-dragon half-basilisk! Super Umber-Hulks.
>
> >DracoLich is a Dragon that turned itself into a Lich!
> > Ouch-and-a-half! These things should be the most powerful
> > non unique dragon in the game, period, and very deep.
> > All dragon and Lich powers rolled into one.
>
> No, I think Neo meant that monsters can have tens of thousands of HP
> whereas the player can only reach a little over 1000 (as an example).

But they don't carry items(and wield them) nor do they have the
AI or spells to compete, so something has to be doen to make them uglier.

Chris Kern's profile photo
Chris Kern
unread,
May 2, 2001, 12:29:02 AM
to
On Tue, 01 May 2001 20:06:10 -0700, Joseph Oberlander
<ober...@pacbell.net> posted the following:
>Chris Kern wrote:
>>
>> On Tue, 01 May 2001 15:53:38 -0700, Joseph Oberlander
>> <ober...@pacbell.net> posted the following:
>>
>> >Fluff. Scummable.
>>
>> There's nothing inherent in a wilderness idea that makes it fluff or
>> scummable. Just because Z's old wilderness was like that doesn't mean
>> it has to be that way.
>
>Unless it is one huge map it is scummable by popping on and off the edges.
>Arena levels also suffer from this to a certian extent.

There could be ways around this, like saving the monsters and letting
them wander between map panels. A properly designed wilderness can
add a lot to the game.

>> >Again, too much gaming consoles. RTM, folks.
>>
>> I think that you and Neo are talking somewhat at cross purposes. Neo
>> wants an RPG-oriented roguelike (which Angband is not really), but you
>> seem content with the tactical orientation of Angband as it is now.
>
>Yes. It is wonderfully refreshing to have a game that is anything but
>Zelda XVIII. Evidently he thinks it should be more like that.

His post was sort of off-topic for this group, but he was talking
about a new roguelike, not another Angband. However, it is nice to
have some secrets in a game. If *identify* was not so hard to get in
Angband I would try to play more without spoilers. Then maybe
artifact finds would be exciting :)

I should probably play with randarts. That would stop the "oh I found
Dor Lomin so I will never identify any more helms" situations.

>> >Scumming is not necessarry.
>>
>> I disagree. If you have an extreme amount of patience this is true,
>> but for most people, you cannot get the equipment necessary to win the
>> game without some scumming.
>
>Most of the items that you scum for can be easily dealt with by
>making those properties part of certain artifacts.

Perhaps. It's mostly Word of Recall, stat restore, and restore life
levels that must be scummed. I think there should be a medical
building in town that can heal stats and RLL, and WoR should be in
shop 4. But I've been saying these since 2.8.3 :-)

>> > IMan chracters can win, afterall.
>>
>> Not in V.
>
>Absolutely. Been done. OTOH, I'm not Lev ;)

I don't think it has. Are you sure you're not thinking of a Z ironman
win?



>> >Angband has a good balance, IMO.
>>
>> The biggest problem with Angband's artifacts is that over half of them
>> are totally worthless.
>
>Overall it does far far better than anything else on the market, IMO.

Could be much better, though.


>> > > A -- Asymmetrical game mechanics or just plain asymmetrical powers
>> > > make monsters very different from the player in e.g. hit points.
>> > > (Necessary to some extent if the player is to survive, but
>> > > undesirable past a certain point.)
>>
>> >Like fixing the Draco-lich/lisk nonsence?
>> >Dracolisk is a half-dragon half-basilisk! Super Umber-Hulks.
>>
>> >DracoLich is a Dragon that turned itself into a Lich!
>> > Ouch-and-a-half! These things should be the most powerful
>> > non unique dragon in the game, period, and very deep.
>> > All dragon and Lich powers rolled into one.
>>
>> No, I think Neo meant that monsters can have tens of thousands of HP
>> whereas the player can only reach a little over 1000 (as an example).
>
>But they don't carry items(and wield them) nor do they have the
>AI or spells to compete, so something has to be doen to make them uglier.

It's a necessity because of the game design, but you could make a game
where the monsters did not have to possess these compensating factors.

-Chris

Joseph Oberlander's profile photo
Joseph Oberlander
unread,
May 2, 2001, 4:37:07 AM
to
> >Unless it is one huge map it is scummable by popping on and off the edges.
> >Arena levels also suffer from this to a certian extent.
>
> There could be ways around this, like saving the monsters and letting
> them wander between map panels. A properly designed wilderness can
> add a lot to the game.
My preserve option would also work, since the wilderness state is also
generated off of a seed. Just make 20-50 seeds, one for each sector,
and save what is where when you leave. Erase the creatures when you move
more than 3 grids away.(and regenerate monsters only when you come back)

> >> >Again, too much gaming consoles. RTM, folks.
> >>
> >> I think that you and Neo are talking somewhat at cross purposes. Neo
> >> wants an RPG-oriented roguelike (which Angband is not really), but you
> >> seem content with the tactical orientation of Angband as it is now.
> >
> >Yes. It is wonderfully refreshing to have a game that is anything but
> >Zelda XVIII. Evidently he thinks it should be more like that.
>
> His post was sort of off-topic for this group, but he was talking
> about a new roguelike, not another Angband. However, it is nice to
> have some secrets in a game. If *identify* was not so hard to get in
> Angband I would try to play more without spoilers. Then maybe
> artifact finds would be exciting :)

Make it the same price, but for sale in the magic shop(#5)
Solves the problem.

> I should probably play with randarts. That would stop the "oh I found
> Dor Lomin so I will never identify any more helms" situations.

Randarts are nice, actually. OTOH, some version have *ID* as a high-level
spell.



> >> >Scumming is not necessarry.
> >>
> >> I disagree. If you have an extreme amount of patience this is true,
> >> but for most people, you cannot get the equipment necessary to win the
> >> game without some scumming.
> >
> >Most of the items that you scum for can be easily dealt with by
> >making those properties part of certain artifacts.
>
> Perhaps. It's mostly Word of Recall, stat restore, and restore life
> levels that must be scummed. I think there should be a medical
> building in town that can heal stats and RLL, and WoR should be in
> shop 4. But I've been saying these since 2.8.3 :-)

Sure. Makes sense. OTOH, activation for WoR or Restore Life
would be ultra-cool for certain artifacts.



> >> > IMan chracters can win, afterall.
> >>
> >> Not in V.
> >
> >Absolutely. Been done. OTOH, I'm not Lev ;)
>
> I don't think it has. Are you sure you're not thinking of a Z ironman
> win?

Nope. Vanilla - strict ironman. A few times, in fact. They just dove
very very slowly and did not take every down stari they saw(no Kamakazi
mode)



> >> >Angband has a good balance, IMO.
> >>
> >> The biggest problem with Angband's artifacts is that over half of them
> >> are totally worthless.
> >
> >Overall it does far far better than anything else on the market, IMO.
>
> Could be much better, though.

Sure, but since it is in developmetn, it gets better and better - not
like say Diablo, which got shelved after a year. Bugs remain and well -
tough - tey have moved on.



> >> > > A -- Asymmetrical game mechanics or just plain asymmetrical powers
> >> > > make monsters very different from the player in e.g. hit points.
> >> > > (Necessary to some extent if the player is to survive, but
> >> > > undesirable past a certain point.)
> >>
> >> >Like fixing the Draco-lich/lisk nonsence?
> >> >Dracolisk is a half-dragon half-basilisk! Super Umber-Hulks.
> >>
> >> >DracoLich is a Dragon that turned itself into a Lich!
> >> > Ouch-and-a-half! These things should be the most powerful
> >> > non unique dragon in the game, period, and very deep.
> >> > All dragon and Lich powers rolled into one.
> >>
> >> No, I think Neo meant that monsters can have tens of thousands of HP
> >> whereas the player can only reach a little over 1000 (as an example).
> >
> >But they don't carry items(and wield them) nor do they have the
> >AI or spells to compete, so something has to be doen to make them uglier.
>
> It's a necessity because of the game design, but you could make a game
> where the monsters did not have to possess these compensating factors.

Sure - I guess so, but the fact is, a huge Dragon(tm) will always have more HP
and raw damage per round than a puny Elf. You need those heals and speed
in almost every piece of literature(or great luck and cunning)

Timo Pietilä's profile photo
Timo Pietilä
unread,
May 2, 2001, 5:03:36 AM
to
Chris Kern wrote:

> >> > IMan chracters can win, afterall.
> >>
> >> Not in V.
> >
> >Absolutely. Been done. OTOH, I'm not Lev ;)
>
> I don't think it has. Are you sure you're not thinking of a Z ironman
> win?

Can be done and has been done. That of course depends of type of
ironman. If you play "dive as soon as you see downstairs" then it is
impossible, but if you play just regular from-to-top ironman that can
stay on single level as long as he wishes it can be done without
artifacts even. Artifactless, bookless from-to-top hobbit ranger is
completely winnable ironman game. Hard, but doable.

Timo Pietilä

--
A(2.9.2) C "Wanderer" DP L:17 DL:350' A-- R--- Sp w:LxBow(+6,+9)

Windsor Williams's profile photo
Windsor Williams
unread,
May 2, 2001, 6:17:24 AM
to
thor...@visi.com (David Thornley) wrote in
<apBH6.21539$9f2.1...@ruti.visi.com>:
>In article <3aed8d92$0$12248$ed9e...@reading.news.pipex.net>,
>Matt Thrower <REMOVETHISSPAMPROTE...@cramersystems.com>
>wrote:
>>
>>This is to make death non-permanent, but to impose some kind of penalty
>>on the player which is catastrophic enough to serioulsy impact gameplay
>>and therefore make death very unpleasent but which is, unlitmately,
>
>In Cthangband, if you have a lot of money (IIRC, something like
>700,000 GP), you can have a magic shop do a Ritual of Recall for you.
>If you are then killed, you instead appear in the shop fully healed,
>naked, and broke. (The prudent will have extra kit in a house in
>town, and likely stuff to sell.) To me, it feels too much like
>cheating to make it worthwhile for me to do it. Other people may
>feel differently. (Since it is a part of the game, it isn't
>cheating, and should be used by anybody who wants to and has the
>cash.)

I _really_ like this idea. One problem with Angband (and I'm sure
plenty of people will tell me it isn't a problem, it's the whole
point of the game) is that you can invest a lot of time in building
a character, and then lose him or her to a situation beyond your
control. Yes, even if you do everything "right" sometimes you get
killed. Being able to buy "insurance" (which is effectively what it
is) against this would help greatly, and if you make the insurance
expensive enough, it won't be a free pass for stupid/less-than-
careful gameplay.

What I think would make sense would be to scale the cost to the
character's level. Recalling/resurrecting an average person (your
randomly generated 1st level character, say) would be expensive
enough, but bringing back a powerful mage/priest/hero from the dead
should be _amazingly_ expensive. An additional expense factor for
the various races would work nicely, too, as a way of balancing out
some of the more advantageous races (Dunedain, High Elves) a little
more.

Another nice effect is that this would actually give higher-level
characters something to do with all that money. Picture a 48th-level
character who actually _cares_ about money, and needs another few
hundred thousand -- wouldn't it be a nice change from the standard
"money has been useless since statgain (and mostly useless even
before that)" mindset?

For the purists, the character's record should definitely include
the number of times he or she has been brought back. Note that I'm
thinking this number would be along the lines of 2, or perhaps 3 at
the outside (although I can picture a borg player with 4 or 5).
We're talking an expensive-but-achievable amount of money, to give
the player a little safety against those "did everything right and
still died" situations.

Windsor

James WWW Wilson's profile photo
James WWW Wilson
unread,
May 2, 2001, 1:16:07 PM
to
Stig E. Sandoe <st...@ii.uib.no> said:
>Morale:
>- Make levels more fun
>- Use a persistent level above and below to avoid blatant scumming,
> but make normal medieval easy-to-produce items in the shop _common_.
Yes, as something like Phase Door is such a staple of dungeoneers I
think it should always be available. Restore stats should be available
in town all the time, but maybe not in potion form, I mean that you
cannot get something to take into the dungeon to restore stats, all the
time.
--
James
THE HUMPTY DANCE IS YOUR CHANCE TO DO THE HUMP!

Matthew K Lahut's profile photo
Matthew K Lahut
unread,
May 2, 2001, 6:37:30 PM
to
I feel like I should contribute to some of the observations you made. You
make a lot of important points, but another crucial one is that you simply
cannot please all people all the time.
Each roguelike has its own strengths and weaknesses, and it's impossible
to be aware of all of them. There are also some larger issues that have
been debated before, and may be debated again before all is said and done.

Personally, the fun I get from roguelikes is the sense of having "beaten
the system". Accordingly, I feel no guilt about reading any and all
spoilers for them, even adding to them if I feel it is necessary. Know
thine enemy, as they say. I really hate YASDs resulting from "If I had
only known this ahead of time..."

I also enjoy the various voluntary challenges that roguelikes offer
(though I must admit, this is probably not a consideration for writing
another one.) The challenge must be documented somehow, though. Angband
accomplishes this with birth options, Nethack with #conduct. Adom has no
organized set of conducts like this, but several (cats, praying,
weapon-related) can be discerned from the game-end output.

Generally I don't worry too much about scumming concerns; I feel that any
scumming technique is balanced by the incurred boredom. If a scumming
trick is too easy for the reward (Adom's casino or Nethack's foocubi, for
instance), then I consider it part of the game and not to be frowned upon.
This is why I've never attempted an Angband Ironman; IMHO it would take
ages of mindless wandering on the same level to generate enough creatures
to drop necessary equipment.

I'll try to correct (what I consider) misconceptions that you may have
about the first section, evaluation of other games. You may find an
interesting idea that you had missed in your classifications.

On Mon, 30 Apr 2001, Graaagh the Mighty wrote:

> Key:

> Items column:
> I -- Easy to identify stuff/detect bad stuff/whatever, and necessary.
> (Undesirable -- takes some of the fun out of the game!)

I agree with your assessment here... especially in Angband, identification
becomes a simple and tedious chore as soon as you have a reasonable
income.

> C -- Hard to identify stuff and easy to wind up with a
> nearly-unplayable (or even actually unwinnable) game (or get
> killed) due to cursed stuff or lost items. (Can be combined with
> I or II; e.g. ADOM has CI because in the early game C holds true
> and in the late game I holds true.

I'm not sure what you're getting at here. This is one of the challenges of
nearly every roguelike... find out what all your stuff does. It's one of
the things that makes roguelikes hard. You learn effects of various items
by playing again, and learning how to identify things more efficiently the
hard way.

> E -- Cursed stuff is not a threat, either because it is easily
> detected and avoided, easily removed, or just not that bad.
> (Mutually exclusive with C.) (Undesirable -- useless gameplay
> elements are in general undesirable.)

This feature is essentially identical to II.

> R -- A weird and questionable mechanism is needed to access stuff
> saved somewhere, some locations, or such in reasonable time (e.g.
> *band's Word of Recall). (Undesirable -- bad role-play.)

So you don't like Word of Recall, fine. That's your opinion. I think
they're necessary in Angband to avoid boredom. Can you give an example of
another roguelike feature that fits this criteria?

> Z -- Saved stuff is prone to destruction, or stuff can't be saved.
> (Undesirable usually -- stuff is usually necessary -- symbol
> omitted if saving stuff isn't vital or at least highly
> desirable.)

Here you open the argument of limited inventory. Every roguelike has this
to some extent. Adom doesn't really have this attribute; use the
barbarian's glade.

> Structure column:


> B -- indicates "bad" quests (e.g. random monsters and other stuff that
> doesn't make very much sense). (Undesirable: bad roleplay.)

Other than *band-variant-style "joke" monsters, could you give some
examples of this?

> H -- indicates heavy-handed game mechanics are used. (Undesirable.)
> HH -- indicates heavy-handed game mechanics are used extensively.
> (Undesirable.)

You have H or HH included in each roguelike in your chart. It seems to be
a pretty fundamental concept. What do you consider to be too
heavy-handed? The term seems vague to me.

> W -- indicates a wilderness. (Desirable.)

Again, tastes vary. Many games work fine without a wilderness, and would
be harmed by the insertion of one.

> Spoilers/documentation column:
> N -- indicates that reading spoily information is pretty much
> necessary to win the game. (Undesirable.)

Another item that you have included in each roguelike in your chart (And
it's pretty true for Nethack, too.) This isn't always true, there's always
*someone* who has finished the game without spoilers, though they are
usually pretty rare.

> S -- indicates that reading spoily information is discouraged.
> (Neutral.)

Depends on who's doing the discouraging. I've already said my views on
roguelike spoilers. I only read spoilers for games that already have great
replay value, such as roguelikes; for me, they enhance the replay value
and I have more fun with the game. For games I only expect to play
through once, such as single-player FPS (Thief, Deus Ex, etc.), or console
RPGs (Zelda, Final Fantasy <foo>) I will only read spoilers if I am
otherwise stuck.

> D -- indicates that the game has documentation. (Desirable.)
> DD -- indicates that the game has excellent documentation.
> (Desirable.)


> DDD -- indicates that the game has excellent documentation and
> moreover this is presented "in-game" in role-played fashion to
> the greatest extent possible -- i.e. the outside-the-game-world
> manuals only explain getting started, character generation, the
> program's interface, and other elements not themselves part of
> the role playing proper. (Desirable -- "learn as you go along"
> is very good role-playing so long as it isn't slow and
> frustrating trial-and-error exclusively!)

Debatable. If I was playing a roguelike that always gave me the same
hints, I'd find it annoying. Nethack and Adom both have a decent
implementation of this (the Oracle and Mad Minstrel, respectively).

If you've never tried it, consider downloading Avernum
(www.spidweb.com). Although it is a one-campaign RPG, its documentation
system is well done, giving appropriate help when new things are first
encountered. It also has some excellent features that you may be
interested in adding to your project.

> C -- indicates that the game designers closed the source code.
> (Undesirable.)

A matter of opinion, certainly. This will have a *major* effect on spoiler
availability. If you're writing this new game yourself, your views on this
may change over the development process.

> Fairness column:
> (snip)
Personally, I like it when nearly *any* event, good or bad, has a
miniscule chance of happening. You say that early deaths are unfair. What
about characters that find two artifacts before dlvl 4? Is that unfair
too? Don't be overly nice to your players by "trying to be fair" to
low-level characters; that's part of the fun. If bad luck never happened,
the good luck wouldn't feel as good.

> Miscellaneous column:
> T -- slow and tedious to start a new character. (Undesirable,
> especially in combination with 'E' or 'U' in fairness column.)

I see how this is true for paper RPGs, but why Moria and *band variants?

> R -- you have to be a rocket scientist to start a new character.
> (Undesirable -- basicaly you'll be messing with zillions of
> options and poring over documentation. Or dying a lot. Or both.)

I disagree, at least as far as Angband and friends go. It's part of the
learning process to see which characters you're good with, and what
starting attributes are useful.

> S -- Starting a new character, it is well-nigh necessary to scum for
> high starting stats or something similar. (Undesirable.)

> SS -- The game actually has built-in features to assist in automated
> scumming for high starting stats or whatever. (Undesirable.)

Agreed.

> P -- Polymorphing or other random and unpredictable elements make the
> game chaotic and reduce its structure.
> (Can be combined with Z, when endgame characters are all alike in
> that they all polymorph a lot or whatever and play similarly
> regardless.) (Undesirable.)

I completely disagree. IMHO Nethack's polymorph system is one of its
great strengths. Though it creates problems for some characters, it
provides solutions to others. This fits in with my earlier statement about
liking that any event has a non-zero chance of occurring.

> F -- indicates that every class plays like a fighter, possibly with
> spell support. (Undesirable: bad roleplay, *unless* the game only
> has classes that should properly be warriors.)

This is true of *many* games, and I agree that it's undesirable. I believe
that it is partially the fault of the interface. Suppose Angband could be
configured so that the default action for a mage, when moving toward a
monster, was to magic missile rather than melee attack? How would that
change things?

> G -- Game has a glut of artifacts. (Undesirable: artifacts should be
> rare and special. It's bad role play otherwise.)

This is why I don't play Angband as much as I used to; with my best
character, I throw out three out of every four artifacts I stumble across.
The treasure filtering gets annoying when there are such stockpiles of
mostly-lousy treasure (i.e. dragon drops).

> M -- Some minor task requires inordinate amounts of the player's
> attention, e.g. avoiding starvation or repairing stat drains a
> lot. (Undesirable, even if realistic, because *boring*.)

You would probably consider this an attribute of Nethack too.
Other people have criticized Angband's system for not making food
important enough; it's a renewable resource that just occupies one
inventory slot all the time.

> W -- Weird game mechanics. (Undesirable -- catch-all for weird,
> unrealistic or bad roleplay game mechanics not covered above.)

Don't call it this. Specify what weirdness you like or dislike. (Which, in
most cases, you did later.)

> (chart snipped)
> (footnotes snipped, resisting temptation to defend the individual games
> I like)

- Matt



Kieron Dunbar's profile photo
Kieron Dunbar
unread,
May 3, 2001, 7:12:18 AM
to
Once upon a time, Braeus wrote thus:
> Java is evil. Python is not.

I don't know about Java, but Python is completely amoral. It would destroy 90%
of life on earth without a second thought. And you suggest we use it in
Roguelike creation?

kwaheri, Kieron (reverse username to reply)

Kieron Dunbar's profile photo
Kieron Dunbar
unread,
May 3, 2001, 7:13:50 AM
to
Once upon a time, Timo Pietilä wrote thus:
> Graaagh the Mighty wrote:
>> R -- A weird and questionable mechanism is needed to access stuff
>> saved somewhere, some locations, or such in reasonable time (e.g.
>> *band's Word of Recall). (Undesirable -- bad role-play.)

>> Game |Life|Item|Structure |Docs |Fair|Scumming|Misc

>> Angband TSI IIER HLVClCtRR15 ND E16 NS17 RSSZFGA

> Angband TSI IE TLVClCtRR SD R SM ZGA

> I didn't get same result.

Did they look like objective criteria to you, then? The above gives me some
idea of Neo's views about the way the town and dungeon work, but whether a
mechanism is weird or questionable is entirely in the eye of the beholder.

Personally speaking, I don't tend to see roguelikes in terms of role-playing,
so I'd just say it works as a game mechnism and leave it at that.

The fact that you have different views about whether Angband fulfils several
of the criteria mentioned just tells me that you aren't Neo. Which doesn't
come as too much of a surprise to me.

Timo Pietilä's profile photo
Timo Pietilä
unread,
May 3, 2001, 7:23:50 AM
to
Kieron Dunbar wrote:
>
> Once upon a time, Timo Pietilä wrote thus:
> > Graaagh the Mighty wrote:

> >> Game |Life|Item|Structure |Docs |Fair|Scumming|Misc
>
> >> Angband TSI IIER HLVClCtRR15 ND E16 NS17 RSSZFGA
> > Angband TSI IE TLVClCtRR SD R SM ZGA
>
> > I didn't get same result.

> Personally speaking, I don't tend to see roguelikes in terms of role-playing,


> so I'd just say it works as a game mechnism and leave it at that.

Same here.

> The fact that you have different views about whether Angband fulfils several
> of the criteria mentioned just tells me that you aren't Neo. Which doesn't
> come as too much of a surprise to me.

That was my point. Every player gets different results in that table. It
isn't clear if something is good or not. Or if something doesn't belong
to roguelike or not. Roguelikes are IMHO not RPG:s and so they should
not be classified using table for RPG:s.

Timo Pietilä

--

A(2.9.2) C "Wanderer" DP L:17 DL:350' A-- R--- Sp w:LxBow(+6,+9)

Graaagh the Mighty's profile photo
Graaagh the Mighty
unread,
May 3, 2001, 9:36:14 PM
to
On Wed, 02 May 2001 00:49:35 +0300, Timo =?iso-8859-1?Q?Pietil=E4?=
<timo.p...@helsinki.fi> sat on a tribble, which squeaked:
II -- greater identify is available in spades,
once you get past a certain point.
R -- Ever zapped a rod of recall?
H -- Magic stairs only appear when you kill
Sauron? No like key and door or
anything? say what? ...
T -- umm, Angband has no real spatial
structure aside from depth and the odd
vault or pit. No orc barracks levels,
swampy areas... What "structure" there
is is a slight fluctuation in a random
background rather than woven through
the game.
N -- Angband is well-nigh
unwinnable without
reading r_info.txt or
using the ng and asking
"spoily" questions.
S -- Spoily stuff isn't
frowned upon in the
community.
R -- Recent versions
*did* fix the
double
manastorm.
N -- Ever heard of
statgain?
M -- GoI is well-
earned.
R -- Uh, you weren't initially bewildered by the plethora of options
presented at character creation?
SS -- The game is well-nigh unwinnable without good starting stats,
and moreover the autoroller and point-based birth options
provide not one but *two* built-in ways to scum for them.
F -- In plain Angband it's well-nigh impossible to play a pure
spellcaster and win. Someone did it with a mage *once*.
With priests I doubt it's ever been done.
Also, just because it has rarely been managed doesn't mean
this flag doesn't get stuck there. Simply because a mage
*can* play as a fighter with spell support and moreover
*will* have an easier time if played as such means that it
isn't really a true spellcaster class, just a class that can
*as a challenge game* be played as a pure spellcaster. The
two are not one and the same.
W -- Go to the corner grocery store. Does it present itself to you
as a list of items and prices, or as a physical space to browse?
Angband characters seem to order their stuff from EBay and
Amazon.com over the Middle Earth Internet. If that isn't weird, I
don't know what is.

Graaagh the Mighty's profile photo
Graaagh the Mighty
unread,
May 3, 2001, 10:27:27 PM
to
On Wed, 02 May 2001 04:29:02 GMT, ke...@grinnell.edu (Chris Kern) sat

on a tribble, which squeaked:
>There could be ways around this, like saving the monsters and letting


>them wander between map panels. A properly designed wilderness can
>add a lot to the game.

Or (my original suggested fix in original post of thread) get rid of
"panels" entirely, and just have a giant 3d cube grid with a radius
around the player active. (This also gets you water and trapdoors that
operate sensibly and stairs monsters might use.) If you want to add
alternate worlds and places with strange topologies, allowing multiple
"cubeworlds" to link with "portals" would work.

Lighting has to make more sense too. Orc-inhabited areas should
probably have torches along the walls, and their own light. A cave of
slimes and jellies of course could be quite dark, aside from the eerie
glows around phosphorescent life forms and Will-o-Wisps. Sunlight and
day/night are easy: orthographically project light from the ceiling of
the "cubeworld", stopped by floors, dimmed close to sunset/sunrise,
and dimmed going into water.

Now, making sure the game generates water that obeys Archimides'
Principle (a contiguous body of water fills its container up to a
uniform height) is of course trickier. (Actually, the height can be
non-uniform if serious differences in air pressure exist between two
exposed bits of water surface; this is useless for the game
programming purpose however.)

>His post was sort of off-topic for this group, but he was talking
>about a new roguelike, not another Angband. However, it is nice to
>have some secrets in a game. If *identify* was not so hard to get in
>Angband I would try to play more without spoilers. Then maybe
>artifact finds would be exciting :)

Or if *Identify* weren't so all-fired necessary because mistakes were
less costly except when compounded massively. (Then use randarts.)

>Perhaps. It's mostly Word of Recall, stat restore, and restore life
>levels that must be scummed.

I've had to scum up other things fairly often, notably:
* Teleportation
* Temp speed
* Identify

>>> >AYBABTU has a good balance, IMO.


>>>
>>> The biggest problem with Angband's artifacts is that over half of them
>>> are totally worthless.
>>
>>Overall it does far far better than anything else on the market, IMO.
>
>Could be much better, though.

Exactly.

BTW, my post was not "off-topic" as Angband was used frequently in
examples, being a CRPG with which I have significant experience.

>>But they don't carry items(and wield them) nor do they have the
>>AI or spells to compete, so something has to be doen to make them uglier.
>
>It's a necessity because of the game design, but you could make a game
>where the monsters did not have to possess these compensating factors.

Force AI on. Moreover make AI make sense. Hounds follow a smell
gradient and sounds, but they don't communicate complex plans with one
another and perform sneaky englobements -- though when attacking a
group they would try to separate one from the rest and attack this
victim 8 at a time. A pack of orcs, OTOH, would remember things that
weren't in sight, follow sounds less well, and form longer-range plans
and communicate, setting up ambushes and englobements. Trolls are of
course somewhat stupider than this, but smart enough to pick up and
use simple items. A lich would be far more powerful -- the typical orc
might manage to zap off a wand of magic missile on a good day, but a
lich would have no trouble using that Rod of Havoc you carelessly left
lying around, and moreover would be smart enough to go out of his way
to retrieve it before picking a fight with you. Fortunately, a lich
would also probably occur alone and summon unintelligent slaves rather
than other liches or whatever. Feagwath could have 1000 hit points and
a low AC, and be truly *scary* still even with toned-down summons.

Julian Lighton's profile photo
Julian Lighton
unread,
May 3, 2001, 11:19:59 PM
to
In article <3AF13D12...@dimetrodon.demon.co.uk>,

Kieron Dunbar <nor...@dimetrodon.demon.co.uk> wrote:
>Once upon a time, Braeus wrote thus:
>
>> Java is evil. Python is not.
>
>I don't know about Java, but Python is completely amoral. It would destroy 90%
>of life on earth without a second thought. And you suggest we use it in
>Roguelike creation?
Sounds like a plan.
--
Julian Lighton jl...@fragment.com
"Can I play with madness?" -- Iron Maiden

Graaagh the Mighty's profile photo
Graaagh the Mighty
unread,
May 4, 2001, 12:57:58 AM
to
On Tue, 01 May 2001 15:53:38 -0700, Joseph Oberlander
<ober...@pacbell.net> sat on a tribble, which squeaked:
>> > T -- indicates survival tactics require teleportation capabilities and
>> > massive detection capabilities.
>> > (Undesirable because it is bad roleplay, removes some strategic
>> > elements one could otherwise have, and virtually forces the use
>> > of heavy-handed game mechanics around vaults, special levels,
>> > &c -- also, the need for massive detection leads to the
>> > availability of massive detection, which then erases the element
>> > of surprise or at least vastly reduces it!).
>
>Desireable. In RL, if I go to the wrong side of town and make trouble, I
>will be in situations where I am way over my head. Retreat is an option,
>and in Angband, nothing requires that you kill anything unless you decide
>to wake it up/get to close or attack it.

The need for tactics, including choosing your fights and being able to
escape, is desirable.

This inflating into needing to be omniscient and able to teleport at
will is undesirable.

One good aspect of the recent "closed vaults" idea is to add that
element of the unknown surprise factor back into the game. (Randarts
and the proposal to randomize uniques and maybe some other monsters
are others.)

>> > I -- indicates temporary invulnerability is available in the game.
>> > (Neutral, but undesirable if too common.)
>
>GoI needs to be made to not work at all against H-H damage(magical attacks
>and such are blocked)

I wouldn't object to that. The +100 to AC it gives for its duration is
quite enough. GoI then is like the phantom menace: "Starten up da
shield!" -- things that step inside can still hit you. :) In fact,
making it a shield radius (things that close to within that radius can
hit you with anything; otherwise nothing) would also be interesting.
Giving it a resistance to penetration would be interesting too (fixed
chance for a monster to fail to enter the shield, unless the player
steps toward it and thus lets it in). Distinct of course from rune of
protection but similar in some ways. Summoning would have to be
re-worked: ADOM-style summoning or else summoning around a globed
player surrounds the globe but won't penetrate it (except when the
summoner is inside the globe himself!) ... This would make it live up
to its name, Globe.

>I think this is great and necessarry.

It's an artifact of the low inventory capacity plus there being only
one town, with most places in the game very far as the player walks
from the town.

>> > T -- indicates themed areas, with certain monsters/items more likely,
>> > and/or in-character drops for monsters. (Desirable. Games with
>> > too little spatial structure, e.g. vanilla Angband, are less
>> > interesting and must rely on temporal structure too heavily to
>> > avoid actually being boring.)
>
>Themed games can also be seen as a give-away/pattern game. Very easy to
>slide down the slope to PSX type games where it is scripted.

What, you don't think high degrees of randomization and themes can
coexist?

>Life is random. I personally LOVE random quests.

Yeah, but "This level is guarded by ... " doesn't make much
role-playing sense. Why are they there? How does vanquishing them make
the passage forward available? A guardian monster carrying a key makes
sense; so does one that blocks a path or makes it very dangerous to
traverse unprepared. A mysterious engraving, a bunch of guardian
"yellow jellies", and a magic appearing staircase are the role-play
equivalent of a massive kluge.

Note that Zang is clearly fun to play despite having problems in the
role-play-logic department; plain Angband is even worse in that area
but also fun to play. I'm not suggesting Zangband or regular Angband
is *bad*. I'm suggesting there exists a theoretical possibility that
something *better* can be crafted.

>> > W -- indicates a wilderness. (Desirable.)
>
>Fluff. Scummable. Not desireable as it detracts from the overall continuity.
>(you can play Angband sans wilderness just fine)

Wilderness as implemented in most roguelikes is bad -- see 'WW'.
Wilderness as implemented in e.g. Zelda is a step in the right
direction. The insane ability to regenerate the monsters instantly is
scummable there, of course.

Now a realistic wilderness, with the same mechanics as the dungeons
just different symbols, *does* present one problem: large distances.
But that can be fixed with the UI: extend the "run" commands to
include a disturbable "flow to" command with some intelligence about
negotiating obstacles and ignoring friendly/harmless NPCs with respect
to disturbance.

>> > E -- Game has secrets/Easter eggs. (Desirable.)
>
>Nope. Very very undesireable. Playing too much Nintendo. What makes
>Angband truly great is that there is no "powerup behind door 4 on level.."
>nonsense.

That's because they are invariably fixed. Random secrets are nicer --
different from game to game with only a subtle clue (but there *is* a
clue) to suggest you dig here/whatever. Moreover, they are
implementable. A secret also even be planned as to its existence and
possibly also some or all of its contents, but randomly placed within
certain limits. Very rare occurrences could provide surprise and
curiosity as well -- sort of like the One Ring, but able to be more
elaborate, such as a quest you hardly ever can discover, or a hidden
level that is rarely generated. To some extent this exists -- rare
artifacts; GCVs and other rare vaults; ...

>> > DDD -- indicates that the game has excellent documentation and
>> > moreover this is presented "in-game" in role-played fashion to
>> > the greatest extent possible -- i.e. the outside-the-game-world
>> > manuals only explain getting started, character generation, the
>> > program's interface, and other elements not themselves part of
>> > the role playing proper. (Desirable -- "learn as you go along"
>> > is very good role-playing so long as it isn't slow and
>> > frustrating trial-and-error exclusively!)
>
>Again, too much gaming consoles. RTM, folks.

No, just good roleplay. Hey, sometimes the gaming console guys hit
upon a good idea. The manual of a CRPG, IMO, should explain the
interface; details of the game world itself should be self-explanatory
-- discovering it should be a part of role-play.

>> > U -- indicates that unfair (i.e. difficult to avoid *and* difficult to
>> > recover from) events can occur in any stage of the game.
>> > Unavoidable deaths are the most common unfair event.
>> > (Undesirable.)
>
>Angband has none of these with the speed-fix-patch.

Who said anything specifically about Angband? If you'd looked at the
table you'd have noticed vanilla didn't have a U, and the comment says
that it only deserved an R before the speed-fix-patch.

>> > N -- indicates that the game designers responded to players abusing
>> > scummable features (e.g. stat potions) by making the scumming
>> > *necessary* (e.g. the leap in monster nastiness in Angband at
>> > 2000'). (Undesirable.)
>
>Scunning is not necessarry. IMan chracters can win, afterall.

For all practical purposes it is. Ironman is a challenge game,
therefore cannot be considered representative of how the "standard"
game is played.

>> > T -- indicates that the game designers limited scumming by creating
>> > time or progression limitations of some kind, e.g. finitely many
>> > monsters/items generated whole game, time limit, move limit,
>> > inability to save the game, or similar. (Undesirable.)
>> > U -- indicates that the game designers used something really evil and
>> > unfair to limit some form of scumming, making it exceedingly
>> > dangerous, but with unfair side effects for "legit" characters.
>> > (Undesirable.)
>> > S -- indicates that the game designers limited scumming by rendering
>> > it both unnecessary and either undesirable past a point or
>> > impossible without using any of the above methods. (Desirable.)
>> > M -- indicates that unlimited scumming can create munchkins.
>
>My half-preserve model would fix almost all of this nonsense.

True. [O] goes a long way, removing the need for statgain scumming
too. Also, there's no time or progression limitation (T) in any *band
I'm aware of. That applied to ADOM and some others, but not Angband.

>> > S -- Starting a new character, it is well-nigh necessary to scum for
>> > high starting stats or something similar. (Undesirable.)
>
>Point-based half-maximize(my idea) would fix this if combined with
>3E norms for stat increases.(this REALLY should be done)

Point being? Of course there are solutions to this -- if it were an
unavoidable issue in roguelikes I wouldn't have even included it.

>
>> > SS -- The game actually has built-in features to assist in automated
>> > scumming for high starting stats or whatever. (Undesirable.)
>
>Bye-bye with the above proposal. You have a finite amount of points
>to allocate, and since things are rounded down(avg 10 - 60 points to
>distribute+racial bonuses)), you will always be short as racial minimims
>also have to be paid for out of that.

If you get rid of autoroller and make point-based automatic, it's no
longer automated scumming, but part of the game (your physical and
mental training prior to tackling the dungeon, say). Especially if you
cast it in a role-playing framework as such, by e.g. putting a
stat-training-hall into the town, and letting players spend gold to
train their stats, but only so many points can be trained each clevel
(including some at the start of the game -- clevel 1) and each costs
only so much. E.g. to raise str there to 18/20 from 18/10 takes 1
point and 100 gold; it's 2 points and 200 gold to get from 18/110 to
18/120. You start with so many points, and get some each clevel
gained. Unspent points can be spent later (e.g. when you have the
gold). (Equipment bonuses ignored.) In this case you might get rid of
stat potions *entirely*, except you might want to keep chr potions.
(Nobody will spend much money on chr anyway.)

>Fixed by moving the last three 4th-book spells to a special book and
>moving soe of the Raals spells to the 4th. Easy access at decent levels to
>Raal's spells would solve most of the midgame power-crisis.

No, the only real solution is to make pure spellcasters truly terrible
at melee, at least without Tenser's. Fixing the midgame power-crisis
is necessary to make truly awful melee capability a reasonable curse
to foist upon the pure spellcaster classes, of course.

>(the last 3 spells are to powerful, IMO, for the 4th book)

Mana storm certainly is. The genocides are balanced by the cost in hit
points, with attendant danger factor.

>> > G -- Game has a glut of artifacts. (Undesirable: artifacts should be
>> > rare and special. It's bad role play otherwise.)
>
>Angband has a good balance, IMO. The random generation routine for them
>though, needs to be SERIOUSLY rebalanced. Items should not have every
>resist, for instance.

Except very rare and special items that are purely mythical like
Bladeturner. :-)

Other roguelikes get by without characters typically finding dozens of
artifacts a game, with many not worthy of the status. Some of the
weaker "artifacts" might be better off made rare ego items, e.g. the
'thancs into Daggers of <Element> of Smiting, the Paurfoos into Gloves
of Elemental Mastery (<Element>), ... -- destroyable but replaceable
too. Ringil, Bladeturner, Aule, Deathwreaker, Caspanion, Colluin, and
such of course would keep their exalted status as incredibly powerful
unique creations.

>> > M -- Some minor task requires inordinate amounts of the player's
>> > attention, e.g. avoiding starvation or repairing stat drains a
>> > lot. (Undesirable, even if realistic, because *boring*.)
>
>Add an amulet of Sustenance or make Hold Life stop you from needing food.

Actually, food management in Angband is non-tedious, and fuel
management (pre-Phial) only mildly tedious. This referred more to food
management in ADOM, which is a serious issue in the early game and a
nonissue in the late game. In ADOM, promising early game characters
can easily starve through no fault of their own. Angband earned an 'M'
simply because fixing stat and xp drains takes a significant part of a
player's time in the later game. Making drains temporary (with the
possible exception of Time attacks, which are *meant* to be
exceedingly nasty) but last several rounds would fix this. Drains
would be a significant threat still, but not a threat of massive
annoyance and money lossage -- just a threat if they lost you that
spell or blow or 0% fail and the in-progress battle was going badly as
a consequence. That is, drains would (at least mostly) drop from the
strategic scale of the game down to the tactical scale.

>> > A -- Asymmetrical game mechanics or just plain asymmetrical powers
>> > make monsters very different from the player in e.g. hit points.
>> > (Necessary to some extent if the player is to survive, but
>> > undesirable past a certain point.)
>
>Like fixing the Draco-lich/lisk nonsence?
>Dracolisk is a half-dragon half-basilisk! Super Umber-Hulks.
>
>DracoLich is a Dragon that turned itself into a Lich!
> Ouch-and-a-half! These things should be the most powerful
> non unique dragon in the game, period, and very deep.
> All dragon and Lich powers rolled into one.

That's more a matter of mismatching names and capabilities. By
asymmetry I meant more that fundamentally very different rules apply
to PCs and NPCs. In Angband, there are attacks each can get that
others can never have of a magical nature; this isn't so bad, but the
monster hitpoint inflation means that even should-be-comparable powers
aren't. The [Z] problem where something might breathe chaos at the
player for 600 damage or instead target a monster adjacent to the
player and then do 800 highlights this. That [Z] problem is *not* a
bug in [Z]; it's a symptom of a design flaw. The design flaw is, of
course, a bug.

Graaagh the Mighty's profile photo
Graaagh the Mighty
unread,
May 4, 2001, 12:58:03 AM
to
On Wed, 2 May 2001 18:37:30 -0400, Matthew K Lahut
<mla...@andrew.cmu.edu> sat on a tribble, which squeaked:
>> C -- Hard to identify stuff and easy to wind up with a
>> nearly-unplayable (or even actually unwinnable) game (or get
>> killed) due to cursed stuff or lost items. (Can be combined with
>> I or II; e.g. ADOM has CI because in the early game C holds true
>> and in the late game I holds true.
>I'm not sure what you're getting at here. This is one of the challenges of
>nearly every roguelike... find out what all your stuff does.

Yeah. That's why my statement is a logical "and". Hard identification
is good; but being able to be screwed really easily because of it is
bad. Angband has id too easy. ADOM has it hard enough in early game
but has converse problem. You can seriously screw yourself with cursed
stuff, the IBM Guild Manual, ...

>> E -- Cursed stuff is not a threat, either because it is easily
>> detected and avoided, easily removed, or just not that bad.
>> (Mutually exclusive with C.) (Undesirable -- useless gameplay
>> elements are in general undesirable.)
>This feature is essentially identical to II.

You can have neither I, II, C, nor E. Cursed stuff that is really
game-losing is detectable before it's too late; mildly cursed stuff is
a setback but harder to detect before being stuck with it. Same for
potions/scrolls with bad effects...

>> R -- A weird and questionable mechanism is needed to access stuff
>> saved somewhere, some locations, or such in reasonable time (e.g.
>> *band's Word of Recall). (Undesirable -- bad role-play.)

>So you don't like Word of Recall, fine. That's your opinion. I think
>they're necessary in Angband to avoid boredom.

I agree. But that's symptomatic of the game's odd organization --
basically only one town and excessively linear. ADOM lacks recall and
has fewer problems -- the main game dungeon only goes down 50 dlevels
and shortcuts become available, plus multiple towns and other
dungeons.

>> Z -- Saved stuff is prone to destruction, or stuff can't be saved.
>> (Undesirable usually -- stuff is usually necessary -- symbol
>> omitted if saving stuff isn't vital or at least highly
>> desirable.)
>Here you open the argument of limited inventory. Every roguelike has this
>to some extent. Adom doesn't really have this attribute; use the
>barbarian's glade.

Just because a bug/issue has a workaround doesn't mean it's fine and
dandy to leave it unfixed. And it has been acknowledged as a bug:
* ADOM monsters picking things up and not dropping them on death
(and related, game crashes associated with NPCs picking stuff up --
smacks of pointer/memory mismanagement to me!);
* A friendly NPC can pick something up, and you must either give it
up or do something drastic that is liable to impact your alignment
and maybe end your life. (Often the NPC is quite able to kick your
a$$ in combat...)

>> Structure column:
>> B -- indicates "bad" quests (e.g. random monsters and other stuff that
>> doesn't make very much sense). (Undesirable: bad roleplay.)
>Other than *band-variant-style "joke" monsters, could you give some
>examples of this?

Kill 30 of <random>, etc.
Roleplay my foot. Kill 30 of them *why*? How does this unbar your
passage -- does one of them carry a key? All pieces of the key to
assemble? Someone assigned it as a test of your abilities? If the
latter, how do you prove to them that you did it, and how do they
unbar the way when you do? There should be a plausible in-character
mechanic for a game behavior, aside from pure interface issues.

>> H -- indicates heavy-handed game mechanics are used. (Undesirable.)
>> HH -- indicates heavy-handed game mechanics are used extensively.
>> (Undesirable.)
>You have H or HH included in each roguelike in your chart. It seems to be
>a pretty fundamental concept. What do you consider to be too
>heavy-handed? The term seems vague to me.

This is impossible. Why? Just because. This will magically appear when
this has occurred -- why? It just does, there is no in-character
reason behind it. It's like you suggest something your character will
do, and the DM says "This simply isn't allowed", rather than "you try
<foo> but fail due to <bar>" or "you try <foo> and here are the
(perhaps unintended) consequences". The game holding your hand (e.g.
physically barring your character from going somewhere damgerous
purely on the basis of clevel) falls into this category too. The
DM/rules/CPU enforces the consequences of actions, rather than
limiting the actions directly; the consequences then guide the
player's choices. The sole exception being the laws of physics -- you
can't choose not to fall after triggering that trap door, etc. Of
course a CRPG must have some limitation. Too-creative stuff isn't
possible, but basic stuff is -- walk north key either works or,
because something is in the way, fails. Something that's there has a
sensible in-character reason for being there; something that happens
has a sensible in-character mechanism for occurring; NPCs have
sensible in-character reasons for their actions...

>> W -- indicates a wilderness. (Desirable.)
>Again, tastes vary. Many games work fine without a wilderness, and would
>be harmed by the insertion of one.

Perhaps. A game set entirely in caves for example. But the trick
clause here is "set *entirely* in caves". Angband doesn't qualify: it
has the town. A game that starts you in a cave doesn't necessarily
qualify: unless the entrance you know of collapsed behind you, what's
to stop you leaving? A heavy-handed "you just can't"? It is possible,
admittedly -- for instance this premise: "You have fallen into a cave
through a sink-hole. The way you fell in is beyond your reach. You
must explore looking to escape; when you do, you win." You have two
options: find a way to make the entrance reachable (rope? boots of
flying?) or find another exit of course... In this case the wilderness
is unnecessary since the game has been won when the game would
otherwise have to let you into it.

>> Spoilers/documentation column:
>> N -- indicates that reading spoily information is pretty much
>> necessary to win the game. (Undesirable.)
>Another item that you have included in each roguelike in your chart (And
>it's pretty true for Nethack, too.) This isn't always true, there's always
>*someone* who has finished the game without spoilers, though they are
>usually pretty rare.

Nah. As an oversimplification, there are two spoilers, S1 and S2.
Someone plays knowing neither, discovers S1, and dies. They report S1.
Someone else (or they) play, spoiled with S1, and discover S2, and
die. Someone else (or they) play, spoiled with both, and win.

Usually it's something like this. You either need spoilers or (with
many roguelikes) *hundreds* of attempts.

>Debatable. If I was playing a roguelike that always gave me the same
>hints, I'd find it annoying. Nethack and Adom both have a decent
>implementation of this (the Oracle and Mad Minstrel, respectively).

The hints would not be forced upon you. Pern has it to some extent
IIRC: the "Adventurer's Guide to Middle Earth" pamphlet. Cheesy but a
step in the right direction. Also, if you're familiar with it, you can
not bother with it. Same with talking to an NPC with useful info that
is unchanging from game to game. Talking to the NPC is like opening
the help browser and going to a particular topic; it's just
in-character whereas the help browser is external.

Also, we're talking the hints and lore of the game world, rather than
the program's UI. The latter should be explicated in the
documentation, and possibly also by a tutorial mode of the game.

>...giving appropriate help when new things are first
>encountered.

Like that.
For examples (mostly from console games, not all RPGs):
* Some NPCs in Zelda games give game hints when talked to.
* Super Mario World gives tutorial-esque instructions in
its early levels via those speaker-box gadgets, which the player
can opt not to hit. This is actually unclean as it puts
interface stuff into the game universe. There really should
instead be a tutorial mode in which these hints appear automatically
at the appropriate locations in a modeless status display for a bit,
and which can be turned off. Think Microsoft Word's paperclip
assistant thing, but less obtrusive and easier to turn off.

(Incidentally, it can be argued that *every* game of *every* genre
except highly abstract ones like chess or card solitaire are role
playing games. Mario World has you assume the identity of a character
with a quest. So does Zero Wing <g>. Even that dinky crapplet
Minesweeper is a CRPG of sorts -- the window title even names your
role.

>> C -- indicates that the game designers closed the source code.
>> (Undesirable.)
>A matter of opinion, certainly. This will have a *major* effect on spoiler
>availability. If you're writing this new game yourself, your views on this
>may change over the development process.

Heh. My game will be chock-full of dynamic elements. And emergent
properties will undoubtedly occur. Reading the angband source and info
files isn't exactly the same as getting a walkthrough, even to someone
with a Ph.D. in C programming. Why? Emergent properties. APW has been
fine-tuning the borg for years and still hasn't got it all figured out
in terms of the game.

This is actually related to the fear occasionally (and irrationally)
expressed about finding the physics ToE. "Once they find the ToE
that's the last word in science! Everything after that becomes mere
data-gathering. *shudder*" Uh, I think not. Knowing the exact laws and
equations governing the universe won't make the 3-body problem any
easier to solve, or answer at a stroke whether there is other life in
the universe, or whether silicon-based life can evolve naturally.
Exploring the complex ramifications and emergent consequences of those
laws would never end, certainly not in the foreseeable future, ToE or
no ToE. The simple equations underlying the Mandelbrot fractal are
well-known and it still is largely unexplored, and will *forever*
remain that way! New phenomena and patterns with new behaviors are
still being discovered in Conway's Life cellular automaton 40-odd
years after it was discovered, and that bears a strong resemblance to
a physics theory -- arguably it *is* a physics theory, albeit
describing a class of universes distinct from our own. (This follows
from a modern restatement of Platonism, that every mathematical
structure has objective reality and our universe is one that happens
to support "self-aware substructures" -- that is, people, which in
this universe specifically take the form of "human beings", and
perhaps other forms not yet discovered. And that restatement is in
fact a viable ToE itself, though not specific enough to answer what
exactly the physical equations are for our specific universe.)
To relate this back to the salient topic, discovering the ToE of
physics is like discovering the source code for that RPG called "life"
in which we are characters. Reading the source wouldn't spoil the game
though. Neither would it with a sufficiently complex CRPG.

As an added note, other games have this property of emergent
complexity. Chess has a set of rules damn near everybody knows. Very
few people become grandmasters. Even those haven't gotten it all
figured out. New openings and tactics and concepts have been
discovered in recent centuries. This is true despite the game being
around for thousands of years.

>Personally, I like it when nearly *any* event, good or bad, has a
>miniscule chance of happening. You say that early deaths are unfair. What
>about characters that find two artifacts before dlvl 4? Is that unfair
>too? Don't be overly nice to your players by "trying to be fair" to
>low-level characters; that's part of the fun. If bad luck never happened,
>the good luck wouldn't feel as good.

Bad luck is fine. Game-ending bad luck is questionable at best.

>> Miscellaneous column:
>> T -- slow and tedious to start a new character. (Undesirable,
>> especially in combination with 'E' or 'U' in fairness column.)
>I see how this is true for paper RPGs, but why Moria and *band variants?

Umm, because you don't just pick a race and class and appear in the
town?

Option glut and the need to autoscum for good stats or do the point
based thing is why starting characters is slow in most *bands.

>> R -- you have to be a rocket scientist to start a new character.
>> (Undesirable -- basicaly you'll be messing with zillions of
>> options and poring over documentation. Or dying a lot. Or both.)
>I disagree, at least as far as Angband and friends go. It's part of the
>learning process to see which characters you're good with, and what
>starting attributes are useful.

I speak of the complexity of the character generation process itself,
and the software interface to it, not the decisions of race/class
combos or even which stats to train. Contrast *bands with ADOM. The
latter has a much more streamlined and automated system.

>> P -- Polymorphing or other random and unpredictable elements make the
>> game chaotic and reduce its structure.
>> (Can be combined with Z, when endgame characters are all alike in
>> that they all polymorph a lot or whatever and play similarly
>> regardless.) (Undesirable.)
>I completely disagree. IMHO Nethack's polymorph system is one of its
>great strengths. Though it creates problems for some characters, it
>provides solutions to others. This fits in with my earlier statement about
>liking that any event has a non-zero chance of occurring.

Nethack is too volatile to keep long term structure. Stability is
nice, and so is unpredictability. Finding the balance is important.
Angband IMO is too stable, having locked long ago into a cycle of
rising inflation -- stronger and nastier monsters, more and more
detection and teleportation for players. Nethack is too unstable. With
[Z] and [P] it can go either way depending on race/class combinations
and (in [P] at least) use of altars. Choice is certainly good of
course.

Nethack's volatility would seem to make long-range planning a
worthless endeavor in that game. Highly radical changes that totally
rearrange things happen with too high a probability, and
polymorph-mania is a part of that. Now, Nethack is fun, but it's fun
comes more from zaniness than from roleplay... I'm not saying there's
not room for both, not even both in one game, mind you.

>This is true of *many* games, and I agree that it's undesirable. I believe
>that it is partially the fault of the interface. Suppose Angband could be
>configured so that the default action for a mage, when moving toward a
>monster, was to magic missile rather than melee attack? How would that
>change things?

The interface aspect is true. But the problem is that roguelikes are
still stuck in the Stone Age of interfaces. Weird-wilderness issues
stem from the same source ultimately: the need to save keystrokes to
cross large wilderness areas rapidly.

The solution (and you'll hate me for this even though it is logically
inevitable) is to use a graphics display and mouse.

You can, of course, use ASCII tiles if you want ASCII's
easy-to-interpret properties, or just its look and feel.

With that, a basic action can be done with a click.
Left double-click point: flow-to it, disturb as necessary. (Solves
wilderness weirdness at a stroke -- a huge contiguous wilderness
becomes ok to navigate.)
Right click point: get menu of targetable actions -- fire missile
(submenu for available missiles), cast spell (menu of spells from MM
to Mana Storm), look (brings up e.g. "this is a tree" or "a patch of
grass; a moderately wounded grizzly bear is occupying this spot"),
watch (brings up the look display in a modeless status area that keeps
updating as things happen; following a creature if one was hit, so you
can keep a wary eye on that grizzly bear), etc.
Right double-click point: default action, which can be reconfigured as
the game progresses. Fire unenchanted arrow? Magic missile? Maybe
later change it to fire the Black Arrow of Bard or cast an acid bolt.
(Bye bye macro cruft while we're at it.)

>> G -- Game has a glut of artifacts. (Undesirable: artifacts should be
>> rare and special. It's bad role play otherwise.)
>This is why I don't play Angband as much as I used to; with my best
>character, I throw out three out of every four artifacts I stumble across.
>The treasure filtering gets annoying when there are such stockpiles of
>mostly-lousy treasure (i.e. dragon drops).

It's a symptom of Angband's years-long arms race between players and
monsters, really. Both just keep getting bigger and badder Pointy
Things, and the former get smarter and more spoiled while the latter
get hit points and more hit points. That in turn is partially because
of the You Against The World issue, but not entirely as evidenced by
variants that have friendly NPCs and NPCs that fight among themselves
from time to time. Of course there's also the Ontogeny Recapitulates
Phylogeny Effect, in which each game re-enacts in miniature the arms
race. Indeed, the recapitulation was consciously designed in in at
least one instance -- when Angband proper was created, it was done by
doubling the depth of the dungeon, leaving the Balrog (as Muar) where
he was at 2500', and adding Morgoth as the game-winner target at the
new bottom. (Well that's a slight oversimplification, but there you
have it.) Of course, to some extent character development in an RPG
must perforce involve a character getting better Pointy Things and
more capabilities in general, and thus being able to tackle more
dangerous places and quests...

>> M -- Some minor task requires inordinate amounts of the player's
>> attention, e.g. avoiding starvation or repairing stat drains a
>> lot. (Undesirable, even if realistic, because *boring*.)
>You would probably consider this an attribute of Nethack too.
>Other people have criticized Angband's system for not making food
>important enough; it's a renewable resource that just occupies one
>inventory slot all the time.

Spellcasters get it cheaper: 1/4 of a slot, given that a couple other
useful spells are in the book with their food spell. :-)

A happy medium is to be sought.

>> W -- Weird game mechanics. (Undesirable -- catch-all for weird,
>> unrealistic or bad roleplay game mechanics not covered above.)
>Don't call it this. Specify what weirdness you like or dislike. (Which, in
>most cases, you did later.)

It was a catch-all -- I specified more clearly in each case. Inventing
one symbol for stores with interfaces like Amazon.com instead of a
13th-century bazaar or shop, another for a wilderness where the
physics is different from in the dungeons, yet another for the
existence of magic time limits (ADOM has several of these, of which
the only one that can really be justified is the much-berated 90-day
jump in background corruption, which can be justified as representing
the chaos creatures, after establishing their beach-head, opening the
Gate wider to permit full-scale invasion to commence.)

>> (chart snipped)
>> (footnotes snipped, resisting temptation to defend the individual games
>> I like)

The games all have the redeeming characteristic of being fun.
The role-play can be improved, that's all.
The only defense necessary is *if* one of my claims is untrue *then*
attempt to demonstrate this...

cropt's profile photo
cropt
unread,
May 4, 2001, 1:00:32 AM
to
Graaagh the Mighty <inv...@erehwon.invalid> wrote:
> W -- Go to the corner grocery store. Does it present itself to you
> as a list of items and prices, or as a physical space to browse?
> Angband characters seem to order their stuff from EBay and
> Amazon.com over the Middle Earth Internet. If that isn't weird, I
> don't know what is.
Simplified, not weird. Just abstracting away the unneeded parts of
shopping. I'd find it weird if EBay tried to put the browsing of a
physical space back in there. Maybe they could do it to make stealing
more realistic... =_=

Steven Fuerst's profile photo
Steven Fuerst
unread,
May 4, 2001, 1:22:45 AM
to
Graaagh the Mighty wrote:
> Note that Zang is clearly fun to play despite having problems in the
> role-play-logic department; plain Angband is even worse in that area
> but also fun to play. I'm not suggesting Zangband or regular Angband
> is *bad*. I'm suggesting there exists a theoretical possibility that
> something *better* can be crafted.

I know this might be strange... but 'fun' is often orthogonal to perfect
realism. You can have both, but I think it requires alot more thought
than what you've given the problem.

>
> That's more a matter of mismatching names and capabilities. By
> asymmetry I meant more that fundamentally very different rules apply
> to PCs and NPCs. In Angband, there are attacks each can get that
> others can never have of a magical nature; this isn't so bad, but the
> monster hitpoint inflation means that even should-be-comparable powers
> aren't. The [Z] problem where something might breathe chaos at the
> player for 600 damage or instead target a monster adjacent to the
> player and then do 800 highlights this. That [Z] problem is *not* a
> bug in [Z]; it's a symptom of a design flaw. The design flaw is, of
> course, a bug.

Actually it was a bug... one that was fixed about a year ago. I missed
one of the places that used the GF_ type of the projection when adding
the changes from [O] to [Z] in 2.3.4

Steven

Timo Pietilä's profile photo
Timo Pietilä
unread,
May 4, 2001, 4:26:27 AM
to
Graaagh the Mighty wrote:
>
> On Wed, 02 May 2001 00:49:35 +0300, Timo =?iso-8859-1?Q?Pietil=E4?=
> <timo.p...@helsinki.fi> sat on a tribble, which squeaked:
>
> >
> >
> >Graaagh the Mighty wrote:

> >> Game |Life|Item|Structure |Docs |Fair|Scumming|Misc
> >
> >> Angband TSI IIER HLVClCtRR15 ND E16 NS17 RSSZFGA
> >> W18
> >Angband TSI IE TLVClCtRR SD R SM ZGA
> II -- greater identify is available in spades,
> once you get past a certain point.

Not available enough. Not for me. For player like you who crawls through
levels it probably is.

> R -- Ever zapped a rod of recall?

Yes, but that isn't odd method to me.

> N -- Angband is well-nigh
> unwinnable without
> reading r_info.txt or
> using the ng and asking
> "spoily" questions.

Then how did I won my first game? I wasn't visiting newsgroup all of
time. In fact whole internet wasn't accesible at that time.

> S -- Spoily stuff isn't
> frowned upon in the
> community.

It isn't couraged to use spoily stuff.

> R -- Recent versions
> *did* fix the
> double
> manastorm.

So in this we agree? Even earlier double manastorm wasn't a problem. I
didn't even know that bug was there with my first 10 winners.

> N -- Ever heard of
> statgain?

Yes, but that is not scummable. It only requires you to slow down at
that point of game. You *don't* need max stats to go deeper. Only some
constitution to get higher HP.

> M -- GoI is well-
> earned.

In what way?

> R -- Uh, you weren't initially bewildered by the plethora of options
> presented at character creation?

That's right.

> SS -- The game is well-nigh unwinnable without good starting stats,
> and moreover the autoroller and point-based birth options
> provide not one but *two* built-in ways to scum for them.

Bulls*it. I was playing this game without autoroller and point based.
Game is totally winnable without perfect starting stats. But that other
part is right, game has a feature to get higher starting stats. So I
would have put there a single S but not the first one.

> F -- In plain Angband it's well-nigh impossible to play a pure
> spellcaster and win. Someone did it with a mage *once*.
> With priests I doubt it's ever been done.

Pure spellcaster doesn't mean that you use only spells. Priestly types
work pretty much perfectly in that area. Mages are problem. They need
some rebalancing. Game is winnable using only prayers for priest if you
allow low level priest to hit some monsters in head into beginning.

Rangers are not warriors also and they play like rangers. Also paladins
play like paladins (they are warrior priests) and rogues use stealth,
fighting and spells. For all those this flag is not correct. So this
flag is correct only for mage.

> W -- Go to the corner grocery store. Does it present itself to you
> as a list of items and prices, or as a physical space to browse?
> Angband characters seem to order their stuff from EBay and
> Amazon.com over the Middle Earth Internet. If that isn't weird, I
> don't know what is.

Symbolism. The shop interior and whole interact into store is presented
like that. It isn't weird for me. No weirder than nethacks store.

After all roguelike games are not RPG:s. They are roguelikes.


Timo Pietilä

--
A(2.9.2) C "Wanderer" DP L:20 DL:750' A-- R--- Sp w:LxBow(+9,+9)

Matthias Kurzke's profile photo
Matthias Kurzke
unread,
May 4, 2001, 5:14:05 AM
to
Graaagh the Mighty wrote:
> On Wed, 02 May 2001 04:29:02 GMT, ke...@grinnell.edu (Chris Kern) sat
> on a tribble, which squeaked:
>
>
>> There could be ways around this, like saving the monsters and letting
>> them wander between map panels. A properly designed wilderness can
>> add a lot to the game.
>
>
> Or (my original suggested fix in original post of thread) get rid of
> "panels" entirely, and just have a giant 3d cube grid with a radius
> around the player active. (This also gets you water and trapdoors that
> operate sensibly and stairs monsters might use.) If you want to add
> alternate worlds and places with strange topologies, allowing multiple
> "cubeworlds" to link with "portals" would work.

I hope the player won't completely lose orientation ... and the game be playable on computers with only 1GHz processors...

>
> Lighting has to make more sense too. Orc-inhabited areas should
> probably have torches along the walls, and their own light. A cave of
> slimes and jellies of course could be quite dark, aside from the eerie
> glows around phosphorescent life forms and Will-o-Wisps. Sunlight and
> day/night are easy: orthographically project light from the ceiling of
> the "cubeworld", stopped by floors, dimmed close to sunset/sunrise,
> and dimmed going into water.
>

All of this is nigh-impossible to get in a roguelike ASCII world. How many shades of light do you want to exist?
Matthias

Mårten Woxberg's profile photo
Mårten Woxberg
unread,
May 4, 2001, 7:55:57 PM
to
On Fri, 04 May 2001 04:58:03 GMT, inv...@erehwon.invalid (Graaagh the
Mighty) wrote:
>On Wed, 2 May 2001 18:37:30 -0400, Matthew K Lahut
><mla...@andrew.cmu.edu> sat on a tribble, which squeaked:
>

<sniip>


>
>>> W -- indicates a wilderness. (Desirable.)
>>Again, tastes vary. Many games work fine without a wilderness, and would
>>be harmed by the insertion of one.
>
>Perhaps. A game set entirely in caves for example. But the trick
>clause here is "set *entirely* in caves". Angband doesn't qualify: it
>has the town. A game that starts you in a cave doesn't necessarily
>qualify: unless the entrance you know of collapsed behind you, what's
>to stop you leaving? A heavy-handed "you just can't"? It is possible,
>admittedly -- for instance this premise: "You have fallen into a cave
>through a sink-hole. The way you fell in is beyond your reach. You
>must explore looking to escape; when you do, you win." You have two
>options: find a way to make the entrance reachable (rope? boots of
>flying?) or find another exit of course... In this case the wilderness
>is unnecessary since the game has been won when the game would
>otherwise have to let you into it.

The fallen through a hole and can't get up is just an excuse to play..
why need it?? I wouldnt start the game and thus I wouldnt fall down..
game completed.. or why is the character so dumb he falls into a hole?
when he is so smart he can use spells etc..
and the Town is a part of the Dungeon in Angband IMHO


<snip>

Geez you guys make LONG posts!

I just wanted to say that I'm all for a little more
RPGing in Angband.. but don't make it into a Final Fantasy game..

/Mårten

Joseph Oberlander's profile photo
Joseph Oberlander
unread,
May 4, 2001, 8:45:01 PM
to
In other games, you have a shop and an inventory.
A fixed inventory.

I sugest that all shops have a second list of items that are normal
mundane ones. You pay BM prices, though, but in this case you
could get say 50 CCW potions since they are one of the ten "normal"
items.

This would get rid of almost all scumming.


The shop has a first page, with 10 fixed slots.
The second page is all the special items and such. Stuff you sell goes
into the appropriate slot, of course. First-page items can also show
up there.

General store, for instance would carry:
Various food and drink(6 slots)
Oil, Lamps and torches(3 slots)
Cloak(1 slot)

Weapon Store would carry:
Arrows, pebbles, shots, and bolts - as many as you want, but plain.(4)
Basic edged weapons - dagger, tulwar, longsword(3)
Basic shooters(sling, short bow, light x-bow(3)

BM has it as well:(twice normal BM price!)
Speed potions
Teleport level
(etc - very basic non-special stuff that we all scum for)

Temple:
CLW, CSW, CCW, Restore Life(4)
Priestly books(4)
Whip and Mace(2)

Magic shop
Basic books(4)
Basic staves(ID, detect invis, etc)(6)

Alchemist
Phase-door
WoR
Enchant weapon and armor(3)
Satisfy hunger
*ID*(4K a pop!)
etc.

This would cut down on the tedium as well. Buy 3 stacks of 99 arrows and
enchant them to hit if you have the money(at 3-4 AU an arrow!)

Joseph Oberlander's profile photo
Joseph Oberlander
unread,
May 4, 2001, 8:50:38 PM
to
> > SS -- The game is well-nigh unwinnable without good starting stats,
> > and moreover the autoroller and point-based birth options
> > provide not one but *two* built-in ways to scum for them.
>
> Bulls*it. I was playing this game without autoroller and point based.
> Game is totally winnable without perfect starting stats. But that other
> part is right, game has a feature to get higher starting stats. So I
> would have put there a single S but not the first one.
I *love* to play without the roller. This is like Wizardry(and twenty
other games from the early days of the genre) - one shot and there you
go. Completely winnable, just requires a different strategy.

Chris Kern's profile photo
Chris Kern
unread,
May 4, 2001, 8:48:03 PM
to
On Fri, 04 May 2001 01:36:14 GMT, inv...@erehwon.invalid (Graaagh the
Mighty) posted the following:

>SS -- The game is well-nigh unwinnable without good starting stats,

Ridiculous! Reaching stat gain can be done with very poor starting
stats. I have no doubts that I could get a mage to stat gain with no
abilities over 17.

>F -- In plain Angband it's well-nigh impossible to play a pure
> spellcaster and win. Someone did it with a mage *once*.
> With priests I doubt it's ever been done.

Priests have excellent attack spells. Between Annihiliation, Orb of
Draining, Dispel Evil, and Banishment, I'm sure it's been done by
somebody.

-Chris

Chris Kern's profile photo
Chris Kern
unread,
May 4, 2001, 8:49:10 PM
to
On Fri, 04 May 2001 11:26:27 +0300, Timo =?iso-8859-1?Q?Pietil=E4?=
<timo.p...@helsinki.fi> posted the following:
>Pure spellcaster doesn't mean that you use only spells.

I'm curious, then, what does this mean?

-Chris

Chris Kern's profile photo
Chris Kern
unread,
May 4, 2001, 8:50:34 PM
to
On Thu, 03 May 2001 12:12:18 +0100, Kieron Dunbar
<nor...@dimetrodon.demon.co.uk> posted the following:
>Once upon a time, Braeus wrote thus:
>
>> Java is evil. Python is not.
>
>I don't know about Java, but Python is completely amoral.

^^^^^^

Yes, I believe we can say a programming language does not possess
morals :-)

-Chris

Chris Kern's profile photo
Chris Kern
unread,
May 4, 2001, 9:26:00 PM
to

I agree completely. There is no reason to not have a spellbook that
you need in the shop. Angband is constructed in such a way where you
can't just say "Oh well, no 3rd spellbook...who needs orb of draining
anyway, I'll just go back down to 1650'."
-Chris (I personally consider wandering around at 50' just as much
scumming as resting near the stairs waiting for the stores to roll
over.)

Brian Barnes's profile photo
Brian Barnes
unread,
May 4, 2001, 11:55:53 PM
to
I thought the point of vanilla was to be as tedious and patience-testing as
possible. Otherwise, the [V] town might have more shops and services, and
[V] would have some form of auto-squelch. Right? :/
-Brian



Robert Ruehlmann's profile photo
Robert Ruehlmann
unread,
May 5, 2001, 5:44:27 AM
to
Sounds like a good idea. I used to think that no type of item should be
always available at the stores to give players an extra challenge from time
to time (like playing without phase door scrolls for a while). But town
scumming is just too easy for this to have any effect. Making items that
players would rather town-scumm for than live without always available
removes the need for town-scumming.

The selection of items seems pretty good, but having a steady supply of
speed potions might lead to rich players always running around with a
"temporary" speed boost. Any idea if this really is a problem and how it
could be prevented?

Anyway ... moving the table of objects sold in the stores to
lib/edit/b_info.txt is already on my ToDo list. Extending the format so
that it's possible to mark items as "always try to keep in stock" shouldn't
be too tricky.

--
Robert Ruehlmann ( r...@angband.org )
"Thangorodrim - The Angband Page" : http://thangorodrim.angband.org/
Visit the #angband chat channel at irc.worldirc.org



Eytan Zweig's profile photo
Eytan Zweig
unread,
May 5, 2001, 6:06:05 AM
to
>===== Original Message From "Robert Ruehlmann" <r...@angband.org> =====

>"Joseph Oberlander" <ober...@pacbell.net> wrote:
>> In other games, you have a shop and an inventory.
>>
>> A fixed inventory.
>>
Great idea, except:

>> BM has it as well:(twice normal BM price!)
>> Speed potions
>> Teleport level
>> (etc - very basic non-special stuff that we all scum for)
>>

I really don't think the black market should be included in this. If an item
is deemed important enough to be always present, it should be moved out of
the
BM into a normal shop. If it is deemed too cheap, it should be made more
expensive. Putting it in the black market just so you can double the price
again is not a good way to go about doing this.

Also, I'm not sure why the always present items have to be more expensive in
the first place. The difference in price is negligable for a late player,
and
potentially very problematic for an early player - making the game more
difficult by making it harder to start a characer will just make the game
more
tedious. Again, some items might simply need individual price adjustments -
scrolls of *ID* are a good example if they are to be available at the
alchemist's.

>Sounds like a good idea. I used to think that no type of item should be
>always available at the stores to give players an extra challenge from time
>to time (like playing without phase door scrolls for a while). But town
>scumming is just too easy for this to have any effect. Making items that
>players would rather town-scumm for than live without always available
>removes the need for town-scumming.
>
>The selection of items seems pretty good, but having a steady supply of
>speed potions might lead to rich players always running around with a
>"temporary" speed boost. Any idea if this really is a problem and how it
>could be prevented?
>
>Anyway ... moving the table of objects sold in the stores to
>lib/edit/b_info.txt is already on my ToDo list. Extending the format so
>that it's possible to mark items as "always try to keep in stock" shouldn't
>be too tricky.
>

I'm glad to hear this - I was planning on doing it myself in Ey but kept
putting it off because there are other things that I preferred to do. I'd be
happy to just wait until it's in Vanilla and copy it from there :).

>--
>Robert Ruehlmann ( r...@angband.org )
>"Thangorodrim - The Angband Page" : http://thangorodrim.angband.org/
>Visit the #angband chat channel at irc.worldirc.org
>

------------------------------------------------------------
Get your FREE web-based e-mail and newsgroup access at:
http://MailAndNews.com

Create a new mailbox, or access your existing IMAP4 or
POP3 mailbox from anywhere with just a web browser.
------------------------------------------------------------

Matthias Kurzke's profile photo
Matthias Kurzke
unread,
May 5, 2001, 7:54:59 AM
to
I actually like changning shop inventory, as long as the most basic
necessities (i.e. CCW, Phase Door, maybe ID) are usually there.
Everythng else - you can do without. At least usually.

I'd rather have "services" added than guaranteed items, though. The
complete randomness is something I wouldn't want to give up for a
convenience.

How about "auto-scum for basic necessities in town" ;-)

>The selection of items seems pretty good, but having a steady supply of
>speed potions might lead to rich players always running around with a
>"temporary" speed boost. Any idea if this really is a problem and how it
>could be prevented?
>

I think this is a problem. I believe speed potions shouldn't be easily
available. They're so great for killing low-level uniques - I think
it's good that you have to be careful about them and cannot just waste
them. Likewise, Healing and *Healing*.

For Psiband, I just created a bookstore, and that meant no books
except there, i.e. lots of free slots in the Temple. Now the Restore
Stat potions are usually available somewhere :-) and you even have
choice where the shopkeeper likes you more...

>Anyway ... moving the table of objects sold in the stores to
>lib/edit/b_info.txt is already on my ToDo list. Extending the format so
>that it's possible to mark items as "always try to keep in stock" shouldn't
>be too tricky.
>

That's very good...

oh, that reminds me of something else. Who else can't remember what
b_info, g_info, and so on mean?

couldn't we use more descriptive names? like
"artefact.txt"
"ego-item.txt"
"playrace.txt"
"monsters.txt"

etc.///

the [a-z]_info.txt format, while mathcing the source, isn't SO very
convenient for looking up things...

Matthias

Chris Kern's profile photo
Chris Kern
unread,
May 5, 2001, 10:38:14 AM
to
On Sat, 5 May 2001 11:44:27 +0200, "Robert Ruehlmann"
<r...@angband.org> posted the following:
>Sounds like a good idea. I used to think that no type of item should be
>always available at the stores to give players an extra challenge from time
>to time (like playing without phase door scrolls for a while). But town
>scumming is just too easy for this to have any effect.

Phase Door scrolls do not necessarily have to be always available. In
my mind, the only items that are essential for play are the following:
Scroll of Word of Recall
Potion of Restore Life Levels
Potion of Cure Critical Wounds
Potion of Restore [statistic]
Spellbooks

These are the only items that I townscum for.

In addition, at the beginning of the game it's nice to have a Lantern,
and armor your character can actually afford. A bookstore would not
be a bad addition as well.

I do not think that Potions of Speed should be guaranteed. I also
don't think that Scrolls of *Identify* should be guaranteed, except I
do think they should show up in shop 5 as regular items. (I also
wouldn't mind seeing Scrolls of Teleport and Scrolls of Teleport Level
generated in shop 5, but that might be too much, I'm not sure.)

-Chris

Eytan Zweig's profile photo
Eytan Zweig
unread,
May 5, 2001, 12:27:38 PM
to
>===== Original Message From ke...@grinnell.edu (Chris Kern) =====

>On Sat, 5 May 2001 11:44:27 +0200, "Robert Ruehlmann"
><r...@angband.org> posted the following:
>
>>Sounds like a good idea. I used to think that no type of item should be
>>always available at the stores to give players an extra challenge from time
>>to time (like playing without phase door scrolls for a while). But town
>>scumming is just too easy for this to have any effect.
>
>Phase Door scrolls do not necessarily have to be always available. In
>my mind, the only items that are essential for play are the following:
>Scroll of Word of Recall
>Potion of Restore Life Levels
>Potion of Cure Critical Wounds
>Potion of Restore [statistic]
>Spellbooks
>
Also some form of food - I just had a very promising warrior come *very*
close
to death because he ran out of food, and when he recalled to town he
discovered there was no food in the general store and no satisfy hunger at
the
alchemists. I had to survive off potions of cure light wounds while waiting
in
50' for the stores to restock.

This is an extreme situation, of course, but no reason for it ever to occur.

Similarly, flasks of oil for lanterns, potions of cure light/serious wounds
for beginning characters who don't need/can't afford CCW yet, and the basic
ammo types for all 3 shooters (pebbles, arrows, bolts) should IMO be made
permanent fixtures of the town.

>These are the only items that I townscum for.
>

Yes, but, from what I know of you from other posts, you're a very
experienced
player who tends to run through the early game. That's not the only kind of
player to take into consideration.

Eytan

Chris Kern's profile photo
Chris Kern
unread,
May 5, 2001, 4:59:50 PM
to
On Sat, 5 May 2001 12:27:38 -0400, Eytan Zweig
<eyt...@MailAndNews.com> posted the following:
>>===== Original Message From ke...@grinnell.edu (Chris Kern) =====

>>These are the only items that I townscum for.


>>
>
>Yes, but, from what I know of you from other posts, you're a very
>experienced
>player who tends to run through the early game. That's not the only kind of
>player to take into consideration.

You're right, I didn't consider that. I didn't list ammo because I
hardly ever use missile weapons :-) But I agree that food, oil, and
missiles should be guaranteed as well.

-Chris

Johan Kullstam's profile photo
Johan Kullstam
unread,
May 5, 2001, 7:17:33 PM
to
ke...@grinnell.edu (Chris Kern) writes:
> On Sat, 5 May 2001 11:44:27 +0200, "Robert Ruehlmann"
> <r...@angband.org> posted the following:
>
> >Sounds like a good idea. I used to think that no type of item should be
> >always available at the stores to give players an extra challenge from time
> >to time (like playing without phase door scrolls for a while). But town
> >scumming is just too easy for this to have any effect.
>
> Phase Door scrolls do not necessarily have to be always available. In
> my mind, the only items that are essential for play are the following:
> Scroll of Word of Recall
> Potion of Restore Life Levels
> Potion of Cure Critical Wounds
> Potion of Restore [statistic]
> Spellbooks
>
> These are the only items that I townscum for.

if you play warrior or rogue then add bolts (or arrows) to this list.
fortunately you can get them in both 1 and 3 shops.

> In addition, at the beginning of the game it's nice to have a Lantern,
> and armor your character can actually afford.

i've always been able to find a robe or soft leather. in the small
armors, you can most always find at least 2 of 3 of mitten, shoe, or
hat.

> A bookstore would not
> be a bad addition as well.
>
> I do not think that Potions of Speed should be guaranteed. I also
> don't think that Scrolls of *Identify* should be guaranteed, except I
> do think they should show up in shop 5 as regular items. (I also
> wouldn't mind seeing Scrolls of Teleport and Scrolls of Teleport Level
> generated in shop 5, but that might be too much, I'm not sure.)

scroll of teleport might be too powerful.

i think a healer service would a nice addition. you could restore a
stat or exp. maybe on an individual basis rather than all in one go
as in Z. i'd also like to see an enchanter shop. prices could be
high to prevent abuse by lower level players.

--
J o h a n K u l l s t a m
[kull...@ne.mediaone.net]
Don't Fear the Penguin!

Johan Kullstam's profile photo
Johan Kullstam
unread,
May 5, 2001, 7:22:42 PM
to
ke...@grinnell.edu (Chris Kern) writes:
> On Fri, 04 May 2001 01:36:14 GMT, inv...@erehwon.invalid (Graaagh the
> Mighty) posted the following:
>
>
> >SS -- The game is well-nigh unwinnable without good starting stats,
>
> Ridiculous! Reaching stat gain can be done with very poor starting
> stats. I have no doubts that I could get a mage to stat gain with no
> abilities over 17.

didn't someone a few years back hack a feature to auto-roll with stat
maximum (as opposed to minimum)?

> >F -- In plain Angband it's well-nigh impossible to play a pure
> > spellcaster and win. Someone did it with a mage *once*.
> > With priests I doubt it's ever been done.
>
> Priests have excellent attack spells. Between Annihiliation, Orb of
> Draining, Dispel Evil, and Banishment, I'm sure it's been done by
> somebody.

priests have the best attack spells of the game. i would think that
it would have to be a priest.

Graaagh the Mighty's profile photo
Graaagh the Mighty
unread,
May 5, 2001, 9:08:37 PM
to
On Fri, 04 May 2001 11:14:05 +0200, Matthias Kurzke <maw...@gmx.de>

sat on a tribble, which squeaked:
>All of this is nigh-impossible to get in a roguelike ASCII world. How many shades of light do you want to exist?

Firstly, who said anything about true ASCII? ASCII tiles or, God
forbid, actual graphics are options to consider.

Secondly, we could have a way for the player to check (using the UI)
the actual light level, and represent on-screen just two general
states: enough light to see that square, or not enough. (This could
even depend on PC's stats/items.) Three or four states could be
managed if colors were allocated and used sensibly, as the basic VGA
color palette that is more or less universally available (and that
Angband uses) has "dark" and "light" versions of every hue it has, as
well as four unsaturated colors -- white, pale grey, darker grey, and
black. Black could be used for too-dark areas, the darker set of hues
in dim light, and the brighter set of hues in bright light. Things
with their own glow might be white, with the greys used for grey
things in dim or bright light. Alternatively, some things might be
white in bright light and light grey in dim light, and some (dark)
things dark grey in bright light and black in dim light, rendering
them perhaps dangerously undetectable in dim light. To make it even
more interesting, an even dimmer light where you can't get as much
information or detail could be simulated using nothing but the greys
and black...

Graaagh the Mighty's profile photo
Graaagh the Mighty
unread,
May 5, 2001, 9:13:09 PM
to
On Fri, 04 May 2001 23:55:57 GMT, Mårten Woxberg
<ma...@telia.junk.com> sat on a tribble, which squeaked:
>I just wanted to say that I'm all for a little more
>RPGing in Angband.. but don't make it into a Final Fantasy game..

Agreed. Monsters that don't chase you are, well, boring. :-)

Graaagh the Mighty's profile photo
Graaagh the Mighty
unread,
May 5, 2001, 10:56:56 PM
to
On Sat, 05 May 2001 14:38:14 GMT, ke...@grinnell.edu (Chris Kern) sat

on a tribble, which squeaked:
>Potion of Restore [statistic]

For [statistic] in {STR, DEX, INT, WIS, CON}.

>Spellbooks
>
>These are the only items that I townscum for.

When I townscum, it's often for stuff you didn't list:
* Speed potions
* Teleport scrolls
* Satisfy hunger scrolls

Making speed potions readily available in huge numbers isn't so good
IMO. Make them a bit more likely than currently to turn up in the
dungeon, and therefore in the BM, but don't guarantee them.

>In addition, at the beginning of the game it's nice to have a Lantern,
>and armor your character can actually afford. A bookstore would not
>be a bad addition as well.

The general store should guarantee a lantern, torches, diggers,
cloaks, and food; the armor store should guarantee gloves, boots other
than metal, armor that's soft leather armor or lighter, caps lighter
than helmets, and such -- unenchanted too, so affordable.

>I do not think that Potions of Speed should be guaranteed. I also
>don't think that Scrolls of *Identify* should be guaranteed, except I
>do think they should show up in shop 5 as regular items.

If I could choose between making teleportation or *id* appear in shop
5 I'd take teleportation in a heartbeat. *id* should be BM/dungeon
item, just a tad less rare. Teleportation should be regular shop 5
item and also a tad less rare. Note that [O] has teleport scrolls
appear consistently in shop 5, as well as having a bookstore.

Julian Day's profile photo
Julian Day
unread,
May 6, 2001, 12:44:00 PM
to
On Mon, 30 Apr 2001 23:17:38 GMT, Scott Baxter <scott....@sympatico.ca>
wrote:
>A Java roguelike would be cool to try (wasn't ADOM going to do this at
>some point?), but I wouldn't expect it run as quickly as any *band.

There's a game called Tyrant coded purely in Java:

http://www.mikera.net/tyrant

It's not nearly as complex as ADOM, Angband, etc., but it's still a fun
little game, and the author has done some very good work with regards to
things like landscape-generation.
--
Julian Day <ac...@sfn.saskatoon.sk.ca>
http://www.sfn.saskatoon.sk.ca/~ac881

Art Mruczek's profile photo
Art Mruczek
unread,
May 6, 2001, 5:51:36 PM
to
On Sun, 06 May 2001 02:56:56 GMT, inv...@erehwon.invalid (Graaagh the Mighty)
wrote:
>On Sat, 05 May 2001 14:38:14 GMT, ke...@grinnell.edu (Chris Kern) sat
>on a tribble, which squeaked:

>>In addition, at the beginning of the game it's nice to have a Lantern,
<obvious snippage> ^^^^^^^

>The general store should guarantee a lantern, torches, diggers,

<and more snippage> ^^^^^^^

I tend to disagree. Just as a bit of background, I've been playing
since Moria, and remember fondly the days when there was *no* artifact
light source at all. Lanterns were the best you got, and you *had*
to save an inventory slot for oil. It wasn't so bad, really, despite
what some more recent folks have said about the game being "impossible"
without the Phial. Oil is light, it was only one less inventory slot
that you couldn't use for hauling treasure, and it makes a reasonably
useful thrown weapon, especially for low level characters.

Even now, though one of my first purchases is usually a lantern, if it
isn't available, I don't sweat it. The native depth of a lantern is
level 3, and they're common as dirt in the early dungeon levels.

But making a lantern guaranteed effectively removes any usefulness for
torches whatsoever. I can't imagine anyone *not* buying a lantern if
it were available, and once you have one, you never go back to torches.
Guaranteeing a lantern in the general store simply makes torches one
more "broken stick" you can find in the dungeon.

Personally, I'm of Eytan's school when it comes to dungeon items:
if it has no use whatsoever, it shouldn't be in k_info.txt. Heck,
even a broken dagger can be useful once in a while (it's light, and
who knows, it might turn out to be the HA that is the only source of
see invisible you have for a while). But once you have a lantern,
torches go on the autosquelch list. :-)

Only in silence the word,
Only in dark the light,
Only in dying life,
Bright the hawk's flight on the empty sky.

Mårten Woxberg's profile photo
Mårten Woxberg
unread,
May 6, 2001, 6:40:51 PM
to
On Sun, 06 May 2001 01:13:09 GMT, inv...@erehwon.invalid (Graaagh the
Mighty) wrote:
>On Fri, 04 May 2001 23:55:57 GMT, Mårten Woxberg
><ma...@telia.junk.com> sat on a tribble, which squeaked:
>
>>I just wanted to say that I'm all for a little more
>>RPGing in Angband.. but don't make it into a Final Fantasy game..
>
>Agreed. Monsters that don't chase you are, well, boring. :-)

You obviously haven't played Final Fantasy 8 :)

There's a robot about a quarter in on the first disc
that chases you!!! really cool.. I ran for my life the first
time.. and the CG movies just rocks..

I have to do one or two for Angband someday..

/Mårten

Chris Kern's profile photo
Chris Kern
unread,
May 6, 2001, 6:43:30 PM
to
On Sun, 06 May 2001 21:51:36 GMT, amruczek@*REMOVE*stny.rr.com (Art
Mruczek) posted the following:

^^^^^^^
>
>I tend to disagree. Just as a bit of background, I've been playing
>since Moria, and remember fondly the days when there was *no* artifact
>light source at all. Lanterns were the best you got, and you *had*
>to save an inventory slot for oil.
Yes, but Angband is not Moria. Remember that in Moria the lantern did
not provide 2 squares of viewing radius. And this is a total
non-sequitur. "It was good enough for us in Moria" is not a valid
argument when trying to decide what goes into Angband.

>Even now, though one of my first purchases is usually a lantern, if it
>isn't available, I don't sweat it. The native depth of a lantern is
>level 3, and they're common as dirt in the early dungeon levels.

The extra square of view can mean the difference between life and
death in the early levels.

>But making a lantern guaranteed effectively removes any usefulness for
>torches whatsoever.

Torches are stupid anyway, they should not even exist in the game they
way things are. Either Lanterns should be so expensive/rare that you
are forced to use torches for a while, or there should be some other
advantage to torches. Making people use torches sometimes because
shop 1 has no lanterns is a dumb restriction on gameplay.

-Chris

Joseph William Dixon's profile photo
Joseph William Dixon
unread,
May 6, 2001, 8:25:51 PM
to
On Sun, 6 May 2001, Chris Kern wrote:
> Torches are stupid anyway, they should not even exist in the game they
> way things are. Either Lanterns should be so expensive/rare that you
> are forced to use torches for a while, or there should be some other
> advantage to torches. Making people use torches sometimes because
> shop 1 has no lanterns is a dumb restriction on gameplay.
Just like it's a dumb restriction on reality that you have to use a
flashlight or candles during a power-outage because the stores had no
kerosene ('storm') lanterns when you needed/wanted one.

--
"...there are hardly any excesses of the most crazed psychopath that cannot
easily be duplicated by a normal, kindly family man who just comes into
work every day and has a job to do." [Terry Pratchett, "Small Gods"]
http://www.chebucto.ns.ca/~aa343/index.html

Graaagh the Mighty's profile photo
Graaagh the Mighty
unread,
May 6, 2001, 11:39:04 PM
to
On Sun, 6 May 2001 21:25:51 -0300, Joseph William Dixon
<aa...@chebucto.ns.ca> sat on a tribble, which squeaked:
> Just like it's a dumb restriction on reality that you have to use a
>flashlight or candles during a power-outage because the stores had no
>kerosene ('storm') lanterns when you needed/wanted one.

Tell me, Mr. Dixon, have *you* fought a pack of ravening Cave Spiders
or one of the Maggothounds during a power outage using a flashlight as
your light source?

Chris Kern's profile photo
Chris Kern
unread,
May 6, 2001, 11:48:35 PM
to
On Sun, 6 May 2001 21:25:51 -0300, Joseph William Dixon
<aa...@chebucto.ns.ca> posted the following:
>On Sun, 6 May 2001, Chris Kern wrote:
>> Torches are stupid anyway, they should not even exist in the game they
>> way things are. Either Lanterns should be so expensive/rare that you
>> are forced to use torches for a while, or there should be some other
>> advantage to torches. Making people use torches sometimes because
>> shop 1 has no lanterns is a dumb restriction on gameplay.
>
> Just like it's a dumb restriction on reality that you have to use a
>flashlight or candles during a power-outage because the stores had no
>kerosene ('storm') lanterns when you needed/wanted one.

Angband is not reality, nor should it be.

-Chris

Matthias Kurzke's profile photo
Matthias Kurzke
unread,
May 7, 2001, 2:05:08 AM
to
On Sun, 06 May 2001 22:43:30 GMT, ke...@grinnell.edu (Chris Kern)
wrote:
If a lantern cost 100 gold for my starting characters, I couldn't buy
one. (I use point-based and only have 100 AU, and that is mostly for
armor (and a whip if it's a warrior or rogue).) Even as it is, I can't
buy one on first trip since it's too expensive -- and they're really
easily found. Getting good radius 2 light and fuelling it is already
TOO EASY in Angband - no reason to make it EVEN EASIER by guaranteeing
items to appear. Great about Angband is that nothing, NOTHING is
guaranteed, everything is RANDOM, except for Sauron, Morgoth, the
Massive Iron Crown and Grond. I don't want to give this up in the
shops or anywhere. Call me a traditionalist -- I am one, maybe...

Matthias

Timo Pietilä's profile photo
Timo Pietilä
unread,
May 7, 2001, 4:26:26 AM
to
In that context it means that pure spellcaster doesn't play as warrior
but rely on spells and magical means (potions, wands, scrolls etc.). It
doesn't mean that spellcaster *cannot* use melee or *should* not use
melee.

In other words pure spellcaster means that mage should play as mage and
priest as priest, nothing more.

Timo Pietilä

--
A(2.9.2) C "Wanderer" DP L:22 DL:600' A-- R--- !Sp w:LxBow(+9,+9)
A/Gu L/W/D H+ D c-- f PV+ s-(+) TT- d(+) P++ M+
C-- S+ I-(++) So+ B++ ac GHB- SQ RQ++ V+ F:Z Rod Stacking

Chris Kern's profile photo
Chris Kern
unread,
May 7, 2001, 10:04:36 AM
to
On Mon, 07 May 2001 06:05:08 GMT, mku...@gmx.de (Matthias Kurzke)
posted the following:
>If a lantern cost 100 gold for my starting characters, I couldn't buy
>one. (I use point-based and only have 100 AU, and that is mostly for
>armor (and a whip if it's a warrior or rogue).) Even as it is, I can't
>buy one on first trip since it's too expensive -- and they're really
>easily found. Getting good radius 2 light and fuelling it is already
>TOO EASY in Angband - no reason to make it EVEN EASIER by guaranteeing
>items to appear.

But you can just suicide and get a new character where lanterns will
hopefully appear. It doesn't make sense from a realistic viewpoint or
a gameplay standpoint to have basic items denied to you by the
shopkeepers.

(Couldn't get their shipments in maybe? "I know there's no door in
the town, we've been hounding mayor Maggot about that, but he just
likes whining around...just leave the lanterns outside and I'll climb
over the wall and get them")

-Chris

Kieron Dunbar's profile photo
Kieron Dunbar
unread,
May 7, 2001, 2:29:13 PM
to
Once upon a time, Graaagh the Mighty wrote thus:
> On Wed, 2 May 2001 18:37:30 -0400, Matthew K Lahut
> <mla...@andrew.cmu.edu> sat on a tribble, which squeaked:
> bad. Angband has id too easy. ADOM has it hard enough in early game
> but has converse problem. You can seriously screw yourself with cursed
> stuff, the IBM Guild Manual, ...

You can't do it if you don't try unidentified stuff too much. If you're
playing a literate character, you'll get your entire pack identified before
too long, so why annoy your god in the meantime? If, as a general rule, you
make your way over to the CoC once you've killed 500 monsters, you should find
that your opportunities to mess your game up are that much more limited.

> Kill 30 of <random>, etc.
> Roleplay my foot. Kill 30 of them *why*? How does this unbar your
> passage -- does one of them carry a key? All pieces of the key to

How does one of them having a key (which just happens to fit the lock on every
set of stairs leading down from this depth) give any more roleplaying than
having the stairs magically appear when you kill the last one?

>>> W -- indicates a wilderness. (Desirable.)
>>Again, tastes vary. Many games work fine without a wilderness, and would
>>be harmed by the insertion of one.
> Perhaps. A game set entirely in caves for example. But the trick

For me the question is not whether the notion of a wilderness can be added to
the game universe, but what would be added to the game by creating such a
wilderness. You could, if you wanted, add a wilderness to Angband in about
five minutes. This wilderness might have no other towns, no other dungeons or
caves, no hills, no mountains, no streams, no trees, no monsters, not even a
blade of grass or a cute bunny rabbit to nibble on it. It would still be a
wilderness, but it would add absolutely nothing to the game. As such, it would
not be desirable, even though it would be a wilderness.

> has the town. A game that starts you in a cave doesn't necessarily
> qualify: unless the entrance you know of collapsed behind you, what's
> to stop you leaving? A heavy-handed "you just can't"? It is possible,

Since we're discussing roguelikes, the answer of "nothing, but you'll never
return if you do." deserves a mention here.

> (Incidentally, it can be argued that *every* game of *every* genre
> except highly abstract ones like chess or card solitaire are role
> playing games. Mario World has you assume the identity of a character

It can be argued that the pack of cards you might play patience with is a role
playing game, but you might get some curious looks if you try. It doesn't have
to fit any notions about not having anything happen within it that can't be
explained in terms of the actions of rational entities. It just has to be able
to be shuffled and dealt in a pseudo-random order. You can call anything a
role-playing game, but you need to find some balance between a definition
which no game fits and a definition which says nothing about those games which
fit it other than that they are games.

And I don't even want to consider whether chess is more of a role-playing game
than minesweeper...

> Bad luck is fine. Game-ending bad luck is questionable at best.

The problem with this is that there's no clear dividing line between bad luck
and bad judgement. Not being well enough equipped to survive a breath from a
dracolich the moment he first steps into the dungeon is reasonable. Being in
the same condition on level 96 probably isn't. Unless you want the boundary
between dracolich-free and dracolich-infested territory to be a clearly
defined one, you have to have a period somewhere between level 1 and level 96
where you might see dracoliches, but will be unlikely to. If dying ends the
game, dying to one during that period would be game-ending bad luck by
definition.

> I speak of the complexity of the character generation process itself,
> and the software interface to it, not the decisions of race/class
> combos or even which stats to train. Contrast *bands with ADOM. The
> latter has a much more streamlined and automated system.

Contrast using the autoroller in Angband with using its equivalent in ADOM. I
know which I'd prefer.

In any case, I think the mechanics of selecting a character are always trivial
compared to the thought that needs to go into selecting a type of character
that fits your needs.

> Nethack's volatility would seem to make long-range planning a
> worthless endeavor in that game. Highly radical changes that totally

As NetHack is a lot more susceptible to long-range planning than Angband (not
only can you predict certain aspects of things you will encounter later, you
can also change them through your actions now), I'm quite curious as to what
you mean by this. If it's just a symptom of not knowing anything about the
game, could you please describe what you mean by "Nethack".

> existence of magic time limits (ADOM has several of these, of which
> the only one that can really be justified is the much-berated 90-day

JOOI, how do you consider the 4-day limit for the cute dog? Both considering
it unjustified and considering it unmagical would be consistant with this
statement, so what do you think?

kwaheri, Kieron (reverse username to reply)

Joseph William Dixon's profile photo
Joseph William Dixon
unread,
May 7, 2001, 5:14:21 PM
to
On Mon, 7 May 2001, Chris Kern wrote:
>
> But you can just suicide and get a new character where lanterns will
> hopefully appear. It doesn't make sense from a realistic viewpoint or
> a gameplay standpoint to have basic items denied to you by the
> shopkeepers.
Lanterns are basic items. Torches are.

Joseph William Dixon's profile photo
Joseph William Dixon
unread,
May 7, 2001, 5:15:11 PM
to
On Mon, 7 May 2001, Joseph William Dixon wrote:
> On Mon, 7 May 2001, Chris Kern wrote:
> > But you can just suicide and get a new character where lanterns will
> > hopefully appear. It doesn't make sense from a realistic viewpoint or
> > a gameplay standpoint to have basic items denied to you by the
> > shopkeepers.
>
> Lanterns are basic items. Torches are.
^^^
"aren't", of course... :)
Art Mruczek's profile photo
Art Mruczek
unread,
May 7, 2001, 5:19:08 PM
to
On Mon, 07 May 2001 14:04:36 GMT, ke...@grinnell.edu (Chris Kern) wrote:
>On Mon, 07 May 2001 06:05:08 GMT, mku...@gmx.de (Matthias Kurzke)
>posted the following:
>
>>If a lantern cost 100 gold for my starting characters, I couldn't buy
>>one. (I use point-based and only have 100 AU, and that is mostly for
>>armor (and a whip if it's a warrior or rogue).) Even as it is, I can't
>>buy one on first trip since it's too expensive -- and they're really
>>easily found. Getting good radius 2 light and fuelling it is already
>>TOO EASY in Angband - no reason to make it EVEN EASIER by guaranteeing
>>items to appear.
>
>But you can just suicide and get a new character where lanterns will
>hopefully appear. It doesn't make sense from a realistic viewpoint or
>a gameplay standpoint to have basic items denied to you by the
>shopkeepers.
>

Now this is a serious, serious scummer: someone who's willing to
ditch a character just because he can't get a lantern before entering
the dungeon. ;-P

But seriously, I think the point that I, at least, want to make, and
I suspect Matthias as well (though I don't want to put words into his
mouth), is that lanterns are *not* basic items. Torches are basic
items. It's pretty iffy to enter the dungeon with no light source,
but a lantern is not necessary. If you really need that radius 2
light source to keep from dying, you should be detecting more.

Chris Kern's profile photo
Chris Kern
unread,
May 8, 2001, 12:23:26 AM
to
On Mon, 07 May 2001 21:19:08 GMT, amruczek@*REMOVE*stny.rr.com (Art
Mruczek) posted the following:
>On Mon, 07 May 2001 14:04:36 GMT, ke...@grinnell.edu (Chris Kern) wrote:


>
>>On Mon, 07 May 2001 06:05:08 GMT, mku...@gmx.de (Matthias Kurzke)
>>posted the following:
>>
>>>If a lantern cost 100 gold for my starting characters, I couldn't buy
>>>one. (I use point-based and only have 100 AU, and that is mostly for
>>>armor (and a whip if it's a warrior or rogue).) Even as it is, I can't
>>>buy one on first trip since it's too expensive -- and they're really
>>>easily found. Getting good radius 2 light and fuelling it is already
>>>TOO EASY in Angband - no reason to make it EVEN EASIER by guaranteeing
>>>items to appear.
>>
>>But you can just suicide and get a new character where lanterns will
>>hopefully appear. It doesn't make sense from a realistic viewpoint or
>>a gameplay standpoint to have basic items denied to you by the
>>shopkeepers.
>>
>Now this is a serious, serious scummer: someone who's willing to
>ditch a character just because he can't get a lantern before entering
>the dungeon. ;-P

Hey now, I don't do that very often :-)

>But seriously, I think the point that I, at least, want to make, and
>I suspect Matthias as well (though I don't want to put words into his
>mouth), is that lanterns are *not* basic items. Torches are basic
>items. It's pretty iffy to enter the dungeon with no light source,
>but a lantern is not necessary. If you really need that radius 2
>light source to keep from dying, you should be detecting more.

The price of lanterns should be increased, then. I don't see why
they're not "basic items" when you can buy them with 90 out of 100
characters.

-Chris

Scott Holder's profile photo
Scott Holder
unread,
May 8, 2001, 5:24:38 PM
to

"Graaagh the Mighty" <inv...@erehwon.invalid> wrote in message
news:3af618b6...@news.primus.ca...

> On Sun, 6 May 2001 21:25:51 -0300, Joseph William Dixon
> <aa...@chebucto.ns.ca> sat on a tribble, which squeaked:
>
> > Just like it's a dumb restriction on reality that you have to use a
> >flashlight or candles during a power-outage because the stores had no
> >kerosene ('storm') lanterns when you needed/wanted one.
>
> Tell me, Mr. Dixon, have *you* fought a pack of ravening Cave Spiders
> or one of the Maggothounds during a power outage using a flashlight as
> your light source?
I played Angband on my laptop in my car out in my driveway using the dome
light during a power outtage, does that count? :) Don't remember if I fought
any Cave Spiders or Maggothounds though...

Scott Holder