#list of people
who=[['Alex'],['Alfred'],['Anita'],['Anne'],['Bernard'],['Bill'],['Charley'],['Claire'],
['David'],['Eric'],['Frans'],['Goeroge'], ['Herman'],['Joe'], ['Maria'],['Max'], ['Paul'],
 ['Peter'], ['Philip'], ['Richard'], ['Robert'], ['Sam'], ['Susan'], ['Tom']]



#list of descritions
eyes = {'john':"green", 'sam': "green", 'tom': "blue", 'jim': "brown"}
hair = {'john':"brown", 'sam': "black", 'tom': "blond", 'jim': "red"}

# random descriptions
x = "brown"
random_word = "hair"

#guesswho_tester

def test_yes(t,y):
    result = [name for (name, value) in t.items() if value == y]
    return (result)

def test_no(t,y):
    result = [name for (name, value) in t.items() if value == y]
    for i in result:
        result=i
    return str (result)


#who.remove (test_yes(eyes,"brown"))
#who.remove (test_yes(hair,"blond"))
print (test_yes(eyes,"green"))
print (who)
