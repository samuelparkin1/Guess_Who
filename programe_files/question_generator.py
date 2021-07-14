import random
from typing import Coroutine, Counter
from user_data import players, player_genders, player_eye_colours, player_hair_colours, player_glasses, players_bald, players_facial_hair
#from filter import x,test_yes, test_no
temporary_players_options =[]
temporay_eye_colour_options =[]
temporary_hair_colour_options=[]
temporary_gender_options=[]
temporary_bald_options = []
temporary_glasses_options = []
temporary_facial_hair_options = []
answer_options= ("Yes", "No")
feature_guesses = 0

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
                print (f"Oh hey there {random_name}")
                return True
                
            else:
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
                print (temporary_players_options)  
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
        question_generator(question, facial_hair_question, player_hair_colours, "Yes")
        if facial_hair_question in question_list:
            question_list.remove(facial_hair_question)
    except IndexError:
        question_list.remove(facial_hair_question)
        print("hmm.. I can't remember if you had facial hair")


    #Ask the user if they're ready to play.
    play_agin = "Yes"
    player_ready = input ("Ready to play guess who?")
    while player_ready == "Yes" and play_agin == "Yes":
        
        feature_guesses = 0

        # Gererate a temporary list of players.
        temporary_player_list(players,temporary_players_options)

        # Gererate a temporary list of possible eye colours.  
        temporary_list(player_eye_colours,temporay_eye_colour_options)

        # Gererate a temporary list of passible hair colours. 
        temporary_list(player_hair_colours,temporary_hair_colour_options)

        # Gererate a temporary list of passible hair colours. 
        temporary_list(player_genders,temporary_gender_options)

        # Gererate a temporary list of passible glasses options 
        temporary_list(player_glasses,temporary_glasses_options)

        # Gererate a temporary list of passible bald options. 
        temporary_list(players_bald,temporary_bald_options)

        # Gererate a temporary list of passible facial hair options.
        temporary_list(players_facial_hair,temporary_facial_hair_options)

        #This is a list of the question functions that input into the question generator.
        question_list = [eye_question, hair_question, gender_question, bald_question, glasses_question, facial_hair_question]

        # print (temporary_players_options)
        # print (temporary_eye_colour_options)
        # print (temporary_hair_colour_options)
        # print (temporary_gender_options)
        # print (temporary_bald_options)
        # print (temporary_glasses_options)
        # print (temporary_facial_hair_options)
        print (int(feature_guesses))

        # This loops starts asking the user random questions.
        
        while True:
            try:
                if int(feature_guesses) < 3 and len (question_list) > 1 and len(temporary_players_options) > 2:
                    random.choice(question_list)()
                    print (int(feature_guesses))
                        
                else:
                    if len(temporary_players_options) > 0:
                        if name_question() == True:
                            break                
                    else:
                        print("Seems like you slipped my detection")
                        break                     
        
            except IndexError:
                print ("I've run out of question....")
                break

        play_agin = input ("Play again?")      

