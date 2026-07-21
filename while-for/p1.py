input_string=input("Enter a String : ")
vowel = "AEIOU"
modifier_string = ""
for char in input_string:
    upper_char = char.upper()
    if upper_char in vowel:
        modifier_string += "*"
    else :
        modifier_string += upper_char
print("Modifier String : ", modifier_string)