formatter = "{} {} {} {}"

print (formatter.format(1,2,3,4))

print (formatter.format("one","two","three","four"))

print (formatter.format(True, False, True, False))

print (formatter.format(formatter, formatter, formatter, formatter))

print (formatter.format("I am", "kinda enjoying", "programming", "unlike before"))

# Syntax
# We are passing argumets to formatter as variables,keywords and strings by using the .format() function
# True and False are keywords
# true , false, TRUE, FALSE or anyother variation is not
