size = int(input("Enter the number of plants: "))
heights = list(map(float,input("Enter the hieghts of the plants: ").split(sep=" ")))
sets = set(heights)
average = sum(sets)/len(sets)
print("%.3f"%average)