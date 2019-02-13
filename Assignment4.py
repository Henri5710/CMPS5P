#!/usr/bin/env python
# coding: utf-8

# In[56]:


#                          
# NO CODE HERE
#
# QUESTION 1
#                          
# NO CODE HERE
#
import math                     # DO NOT CHANGE THIS LINE 
#                          
# NO CODE HERE
#
def step_count(ins_str):        # DO NOT CHANGE THIS LINE 
    result = 0                    # DO NOT CHANGE THIS LINE 
    for c in ins_str:
        if c not in ['r','R','l','L','u','U','d','D']:
            result = -1
            break
        else:
            result = result + 1
    return result                 # DO NOT CHANGE THIS LINE 
#                          
# NO CODE HERE
#
def distance(ins_str):          # DO NOT CHANGE THIS LINE 
    result = 0                    # DO NOT CHANGE THIS LINE 
    vert = 0
    hor = 0
    calc = True
    for c in ins_str:
        if c not in ['r','R','l','L','u','U','d','D']:
            calc = False
            result = -1
            break
        elif c in ['r','R']:
            hor = hor + 1
        elif c in ['l','L']:
            hor = hor - 1
        elif c in ['u','U']:
            vert = vert + 1
        elif c in ['d','D']:
            vert = vert - 1
    if calc:
        result = math.sqrt(vert**2 + hor**2)
        result = round(result, 4)
    return result                 # DO NOT CHANGE THIS LINE 
#                          
# NO CODE HERE
#
if __name__ == "__main__":      # DO NOT CHANGE THIS LINE 
    print(step_count('LRlURRDu')) # DO NOT CHANGE THIS LINE
    print(distance('LRlURRDu'))   # DO NOT CHANGE THIS LINE 
#                          
# NO CODE HERE
#                                                  
# QUESTION 2
#                          
# NO CODE HERE
#
def compress(input_str):                            # DO NOT CHANGE THIS LINE
    result = ''                                       # DO NOT CHANGE THIS LINE
    char = ''
    occurence = 0
    x = 0
    while x < len(input_str):
        char = input_str[x]
        occurence = 1
        y = x + 1
        while y < len(input_str):
            if input_str[x] == input_str[y]:
                occurence = occurence + 1
                y = y + 1
            elif input_str[x] != input_str[y]:
                break
        x = x + occurence 
        result = result + char + str(occurence)
    return result                                     # DO NOT CHANGE THIS LINE
#                          
# NO CODE HERE
#
if __name__ == "__main__":                          # DO NOT CHANGE THIS LINE 
    print(compress(''))                               # DO NOT CHANGE THIS LINE
    print(compress('a'))                              # DO NOT CHANGE THIS LINE
    print(compress('AAAAATTTTGGGGCCCCAAA'))           # DO NOT CHANGE THIS LINE
    print(compress('##########'))                     # DO NOT CHANGE THIS LINE
    print(compress('zzz ZZ  zZzZ'))                   # DO NOT CHANGE THIS LINE
#                          
# NO CODE HERE
#
# QUESTION 3
#
# NO CODE HERE
#
def any_smaller(lst, level):    # DO NOT CHANGE THIS LINE 
    result = False                # DO NOT CHANGE THIS LINE
    smallest = level
    x = 0
    while x < len(lst):
        if min(lst[x]) < smallest:
            smallest = min(lst[x])
            #print(smallest)
        x = x+1
        if (level > smallest):
            result = True
            break
    return result                 # DO NOT CHANGE THIS LINE
#                          
# NO CODE HERE
#
def all_smaller(lst, level):    # DO NOT CHANGE THIS LINE 
    result = True                 # DO NOT CHANGE THIS LINE
    largest = 0
    x = 0
    while x < len(lst):
        if max(lst[x]) > largest:
            largest = max(lst[x])
            #print(largest)
        x = x+1
    if (level <= largest):
        result = False
    return result                 # DO NOT CHANGE THIS LINE
#                          
# NO CODE HERE
#

def max_exp(lst, level):        # DO NOT CHANGE THIS LINE
    result = 0                    # DO NOT CHANGE THIS LINE
    
    def solve_tank(tank, fish):
        '''
        add all values in a tank together if nothing in the tank is bigger than the fish

        otherwise return -1
        '''
        exp = 0
        if !all_smaller(tank, fish):
            return -1
        else:
            for row in tank:
                for bf in row:
                    exp = exp+bf
            return exp

    def slice_tank(tank, y_offset = 0, x_offset = 0):
        return [
            [
                tank[y_offset][x_offset], 
                tank[y_offset][x_offset+1]
            ],[
                tank[y_offset+1][x_offset], 
                tank[y_offset+1][x_offset+1]
            ]
        ]

    sums = []
    width = len(lst[0])
    height = len(lst)

    for i in range(0, height):
        for j in range(0, width):
            sums.append(
                solve_tank(
                    slice_tank(
                        lst, 
                        i, 
                        j), 
                    level
                    ))

    return max(sums)

## henri's code below
    sums = []
    if all_smaller(lst,level):
        y = 0
        while y != len(lst):
            x = 0
            while x+1 != len(lst[y]):
                total = lst[y][x] + lst[y][x+1]
                x = x+1
                sums.append(total)
            y = y + 1
        #print(sums)
        width = len(lst[0])-1
        height = len(lst) - 1
        runs = width * height
        #print(runs)
        combos = len(lst[0])-1
        final = []
        start = 0
        while runs != 0:
            sums2 = sums[start]+sums[start+combos]
            final.append(sums2)
            runs = runs - 1
            start = start + 1
        print(final)
        result = max(final)
    return(result)                # DO NOT CHANGE THIS LINE
#                          
# NO CODE HERE
#
if __name__ == "__main__":      # DO NOT CHANGE THIS LINE 
    lst1 = [[5,4,3],              # DO NOT CHANGE THIS LINE 
         [6,7,8],               # DO NOT CHANGE THIS LINE 
         [4,7,8]]               # DO NOT CHANGE THIS LINE 
    lst2 = [[7,7,7,7,7],          # DO NOT CHANGE THIS LINE 
          [1,6,5,5,5],          # DO NOT CHANGE THIS LINE 
          [9,8,5,5,1]]          # DO NOT CHANGE THIS LINE 
    print(any_smaller(lst1, 3))   # DO NOT CHANGE THIS LINE 
    print(any_smaller(lst1, 4))   # DO NOT CHANGE THIS LINE 
    print(all_smaller(lst1, 8))   # DO NOT CHANGE THIS LINE 
    print(all_smaller(lst1, 10))  # DO NOT CHANGE THIS LINE 
    print(max_exp(lst1, 9))       # DO NOT CHANGE THIS LINE 
    print(max_exp(lst2, 7))       # DO NOT CHANGE THIS LINE 
#                          
# NO CODE HERE
#


# In[ ]:




