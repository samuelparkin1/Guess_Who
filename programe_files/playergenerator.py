import random


male_names =["Liam", "Noah", "Liam", "Noah",'Oliver','Elijah','William','James','Benjamin','Lucas','Henry','Alexander']
female_names =["Olivia", "Emma", "Ava","Charlotte","Sophia",'Amelia','Isabella','Mia','Evelyn','Harper',]
other_names = ['Charlie','Casey','Stevie','Remy','Finley','Monroe','Jodie','Skyler','Jude',]

name = []

player_genders= {}
genders=("Male", "Female", "Other")

player_eye_colours = {}
eye_colours = ("Amber","Blue","Brown", "Grey", "Green", "Hazel")

player_hair_colours = {}
hair_colours =("Black", "Brown", "Blonde", "White", "Grey", "Red",)

players_glasses ={}
glasses_options = ("Yes", "No")

players_bald ={}
bald_options=("Yes","No")

players_facial_hair ={}
facial_hair_options=("Yes","No")

player_genders = {}
all_names = (male_names+female_names+other_names)

######################  UNCOMMENT SECTION BELOW TO CREATE NEW LISTS ###################################     

# for i in male_names: 
#     player_genders[i] = "Male"

# for i in female_names:
#     player_genders[i] = ("Female")

# for i in other_names:
#     player_genders[i] = ("Other")

# for i in all_names:
#     player_eye_colours[i] = random.choice(eye_colours)

# for i in all_names:
#     player_hair_colours[i] = random.choice(hair_colours)

# for i in all_names:
#     players_glasses[i] = random.choice(glasses_options)

for i in male_names+other_names:
    players_facial_hair[i] = random.choice(facial_hair_options)

for i in female_names:
    players_facial_hair[i] = "No"

# for i in all_names:
#     players_bald[i] = random.choice(bald_options)

# print ("\n")
# print (all_names)
# print ("\n")
# print (player_genders)
# print ("\n")
# print (player_eye_colours)
# print ("\n")
# print (player_hair_colours)
# print ("\n")
# print (players_glasses)
# print ("\n")
# print (players_bald)
# print ("\n")
print (players_facial_hair)
