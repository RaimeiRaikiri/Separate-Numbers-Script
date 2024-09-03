def separate_nums(string):
    # Remove random signs and phrases
    # This set is very specifici to the task 
    string = string.replace('-', '')
    string = string.replace('*', '')
    string = string.replace('ch', '')
    string = string.replace('+', '')
    string = string.replace('.', '')
    string = string.replace('something', '')
    
    
    listOfNames = []
    listOfNums = []
    tempString = ''
    tempNum = ''
    ignoreTillLetter = False
    
    for char in string:
        if char == '/':
            # ignore the following numbers if they are preceded by a / 
            # As it is a total number out of something (eg. 10/100) the 10 is the important number
            ignoreTillLetter = True
        elif char.isnumeric() and ignoreTillLetter == False:
            if tempString != '':
                listOfNames.append(tempString)
                tempString = ''
            tempNum += char
        elif not char.isnumeric():
            if tempNum != '':
                listOfNums.append(tempNum)
                tempNum = ''
            if char != ' ':
                ignoreTillLetter = False
                tempString += char
    
    # Check if final number or string has been added to the list, if not add it
    if tempNum != '' and tempNum != listOfNums[-1]:
        listOfNums.append(tempNum)
    if tempString != '' and tempString != listOfNames[-1]:
        listOfNames.append(tempString)
        
    return listOfNames, listOfNums

# List of books and current progress in terms of chapters
string = 'supreme magus ch 1235 shadow slave ch 1306 *my vampire system 1714sword god in a world of magic - 810 *strongest necromancer of heavens gate - 550tbate - 300 somethingre evolution -1042death and me - 153/2000+isekai journey of the magic archer- 169/550+Global lord onehundredpercent drop rate- 545Blood warlock- 94cultivation online- 655level up legacy- 32cultivation online-1101void system-111reverend insanity- 1413Fey merchant - 899Mother of learning - 65Supreme lord: I can extract everything- 961 *Gods eyes - 870Dark magus returns - 46Infinite mana in the apocalypse - 61Birth of the demonic sword - 49Oracle paths - 1125 *Necromancer of shadows - 30Kill the sun - 254Infinite potential system - 46Lightning is the only way. - 113Energy system - 110An extras pov - 413 *Leveling Endlessly with the Strongest System! - 200Atticus odyssey - 671*Damned Demon - 108Reincarnated with the strongest system - 5A regressors tale of cultivation - 13Chrysalis - 424The first legendary beast master - 409Lotm- 134The academy’s weapon replicator -  16.2The first order - 82Divine hunter - 6Omega summoner - 19New Eden - 873The dark king - 24Magic’s return I can see the spirit - 282Spellcraft - 37Astral pet store - 23The bloodline system - 83Taking the mafia to the magic world - 822Genetic Ascension* - 257Obtaining ten x rewards - 127I can copy and evolve talents - 32'
list1, list2 = separate_nums(string)

# Seperated both lists
for index in range(0, len(list1)):
    print(list1[index] + ': ' + list2[index])

            
    