'''
x = 0
while x <= 10:
  x +=1
  print(x)
#print(x)


list1 = [1,4,7,9,11,34,65]
for item in list1:
  #print(item)
  if item <= 20:
    print(item)


numb1 = int(input("Please enter a number:\n"))
numb2 = int(input("Please enter another number:\n"))
numb3 = numb1 + numb2
print(numb3)

'''
list2 = []
counter = 0
while counter < 5:
  var = int(input("Type a number to be added into the list:\n"))
  list2.append(var)
  counter +=1
print(sum(list2))


#hi tim this is secret branch

#it seems that I can switch branches with repl.it, but not merge them in repl.it itself.