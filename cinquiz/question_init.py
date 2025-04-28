# Run this to create a new questions.json that the app requires to read from.

from pathlib import Path
import json

file_location = Path("./questions.json")
json_data = ""

quiz_data = [
    [
        {"question_text": "Q1: What is the capital of New York?"},
        {"options": ["New Delhi", "Albany", "Austin", "Little Rock"]},
        {"correct_option_index": 1},
    ],
    [
        {"question_text": "Q2: Who is the main character of Kung Fu Panda?"},
        {"options": ["Po", "Jill", "Moe", "Fifi"]},
        {"correct_option_index": 0},
    ],
    [
        {"question_text": "Q3: When was the United States founded?"},
        {"options": ["1929", "1886", "12 B.C.", "1776"]},
        {"correct_option_index": 3},
    ],
    [
        {"question_text": "Q4: How fast can bees fly on average?"},
        {"options": ["102MPH", "1MPH", "37MPH", "15MPH"]},
        {"correct_option_index": 3},
    ],
    [
        {"question_text": "Q5: Where is the car brand Toyota from?"},
        {"options": ["Africa", "Korea", "Japan", "China"]},
        {"correct_option_index": 2},
    ],
]

for i in range(len(quiz_data)):
    all_data = quiz_data[i]
    json_data = json.dumps(all_data) + "\n"

    if not file_location.is_file():
        with open(file_location, "w") as newfile:
            newfile.write(json_data)
    else:
        with open(file_location, "a") as file:
            file.write(json_data)
