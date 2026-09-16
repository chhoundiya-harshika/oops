

print("1.ADD")
print ("2.SUB")
print("3.MUL")
print("4.DIV")
print("5.FACTORIAL")

choice =input("Enter your choice")


num1 = int(input("Enter first number"))
num2 = int(input("Enter Second number"))

match choice:
    case "ADD": 
        print(num1+num2)
    case "SUB":
        print(num1-num2)
    case "MUL":
        print(num1*num2)
    case "DIV":
        print(num1/num2)
    case "FACTORIAL":
        print(num1*(num1-1))
    
        