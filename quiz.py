questions = [
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "What language is this written in?", "answer": "python"}
]

score = 0

for items in questions:
    user = input(items["question"] + " What is your answer: ")

    if user.lower() == items["answer"]:
        score += 1
        print("Correct!")
    else:
        print(f"Wrong! Answer was {items['answer']}")

print(f"Total score is: {score}")
        

    
