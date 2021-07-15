import random


male_names =['Oliver', 'Liam', 'Ethan', 'Aiden', 'Gabriel', 'Caleb', 'Theodore', 'Declan', 'Owen', 'Elijah', 'Henry', 
'Jackson', 'Grayson', 'Levi', 'Benjamin', 'Finn', 'Miles', 'Alexander', 'Sebastian', 'Leo', 'Landon', 'Emmett', 'Everett',
 'Milo', 'Jasper', 'Archer', 'Lucas', 'Noah', 'Harrison', 'Hudson', 'Felix', 'Jacob', 'Atticus', 'Lincoln', 'Gavin',
  'Dominic', 'Jack', 'Atlas', 'Isaac', 'Logan', 'Wyatt', 'Silas', 'Cole', 'Theo', 'Holden', 'Luke', 'William', 'Isaiah', 
  'Adrian', 'Elias', 'Samuel', 'Arthur', 'Gideon', 'Kaden', 'Arlo', 'James', 'Adam', 'Colton', 'Ronan', 'Roman', 'Asher',
   'Nolan', 'Jonah', 'Rhys', 'Nathan', 'Axel', 'August', 'Connor', 'Xavier', 'Charles', 'Eli', 'Daniel', 'Nathaniel', 
   'Ezra', 'Beau', 'Zachary', 'Tobias', 'Carter', 'Matthew', 'Ian', 'Ezekiel', 'Aaron', 'Thomas', 'Xander', 'Soren', 
   'Oscar', 'Callum', 'Nicholas', 'Ace', 'Josiah', 'Michael', 'Vincent', 'Edward', 'Lachlan', 'Chase', 'Apollo', 'David', 
   'Jace', 'Malachi']

female_names =['Charlotte', 'Ava', 'Amelia', 'Olivia', 'Aurora', 'Violet', 'Luna', 'Hazel', 'Chloe', 'Aria', 'Scarlett',
 'Isla', 'Abigail', 'Freya', 'Adeline', 'Sophia', 'Nora', 'Adelaide', 'Emma', 'Mila', 'Lily/Lilly', 'Grace', 'Maeve', 
 'Ivy', 'Ella', 'Eleanor', 'Audrey', 'Genevieve', 'Iris', 'Isabella', 'Lucy', 'Ophelia', 'Eloise', 'Vivienne', 'Lorelei',
  'Wren', 'Hannah', 'Clara', 'Lydia', 'Madeline', 'Claire', 'Astrid', 'Thea', 'Kaia', 'Cora', 'Penelope', 'Naomi', 'Zoey',
  'Aaliyah', 'Elizabeth', 'Evangeline', 'Autumn', 'Esme', 'Mia', 'Daisy', 'Ruby', 'Margot', 'Layla', 'Anastasia', 'Sadie',
   'Stella', 'Lila', 'Rosalie', 'Daphne', 'Fiona', 'Phoebe', 'Savannah', 'Alice', 'Eliana', 'Eliza', 'Gemma', 'Arabella', 
   'Athena', 'Maya', 'Saoirse', 'Zoe', 'Sienna', 'Evelyn', 'Rose', 'Harper', 'Josephine', 'Felicity', 'Delilah', 'Amaya',
    'Caroline', 'Olive', 'Adalyn', 'Brielle', 'Matilda', 'Aurelia', 'Willow', 'Natalie', 'Leilani', 'Ada', 'Elena', 
    'Mabel', 'Emily', 'Isabelle', 'Nadia', 'Amara']

other_names = ['Bowie', 'Avery', 'Riley', 'Jules', 'Parker', 'Denali', 'Navy', 'Jordan', 'Sawyer', 'Rowan', 'Zenith', 
'Charlie', 'Quinn', 'Peyton', 'Hayden', 'Blake', 'Emerson', 'Elliott', 'Windsor', 'Linden', 'Amari',]

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

all_names = (male_names+female_names+other_names)

#####################  UNCOMMENT SECTION BELOW TO CREATE NEW LISTS ###################################     

for i in male_names: 
    player_genders[i] = "Male"

for i in female_names:
    player_genders[i] = ("Female")

for i in other_names:
    player_genders[i] = ("Other")

for i in all_names:
    player_eye_colours[i] = random.choice(eye_colours)

for i in all_names:
    player_hair_colours[i] = random.choice(hair_colours)

for i in all_names:
    players_glasses[i] = random.choice(glasses_options)

for i in male_names+other_names:
    players_facial_hair[i] = random.choice(facial_hair_options)

for i in female_names:
    players_facial_hair[i] = "No"

for i in all_names:
    players_bald[i] = random.choice(bald_options)

print (f"Player = {male_names+female_names+other_names}")
print ("\n")
print (f"player_genders= {player_genders}")
print ("genders = ('Male', 'Female', 'Other')")
print ("\n")
print (f"player_eye_colours = {player_eye_colours}")
print ("eye_colours = ('Amber','Blue','Brown', 'Grey', 'Green', 'Hazel')")
print ("\n")
print (f"player_hair_colours = {player_hair_colours}")
print (f"hair_colours =('Black', 'Brown', 'Blonde', 'White', 'Grey', 'Red')")
print ("\n")
print (f"players_glasses ={players_glasses}")
print ("glasses_options = ('Yes', 'No')")
print ("\n")
print (f"players_bald ={players_bald}")
print ("bald_options=('Yes','No')")
print ("\n")
print (f"players_facial_hair ={players_facial_hair}")
print ("facial_hair_options = ('Yes','No')")

