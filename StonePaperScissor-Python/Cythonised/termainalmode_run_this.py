from TerminalMode import main 
MainList={"STONE","PAPER","SCISSOR"}

H_C = input("STONE PAPER OR SCISSOR : ")
H_C = H_C.upper()

if H_C in MainList:
    C_C, Result = main(H_C)
    print('\n'+H_C + ' VS '+C_C)
    print('\n'+Result+'\n')
else:
    print("INVALIED INPUT")
