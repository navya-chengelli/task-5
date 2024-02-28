
input_string = input("Enter a string: ")
most_frequent_char = ""
max_count = 0
for char in input_string:
    count = 0
    for c in input_string:
        if c == char:
            count += 1
    if count > max_count:
        max_count = count
        most_frequent_char = char
print("Most frequent character:", most_frequent_char)
