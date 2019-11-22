#
#
#
#
from sys import argv # importing the argv from sys library


script, filename = argv # declear the argv


txt = open(filename) # opening the file using open()

print(f"Here's your file {filename}:") # calling a print of filename

print(txt.read()) # reading of the filename

print("Type the filename again:")

file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
