input_string = input("Enter a string: ")
input_string = input_string.replace(" ", "").lower()
start_index = 0
end_index = len(input_string) - 1
is_palindrome = True
while start_index < end_index:  
    if input_string[start_index] != input_string[end_index]:
        is_palindrome = False
        break  
    start_index += 1
    end_index -= 1
if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")