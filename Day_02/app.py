# Day 02 Project: Smart Access Control & Profile Manager

print("--- 1. Dictionary & System Profiles ---")
# User profile storage using Key-Value pairs
user_profile = {
    "username": "Pestingo",
    "role": "Developer",
    "tier": "Premium",
    "login_count": 42
}
print(f"Current User Profile: {user_profile}")

# Updating dictionary elements
user_profile["login_count"] += 1
user_profile["status"] = "Active"
print(f"Updated Profile: {user_profile}\n")


print("--- 2. Conditional Logic (if-elif-else) ---")
# Determining feature access based on user tier
user_tier = user_profile["tier"]

if user_tier == "Admin":
    print("🔓 Access Granted: Full System Root Access.")
elif user_tier == "Premium":
    print("✨ Access Granted: Premium features unlocked, no restrictions.")
elif user_tier == "Standard":
    print("👍 Access Granted: Standard dashboard features enabled.")
else:
    print("⚠️ Access Denied: Please upgrade your subscription tier.")
print()


print("--- 3. Sets & Set Operations ---")
# Managing unique system security tokens/tags
required_clearance = {"auth_token", "secure_shell", "encryption_key"}
user_hardware_tags = {"secure_shell", "legacy_token", "biometric_id"}

print(f"Required Clearance Tags: {required_clearance}")
print(f"User Hardware Tags:       {user_hardware_tags}")

# 1. Intersection: Find overlapping elements (What matches)
matching_clearance = required_clearance.intersection(user_hardware_tags)
print(f"Matching Access Keys: {matching_clearance}")

# 2. Difference: Find what keys the user is missing
missing_clearance = required_clearance.difference(user_hardware_tags)
print(f"Missing Required Keys: {missing_clearance}")

# 3. Union: Combine all unique tags across the network log
all_network_tags = required_clearance.union(user_hardware_tags)
print(f"Total Unique Network Tags Registered: {all_network_tags}")