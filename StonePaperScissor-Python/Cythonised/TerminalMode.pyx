from random import randrange
MainDict = {"STONE":0,"PAPER":1,"SCISSOR":2}
MainList = list(MainDict.keys())

cpdef  main(str H_CC):
	cdef int C_C = randrange(0,3)
    cdef int H_C = MainDict[H_CC]
	
	
    if (H_C == C_C):
        Result = "TIE"
    elif (H_C == 0 and C_C == 2) or (H_C == 1 and C_C == 0) or (H_C == 2 and C_C == 1):
        Result = "WIN"
    else:
        Result = "LOSS"

    return MainList[C_C], Result
