#                          
# NO CODE HERE
#
# QUESTION 1
#  
# NO CODE HERE
#
def password_check(password):           # DO NOT CHANGE THIS LINE 
	result = True                         # DO NOT CHANGE THIS LINE 
	#Bools used later declared
	alpha = False
	num = False
	special = False
	#Check for length:
	if len(password) >= 8:
		for c in password:
			#Check for '?':
			if c == '?':
				result = False
				return result
			#Check for at least one letter:
			elif c.isalpha():
				alpha = True
			#Check for at least one number:
			elif c.isdigit():
				num = True
			#Check for at least one special
			#If not '?', or alpha, or num, must be special:
			else:
				special = True
		#Check that there is at least one of each:
		if alpha & num & special:
			#Check for consecutive characters:
			char = ''
			x = 0
			while x < len(password):
				char = password[x]
				occurence = 1
				y = x + 1
				while y < len(password):
					if password[x] == password[y]:
						occurence = occurence + 1
						y = y + 1
					elif password[x] != password[y]:
						break
				if occurence > 2:
					result = False
					return result
				else:
					x = x + occurence
			#Check that number of unique characters is at least half the length of password:
			unique = []
			for c in password:
				if c not in unique:
					unique.append(c)
			if len(unique) < (len(password)/2.0):
				result = False
		else:
			result = False
	else:
		result = False
	return result                         # DO NOT CHANGE THIS LINE 
# 
# Only use this space to write helper functions (if necessary)
#
if __name__ == "__main__":              # DO NOT CHANGE THIS LINE 
  print(password_check('a12#8'))        # DO NOT CHANGE THIS LINE 
  print(password_check('a1234567#?'))   # DO NOT CHANGE THIS LINE 
  print(password_check('abcdefgh#'))    # DO NOT CHANGE THIS LINE 
  print(password_check('a12345678'))    # DO NOT CHANGE THIS LINE 
  print(password_check('12345678#'))    # DO NOT CHANGE THIS LINE 
  print(password_check('abbbcd1@'))     # DO NOT CHANGE THIS LINE 
  print(password_check('a1@a1@1@'))     # DO NOT CHANGE THIS LINE 
  print(password_check('a123456#7'))    # DO NOT CHANGE THIS LINE 
#                          
# NO CODE HERE
#
# QUESTION 2
#  
# NO CODE HERE
#
def word_counter(file_name):            # DO NOT CHANGE THIS LINE 
	result = 0                            # DO NOT CHANGE THIS LINE 
	
	#Read in file:
	file = open(file_name,'r')
	file_lines = file.readlines()
	file.close()
	
	#Separate read in lines into words:
	words = []
	for i in range (0,len(file_lines)):
		words.append(file_lines[i].split())
	
	#Flatten word list:
	flat_words = []
	for sub in words:
		for i in sub:
			flat_words.append(i)
	
	result  = len(flat_words)

	return result                         # DO NOT CHANGE THIS LINE 
#                          
# NO CODE HERE
#
if __name__ == "__main__":              # DO NOT CHANGE THIS LINE 
  print(word_counter('input1.txt'))     # DO NOT CHANGE THIS LINE 
  print(word_counter('input2.txt'))     # DO NOT CHANGE THIS LINE 
  print(word_counter('input3.txt'))     # DO NOT CHANGE THIS LINE 
  print(word_counter('input4.txt'))     # DO NOT CHANGE THIS LINE 
#                          
# NO CODE HERE
#
def most_frequent(file_name):           # DO NOT CHANGE THIS LINE 
	result1 = ''                          # DO NOT CHANGE THIS LINE 
	result2 = 0                           # DO NOT CHANGE THIS LINE 
	
	#Read in file:
	file = open(file_name,'r')
	file_lines = file.readlines()
	file.close()
	
	#Separate read in lines into words:
	words = []
	for i in range (0,len(file_lines)):
		words.append(file_lines[i].split())
	
	#Flatten word list:
	flat_words = []
	for sub in words:
		for i in sub:
			flat_words.append(i)
	
	#Set all words to lower case:
	flat_words = [c.lower() for c in flat_words]
	
	#Create dictionary:
	mydict = {}
	keys = []
	values = []
	x = 0
	while x < len(flat_words):
		occurence = 1
		y = x + 1
		while y < len(flat_words):
			if flat_words[y] == flat_words[x]:
				occurence = occurence + 1
				del(flat_words[y])
			else:	
				y = y + 1
		keys.append(flat_words[x])
		values.append(occurence)
		x = x + 1
	item = 0
	while item < len(keys):
		mydict.update({keys[item] : values[item]})
		item += 1
	result1 = max(mydict, key=mydict.get)
	result2 = max(mydict.values())
	return result1, result2               # DO NOT CHANGE THIS LINE 
#                          
# NO CODE HERE
#
if __name__ == "__main__":              # DO NOT CHANGE THIS LINE 
  print(most_frequent('input1.txt'))    # DO NOT CHANGE THIS LINE 
  print(most_frequent('input2.txt'))    # DO NOT CHANGE THIS LINE 
  print(most_frequent('input3.txt'))    # DO NOT CHANGE THIS LINE 
  print(most_frequent('input4.txt'))    # DO NOT CHANGE THIS LINE 
#                          
# NO CODE HERE
#