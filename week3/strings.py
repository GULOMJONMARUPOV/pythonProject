# # 03/04/2021
#
fullname = 'dardi saro'
msg = 'Funksiyahoi stingro dar bidon dida bromadestem'
print(fullname)
print(fullname.upper())
print(fullname.lower())
print(fullname.title())
print(msg.replace('.', '!!!!!').title())
print(msg.replace('bidon', 'jave'))
#
# # concatenations
msg1 = fullname+ msg
print(msg1)
msg1 = fullname.title() + ',' + msg
print(msg1)
print(fullname.upper() + ','+ msg)
#
# # working  with whitespacing  in string: \t, \n ,etc
msg2 = fullname.upper() + "\nt\t\t," + msg
print(msg2)
#
msg3 = '\n\t\t\t' + fullname.upper() + "," + msg
# str.strip () removes leading and preceding white space
print(msg3.strip())
print(msg3.strip() + '!!!')
print(msg3 + '!!!')
print(fullname.title() + '\t,'+ msg)
#
# # fstring
# msg3 =  '\n\t\t\t' + fullname.upper()
# msg4= f"\n\t\t\t' {fullname.upper()},{msg}"
# print("fstring")
# last_name = f"tesha"
# print(msg4 + '!!!')
#
print("intigers: ********")
num = 5
num2 = 8
print(num)
message = "One of the Pyton's strenght is its diverse community"
print(message)
print(f"num + num2 = {num + num2}")
print(f"num - num2 = {num - num2}")
print(f"num * num2 = {num * num2}")
print(f"num / num2 = {num / num2}")
# str (expression) - this will convert the data type to str
print("value of num is : " + str(num))
print("num + num2 = " + str(num + num2))
#
num3 = "666" # it is a string(str) not an intiger(int)
# print(f"num + num3 = {num + num3}")
print(f"num + num3 = {num + int(num3)}")
# # ctrl + clk - will take you whre the specific variable is defined
#
print(f"3**2 = {3**2}") # 3**2
#
