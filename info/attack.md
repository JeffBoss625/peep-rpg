# Melee Attack Algorithm

1. a target is determined for the attack. this may be:

   * a collection of body parts (area)
   
   * a specific body part
   
   * a specific weakness (e.g. gap in armor or exposed area on the side). Note that damaged armor will have
     naturally more gaps and exposures to exploit.  A breast plate with a hole or large gash could 
     allow an assassin to put their dagger right through without any protection. This is represented in the game
     as reduced body coverage which decreases with armor damage.
     
     Penalties for Armor damage are amplified by attacker cunning and experience. Seasoned adversaries 
     may scan the defenders entire body for damaged and exposed areas matching weak spots against
     attacks in their arsenal that exploit those weaknesses, such as a piercing attack aimed at a 
     hole in a damaged breastplate. However, arrogant adversaries (unwise) may go too far with this approach, 
     aiming for small openings that are beyond their skill ratio and unlikely to hit
     because they underestimate the opponent's agility and skill relative to their own own.
     
     To find a weakness, the attacker scans the defender sizing up coverage/exposure of body
     parts that are accessible to them and selecting the attack(s) that can hit the most 
     egregious openings. Some attackers will specialize and have bonuses for certain types of 
     targets like neck or head. A defender covered in thick body plate, for example, may lead 
     a savvy dwarf to crush his exposed foot with a hammer.
     
2. The attacker rolls for hitting their target. For small targets, the lightness and design of the
   weapon and lightness of overall weight of weapon increases chance to hit along with 
   familiarity with the weapon, experience, training, strength and dexterity. Attacker
   advantages are compared with defender experience, agility, weight, class and so on to 
   determine chance of hit.  Trained fighters, thieves and assassins, samorai, get evade/dodge bonuses 
   over other classes.

3. The defender defends

   * If the attack cannot be avoided, the defender will attempt to **block** with shield, 
     bracers, or weapon. The lightness of the 
     item used to deflect along with experience blocking with the item and defender's class
     dexterity and experience will increase odds.
   
4. If a defender's **block** succeeds, a determination is made for **deflection**. Deflection is the 
   successful redirecting of the attack away from equipment and defender resulting in
   less damage.
   
    * A highly successful **deflection** redirects most of the attack away from the defender and 
      his or her equipment. Success depends again on class, dexterity, and experience, but also
      the material used to deflect and the type and weight of the attack. Hard smooth materials 
      such as titanium plate have 
      higher deflection rates. At the same time, heavy blows with a hammer are much harder to deflect.
      Partial deflection can be thought of as redirecting much, but not all, of the damage away from vital
      or sensitive areas of the body.

    * Any portion of attack that is not deflected is then calculated for **penetration** 
    
      Penetration is determined by the type of material, the type of attack and the type and
      weight of weapon and power of the attack. Pierce attacks with heavy pointed weapons
      are more effective penetrating chainmail, for example, than slash attacks on chainmail.
      
      An attack that successfully penetrates equipment looses some power due to **absorbtion**
      of the equipment taking the hit.
    
      Failed armor penetration from piercing and slashing attacks result in a conversion 
      of the attack power to crushing attack applied against subsequent layers.
      
      **Absorbtion** is determined by the type of blocking the blow. Heavier equipment with
      hard material will absorb more than light soft material. The best equipment will absorb
      a large amount of power even from a heavy strike without sustaining noticable damage. But powerful
      hits from heavy weapons will damage most normal equipment. Type and thickness of **material**,
      weapon and type of attack (pierce, slash, crush, fire, ...), as well as **construction**
      factors will determine how much power 
      is absorbed, 
      how much passes through and how much **damage** is done to the equipment that absorbed the
      blow. Slashing weapons do more damage to leather and cloth than crushing weapons, for example.
      Thick felt can absorb some damage from heavy crushing attacks, and so on.
      
      For blocks, the portion of damage and force that penetrates the item may hit underlying layers of 
      protection such as an arming doublet undershirt which in turn may absorb some damage before 
      the remaining power of the attack then affects the defender.
      
   Example: A blocked, but penetrating attack:


        A goblin thrusts his spear at a novice fighter. The spear rips through his shield and
        jack-of-plate doublet hitting the novice's torso and causing 5 points damage.
        
        Details:
    
        A goblin thrusts a spear at a novice fighter. The fighter could not move enough avoid the thrust but
        does manage to move his light-weight wood/leather shield up to block. 
        The block has a poor deflection and 95% of the thrust is delivered to the shield and 
        penetrates clean through. The shield absorbs only 15% of the thrust.
        The remaining 80% of the thrust strikes the fighter's jack-of-plate doublet. 
        The doublet does not deflect the blow.  The spear hit lands between metal plates in the 
        doublet which absorbs only 10% of the thrust as the spear penetrates through wounding
        the fighter who takes 70% of the damage (5 points).
        
        The novice's shield and doublet take piercing damage and are now slightly less effective.
       
   Example: A blocked attack:
   
           A goblin thrusts his spear at a novice fighter. The spear glances heavily off his shield
           doing 1 damage to his arm.
           
           
           Details:
       
           A goblin thrusts a spear at a novice fighter. The fighter could not move 
           enough avoid the thrust but
           does manage to move his light-weight wood/leather shield up to block. 
           The block has a decent deflection and 65% of the thrust glances off, while 35% 
           crushing damage is delivered into the fighter's block. 
           The shield absorbs 25% of the crushing power from the thrust, leaving 10%
           power delivered through to the novice's arm and side for 1 damage.
           
           The novice's shield is lightly marked from the blow.
               

5. If the defender's **block** fails, the attacker may score a hit directly on the defender.

        Summary of attack:
        
        A goblin thrusts his spear at a novice fighter. The novice fails to raise his
        shield in time and the thrust rips through his jack-of-plate doublet into his torso causing
        8 points damage.
        
        Details:
    
        A goblin thrusts a spear at a novice fighter. The fighter could not move enough avoid the 
        thrust he also fails to raise his light-weight wood/leather shield up to block. 
        The remaining thrust strikes the fighter's jack-of-plate doublet. 
        The doublet does not deflect the blow.  The spear hit lands between metal plates in the 
        doublet which absorbs only 10% of the thrust as the spear penetrates through wounding
        the fighter who takes 90% of the damage (8 points).
        
        The novice's doublet takes piercing damage and are now slightly less effective.
    
    ... or the attack may be **deflected** by the underlying equipment, glancing off a titanium chestplate
    for example. Again, experience, strength, class and material play a role in chance and 
    amount of deflection.
    
6. Slashing and Piercing attacks that land and fail to penetrate armor are converted to crush attack 
   damage on lower layers. For this reason, cushion under-armor can be effective.
   
       A goblin thrusts his spear at a novice fighter. The spear knocks hard against his jack-of-plate
       doublet bruising him for 2 damage.
       
       
       Details:
   
        A goblin thrusts a spear at a novice fighter. The fighter could not move enough avoid the 
        thrust he also fails to raise his light-weight wood/leather shield up to block. 
        The spear thrust strikes the fighter's jack-of-plate doublet. 
        The doublet does not deflect the blow.  The spear rams into a metal plate in the 
        doublet and does not penetrate the armor. 60% of the thrust is absorbed by the
        doublet and 20% by the underlying quilted padding. The remaining force jams into the fighter's
        torso causing a nasty bruise (2 points)
        
        The novice's doublet takes minor damage.
