from itertools import product

def multiply(res):
    output = []
    for i in res:
        output.append(bin(int(i[0], 2) * int(i[1], 2))[2:].zfill(n * 2))
    return output

val_x = []
val_y = []

if __name__ == "__main__":

    filename = "rom_{0}x{1}.dat"

    while True:
        try:
            n = int(input('Enter n = '))
            
            name = filename.format(f'{2**(2*n)}', f'{2*n}')
            fileobject = open(name,'w')

            for x in range(n ** 2):
                arr = 0
                for y in range(n ** 2):            
                    if y == 0:
                        arr += 1
                if arr == 1:
                    val_x.append(bin(x)[2:].zfill(n))
                    val_y.append(bin(x)[2:].zfill(n))

            res_xy = list(product(val_x, val_y))

            res_z = (multiply(res_xy))
            for index in range(len(res_z)):
                value = res_z[index]
                print(value)
                fileobject.write(f'{value}\n')

            fileobject.close()
            
        except (ValueError, KeyError,NameError) as e:
            print(f'Invalid value or action ({e})')
            print("Please enter valid integer value")
        else:
            break

    filename = "multi.v"

    fileobject = open(filename,'w')
        
    fileobject.write(f"""module mempy #(parameter N = {n})
    (input [(2*N) - 1:0] address,
     input read_en,
     input ce,
     output [(2*N) - 1:0] data);
              
 reg [(2*N) - 1:0] mem [0: 2**(2*N)-1];

  assign data = (ce && read_en) ? mem[address] : 0;
  
    initial begin
  $readmemb("{name}", mem);
    end
endmodule""")

    fileobject.close()

    filename = "multi_TB.v"

    fileobject = open(filename,'w')
        
    fileobject.write(f"""`timescale 1ns / 1ps

module mempy_TB;

 parameter N = {n};

  reg [(2*N) - 1:0] address;
  reg read_en, ce;
  wire [(2*N) - 1:0] data;
 
 integer i,j;
  
mempy dut(.address(address),
          .data(data),
          .read_en(read_en),
          .ce(ce));

 initial begin
   address = 0;
   read_en = 0;
   ce      = 0;
   #10 $monitor ("address = %h, data = %h, read_en = %b, ce = %b", address, data, read_en, ce);
   for (i = 0; i < 2**(2*N); i = i + 1 )begin
     for (j = 0; j < 2**(2*N); j = j + 1)begin
     #5 address = {{i,j}};
     read_en = 1;
     ce = 1;
     #5 read_en = 0;
     ce = 0;
     address = 0;
    end
  end
end
endmodule""")

    fileobject.close()
