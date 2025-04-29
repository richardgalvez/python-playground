from flask import Flask, render_template, request, redirect, url_for, session
from quiz import Cinquiz, Question

app = Flask(__name__)
app.secret_key = "CINQUIZ_KEY"

cq = Cinquiz()

cq.add_question(
    Question(
        "Q1: What is the capital of New York?",
        ["Trenton", "Albany", "Austin", "Atlanta"],
        1,
    )
)
cq.add_question(
    Question(
        "Q2: Who is the main character of Kung Fu Panda?",
        ["Po", "Jill", "Moe", "Fifi"],
        0,
    )
)
cq.add_question(
    Question(
        "Q3: When was the United States founded?", ["1929", "1886", "1492", "1776"], 3
    )
)
cq.add_question(
    Question(
        "Q4: How fast can bees fly on average?", ["102MPH", "4MPH", "27MPH", "15MPH"], 3
    )
)
cq.add_question(
    Question(
        "Q5: Where does the car brand Toyota originate from?",
        ["Africa", "India", "Japan", "China"],
        2,
    )
)


@app.route("/")
def index():
    session["current_question"] = 0
    session["score"] = 0
    return redirect(url_for("quiz"))


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        selected_option = request.form.get("option")
        current_question_index = session.get("current_question")
        if selected_option is not None:
            correct_option = cq.questions[current_question_index].correct_option_index
            if int(selected_option) == correct_option:
                session["score"] += 1

        session["current_question"] += 1
        if session["current_question"] >= len(cq.questions):
            return redirect(url_for("results"))

    current_question_index = session.get("current_question")
    question = cq.questions[current_question_index]
    return render_template(
        "quiz.html",
        question=question,
        question_index=current_question_index + 1,
        total_questions=len(cq.questions),
    )


@app.route("/results")
def results():
    score = session.get("score")
    total_questions = len(cq.questions)
    return f"<h1>Your Score: {score}/{total_questions}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
