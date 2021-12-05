with open("C:/Users/Alexandra/Desktop/Python/Lista Clasei 11A.txt", 'rt') as f:
    linii = list(f)

n = 0
g = 0
e = 0
totalg = 0
totale = 0
total = 0
print("Nume", "Prenume", "Nota", "Limba straina", sep='\t')
for i in linii:
    campuri = i.split()
    nota = int(campuri[2])
    limba = str(campuri[3])
    n = n+1
    total = total + nota
    if limba=='Germ':
        with open("Lista Clasei 11A Germana.txt", 'a') as gr: 
            y = str(print(campuri[0],campuri[1],nota, limba, sep='\t'))
            gr.write(campuri[0])
            gr.write(' ')
            gr.write(campuri[1])
            gr.write(' ')
            gr.write(str(nota))
            gr.write('\n')
            g = g+1
            totalg = totalg + nota
    elif limba=='Eng':
        with open("Lista Clasei 11A Engleza.txt", 'a') as en:
            y = str(print(campuri[0],campuri[1], nota, limba, sep='\t'))
            en.write(campuri[0])
            en.write(' ')
            en.write(campuri[1])
            en.write(' ')
            en.write(str(nota))
            en.write('\n')
            e = e+1
            totale = totale + nota
     
print("Media clasei (", n, "studenti ) este de", total/float(n))
print("Media grupei de germana (", g, "studenti ) este de", totalg/float(g))
print("Media grupei de engleza (", e, "studenti ) este de", totale/float(e))   
