def get_topic_choice():
    """
    Prompts the user to choose a topic from a predefined list.

    Returns:
        str: The topic selected by the user.
    """
    topics = {
        1: "Geography",
        2: "Music",
        3: "History",
        4: "Movie",
        5: "Python",
        6: "Space",
        7: "Comics",
        8: "Art",
        9: "Video Games",
        10: "Physics",
        11: "Others"
    }

    print("Choose a topic:")
    for key, topic in topics.items():
        print(f"{key}. {topic}")

    while True:
        try:
            choice = int(input("Enter the number of your topic choice: "))
            if choice in topics:
                return topics[choice]
            else:
                print("Invalid choice. Please select a valid topic number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
