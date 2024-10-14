from Numbers import Numbers

print("0. exit\n"+"1. append\n"+"2. print sums\n"+"3. compare sums")
choice = int(input("Enter choice :"))
while choice != 0:
    if choice == 1:
        index = int(input("index (0 or 1) ->"))
        num = int(input("value ->"))
        select_1 = Numbers(num, index)
        print(select_1.__str__())
    elif choice == 2:
        print(Numbers.total_lists())
    elif choice == 3:
        print(Numbers.__eq__())
    print("0. exit\n"+"1. append\n"+"2. print sums\n"+"3. compare sums")
    choice = int(input("Enter choice :"))