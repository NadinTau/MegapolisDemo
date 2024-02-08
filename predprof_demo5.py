def readFile(filename):
    f = open(filename, 'r', encoding = 'utf-8')
    global z1,z2,z3,z4,z5
    z1,z2,z3,z4,z5=f.readline().strip().split(',')
    tab=[]
    for i in range(500):
        d1,d2,d3,d4,d5=f.readline().strip().split(',')
        tab.append([d1,d2,d3,d4,d5]) 
    return tab

def generate_hash(s):
    alphabet = [chr(i) for i in range(1040, 1104)]
    alphabet.append(' ')
    alphabet.append('ё')
    d = {letter: i for i, letter in enumerate(alphabet,1)}
    p = 67
    m = 10**9 + 9
    hash_value = 0
    p_pow = 1
    for c in s:
        hash_value = (hash_value + d[c] * p_pow) % m
        p_pow = (p_pow * p) 
    return int(hash_value)
print(generate_hash('Пванов Иван'))

def writeFile(filename, students):
    fn=open(filename,'w', encoding = 'utf-8')
    fn.write(z1+','+z2+','+z3+','+z4+','+z5+'\n') # заголовок таблицы
    for i in range(500):
        fn.write(str(generate_hash(students[i][1]))+','+students[i][1]+','+\
            students[i][2]+','+students[i][3]+','+students[i][4]+'\n')
    fn.close()

students = readFile("students.csv")
writeFile("students_with_hash.csv", students)

