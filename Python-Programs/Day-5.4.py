import random
print(f"Let's Play Rock{0}, Paper{1}, Scissors{2}")

player_choice = int(input("Enter your choice (0-2): "))
computer_choice = random.randint(0, 2)

print(f"Computer's choice: {computer_choice}")

if player_choice == computer_choice:
    print("It's a tie!")
elif (player_choice == 0 and computer_choice == 2) or \
     (player_choice == 1 and computer_choice == 0) or \
     (player_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You Lose!") or \
        print("Invalid choice!")