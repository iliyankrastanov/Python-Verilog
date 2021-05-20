`timescale 1ns / 1ps

module mul (x, y, p);
parameter n = 2;

input  [(n-1)    :0]  x;
input  [(n-1)    :0]  y;
output [(2*n)-1  :0]  p;

wire [(n-1) :0] multi_tmp [(n-1) :0];
wire [(n-1) :0] produ_tmp [(n-1) :0];
wire [(n-1) :0] carry_tmp;

genvar i, j;
generate 
 //initialize values
 for(j = 0; j < n; j = j + 1) begin
    assign multi_tmp[j] =  x & {n{y[j]}};
 end
 
 assign produ_tmp[0] = multi_tmp[0];
 assign carry_tmp[0] = 1'b0;
 assign p[0] = produ_tmp[0][0];
 
 for(i = 1; i < n; i = i + 1) begin
    cla_adder #(.width(n)) add1
       (
         .sum        (produ_tmp[i]),
         .carry_out  (carry_tmp[i]),
         .carry_in   (1'b0)        ,
         .in1        (multi_tmp[i]),
         .in2        ({carry_tmp[i-1],produ_tmp[i-1][(n-1)-:(n-1)]})
       );     
    assign p[i] = produ_tmp[i][0];
 end 
    assign p[(n+n-1):n] = {carry_tmp[n-1],produ_tmp[n-1][(n-1)-:(n-1)]};
endgenerate
endmodule //end Multiplier
//-------------------------------------------------------------------------//
`timescale 1ns / 1ps

module cla_adder (in1, in2, carry_in, sum, carry_out);
parameter width = 4;

input  [width - 1 :0]  in1;
input  [width - 1 :0]  in2;
input                  carry_in;
output [width - 1 :0]  sum;
output                 carry_out;
//assign {carry_out, sum} = in1 + in2 + carry_in;
wire [width - 1 :0]  gen;
wire [width - 1 :0]  pro;
wire [width     :0]  carry_tmp;

genvar j, i;
generate
 //assume carry_tmp in is zero
 assign carry_tmp[0] = carry_in; 
 //carry generator
 for(j = 0; j < width; j = j + 1) begin
    assign gen[j] = in1[j] & in2[j];
    assign pro[j] = in1[j] | in2[j];
    assign carry_tmp[j+1] = gen[j] | pro[j] & carry_tmp[j];
 end 
 assign carry_out = carry_tmp[width]; 
 //assign sum[0] = in1[0] ^ in2 ^ carry_in;
 for(i = 0; i < width; i = i+1) begin
    assign sum[i] = in1[i] ^ in2[i] ^ carry_tmp[i];
 end 
endgenerate 
endmodule //end CLA Adder
