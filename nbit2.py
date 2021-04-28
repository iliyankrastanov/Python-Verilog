from itertools import product

arr = 0
val_x = []
val_y = []
n = int(input('n = ')) 

def multiply(product, *nums):
    factor = product
    for num in nums:
        factor *= num
    return factor

if __name__ == "__main__":

    for x in range(n + 1):
        for y in range(n + 1):
            if y == 0:
                arr += 1
        if arr == 1:
            val_x.append(bin(x)[2:].zfill(n))
            val_y.append(bin(x)[2:].zfill(n))
        arr = 0

res = list(product(val_x, val_y))

print(res)
print(f'Z = {multiply(res)}') # Ne umnojava truple-a a go dublira
