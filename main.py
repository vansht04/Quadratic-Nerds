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
    fill(100, 100, 255)  #blue color if the button is selected
  elif self.is_hovered():
    fill(250, 255, 90)  #yellow color if the button is hovered
  else:
    fill(145, 232, 31)  #green color for the default state
  rect(self.x, self.y, self.w, self.h, 5)  #draw the button rectangle
  fill(0)
  textSize (16)
  textalign(CENTER, CENTER)
  text(self. label, self.x + self.w / 2, self.y + self.h / 2)  #draw the label text

def is_clicked(self, mx, my):
  return self.x ‹= mx ‹= self.x + self.w and self.y ‹= my <= self.y + self.h  #check if button is clicked

def is_hovered(self):
  return self.x <= mouseX <= self.x + self.w and self.y ‹= mouseY <= self.y + self.h  #check if the button is hovered

def setup():
  size(600, 600)  #set size of the window
  global game_state, score, question_index, questions, answered_questions, selected_answers
  game_state = 'start'  #inital game state
  score = 0  #initial score
  question_index = 0  #index of current question
  answered_questions = []  #to track the answered questions
  selected_answers = []  #to track selected answers
  questions = [  #list of questions with their correct answers
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
  button_start = Button("Click to Play", 252, 380, 120, 50)  #create the start button
  button_instructions = Button("Instructions", 252, 460, 120, 50)  #create the instructions button
  button_answers = [  #create the answer buttons
    Button("", 100, 300, 120, 50),
    Button("", 250, 300, 120, 50),
    Button("", 400, 300, 120, 50),
    Button("", 100, 400, 120, 50),
    Button("", 250, 400, 120, 50),
    Button("", 400, 400, 120, 50),
  ]
  generate_question()  #generate the first question

def draw():
  if game_state == 'start':
    start_screen()  #display the start screen
  elif game_state == 'instructions':
    instructions_screen()  #display the instructions screen
  elif game_state == 'game':
    game_screen()  #display the game screen
  elif game_state == 'feeback':
    feedback_screen()  #display the feedback screen
  elif game_state == 'end':
    end_screen()  #display the end screen

def start_screen():
  img = loadImage("startimage.jpg")  #load the start screen image
  image(img, 0, 0, 600, 600)  #display the start screen image
  textSize(32)
  textAlign(CENTER, CENTER)
  fill(255)
  text("Quadratic Nerds", width / 2, 250)  #display the game title
  button_start.display()  #display the start button
  button_instructions.display()  #display the instructions button

def instructions_screen():
  img = loadImage("instructionsimage.jpg")  #load the instructions screen image
  image(img, 0, 0, 600, 600)  #display the instructions screen image
  fill(255)
  textSize(32)
  textAlign(CENTER, CENTER)
  text("Instructions", width / 2, 100)  #display the instructions title
  textSize(16)
  text("Welcome to Grade 10 Math!\nToday you will learn about solving and factoring equations.\n \nHere are the instructions to the game:\n1. You will be given a quadratic equation either factored or not.\n2. Choose the two correct answers by clicking on the button.\n3. Click 'n' to move to the next question.\n4. Your score will be tracked.\n5. The game ends after 10 questions.\n6. Have fun learning!", width / 2, height / 2)
  textSize(20)
  fill(255)
  text("Press 'b' To Go Back", width / 2, height - 100)  #display the back button text

def game_screen():
  img = loadImage("gameimage.jpg")  #load the game screen image
  image(img, 0, 0, 600, 600)  #display the game screen image
  textSize(32)
  textAlign(CENTER, CENTER)
  fill(255)
  text("Solve: " + questions[questions_index].equation, width / 2, 200)  #display the current question
  for button in button_answers:
    button.display()  #display the answer buttons
  textSize(20)
  fill(255)
  text("Score: " + str(score), width - 70, 30)  #display the current score
  text("Question: " + str(question_index + 1) + "/10", width - 100, 60)  #display the current question number
  text("Press 'b' To Go Back", width / 2, height - 50)  #display the back button text

def feedback_screen():
  img = loadImage("gameimage.jpg")  #load the feedback screen image
  image(img, 0, 0, 600, 600)  #display the feedback screen image
  textSize(32)
  textAlign(CENTER, CENTER)
  fill(255)
  correct_answers_str = ', '.join(map(str, questions[questions_index].correct_answers))  #create a string of correct answers
  text("Correct Answers: " + correct_answers_str, width / 2, height / 2)  #display the correct answers
  textSize(20)
  fill(255)
  text("Score: " + str(score), width - 70, 30)  #display the current score
  if question_index < len(questions):
    fill(255)
    text("Press 'n' For Next Question", width / 2, height - 50)  #display the next question prompt
  fill(255)
  text("Press 'b' To Go Back", width / 2, height - 50)  #display the back button text

def end_screen():
  img = loadImage("gameimage.jpg")  #load end screen image
  image(img, 0, 0, 600, 600)  #display end screen image
  textSize(32)
  textAlign(CENTER, CENTER)
  fill(255)
  text("Game Over!", width / 2, height / 2 - 50)  #display the game over message
  text("Your Final Score Is: " + str(score), width / 2, height / 2)  #display the final score
  textSize(20)
  fill(255)
  text("Thanks For Playing!!! \nPress 'b' To Go Back To Start", width / 2, height - 50) #display the thank you message

def generate_question():
  global question, options, questions
  random_shuffle(questions)  #shuffle the questions
  question = question[questions_index]  #select the current questions
  options = [question.correct_answers[0], question.correct_answers[1], question.correct_answers[0] + 1, question.correct_answers[1] + 1, question.correct_answers[0] - 1, question.correct_answers[1] - 1]
  random_shuffle(options)  #shuffle the answer options
  for i in range(6):
    button_answers[i].label = str(options[i])  #assign the labels to the answer buttons
    button_answers[i].selected = False  #set the selected state of the buttons to false

def mouse_pressed():
  global game_state, score, selected_answers
  if game_state == 'start':
    if button_start.is_clicked(mouseX, mouseY):
      game_state = 'game'  #switch to game state if the start button is clicked
    elif button_instructions.is_clicked(mouseX, mouseY):
      game_state = 'instructions'  #switch to instructions state if the instructions button is clicked
  elif game_state == 'game':
    for button in button_answers:
      if button.is_clicked(mouseX, mouseY):
        if button.selected:
          button.selected = False  #deselect the button if it was already selected
          if int(button.label) in selected_answers:
            selected_answers.remove(int(button.label))  #remove the answer from selected answers
        else:
          button.selected = True  #select the button 
          selected_answers.append(int(button.lable))  #add the answer to selected answers
        if len(selected_answers) == 2:
          check_answers()  #check the answers if two are selected

def key_pressed():
  global game_state, question_index, score, selected_answers, answered_questions
  if key == 'b':
    game_state = 'start'  #switch to start state
    question_index = 0  #reset questions index
    score = 0  #reset score
    answered_questions = []  #clear answered questions
    selected_answerrs = []  #clear selected answers
    generate_question()  #generate a new question
  elif key == 'n' and game_state = 'feedback':
    if question_index >= len(questions) - 1:
      game_state = 'end'  #switch to end state if all questions are answered
    else:
      question_index += 1  #move to next question
      selected_answers = []  #clear selected answers
      question = questions[question.index]  #select the next question
      options = [question.correct_answers[0], question.correct_answers[1], question.correct_answers[0] + 1, question.correct_answers[1] + 1, question.correct_answers[0] - 1, question.correct_answers[1] - 1]
      random_shuffle(options)   #shuffle the answer options
      for i in range(6):
        button_answers[i].label = str(options[i])  #assign the labels to answer buttons
        button_answers[i].selected = False  #set the selected state of the buttons to false
      game_state = 'game'  #switch to game state

def check_answers():
  global game_state, score
  correct = questions[question_index].correct_answers  #get the correct answers for the current question
  if sorted(selected_answers) == sorted(correct):
    score += 1  #increase score if the selected answers are correct
  answered_questions.append(question_index)  #add the question to answered questions
  game_state = 'feedback'  #switch to feedback state

def shuffle(lst):
  for i in range(len(lst)- 1, 0 - 1):
    j = int(random(0, i + 1))
    lst[i], lst[j] = lst[j], lst[i]  #swap the elements
