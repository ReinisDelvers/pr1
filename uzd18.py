while True:
  problem = input("Ievadi darbību: ")
  try:
    solution = eval(problem)
    print(solution)
  except:
    print("Darbību nevarēja aprēķināt")


    