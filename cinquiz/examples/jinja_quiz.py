from jinja2 import Environment, FileSystemLoader

questions = [
    {"question1": "What is the capital of New York?", "answer": "Albany"},
    {"question2": "Who is the main character of Kung Fu Panda?", "answer": "Po"},
    {"question3": "Where is the United States located?", "answer": "North America"},
    {"question4": "How fast can bees fly on average?", "answer": "50 MPH"},
    {"question5": "What year was YouTube created?", "answer": "2005"},
]

env = Environment(loader=FileSystemLoader("templates/"))
template = env.get_template("quiz.txt")

for question in questions:
    file = "./templates/quiz.txt"
    content = template.render(question)

    with open(file, mode="w", encoding="utf-8") as quiz:
        quiz.write(content)
        print(f"Wrote to {file}")
