# Processing code written in Python mode

#import the shuffle function from the random module and rename it to random_shuffle
from random import shuffle as random_shuffle

class Question:
  def __init__(self, equation, correct_answers):
    self.equation = equation   #store the equation of the question
    self.correct_answers = correct_answers  #store the correct answers for the question

class Button:
  def __init__(self, label, x, y, w, h):
    self.label = label  #the text label of the button
    self.x = x  #the x-coordinate of the button
    self.y = y  #the y-coordinate of the button
    self.w = w  #the width of the button
    self.h = h  #the height of the button
    self.selected = False  #boolean to track if the button is selected

#display method inside the button class
def display(self):
  if self.selected:
    fill(100, 100, 255)
  elif self.is_hovered():
    fill(250, 255, 90)
  else:
    fill(145, 232, 31)
  rect(self.x, self.y, self.w, self.h, 5)
  fill(0)
  textSize (16)
  textalign(CENTER, CENTER)
  text(self. label, self.x + self.w / 2, self.y + self.h / 2)


def is_clicked(self, mx, my):
  return self.x ‹= mx ‹= self.x + self.w and self.y ‹= my <= self.y + self.h

def is_hovered(self):
  return self.x <= mouseX <= self.x + self.w and self.y ‹= mouseY <= self.y + self.h

def setup():
  size(600, 600)
  global game_state, score, question_index, questions, answered_questions, selected_answers
  game_state = 'start'
  score = 0
  question_index = 0
  answered_questions = []
  selected_answers = []
  questions = [
    Question("(x + 1)(x + 1) = 0", [-1, -1]),
    Question("x^2 - 16 = 0", [-4, 4]),
    Question("x^2 - 4x + 4 = 0", [2, 2]),
    Question("x^2 + 8x + 15 = 0", [5, -3]),
    Question("(x + 2)(x + 1) = 0", [-2, 1]),
    Question("x^2 - 9 = 0", [-3, 3]),
    Question("2x^2 - 22x + 48 = 0", [8, 3]),
    Question("x^2 + 2x - 3 = 0", [-3, 1]),
    Question("(x + 1)(x - 2) = 0", [-1, 2]),
    Question("x^2 + 5x + 6 = 0", [-3, 2]),
  ]
  global button_start, button_instructions, button_answers
  button_start = Button("Click to Play", 252, 380, 120, 50)
  button_instructions = Button("Instructions", 252, 460, 120, 50)
  button_answers = [
    Button("", 100, 300, 120, 50),
    Button("", 250, 300, 120, 50),
    Button("", 400, 300, 120, 50),
    Button("", 100, 400, 120, 50),
    Button("", 250, 400, 120, 50),
    Button("", 400, 400, 120, 50),
  ]
  generate_question()

def draw():
  if game_state == 'start':
    start_screen()
  elif game_state == 'instructions':
    instructions_screen()
  elif game_state == 'game':
    game_screen()
  elif game_state == 'feeback':
    feedback_screen()
  elif game_state == 'end':
    end_screen()

def start_screen():
  img = loadImage("startimage.jpg")
  image(img, 0, 0, 600, 600)
  textSize(32)
  textAlign(CENTER, CENTER)
  fill(255)
  text("Quadratic Nerds", width / 2, 250)
  button_start.display()
  button_instructions.display()

def instructions_screen():
  img = loadImage("instructionsimage.jpg")
  image(img, 0, 0, 600, 600)
  fill(255)
  textSize(32)
  textAlign(CENTER, CENTER)
  text("Instructions", width / 2, 100)
  textSize(16)
  text("Welcome to Grade 10 Math!\nToday you will learn about solving and factoring equations.\n \nHere are the instructions to the game:\n1. You will be given a quadratic equation either factored or not.\n2. Choose the two correct answers by clicking on the button.\n3. Click 'n' to move to the next question.\n4. Your score will be tracked.\n5. The game ends after 10 questions.\n6. Have fun learning!", width / 2, height / 2)
  textSize(20)
  fill(255)
  text("Press 'b' To Go Back", width / 2, height - 100)

def game_screen():
  img = loadImage("gameimage.jpg")
  image(img, 0, 0, 600, 600)
  textSize(32)
  textAlign(CENTER, CENTER)
  fill(255)
  text("Solve: " + questions[questions_index].equation, width / 2, 200)
  for button in button_answers:
    button.display()
  textSize(20)
  fill(255)
  text("Score: " + str(score), width - 70, 30)
  text("Question: " + str(question_index + 1) + "/10", width - 100, 60)
  text("Press 'b' To Go Back", width / 2, height - 50)

def feedback_screen():
  img = loadImage("gameimage.jpg")
  image(img, 0, 0, 600, 600)
  textSize(32)
  textAlign(CENTER, CENTER)
  fill(255)
  correct_answers_str = ', '.join(map(str, questions[questions_index].correct_answers))
  text("Correct Answers: " + correct_answers_str, width / 2, height / 2)
  textSize(20)
  fill(255)
  text("Score: " + str(score), width - 70, 30)
  if question_index < len(questions):
    fill(255)
    text("Press 'n' For Next Question", width / 2, height - 50)
  fill(255)
  text("Press 'b' To Go Back", width / 2, height - 50)

def end_screen():
  img = loadImage("gameimage.jpg")
  image(img, 0, 0, 600, 600)
  textSize(32)
  textAlign(CENTER, CENTER)
  fill(255)
  text("Game Over!", width / 2, height / 2 - 50)
  text("Your Final Score Is: " + str(score), width / 2, height / 2)
  textSize(20)
  fill(255)
  text("Thanks For Playing!!! \nPress 'b' To Go Back To Start", width / 2, height - 50)

def generate_question():
  global question, options, questions
  random_shuffle(questions)
  question = question[questions_index]
  options = [question.correct_answers[0], question.correct_answers[1], question.correct_answers[0] + 1, question.correct_answers[1] + 1, question.correct_answers[0] - 1, question.correct_answers[1] - 1]
  random_shuffle(options)
  for i in range(6):
    button_answers[i].label = str(options[i])
    button_answers[i].selected = False

def mouse_pressed():
  global game_state, score, selected_answers
  if game_state == 'start':
    if button_start.is_clicked(mouseX, mouseY):
      game_state = 'game'
    elif button_instructions.is_clicked(mouseX, mouseY):
      game_state = 'instructions'
  elif game_state == 'game':
    for button in button_answers:
      if button.is_clicked(mouseX, mouseY):
        if button.selected:
          button.selected = False
          if int(button.label) in selected_answers:
            selected_answers.remove(int(button.label))
        else:
          button.selected = True
          selected_answers.append(int(button.lable))
        if len(selected_answers) == 2:
          check_answers()

def key_pressed():
  global game_state, question_index, score, selected_answers, answered_questions
  if key == 'b':
    game_state = 'start'
    question_index = 0
    score = 0
    answered_questions = []
    selected_answerrs = []
    generate_question()
  elif key == 'n' and game_state = 'feedback':
    if question_index >= len(questions) - 1:
      game_state = 'end'
    else:
      question_index += 1
      selected_answers = []
      question = questions[question.index]
      options = [question.correct_answers[0], question.correct_answers[1], question.correct_answers[0] + 1, question.correct_answers[1] + 1, question.correct_answers[0] - 1, question.correct_answers[1] - 1]
      random_shuffle(options)
      for i in range(6):
        button_answers[i].label = str(options[i])
        button_answers[i].selected = False
      game_state = 'game'

def check_answers():
  global game_state, score
  correct = questions[question_index].correct_answers
  if sorted(selected_answers) == sorted(correct):
    score += 1
  answered_questions.append(question_index)
  game_state = 'feedback'

def shuffle(lst):
  for i in range(len(lst)- 1, 0 - 1):
    j = int(random(0, i + 1))
    lst[i], lst[j] = lst[j], lst[i]
