import random

def play():
    options = ["stone", "scissor", "paper"]
    user_choice = input("Enter your choice (stone, scissor, paper): ").lower()
    
    if user_choice not in options:
        print("Invalid input!")
        return

    comp_choice = random.choice(options)
    print(f"Computer chose: {comp_choice}")

    if user_choice == comp_choice:
        print("Draw")
    elif (user_choice == "stone" and comp_choice == "scissor") or \
         (user_choice == "scissor" and comp_choice == "paper") or \
         (user_choice == "paper" and comp_choice == "stone"):
        print("You win")
    else:
        print("Computer win")

play()