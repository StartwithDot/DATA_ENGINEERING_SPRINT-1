import os

def count_long_names(names, min_length):
    count = 0
    for name in names:
        if len(name) >= min_length:
            count = count + 1
    return count

def main():
    companies = ["Tata", "Infosys Limited", "Wipro", "Reliance Industries Limited", "dotset"]
    print("Long names:", count_long_names(companies, 5))
    print("Current folder:", os.getcwd())

if __name__ == "__main__":
    main()

#TEST 1
# A list with no matching names, output = 0
#TEST 2
# A list where all names match, output = 5
#TEST 3
# A name exactly min_length characters long, output = in this case is 1