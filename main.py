sentence = "I love Pizza"
sentence = sentence.lower()#converting string into upper case
print(sentence)
print(sentence.lower())#converting string into lower case
print(sentence.islower())#checking whether string is in lower or not
print(sentence.isupper())#checking whether sting is in upper case or not
length_of_string = len(sentence)#len(function) calculates the length of the string
print(length_of_string)
print(sentence.replace("love",'hate'))#replacing a part of the string
print(sentence.index("p"))#getting the index number of letter p. index statrs from zero
#to print sentence in next line, use \n command
print("I love pizzas \n nachos and macbooks.")