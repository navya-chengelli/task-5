s = input("Enter a sentence")
count1=0
count2=0
count3=0
count4=0
count5=0
for i in s:
  if (i=='a'):
      count1 = count1+1
      print(count1,'a')
  if (i=='e'):
      count2 = count2+1
      print(count2,'e')
  if (i=='o'):
      count3 = count3+1
      print(count3,'o')
  if (i=='u'):
      count4 = count4+1
      print(count4,'u')
  if (i=='i'):
      count5 = count5+1
      print(count4,'i')
count6 = count1+count2+count3+count4+count5
print(count6) 