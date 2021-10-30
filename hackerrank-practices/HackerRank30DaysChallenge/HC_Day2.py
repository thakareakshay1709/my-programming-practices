#!/usr/bin/env python
# coding: utf-8

# # This is the exercise with 'Operators'
# # Day 2 challange - Hacker Rank - Python

# In[13]:


#Executing solve function
def solve(meal_cost, tip_percent, tax_percent):
    print("Solve function - ","Meal =",meal_cost," Tip % =",tip_percent," Tax % =",tax_percent)
    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100
    total = round(meal_cost + tip + tax)
    print("Total =",total, "Meal =",meal_cost," Tip =",tip, " Tax =", tax)
    
meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())
#Called solve function
solve(meal_cost,tip_percent,tax_percent)
#print("Total Cost=",total_cost)
    


# In[ ]:




