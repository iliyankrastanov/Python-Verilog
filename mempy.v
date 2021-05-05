module mempy #(parameter N = 8)
    (input [N - 1:0] address,
     input read_en,
     input ce,
     output [N - 1:0] data);
              
 reg [N - 1:0] mem [0: 2**(2*N)-1];
 integer file_pointer;

  assign data = (ce && read_en) ? mem[address] : 0;

 integer i;
  
    initial begin
  $readmemb("rom_256x8.dat", mem);
    end
endmodule
