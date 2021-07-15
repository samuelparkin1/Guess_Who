import random
import os
from user_data import *

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
    try:
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
    except NameError:
        print ("Unable to find user_data.py")


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
    except NameError:
        print ("Unable to find user_data.py")

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
    except NameError:
        print ("Unable to find user_data.py")

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
    except NameError:
        print ("Unable to find user_data.py")

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
    except NameError:
        print ("Unable to find user_data.py")

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
    except NameError:
        print ("Unable to find user_data.py")

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
    except NameError:
        print ("unable to find user_data.py")

# while the run_game is "Yes" to game will continue to play"
run_game = "Yes"
play_again = []
new_game = []
while run_game == 'Yes':
    os.system('cls||clear')
    print("""   _____                      __     __           ___  
  / ____|                     \ \   / /          |__ \ 
 | |  __ _   _  ___  ___ ___   \ \_/ /__  _   _     ) |
 | | |_ | | | |/ _ \/ __/ __|   \   / _ \| | | |   / / 
 | |__| | |_| |  __/\__ \__ \    | | (_) | |_| |  |_|  
  \_____|\__,_|\___||___/___/    |_|\___/ \__,_|  (_)  """)

    print ("""
                Created by Sam Parkin""")
    userinput = input("""
                Would you like to play?
                Please enter Yes / Exit.\n
                        """).capitalize()
    
    if userinput not in ["Yes" , "Exit"]:
        os.system('cls||clear')
        print ("Please enter Yes or Exit" )

    elif userinput == "Yes":
        run_game = userinput          
        new_game = userinput
        os.system('cls||clear')

        #This will ask the user for information out them to store in user_data.py
        while run_game == "Yes" and new_game == "Yes":
            try:
                #clear terminal window
                os.system('cls||clear')
                #Welcome message
                print ("Hi and welcome to Guess Who!")
                print ("Before we move on, I just need to know a little about you.\n")
                #get user name
                player_name()
                #user to enter gender 
                user_input("What is your gender? ", "Please select from the following options: ", player_genders, genders)
                #user to put in their eye colour. 
                user_input("What colour eyes do you have? ", "Which eye colour is closest to yours: ", player_eye_colours, eye_colours)
                #user to put in their hair colour. 
                user_input("What colour hair do you have? ", "Which hair colour is closest to yours: ",player_hair_colours, hair_colours)
                #ask user if they wear glasses.
                user_input("Do you wear glasses? ","Please enter", player_glasses, glasses_options)
                #ask user if they're bald.
                user_input("Would you say you're bald? ","Please enter", players_bald, bald_options)
                #ask user if they're bald.
                user_input("Lastly, Do you have facial hair? ","Please enter", players_facial_hair, facial_hair_options)
                    #Ask the user if they're ready to play.

                # Will ask the user if they want to add another player or contine. Also allows the user to exit to the main menu.    
                while True:
                    print ("Thanks for that!\n")
                    print ("My friend, Inspector Bot, considers themselves as a real Sherlock Holmes and believe they can find anybody!")
                    print ("Inspector Bot is going to ask some random question to guess who you are.")
                    userinput = input("\nAre you ready to play Guess You against Inspector Bot or would you like to add another player?\n\nYes, Add or Exit: ").capitalize()
                    os.system('cls||clear')
                    if userinput not in ["Yes" , "Add", "Exit"]:
                        print ("Please enter Yes or No" )
                    elif userinput == "Yes":
                        play_again = userinput            
                        os.system('cls||clear')
                        break
                    elif userinput == "Add":
                        play_again = ""
                        break
                    elif userinput == "Exit":
                        new_game = False
                        break

               #If the user has selected "Yes" the programme will create temporary list.
               #These lists are used to eliminate possible players as the question get asked. 
                while play_again == "Yes":
                    #resets the guesses  
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
                
                    #This will start to ask randon question while there are still questions within the question list              
                    while True:
                        try:
                            if int(feature_guesses) < 3 and len (question_list) > 1 and len(temporary_players_options) > 2:
                                random.choice(question_list)()
                                os.system('cls||clear')                                    
                            else:
                                if len(temporary_players_options) > 0:
                                    if name_question() == True:
                                        break
                                #if the user has answer incorrectly to one of the questions and is unable to find the
                                #  correct answer                 
                                else:
                                    print("Seems like you slipped my detection")
                                    break
                        #to catch error if there the questions list runs out of question functions
                        except IndexError:
                            print ("I've run out of question....")
                            break
                    # Allows the user to play again or exit back to the start         
                    while True:
                        userinput = input("Do you want to play again?\nYes or Exit: ").capitalize()
                        os.system('cls||clear')
                        if userinput not in ["Yes" , "Exit"]:
                            print ("Please enter Yes or Exit\n")
                        elif userinput == "Yes":
                            play_agin = userinput
                            os.system('cls||clear')
                            break   
                        else:
                            play_again = userinput            
                            new_game = userinput
                            os.system('cls||clear')
                            break
            #This catch the error if the programme is unable to locate the user_data file.
            #   it will notify the user of teh fault and exit the programme           
            except NameError:
                print ("unable to find user_data.py")
                userinput = input("Please ensure file is in the correct location.\n\n Press Enter to exit programme").capitalize()
                os.system('cls||clear')
                run_game = False        
                new_game = False  

    #This will terminate the programme
    elif userinput == "Exit":
        run_game = userinput          
        new_game = userinput
        os.system('cls||clear')
        break

     

