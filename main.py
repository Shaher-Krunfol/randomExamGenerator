import random
import json

# Define categories and questions with answers
categories = ["Data Structure", "Algorithms", "OOP", "Python"]

def load_questions_from_json():
    try:
        with open("questions.json", "r") as file:
            questions = json.load(file)
            return questions
    except FileNotFoundError:
        return {}

# Load questions from the JSON file
questions = load_questions_from_json()


# Create a list to store all added questions
added_questions = []

def load_added_questions():
    try:
        with open("added_questions.json", "r") as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_added_questions():
    with open("added_questions.json", "w") as file:
        json.dump(added_questions, file)

# Load previously added questions
added_questions = load_added_questions()

asked_questions = set()

def get_random_question():
    category = random.choice(categories)
    available_questions = [q for q in questions[category] if q["question"] not in asked_questions]
    
    if not available_questions:
        # If all questions in a category have been asked, reset the asked_questions set
        asked_questions.clear()
        available_questions = questions[category]

    question_obj = random.choice(available_questions)
    question = question_obj["question"]
    answer = question_obj["answer"]

    asked_questions.add(question)  # Add the question to the set of asked questions
    return category, question, answer

def search_question(query):
    found = False

    # Search in predefined questions
    for category in categories:
        for question_obj in questions[category]:
            if query.lower() in question_obj["question"].lower():
                print(f"Category: {category}")
                print(f"Question: {question_obj['question']}")
                print(f"Answer: {question_obj['answer']}\n")
                found = True

    # Search in added questions
    for q in added_questions:
        if query.lower() in q["question"].lower():
            print(f"Category: {q['category']}")
            print(f"Question: {q['question']}")
            print(f"Answer: {q['answer']}\n")
            found = True

    if not found:
        print("No matching questions found.\n")

def add_question(category, new_question, new_answer):
    if category in categories:
        questions[category].append({"question": new_question, "answer": new_answer})
        added_questions.append({"category": category, "question": new_question, "answer": new_answer})
        save_added_questions()  # Save the updated list of added questions
        print("Question added successfully.\n")
    else:
        print("Invalid category for adding a question.\n")

def view_added_questions():
    print("Added Questions:")
    for i, q in enumerate(added_questions, 1):
        print(f"{i}. Category: {q['category']}")
        print(f"   Question: {q['question']}")
        print(f"   Answer: {q['answer']}\n")
        
def display_all_questions():
    for category, category_questions in questions.items():
        print(f"Category: {category}")
        for index, q in enumerate(category_questions, 1):
            print(f"  {index}. Question: {q['question']}")
            print(f"     Answer: {q['answer']}")
        print()

def main():
    while True:
        print("1. Get a specific number of questions")
        print("2. Get a random question")
        print("3. Search for a question")
        print("4. Add a question")
        print("5. View added questions")
        print("6. View All questions")
        print("7. Quit")
        choice = input("Enter your choice (1/2/3/4/5/6/7): ").strip()

        if choice == "1":
            num_questions = int(input("Enter the number of questions you want: "))
            if num_questions <= 0:
                print("Please enter a valid number of questions.\n")
                continue

            category = input("Enter the category (Data Structure, Algorithms, OOP, Python): ").strip()
            print("Available categories:", categories)  # Add this line
            print(f"Entered category: {category}")  # Add this line
            if category not in categories:
                print("Invalid category. Please choose from the provided categories. \n")
                continue

            for _ in range(num_questions):
                question_obj = random.choice(questions[category])
                question = question_obj["question"]
                answer = question_obj["answer"]
                print(f"Category: {category}")
                print(f"Question: {question}")
                if _ < num_questions - 0:
                    show_answer = input("Do you want to see the answer for this question? (yes/no): ").strip().lower()
                    if show_answer == "yes":
                        print(f"Answer: {answer}\n")

        elif choice == "2":
            category, question, answer = get_random_question()
            print(f"Category: {category}")
            print(f"Question: {question}")
            show_answer = input("Do you want to see the answer for this question? (yes/no): ").strip().lower()
            if show_answer == "yes":
                print(f"Answer: {answer}\n")

        elif choice == "3":
            query = input("Enter a keyword to search for a question: ").strip()
            search_question(query)
            
        elif choice == "4":
            category = input("Enter the category to add a question (Data Structure, Algorithms, OOP, Python): ").strip()
            new_question = input("Enter the new question: ").strip()
            new_answer = input("Enter the answer to the new question: ").strip()
            add_question(category, new_question, new_answer)
            
        elif choice == "5":
            view_added_questions()
        
        elif choice == "6":
                display_all_questions()
            
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, 5, 6 or 7.\n")

    # Save the added questions before exiting
    save_added_questions()

if __name__ == "__main__":
    main()

