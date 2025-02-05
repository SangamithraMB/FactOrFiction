import wikipedia
import random


def get_random_wikipedia_article(topic):
    """
    Fetches a random Wikipedia article based on a chosen topic.

    Args:
        topic (str): The topic for which a random Wikipedia article is to be fetched.

    Returns:
        wikipedia.WikipediaPage: A random Wikipedia page related to the selected topic.

    Raises:
        wikipedia.exceptions.PageError: If no relevant page is found.
    """
    search_results = wikipedia.search(topic)
    if search_results:
        random_page_title = random.choice(search_results)
        page = wikipedia.page(random_page_title)
        return page
    else:
        raise wikipedia.exceptions.PageError("No article found for the topic.")
