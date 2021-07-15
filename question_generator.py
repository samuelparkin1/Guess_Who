import random
import os
from user_data import *
from functions import *

run_game = "Yes"
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

        while run_game == "Yes" and new_game == "Yes":
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
                    new_game = ""
                    break

            while play_again == "Yes":
                     
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
              
                while True:
                    try:
                        if int(feature_guesses) < 3 and len (question_list) > 1 and len(temporary_players_options) > 2:
                            random.choice(question_list)()
                            os.system('cls||clear')
                                
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
    else:
        run_game = userinput          
        new_game = userinput
        os.system('cls||clear')
        break

     

