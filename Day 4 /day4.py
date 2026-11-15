# Day 4: Strings
# 1. Concatenate the string "Thirty", "Days", "Of", "Python" to a single string. "Thirty Days Of Python"
string1 = "Thirty"
string2 = "Days"
string3 = "Of"
string4 = "Python"
result1 = string1 + " " + string2 + " " + string3 + " " + string4
print(result1)

# 2. Concatenate the string "Coding", "For", "All" to a single string. "Coding For All"
result2 = "Coding" + " " + "For" + " " + "All"
print(result2)

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = result2

# 4. print the variable company using print().
print(company)

# 5. print the length of the company string using len() method and print().
print(len(company))

# 6. Change all the charaters to uppercase using the upper() method. 
print(company.upper())

# 7. Change all the characters to lowercase letters using the lower() method. 
print(company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(result2.capitalize())
print(result2.title())
print(result2.swapcase())

# 9. Cut(slice) out the first word of Coding for all string.
result3 = result2[0:7]
print(result3)

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(result2.index("Coding"))
print(result2.find("Coding"))

# 11. Replcae the word coding in the string 'Coding For All' to Python.
result4 = result2.replace("Coding", "Python")
print(result4)

# 12. Change Python for Everyone to Python for All using the replace method or other mehthods. 
result5 = "Python For Everyone".replace("Everyone", "All")
print(result5)

# 13. Split the string "Coding For All" using space as the separator (split()).
result6 = result2.split()
print(result6)

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma
string6 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
result7 = string6.split(", ")
print(result7)

# 15. What is the character at index 0 in the string Coding For All. 
result8 = result2[0:1]
print(result8)

# 16. What is the last index of the string Coding For All.
result9 = result2[-1:]
print(result9)

# 17. What character is at index 10 in "Coding For All" string.
result10 = result2[10:11]
print(f"this is result 10 '{result10}' which is a blank space and why i wrote this")

# 18. Create an acronym or an abbreviation for the name "Python For Everyone".
PFR = "Python For Everyone"

# 19. Create an acronym or an abbreviation for the name 'Coding For All'. 
CFA = "Coding For All"

# 20. Use index to determine the position of the first occurrence of C in Coding For All. 
print(result2.index("C"))


# 21. Use index to determine the position of the first occurrence of F in Coding For All. 
print(result2.index("F"))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People. 
string7 = "Coding For All People"
print(string7.rfind("l"))

# 23. Use index or find to find the position of the first occurrence of the word "because" in the following sentence: "You cannot end a sentence with becaseu becaseu because is a conjunction"
string8 = "You cannot end a sentence with because because because is a conjunction"
print(string8.find("because"))

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: "You cannot end a sentence with because because because is a conjunction"
print(string8.rfind("because"))

# 25. Slice out because because because
string9 = string8[31:54]
print(string9)

# some questions were dupes
# 28. Does 'Coding For All' start with a substring Coding?
print(result2.rindex("Coding"))

# 29. Does 'Coding For All' end with the substring coding?
print(result2.find("coding"))

