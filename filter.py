#list of people
players= ['Liam', 'Noah', 'Oliver', 'Elijah', 'William', 'James', 'Benjamin', 'Lucas', 'Henry', 'Alexander', 
'Olivia', 'Emma', 'Ava', 'Charlotte', 'Sophia', 'Amelia', 'Isabella', 'Mia', 'Evelyn', 'Harper', 'Charlie', 'Casey', 'Stevie', 
'Remy', 'Finley', 'Monroe', 'Jodie', 'Skyler', 'Jude']

#list of descritions
player_eye_colours = {
    'Liam': 'Green', 'Noah': 'Grey', 'Oliver': 'Blue', 'Elijah': 'Grey', 'William': 'Blue', 'James': 'Blue', 'Benjamin': 'Grey', 
    'Lucas': 'Green', 'Henry': 'Green', 'Alexander': 'Amber', 'Olivia': 'Green', 'Emma': 'Blue', 'Ava': 'Blue', 'Charlotte': 'Grey', 
    'Sophia': 'Grey', 'Amelia': 'Hazel', 'Isabella': 'Grey', 'Mia': 'Blue', 'Evelyn': 'Grey', 'Harper': 'Grey', 'Charlie': 'Amber', 
    'Casey': 'Hazel', 'Stevie': 'Amber', 'Remy': 'Grey', 'Finley': 'Hazel', 'Monroe': 'Brown', 'Jodie': 'Grey', 'Skyler': 'Grey', 
    'Jude': 'Hazel'}

result = [name for (name, value) in player_eye_colours.items() if value != "Brown"]
for i in result:
    if i in players:
        players.remove(i)

print (players)


