import random
from typing import Coroutine
from user_data import players, player_genders, player_eye_colours, player_hair_colours, player_glasses, players_bald, players_facial_hair
from filter import x,test_yes, test_no
temporary_players =[]
temporary_eye_colour =[]
temporary_hair_colour=[]
temporary_gender=[]
temporary_bald = []
temporary_glasses = []
temporary_facial_hair = []
answer_options= ("Yes", "No")
question_countdown = 10

# This function is to generate a tempory lists.
def temporary_player_list(data, temp_list):
    for i in data:
        if i not in temp_list:
            temp_list.append(i)

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
                if function in question_list:
                    question_list.remove(function)
                question_countdown -= 1
                break
            else:
                question_countdown -= 1
                break
            
# This function will choose a random eye colour from the temporary_eye_colour list.
# Once the eye colour is asked it will remove it from the list so not to asked again  
def eye_question():
    try:
        random_eye_colour = random.choice(temporary_eye_colour)
        temporary_eye_colour.remove(random_eye_colour)
        question = (f"Do you have {random_eye_colour} eyes? ")
        question_generator(question, eye_question)
    except IndexError:
        question_list.remove(eye_question)
        print("hmm.. I can't think of any other eye colours")

# This function will choose a random hair colour from the temporary_hair_colour list.
# Once the hair colour is asked it will remove it from the list so not to asked again.
def hair_question():
    try:
        random_hair_colour = random.choice(temporary_hair_colour)
        temporary_hair_colour.remove(random_hair_colour)
        question = (f"Do you have {random_hair_colour} Hair? ")
        question_generator(question, hair_question)
    except IndexError:
        question_list.remove(hair_question)
        print("hmm.. I can't think of any other hair colour")

# This function will choose a random gender from the temporary_gender list.
# Once the gender has been asked it will remove it from the list so not to asked again.
def gender_question():
    try:
        random_gender = random.choice(temporary_gender)
        temporary_gender.remove(random_gender)
        question = (f"Would you classify your gender as {random_gender}? ")
        question_generator(question, gender_question)
    except IndexError:
        question_list.remove(gender_question)
        print("hmm.. I can't think of any other genders")

# This function will choose a random bald option from the temporary_bald list.
# Once the option has been asked it will remove it from the list so not to asked again.
def bald_question():
    try:
        question = (f"Are you bald? ")
        question_generator(question, bald_question)
        if  bald_question in question_list:
            question_list.remove(bald_question)
    except IndexError:
        question_list.remove(bald_question)
        print("hmm.. I can't remember if you had hair or not")

# This function will choose a random glasses option from the temporary_glasses list.
# Because this is only a Yes or No option, it will remove the function from the question list
# so not to asked again.
def glasses_question():
    try:
        question = (f"Do you wear glasses? ")
        question_generator(question, glasses_question)
        if glasses_question in question_list:
            question_list.remove(glasses_question)
    except IndexError:
        question_list.remove(glasses_question)
        print("hmm.. I can't remember if you wear glasses or not")

# This function will choose a random glasses option from the temporary_glasses list.
# Because this is only a Yes or No option, it will remove the function from the question list
# so not to asked again.
def facial_hair_question():
    try:
        question = (f"Do you have facial hair? ")
        question_generator(question, facial_hair_question)
        if facial_hair_question in question_list:
            question_list.remove(facial_hair_question)
    except IndexError:
        question_list.remove(facial_hair_question)
        print("hmm.. I can't remember if you had facial hair")


# Gererate a temporary list of players.
temporary_player_list(players,temporary_players)

# Gererate a temporary list of possible eye colours.  
temporary_list(player_eye_colours,temporary_eye_colour)

# Gererate a temporary list of passible hair colours. 
temporary_list(player_hair_colours,temporary_hair_colour)

# Gererate a temporary list of passible hair colours. 
temporary_list(player_genders,temporary_gender)

# Gererate a temporary list of passible glasses options 
temporary_list(player_glasses,temporary_glasses)

# Gererate a temporary list of passible bald options. 
temporary_list(players_bald,temporary_bald)

# Gererate a temporary list of passible facial hair options.
temporary_list(players_facial_hair,temporary_facial_hair)

#This is a list of the question fuctions that input into the question generator.
question_list = [eye_question, hair_question, gender_question, bald_question, glasses_question, facial_hair_question]

print (temporary_players)
print (temporary_eye_colour)
print (temporary_hair_colour)
print (temporary_gender)
print (temporary_bald)
print (temporary_glasses)
print (temporary_facial_hair)

# This pick a question function from the question list at random
for i in range(100):
    try:
        random.choice(question_list)()  
    except IndexError:
        print ("I've run out of question....")
        break

