fin=open("date.txt", 'r')   #am deschis fisierul din care citesc
lista=[int(element) for element in fin.readline().split()]  #am citit prima linie din fisier
n=lista[0]  #n
m=lista[1]  #m
contor=1 #am initializat contorul cu 1 astfel incat sa citesc excat m muchii din fisier
muchii=[]   #lista pentru muchii
cuvinte=[]  #lista pentru cuvinte
stare_initiala=0    #starea initiala
nr_stari_finale=0   #numarul starilor finale
stare_finala=0  #starea finala
nr_cuvinte=0    #numarul cuvintelor
for linie in fin.readlines():   #citirea elementelor
    if contor <= m: #daca contor <= m =>ca sunt muchii
        linie=linie.split()
        stanga=int(linie[0])
        dreapta=int(linie[1])
        litera=linie[2]
        muchii.append([stanga, dreapta, litera])
        contor+=1
    elif contor==m+1:   #daca contor==m+1 =>starea initiala
        contor+=1
        linie=linie.split()
        stare_initiala=int(linie[0])
    elif contor==m+2:   #daca contor==m+2 =>numarul starilor finale
        contor+=1
        linie=linie.split()
        nr_stari_finale=int(linie[0])
        stare_finala=int(linie[1])
    elif contor==m+3:   #daca contor==m+1 =>numarul cuvintelor
        contor+=1
        linie=linie.split()
        nr_cuvinte=int(linie[0])
    else:
        linie=linie.split() #altfel =>cuvintele
        cuvinte.append(linie)
for cuv in cuvinte: #parcurgem lista cuvintelor
    drum=[] #initializam lista in care vom adauga drumul cu [] pentru fiecare cuvant
    cuvant=cuv[0]
    i=0 #index pentru parcurgerea listei de muchii
    lungime=0   #va avea in final lungimea totala a cuvantului
    for litera in cuvant:   #parcurgem literele din cuvant
        ok=0    #initializam ok=0 in sensul in care in momentul in care imi gaseste in lista de muchii prima aparitie a literei sa retina nodurile 
        j=0
        while ok==0 and i<len(muchii):  #cat timp n-am gasit litera si nu am ajuns la finalul parcurgerii listei cu muchii
            if muchii[i][2]!=litera:    #daca sunt diferite crestem indexul de parcurgere => nu o sa am o bucla
                i+=1
            else:
                ok=1    #altfel am gasit litera
                if litera in cuvant[lungime+1:]:    #daca gasesc litera de la pozitia ei +1 => pun in drum nodurile respective
                    drum.append([muchii[i][0], muchii[i][1]])
                else:   #altfel litera nu se mai gaseste
                    if muchii[i][0]==muchii[i][1]:      #daca muchiile sunt egale => fortez sa nu imi mai intre in recurenta => imi trebuie doua noduri diferite
                        j=i+1   #plec cu un j de la i+1
                        while j<len(muchii):    #cat timp nu am terminat de parcurs elementele din muchii
                            if  muchii[i][1]== muchii[j][0] and muchii[j][0]!=muchii[j][1] and muchii[j][2]==litera:
                            #conditii: daca este o continuare(nod final=cel initial) si perechea de noduri este formata din doua noduri diferite si litera din tuplul de muchii == litera     
                                drum.append([muchii[j][0], muchii[j][1]])
                            j+=1        #cresc j   
                    else:
                        drum.append([muchii[i][0], muchii[i][1]])   #altfel pun drumul intrucat inseamna ca perechea de noduri este diferita si corespunde cerintelor
        lungime+=1  #cresc lungimea
    if drum[len(drum)-1][1]==stare_finala:  #daca cel mai din dreapta nod este egal cu cel final => am gasit un traseu complet; afisez da si drumul
        print('DA')
        print(stare_initiala, end=" ")  #afisez starea initiala
        i=0 #plec cu un i=0
        while i<len(drum)-1:    #parcurg lista cu drumuri pana la len(drum)-1
            if drum[i][0]==drum[i][1]:  #daca cele doua extremitati sunt egale => afisez numai una dintre ele
                print(drum[i][1], end=" ")
                if drum[i+1][0]!=drum[i+1][1] and drum[i][1]==drum[i+1][0]:
                #verific daca urmatoarea pereche dupa cea cu extremitatile egale este diferita => daca e diferita trebuie sa afisez ambele extremitati pentru ca ies din recurenta
                    print(drum[i+1][0], drum[i+1][1], end=" ")  
                    i+=1    #cresc i-ul ca sa trec peste perechea respectiva
            elif drum[i][1]==drum[i+1][0]:  #altfel daca extremitatea dreapta de la perechea curenta == cea stanga de la perechea urmatoare => afisez numai una din ele
                print(drum[i][1], end=" ")
            i+=1    #incrementez
        print(stare_finala) #afisez starea finala
        print()
    else:   #altfel => nu corespunde cerintelor => cuvantul nu este acceptat
        print("NU")   
        print()
        