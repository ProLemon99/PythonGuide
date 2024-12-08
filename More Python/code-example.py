# Basic Quiz
print("Welcome to the Basic Quiz!")

answers={
    'a':'a) Paris',
    'b':'b) London',
    'c':'c) Berlin',
    'd':'d) Rome'
    }

question = "What is the capital of France"
print(f"Question: {question}")
print("a) Paris\nb) London\nc) Berlin\nd) Rome")

inp = input(f"Enter your answer (a, b, c, or d): ")
answer='a'
if inp in answers:
    inp = answers[inp]
else:
    print("Invalid selection")

print("\nQuiz Results:")
print(f"Question {question}")
print(f"Your answer: {inp}")
print(f"Correct answer: {answers.get(answer)}")

if inp == answers.get(answer):
    print("Correct!!")
else:
    print(f"Incorrect. The correct answer is {answers.get(answer)}")