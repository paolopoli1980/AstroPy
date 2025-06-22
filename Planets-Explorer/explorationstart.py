from planetcalculation import calculation


listdata=[]
listdata2=[]
with open("dataplanets.dat", "r") as file:
    for riga in file:
        listdata.append(riga)


for elementi in listdata:
    listdata2.append(elementi.split(','))
#print(listdata2[0])
word='a'
while word!='e':
    for i,elementi in enumerate(listdata2):
        print(i,'t*,              tp,           e,                axisangle,        majax,        rplanet,    density planet,      albedo')

        for el in elementi:
            print(el[:-5]+' , ',end='')
        if (i+1)%20==0:
            input()
        print()

    word=input('Insert the planet you want to explore =')
    try:
        if 0<=int(word)<len(listdata2):
        #    print('ok')
        #input()
            calculation(float(listdata2[int(word)][0]),float(listdata2[int(word)][1]),float(listdata2[int(word)][2]),float(listdata2[int(word)][3]),float(listdata2[int(word)][4]),float(listdata2[int(word)][5]),float(listdata2[int(word)][6]),float(listdata2[int(word)][7]))
    except:
        pass
    
print (float(listdata2[0][4]))
