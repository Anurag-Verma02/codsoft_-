Tasks = []

def addtask():
  b = input("Enter the task which you want to do: ")
  Tasks.append(b)
  print(f"{b} is added to the task list.")

def removetask():
  try:
    c = input("Enter the task which you want to remove: ")
    Tasks.remove(c)
    print(f"{c} is removed from the task list.")
  except ValueError :
    print("Task not found.")  

def viewtask():
  print("your task list is: ")
  task = 0
  for index, task in enumerate(Tasks):
    print(f"{index+1}: {task}")
    

print("WELCOME TO THE TO DO LIST ")
print("-------------------------------------------------- ")
print("-------------------------------------------------- ")
while True:    
  
  print("\nWHAT WOULD YOU LIKE TO DO?")
  print("1. Add a task which you want to do.")
  print("2. Remove the task which you have completed.")
  print("3. Show the tasks which you have to do.")
  print("4. Exit the program.")
  print("-------------------------------------------------- ")
  a = input("Enter your choice(1-4): ")
  print("-------------------------------------------------- ")
  if a == "1":
    addtask()
  elif a == "2":
    removetask()
  elif a == "3":
    viewtask()
  elif a == "4":
    print("YOU HAVE QUITED THE PROGRAM.")
    break
  else:
    print("PLEASE ENTER A CHOICE FROM 1 TO 4 ONLY")

print("Thank you for using the program.")
  

  
