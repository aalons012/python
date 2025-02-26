# TypeCasting → The Process of converting a variable from 1 data to another

# there are various functions to convert a value/variable to the Following
#   - str()
#   - int()
#   - float()
#   - bool() 

# Lets get to it shall we ?

name = "Andy Alonso"
age = 23
gpa = 3.88
is_student = True

# you can actually get the data type of a variable/value by using this \
# ↓↓↓

# well be using the name in line 12 → type(name)

# ↑↑↑
# once running it...theres nothin
# sooo we need to add print + type + Variable
# As Shown Below

print()
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))
print()

# using these typcast form we can form 1 data type to another
# peakk this one truuuuustttt

print("FOR INT")
gpa = int(gpa)
print()
print(f"GPA Whole number (NOT ROUNDED): {gpa}")
print()

# Once hitting run what its "different" right?
# yep :))
# only difference is that it truncate the decimal point to A WHOLE NUMBER
# now
# lets change the age to a float
# Shall we 

age = float(age)
print(f"your age: {age}")
print()

# After hitting run it became a number with a decimal point
# WOW
# and now
# lets convert a number to a string

age = str(age)
print(age)
print()
# age += 1

# and with that it becomes a string...NOT A INTEGER
# it may look the same way it is butttt its not
# dont belive me? 
# Uncomment line 61 and run it
# LOOOOK

print(type(age))
print()

# told you...LOL
# it is the same thing as doing this ↓
#   -  age = "25" 
# after uncommenting line 61 it give you an error
# WHY???
# because the AGE IS A STRING 
# now
# what if we do this instead

age += "1"
print(age)
print()

# what do you think will happen???
# run it...
# WOA I AINT THAT OLD MAN WTF LMAOOOO
# oh wait its still a float because of the other formatting soo ig i aint that old then huh LOL
#  so now im 23.01 years old...nice :))

# SO
# Strings and Numbers behave different
# with numbers
# it can be used them within arithmetic Exoressions
# Strings... 
# not so much

# Now its time to take our variable name and typecast it to a boolean

name = bool(name)
print(name)

# for this it gives a different response  
# if you typecast your string of text into a boolean
# NO MATTER WHAT 
# IF IT HAS ANY TEXT
# OF ANY KIND
# ...it becomes true...See?
# and remember
# Boolean can ONLY Display either
# True
# or
# False
# so if it has text? Its True
# If theres NO text? Its False
# SIMPLE AS IT IS 
