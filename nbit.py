from itertools import product
arr = 0
val_x = []
val_y =[]
n = int(input('n = '))

if __name__ == "__main__":

    for x in range(n + 1):
        for y in range(n + 1):
            if y == 0:
                arr += 1
        if arr == 1:

            val_x.append(f"{x:02b}")
            val_y.append(f"{x:02b}")
        arr = 0

res = list(product(val_x, val_y))
print(res)
