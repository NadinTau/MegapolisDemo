import random

def readFile(filename):
    f = open(filename, 'r', encoding = 'utf-8')
    students=[]
    for i in range(501):
        d1,d2,d3,d4,d5=f.readline().strip().split(',')
        students.append([d1,d2,d3,d4,d5]) 
    return students

def writeFile(filename):
    fn=open(filename,'w', encoding = 'utf-8')
    fn.write(students[0][0]+','+students[0][1]+','+\
            students[0][2]+','+students[0][3]+','+students[0][4]+','+','+'\n') # заголовок таблицы
    for i in range(1,501):
        fn.write(students[i][0]+','+students[i][1]+','+\
        students[i][2]+','+students[i][3]+','+students[i][4]+','\
        +generate_login(i)+','+generate_password(8)+'\n')
    fn.close()

def generate_login(n):
    '''Генератор логина для ученика
на вход подается порядковый номер ученика в списке
выход - сгенерированный логин по образцу Фамилия_ИО
'''
    fio=students[n][1].split()
    login = fio[0]+'_'+fio[1][0]+fio[2][0]
    return login

def generate_password(length):
    '''Генератор пароля для ученика
на вход подается длина пароля
выход - сгенерированный пароль
'''
    # список разрешенных символов
    characters = 'QWERTYUIOPLKJHGFDSAZXCVBNMmnbvcxzasdfghjklpoiuytrewq1234567890'
    #сборка пароля с помощью join и цикла
    password = ''.join(random.choice(characters) for _ in range(length)) 
    if any(x in '0123456789' for x in password) and \
       any(x in 'qwertyuioplkjhgfdsazxcvbnm' for x in password) and\
       any(x in 'QWERTYUIOPLKJHGFDSAZXCVBNM' for x in password):
        return password
    else: return generate_password(length) 

students = readFile("students.csv")
writeFile("students_password.csv")
