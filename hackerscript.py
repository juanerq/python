from pathlib import Path
from time import sleep
from random import randrange
import sqlite3
import re
from shutil import copyfile

def delayAction():
  numberHours = randrange(1, 4)
  numberMinuts = randrange(1, 59)
  print(f"Durmiendo {numberHours} hora(s) y {numberMinuts} minuto(s)")
  # sleep(numberHours * 60 * 60 + numberMinuts * 60)


def getChromeHistory(userPath):
  urls = None
  while not urls: 
    try:
      historyPath = f"{userPath}/.config/google-chrome/Default/History"
      tempHistory =  historyPath + "temp"
      copyfile(historyPath, tempHistory)
      connection = sqlite3.connect(tempHistory)
      cursor = connection.cursor()
      cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC LIMIT 10")
      urls = cursor.fetchall()
      connection.close()
      return urls
    except sqlite3.OperationalError as error:
      print("Database a use. Retrying in 3 seconds...")
      sleep(3)


def createTxtFile(path, name):
  hackerFile = open(f"{path}/{name}", "w")
  hackerFile.write("I am Hacker and I'M in  your sistem.\n")
  return hackerFile


def scareUser(hackerFile, chromeHistory):
  for item in chromeHistory:
    hackerFile.write(f"I have seen that you visited the website of {item[0]}, interesting...\n")
    # result = re.findall("https://www.youtube.com/watch", item[2])
    # if len(result) == 1:
    #   print(item[2])


def main():
  delayAction()

  userPath = Path.home() 
  desktopPath = f"{userPath}/Escritorio"

  hackerFile = createTxtFile(desktopPath, "From you")
  chromeHistory = getChromeHistory(userPath)
  scareUser(hackerFile, chromeHistory)

 
if __name__ == "__main__":
  main()
