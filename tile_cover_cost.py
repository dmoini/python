def ask():
    width = int(input("What is the width of each tile? "))
    length = int(input("What is the length of each tile? "))
    cost = int(input("What is the cost of each tile? "))
    return width, length, cost

def cost():
    width, length, cost = ask()
    print(width * length * cost)


cost()
