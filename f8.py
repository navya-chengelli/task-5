string1 = input("Enter the first string: ").replace(" ", "").lower()
string2 = input("Enter the second string: ").replace(" ", "").lower()
string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()
if len(string1) != len(string2):
    print("The strings are not anagrams.")
else:
    sorted_str1 = sorted(string1)
    sorted_str2 = sorted(string2)
    if sorted_str1 == sorted_str2:
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")
