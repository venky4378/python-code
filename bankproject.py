class bankaccount:
    def __init__(self,account_number,initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
    def deposit(self,amount):
        self.balance +=amount
        return self.balance
    def withdrawl(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient Funds"
    def check_balance(self,):
        return self.balance
accounts = {}
while True:
    print("1. Create an account")
    print("2. Deposit")
    print("3. Withdrawl")
    print("4. Check Balance")
    print("5. Exit")

    choice = int(input("Choose an option: ").strip())
    if choice == 1:
        acc_num = float(input("Enter your new account number: ").strip())
        initial_balance = float(input("Enter your initial balance: ").strip())
        accounts[acc_num] = bankaccount(acc_num,initial_balance)
        print("Account Created")
    elif choice ==2:
        acc_num = float(input("Enter your account number: ").strip())
        if acc_num in accounts:
            dep_amount = float(input("Enter your deposit amount: ").strip())
            nb = accounts[acc_num].deposit(dep_amount)
            print("New Balance: ",nb)
        else:
            print("Couldn't find an account",acc_num)
    elif choice == 3:
        acc_num = float(input("Enter Your account Number: ").strip())
        if acc_num in accounts:
            wid_amount = float(input("Enter your withdrawl ammount: ").strip())
            wd = accounts[acc_num].withdrawl(wid_amount)
            print("Status: ",wd)
        else:
            print("couldnt find your account",acc_num)
    elif choice == 4:
        acc_num = float(input("Enter Your account Number: ").strip())
        if acc_num in accounts:
            b = accounts[acc_num].check_balance()
            print("Your balance is: ",b)
        else:
            print("couldnt find your account",acc_num)
    elif choice == 5:
        print("tHANKS FOR VISITING OUR SERVICE")






 

















# class Computer():
#     def __init__(self,brand,model):
#         self.__brand = brand
#         self.__model = model
#     def get_info(self):
#         return self.__brand +" " +self.__model
# computer1=Computer("Acer","Nitrov15")
# computer1.get_info()



























# class BankAccount():
#     def __init__(self, balance):
#         self.__balance = balance
#     def deposit(self, amount):
#         self.__balance += amount
#     def get_balance(self):
#         return self.__balance
# account =BankAccount(100)
# account.deposit(50)
# print(account.get_balance())
















































# class Bike:
#     def petrol_level(self):
#         print("petrol level is sufficient to drive")
#     def drive(self):
#         print("Let's Go!")
#     def go (self):
#         print("Bike is Going!")
# class person(Bike):
#     pass
# person_bike=Bike()
# person_bike.petrol_level()
# person_bike.drive()
# person_bike.go()
# class Truck(Bike):
#     def truck_info(self):
#         print("Truck is Going!")
# truck_started =Bike()
# truck_started.petrol_level()
# truck_started =Truck()
# truck_started.truck_info()






























# class Car:
#     wheels = 4
#     def __init__(self, maker, model):
#         self.maker=maker
#         self.model = model
# my_car = Car("Audi","a3")
# print(my_car.maker,my_car.model)
