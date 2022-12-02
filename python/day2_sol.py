me2elf = {"X":"A", "Y":"B", "Z":"C"}
elfwin = {"A":"C", "B":"A", "C":"B"}
elflose={"A":"B", "B":"C","C":"A"}
shapescore = {"A":1, "B":2, "C":3}

def main():
    inputx = open("day2_input.txt")
    score = 0
    for x in inputx.readlines():
        elfcol = x.split(" ")[0]
        mycol = x.split(" ")[1].strip("\n")
       # myres = me2elf[mycol]

        #check 
        # if elfcol == myres:
        #     #draw
        #     score += 3
        # elif elfwin[myres]==elfcol:
        #     #win
        #     score+=6
        # else:
        #     score+=0
        if mycol=="X":
            myres = elfwin[elfcol]
            score+=shapescore[myres]
        elif mycol=="Y":
            score+=shapescore[elfcol]
            score+=3
        elif mycol=="Z":
            myres=elflose[elfcol]
            score+=shapescore[myres]
            score+=6


    print(score)

if __name__=="__main__":
    main()