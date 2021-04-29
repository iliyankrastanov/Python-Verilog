from itertools import product

def multiply(res):
    output = []
    for i in res:
        output.append(bin(int(i[0], 2) * int(i[1], 2))[2:].zfill(n * 2))
    return output

arr = 0
val_x = []
val_y = []

if __name__ == "__main__":

    while True:
        try:
            n = int(input('Enter n = '))       
                
            for x in range(n ** 2):
                for y in range(n ** 2):            
                    if y == 0:
                        arr += 1
                if arr == 1:
                    val_x.append(bin(x)[2:].zfill(n))
                    val_y.append(bin(x)[2:].zfill(n))
                arr = 0

            res_xy = list(product(val_x, val_y))
            #print(f'Input = {res_xy}')

            res_z = (multiply(res_xy))
            print(f'Output = {res_z}')

        except (ValueError, KeyError,NameError) as e:
            print(f'Invalid value or action ({e})')
            
        else:
            break
