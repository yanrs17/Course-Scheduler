from bs4 import BeautifulSoup
import ast, re

html_doc = """
<html xmlns="http://www.w3.org/1999/xhtml"><head><link title="長い行を折り返す" href="resource://gre-resources/plaintext.css" type="text/css" rel="alternate stylesheet" /></head><body><pre>{
    "ANA300Y1-Y-20169": {
        "org": "ANA",
        "orgName": "Anatomy (ANA)",
        "courseTitle": "Human Anatomy and Histology",
        "code": "ANA300Y1",
        "courseDescription": "&lt;p&gt;Structure of the human body and its relationship to function. Basic Human&amp;nbsp; Histology, Gross Anatomy, and Neuroanatomy.&lt;\/p&gt;",
        "prerequisite": "BIO130H1",
        "corequisite": "",
        "exclusion": "ANA126Y1",
        "recommendedPreparation": "",
        "section": "Y",
        "session": "20169",
        "webTimetableInstructions": null,
        "breadthCategories": "Living Things and Their Environment (4)",
        "distributionCategories": "Science",
        "meetings": {
            "LEC-0101": {
                "schedule": {
                    "MO-35575": {
                        "meetingScheduleId": "35575",
                        "meetingDay": "MO",
                        "meetingStartTime": "09:00",
                        "meetingEndTime": "10:00"
                    },
                    "TU-35576": {
                        "meetingScheduleId": "35576",
                        "meetingDay": "TU",
                        "meetingStartTime": "09:00",
                        "meetingEndTime": "10:00"
                    },
                    "FR-35574": {
                        "meetingScheduleId": "35574",
                        "meetingDay": "FR",
                        "meetingStartTime": "10:00",
                        "meetingEndTime": "12:00"
                    }
                },
                "instructors": {
                    "17595": {
                        "instructorId": "17595",
                        "firstName": "B.",
                        "lastName": "Ballyk"
                    }
                },
                "teachingMethod": "LEC",
                "sectionNumber": "0101",
                "subtitle": "",
                "cancel": "",
                "waitlist": "Y",
                "online": "",
                "enrollmentCapacity": "400",
                "enrollmentIndicator": "P",
                "meetingStatusNotes": "",
                "enrollmentControls": [
                    {
                        "postId": "362",
                        "postCode": "ASSPE2082",
                        "postName": "SP PHARMACOLOGY",
                        "subjectId": "1",
                        "subjectCode": "*",
                        "subjectName": "",
                        "designationId": "1",
                        "designationCode": "*",
                        "designationName": "",
                        "yearOfStudy": "3",
                        "typeOfProgramId": "1",
                        "typeOfProgramCode": "*",
                        "typeOfProgramName": "All Types",
                        "primaryOrgId": "1",
                        "primaryOrgCode": "*",
                        "primaryOrgName": "",
                        "secondaryOrgId": "1",
                        "secondaryOrgCode": "*",
                        "secondaryOrgName": "",
                        "assocOrgId": "1",
                        "assocOrgCode": "*",
                        "assocOrgName": "",
                        "adminOrgId": "1",
                        "adminOrgCode": "*",
                        "adminOrgName": ""
                    },
                    {
                        "postId": "362",
                        "postCode": "ASSPE2082",
                        "postName": "SP PHARMACOLOGY",
                        "subjectId": "1",
                        "subjectCode": "*",
                        "subjectName": "",
                        "designationId": "1",
                        "designationCode": "*",
                        "designationName": "",
                        "yearOfStudy": "4",
                        "typeOfProgramId": "1",
                        "typeOfProgramCode": "*",
                        "typeOfProgramName": "All Types",
                        "primaryOrgId": "1",
                        "primaryOrgCode": "*",
                        "primaryOrgName": "",
                        "secondaryOrgId": "1",
                        "secondaryOrgCode": "*",
                        "secondaryOrgName": "",
                        "assocOrgId": "1",
                        "assocOrgCode": "*",
                        "assocOrgName": "",
                        "adminOrgId": "1",
                        "adminOrgCode": "*",
                        "adminOrgName": ""
                    },
                    {
                        "postId": "369",
                        "postCode": "ASSPE2340",
                        "postName": "SP PHARM &amp; BIOMED TOXICOLOGY",
                        "subjectId": "1",
                        "subjectCode": "*",
                        "subjectName": "",
                        "designationId": "1",
                        "designationCode": "*",
                        "designationName": "",
                        "yearOfStudy": "3",
                        "typeOfProgramId": "1",
                        "typeOfProgramCode": "*",
                        "typeOfProgramName": "All Types",
                        "primaryOrgId": "1",
                        "primaryOrgCode": "*",
                        "primaryOrgName": "",
                        "secondaryOrgId": "1",
                        "secondaryOrgCode": "*",
                        "secondaryOrgName": "",
                        "assocOrgId": "1",
                        "assocOrgCode": "*",
                        "assocOrgName": "",
                        "adminOrgId": "1",
                        "adminOrgCode": "*",
                        "adminOrgName": ""
                    },
                    {
                        "postId": "369",
                        "postCode": "ASSPE2340",
                        "postName": "SP PHARM &amp; BIOMED TOXICOLOGY",
                        "subjectId": "1",
                        "subjectCode": "*",
                        "subjectName": "",
                        "designationId": "1",
                        "designationCode": "*",
                        "designationName": "",
                        "yearOfStudy": "4",
                        "typeOfProgramId": "1",
                        "typeOfProgramCode": "*",
                        "typeOfProgramName": "All Types",
                        "primaryOrgId": "1",
                        "primaryOrgCode": "*",
                        "primaryOrgName": "",
                        "secondaryOrgId": "1",
                        "secondaryOrgCode": "*",
                        "secondaryOrgName": "",
                        "assocOrgId": "1",
                        "assocOrgCode": "*",
                        "assocOrgName": "",
                        "adminOrgId": "1",
                        "adminOrgCode": "*",
                        "adminOrgName": ""
                    },
                    {
                        "postId": "378",
                        "postCode": "ASSPE2573",
                        "postName": "SP BIOMEDICAL TOXICOLOGY",
                        "subjectId": "1",
                        "subjectCode": "*",
                        "subjectName": "",
                        "designationId": "1",
                        "designationCode": "*",
                        "designationName": "",
                        "yearOfStudy": "3",
                        "typeOfProgramId": "1",
                        "typeOfProgramCode": "*",
                        "typeOfProgramName": "All Types",
                        "primaryOrgId": "1",
                        "primaryOrgCode": "*",
                        "primaryOrgName": "",
                        "secondaryOrgId": "1",
                        "secondaryOrgCode": "*",
                        "secondaryOrgName": "",
                        "assocOrgId": "1",
                        "assocOrgCode": "*",
                        "assocOrgName": "",
                        "adminOrgId": "1",
                        "adminOrgCode": "*",
                        "adminOrgName": ""
                    },
                    {
                        "postId": "378",
                        "postCode": "ASSPE2573",
                        "postName": "SP BIOMEDICAL TOXICOLOGY",
                        "subjectId": "1",
                        "subjectCode": "*",
                        "subjectName": "",
                        "designationId": "1",
                        "designationCode": "*",
                        "designationName": "",
                        "yearOfStudy": "4",
                        "typeOfProgramId": "1",
                        "typeOfProgramCode": "*",
                        "typeOfProgramName": "All Types",
                        "primaryOrgId": "1",
                        "primaryOrgCode": "*",
                        "primaryOrgName": "",
                        "secondaryOrgId": "1",
                        "secondaryOrgCode": "*",
                        "secondaryOrgName": "",
                        "assocOrgId": "1",
                        "assocOrgCode": "*",
                        "assocOrgName": "",
                        "adminOrgId": "1",
                        "adminOrgCode": "*",
                        "adminOrgName": ""
                    },
                    {
                        "postId": "382",
                        "postCode": "ASSPE2675",
                        "postName": "SP PHARM &amp; BIOMED TOX(GENERAL)",
                        "subjectId": "1",
                        "subjectCode": "*",
                        "subjectName": "",
                        "designationId": "1",
                        "designationCode": "*",
                        "designationName": "",
                        "yearOfStudy": "3",
                        "typeOfProgramId": "1",
                        "typeOfProgramCode": "*",
                        "typeOfProgramName": "All Types",
                        "primaryOrgId": "1",
                        "primaryOrgCode": "*",
                        "primaryOrgName": "",
                        "secondaryOrgId": "1",
                        "secondaryOrgCode": "*",
                        "secondaryOrgName": "",
                        "assocOrgId": "1",
                        "assocOrgCode": "*",
                        "assocOrgName": "",
                        "adminOrgId": "1",
                        "adminOrgCode": "*",
                        "adminOrgName": ""
                    },
                    {
                        "postId": "382",
                        "postCode": "ASSPE2675",
                        "postName": "SP PHARM &amp; BIOMED TOX(GENERAL)",
                        "subjectId": "1",
                        "subjectCode": "*",
                        "subjectName": "",
                        "designationId": "1",
                        "designationCode": "*",
                        "designationName": "",
                        "yearOfStudy": "4",
                        "typeOfProgramId": "1",
                        "typeOfProgramCode": "*",
                        "typeOfProgramName": "All Types",
                        "primaryOrgId": "1",
                        "primaryOrgCode": "*",
                        "primaryOrgName": "",
                        "secondaryOrgId": "1",
                        "secondaryOrgCode": "*",
                        "secondaryOrgName": "",
                        "assocOrgId": "1",
                        "assocOrgCode": "*",
                        "assocOrgName": "",
                        "adminOrgId": "1",
                        "adminOrgCode": "*",
                        "adminOrgName": ""
                    }
                ]
            }
        }
    },
    "ANA301H1-S-20171": {
        "org": "ANA",
        "orgName": "Anatomy (ANA)",
        "courseTitle": "Human Embryology",
        "code": "ANA301H1",
        "courseDescription": "&lt;p&gt;Human embryology from fertilization to the end of the fetal period. Current concepts in mammalian morphogenesis applied to the development of the various organ systems; etiologies and pathogenesis of some of the more common human congenital abnormalities.&lt;\/p&gt;",
        "prerequisite": "BIO130H1",
        "corequisite": "",
        "exclusion": "",
        "recommendedPreparation": "",
        "section": "S",
        "session": "20171",
        "webTimetableInstructions": null,
        "breadthCategories": "Living Things and Their Environment (4)",
        "distributionCategories": "Science",
        "meetings": {
            "LEC-0101": {
                "schedule": {
                    "MO-30149": {
                        "meetingScheduleId": "30149",
                        "meetingDay": "MO",
                        "meetingStartTime": "13:00",
                        "meetingEndTime": "15:00"
                    },
                    "FR-30148": {
                        "meetingScheduleId": "30148",
                        "meetingDay": "FR",
                        "meetingStartTime": "13:00",
                        "meetingEndTime": "15:00"
                    }
                },
                "instructors": {
                    "15352": {
                        "instructorId": "15352",
                        "firstName": "M.",
                        "lastName": "Bidmos"
                    }
                },
                "teachingMethod": "LEC",
                "sectionNumber": "0101",
                "subtitle": "",
                "cancel": "",
                "waitlist": "Y",
                "online": "",
                "enrollmentCapacity": "500",
                "enrollmentIndicator": null,
                "meetingStatusNotes": "",
                "enrollmentControls": []
            }
        }
    },
    "ANA400H1-S-20171": {
        "org": "ANA",
        "orgName": "Anatomy (ANA)",
        "courseTitle": "Anatomy Dissection",
        "code": "ANA400H1",
        "courseDescription": "&lt;p&gt;A focussed series of Anatomical dissections will be made and the surgical implications of the findings will be the subject of seminars.&amp;nbsp; Attitudes to dissection of the human body, complications of surgery and other relevant issues will be discussed.&lt;\/p&gt;",
        "prerequisite": "ANA300Y1 and  permission of department.  Normally a B+ standing will be required",
        "corequisite": "",
        "exclusion": "",
        "recommendedPreparation": "",
        "section": "S",
        "session": "20171",
        "webTimetableInstructions": "To enrol in this course, please contact Beblan Soorae, the Undergraduate Administrative Officer, at b.soorae@utoronto.ca",
        "breadthCategories": "Living Things and Their Environment (4)",
        "distributionCategories": "Science",
        "meetings": {
            "LEC-0101": {
                "schedule": {
                    "TU-30151": {
                        "meetingScheduleId": "30151",
                        "meetingDay": "TU",
                        "meetingStartTime": "13:00",
                        "meetingEndTime": "15:00"
                    },
                    "TH-30150": {
                        "meetingScheduleId": "30150",
                        "meetingDay": "TH",
                        "meetingStartTime": "13:00",
                        "meetingEndTime": "15:00"
                    }
                },
                "instructors": {
                    "15353": {
                        "instructorId": "15353",
                        "firstName": "M.",
                        "lastName": "Bidmos"
                    }
                },
                "teachingMethod": "LEC",
                "sectionNumber": "0101",
                "subtitle": "",
                "cancel": "",
                "waitlist": "N",
                "online": "",
                "enrollmentCapacity": "9999",
                "enrollmentIndicator": "E",
                "meetingStatusNotes": "",
                "enrollmentControls": []
            }
        }
    },
    "ANA498Y1-Y-20169": {
        "org": "ANA",
        "orgName": "Anatomy (ANA)",
        "courseTitle": "Project in Anatomy",
        "code": "ANA498Y1",
        "courseDescription": "&lt;p&gt;A research project in Histology, Cellular or Molecular Biology, Developmental Biology, Neuroanatomy or Gross Anatomy. Not eligible for CR\/NCR option.&lt;\/p&gt;",
        "prerequisite": "Permission of a professor to supervise the project",
        "corequisite": "",
        "exclusion": "",
        "recommendedPreparation": "",
        "section": "Y",
        "session": "20169",
        "webTimetableInstructions": "To enrol in this course, please contact Beblan Soorae, the Undergraduate Administrative Officer, at b.soorae@utoronto.ca",
        "breadthCategories": "Living Things and Their Environment (4)",
        "distributionCategories": "Science",
        "meetings": {
            "LEC-0101": {
                "schedule": {
                    "-": {
                        "meetingScheduleId": null,
                        "meetingDay": null,
                        "meetingStartTime": null,
                        "meetingEndTime": null
                    }
                },
                "instructors": {
                    "15355": {
                        "instructorId": "15355",
                        "firstName": "H.",
                        "lastName": "Sun"
                    }
                },
                "teachingMethod": "LEC",
                "sectionNumber": "0101",
                "subtitle": "",
                "cancel": "",
                "waitlist": "N",
                "online": "",
                "enrollmentCapacity": "9999",
                "enrollmentIndicator": "E",
                "meetingStatusNotes": "",
                "enrollmentControls": []
            }
        }
    }
}</pre></body></html>
"""
#html_doc = re.sub(r'["]\s*["]', '"', html_doc)


soup = BeautifulSoup(html_doc)
result = soup.pre.string
#re.sub('["]\s*["]', '"', result)
result = result.replace("\n", '').replace("null", "\"\"")


"""
start, value, last = re.match(r'(\s*{\s*".*?"\s*:\s*")(.*)("\s*})', result).groups()
fixed = value.replace('"', "") # remove quotes
#fixed = value.replace("\\\"", "")
d = (start + fixed + last + "}")

#print(d)
dict_d = ast.literal_eval(d)
print(dict_d)
"""

print(ast.literal_eval(result))

morgan = ast.literal_eval(result)