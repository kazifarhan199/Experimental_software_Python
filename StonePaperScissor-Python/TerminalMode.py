from random import randrange

MainDict = {"STONE":0,"PAPER":1,"SCISSOR":2}
MainList = list(MainDict.keys())

def main(H_C):
    C_C = randrange(0,3)
    H_C = MainDict[H_C]
    if (H_C == C_C):
        Result = "TIE"
    elif (H_C == 0 and C_C == 2) or (H_C == 1 and C_C == 0) or (H_C == 2 and C_C == 1):
        Result = "WIN"
    else:
        Result = "LOSS"
    return MainList[C_C], Result

if __name__ == '__main__':
    H_C = input("STONE PAPER OR SCISSOR : ")
    H_C = H_C.upper()

    if H_C in MainList:
        C_C, Result = main(H_C)
        print('\n'+H_C + ' VS '+C_C)
        print('\n'+Result+'\n')
    else:
        print("INVALIED INPUT")
