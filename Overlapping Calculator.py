import itertools
from random import randint

AI = {'0.5': ['CSC336H1', 'CSC310H1', 'CSC330H1', 'CSC438H1', 'CSC448H1', 'CSC463H1'],
      '2.5': ['CSC401H1', 'CSC485H1', 'CSC320H1', 'CSC420H1', 'CSC321H1', 'CSC411H1', 'CSC412H1', 'CSC384H1', 'CSC486H1']}
CL = {'ALL': ['CSC318H1', 'CSC401H1', 'CSC485H1', 'PSY100H1'],
       '1.5': ['CSC309H1', 'CSC321H1', 'CSC330H1', 'CSC411H1', 'CSC428H1', 'CSC486H1']}
CS = {'ALL': ['CSC324H1', 'CSC443H1', 'CSC469H1', 'CSC488H1'],
      '1.0': ['CSC372H1', 'CSC358H1', 'CSC458H1']}
GD = {'ALL': ['CSC300H1', 'CSC301H1', 'CSC318H1', 'CSC324H1', 'CSC384H1', 'CSC418H1', 'CSC404H1']}
IT = {'ALL': ['CSC309H1', 'CSC358H1', 'CSC458H1', 'CSC411H1'],
      '0.5': ['CSC310H1', 'CSC443H1', 'CSC469H1']}

ALL_FOCUSES = {'AI': AI, 'CL': CL, 'CS': CS, 'GD': GD, 'IT': IT}

def getAllCombinations(subjectPost):
    
    allCombinations = []
    #oneCombination = []
    
    for fce in subjectPost.keys():
        if fce.lower() == 'all':
            allCombinations += [[subjectPost[fce]]] # Or use .append() ?
        else:
            # Assume all are float except 'all'
            # Assume all courses are 0.5 FCE
            numCourses = int(float(fce) / 0.5)
            oneCombination = []            
            for subset in itertools.combinations(subjectPost[fce], numCourses):
                oneCombination += [list(subset)]
            allCombinations += [oneCombination]
    return allCombinations

def combineAllCombinations(allCombinations):
    
    #allCombinations = getAllCombinations(CS)
    if len(allCombinations) == 1:
        result = allCombinations[0]
    elif len(allCombinations) == 2:
        result = convert2into1(allCombinations[0], allCombinations[1])
    else:
        # Haven't implemented when len > 2
        pass
    return result

def convert2into1(combo1, combo2):
    
    combo = list(itertools.product(combo1, combo2))
    result = []
    for i in range(len(combo)):
        result += [combo[i][0] + combo[i][1]]   
    return result
                
def getResult(subjectPost):

    result = getAllCombinations(subjectPost)
    return combineAllCombinations(result)

def getLeastNumCoursesIn2(subjectPosts):
    
    oneCombination = []            
    for subset in itertools.combinations(subjectPosts.values(), 2):
        oneCombination += [list(subset)]
        
    NumCourse = {}
    
    for combo in oneCombination:
        result0 = getResult(combo[0])
        result1 = getResult(combo[1])
        result = convert2into1(result0, result1)
        
        for subjectPost in subjectPosts.keys():
            if subjectPosts[subjectPost] == combo[0]:
                sp1 = subjectPost
            if subjectPosts[subjectPost] == combo[1]:
                sp2 = subjectPost       

        for i in range(len(result)):
                          
            
            currentCombo = list(set(result[i]))
            lenOfCurrentCombo = len(currentCombo)
            if lenOfCurrentCombo not in NumCourse:
                NumCourse[lenOfCurrentCombo] = []
            else:
            #if lenOfCurrentCombo == 8:
                currentCombo.sort()
                wantsToAdd = [[[sp1, sp2], currentCombo]]
                if wantsToAdd[0] not in NumCourse[lenOfCurrentCombo]:
                    NumCourse[lenOfCurrentCombo] += wantsToAdd
            #if lenOfCurrentCombo < leastNumCourse:
                #leastNumCourse = lenOfCurrentCombo
    return NumCourse    

if __name__ == '__main__':

    result = getLeastNumCoursesIn2(ALL_FOCUSES)
    #print result