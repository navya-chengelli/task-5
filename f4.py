s = input("Enter a string ")
unchar = []
number = 0
for i in s:
  if i not in unchar:
    unchar.append(i)
number = len(unchar)
print(number)