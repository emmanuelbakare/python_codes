""" 
Special character you can use includes
.,^,*,$, +, ?, {m,n}, |, (),[]
"""
import re
#  . CHARACTER (dot)
# this mean match every character in the string except a new line \n
# . will match 1 xter '..' will match 2 xter

string = "go and do good to all the gods"
# regex = r'.' # match each charater e.g 'g'
# regex = r'..' # match 2 xters each  e.g 'go'
# regex = r'g..' # match 3 xters starting with g  return ['go ', 'goo', 'god']

# matches = re.findall(regex,string)
# print(matches)  



# ^ CHARACTER  (caret)
#matches the first character in the string
# string = "go and do good to all the gods"
# regex = r"^go"
# matches = re.findall(regex,string)
# print(matches)

# $ CHARACTER (dollar)
