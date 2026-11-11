states = ["Kerala", "Karnataka", "Tamil Nadu", "Maharashtra", "Gujarat","srilanka"]

company = {
    "cin": "ACV-9915",
    "name": "WATRIX CONSTRUCTION SOLUTIONS LLP",
    "state": "kerala",
    "status":"active",
}

number_of_states = 6
total_with_one_more = number_of_states + 1

print(states)
print("How many states:", len(states))
print(company["name"], "is in", company["state"])
print(company)
print("States plus one:", total_with_one_more)
print(states[0])
print(states[:2:])
print(states[::-1])
print(company)
print(number_of_states*2)