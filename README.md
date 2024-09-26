
# Catechism Quiz Application

This Python program quizzes users on the Westminster Shorter Catechism. The user is prompted with a question, and they must type the first letter of each word of the correct answer. The program then provides feedback on the accuracy of the typed answer and gives a score at the end.

## Features
- Loads catechism questions and answers from `catechism.txt`.
- Users input the first letter of each word in the answer.
- The program displays colored feedback for correct and incorrect answers.
- Shows a score based on the accuracy of the user’s input.

## Requirements
- Python 3.x
- `colorama` library for colored terminal text (Windows compatibility).
- `msvcrt` library (available by default on Windows).

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/happelj/catechism-quiz.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd catechism-quiz
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python catechizer.py
   ```

## Usage

1. Enter the catechism question number you want to answer when prompted.
2. Type the first letter of each word in the answer as prompted.
3. The program will provide feedback and a final score.

## Example File Structure

```
/catechism-quiz
│── catechizer.py
│── catechism.txt
└── README.md
```

## License
This project is licensed under the MIT License.
