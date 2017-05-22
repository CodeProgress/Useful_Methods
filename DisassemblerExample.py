import dis

def square(x):
    print "running"
    return x*x

dis.disassemble(square.func_code)

#   4           0 LOAD_CONST               1 ('running')
#               3 PRINT_ITEM          
#               4 PRINT_NEWLINE       

#   5           5 LOAD_FAST                0 (x)
#               8 LOAD_FAST                0 (x)
#              11 BINARY_MULTIPLY     
#              12 RETURN_VALUE 
