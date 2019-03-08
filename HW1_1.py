#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Exercise 1:
#Get user input:
userNum = int(input("Enter seconds from midnight: "))

#Convert user input to hrs,min,sec:
hours = int(userNum/3600)
minutes = int((userNum - hours*3600)/60)
seconds = userNum%60

#Format converted input:
if(hours>=24):
    days = int(hours/24)
    hours = hours - 24*days
if(hours<10):
    hours = "0" + str(hours)
if(minutes<10):
    minutes = "0" + str(minutes)
if(seconds<10):
    seconds = "0" + str(seconds)
    
#Output the final answer in correct format:
print("Time in military format is: %s:%s:%s"%(hours,minutes,seconds))


# In[ ]:





# In[ ]:




