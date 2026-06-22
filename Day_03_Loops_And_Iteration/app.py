# Day 03 Project: System Launch Countdown & Analytics Utility
import time

print("--- 1. Countdown Sequence (For Loop & Range) ---")
# Using range(start, stop, step) to count backward from 5 to 1
for seconds in range(5, 0, -1):
    print(f"🚀 T-minus {seconds} seconds...")
    time.sleep(0.5)  # Shorter sleep just for quick terminal execution demo
print("💥 Lift-off! System core loops activated.\n")


print("--- 2. Sum of Multiples Challenge ---")
# Scenario: Find the sum of all numbers between 1 and 20 that are multiples of 3 or 5
total_sum = 0
upper_limit = 21  # range is exclusive of the stop number

for num in range(1, upper_limit):
    if num % 3 == 0 or num % 5 == 0:
        total_sum += num

print(f"The sum of all numbers between 1 and 20 divisible by 3 or 5 is: {total_sum}\n")


print("--- 3. Dynamic Buffer Clearance (While Loop) ---")
# Simulating queue processing where elements decrease dynamically
system_logs = ["Log_Error_01", "Log_Warn_02", "Log_Info_03", "Log_Debug_04"]
print(f"Initial System Log Queue: {system_logs}")

while len(system_logs) > 0:
    processed_log = system_logs.pop(0)  # Remove from front of list
    print(f"🔧 Processing and clearing: {processed_log}")

print(f"Queue Status: {len(system_logs)} items left. Buffer clear.")