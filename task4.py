import random
def readfile(namefile):
    '''
    Read file and create list of students
    :param namefile: str, name file
    :return: list of students
    '''
    f = open(namefile, 'r', encoding='utf-8')
    students = []
    for i in range(501):
        students.append(f.readline().strip().split(','))
    return students


def generateLogin(fio):
    '''
    Generate login for student Familia_IO"
    :param fio: str, name students
    :return: str, login
    '''
    f,i,o=fio.split()
    return f+'_'+i[0]+o[0]

def generatePassword(l):
    s='QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm1234567890'
    password=''.join(random.choice(s) for _ in range(l))
    if any(x in 'QWERTYUIOPLKJHGFDSAZXCVBNM' for x in password) and \
            any(x in 'qwertyuioplkjhgfdsazxcvbnm' for x in password) and \
            any(x in '1234567890' for x in password):
        return password
    else: return generatePassword(l)


def writefile(name):
    '''
    Write new file with hash-key
    :param name: str, name file
    '''
    f = open(name, 'w', encoding='utf-8')
    f.write(','.join(students[0]) + '\n')
    for i in range(1, 501):
        students[i].append(generateLogin(students[i][1]))
        students[i].append(generatePassword(8))
        f.write(','.join(students[i])+'\n')
    f.close()


students = readfile('/home/teacher/Загрузки/students.csv')
writefile('/home/teacher/Загрузки/students_password.csv')