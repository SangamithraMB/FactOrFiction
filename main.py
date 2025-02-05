import wikipedia
import random
import warnings
from bs4 import GuessedAtParserWarning

import fetching_wiki_data
import game_description_rules
import modify_fact
import player_guess
import players_rounds
import topic_options

warnings.filterwarnings("ignore", category=GuessedAtParserWarning)


def main():
    """
    Main function that runs the Fact or Fiction game.
    It allows the user to choose a topic, fetches random facts from Wikipedia articles,
    and generates false versions of those facts by modifying numbers.
    The game proceeds round by round with players guessing whether the statement is fact or fiction.
    """
    game_description_rules.print_game_description()
    game_description_rules.print_game_rules()
    num_players = players_rounds.get_number_of_players()
    num_rounds = players_rounds.get_number_of_rounds()

    print("Let the players choose a topic!")
    topic_choice = topic_options.get_topic_choice()
    print(f"Selected topic: {topic_choice}\n")

    facts = set()
    false_facts = set()

    print(f"From Wikipedia, Presenting statements about {topic_choice}...\n")

    while len(facts) < num_rounds:
        try:
            random_page = fetching_wiki_data.get_random_wikipedia_article(topic_choice)
            fact = modify_fact.extract_first_sentence(random_page)

            if fact:
                if fact not in facts:
                    facts.add(fact)

                    false_fact = modify_fact.modify_numbers_in_fact(fact)
                    if false_fact not in false_facts:
                        false_facts.add(false_fact)

        except wikipedia.exceptions.DisambiguationError:
            continue
        except wikipedia.exceptions.PageError:
            continue

    player_scores = {f"Player {i + 1}": 0 for i in range(num_players)}

    for round_num, (fact, false_fact) in enumerate(zip(facts, false_facts), 1):
        correct_answer = random.choice(["fact", "fiction"])
        statement = fact if correct_answer == "fact" else false_fact
        print(f"Round {round_num}: {statement}")

        player_guesses = player_guess.get_player_guesses(num_players, round_num, correct_answer, time_limit=20)

        for player, guess in player_guesses.items():
            if guess == "timeout":
                print(f"{player} didn't answer in time.")
            elif guess == correct_answer:
                print(f"{player} guessed correctly!")
                player_scores[player] += 1
            else:
                print(f"{player} guessed wrong.")

    print("\nFinal Scores:")
    for player, score in player_scores.items():
        print(f"{player}: {score} points")

    highest_score = max(player_scores.values())
    winners = [player for player, score in player_scores.items() if score == highest_score]

    if len(winners) > 1:
        print("\nIt's a tie!")
        print("The winners are:")
        for winner in winners:
            print(f"{winner} with {highest_score} points")
    else:
        winner = winners[0]
        print(f"\nCongratulations, {winner}! You are the winner!")


if __name__ == "__main__":
    main()
