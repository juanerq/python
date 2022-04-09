# from distutils.command.clean import clean
# from random import randint
# from os import system

# result = False

# while result != True:
#   system("clear")
#   num1 = randint(1, 100)
#   num2 = randint(1, 100)

#   resultMult = int(input("Dame el resultado de multiplicar {} x {} = ".format(num1, num2)))

#   if resultMult == (num1 * num2):
#     result = True

# print("Lo has conseguido!!")


# fibo = [0,1]

# for i in range(1,10):
#   suma = fibo[i - 1] + fibo[i]
#   fibo.append(suma)

# print(fibo)


# 0 1 1 2 3 5 8 13 21...

# cache = {6: 8}

# def fibo(n):
#   if n == 0 or n == 1:
#     return n
#   else:
#     return fibo(n - 2) + fibo(n - 1)

# print(fibo(10))

# list = [11,2,3,54,1,2,8,9]

# def bubbleSort(list):
#   length = len(list) - 1
#   for e in range(0, length):
#     for i in range(0, length):
#       if list[i] > list[i+1]:
#         aux = list[i]
#         list[i] = list[i+1]
#         list[i+1] = aux

#   return list

# print(bubbleSort(list))

def quickSort(list):
  if len(list) < 1:
    return []

  listLeft = []
  listRight = []
  pivot = list.pop(0)

  for n in list:
    if n < pivot:
      listLeft.append(n)
    else:
      listRight.append(n)

  return quickSort(listLeft) + [pivot] + quickSort(listRight)

# print(quickSort(list))

def factorial(num):
  if num <= 1:
    return 1
  print(num)
  return num * factorial(num - 1)
   

# print(factorial(5)) 

text = "Hola, me llamo Juan. ¿Tu como te llamas?"

def countCharacters(text):
  textToList = list(text)

  def count(character):
    cont = 0
    while character in textToList:
      cont += 1
      del textToList[textToList.index(character)]
    return cont

  return count

countFunction = countCharacters(text)

# print( countFunction(" ") )
# print( countFunction(",") )
# print( countFunction(".") )


listNumber = [11,2,3,54,1,2,8,9,0]

# List Comprehesion
listNumber = [num + 1 for num in listNumber]

def lookUpNumber(list):
  num = [0,0]

  for n in range(1, len(list)):
    if list[num[0]] > list[n]:
      num[0] = n
    elif list[num[1]] < list[n]: 
      num[1] = n

  return f'Bigger number: {list[num[1]]}\nMinor number: {list[num[0]]}'

print( lookUpNumber(listNumber) )


# Filtrado de listas
print('Filtrado de listas')
for num in listNumber[1:5]:
  print(num)