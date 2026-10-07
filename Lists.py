# my_list = []
# print(my_list)

# fruits = ["apple", "banana", "pineapple"]
# print(fruits)

#append it will add element at end of the list
# colors=["red","pink"] 
# colors.append("yellow")
# print("After appending an element:", colors.append())

#functions
# num=[1,2,3,4,5]
# # print("No.of list:", len(num))

# print("sum list:", sum(num))#sum

# #sorted
# print("List in Ascending order", sorted(num))
# print("List in Ascending order", sorted(num, reverse =True))

#create a list of 10 num and display the sum of last four element
#remove the items from the list located at 2nd and 5th position
#print the diff b/w highest & smallest element
#append a new element in a list which is half of the item of 3rd position 


#create a list of 10 num and display the sum of last four element

# num = [1,2,3,4,5,6,7,8,9,10]
# print(sum(num[-4:]))

#remove the items from the list located at 2nd and 5th position

# num = [1,2,3,4,5,6,7,8,9,10]
# print(num.pop(1))
# num = [1,2,3,4,5,6,7,8,9,10]
# print(num.pop(4))

#append a new element in a list which is half of the item of 3rd position 
# num = [1,2,66,4,5,6,7,8,9,10]
# num.append(33)
# print(num)

#print the diff b/w highest & smallest element
# num =[1,2,3,4,5]
# print(min(num))
# print(max(num))

#print sum of 10 even numbers
# num = int(input("enter a number: "))
# sum=0
# for i in range(num):
#     if(num%2==0):
#         sum+=i
# print(i)

#accept two values S ans N. print square of first N numbers starting from s



#reverse the accepted string

# user_string = input("Enter a string: ")
# reversed_string = user_string[::-1]

# print("Reversed string:", reversed_string)
# #accept sentence from user and count the vowels
# sentence = input("Enter a sentence: ").lower()

# Count each vowel and add them up
# total_vowels = (sentence.count('a') + 
#                 sentence.count('e') + 
#                 sentence.count('i') + 
#                 sentence.count('o') + 
#                 sentence.count('u'))

# print("Number of vowels:", total_vowels)

#remove duplicates from list
my_list = [1, 2, 2, 3, 4, 4, 5]

# Convert to set to remove duplicates, then back to a list
clean_list = list(set(my_list))

print("Without duplicates:", clean_list)
#reverse the list
my_list = [10, 20, 30, 40]
reversed_list = my_list[::-1]

print("Reversed list:", reversed_list)





