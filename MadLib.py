#MadLib.py
#Name: Ayo Fatoye
#Date: September 10, 2024
#Assignment: Madlib

def main():
  print("Madlib")
  #Ask user for words
  noun1 = input("Enter a noun: ")
  name = input("Enter a name: ")

  #Print the story with the user supplied words.
  print("I like to ride a " + noun1 + " with my friend " + name + " is fun.")
  print("I like to ride a", noun1, "with my friend", name, "is fun.")

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
