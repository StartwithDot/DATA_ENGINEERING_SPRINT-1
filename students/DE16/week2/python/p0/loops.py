states = ["Kerala", "Karnataka", "Tamil Nadu", "Maharashtra", "Gujarat"]

count = 0
for state in states:
    if state.startswith("K"):
        print(state)
        count = count + 1

print("States starting with K:", count)


#EXERCISE to M


count = 0
for state in states:
    if state.startswith("M"):
        print(state)
        count = count + 1

print("States starting with M:", count)

#EXERCISE to else condition

count = 0
Not_k = 0
for state in states:
    if state.startswith("K"):
            print(state)
            count = count + 1
    else:
        print("Not a K state:", state)
        Not_k = Not_k + 1
print("----")
print("States starting with K:", count)
print("states not starting with K:", Not_k)
print("The Total number of states:", count+Not_k)