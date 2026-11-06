import os

def count_long_names(names, min_length):
    count = 0
    for name in names:
         if len(name) >= min_length:
              count = count + 1
    return count

def main():
    companies = ["TATA","Infosys Limited","Wipro","Reliance Industries Limited"]
    print("Long names:", count_long_names(companies,10))
    print("Current folder:", os.getcwd())


if __name__ == "__main__":
        main()
        #this function helps to count long company names. it goes through each name and add 1 to count 
        #it has a list of companies and we want to count how many names are long
        

