states = ["Kerala", "Karnataka", "Tamil Nadu", "Maharashtra", "Gujarat"]

count = 0
count1 = 0
for state in states:
    if state.startswith("K"):
        print(state)
        count = count + 1
    else:
        print(f"not a K state: {state} ")
        count1 = count1 + 1
        

print("States starting with K:", count)
print("states not starting with K:", count1)