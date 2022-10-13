# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 17:08:55 2022

@author: PC_RC
"""

class Citizen:
    def __init__(self, name, age, dob, id_number):
        self.citizen_name = name
        self.citizen_age = age
        self.citizen_dob = dob
        self.citizen_id_number = id_number
    
    def add_citizen(self):
        print("Name: " + self.citizen_name)
        print("Age: " + str(self.citizen_age))
        print("Date Of Birth: " + self.citizen_dob)
        print("ID Number: " + self.citizen_id_number)
        
        
        
citizen1 = Citizen("Ishaan Patil", "11", "7th October 2011", "0269")
citizen1.add_citizen() 

citizen2 = Citizen("Sushanth Subramanya", "12", "12th September 2010", "42069")
citizen2.add_citizen()
        