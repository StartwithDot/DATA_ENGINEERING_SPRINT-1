states = ["Kerala", "Karnataka", "Maharashtra", "Tamil Nadu", "Gujarat","Punjab"]

company = {
    "cin": "ACV-9644",
    "name": "ZOOKA HOMES LLP",
    "state": "Kerala",
}

number_of_states = 6
total_with_one_more = number_of_states + 1
company["status"] = "Active"

print(states[0])
print("How many states:", len(states))
print(company["name"],"is in", company["state"])
print(company)
print("Company status:", company["status"])
print("states plus one:", total_with_one_more)
print("states multiply by two:", number_of_states * 2)