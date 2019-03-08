#!/usr/bin/env python
# coding: utf-8

# In[30]:


#Programmer: Henri Geneste
#Student ID#: 1675311
#Date: 1/25/2019
#Compiler Used: Jupyter Notebooks (Hyperion.ucsc.edu)
#Purpose: Calculate average GPA of a student with user inputted data

#Initial Conditions
done = str('nope')
totalCredits = 0.0
totalGrade = 0.0

#Main loop for input
while done != 'DONE':

    #Ask user for letter grade:
    userGrade = input('Enter grade (A, B, C, D, or F): ')
    
    #User input validation:
    while userGrade not in ['A','B','C','D','F']:
        print('Invalid grade! Try again!\n')
        userGrade = input('Enter grade (A, B, C, D, or F): ')
    
    #Ask user for credit value:
    userCredit = input('Enter credit count (2, 3, or 5): ')
    
    #User input validation:
    while userCredit not in ['2','3','5']:
        print('Invalid credit count! Try again!\n')
        userCredit = input('Enter credit count (2, 3, or 5): ')
    
    userCredit = float(userCredit)
    
    #Computation of total grade points earned:
    if userGrade is 'A':
        totalGrade += 4.0*userCredit
    elif userGrade is 'B':
        totalGrade += 3.0*userCredit
    elif userGrade is 'C':
        totalGrade += 2.0*userCredit
    elif userGrade is 'D':
        totalGrade += 1.0*userCredit
        
    totalCredits += userCredit
    done = str(input('If you are done, enter DONE; otherwise, just press enter: '))
    if done != 'DONE':
        print("\n")
    
#Computation of average gpa:
gpa = totalGrade / totalCredits
#Output average gpa:
print('\nAverage GPA is: %.2f'%(gpa))


# In[ ]:




