import re
import json

# Parse the text to extract questions, options, and correct answers
def new_func():
    return open('Task.txt', 'r')

with new_func() as file:
    text = file.read()

questions = re.findall(r'Question ID: (\d+)\n\n(.+?)\n\nAnswer \((.)\)', text, re.DOTALL)
questions_dict = {}

# Function to solve the multiple choice question
def solve_mcq(question):
    options = re.findall(r'\(([A-D])\) (.+?)\n', question[1])
    correct_answer = question[2]
    return options, correct_answer

# Function to solve the mathematical question
def solve_math_question(question):
    question_text = question[1].strip()
    answer_text = question[2].split('\n')[0].strip()
    return question_text, answer_text

# Solve each question
for question_id, question_text, answer in questions:
    if 'matrix' in question_text:
        options, correct_answer = solve_mcq((question_id, question_text, answer))
        questions_dict[question_id] = {
            'type': 'mcq',
            'question': question_text.strip(),
            'options': options,
            'correct_answer': correct_answer
        }
    elif 'increasing' in question_text:
        question_text, answer_text = solve_math_question((question_id, question_text, answer))
        questions_dict[question_id] = {
            'type': 'math',
            'question': question_text,
            'correct_answer': answer_text
        }

# Write questions and answers to a JSON file
with open('questions.json', 'w') as json_file:
    json.dump(questions_dict, json_file, indent=4)

print("Questions and solutions have been saved to questions.json file.")
