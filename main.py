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
  
