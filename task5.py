def readfile(namefile):
    '''
    Read file and create list of students
    :param namefile: str, name file
    :return: list of students
    '''
    f=open(namefile,'r',encoding='utf-8')
    students=[]
    for i in range(501):
        students.append(f.readline().strip().split(','))
    return students

def hash(fio):
    '''
    Generate hash-key for student
    :param fio: str, name student
    :return: int, hash-key
    '''
    h=0
    st=0
    liter = '*ёйцукенгшщзхъэждлорпавыфячсмитьбю ЁЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ'
    p = 67
    m = 10 ** 9 + 9
    for x in fio:
        h+=(liter.index(x)*p**st)%m
        st+=1
    return h

def writefile(name):
    '''
    Write new file with hash-key
    :param name: str, name file
    '''
    f = open(name, 'w', encoding='utf-8')
    f.write(','.join(students[0])+'\n')
    for i in range(1,501):
        students[i][0]=str(hash(students[i][1]))
        f.write(','.join(students[i]) + '\n')
    f.close()


students=readfile('/home/teacher/Загрузки/students.csv')
writefile('/home/teacher/Загрузки/students_with_hash.csv')

