#Pig Latin Translator
#Susan Puckett
#Go from Pig Latin to regular English words
'''This code takes into account these Pig Latin concepts from Wikipedia:
  1) "For words that begin with consonant sounds, all letters before the initial vowel are placed at the end of the word sequence. 
     Then,"ay"  is added..." 
  2) "For words that begin with vowel sounds, one just adds "way" or "yay" to the end (or just "ay")."
'''

pig_word = input("Enter word in Pig Latin here: ")
 
if len(pig_word)>0 and pig_word.isalpha():
  x=0
else:
  print("Did you enter only letters? No")
  print("Please run again and enter a word in Pig Latin")
  quit()

pig_word = pig_word.lower()

if (pig_word[-2:])!="ay":
  print("But, the word does not end in \"ay\". Please try again.")
  quit()
  
vowels = ['a','e','i','o','u']

if pig_word[0] not in vowels:
  print("But, the first letter is a consonant. Please try again.")
  quit()

#Converting Pig Latin to English

clusters_two = ['bl', 'br', 'ch', 'ck', 'cl', 'cr', 'dr', 'fl', 'fr', 'gh', 'gl', 'gr', 'ng', 'ph', 'pl', 'pr', 'qu', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'th', 'tr', 'tw', 'wh', 'wr']
clusters_three = ['nth', 'sch', 'scr', 'shr', 'spl', 'spr', 'squ', 'str', 'thr']
  

if pig_word[-3:] == 'way':
  print("The English word is one of the following:")
  minus_way = pig_word[:-3]
  w_minus_way = 'w'+ pig_word[:-3]
  print(minus_way + " or " + w_minus_way )
  quit()

if pig_word[-3:] == 'yay':
  print("The English word is one of the following:")
  minus_yay = pig_word[:-3]
  y_minus_yay = 'y'+ pig_word[:-3]
  print(minus_yay + " or " + y_minus_yay )
  quit()
  
minus_ay = pig_word[:-2]
if minus_ay[-2:] in clusters_two and minus_ay[-3:] in clusters_three:
  print("The English word is either:  " + minus_ay[-2:] + minus_ay[:-2] + " or " + minus_ay[-3:] + minus_ay[:-3])
elif minus_ay[-2:] in clusters_two:
  print("The English word is:  " + minus_ay[-2:] + minus_ay[:-2])
elif minus_ay[-3:] in clusters_three:
  print("The English word is:  " + minus_ay[-3:] + minus_ay[:-3])
else:
  print("The English word is: " + minus_ay + " or " + minus_ay[-1] + minus_ay[:-1])
