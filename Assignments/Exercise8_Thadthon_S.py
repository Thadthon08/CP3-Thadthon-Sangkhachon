UsernameInput = input("Username : ")
PasswordInput = input("Password : ")
if UsernameInput == "admin" and PasswordInput == "1234":
    print("Welcome To Sommai Shop")
    print("----------------------")
    print("1.Apple x", 30, "THB")
    print("2.Banana x", 10, "THB")
    print("3.Milk x", 40, "THB")
    print("4.Chocolate x", 50, "THB")
    print("----------------------")
    select = int(input("option :"))
    if select == 1 :
        print("Apple (30 THB)")
        num1 = int(input("Piece :"))
        print("Total = ",30*num1,"THB")
    elif select == 2 :
        print("Banana (10 THB)")
        num2 = int(input("Piece :"))
        print("Total = ", 10 * num2,"THB")
    elif select == 3 :
        print("Milk (40 THB)")
        num3 = int(input("Piece :"))
        print("Total = ", 40 * num3,"THB")
    elif select == 4 :
        print("Chocolate (50 THB)")
        num4 = int(input("Piece :"))
        print("Total = ", 50 * num4,"THB")
else:
    print("Please try again !!")
