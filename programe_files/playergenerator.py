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

# for i in male_names+other_names:
#     players_facial_hair[i] = random.choice(facial_hair_options)

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
# print (players_facial_hair)



all_names= ('Liam', 'Noah', 'Liam', 'Noah', 'Oliver', 'Elijah', 'William', 'James', 'Benjamin', 'Lucas', 'Henry', 'Alexander', 'Olivia', 'Emma', 'Ava', 'Charlotte', 'Sophia', 'Amelia', 'Isabella', 'Mia', 'Evelyn', 'Harper', 'Charlie', 'Casey', 'Stevie', 'Remy', 'Finley', 'Monroe', 'Jodie', 'Skyler', 'Jude')


player_genders = {'Liam': 'Male', 'Noah': 'Male', 'Oliver': 'Male', 'Elijah': 'Male', 'William': 'Male', 'James': 'Male', 'Benjamin': 'Male', 'Lucas': 'Male', 'Henry': 'Male', 'Alexander': 'Male', 'Olivia': 'Female', 'Emma': 'Female', 'Ava': 'Female', 'Charlotte': 'Female', 'Sophia': 'Female', 'Amelia': 'Female', 'Isabella': 'Female', 'Mia': 'Female', 'Evelyn': 'Female', 'Harper': 'Female', 'Charlie': 'Other', 'Casey': 'Other', 'Stevie': 'Other', 'Remy': 'Other', 'Finley': 'Other', 'Monroe': 'Other', 'Jodie': 'Other', 'Skyler': 'Other', 'Jude': 'Other'}


player_eye_colours = {'Liam': 'Green', 'Noah': 'Grey', 'Oliver': 'Blue', 'Elijah': 'Grey', 'William': 'Blue', 'James': 'Blue', 'Benjamin': 'Grey', 'Lucas': 'Green', 'Henry': 'Green', 'Alexander': 'Amber', 'Olivia': 'Green', 'Emma': 'Blue', 'Ava': 'Blue', 'Charlotte': 'Grey', 'Sophia': 'Grey', 'Amelia': 'Hazel', 'Isabella': 'Grey', 'Mia': 'Blue', 'Evelyn': 'Grey', 'Harper': 'Grey', 'Charlie': 'Amber', 'Casey': 'Hazel', 'Stevie': 'Amber', 'Remy': 'Grey', 'Finley': 'Hazel', 'Monroe': 'Brown', 'Jodie': 'Grey', 'Skyler': 'Grey', 'Jude': 'Hazel'}


player_hair_colours = {'Liam': 'Grey', 'Noah': 'Grey', 'Oliver': 'Black', 'Elijah': 'Grey', 'William': 'Brown', 'James': 'Blonde', 'Benjamin': 'White', 'Lucas': 'Black', 'Henry': 'Grey', 'Alexander': 'Black', 'Olivia': 'White', 'Emma': 'Grey', 'Ava': 'Blonde', 'Charlotte': 'White', 'Sophia': 'Grey', 'Amelia': 'Black', 'Isabella': 'Red', 'Mia': 'Blonde', 'Evelyn': 'Brown', 'Harper': 'Blonde', 'Charlie': 'Red', 'Casey': 'Black', 'Stevie': 'Red', 'Remy': 'Grey', 'Finley': 'Blonde', 'Monroe': 'White', 'Jodie': 'Blonde', 'Skyler': 'Brown', 'Jude': 'Red'}


player_glasses = {'Liam': 'Yes', 'Noah': 'No', 'Oliver': 'No', 'Elijah': 'Yes', 'William': 'Yes', 'James': 'Yes', 'Benjamin': 'Yes', 'Lucas': 'No', 'Henry': 'Yes', 'Alexander': 'No', 'Olivia': 'No', 'Emma': 'Yes', 'Ava': 'No', 'Charlotte': 'No', 'Sophia': 'Yes', 'Amelia': 'Yes', 'Isabella': 'No', 'Mia': 'No', 'Evelyn': 'Yes', 'Harper': 'No', 'Charlie': 'No', 'Casey': 'No', 'Stevie': 'Yes', 'Remy': 'No', 'Finley': 'No', 'Monroe': 'Yes', 'Jodie': 'Yes', 'Skyler': 'No', 'Jude': 'No'}


players_bald {'Liam': 'Yes', 'Noah': 'No', 'Oliver': 'No', 'Elijah': 'Yes', 'William': 'No', 'James': 'No', 'Benjamin': 'Yes', 'Lucas': 'No', 'Henry': 'No', 'Alexander': 'Yes', 'Olivia': 'Yes', 'Emma': 'Yes', 'Ava': 'Yes', 'Charlotte': 'No', 'Sophia': 'No', 'Amelia': 'Yes', 'Isabella': 'No', 'Mia': 'No', 'Evelyn': 'No', 'Harper': 'No', 'Charlie': 'No', 'Casey': 'No', 'Stevie': 'No', 'Remy': 'No', 'Finley': 'No', 'Monroe': 'Yes', 'Jodie': 'No', 'Skyler': 'Yes', 'Jude': 'No'}


players_facial_hair{'Liam': 'No', 'Noah': 'No', 'Oliver': 'Yes', 'Elijah': 'No', 'William': 'No', 'James': 'No', 'Benjamin': 'Yes', 'Lucas': 'No', 'Henry': 'Yes', 'Alexander': 'Yes', 'Charlie': 'Yes', 'Casey': 'Yes', 'Stevie': 'No', 'Remy': 'No', 'Finley': 'No', 'Monroe': 'Yes', 'Jodie': 'Yes', 'Skyler': 'Yes', 'Jude': 'No'}