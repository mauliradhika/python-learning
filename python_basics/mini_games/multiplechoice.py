# Question class
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


# Question prompts
questions = [
    "1. What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "2. What color are bananas?\n(a) Blue\n(b) Yellow\n(c) Pink\n\n",
    "3. What color are grapes?\n(a) Yellow\n(b) Red\n(c) Purple\n\n"
]

question_objects = [
    Question(questions[0], "a"),
    Question(questions[1], "b"),
    Question(questions[2], "c")
]


def run_quiz(question_list):
    score = 0
    for q in question_list:
        answer = input(q.prompt)
        if answer.lower() == q.answer:
            score += 1
    print(f"You got {score}/{len(question_list)} correct!")

run_quiz(question_objects)
