import random
from user_data import player_genders, player_eye_colours, player_hair_colours
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


temporary_eye_colour =[]
temporary_hair_colour=[]
temporary_gender=[]


def tempory_list(data, temp_list):
    for i in data.values():
        if i not in temp_list:
            temp_list.append(i)


# Gererate a list of passible eye colours.  
tempory_list(player_eye_colours,temporary_eye_colour)
# Gererate a list of passible eye colours.  
tempory_list(player_eye_colours,temporary_eye_colour)

def eye_question():
        random_eye_colour = random.choice(temporary_eye_colour) 

questions = ['Is the colour of your eyes ' + random.choice(temporary_eye_colour) + '?', 'Question 2', 'Question 3'] #You can add as many questions as you like
random.shuffle(questions)  #Mixes the items in "questions" into a random order
print (questions[0])
print (questions[1])
print (questions[2])

print (temporary_eye_colour)
