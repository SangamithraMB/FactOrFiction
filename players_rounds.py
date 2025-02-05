def get_number_of_players():
    """
    Prompts the user to enter the number of players.

    Returns:
        int: The number of players must be greater than 0 and less than or equal to 3.
    """
    while True:
        try:
            players_number = int(input("Enter the number of players(1-3): "))
            if 0 < players_number <= 3:
                return players_number
            else:
                print("Please enter a number greater than 0 and less than or equal to 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_number_of_rounds():
    """
    Prompts the user to enter the number of rounds.

    Returns:
        int: The number of rounds must be greater than 0 and less than or equal to 3.
    """
    while True:
        try:
            rounds = int(input("Enter the number of rounds: "))
            if 0 < rounds <= 3:
                return rounds
            else:
                print("Please enter a number greater than 0 and less than or equal to 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
