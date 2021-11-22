with open("c:/Users/Alexandra/Desktop/Python/text.txt", "w") as f:
    a = str(input("Scrieti textul pe care doriti sa-l verificati: "))
    f.write(a)

with open("c:/Users/Alexandra/Desktop/Python/text.txt", "r") as f:
    tx = f.read()
tx = list(tx)
vocale = []
for i in range(0, len(tx)):
    if (tx[i]=='a') or (tx[i]=='e') or (tx[i]=='i') or (tx[i]=='o') or (tx[i]=='u') or (tx[i]=='A') or (tx[i]=='E') or (tx[i]=='I') or (tx[i]=='O') or (tx[i]=='U'):
        vocale.append(tx[i])
vocale = str(vocale)
with open("vocale.txt", 'w') as f:
    f.write(vocale)