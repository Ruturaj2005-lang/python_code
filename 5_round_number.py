import random
user_score = 0
computer_score = 0
print("Guess number between 1 and 10\n")
for round in range(1, 6):
    print("Round:", round)
    secret = random.randint(1, 10)
    guess = int(input("Enter your guess: "))
    if guess == secret:
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        print("Correct number was:", secret)
        computer_score += 1
    print()

print("Final Result")
print("Your Score:", user_score)
print("Computer Score:", computer_score)
