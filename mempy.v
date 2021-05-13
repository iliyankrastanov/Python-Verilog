module mempy #(parameter N = 2)
    (input [(2*N) - 1:0] address,
     input read_en,
     input ce,
     output [(2*N) - 1:0] data);
              
 reg [(2*N)-1:0] mem [0:2**(2*N)-1];

  assign data = (ce && read_en) ? mem[address] : 0;
  
    initial begin
  $readmemb("rom_16x4.dat", mem);
    end
endmodule
