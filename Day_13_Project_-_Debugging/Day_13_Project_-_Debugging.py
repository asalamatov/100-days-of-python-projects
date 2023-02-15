############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# Corrected Version:
def my_function():
  for i in range(1, 20): # 20 is not included
    if i == 19:
      print("You got it")
my_function()



# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# Corrected Version:
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5) # index 6 is not in the list above, it ends with index 5
print(dice_imgs[dice_num])



# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# Corrected Version:
year = int(input("What's your year of birth?"))
if year > 1980 and year <= 1994: # 1994 is not included, so nothing will be printed
  print("You are a millenial.")
elif year > 1994: # 1994 is not included, so nothing will be printed
  print("You are a Gen Z.")



# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# Corrected Version:
age = int(input("How old are you?")) # type conversion error
if age >= 18: #18 is not included
    print("You can drive at age {age}.") #indentation error



# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# Corrected Version:
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: ")) # not ==, but =
total_words = pages * word_per_page
print(total_words)



# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

# Corrected Version:
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item) # indent
  print(b_list)

mutate([1,2,3,5,8,13])