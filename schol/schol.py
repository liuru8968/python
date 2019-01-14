data = []
university = []
hkust = []
college = []
academy =[]
with open('schol.txt','r') as f:
    for line in f:
        data.append(line.strip())
        if '大學' in line :
            university.append(line.strip())
        if '科大' in line :
            hkust.append(line.strip())
        if '學院' in line:
            college.append(line.strip())
        if '軍官學校' in line:
            academy.append(line.strip())
print('總共有',len(university),'所大學')
print('總共有',len(hkust),'所科大大學')
print('總共有',len(college),'所學院')
print('總共有',len(academy),'所軍官校')
print('-----------------------------------------')
print('台灣總共有',len(data),'所大學')
