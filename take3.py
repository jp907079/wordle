# import the data sets
import csv
import pandas as pd
import random
  

with open('C:/Users/yixin/Downloads/archive (2)/valid_solutions.csv', 'r') as guesses:
    csv_reader = csv.reader(guesses)
    list_of_Guesses = list(csv_reader)

with open('C:/Users/yixin/Downloads/archive (2)/valid_solutions.csv', 'r') as solutions:
    csv_reader = csv.reader(solutions)
    list_of_Solutions = list(csv_reader)

print(len(list_of_Guesses), 'possible guesses.')
keyWord = random.choice(list_of_Solutions)
keyWord = "".join(keyWord)
print("Let's try to guess:", keyWord,'\n\n')

#Grey
absent_Letters = []
#Yellow
present_Letters = []
#Green
correct_Letters = []
myAnswer = ['0','0','0','0','0']
res = ''


def guess(word):
    list_of_Guesses.remove(word)

    word = "".join(word)
    print('\n\nYou guessed',word)

    if(word==keyWord):
        print('You guessed correctly!')
        res = keyWord
    else:        
        for i in range(len(word)):
            if(word[i] == keyWord[i]):
                if(myAnswer[i]==word[i]):
                    continue
                else:
                    myAnswer[i] = word[i]
                    correct_Letters.insert(i, word[i])
            elif(word[i] in keyWord):
                #Yellow
                if(word[i] in present_Letters):
                    continue
                elif(word[i] in correct_Letters):
                    continue
                else:
                    present_Letters.append(word[i])
            else:
                #Grey
                if(word[i] in absent_Letters):
                    continue
                else:
                    absent_Letters.append(word[i])
                

def cleanList():
    #Remove all words that contain grey letters
    for i in range (len(absent_Letters)):
        try:
            #print("I am checking",absent_Letters[i])
            for j in range(len(list_of_Guesses)):
                if("".join(absent_Letters[i]) in "".join(list_of_Guesses[j])):
                    #print('I removed', ''.join(list_of_Guesses[j]), "because it contains", absent_Letters[i])
                    list_of_Guesses.remove(list_of_Guesses[j])
            #print(len(list_of_Guesses), 'remaining guesses')
        except:
            continue
    #print(len(list_of_Guesses),'remaining\n\n')
    
    #Remove all words that do not contain yellow letters
    for i in range (len(present_Letters)):
        try: 
            #print("I am checking", present_Letters[i])
            for j in range(len(list_of_Guesses)):
                if("".join(present_Letters[i]) in "".join(list_of_Guesses[j])):
                    continue
                else:
                    #print('i removed',list_of_Guesses[j],'because it does not have a',present_Letters[i])
                    list_of_Guesses.remove(list_of_Guesses[j])
            #print(len(list_of_Guesses), 'remaining guesses')
        except:
            continue
        
    #remove all words that do not contain green letters
    for i in range(len(correct_Letters)):
        try: 
            #print("I am checking", correct_Letters[i])
            for j in range(len(list_of_Guesses)):
                if("".join(correct_Letters[i]) in "".join(list_of_Guesses[j])):
                    continue
                else:
                    #print('i removed',list_of_Guesses[j],'because it does not have a',correct_Letters[i])
                    list_of_Guesses.remove(list_of_Guesses[j])
            #print(len(list_of_Guesses), 'remaining guesses')
        except:
            continue
        
    print(len(list_of_Guesses), 'remaining \n\n')
    



def displayStats():
    print(*myAnswer)
    print('Grey:', *absent_Letters)
    print('Yellow:', *present_Letters)
    print('Green:', *correct_Letters)
    print('Remaining Possible Words', len(list_of_Guesses),'\n\n')


count=0

while(res != keyWord):
    guess(random.choice(list_of_Guesses))
    displayStats()
    print('Cleaning...')
    cleanList()
    count= count+1
    
    if(len(list_of_Guesses)<10):
        print(*list_of_Guesses)
    
    if(len(list_of_Guesses)==1):
        #res = keyWord
        print('Tries:',count)
        break
    res = "".join(myAnswer)
    #if(count==5):
    #    res = keyWord
    #    print("\n\nYou ran out of tries!\n\n")
    
#displayStats()
print('Answer:',res)
#while(res!=keyWord):
#    guess(random.choice(list_of_Guesses))
#    displayStats()
#    print('Cleaning...')
#    cleanList()
#    res = myAnswer
#    count=count+1
#    if(count==5):
#        res=keyWord
    

