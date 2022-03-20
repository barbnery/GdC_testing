from tempConvert import fahr_cel, cel_fahr

print("Init unit testing temperature conversion:\n")

print("Fahrenheit to Celsius:\n")
test=fahr_cel(32)
print("32.0 fahrenheit to C: ",test)
assert test == 0.0, "Should be 0.0"

test=fahr_cel(113)
print("113.0 fahrenheit to C: ",test)
assert test == 45.0, "Should be 45.0"

test=fahr_cel(50)
print("50.0 fahrenheit to C: ",test)
assert test == 10.0, "Should be 10.0"

test=fahr_cel(59)
print("59.0 fahrenheit to C: ",test)
assert test == 15.0, "Should be 15.0"



print("Celsius to Fahrenheit:\n")
test=cel_fahr(0)
print("0.0 celsius to F: ",test)
assert test == 32.0, "Should be 32.0"

test=cel_fahr(15)
print("15.0 celsius to F: ",test)
assert test == 59.0, "Should be 59.0"

test=cel_fahr(110)
print("110.0 celsius to F: ",test)
assert test == 230.0, "Should be 230.0"

test=cel_fahr(25)
print("25.0 celsius to F: ",test)
assert test == 77.0, "Should be 77.0"
