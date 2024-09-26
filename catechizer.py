import msvcrt
import sys
from colorama import init, Fore, Style

wrong_words = 0
percent_correct = 0

# Initialize colorama
init()

# Read the contents of the file
file_path = 'catechism.txt'  # Replace with the actual path to your file
with open(file_path, 'r') as file:
    test = file.read()

# Split the catechism into questions and answers
catechisms = {}
lines = test.splitlines()
i = 0

while i < len(lines):
    if lines[i].isdigit():  # If a number is found, it's a new question
        number = int(lines[i])
        question = lines[i + 1]
        answer = []
        i += 2
        while i < len(lines) and not lines[i].isdigit():
            answer.append(lines[i])
            i += 1
        catechisms[number] = (question, ' '.join(answer))
    else:
        i += 1

# Function to display the question and check answer
def catechism_quiz(catechism_number):
    global wrong_words
    
    if catechism_number not in catechisms:
        print("Invalid catechism number.")
        return
    
    question, answer = catechisms[catechism_number]
    
    # Display the question
    print(f"Question {catechism_number}: {question}\n")
    
    # Split the answer into words
    words = answer.split()
    output = [""] * len(words)  # To keep track of colored words
    word_index = 0  # Index to track which word to output next
    words_in_line = 0  # Counter to track the number of words printed on the current line
    
    print("Start typing the first letter of each word in the answer:")
    
    # Loop to handle input of first letters
    while word_index < len(words):
        char = msvcrt.getch().decode("utf-8").lower()  # Read one character

        if char == words[word_index][0].lower():  # Correct first letter
            output[word_index] = words[word_index] + " "
            sys.stdout.write(words[word_index] + " ")  # Print the correct word
        else:
            output[word_index] = f"{Fore.RED}{words[word_index]}{Style.RESET_ALL} "
            sys.stdout.write(f"{Fore.RED}{words[word_index]}{Style.RESET_ALL} ")  # Print the incorrect word
            wrong_words += 1

        words_in_line += 1
        
        # Check if 10 words have been printed and move to the next line
        if words_in_line == 10:
            sys.stdout.write("\n")
            words_in_line = 0  # Reset the counter after moving to the next line

        # Move to the next word
        word_index += 1
        sys.stdout.flush()  # Ensure the output is updated in real-time
    
    # After the loop, ensure that final output is clean and visible
    #sys.stdout.write("\n\nTyping complete!\n")
    sys.stdout.flush()
    
    # Calculate the percentage of correct words
    total_words = len(words)
    correct_words = total_words - wrong_words
    percent_correct = round((correct_words / total_words) * 100, 2)
    print("\n")
    print(f"You typed {correct_words} out of {total_words} words correctly.")
    print(f"Your score: {percent_correct}% correct")

# Main loop to select catechism
while True:
    try:
        catechism_number = int(input("\nEnter the catechism number (or 0 to exit): "))
        if catechism_number == 0:
            print("Exiting.")
            break
        catechism_quiz(catechism_number)
        wrong_words = 0  # Reset wrong words for the next catechism question
    except ValueError:
        print("Please enter a valid number.")
