#uses type() to find variable type/class
testint=7 ** 5 #calculated 7exp(5) a.k.a 7^5 in some languages
print(testint)
print("7exp(5) = ",type(testint))
truncatingdivint = 17//5 #truncating division
print("truncated division of 17/5: ",truncatingdivint)
print("get variable type/class: ", type(truncatingdivint))
remainder = 17%5
print("get remainder of truncated division 17/5: ", remainder)
print("get the truncated and remainder at the same time(as a tuple): ", divmod(17,5))

#example that a-= 3 is progromatically a=a-3
a=10
print("a should be 10: a = ",a)
a -= 3
print("a should now be 7: a = ", a)
binarynum = 0b10 #base 2
print("binary num = ", binarynum)
octalnum = 0o10
print("octal based num = ", octalnum)
hexnum = 0x10
print("hex based num = ", hexnum)

#type converstions
print("Convert True to 1 using type conversion: ", int(True))
print("Convert float to int using type conversion: ", int(7.9))
print("Convert string to int using type conversion: ", int("42"))
