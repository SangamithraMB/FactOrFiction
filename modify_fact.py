import re
import random


def extract_first_sentence(page):
    """
    Extracts the first sentence containing a number from the Wikipedia summary.

    Args:
        page (wikipedia.WikipediaPage): The Wikipedia page from which the sentence is extracted.

    Returns:
        str or None: The first sentence with a number if it exists, otherwise None.
    """
    summary = page.summary
    first_sentence = re.split(r'(?<!\w\.\w)(?<![A-Z][a-z]\.)[.!?]\s+', summary)[0]
    if re.search(r'\d', first_sentence):
        return first_sentence.strip()
    return None


def modify_numbers_in_fact(fact, percentage_range=10):
    """
    Modifies the numerical values in a fact by a random percentage within a range.

    Args:
        fact (str): The fact containing numerical values.
        percentage_range (int, optional): The percentage range within which the numbers are modified. Defaults to 10%.

    Returns:
        str: The modified fact with altered numbers.
    """

    def replace_with_random(match):
        original_number = float(match.group())
        variation = (percentage_range / 100.0) * original_number
        random_number = original_number + random.uniform(-variation, variation)

        max_realistic_number = 2024

        if random_number > max_realistic_number:
            return str(int(original_number))

        return str(int(random_number)) if original_number.is_integer() else str(round(random_number, 2))

    false_fact = re.sub(r'\d+(\.\d+)?', replace_with_random, fact)
    return false_fact
