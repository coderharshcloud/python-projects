num1=input("enter your number:")
num2=input("enter another number:")
op=input("which operation do you want to perform:")


def calculation():
     if op == "+":
          print(int(num1) + int(num2))
     elif op == "-":
          print(int(num1) - int(num2))
     elif op == "*":
          print(int(num1) * int(num2))
     elif op == "/":
          print(int(num1) / int(num2))


calculation()


     

