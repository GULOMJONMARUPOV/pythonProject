# #03/11/2021
cars = ['mercedes','tesla','toyota','reno']
#Making Numerical List
# for num in range(4):
#     print(num)
# for num in range(4):
#     print(f"number:{num}")
# # shift + f6 -shortcut for Refactor(rename)
# # ctrl + Y - deletes line
nums =  range(5) #this does not means nums =[0, 1, 2, 3]
print(nums)
nums2 = list(range(5))# this creates list daata structure from sequence of number
print(nums2)
for num in nums2:
    print(num)
print("range with start and stop ---")
for num in range(1, 3):
    print(num)
print("range with start and stop ---")
# for num in range(1,10,2):
#     print(num)
# print("Exercise 1: print all even number from 1 to 10 (10 should be included)")
# for num in range(0, 14 , 2):
#     print(num)
# print("print all even number from 1 to 12(12 should be included)")
# evens = []
# for num in range(0, 14, 2):
#     print(num)
#     evens.append(num)
#     print(evens)
# print(evens)
# print(f"thi is final list:{evens}")
# print("Exercise2: print the square of numbers from 10 to 20")
# #for num in range(10,21):
#     #print(num**2)
#     #print(num*num)
# squares =list()
# #for num in range(10,21):
#  #   squares.append(num**2)
# #print(squares)
# for num in range(10,21):
#     squares.append(num**2)
# print(f"final list:{(squares)}")
# print(f"min(squares):{min(squares)}")
# print(f"max(squares):{max(squares)}")
# print(f"sum(squares):{sum(squares)}")
#
# cars = ['mercedes','tesla','toyota','reno']
# cars_len =len(cars)
# for car in cars:
#     print(car)
#     print(f"index of the {car} is {cars.index(car)}")
# print("looping the list using index******")
# for ind in range(4):
#     print(ind)
#     print(f"index of the {cars[ind]} is {ind}")
# for ind in range(len(cars)):
#     print(ind)
#     print(f"index of the {cars[ind]} is {ind}")
#
# #-----------------------------------
# print("list comprehension:")
# squares1 = list()
# for num in range(10,21):
#     squares1.append(num**2)
# print(squares1)
# squares =[num**2 for num in range(10,21)]# for read only now, use later
# print(squares)
# ### exercise 4-5 from book page 64
# nums =[]
# #for num in range(1,100000):
#  #   print()
#   #  nums.append(num)
# #print(nums)
# for num in range(1,101):
#     print(num)
#     nums.append(num)
# print(nums)
# print(f"smallest:{min(nums)}")
# print(f"biggest:{max(nums)}")
# print(f"total:{sum(nums)}")
#
#
