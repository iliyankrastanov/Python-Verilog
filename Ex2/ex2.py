# reading files
filename = "{0}_{1}.txt"
name = filename.format(f'{"Pass"}', f'{"Fail"}')

f = open(name,'w')
f1 = open("rom_16x4.dat", "r")
f2 = open("results.dat", "r")  
i = 0
  
for line1 in f1:
    i += 1
      
    for line2 in f2:
          
        # matching line1 from both files
        if line1 == line2:  
            print(" Line ", i, ": PASS") 
            f.write("PASS\n") 
            
                
        else:
            print(" Line ", i, ":")
            # else print that line from both files
            print("\tFAIL")
            print("\tFile 1:", line1, end='')
            print("\tFile 2:", line2, end='')
            f.write(f"Different found in Line {i}\n " )
            f.write(f"Line {i} in File1)--> {line1} ")
            f.write(f"Line {i} in File2)--> {line2}")
            
        break
      
# closing files
f1.close()                                       
f2.close() 
f.close()