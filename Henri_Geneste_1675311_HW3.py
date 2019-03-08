#!/usr/bin/env python
# coding: utf-8

# In[66]:


#Programmer: Henri Geneste
#Student ID#: 1675311
#Date: 2/01/2019
#Compiler Used: Jupyter Notebooks (Hyperion.ucsc.edu)
#Purpose: Compare 3 applicants and determine the best one

def getInputs():
    
    #Ranking Input:
    ranking = input('Enter Undergraduate university ranking (low-ranked, medium-ranked, high-ranked): ')
    while ranking not in ['low-ranked','medium-ranked','high-ranked']:
        print('Invalid ranking! Try again!\n')
        ranking = input('Enter Undergraduate university ranking (low-ranked, medium-ranked, high-ranked): ')
    
    #GPA Input:
    gpa_ok = False
    while not gpa_ok:
        gpa = input('Enter undergraduate GPA (0.0 - 4.0): ')
        try:
            check = float(gpa)
            if 0.0 <= check <= 4.0:
                gpa_ok = True
            else:
                print('Invalid GPA! Try again!\n')
        except:
            print('Invalid GPA! Try again!\n')  
    gpa = float(gpa)
    
    #TOEFL Input:
    toefl_ok = False
    while not toefl_ok:
        toefl = input('Enter TOEFL score (0 - 120): ')
        try:
            check = int(toefl)
            if 0 <= check <= 120:
                toefl_ok = True
            else:
                print('Invalid TOEFL score! Try again!\n')
        except:
            print('Invalid TOEFL score! Try again!\n') 
    toefl = int(toefl)
    
    #GRE Input:
    gre_ok = False
    while not gre_ok:
        gre = input('Enter GRE score (260 - 340): ')
        try:
            check = int(gre)
            if 260 <= check <= 340:
                gre_ok = True
            else:
                print('Invalid GRE score! Try again!\n')
        except:
            print('Invalid GRE score! Try again!\n') 
    gre = int(gre)
    
    #Number of Publications Input:
    pub_ok = False
    while not pub_ok:
        pub = input('Enter the number of publications: ')
        try:
            check = int(pub)
            if 0 <= check:
                pub_ok = True
            else:
                print('Invalid number of publications! Try again!\n')
        except:
            print('Invalid number of publications! Try again!\n')
    pub = int(pub)
    
    return (ranking, gpa, toefl, gre, pub)

def computeNormGPA(ranking, gpa):
        #Conversion to numeric equivalent:
        if ranking == 'low-ranked':
            rankWeight = 0.9
        elif ranking == 'medium-ranked':
            rankWeight = 1.0
        elif ranking == 'high-ranked':
            rankWeight = 1.1
        
        #Computation:
        normGPA = (rankWeight * gpa) / 4.0
        if normGPA > 1.0:
            normGPA = 1.0
        return normGPA
    
def computeNormTestScore(toefl, gre):
    #Computation:
    normTestScore = (0.6*(float(toefl)/120.0)) + (0.4 *(float(gre)/340.0))
    return normTestScore

def computeNormPubScore(pub):
    #Conversions:
    if pub == 0:
        normPubScore = 0
    elif pub == 1:
        normPubScore = 0.5
    elif pub >= 2:
        normPubScore = 1.0
    return normPubScore

def computeNormTotalScore(ranking, gpa, toefl, gre, pub):
    #Computation:
    normTotScore = 0.5*computeNormGPA(ranking, gpa) + 0.3 * computeNormTestScore(toefl, gre) + 0.2 * computeNormPubScore(pub)
    return normTotScore

def findBestCandidate():
    #Declaration of lists to be used:
    candidates = []
    normScore = []
    number = ['first','second','third']
    #Prompt user for data:
    for i in range(0,3):
        print('\nGetting the academic achievements of the %s applicant ...'%(number[i]))
        candidates.append(getInputs())
        normScore.append(computeNormTotalScore(candidates[i][0],candidates[i][1],candidates[i][2],candidates[i][3],candidates[i][4]))
        if i == 2:
            print('\n')
            #Print normalized total scores of each applicant:
            for y in range(0,3):
                print('Normalized total score of the %s applicant is: %.4f'%(number[y],normScore[y]))
            
            #Determine and print best applicant:
            print('\nThe %s applicant is the best candidate.'%(number[normScore.index(max(normScore))]))

#Call main function:        
findBestCandidate()


# In[ ]:




