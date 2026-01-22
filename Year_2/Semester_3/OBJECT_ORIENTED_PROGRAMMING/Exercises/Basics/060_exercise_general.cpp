/*
 * Exercise 15: Inventory Management System
 * 
 * Create a base class Item with:
 * - Protected members: itemId (string), itemName (string), price (double), quantity (int)
 * - Constructor initializing all members
 * - Pure virtual methods: calculateTotalValue(), applyDiscount(double percent)
 * - Virtual method displayInfo()
 * - Virtual destructor
 * 
 * Create three derived classes:
 * - Electronics: additional members warrantyMonths (int), brand (string); 
 *   implement virtual methods with electronics-specific behavior
 * - Clothing: additional members size (string), material (string); 
 *   implement virtual methods with clothing-specific behavior
 * - Food: additional members expirationDate (string), isPerishable (bool); 
 *   implement virtual methods with food-specific behavior (discount for perishables near expiry)
 * 
 * Create an Inventory class with:
 * - Private member: items (vector of Item pointers)
 * - Method addItem(Item*) to add any type of item
 * - Method removeItem(string itemId) returning bool for success
 * - Method findItem(string itemId) returning Item pointer or nullptr
 * - Method calculateTotalInventoryValue() summing all items
 * - Method displayInventory() showing all items polymorphically
 * - Method applySeasonalDiscount(double percent) to all items
 * - Destructor freeing all memory
 * 
 * In main(), create an inventory with 2 of each item type from user input, 
 * display inventory, calculate total value, apply discounts to specific items, 
 * find and modify specific items, display updated inventory, and ensure proper cleanup.
 */

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    // Your code here
    
    return 0;
}
