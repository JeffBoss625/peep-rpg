# Peep-RPG
## Requirements to Run Peep-RPG
- Python 3 installed on terminal
- Any computer with a terminal available for use
## How to run Peep-RPG
- gitclone
- cd into directory
- Command “python peep-rpg”

## Classes and Abilities

## World Building
## Monsters and AI


## Sleep Cycles
Sleep cycles are implemented for the monsters to simulate real life sleeping patterns. The cycle that was used to model this is the 4 stage REM sleep cycle. This is used to make a calculation on how easily a monster will wake up due to noise: In the deeper stages of sleep like REM and NREM 3 the monster will respond less to sound and will not get up until a large amount of noise is made. However, when the monster is in NREM 1 and NREM 2, they will be easily awakened by any sound that the player makes. To demonstrate this idea here I graphed out the function for calculating the “deepness” of sleep:
![sleep_cycles](sleepcycles.png)
Here is a part of the function for getting this result (more found in ____.py):
```
def handle_sound(time, sleep):
   time_passed = time - sleep.age_checked
   sleep.age_checked = time
   rem = sleep.limit
   n3 = 0.8 * sleep.limit
   n2 = 0.5 * sleep.limit
   n1 = 0.2 * sleep.limit
   if sleep.total_cycles >= sleep.cycle_target:
       sleep.target = 0
       sleep.sleepiness -= 0.025 * time_passed * ((sleep.cycles * 0.1) + 1)
       if sleep.sleepiness <= sleep.target:
           sleep.sleepiness = sleep.target
           return time, sleep.sleepiness...  

            ...

            sleep.timer[1] = 20 * (1 - (sleep.cycles * 0.15))
           elif sleep.target == n2:
               sleep.timer[1] = 25 * (1 + (sleep.cycles * 0.05))
           else:
               sleep.timer[1] = 5
   else:
       sleep.timer[1] -= time_passed
   return time, sleep.sleepiness
```
## Physics
One of the key aspects of peep-rpg is the use of physics models and calculations to simulate interactions in the dungeon.
### Light and Sound
Inverse Square Law Equation: k/x
This equation helps represent the dissipation of light and sound within the dungeon by having x equal to the distance away from source of the light or sound, and k be the coefficient that will represent how quickly the sound/light dissipates. In the case of peep-rpg, light dissipates faster than sound because the dungeon echos sound. To represent this, the coefficient k is greater for sound than it is for light. 


```
def brightness_at(lightsources, pos):
   pos_x = pos[0]
   pos_y = pos[1]
   brightness = []
   for light in lightsources:
       distance_x = abs(light.pos[0] - pos_x)
       distance_y = abs(light.pos[1] - pos_y)
       tot_distance = sqrt(distance_x ** 2 + distance_y ** 2)
       if tot_distance == 0:
           brightness.append(light.brightness)
       else:
           brightness.append(light.brightness / (tot_distance ** 2))
```


Light determines how far or what the player is able to see in the dungeon:
Ssc of light in a dungeon
Sound is in early implementation. Its only function is for waking monsters from their natural sleep cycles. The future idea for sound is to develop the AI of monsters to track the sounds that the player makes throughout the dungeon until the player is in sight.

### Items
Items play a large role in this game because of how physics is utilized in calculations. There are many variables that go into these calculations that are shown below:
```
class Layer:
   elasticity: float = 1.0
   thickness: float = 1.0
   area: float = 1.0
   breaking_pt: float = 1.0
   plastic_region: float = 1.0
   toughness: float = 1.0
   hardness: float = 1.0
   durability: float = 1.0


class Strike:
   velocity: float = 1.0
   area: float = 1.0
   mass: float = 1.0

pierceable
f_per_cm = ((strike.mass*(strike.velocity**2))/2)/strike.area
print(f'f_per_cm: {f_per_cm}')
print(f'piercable: {layer.breaking_pt*(layer.hardness**2)}')
if f_per_cm > layer.breaking_pt * (layer.hardness ** 2):
   return "pierce"
return "stop"

def apply_pierce(strike, layer, f_per_cm):
   strike.velocity = (strike.velocity*(strike.mass*100)-(layer.toughness*strike.velocity) / (1 / layer.thickness))
   strike.velocity = max(0, strike.velocity)
   layer.durability -= .02
   return strike, layer
```
Then this force is converted into damage 

*Note that some creatures and monsters that have thicker or unique skin will have their skin added in as an extra layer of armor in calculations.**
