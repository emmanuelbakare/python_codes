import re

string = "Everything good comes in another go"
pattern= r"go"






# matches = re.findall(pattern, string) #returns all occurrences of pattern
# print(matches) 

# returns a match if the first charater of the string is the pattern
#


#
# matches = re.finditer(pattern, string) # return iterable with occurrence of match objects  
# for match  in matches:
#     print(match)


# matches = re.search(pattern, string) # returns a match object of the first occurrence of pattern
# print(matches)
# print(type(matches))

# MATCH OBJECT
string = "go get some water for everyone"
mymatch = re.match(pattern, string) 
print(mymatch) # this returns none because the string start with "Everything" , if it starts with "go" e.g. string="go everywhere you want" the ouptut will return a value 

#other method of the match object can be
# print("Match object: ", mymatch ) # returns a match object
# print("match.group: ", mymatch.group())  #return the pattern match
# print("match.start: ", mymatch.start())  # returns the begining index of the match in the string
# print("match.end: ", mymatch.end())   # returns the end index of the match in the string
# print("match.span: ", mymatch.span())  # returns a tuple of the begining and end index of the match









