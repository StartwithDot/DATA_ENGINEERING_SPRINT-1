states = ["Kerala", "Karnataka", "Tamil Nadu", "Maharashtra", "Gujarat","Delhi"]

company = {
    "cin": "ACW-2217",
    "name": "VIRGO STARS INTERNATIONAL LLP",
    "state": "kerala",
    "status": "Active",
}

number_of_states = 6
total_with_one_more = number_of_states + 1

print(states)
print("How many states:", len(states))
print(company["name"], "is in", company["state"])
print(company)
print("States plus one:", total_with_one_more)

# OUTPUT EXCERCISE 3-->
# ['Kerala', 'Karnataka', 'Tamil Nadu', 'Maharashtra', 'Gujarat']
# How many states: 5
# VIRGO STARS INTERNATIONAL LLP is in kerala
# {'cin': 'ACW-2217', 'name': 'VIRGO STARS INTERNATIONAL LLP', 'state': 'kerala'}
# States plus one: 6


print(states[0])
print("The status of company", company["name"],"is",company["status"])
print(number_of_states*2)

# OUTPUT EXCERCISE 4-->
# ['Kerala', 'Karnataka', 'Tamil Nadu', 'Maharashtra', 'Gujarat', 'Delhi']
# How many states: 6
# VIRGO STARS INTERNATIONAL LLP is in kerala
# {'cin': 'ACW-2217', 'name': 'VIRGO STARS INTERNATIONAL LLP', 'state': 'kerala', 'status': 'Active'}
# States plus one: 7
# Kerala
# status of company VIRGO STARS INTERNATIONAL LLP is Active
# 12