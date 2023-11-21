import random
import json

# Define categories and questions with answers
categories = ["computer Architecture", "operating Systems", "networks", "databases", "programming Languages"]

questions = {
    "computer architecture": [
        {"question": "What is the purpose of a CPU cache?", "answer": "To store frequently used data and instructions to reduce the time it takes to fetch them from main memory."},
        {"question": "Explain the concept of pipelining in computer architecture.", "answer": "Pipelining is a technique where multiple instructions are overlapped in execution, improving the throughput of the CPU."},
        {"question": "What is the Von Neumann architecture?", "answer": "A computer architecture that uses a single data bus to transfer data between the CPU and memory."},
    ],
    "operating systems": [
        {"question": "What is the role of an operating system?", "answer": "To manage hardware and software resources, providing services such as process management, memory management, and file systems."},
        {"question": "Explain the difference between multitasking and multiprocessing.", "answer": "Multitasking involves running multiple tasks concurrently on a single processor, while multiprocessing involves running tasks on multiple processors."},
        {"question": "What is virtual memory?", "answer": "A memory management technique that uses both RAM and disk space to simulate larger memory than physically available."},
    ],
    "networks": [
        {"question": "What is the OSI model?", "answer": "A conceptual framework that standardizes the functions of a telecommunication or computing system into seven abstraction layers."},
        {"question": "Explain the difference between TCP and UDP.", "answer": "TCP (Transmission Control Protocol) is a connection-oriented protocol that provides reliable, ordered delivery of data. UDP (User Datagram Protocol) is connectionless and does not guarantee delivery."},
        {"question": "What is subnetting in networking?", "answer": "Subnetting involves dividing a larger network into smaller, more manageable sub-networks to improve performance and security."},
    ],
    "databases": [
        {"question": "What is normalization in database design?", "answer": "Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity."},
        {"question": "Explain the difference between SQL and NoSQL databases.", "answer": "SQL databases are relational and use a structured query language, while NoSQL databases are non-relational and provide a more flexible data model."},
        {"question": "What is ACID in the context of database transactions?", "answer": "ACID stands for Atomicity, Consistency, Isolation, and Durability, which are properties that guarantee the reliability of database transactions."},
    ],
    "programming languages": [
        {"question": "What is the difference between compiled and interpreted programming languages?", "answer": "Compiled languages are translated into machine code before execution, while interpreted languages are translated at runtime."},
        {"question": "Explain the concept of object-oriented programming (OOP).", "answer": "OOP is a programming paradigm that uses objects, which bundle data and methods that operate on the data, to design and implement software."},
        {"question": "What is the significance of pointers in programming languages like C?", "answer": "Pointers allow for direct memory manipulation and are essential for tasks such as dynamic memory allocation and efficient data structures."},
    ],
}


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

def get_random_question():
    category = random.choice(categories)
    question_obj = random.choice(questions[category])
    question = question_obj["question"]
    answer = question_obj["answer"]
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
        print("Question added successfully.")
    else:
        print("Invalid category for adding a question.\n")

def view_added_questions():
    print("Added Questions:")
    for i, q in enumerate(added_questions, 1):
        print(f"{i}. Category: {q['category']}")
        print(f"   Question: {q['question']}")
        print(f"   Answer: {q['answer']}\n")

def main():
    while True:
        print("1. Get a specific number of questions")
        print("2. Get a random question")
        print("3. Search for a question")
        print("4. Add a question")
        print("5. View added questions")
        print("6. Quit")
        choice = input("Enter your choice (1/2/3/4/5/6): ").strip()

        if choice == "1":
            num_questions = int(input("Enter the number of questions you want: "))
            if num_questions <= 0:
                print("Please enter a valid number of questions.")
                continue

            category = input("Enter the category (Computer Architeture, Operating Systems, Networks, Databases, Program Languages): ").lower().strip()
            if category not in categories:
                print("Invalid category. Please choose from the provided categories.")
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
            category = input("Enter the category to add a question (Computer Architeture, Operating Systems, Networks, Databases, Program Languages): ").strip()
            new_question = input("Enter the new question: ").strip()
            new_answer = input("Enter the answer to the new question: ").strip()
            add_question(category, new_question, new_answer)
        elif choice == "5":
            view_added_questions()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, 5, or 6.\n")

    # Save the added questions before exiting
    save_added_questions()

if __name__ == "__main__":
    main()

