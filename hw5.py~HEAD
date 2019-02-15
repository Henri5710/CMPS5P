#                          
# NO CODE HERE
#
# QUESTION 1
#  
# NO CODE HERE
#
'''
def password_check(password):           # DO NOT CHANGE THIS LINE 
	result = True                         # DO NOT CHANGE THIS LINE 
	# Must be at least 8 characters
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
	alpha = False
	num = False
	special = False
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
'''
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
	print(file_lines)
	print(len(file_lines))
	for i in range (0,len(file_lines)):
		words = file_lines[i].split(' ' or '\n')
	print(file_lines[0].split)
	'''
	while i < len(file_lines):
		words = file_lines[i].split()
		i = i+1
		'''
	count = len(words)
	print(words)
	result  = count

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
    #
    # Your code here
    #
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