# Files : creating, opening, reading and writing.


#(i) Creating a file with write mode enabled and then closing it.

my_file = open("SpecialFile.txt", "w")             
my_file.close() 
               


#(ii) Writing to a file.
with open("SpecialFile.txt","w") as f:
 
 f.write("This is a special file created by Python itself(1st line).\n")    


                                              
#(iii) Appending to a file.
with open("SpecialFile.txt","a") as f:
 
 f.write("This special 2nd line has been appened by Python itself..\n")    
                                                   


#(iv) Reading some characters from the file.   

with open("SpecialFile.txt","r") as f:
 spell = f.read(9)                       # This will read first 9 characters from the file.
 print(spell,"\n") 


#(v) Reading the whole file.

with open("SpecialFile.txt","r") as f:
 spell = f.read()                          # This will read the whole file.
 print(spell)       


#(vi) Reading the first line from the file.

with open("SpecialFile.txt","r") as f:
 spell = f.readline()                     # This will read the first line of the file.
 print(spell)


#(vii) Reading the second line from the file.


 spell = f.readline()                      # This will read the second line of the file.
 print(spell)                  
 



