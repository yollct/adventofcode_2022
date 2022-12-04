
def make_assignment(x):
    return(int(x.split("-")[0]), int(x.split("-")[1]))

def check_containment(elf1, elf2):
    containall = False
    #efl1 
    if elf1[0]>=elf2[0] and elf1[1]<=elf2[1]:
        containall=True
    
    if elf2[0]>=elf1[0] and elf2[1]<=elf1[1]:
        containall=True
    
    return(containall)

def check_overlap(elf1, elf2):
    overlap=False
    inters = set(range(elf1[0],elf1[1]+1)).intersection(range(elf2[0], elf2[1]+1))
    if len(inters)>0:
        overlap=True

    return(overlap)


def main():
    inputx = open("day4_input.txt")
    count = 0
    for line in inputx.readlines():
        line = line.strip()
        
        elf1 = make_assignment(line.split(",")[0])
        elf2 = make_assignment(line.split(",")[1])

        #if (check_containment(elf1, elf2)):
        if (check_overlap(elf1, elf2)):
            count+=1

    print(count)

if __name__=="__main__":
    main()
        
        

