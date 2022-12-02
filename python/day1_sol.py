import math 

def sort(listcalories):
    for x in range(len(listcalories)):
        for j in range(0, len(listcalories)-x-1):
            if listcalories[j] < listcalories[j+1]:
                temp=listcalories[j]
                listcalories[j]=listcalories[j+1]
                listcalories[j+1]=temp
    
    return(listcalories)
        

def main():
    inputfile = open("day1_input.txt")

    deer_carry_the_most=0
    most_calories=0
    calories=0
    deer=0
    all_calories=[]
    for le in inputfile.readlines():
        if le =="\n":
            if calories>most_calories:
                deer_carry_the_most = deer
                most_calories=calories
            
            all_calories.append(calories)
            calories=0
            deer+=1
            
        else:
            calories+=int(le)

    final = sort(all_calories)
    print(final[0:3])
    print(f"first three calories {sum(final[0:3])}")
    print(f"{deer_carry_the_most} carry the most calories {most_calories}")

if __name__=="__main__":
    main()
        
