from collections import defaultdict
from functools import reduce

priorities = defaultdict()
for x in range(26):
    priorities[chr(65+x)] = x+1

class rucksack():
    def __init__(self, allitems):
        self.items=allitems
        self.ruck1=[]
        self.ruck2=[]
        self.common=[]

    def assign_items(self):
        nitems=len(self.items)//2

        for e in range(nitems):
            self.ruck1.append(self.items[e])
        
        for e in range(nitems, len(self.items)):
            self.ruck2.append(self.items[e])

    def get_common_items(self):
        for a in self.ruck1:
            for b in self.ruck2:
                if a==b:
                    if a not in self.common:
                        self.common.append(a)

    def assign_priorities(self):
        priority=0
        for i in self.common:
            if i in list(priorities.keys()):
                priority+=priorities[i]
                priority+=26
            else:
                priority+=priorities[i.upper()]

        return(priority)

class elfgroup:
    def __init__(self):
        self.allelf=[]
        self.badge=[]

    def add_elf(self, items):
        thiself = []
        for x in items:
            thiself.append(x)

        self.allelf.append(thiself)
        
    def get_badge(self):
        self.badge=set.intersection(*map(set,self.allelf))

    def assign_priorities(self):
        priority=0
        for i in self.badge:
            if i in list(priorities.keys()):
                priority+=priorities[i]
                priority+=26
            else:
                priority+=priorities[i.upper()]
        return(priority)

def main():
    inputx = open("day3_input.txt")

    allprior = 0
    newgroup = elfgroup()
    for e, line in enumerate(inputx.readlines()):
        if e%3 != 0 or e==0:
            newgroup.add_elf(line.strip("\n"))
        else:
            newgroup.get_badge()
            prior=newgroup.assign_priorities()
            allprior+=prior
            newgroup=elfgroup()
            newgroup.add_elf(line.strip("\n"))

    newgroup.get_badge()
    prior=newgroup.assign_priorities()
    allprior+=prior
    print(allprior)
        # thissack = rucksack(line.strip("\n"))
        # thissack.assign_items()
        # thissack.get_common_items()
        # thisprior = thissack.assign_priorities()
        # allprior+=thisprior

if __name__=="__main__":
    main()
