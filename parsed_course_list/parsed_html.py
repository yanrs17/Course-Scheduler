import os
import re
from bs4 import BeautifulSoup

list = []

for file in os.listdir('/Users/Jun/Desktop/Projects/UTADA/Course-Scheduler/Designators'):
    fullpath = os.path.join('/Users/Jun/Desktop/Projects/UTADA/Course-Scheduler/Designators', file)
    soup = BeautifulSoup(open('/Users/Jun/Desktop/Projects/UTADA/Course-Scheduler/Designators/' + file), "html.parser")

    file = soup.pre.string.replace('20171": ', '20169": ')
    course_list = file.split('20169": ')

    subject_list = []

    for index in range(1, len(course_list)):
        content = course_list[index].split("{")
        wanted = []
        dict = {}
        for part in content[1].split('": '):
            s = ''
            for string in part.split(',')[:-1]:
                s += string
            wanted.append(s)
        dict["org"] = wanted[1].strip('"')
        dict["orgName"] = wanted[2].strip('"')
        dict["courseTitle"] = wanted[3].strip('"')
        dict["code"] = wanted[4].strip('"')
        dict["courseDescription"] = wanted[5].strip('"<p> | <\\/p>"')
        dict["prerequisite"] = wanted[6].strip('"')
        dict["corequisite"] = wanted[7].strip('"')
        dict["exclusion"] = wanted[8].strip('"')
        dict["recommendedPreparation"] = wanted[9].strip('"')
        dict["section"] = wanted[10].strip('"')
        dict["session"] = wanted[11].strip('"')
        dict["webTimetableInstructions"] = wanted[12].strip('"')
        dict["breadthCategories"] = wanted[13].strip('"')
        dict["distributionCategories"] = wanted[14].strip('"')
        if dict["section"] == '2017':
            dict["Course"] = (course_list[index - 1].split("},")[-1].strip('\n    "') + '20171')
        else:
            dict["Course"] = (course_list[index - 1].split("},")[-1].strip('\n    "') + '20169')
        subject_list.append(dict)
    list.append(subject_list)