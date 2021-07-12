import os
from user_data import *

def player_name():
    while True:
        userinput = input("What is your full name?").capitalize()
        os.system('cls||clear')
        if " " not in userinput:
            print ("\nDont forget your last name?")            
        else:
            global name 
            name = userinput
            os.system('cls||clear')
            break

def user_input(category, error_message, feature_list, feature_options ): 
    while True:
        userinput = input(f" {category}:").capitalize()
        os.system('cls||clear')
        if userinput not in feature_options:
            print (error_message)
            print (', '.join(feature_options)+"\n")
        else:            
            feature_list[name] = userinput
            os.system('cls||clear')
            break



#clear terminal window
os.system('cls||clear')

#get user name
player_name()

#user to enter gender 
user_input("Please enter your gender: ", "\nPlease select from the following options: ", player_genders, genders)

#user to put in their eye colour. 
user_input("Please enter your eye colour: ", "\nWhich eye colour is closest to yours: ", player_eye_colours, eye_colours)

#user to put in their hair colour. 
user_input("Please enter the your hair colour: ", "\nWhich hair colour is closest to yours: ",player_hair_colours, hair_colours)

#ask user if they wear glasses.
user_input("Do you wear glasses: ","\nPlease specify", players_glasses, glasses_options)

#ask user if they're bald.
user_input("Are you follicly challenged: ","\nPlease specify", players_bald, bald_options)

#ask user if they're bald.
user_input("Do you have facial hair: ","\nPlease specify", players_facial_hair, facial_hair_options)

print (name)
print (player_genders)
print (player_eye_colours)
print (player_hair_colours)
print (players_glasses)
print (players_bald)
print (players_facial_hair)

