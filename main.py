class Question:
  def __init__(self, question, options, answer):
      self.question = question
      self.options = options
      self.answer = answer

class Quiz:
  def __init__(self, questions):
      self.questions = [Question(**q) for q in questions]
      self.score = 0

  def start_quiz(self):
      name = input("Hello, Welcome to the game of finding the capital of countries.\nWhat is your name? ")
      print("\nWelcome", name, "\nThis is a 10-question quiz about the capital cities of countries around the world")
      for q in self.questions:
          print("\n" + q.question)
          for option in q.options:
              print(option)
          user_answer = input("Your answer: ").upper()
          if user_answer == q.answer.upper():
              print("Well done! " + user_answer + " is correct!")
              self.score += 1
          else:
              print("Sorry, but that answer was wrong.")
          print("Your current score is", self.score, "out of 10")
          print("----------------------------------------------------")
      print("\nCongratulations", name, "your score is", self.score, "out of 10")

questions = [
  {"question": "What is the capital of Turkey?", "options": ["a: Ankara", "b: Istanbul", "c: Izmir"], "answer": "a"},
  {"question": "What is the capital of Poland?", "options": ["a: Krakow", "b: Warsaw", "c: Gdansk"], "answer": "b"},
  {"question": "What is the capital of Germany?", "options": ["a: Hamburg", "b: Berlin", "c: Köln"], "answer": "b"},
  {"question": "What is the capital of Italy?", "options": ["a: Moscow", "b: Rome", "c: Berlin"],"answer": "b"},
  {"question": "What is the capital of United Kingdom?", "options": ["a: London", "b: Portsmouth", "c: Southampton"],"answer": "a"},
  {"question": "What is the capital of France?", "options": ["a: Marseille", "b: Lyon", "c: Paris"],"answer": "c"},
  {"question": "What is the capital of Azerbaijan?", "options": ["a: nakhchivan", "b: Baku", "c: Kebele"],"answer": "b"},
  {"question": "What is the capital of Spain?", "options": ["a: Barcelona", "b: Sevilla", "c: Madrid"],"answer": "c"},
  {"question": "What is the capital of Belgium?", "options": ["a: Brussels", "b: Ghent", "c: Liège"],"answer": "a"},
  {"question": "What is the capital of Denmark?", "options": ["a: Odense", "b: Copenhagen", "c: Helsingor"],"answer": "b"},
]

quiz = Quiz(questions)
quiz.start_quiz()
