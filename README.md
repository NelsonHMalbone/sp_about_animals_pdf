# what is this project:

part of a udemy course called:

Python Mega Course: Learn Python in 60 Days, Build 20 Apps

section 27 project

making a program that produces a pdf for four different aminals that where provide
to us via .txt files
this is a student project

# Day 1
 we must create a new program that makes 4 separate pdfs 
 for each animal in capitializes the first letter of the title
- date 04/25 create new program 
- pandas is installed

# Day 2 
- installed the modules 
  - to read files 
  - create paths to pull data from file
- set up a for loop to add multiple files 

# Day 3 
- always keep "pdf = FPDF(orientation='p', unit='mm', format='A4')" outside of for loop 
if not making multiple pdfs
-     with open(filepath, 'r') as file:
        content = file.read() 
- take that to read files 
