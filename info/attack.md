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

   * Experienced and dexterous defenders will attempt to avoid by stepping away or to the side. 
     Trained fighters, thieves and assassins, samorai, get bonuses over other classes.
     
   * If that is not enough, the defender will attempt to deflect with shield or weapon. The weight of the 
     item used to block along with experience blocking with the item will increase odds
   
4. If a defender's block succeeds, a determination is made if it is a **deflection** or a **block**.
    
    * A **deflection** causes little damage to the defender and the defender's equipment. 
    
    * A **block** will result in a hit to the equipment with **absorbtion** of the item and **damage** to
      equipment determined by the
      type of the attack (pierce, slash, crush, fire, ...), the material/construction of the equipment, and
      the amount of partial deflection that was achieved. A blow may be partially or mostly deflected
      if the deflection roll was high reducing damage to equipment and defender.
      
      For blocks, the portion of damage and force that penetrates the item may hit underlying layers of 
      protection such as an arming doublet undershirt. That item may absorb and take some damage before 
      the damage then affects the defender.
      
    For example:
    
        Summary of attack:
        
        A goblin thrusts his spear at a novice fighter. The spear rips through his shield and
        jack-of-plate doublet hitting the novice's torso and causing 5 points damage.
        
        That's the short summary, in fact, the game engine generated a more detailed account:
    
        A goblin thrusts a spear at a novice fighter. The fighter could not move enough avoid the thrust but
        does manage to move his light-weight wood/leather shield up to block. 
        The block has a poor deflection and 95% of the thrust is delivered to the shield and 
        penetrates clean through. The shield absorbs only 15% of the thrust.
        The remaining 80% of the thrust strikes through to the fighter's jack-of-plate doublet. 
        This thrust penetrates between plates in the doublet which absorbs only 10% of the thrust and so 
        70% of that thrust damages the fighter.
        
        The novice's shield and doublet take piercing damage and are now slightly less effective.
       
5. 