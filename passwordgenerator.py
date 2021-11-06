# An Extremly Symple Password Generator Using Python

import random

Lower = "abcdefghijklmnopqrstuvwxyz"
Upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Number = "0123456789"
Symbol = "[]{}#()*;._-"

all = Lower + Upper + Number + Symbol

length = 25 # Change Value To The Number Of Characters You Want Your Password To Contain

password = "".join ( random.sample ( all,length ) )
print ( " Here is your randomly generated passowrd: " , password )

# That's Literally It, It's That Simple.
