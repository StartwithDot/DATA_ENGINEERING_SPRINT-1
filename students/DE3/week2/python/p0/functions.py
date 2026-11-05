import os

def count_long_names(names, min_length):
    count = 0
    for name in names:
        # TODO: add 1 to count when the name is at least min_length characters long
        length = len(name)
        if length >= min_length:
            count= count +1
    return count

def main():
    companies = ["Tata", "Infosys Limited", "Wipro", "Reliance Industries Limited","NVIDIA"]
    print("Long names:", count_long_names(companies, 5))
    print("Current folder:", os.getcwd())

if __name__ == "__main__":
    main()

# here the main function only runs if we are at the main module i.e suppose if we are importing this function as a module in another program then the '--name--' changes to module name no longer main , so the function not run.
#it has a list of companies and we wnat to count how many companies names are more than a min_length
# since we import the os module from libaray,we can use getcwd() to get the working folder