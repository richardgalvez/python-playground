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
        "Q2: Who is the main character in 'Kung Fu Panda'?",
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
def home():
    session["current_question"] = 0
    session["score"] = 0
    session["user_answers"] = []
    return render_template("index.html")


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        selected_option = request.form.get("option")
        current_question_index: int = session.get("current_question", 0)
        if selected_option is not None:
            correct_option = cq.questions[current_question_index].correct_option_index
            user_option_text = cq.questions[current_question_index].options[
                int(selected_option)
            ]
            session["user_answers"].append(user_option_text)
            if int(selected_option) == correct_option:
                session["score"] += 1

        session["current_question"] += 1
        if session["current_question"] >= len(cq.questions):
            return redirect(url_for("results"))

    current_question_index: int = session.get("current_question", 0)
    question = cq.questions[current_question_index]
    return render_template("quiz.html", question=question)


@app.route("/results")
def results():
    score = session.get("score")
    total_questions = len(cq.questions)
    question = cq.questions
    return render_template(
        "results.html",
        score=score,
        total_questions=total_questions,
        question=question,
        current_question=session["current_question"],
        user_answers=session["user_answers"],
    )


if __name__ == "__main__":
    app.run(debug=True)
