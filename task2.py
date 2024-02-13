def readfile(namefile):
    '''
    Read file and create list of students
    :param namefile: str, name file
    :return: list of students
    '''
    f=open(namefile,'r',encoding='utf-8')
    f.readline()
    students=[]
    for i in range(500):
        students.append(f.readline().strip().split(','))
    return students

def sortdown(students):
    '''
    Поиск данных по учащемуся и вывод на экран
    :param family: фамилия, str
    :param name: имя, str
    :return: -
    '''
    for i in range(500):
        j=i
        while j>0 and students[j][4]>students[j-1][4]:
            students[j],students[j-1]=students[j-1],students[j]
            j=j-1
    return students



students=readfile('/home/teacher/Загрузки/students.csv')
students=sortdown(students)
n=1
for i in range(500):
    if '10' in students[i][3]:
        f,i,o=students[i][1].split()
        print(f'{n} место: {i[0]}.{f}')
        n+=1
    if n==4: break
