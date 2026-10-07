#string
text ="  Welcome to IMCC!  "

#!.strip spaces from string both ends
print("Remove Spaces", text.strip())

#2.lowercase
print("lower case: ", text.lower())

#uppercase
print("Upper case: ", text.upper())

#4. capitalized first letter
text =text.strip()
print("Capitalized first Letters: ", text.capitalize())

#5.title case capitalized each word
print(text.title())

#6. count occurence of a substring
print("Letter C occurs:", text.count("C"),"times in text")

#find position if not fount it will return -1
#print("Position of imcc text is: " text.find("IMCC"))

#8.replace a substring
print(text.replace("IMCC", "python magic"))

#9.check stert end with certain letters
print(text.startswith(" We"))
print(text.endswith("! "))

#10.split the str
print(text.split())