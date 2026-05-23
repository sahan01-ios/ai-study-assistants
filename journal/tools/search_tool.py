def search(query):

    knowledge_base = {
        "python": "Python is a high-level programming language used for software development, automation, and data science.",

        "algorithm": "An algorithm is a step-by-step procedure used to solve a problem or perform a task.",

        "loop": "A loop is a programming structure used to repeat a block of code multiple times.",

        "function": "A function is a reusable block of code designed to perform a specific task.",

        "variable": "A variable is used to store data values in programming.",

        "list": "A list is a Python data structure used to store multiple items in a single variable."
    }

    query = query.lower()

    for keyword, answer in knowledge_base.items():
        if keyword in query:
            return answer

    return f"No exact match found for: {query}"
