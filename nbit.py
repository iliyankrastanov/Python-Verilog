from itertools import product
arr = 0
val_x = []
val_y =[]

n = int(input('n = '))

if __name__ == "__main__":

    for x in range (0, n + 1):
        for y in range (0, n + 1):
            if y == 0:
                arr += 1
        if arr == 1:
            val_x.append(x)
            val_y.append(x)
        arr = 0


    res = list(product(val_x, val_y))
    

    print(res)

    print("--- --- --- ---")
