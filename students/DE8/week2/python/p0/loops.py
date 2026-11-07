states = ["Kerala", "Karnataka", "Tamil Nadu","Meghalaya","Maharashtra", "Gujarat","Delhi","Madhya Pradesh","Maharashtra","Mizoram","Manipur"]



count = 0
for state in states:
    if state.startswith("K"):
        print(state)
        count = count + 1

print("States starting with K:", count)

# OUTPUT --->

# Kerala
# Karnataka
# States starting with K: 2

# EXERCISE 4-->

count = 0
non_k_states = 0
for state in states:
    if state.startswith("M"):
        print(state,"starts with M")
        count = count + 1
    else:
        print("Not a K state:", state)
        non_k_states = non_k_states + 1
print("--------------------------------------")
print("States starting with M:", count)
print("States not starting with M:", non_k_states)
print("Total number of states:", count+non_k_states) 

# OUTPUT --->

# Not a K state: Kerala
# Not a K state: Karnataka
# Not a K state: Tamil Nadu
# Meghalaya starts with M
# Maharashtra starts with M
# Not a K state: Gujarat
# Not a K state: Delhi
# Madhya Pradesh starts with M
# Maharashtra starts with M
# Mizoram starts with M
# Manipur starts with M
# -------------------------------------
# States starting with M: 6
# States not starting with M: 5
# Total number of states: 11



        
# PRACTICE------>

for state in states:
    if state.startswith("K"):
        print(state)
    else:
        print("Not a state starting with K")

for state in states:
    if state.startswith("m".upper()):
        print(state)
    else:
        print("Not a state starting with M")


# OUTPUT --->

# Kerala
# Karnataka
# Not a state starting with K
# Not a state starting with K
# Not a state starting with K
# Not a state starting with K
# Not a state starting with K
# Not a state starting with K
# Not a state starting with K
# Not a state starting with K
# Not a state starting with M
# Not a state starting with M
# Not a state starting with M
# Maharashtra
# Not a state starting with M
# Not a state starting with M
# Madhya Pradesh
# Maharashtra
# Mizoram
# Manipur