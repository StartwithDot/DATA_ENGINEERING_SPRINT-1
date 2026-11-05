states=["Kerala", "Karnataka", "Gujarat","Tamil nadu","Maharastra","GOA"]

company={
    "cin":"ACV-9644",
    "name":"ZONKA HOMES LLP",
    "state":"Kerala",
    'status':'active'
}

num_of_states=6

print(states)
print(company)
print("How many states:",len(states))
print("Company name",company["name"],"is in",company["state"],"company cureent status :", company["status"])
print(states*2)