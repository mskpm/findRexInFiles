import re, os

def findExtFiles(ext='txt', path='.'):
    """Funkcja wyszukuje pliki z rozszerzeniem ext i zwraca \
    listę plików"""
    files = []
    for filename in os.listdir(path):
        if filename.endswith('.'+ ext):
            files.append(filename)
    return files

def findRegxInword(regx, line):
    """Funkcja wyszukuje linię z wyrazem zawierającym regx i zwraca \
    listę wyrazów"""
    words=line.split()
    result=[]
    pattern = re.compile(f'{regx}')
    for word in words:
        if pattern.findall(word):
            result.append(word)
    return result

def findRegxInLine(regx, line):
    """Funkcja sprawdza linię czy wyraz w linii zawiera regx i zwraca \
    TRUE lub FALSE"""
    pattern = re.compile(f'{regx}')
    if pattern.findall(line):
        return True
    return False

line = 'To jest testowa linia tekstu tete alteto.'

path='C:/Users/majkowsp/Documents/SQL scripts'
regx = 'v_var'
ext = 'sql'
extFiles = findExtFiles(ext, path)

def findRegxLinesinFiles(regx, path='.', ext='txt'):
    """Funkcja szuka plikach z rozszerzeniem ext i \
    wypisuje linię zawierającą regx"""
    extFiles = findExtFiles(ext, path)
    for file in extFiles:
        n=0
        with open(path+'/'+file,'r') as fp:
            print(file+':\n')
            lines = fp.readlines()
            for line in lines:
                n+=1
                if findRegxInLine(regx, line):
                    print(str(n)+':\t'+line)
        
path = str(input('Podaj ścieżkę: '))
ext = str(input('Podaj rozszerzenie plików: '))
extFiles = findExtFiles('sql', path)
regx = str(input('Podaj regx: '))

findRegxLinesinFiles(regx,path)

