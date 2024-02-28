string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
max_length = 0
end_position = 0
m = len(string1)
n = len(string2)
table = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if string1[i - 1] == string2[j - 1]:
            table[i][j] = table[i - 1][j - 1] + 1
            if table[i][j] > max_length:
                max_length = table[i][j]
                end_position = i
        else:
            table[i][j] = 0
start_position = end_position - max_length
longest_substring = string1[start_position:end_position]
if longest_substring:
    print("The longest common substring is:", longest_substring)
else:
    print("There is no common substring.")
