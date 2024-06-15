import random

# Function to get choice from the user
def get_choice():
    # Asks for choice until it's 1 or 2
    choice = ""
    while choice not in [1, 2]:
        choice = input("Please press 1 to save a question, 2 to start the game: ")

        # Converts choice to integer if it's a number
        if choice.isdigit():
            choice = int(choice)
        else:
            print("Invalid input, please enter a number.")
            continue

        return choice

# Function to get a question from the user
def get_question():
    # Gets the question from the user
    question = input("Please write the question you want to save: ")

    # Removes leading and trailing spaces from the question
    if question.strip():
        return question

# Function to save the question to the notepad
def save_question(question):
    # Opens the file in append mode and writes the question with a space
    with open('questions.txt', 'a') as file:
        file.write(question + "\n")

    print("Your question has been successfully saved.")

# Function to check if the question is already in the notepad
def question_check(question):
    with open('questions.txt', 'r') as file:
        # Reads the questions from the file
        questions = file.readlines()

        # Combines the user's question with newline for comparison
        if question + '\n' in questions:
            print("Error! The question is already saved.")
            return True
        else:
            return False

# Function to get an answer from the user
def get_answer():
    # Gets the answer from the user
    answer = input("Please write the answer to the question: ")

    # Removes leading and trailing spaces from the answer
    if answer.strip():
        return answer

# Function to save the answer to the notepad
def save_answer(answer):
    # Opens the file in append mode and writes the answer with a space
    with open('answers.txt', 'a') as file:
        file.write(answer + "\n")

    print("Answer has been successfully saved.")

# GAME
# Function to retrieve questions and add them to a list
def get_questions():
    questions = []
    with open('questions.txt', 'r') as file:
        for line in file:
            # Removes leading and trailing spaces from the line
            line = line.strip()
            if line:
                questions.append(line)

    return questions

# Function to retrieve answers and add them to a list
def get_answers():
    answers = []
    with open("answers.txt", "r") as file:
        for answer in file:
            answer = answer.strip()
            if answer:
                answers.append(answer)
    return answers

# Function to check if questions and answers lists are empty
def list_check(questions, answers):
    # If either questions or answers list is empty
    if not questions or not answers:
        return True

# Function to zip two lists and pick a random question from there
def zip_lists(questions, answers):
    # Zips questions and answers into tuples
    return list(zip(questions, answers))

# Function to pick a random element from the zipped list and remove it
def pick_element(list):
    # Picks a random tuple from the zipped list
    element = random.choice(list)

    # Removes the picked tuple from the zipped list
    list.remove(element)

    # Returns the question (0th index) and answer (1st index) of the tuple
    return element[0], element[1]

# Function to get user's answer
def user_answer():
    user_answer = input("Please enter your answer: ")
    return user_answer

# Function for checks of user's answer and the correct answer, adding points, etc.
def checks(user_answer, answer, player_score):
    if user_answer == answer:
        print("Congratulations, you answered correctly!")
        player_score += 50
        print("Score: ", player_score)
        return True, player_score # To continue or break the loop

    else:
        print("Sorry, better luck next time...")
        print("Final score: ", player_score)
        return False, player_score

# Function to ask the user if they want to continue after each question
def user_decision():
    decision = ""

    # Converts the answer to uppercase
    while decision not in ['Y', 'N']:
        decision = input("Press Y to continue, N to quit: ")

        # Converts the input to uppercase and checks
        if decision.upper() == 'Y':
            return True # Continue

        elif decision.upper() == 'N':
            return False # Quit

        else:
            print("Please enter valid characters.")
            continue

        break

# Function for replaying the game at the end
def replay_game():
    replay = ""

    # Converts the answer to uppercase
    while replay not in ['Y', 'N']:
        replay = input("Press Y to play again, N to quit: ")

        # Converts the input to uppercase and checks
        if replay.upper() == 'Y':
            return True # Continue

        elif replay.upper() == 'N':
            return False # Quit

        else:
            print("Please enter valid characters.")
            continue

        break

# Main game controls
while True:

    # Get the choice
    choice = get_choice()

    # Get the questions list and the answers list
    questions = get_questions()
    answers = get_answers()

    # Player score starts from 0
    player_score = 0

    # If choice is 1, it saves a question to the game
    if choice == 1:

        # Get the question
        question = get_question()

        # If the question is not already in questions, save it along with the answer
        if not question_check(question):
            save_question(question)
            answer = get_answer()
            save_answer(answer)

        # If it's already saved, continue the loop
        else:
            continue

    # If choice is 2, the game starts
    elif choice == 2:
        print("Welcome to the Quiz Game!!!")
        print("\n")

        # If questions or answers list is empty, show error
        if list_check(questions, answers):
            print("No questions available, please add questions first.")
            continue

        # Zip questions and answers into tuples
        zipped_list = zip_lists(questions, answers)

        # Loop through questions list length to get questions and answers
        for i in range(len(questions)):

            # Get the question and answer
            question, answer = pick_element(zipped_list)
            print(f"Question {i+1}: {question}")
            print("\n")

            # Get user's answer
            user_answer_str = user_answer()

            # Get the decision and the score from checks
            decision, player_score = checks(user_answer_str, answer, player_score)

            # If checks return False, the answer is wrong, break the loop and end the game
            if not decision:
                break

            # After answer check, ask the user's decision
            user_decision_answer = user_decision()

            print("\n")
            # If user wants to continue, the game continues
            if user_decision_answer:
                print("Game continues...")
                continue

            # If user wants to quit, exit the loop and print the final score
            else:
                # If the player decides to quit the game, print their score
                print(f"You quit the game. Your final score: {player_score}")
                break

        # If the user wants to play again after each game ends
        if replay_game():
            print("Game restarts...")
            continue

        # If the user doesn't want to play again, end the game
        else:
            print("Game exited.")
            break
