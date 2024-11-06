import random
name = input("Enter your name : ")
print("This game is of rock(choose = r) paper (choose = p)and scissor(choose = s) . ")

CommonDict = {
  "r" : 1, 
  "p" : 0,
  "s" : -1
}

ReverseDict = {
1 : "rock",
0 : "paper",
-1 : "scissor"
}

A = "yes" or "y"
while (A == "yes" or A == "y" ):
    list = [0,0]
    
    try:
        n = int(input("How many rounds do you want to play : "))
    
    except:
        print("Please Enter a valid integer value .")
        continue

    for i in range(1,n+1):
        while True:
            human = input("Choose rock, paper or scissors : ").lower()
            
            if human in CommonDict:
                user = CommonDict[human]
                break
            
            else:
                print("Invalid choice! Please enter 'r', 'p', or 's'.")

        computer = random.choice([1, 0, -1])
        UserChoice = ReverseDict[user]
        ComputerChoice = ReverseDict[computer]

        print(f"Your Choice : {UserChoice}\nComputer's Choice : {ComputerChoice}")

        if(computer == user):
            print("Its's a draw .")

        else:
            if(computer == 1 and user == -1):
                print("You Loose !")
                list[0] += 1
            elif(computer == 1 and user == 0):
                print("You Win !")
                list[1] += 1
            elif(computer == 0 and user == -1):
                print("You Win !")
                list[1] += 1
            elif(computer == 0 and user == 1): 
                print("You Loose !")
                list[0] += 1
            elif(computer == -1 and user == 1): 
                print("You Win !")
                list[1] += 1
            elif(computer == -1 and user == 0):
                print("You Loose !")
                list[0] += 1

        def result():
            if (list[0]>list[1]):
                return "You Loose ."
            elif(list[0] == list[1]):
                return "Its a draw ."
            else:
                return "You Win ^_^"
            
    print("-------------------")
    
    final_result = result()
    print(f"Final score of this round is :\nYOU -- COMPUTER\n  {list[1]} -- {list[0]}")
    
    file_content = (f"NAME : {name}\nNumber of games played : {n}\nFinal Score :- \nYOU -- COMPUTER\n  {list[1]} -- {list[0]}\n{final_result}\n------------------------------\n")
    with open(f"{name}.txt" , "a") as f:
        f.write(file_content)
        
        if (list[0]>list[1]):
            print("You Loose .")
        elif(list[0] == list[1]):
            print("Its a draw .")
        else:
            print("You Win ^_^")

    A = input("Do you want to play again ?\n").lower()