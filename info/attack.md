# Melee Attack Algorithm

1. a target is determined for the attack. this may be:

   * a collection of body parts (area)
   
   * a specific body part
   
   * a specific weakness (e.g. gap in armor or exposed area on the side). Note that damaged armor will have
     naturally more gaps and exposures to exploit.  A breast plate with a hole or large gash could 
     allow an assassin to put their dagger right through without any protection. This is represented in the game
     as reduced body coverage which decreases with armor damage that attackers may target and exploit.
     
     Finding weak spots is especially true for cunning and seasoned adversaries. They can not only choose
     a weakness, but will select an attack in their arsenal that exploits that weakness.
     
     To find a weakness, the attacker scans the defender sizing up coverage/exposure of body
     parts that are accessible to them and selecting the attack(s) that can hit the most 
     egregious openings. Some attackers will specialize and have bonuses for certain types of 
     targets like neck or head. A defender covered in thick body plate, for example, may lead 
     a savvy dwarf to crush his exposed foot with a hammer.
     
2. The attacker rolls for hitting their target. For small targets, the lightness and design of the
   weapon and lightness of overall weight of equipment increases chance to hit along with 
   familiarity with the weapon, experience, training strength and dexterity.

3. The defender defends

   * Experienced and dexterous defenders will attempt to **avoid** by stepping away or to the side. 
     Trained fighters, thieves and assassins, samorai, get bonuses over other classes.
     
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

    * Any portion of attack that is not deflected is then calculated for **absorbtion**
    
      **Absorbtion** is determined by the equipment blocking the blow. Heavier equipment with
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
      
    For example:
    
        Summary of attack:
        
        A goblin thrusts his spear at a novice fighter. The spear rips through his shield and
        jack-of-plate doublet hitting the novice's torso and causing 5 points damage.
        
        That's the short summary; the game engine generated a more detailed account:
    
        A goblin thrusts a spear at a novice fighter. The fighter could not move enough avoid the thrust but
        does manage to move his light-weight wood/leather shield up to block. 
        The block has a poor deflection and 95% of the thrust is delivered to the shield and 
        penetrates clean through. The shield absorbs only 15% of the thrust.
        The remaining 80% of the thrust strikes the fighter's jack-of-plate doublet. 
        The doublet does not deflect the blow.  The spear hit lands between metal plates in the 
        doublet which absorbs only 10% of the thrust as the spear penetrates through wounding
        the fighter who takes 70% of the damage (5 points).
        
        The novice's shield and doublet take piercing damage and are now slightly less effective.
       
5. If the defender's **block** fails, the attacker may score a hit directly on the defender.

    For Example:
    
        Summary of attack:
        
        A goblin thrusts his spear at a novice fighter. The novice fails to raise his
        shield in time and the thrust rips through his jack-of-plate doublet into his torso causing
        8 points damage.
        
        That's the short summary; the game engine generated a more detailed account:
    
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