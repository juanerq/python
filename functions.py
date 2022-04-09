# 0 1 1 2 3 5 8 13

def fibonacci(num):
  if num == 0 or num == 1:
    return num
  return fibonacci(num - 2) + fibonacci(num - 1)

def fibonacciLoop(num):
  succession = []
  for i in range(num):
    succession.append(fibonacci(i))
  return succession

def potency(base, exponente = 2):
  if exponente == 0:
    return 1
  return base * potency(base, exponente=exponente - 1)

# a = open(f"{name}.txt", "w")
# a.write(", ".join(fibonacci))
# a.close()

def saveFile(name):
  fibonacciList = [ str(num)  for num in fibonacciLoop(8) ]
  
  with open(f"{name}.txt", "w") as myFile:
    myFile.write(", ".join(fibonacciList) + "\n")

def fileContent(name):
  try:
    with open(f"{name}.txt", "r") as  fileContent:
      return fileContent.read().replace("\n", "").split(", ")
  except FileNotFoundError:
    print("File not found")

def main():
  # print(fibonacci(6))
  # print(potency(5, exponente=4))
  saveFile("fibonacci")
  content = fileContent("fibonacci")
  print(content)

if __name__ == "__main__":
  main()
