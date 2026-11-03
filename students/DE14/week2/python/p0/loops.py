states = ["Kerala","Karnataka","Tamil Nadu" ,"Maharashtra","Gujarat"]

count = 0
total_count = 0
for state in states:
    total_count = total_count + 1
    if state.startswith("M"):
        print(state)
        count = count + 1
    else:
        print("Not a K state:", state)   

print("states starting with K:", count) 
print("Total states:", total_count)  