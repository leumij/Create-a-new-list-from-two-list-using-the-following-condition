# Create a new list from two list using the following condition
# Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

# Pseudocode

# Create a function
def even_odd_list(list1,list2):
  new_list = []
  for num in list1:
    if num%2!=0:
      new_list.append(num)
  for num in list2:
    if num%2 == 0:
      new_list.append(num)
  return new_list

# Given 
list1 =  [10, 20, 23, 11, 17]
list2 = [13, 43, 24, 36, 12]

# Print the new list
print('new_list is ', even_odd_list(list1,list2))