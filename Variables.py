# i meannnnnn
# if you already know this in the other coding languages than just skip till Line ???
# if you dont then

# Variable → A Container for a value which can be the following
#            -  String
#            -  Integer
#            -  Float
#            -  Boolean
# Variables behaves as if it was the value it contains

# each variable must have a unique name
# like ↓↓↓

print("==============================================================")
print()
first_name = "Andy"
print(first_name)
print()

# once you run it it will display the name that you put
# - Yes...you can change the name to any kind
# but dont do it like this 

# print ("first_name")

# ↑↑↑
# When running that you will display "first_name"
# - The only thing is that the Quotation marks dont get displayed

# However You can use your variable along with some texts and its called
# - f-string

##############################################################################################
# HOW TO USE f-string
# To use formatted string literals,
#   - begin using a string with f or F before the opening quotation mark or TRIPLE Quotation
#     mark. Inside the String, you can write a python expression between { and } characters
#     that can refer to variables or literal values 
# This is how you use it

print(f"Hello {first_name} :))")
print()

# the f means format
# AND REMEMBER
#   - USE THE { } ON THE VARIABLE
# And Click run 
##############################################################################################

# now lets goo for something else like ohhh maybeeeeee favorite OST song
# Sooooo ↓↓↓

song = "The Heartwoods - Pokemon Legends: Arceus" 
print(f"Wou like {song}. such a Banger")
print()
print("==============================================================")

#yeahhh ig you get the point same with numbers and float like ↓↓↓

print()
x = 12
print(f"your Favorite number is {x}")
print()
cs_per_game = 8.91
print(f"Im looking at your soccer status...and it tells me you were a CB, RB & RWB. Your Clean Sheets per game was {cs_per_game}")
print()

# Boolean 
#   - It can be either true or false and it starts as a capital like ↓↓↓

is_andy_cool = True
print(f"Is Andy Cool?: {is_andy_cool}")
print()

# we dont usually use it like this really
# we used on the "if" statements...you'll see...

if is_andy_cool:
  print("Cool Guy :))")
else:
  print("No Way Jose")
