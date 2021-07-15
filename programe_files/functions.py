import random
import os
from user_data import *
from question_generator import *

def player_name():
    while True:
        userinput = input("What is your full name? ").capitalize()
        os.system('cls||clear')
        if " " not in userinput:
            print ("Don't forget your last name.\n")            
        else:
            global name 
            name = userinput
            players.append(name)
            os.system('cls||clear')
            break

def user_input(category, error_message, feature_list, feature_options ): 
    while True:
        userinput = input(f"{category}").capitalize()
        os.system('cls||clear')
        if userinput not in feature_options:
            print (error_message)
            print (', '.join(feature_options)+"\n")
        else:            
            feature_list[name] = userinput
            os.system('cls||clear')
            break

# This function is to generate a temporary lists.
def temporary_player_list(data, temp_list):
    for i in data:
        if i not in temp_list:
            temp_list.append(i)

# It takes the players category and makes a list of the different options. 
# It ensure there is no double up in the list.  
def temporary_list(data, temp_list):
    for i in data.values():
        if i not in temp_list:
            temp_list.append(i)
      
# This function is to generate random NAME for the user to answer.
def name_question ():
    try:
        random_name = random.choice(temporary_players_options)
        temporary_players_options.remove(random_name)
        global feature_guesses
        feature_guesses = 0      
        while True:            
            answer = input (f"Is your name {random_name} ? ").capitalize()
            if answer not in answer_options:
                print ("Please type Yes or No")
            elif answer == "Yes":
                os.system('cls||clear')
                print (f"Oh hey there {random_name}")
                return True
                
            else:
                os.system('cls||clear')
                print ("hmm let me keep trying")
                return False

    except IndexError:                
        print("hmm.. I can't think of your name")
        

# This function is to generate random question for the user to answer.
# ONLY WORKS FOR DICTIONARIES
def question_generator(question_to_user, question_function, user_data, option):
        while True:
            answer = input (question_to_user).capitalize()
            if answer not in answer_options:
                print ("Please type Yes or No")
            elif answer == "Yes":
                #This loop will remove any players name that DONT match to uses answer.
                players_to_remove = [name for (name, value) in user_data.items() if value != option]
                for names in players_to_remove:
                    if names in temporary_players_options:
                        temporary_players_options.remove(names)
                #Because the player does match the criteria the question shouldn't be asked again.
                global question_list, feature_guesses
                if question_function in question_list:
                    question_list.remove(question_function) 
                feature_guesses += 1
                break
            else:
                #This loop will remove any players name that DO match to uses answer
                players_to_remove = [name for (name, value) in user_data.items() if value == option]
                for names in players_to_remove:
                    if names in temporary_players_options:
                        temporary_players_options.remove(names)
                print (temporary_players_options)
                feature_guesses += 1
                break
            
# This function will choose a random eye colour from the temporary_eye_colour list.
# Once the eye colour is asked it will remove it from the list so not to asked again  
def eye_question():
    try:
        random_eye_colour = random.choice(temporay_eye_colour_options)
        temporay_eye_colour_options.remove(random_eye_colour)
        question = (f"Do you have {random_eye_colour} eyes? ")
        question_generator(question, eye_question, player_eye_colours, random_eye_colour)
    except IndexError:
        question_list.remove(eye_question)        
        print("hmm.. I can't think of any other eye colours")

# This function will choose a random hair colour from the temporary_hair_colour list.
# Once the hair colour is asked it will remove it from the list so not to asked again.
def hair_question():
    try:
        random_hair_colour = random.choice(temporary_hair_colour_options)
        temporary_hair_colour_options.remove(random_hair_colour)
        question = (f"Do you have {random_hair_colour} Hair? ")
        question_generator(question, hair_question, player_hair_colours, random_hair_colour)
    except IndexError:
        question_list.remove(hair_question)
        print("hmm.. I can't think of any other hair colour")

# This function will choose a random gender from the temporary_gender list.
# Once the gender has been asked it will remove it from the list so not to asked again.
def gender_question():
    try:
        random_gender = random.choice(temporary_gender_options)
        temporary_gender_options.remove(random_gender)
        question = (f"Would you classify your gender as {random_gender}? ")
        question_generator(question, gender_question, player_genders, random_gender)
    except IndexError:
        question_list.remove(gender_question)
        print("hmm.. I can't think of any other genders")

# This function will choose a random bald option from the temporary_bald list.
# Once the option has been asked it will remove it from the list so not to asked again.
def bald_question():
    try:
        question = (f"Are you bald? ")
        question_generator(question, bald_question, players_bald,"Yes")
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
        question_generator(question, glasses_question, player_glasses, "Yes")
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
        question_generator(question, facial_hair_question, players_facial_hair, "Yes")
        if facial_hair_question in question_list:
            question_list.remove(facial_hair_question)
    except IndexError:
        question_list.remove(facial_hair_question)
        print("hmm.. I can't remember if you had facial hair")

