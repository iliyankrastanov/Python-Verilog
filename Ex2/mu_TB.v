`timescale 1ns / 1ps

module mul_TB();
parameter n = 2;

reg  [(n-1)    :0] x;
reg  [(n-1)    :0] y;
wire [(2*n)-1  :0] p;
 
 integer i;
 integer j;
 integer file;
 
mul dut
   (
    .x(x),
    .y(y),
    .p(p)
   );

initial begin
file = $fopen("results.dat","wb");

{i, j, x, y} = 0;
  
   for (i = 0; i < (n*2); i = i + 1)begin
      #1 x = i;
      for (j = 0; j < (n*2); j = j + 1)begin
         y = j;
         #1;
   $fwrite(file, "%4b\n", p);
      end
   end
#1 $finish;
$fclose(file);
end
endmodule
