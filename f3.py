s = input("Enter a string ")
result=" "
for i in s:
  if i not in['a','e','i','o','u']:
    result +=i
print(result)