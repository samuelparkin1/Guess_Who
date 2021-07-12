import random
from typing import Coroutine
from user_data import player_genders, player_eye_colours, player_hair_colours
from filter import x,test_yes, test_no
temporary_players =[]
temporary_eye_colour =[]
temporary_hair_colour=["Black", "Brown", "Blonde", "White", "Grey", "Red", "Pink", "Purple", "Blue", "Green", "Yellow"]
temporary_gender=["Male", "Female", "Other"]
temporary_bald = ["Yes", "No"]
temporary_glasses = ["Yes", "No"]
temporary_facial_hair = ["Yes", "No"]
answer_options= ("Yes", "No")
question_countdown = 10

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
                break
            else:
                question_countdown -= 1
                break
            

def eye_question():
    try:
        random_eye_colour = random.choice(temporary_eye_colour)
        temporary_eye_colour.remove(random_eye_colour)
        question = (f"Do you have {random_eye_colour} eyes? ")
        question_generator(question, eye_question)
    except IndexError:
        question_list.remove(eye_question)
        print("hmm.. I can't think of any other eye colours")

def hair_question():
    try:
        random_hair_colour = random.choice(temporary_hair_colour)
        temporary_hair_colour.remove(random_hair_colour)
        question = (f"Do you have {random_hair_colour} Hair? ")
        question_generator(question, hair_question)
    except IndexError:
        question_list.remove(hair_question)
        print("hmm.. I can't think of any other hair colour")

def gender_question():
    try:
        random_gender = random.choice(temporary_gender)
        temporary_gender.remove(random_gender)
        question = (f"Would you classify your gender as {random_gender}? ")
        question_generator(question, gender_question)
    except IndexError:
        question_list.remove(gender_question)
        print("hmm.. I can't think of any other genders")

def bald_question():
    try:
        question = (f"Are you bald? ")
        question_generator(question, bald_question)
        question_list.remove(bald_question)
    except IndexError:
        question_list.remove(bald_question)
        print("hmm.. I can't remember if you had hair or not")

def glasses_question():
    try:
        question = (f"Do you wear glasses? ")
        question_generator(question, glasses_question)
        question_list.remove(glasses_question)
    except IndexError:
        question_list.remove(glasses_question)
        print("hmm.. I can't remember if you wear glasses or not")

def facial_hair_question():
    try:
        question = (f"Do you have facial hair? ")
        question_generator(question, facial_hair_question)
        question_list.remove(facial_hair_question)
    except IndexError:
        question_list.remove(facial_hair_question)
        print("hmm.. I can't remember if you had facial hair")


# Gererate a temporary list of possible eye colours.  
temporary_list(player_eye_colours,temporary_eye_colour)

# Gererate a temporary list of passible hair colours. 
temporary_list(player_hair_colours,temporary_hair_colour)

# Gererate a temporary list of passible hair colours. 
temporary_list(player_genders,temporary_gender)


question_list = [eye_question, hair_question, gender_question, bald_question, glasses_question, facial_hair_question]
#select a question at random 

for i in range(100):
    try:
        random.choice(question_list)()  
    except IndexError:
        print ("I've run out of question....")
        break

