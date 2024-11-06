def main():
    expence ()    #use for call
    file ()            #use for call
    misc_expence()      #use for call

def expence():
    print("user expence")
    print("________________________")
    expence_name = input("1.name of expence:-")
    expence_amount = float(input("2.amount of expence:-"))
    print(f"expence name is {expence_name},{expence_amount}")
    expence_category =[
        "food:",
        "home loan:",
        "travel fun:",
        "work:",

    ]
    while True:
        print("name of category")
        for i,category_name in enumerate(expence_category):
            print(f"{i+1}.{category_name}")
        value_range = f"[1-{len(expence_category)}]"
        select_expence_category =int( input(f"input expence category::{value_range}"))-1
        break

if __name__ == "__main__":
    main()