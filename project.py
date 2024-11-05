import random
print("This game is of rock(choose = r) paper (choose = p)and scissor(choose = s) . ")
CommonDict = {
  "r" : 1, 
  "p" : 0,
  "s" : -1,
}
ReverseDict = {
1 : "rock",
0 : "paper",
-1 : "scissor"
}


human = input("Choose rock, paper or scissors : ").lower()
user = CommonDict[human]
computer = random.choice([1, 0, -1])
UserChoice = ReverseDict[user]
ComputerChoice = ReverseDict[computer]

print(f"Your Choice : {UserChoice}\nComputer's Choice : {ComputerChoice}")

if(computer == user):
    print("Its's a draw .")

else:
    if(computer == 1 and user == -1):
        print("You Loose !")
    elif(computer == 1 and user == 0):
        print("You Win !")
    elif(computer == 0 and user == -1):
        print("You Win !")
    elif(computer == 0 and user == 1): 
        print("You Loose !")
    elif(computer == -1 and user == 1): 
        print("You Win !")
    elif(computer == -1 and user == 0):
        print("You Loose !")

print("Thank You \n")