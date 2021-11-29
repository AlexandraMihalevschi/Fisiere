with open("Lista Clasei 11A.txt", 'rt') as f:
    linii = list(f)

n = 0
total = 0
for i in linii:
    campuri = i.split()
    nota = int(campuri[2])
    n = n+1
    total = total + nota

print("Media clasei (", n, "de studenti ) este de", total/n)
n, total = 0
for i in linii:
    c = i.split()
    nota1 = int(c[4])
    n = n+1
    total = total + nota1