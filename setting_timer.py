import threading


def get_player_guess_with_timer(player_name, round_num, fact_or_fiction, time_limit=20):
    """
    Collects guess from a player with a time limit.

    Args:
        player_name (str): The name of the player.
        round_num (int): The current round number.
        fact_or_fiction (str): Indicates whether the statement is a fact or fiction.
        time_limit (int): Time limit in seconds for each player to respond.

    Returns:
        str: The player's guess ('fact' or 'fiction') or 'timeout' if they didn't respond in time.
    """
    guess = [None]

    def input_with_timeout():
        player_guess = input(f"{player_name}, Round {round_num}. Is this FACT or FICTION? ").strip().lower()
        if player_guess in ["fact", "fiction"]:
            guess[0] = player_guess

    input_thread = threading.Thread(target=input_with_timeout)
    input_thread.start()

    input_thread.join(timeout=time_limit)

    if guess[0] is None:
        print(f"{player_name} took too long to answer (more than {time_limit} seconds).")
        return "timeout"
    else:
        return guess[0]
