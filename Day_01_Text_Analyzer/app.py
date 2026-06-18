# Day 01 Project: Dynamic Inventory & Text Analyzer

print("--- 1. String Manipulation & Analysis ---")
# Raw text to analyze (simulating an messy system input)
raw_item = "   ||snoitulos_latigid_trams||   "

# Clean the string (Modifying)
clean_item = raw_item.strip().strip("|")

# Reverse the string using slicing to fix the backward name (Slicing/Reversing)
corrected_name = clean_item[::-1]
print(f"Original Raw Text: {raw_item}")
print(f"Corrected Name:    {corrected_name}\n")

print("--- 2. List Operations (Update & Delete) ---")
# Initializing an inventory list
inventory = ["Stingo Cookies", "Legacy App", "Cloud Config", "Unity Blueprint"]
print(f"Initial Inventory: {inventory}")

# Update an element
inventory[1] = corrected_name
print(f"After Update (Index 1): {inventory}")

# Delete elements (Using pop and remove)
removed_by_index = inventory.pop(3)  # Removes 'Unity Blueprint'
inventory.remove("Cloud Config")  # Removes by value

print(f"Removed by index: '{removed_by_index}'")
print(f"Final List: {inventory}\n")

print("--- 3. Tuples & System Metadata ---")
# Fixed system settings that shouldn't change (Immutable)
SYSTEM_VERSION = ("v1.0.0", "Production", 2026)
print(f"System Status: {SYSTEM_VERSION[1]} | Year: {SYSTEM_VERSION[2]}")

# Concatenation & Repetition check
success_msg = "[SUCCESS] " + "Project verified! "
print(success_msg * 2)