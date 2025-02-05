import setting_timer


def get_player_guesses(num_players, round_num, fact_or_fiction, time_limit=20):
    """
    Collects guesses from players for a given round with a time limit.

    Args:
        num_players (int): The number of players.
        round_num (int): The current round number.
        fact_or_fiction (str): Indicates whether the statement is a fact or fiction.
        time_limit (int): Time limit in seconds for each player to respond.

    Returns:
        dict: A dictionary with player names as keys and their guesses as values.
    """
    player_guesses = {}
    for i in range(num_players):
        player_name = f"Player {i + 1}"
        guess = setting_timer.get_player_guess_with_timer(player_name, round_num, fact_or_fiction, time_limit)
        while guess not in ["fact", "fiction", "timeout"]:
            print("Invalid input. Please enter 'fact' or 'fiction'.")
            guess = setting_timer.get_player_guess_with_timer(player_name, round_num, fact_or_fiction, time_limit)
        player_guesses[player_name] = guess
    return player_guesses

