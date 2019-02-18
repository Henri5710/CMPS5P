#                          
# NO CODE HERE
#
# QUESTION 1
#  
# NO CODE HERE
#
def password_check(password):           # DO NOT CHANGE THIS LINE 
	result = True                         # DO NOT CHANGE THIS LINE 
	# Must be at least 8 characters
	alpha = False
	num = False
	special = False
	if len(password) >= 8:
		#print("1:",result)
		for c in password:
			if c == '?':
				result = False
				#print("2:",result)
				return result
			elif c.isalpha():
				alpha = True
			elif c.isdigit():
				num = True
			else:
				special = True
		#print("3:",result)
		#print("check:",alpha,num,special)
		if alpha & num & special:
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
					#print("4:",result)
					return result
				else:
					x = x + occurence
			#print("5:",result)
			unique = []
			for c in password:
				if c not in unique:
					unique.append(c)
			#print('number of unique characters is:', len(unique))
			#print('length of password is:', len(password))
			if len(unique) < (len(password)/2.0):
				result = False
				#print("6:",result)
		else:
			result = False
			#print("7:",result)
	else:
		result = False
		#print("8:",result)
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
	file = open(file_name,'r')
	file_lines = file.readlines()
	file.close()
	words = []
	for i in range (0,len(file_lines)):
		words.append(file_lines[i].split())
	flat_words = []
	for sub in words:
		for i in sub:
			flat_words.append(i)
	print(flat_words)
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
	file = open(file_name,'r')
	file_lines = file.readlines()
	file.close()
	words = []
	for i in range (0,len(file_lines)):
		words.append(file_lines[i].split())
	flat_words = []
	for sub in words:
		for i in sub:
			flat_words.append(i)
	flat_words = [c.lower() for c in flat_words]
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
'''
#OLD VERSION OF PASSWORD CHECK(INCLUDE ALPHA,NUM,SPECIAL BOOLS TO USE)
	if len(password) < 8:
		length = False
	else:
		length = True
	# Must not contain "?"
	for c in password:
		if c == '?':
			question = False
			break
		else:
			question = True
	# Must have at least one alphabetic, one numberical and one special character
	
	for c in password:
		if c.isalpha():
			alpha = True
		elif c.isdigit():
			num = True
		else:
			special = True
	if alpha and num and special:
		one_of_each = True
	else:
		one_of_each = False
	# Must not contain the same character more than 2 times consecutively
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
			no_repeat = False
			break
		else:
			no_repeat = True
			x = x + occurence 
	# The number of distinct characters must not be less than half of the passwords length
	unique = []
	for c in password:
		if c not in unique:
			unique.append(c)
	print('number of unique characters is:', len(unique))
	print('length of password is:', len(password))
	if len(unique) < (len(password)/2.0):
		distinct = False
	else:
		distinct = True

	if length and question and one_of_each and no_repeat and distinct:
		result = True
	else:
		result = False
	
	print('Is the password at least 8 characters:', length)
	print('Does it not contain a question mark:', question)
	print('Does it contain at least one letter:', alpha)
	print('Does it contain at least one number:', num)
	print('Does it contain at least one special character:', special)
	print('Does it contain at least one letter/number/special:', one_of_each)
	print('Is a character never repeated more than twice consecutively:', no_repeat)
	print('Is the number of distinct characters at least half of the password length:', distinct)
	'''