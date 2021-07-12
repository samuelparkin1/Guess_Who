import random
from typing import Coroutine
from user_data import player_genders, player_eye_colours, player_hair_colours
from filter import x,test_yes, test_no
temporary_eye_colour =[]
random_eye_colour =[]
temporary_hair_colour=["Black", "Brown", "Blonde", "White", "Grey", "Red", "Pink", "Purple", "Blue", "Green", "Yellow"]
temporary_gender=[]
answer_options= ("Yes", "No")

question_countdown = 10

# name = []

# player_genders= {}
# genders=("Male", "Female", "Other")

# player_eye_colours = {'john':"green", 'sam': "green", 'tom': "blue", 'jim': "brown"}
# eye_colours = ("Amber","Blue","Brown", "Gray", "Green", "Hazel")

# player_hair_colours = {}
# hair_colours =("Black", "Brown", "Blonde", "White", "Grey", "Red", "Pink", "Purple", "Blue", "Green", "Yellow")

# players_glasses ={}
# glasses_options = ("Yes", "No")

# players_bald ={}
# bald_options=("Yes","No")

# players_facial_hair ={}
# facial_hair_options=("Yes","No")


# This function is to generate a tempory lists. 
# It takes fasical catgoryies and makes a list of the differnt options within then.  
def temporary_list(data, temp_list):
    for i in data.values():
        if i not in temp_list:
            temp_list.append(i)


# This function is to generate random question for the user to answer.
def question_generator(question, function):
        while True:
            answer = input (question).capitalize()
            if answer not in answer_options:
                print ("Please type Yes or No")
            elif answer == "Yes":
                global question_list, question_countdown
                question_list.remove(function)
                question_countdown -= 1
                print ("yes")
            else:
                question_countdown -= 1
                print ("no")
            break

def eye_question():
    try:
        random_eye_colour = random.choice(temporary_eye_colour)
        temporary_eye_colour.remove(random_eye_colour)
        question = (f"Do you have {random_eye_colour} eyes?")
        question_generator(question, eye_question)
    except IndexError:
        question_list.remove(eye_question)
        print("hmm.. I can't think of any other eye colours")

def hair_question():
    try:
        global random_hair_colour
        random_hair_colour = random.choice(temporary_hair_colour)
        temporary_hair_colour.remove(random_hair_colour)
        question = (f"Do you have {random_hair_colour} Hair?")
        question_generator(question, hair_question)
    except IndexError:
        question_list.remove(hair_question)
        print("hmm.. I can't think of any other hair colour")
        
    

# def bald_question():


# def glasses_question():

# def facial_hair_question():

# def gender_question():







# Gererate a temporary list of possible eye colours.  
temporary_list(player_eye_colours,temporary_eye_colour)

# Gererate a temporary list of passible hair colours. 
temporary_list(player_hair_colours,temporary_hair_colour)

# Gererate a temporary list of passible hair colours. 
temporary_list(player_genders,temporary_gender)


question_list = [eye_question, hair_question]
#  gender_question, bald_question, glasses_question, facial_hair_question]
#select a question at random  
next_question = random.choice(question_list)
  #Mixes the items in "questions" into a random order


# print (questions[0])
# print (questions[1])
# print (questions[2])
try:
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
    random.choice(question_list)()
except IndexError:
    "I've run out of question...."

