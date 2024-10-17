allowedsybols = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "*", "/", "-", "+", "^", "%"]
while True:
    problem = input("Ievadi darbību: ")
    for i in problem:
        for a in allowedsybols:
          if i != a:
            problem = input("Ievadi ar pareiziem simboliem: ")
    solution = problem
