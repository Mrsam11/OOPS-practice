# Write a program for “Guess the capitals” using a dictionary to store
# the pairs of states and capitals so that the questions are randomly
# displayed. The program should keep a count of the number of correct and
# incorrect responses.
correct = 0 
uncorrect = 0 
cap = {
    "Pakistan" : "Islamabad" , "India" : "Dehli" ,
    "Australia" : "Sydney" , "Bangladesh" : "Dhaka",
    "Afghanistan" : 'Kabul'
    }
for keys,values in cap.items():
    check = input(f"Enter the capital of {keys} ").title()
    if check == values:
        correct += 1
    else:
        uncorrect += 1
        
print(f"Your Correct Score is {correct}")
print(f"Your UnCorrect Score is {uncorrect}")
    