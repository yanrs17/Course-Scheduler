from selenium import webdriver
import codecs

LIST_COURSE_DESIGNATOR = ['ABP', 'ABS', 'ACT', 'ANA', 'ANS', 'ANT', 'APM', 'ARH', 'AST', 'BCB', 'BCH', 'BIO', 'CAS', 'CCR', 'CDN', 'CHM', 'CIN', 'CJH', 'CJS', 'CLA', 'COG', 'COL', 'CRI', 'CSB', 'CSC', 'CTA', 'DRM', 'DTS', 'EAS', 'ECE', 'ECO', 'EDU', 'EEB', 'EHJ', 'ELL', 'ENG', 'ENV', 'ESS', 'EST', 'ETH', 'EUR', 'FAH', 'FCS', 'FIN', 'FOR', 'FRE', 'FSL', 'GER', 'GGR', 'GRK', 'HAJ', 'HIS', 'HMB', 'HPS', 'HST', 'HUN', 'IFP', 'IMC', 'IMM', 'INI', 'IRE', 'ITA', 'IVP', 'JAH', 'JAL', 'JDC', 'JEE', 'JEG', 'JEH', 'JEI', 'JFE', 'JFG', 'JFL', 'JFP', 'JFV', 'JGA', 'JGE', 'JGI', 'JGJ', 'JHA', 'JHE', 'JHN', 'JHP', 'JIA', 'JLN', 'JLP', 'JLS', 'JMB', 'JNH', 'JNS', 'JOP', 'JPA', 'JPD', 'JPE', 'JPF', 'JPH', 'JPP', 'JPR', 'JPU', 'JQR', 'JRA', 'JSC', 'JSH', 'JSU', 'JSV', 'JUG', 'JUM', 'LAS', 'LAT', 'LIN', 'LMP', 'LTE', 'MAT', 'MGR', 'MGT', 'MGY', 'MHB', 'MIJ', 'MST', 'MUN', 'MUS', 'NEW', 'NFS', 'NMC', 'NML', 'OPT', 'PCJ', 'PCL', 'PHC', 'PHL', 'PHS', 'PHY', 'PLN', 'PMU', 'POL', 'PPG', 'PRT', 'PSL', 'PSY', 'RLG', 'RSM', 'SAS', 'SDS', 'SII', 'SLA', 'SMC', 'SOC', 'SPA', 'STA', 'TBB', 'TRN', 'UNI', 'USA', 'VIC', 'WDW', 'WGS', 'XBC']

def downloadCourses(course):

    browser = webdriver.Firefox()
    browser.get('https://timetable.iit.artsci.utoronto.ca/api/courses?org=&code=' + course  + '&section=&studyyear=&daytime=&weekday=&prof=&breadth=')
    content = browser.page_source

    # if ('<pre>[]</pre>' not in content):
    f = codecs.open(course + '.html', 'w', "utf-8")
    f.write(content)
    f.close()

    browser.quit()

if __name__ == '__main__':
    for i in LIST_COURSE_DESIGNATOR:
        downloadCourses(i)
    