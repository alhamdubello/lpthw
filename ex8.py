#Adding more comments and printing
#printing printing printing
#
#
#
#
#
formatter = "{} {} {} {}"# this should create a variable with a place holder

print(formatter.format(1, 2, 3, 4)) #the place holders will be filled by 1,2,3,4

print(formatter.format("one","two", "three", "four")) # values inserted into the place holder are now strings rather than integers

print(formatter.format(True, False, True, False)) # Now using Booleans to replace the place holders

print(formatter.format(formatter, formatter, formatter, formatter)) # i think creating some type of nested formatting with formatter

##This should represent a multiline strings
print(formatter.format(
  "Try your",
  "Own text here",
  "Maybe a poem",
  "Or a song about fear"
))
