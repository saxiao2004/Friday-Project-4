def study_trivia_questions():
    # Define a dictionary with trivia questions and answers
    trivia_dict = {
        "What is the capital of France?": "Paris",
        "Which planet is known as the Red Planet?": "Mars",
        "Who wrote 'Romeo and Juliet'?": "William Shakespeare",
        "What is the largest mammal in the world?": "Blue Whale",
        "What is the powerhouse of the cell?": "Mitochondria"
    }

    # Greet the user
    print("Welcome to the Trivia Question Study Program!\n")

    # Iterate through the dictionary and ask questions
    for question, correct_answer in trivia_dict.items():
        # Display the question to the user
        print(question)

        # Prompt the user to input their answer
        user_answer = input("Your answer: ").strip()

        # Check if the user's answer matches the correct answer
        if user_answer.lower() == correct_answer.lower():
            print("Correct!\n")
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}\n")

    # Farewell message
    print("You've completed the trivia questions.")

if __name__ == "__main__":
    study_trivia_questions()
