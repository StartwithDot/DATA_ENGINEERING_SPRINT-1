states = ["Kerala", "Karnataka", "Tamil Nadu", "Maharashtra", "Gujarat"]
count = 0
count1 = 0
notkcount = 0

for state in states:
    if state.startswith("K"):
        print("State starts with K:", state)
        count += 1
    else:
        notkcount += 1
        if state.startswith("M"):
            print("State starts with M:", state)
            count1 += 1
        else:
            print("State does not start with K:", state)

print("Number of states starting with K:", count)
print("Number of states starting with M:", count1)
print("Number of states not starting with K:", notkcount)