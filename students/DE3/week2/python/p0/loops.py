states = ["Kerala", "Karnataka", "Tamil Nadu", "Maharashtra", "Gujarat"]

count = 0
total=0
for state  in states:
    total = total +1
    if state.startswith("M"):
        print("State starts with M",state)
        count = count + 1
    elif not state.startswith("K"):
          print("state not starts with K",state)
         

print("States starting with M:", count)
print("Total states counted:", total)