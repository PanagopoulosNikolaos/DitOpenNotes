/*
 * Exercise 13: Game Character System
 * 
 * Create an abstract base class Character with:
 * - Protected members: name (string), health (int), level (int)
 * - Constructor initializing all members
 * - Pure virtual methods attack(), defend(), and specialAbility()
 * - Virtual method displayInfo()
 * - Virtual destructor
 * 
 * Create two derived classes:
 * - Warrior: additional members strength (int), weaponType (string); 
 *   implement all virtual methods with warrior-specific behavior
 * - Mage: additional members mana (int), spellType (string); 
 *   implement all virtual methods with mage-specific behavior
 * 
 * Create a PlayerParty class with:
 * - Private member: characters (vector of Character pointers)
 * - Method addCharacter(Character*) to add warriors or mages
 * - Method battle(Character* enemy) where all party members attack the enemy
 * - Method healParty() restoring health to all members
 * - Method displayParty() showing all characters
 * - Destructor freeing all memory
 * 
 * In main(), create a party with 2 warriors and 3 mages from user input, 
 * display party, simulate a battle with an enemy (created similarly), 
 * show healing after battle, and ensure proper cleanup.
 */

#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    // Your code here
    
    return 0;
}
