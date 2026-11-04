states = ["Kerala","Karnataka","Tamilnadu","Maharashtra","Gujarat"]

count = 0
for state in states:
    if state.startswith("M"):
        print(state)
        count = count + 1
    else :
        print("not an M state:",state)    
print("state starting with M:",count)
print("Total number of states:",count)