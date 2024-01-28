# Set up
questions = [
    {
        "question": "What is the capital of Turkey?",
        "options": ["a: Ankara", "b: Istanbul", "c: Izmir"],
        "answer": "a"
    },
    {
        "question": "What is the capital of Poland?",
        "options": ["a: Krakow", "b: Warsaw", "c: Gdansk"],
        "answer": "b"
    },
    {
        "question": "What is the capital of Germany?",
        "options": ["a: Hamburg", "b: Berlin", "c: Köln"],
        "answer": "b"
    },
    {
        "question": "What is the capital of Italy?",
        "options": ["a: Moscow", "b: Rome", "c: Berlin"],
        "answer": "b"
    },
    {
        "question": "What's the capital of the United Kingdom?",
        "options": ["a: London", "b: Portsmouth", "c: Southampton"],
        "answer": "a"
    },
    {
      "question": "What's the capital of the France?",
      "options": ["a: Marseille", "b: Lyon", "c: Paris"],
      "answer": "c"
    }, 
    {
      "question": "What's the capital of the Azerbaijan?",
      "options": ["a: nakhchivan", "b: Baku", "c: Kebele"],
      "answer": "b"
    }, 
    {
      "question": "What's the capital of the Spain?",
      "options": ["a: Barcelona", "b: Sevilla", "c: Madrid"],
      "answer": "c"
    }, 
    {
      "question": "What's the capital of the Belgium?",
      "options": ["a: Brussels", "b: Ghent", "c: Liège"],
      "answer": "a"
    }, 
    {
      "question": "What's the capital of the Denmark?",
      "options": ["a: Odense", "b: Copenhagen", "c: Helsingor"],
      "answer": "b"
    }, 
  ]
score = 0
# Intro
name = input("Hello, Welcome to the game of finding the capital of countries. \nWhat is your name? ")
print("\nWelcome", name, "\nThis is a 10-question quiz about the capital cities of countries around the world")
# Questions
for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    user_answer = input("Your answer: ").upper()
    if user_answer == q["answer"].upper():
        print("Well done! " + user_answer + " is correct!")
        score += 1
    else:
        print("Sorry, but that answer was wrong.")
    print("Your current score is", score, "out of 10")
    print("----------------------------------------------------")
# Total
print("\nCongratulations", name, "your score is", score, "out of 10")
