states = ["Kerala", "Karnataka", "Tamil Nadu","Maharashtra","Gujarat","Rajasthan"]

company = {
    "cin": "ACV-9770",
    "name": "KENSON GROUP",
      "state": "Kerala",
      "status": "Active",
}

number_of_states = 6
total_with_one_more = number_of_states + 1

print("states:",states)
print("company:",company)
print("status:", company["status"])
print("How many states:", len(states))
print(company["name"], "is in", company["state"])
print("States plus one:", total_with_one_more)
print("number_of_states*2:", number_of_states*2)




