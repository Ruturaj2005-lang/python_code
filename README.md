import random
def get_user_numbers():
    print("Enter 10 different numbers between 1 and 50")
    user_numbers = set()
    while len(user_numbers) < 10:
        num = int(input("Enter a number: "))
        if num >= 1 and num <= 50:
            if num not in user_numbers:
                user_numbers.add(num)
            else:
                print("Number already entered")
        else:
            print("Number must be between 1 and 50")
    return user_numbers
def play_game():
    game_numbers = random.sample(range(1, 51), 10)
    user_numbers = get_user_numbers()
    user_marked = set()
    computer_numbers = set(random.sample(range(1, 51), 10))
    computer_marked = set()
    print("\nYour Numbers:", sorted(user_numbers))
    print("Computer Numbers:", sorted(computer_numbers))
    print("\nNumber Calling Starts...\n")
    for number in game_numbers:
        input("Press Enter to call next number...")
        print("Number Called:", number)
        if number in user_numbers:
            user_marked.add(number)
            print("You marked:", number)
        if number in computer_numbers:
            computer_marked.add(number)
            print("Computer marked:", number)
        print("Your count:", len(user_marked))
        print("Computer count:", len(computer_marked))
        print("--------------------------")
    print("\nGame Over\n")
    if len(user_marked) == 10 and len(computer_marked) == 10:
        print("Match Draw")
    elif len(user_marked) == 10:
        print("You Win")
    elif len(computer_marked) == 10:
        print("Computer Wins")
    else:
        print("No one won")
play_game()
