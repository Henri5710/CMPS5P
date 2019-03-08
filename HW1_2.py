#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Exercise 2:
#Constant variables:
PI = 3.1415

#Get user input:
userRad = float(input("Enter the radius of a circle (in inches): "))

#Convert user input to feet:
radius = userRad * 0.0833

#Compute necessary values:
diameter = 2*radius
perimeter = 2 * PI * radius
area = PI * radius**2

#Output final answers:
print('The diameter of the circle is: %.4f feet'%(diameter))
print('The perimeter of the circle is: %.4f feet'%(perimeter))
print('The area of the circle is: %.4f square feet'%(area))


# In[ ]:




