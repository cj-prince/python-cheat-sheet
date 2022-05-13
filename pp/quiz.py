from question import Question
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b)Orange\n(c)Purple\n\n",
    "What color are bananas?\n(a) Red/Green\n(b)Yellow\n(c)Pink\n\n",
    "What color is the strewberry?\n(a) Red\n(b)Yellow\n(c) Blue\n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a"),
]


def run_quiz(questions):
    score = 0
    for question in questions:
         answer = input(question.prompt)
         if answer == question.answer:
              score += 1
    print("you got", str(score), "out of", str(len(questions)) + 'correct')


run_quiz(questions)
