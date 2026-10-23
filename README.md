This Read Me explains how to use Math_Tutor.

Math_Tutor is only for simple linear equations and does not support negative numbers, variables other than x and advanced functions.
Math_Tutor is built in the python language and uses the ipywidgets import and the IPYTHON.display import.


Title & Description: What is this project? Why did you build it? 

This project is a program that solves simple linear equations and shows the process behind the answers to attempt to explain how to solve simple linear equations to weaker mathematic students. I built this project to try and teach weaker mathematics students the thought process behind linear equations and how to achieve the correct answers and made it interactive using ipywidgets and IPYTHON.display.

Features: A bulleted list of the main functionalities. E.g. 'Saves high scores to a file using File IO' or 'Uses a binary tree to store and search questions.'

The main feature of this project includes using COLORED ipywidgets to both be more appealing to the user.

How to Run: The exact steps to run your project. What needs to be installed? What command starts the program? (python main.py)
Open Math_Tutor.py and a python running software. Copy the code over to your designated python running software and run it.
To use the actual programs:


  Type an equation into the widgets and use Load Equation to confirm your input.
  
  Use Next Step to continue solving while seeing the solver's process.
  
  Use Reset to restart the program.
However I am gonna highlight logic that I am proud of aswell:
  Python natively keeps real numbers and imaginary numbers completely separate. By substituting x = 1j, a string like "3*x + 5" becomes evaluated as the 
  complex number 5 + 3j. By calling .imag you can extract the variable coefficient (3.0), and by calling .real you can extract the standalone constant 
  (5.0).I mostly learnt this because I was LAZY and avoided recursive string spliting because complex.


  I also heard you can execute bad stuff with eval so I went to the official python website and found that u can do {"__builtins__": None} so no importing   
  and opening in the widgets typing input box thing.
  
File Structure: A simple map of your project files and what each one does.


This readme file is for the user reading this, you , to understand the purpose and functions of my other file, Math_Tutor.py.

My Math_Tutor.py is the main program. It runs the linear equation solver while showing the user how to solve it.


Class Design: Briefly describe the main classes in your project and their responsibilities.

There is only one class in my program, the Equation class.

There is NO getters or setters in the Equation class as this code is meant to automatically get the value and print it through a repeated process and you 
can use the Reset button to set the Equation over.

Reflection: What was the hardest problem you faced, and how did you solve it? If you had two more weeks, what would you add?


I am not proud of this but this project is a last minute! I am writing this as it just ticked past 12:42pm...(did not notice and all my work is redundant now)

I actually originally meant to atleast implement multiply(*) and divide(/) and I was just double checking last minute about my code...

and found out that 2x = 2 breaks because of no logic code. #queue problem highlight

I eventually fixed it by automating a multiply(*) and then code broke because 2**x...

So i decided to ditch multiply but keep the 2x = 2 code. #queue problem solved

Honestly I have to put full blame on myself because I thought I had an extra week and rushed widgets last second.

If I had 2 extra weeks would probably add back multiply somehow and also divide + widgets buttons for typing to make options clearer instead of the input box.

If there is also no activities for the 2 extra weeks I might also add brackets with coefficient features.

I also just found out about SymPy so I wrote alot of stuff for nothing.

Maybe I should have done other projects instead of math.
