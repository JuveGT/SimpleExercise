import random as rn
import operator

# This function adds two numbers
def add(number1,number2):
    return number1+number2

# This function subtracts two numbers
def subtract(number1,number2):
    return number1-number2

# This function multiplies two numbers
def multiply(number3,number4):
    return number3*number4

# This function divides two numbers
def divide(number3,number4):
    return number3/number4

#This function has the computer pick
def computer(number3,number4):
    operations = {'+':operator.add, '-':operator.sub,
                  '*':operator.mul, '/':operator.truediv}
    operation = rn.choice(list(operations.keys()))
    print(f"What is {number3} {operation} {number4}? ")
    answer = operations.get(operation)(number3,number4)
    return answer
    


#User input needed to run code
print("We are going to play a math game")
name = input("What is your name? ")
print("Hello! ", name)
num_probs= input(name + ", How many problems do you want to do? ")
print("Select operation.")
print("1. If you want to Add")
print("2. If you want to Subtract")
print("3. If you want to Multiply")
print("4. If you want to Divide")
print("5. If you want the computer to decide")
choice = (input("Enter your choice: "))


current_count = 0
incorrect = []
correct = []

while current_count < int(num_probs):
    current_count=current_count+1
    number1 = rn.randint(1,120) #this should be smaller for positive subtraction
    number2 = rn.randint(75,450)
    number3 = rn.randrange(10,40,2)
    number4 = rn.randrange(1,5,1)
    if choice == "1":
        print(name + ", please add", str(number1) + " to", str(number2))
        user_answer = input(name + ", What is your answer? ")
        print(number1,"+",number2,"=", add(number1,number2))
        correct_answer = add(number1,number2)
    elif choice =="2":
        print(name + ", please subtract", str(number1) + " from", str(number2))
        user_answer = input(name + ", What is your answer? ")
        print(number2,"-",number1,"=", subtract(number2,number1))
        correct_answer = subtract(number2,number1)
    elif choice =="3":
        print(name + ", please multiply", str(number3) + " and", str(number4))
        user_answer = input(name + ", What is your answer? ")
        print(number3,"*",number4,"=", multiply(number3,number4))
        correct_answer = multiply(number3,number4)
    elif choice =="4":
        print(name + ", please divide", str(number3) + " by", str(number4))
        user_answer = input(name + ", What is your answer? ")
        print(number3,"/",number4,"=", divide(number3,number4))
        correct_answer = divide(number3,number4)
    elif choice =="5":
        correct_answer = computer(number3,number4)
        user_answer = input(name + ", What is your answer? ")
    else:
        print("invalid input")
        break

    if float(user_answer)==correct_answer:
        correct.append(user_answer)
    else:
        incorrect.append(user_answer)


print(name + ", you got",str(len(correct)) + " correct out of",str(num_probs) + " problems")
print("and you got",str(len(incorrect)) + " incorrect out of",str(num_probs) + " problems")
