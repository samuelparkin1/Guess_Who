import os

name = "Sam"
eyes = {'john':"green", 'sam': "green", 'tom': "blue", 'jim': "brown"}
eye_colours = ("Amber","Blue","Brown", "Gray", "Green", "Hazel")
hair = {}
hair_colours =("Black", "Brown", "Blonde", "White", "Grey", "Red", "Pink", "Purple", "Blue", "Green", "Yellow")
glasses ={}
glasses_options = ("Yes", "No") 

def colour_input(category, feature_list, feature_colour ): 
    while True:
        userinput = input(f"please enter the colour of your {category}:").capitalize()
        os.system('cls||clear')
        if userinput not in feature_colour:
            print ("\nWhich of these colours is the closest?")
            print (', '.join(feature_colour)+"\n")
        else:
            feature_list[name] = userinput
            os.system('cls||clear')
            break

def yes_no_input(question, feature_list, feature_colour ): 
    while True:
        userinput = input(question).capitalize()
        os.system('cls||clear')
        if userinput not in feature_colour:
            print ("\nPlease specify Yes or No")
            #print (', '.join(feature_colour)+"\n")
        else:
            feature_list[name] = userinput
            os.system('cls||clear')
            break

#clear terminal window
os.system('cls||clear')

#user to put in their eye colour. 
colour_input("eyes", eyes, eye_colours)

#user to put in their hair colour. 
colour_input("hair colour", hair, hair_colours)

#ask user if they wear glasses.
yes_no_input("do you were glasses: ", glasses, glasses_options)

print (eyes)
print (hair)
print (glasses)
