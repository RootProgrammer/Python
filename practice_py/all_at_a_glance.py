print()

#! print single line

print("Hello World!")

print()


#! print multiple lines

print("""Hi Zamaan.
Welcome To Python Programming.
Let\'s Start...""")

print()


#! escape sequences
#? Escape sequences allow you to include special characters in strings.
#? To do this, simply add a backslash (\) before the character you want to escape.

es="""
Single Quote = \'

Double Quote = \"

New Line = \nNEW LINED TEXT

Tab = \tTABBED TEXT

Backslash = \\

Backspace[removes white space] = \bBACKSPACED TEXT

Carriage Return[moves cursor to the beginning & replaces character(s) by characters after <CR> one by one] = \\r
"""
es2="""\na b c d e f g h i j k l m n o p q r s t u v w x y z\rCARRIAGE RETURNED TEXT."""

print(es,es2)

print()
