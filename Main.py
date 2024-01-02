import random
import json
import os

CATEGORIES = ["computer architecture", "operating systems", "networks", "databases", "programming languages"]
FILE_PREFIX = "{category}.json"
ADDED_QUESTIONS_FILE = "added_questions.json"

def load_questions():
    questions = {}
    for category in CATEGORIES:
        file_path = FILE_PREFIX.format(category=category)
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                questions[category] = json.load(file)
        else:
            questions[category] = []
    return questions

# This function reads the contents of the "added_questions.json" file and returns the loaded data as a list
def load_added_questions():
    try:
        with open(ADDED_QUESTIONS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
# his function writes the contents of the added_questions list to the "added_questions.json" file.
def save_added_questions():
    with open(ADDED_QUESTIONS_FILE, "w") as file:
        json.dump(added_questions, file)
        
# This function randomly selects a category and then retrieves a random question (dictionary) from the corresponding list within the questions dictionary.
def get_random_question():
    category = random.choice(CATEGORIES)
    question_obj = random.choice(questions[category])
    return category, question_obj["question"], question_obj["answer"]

# In this function, the questions dictionary is updated by appending a new question (dictionary) to the list associated with the specified category.
# When a user adds a new question, the information is appended to the added_questions list.
def add_question(category, new_question, new_answer):
    if category in CATEGORIES:
        questions[category].append({"question": new_question, "answer": new_answer})
        added_questions.append({"category": category, "question": new_question, "answer": new_answer})
        save_added_questions()
        with open(FILE_PREFIX.format(category=category), "w") as file:
            json.dump(questions[category], file)
        print("Question added successfully.")
    else:
        print("Invalid category for adding a question.\n")
# This function iterates over the added_questions list to display the details of the added questions.
def view_added_questions():
    print("Added Questions:")
    for i, q in enumerate(added_questions, 1):
        print(f"{i}. Category: {q['category']}\nQuestion: {q['question']}\nAnswer: {q['answer']}\n")

def main():
    while True:
        print("1. Get a specific number of questions")
        print("2. Get a random question")
        print("3. Add a question")
        print("4. View added questions")
        print("5. Quit")
        choice = input("Enter your choice (1/2/3/4/5): ").strip()

        if choice == "1":
            num_questions = int(input("Enter the number of questions you want: "))
            if num_questions <= 0:
                print("Please enter a valid number of questions.")
                continue

            category = input("Enter the category (computer architecture, operating systems, networks, databases, programming languages): ").lower().strip()
            if category not in CATEGORIES:
                print("Invalid category. Please choose from the provided categories.")
                continue

            for _ in range(num_questions):
                question_obj = random.choice(questions[category])
                question = question_obj["question"]
                answer = question_obj["answer"]
                print(f"Category: {category}\nQuestion: {question}")
                if _ <= num_questions - 1:
                    show_answer = input("Do you want to see the answer for this question? (yes/no): ").strip().lower()
                    if show_answer == "yes":
                        print(f"Answer: {answer}\n")

        elif choice == "2":
            category, question, answer = get_random_question()
            print(f"Category: {category}\nQuestion: {question}")
            show_answer = input("Do you want to see the answer for this question? (yes/no): ").strip().lower()
            if show_answer == "yes":
                print(f"Answer: {answer}\n")

    
        elif choice == "3":
            category = input("Enter the category to add a question: ").strip()
            new_question = input("Enter the new question: ").strip()
            new_answer = input("Enter the answer to the new question: ").strip()
            add_question(category, new_question, new_answer)

        elif choice == "4":
            view_added_questions()

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 5\n")

    save_added_questions()

if __name__ == "__main__":
    questions = load_questions()
    added_questions = load_added_questions()
    main()
