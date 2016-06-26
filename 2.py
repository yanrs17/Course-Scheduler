import itertools
from random import randint

## ==================================

#AI = {'0.5': ['CSC336H1', 'CSC438H1', 'CSC448H1', 'CSC463H1'],
      #'2.5': ['CSC401H1', 'CSC485H1', 'CSC320H1', 'CSC420H1', 'CSC321H1', 'CSC411H1', 'CSC412H1', 'CSC384H1']}
#CL = {'ALL': ['CSC318H1', 'CSC401H1', 'CSC485H1', 'PSY100H1'],
       #'1.5': ['CSC321H1', 'CSC411H1', 'CSC428H1']}
#CS = {'ALL': ['CSC324H1', 'CSC443H1', 'CSC469H1', 'CSC488H1'],
      #'1.0': ['CSC372H1', 'CSC358H1', 'CSC458H1']}
#GD = {'ALL': ['CSC300H1', 'CSC301H1', 'CSC318H1', 'CSC324H1', 'CSC384H1', 'CSC418H1', 'CSC404H1']}
#IT = {'ALL': ['CSC358H1', 'CSC458H1', 'CSC411H1'],
      #'0.5': ['CSC443H1', 'CSC469H1']}
#CV = {'ALL': ['CSC320H1', 'CSC336H1', 'CSC411H1', 'CSC420H1', 'MAT235H1', 'MAT235H2'],
      #'0.5': ['CSC412H1', 'CSC418H1']}

ASSPE1689 = {
"Req1": ["0.5",  "CSC148H1", "CSC150H1"],
#"Req2": ["1 Requirement", "from Req3, Req4"],
"Req3": ["1.0", "CSC165H1", "CSC236H1"],
#"Req4": ["0.5",  "CSC240H1"],
#"Req5": ["1.0", "MAT135H1", "MAT136H1", "MAT135Y1", "MAT137Y1", "MAT157Y1"],
#"Req6": ["ALL", "CSC207H1", "CSC209H1", "CSC258H1"],
#"Req7": ["0.5",  "CSC263H1", "CSC265H1"],
#"Req8": ["0.5",  "MAT221H1", "MAT223H1", "MAT240H1"],
#"Req9": ["0.5",  "STA247H1", "STA255H1", "STA257H1"],
#"Req10": ["ALL", "CSC369H1"],
#"Req11": ["0.5",  "CSC373H1", "CSC375H1"],
#"Req12": ["1.5", "400 Level CSC Courses", "BCB410H1", "BCB420H1", "BCB430Y1", "ECE489H1"],
#"Req13": ["3.5", "300+ Level CSC Courses ", "BCB410H1", "BCB420H1", "BCB430Y1", "ECE385H1", "ECE489H1", "MAT224H1", "MAT235Y1", "MAT237Y1", "MAT257Y1", "MAT 300/400+ excluding 329Y, 390H & 391H", "STA248H1", "STA261H1", "STA 300-level/ C-level courses, higher"],
#"Req14": ["No more than 2.0", "MAT COURSES", "STA COURSES", "in Req12, Req13"],
#"Req15": ["No more than 1.0", "CSC490H1", "CSC491H1", "CSC494H1", "CSC495H1", "BCB430Y1", "in Req12, Req13"],
#"Req16": ["0.5",  "CSC318H1", "CSC404H1", "CSC411H1", "CSC418H1", "CSC420H1", "CSC428H1", "CSC454H1", "CSC485H1", "CSC490H1", "CSC491H1", "CSC494H1", "CSC495H1", "CSC301H1", "in Req12, Req13"],
#"Req17": ["No more than 0.5", "CSC396Y0", "in Req13"]
}

FOCUS = {
"Req1": ['0.5', 'CSC336H1', 'CSC438H1', 'CSC448H1', 'CSC463H1'],
"Req2": ['2.5', 'CSC401H1', 'CSC485H1', 'CSC320H1', 'CSC420H1', 'CSC321H1', 'CSC411H1', 'CSC412H1', 'CSC384H1']
}

#AI = {'0.5': ['CSC336H1', 'CSC438H1', 'CSC448H1', 'CSC463H1'],
      #'2.5': ['CSC401H1', 'CSC485H1', 'CSC320H1', 'CSC420H1', 'CSC321H1', 'CSC411H1', 'CSC412H1', 'CSC384H1']}
#CL = {'ALL': ['CSC318H1', 'CSC401H1', 'CSC485H1', 'PSY100H1'],
       #'1.5': ['CSC321H1', 'CSC411H1', 'CSC428H1']}
#CS = {'ALL': ['CSC324H1', 'CSC443H1', 'CSC469H1', 'CSC488H1'],
      #'1.0': ['CSC372H1', 'CSC358H1', 'CSC458H1']}
#GD = {'ALL': ['CSC300H1', 'CSC301H1', 'CSC318H1', 'CSC324H1', 'CSC384H1', 'CSC418H1', 'CSC404H1']}
#IT = {'ALL': ['CSC358H1', 'CSC458H1', 'CSC411H1'],
      #'0.5': ['CSC443H1', 'CSC469H1']}
#CV = {'ALL': ['CSC320H1', 'CSC336H1', 'CSC411H1', 'CSC420H1', 'MAT235H1', 'MAT235H2'],
      #'0.5': ['CSC412H1', 'CSC418H1']}

ALL_SUBJECTPOST = {'ASSPE1689': ASSPE1689, 'FOCUS': FOCUS}

## ==================================

def getAllCombinations(subjectPost):
    
    allCombinations = []
    
    for req in subjectPost.values():
        fce = req[0]
        if fce.lower() == 'all':
            allCombinations += [[req[1:]]]
        else:
            # Assume all are float except 'all'
            # Assume all courses are 0.5 FCE
            numCourses = int(float(fce) / 0.5)
            oneCombination = []            
            for subset in itertools.combinations(req[1:], numCourses):
                oneCombination += [list(subset)]
            allCombinations += [oneCombination]
    return allCombinations

def combineAllCombinations(allCombinations):
    
    #print(len(allCombinations))
    if len(allCombinations) == 1:
        result = allCombinations[0]
    else:
        result = []
        if (len(allCombinations) == 2):
            combo = list(itertools.product(allCombinations[0], allCombinations[1]))
        if (len(allCombinations) == 3):
            # Haven't implemented when len > 2
            pass
        for i in range(len(combo)):
            c = []
            for j in range(len(allCombinations)):
                c += combo[i][j]
            result += [c]
    return result
                
def getResult(subjectPost):

    result = getAllCombinations(subjectPost)
    return combineAllCombinations(result)

## ==================================

def getLeastNumCourses(subjectPosts, n):
    
    oneCombination = []            
    for subset in itertools.combinations(subjectPosts.values(), n):
        oneCombination += [list(subset)]
        
    NumCourse = {}
    
    for combo in oneCombination:
        result0 = getResult(combo[0])
        result1 = getResult(combo[1])
        # result2 = getResult(combo[2])
        # ...
        
        if (1): # if ...
            combo = list(itertools.product(result0, result1))
        result = []
        for i in range(len(combo)):
            c = []
            for j in range(n):
                c += combo[i][j]
            result += [c]
        
        for subjectPost in subjectPosts.keys():
            if subjectPosts[subjectPost] == combo[0]:
                sp1 = subjectPost
            if subjectPosts[subjectPost] == combo[1]:
                sp2 = subjectPost
            # ...

        for i in range(len(result)):
                          
            
            currentCombo = list(set(result[i]))
            currentCombo.sort()
            lenOfCurrentCombo = len(currentCombo)
            if lenOfCurrentCombo not in NumCourse:
                NumCourse[lenOfCurrentCombo] = []
            sps = [sp1, sp2] # ...
            sps.sort()
            wantsToAdd = [[sps, currentCombo]]
            if wantsToAdd[0] not in NumCourse[lenOfCurrentCombo]:
                NumCourse[lenOfCurrentCombo] += wantsToAdd
    return NumCourse

if __name__ == '__main__':

    result = getLeastNumCourses(ALL_SUBJECTPOST, 2)
    print(result)