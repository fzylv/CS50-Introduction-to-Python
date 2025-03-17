from project import load_questions, questions_by_difficulty, check_answer, message

def test_load_questions():
    questions = load_questions("quiz.json")
    assert isinstance(questions, list)
    assert len(questions) > 0

def test_questions_by_difficulty():
    questions = [
        {"question": "Q1", "level": "easy"},
        {"question": "Q2", "level": "medium"},
        {"question": "Q3", "level": "hard"},
    ]
    easy_questions = questions_by_difficulty(questions, "easy")
    assert len(easy_questions) == 1
    assert easy_questions[0]["level"] == "easy"

def test_check_answer():
    question = {"question": "Q1", "options": ["A", "B", "C"], "answer": "A"}
    assert check_answer(question, "A") == True
    assert check_answer(question, "B") == False

def test_message():
    assert message(10, 10, "easy") == "Perfect! Are you a wizard or something? 🧙‍♂️✨"
    assert message(8, 10, "medium") == "Amazing! You're ready for your O.W.L.s! 🦉📜"
    assert message(6, 10, "hard") == "Great job! You’re mastering advanced spells!🔥📜"
