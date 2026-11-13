states = ["Kerala", "Tamil Nadu", "Karnataka", "Maharashtra", "Gujarat"]

count = 0
total = 0
for state in states:
    total = total + 1
    if state.startswith("M"):
        print("State starting with M:", state)
        count = count + 1
    elif not state.startswith("K"):
        print("State not starting with K:", state)


print("States starting with M:", count)
print("Total states:", total)

