import os

def count_long_names(names, min_length):
    count = 0
    for name in names:
        if len(name) >= min_length:
            count += 1 #count = count + 1
    return count

def main():
    companies = ["Tata", "Infosys Limited", "Wipro", "Reliance Industries Limited","The Boring Company"]
    print("Long names:", count_long_names(companies, 5))
    print("Current folder:", os.getcwd())

if __name__ == "__main__":
    main()

# output:
# Long names: 2
# Current folder: C:\Users\DataEngineering\DATA_ENGINEERING_SPRINT-1

# exercise 4 output:

# Long names: 4
# Current folder: C:\Users\DataEngineering\DATA_ENGINEERING_SPRINT-1


# what the function does: This function counts the number of names in a given list that have a length greater than or 
# equal to a provided minimum length. It iterates through each name in the list, checks its length, and increments 
# a counter (count) if the condition is met. Finally, it returns the total count of long names.

# TEST 1:
# a list with no matching names, OUTPUT-->0

# TEST 2:
# a list where all names match, OUTPUT-->5

# TEST 3:
# a name exactly min_length characters long, OUTPUT-->output will have that name counted as well,
#    beacuse we added len(name) >= min_length,>= equall to sign means it will count the name if it is equal to min_length .