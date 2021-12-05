import random

def printArbre(arbre, n, position):
    """Params:
        Arbre: Un tas dans un tableau
        n: le nombre d'éléments a afficher
        position: correspond a l'indice courrant"""
    if(position < len(arbre)):
        printArbre(arbre, n+1, (2*position)+1)
        affiche_noeud(arbre, n, position)
        printArbre(arbre, n+1, 2*position)

def affiche_noeud(arbre, n, position):
    """Params:
    Arbre: Un tas dans un tableau
    n: le nombre d'éléments a afficher
    position: correspond a l'indice courrant"""
    for i in range(n):
        print("     ",end=" ")
    if(isinstance(arbre[position], int)):
        print(str(arbre[position])+" "+str(arbre[position]))
    else:
        print(arbre[position])


def minNone(a,b):
  if a is None:
    return b
  elif b is None:
    return a
  else:
    return a if a<b else b

def maxNone(a,b):
  if a is None:
    return b
  elif b is None:
    return a
  else:
    return b if a<b else a

def tabAndnbElt():
    tab= []
    nombreElt=int(input("Combien d'éléments voulez vous trier ?\n"))
    borneMin=int(input("Donnez une borne minimale pour les éléments.\n"))
    borneMax=int(input("Donnez une borne maximale pour les éléments.\n"))
    for i in range(nombreElt):
        tab.append(random.randint(borneMin,borneMax))
    return tab

def initTree(tabElt):
    tas=[None]*(2)
    tas[0]=2
    return tas
def hauteur(x):
    """Cette fonction donne la hauteur de l'arbre représenté dans un tableau
    Paramètre d'entrée: x => c'est l'indice de la position courrante où l'on est dans le tableau"""
    cpt=0
    while (x!=1):
        x=x//2
        cpt=cpt+1
    return cpt  

def swap(a,b,tab):
    interm=tab[b]
    tab[b]=tab[a]
    tab[a]=interm
def insert(tas,x):
    positionOuInserer=tas[0] #Nous avons décidé de stocker dans l'indice 0 du tableau l'entier qui correspond à l'indice où insérer x.
    positionCourante=positionOuInserer
    #insert premier elt
    tas.insert(positionOuInserer,x)
    #parcours
    haut=hauteur(positionOuInserer)
    
    if (positionOuInserer<=((2**haut)+(2**(haut+1)-1))/2): # 2**Hauteur donne le premier noeud de la ligne hauteur 2**haut+1 donne le frère
        
        while (tas[positionCourante]==minNone(tas[positionCourante],tas[positionCourante//2]) and positionCourante>3):
            #position Courante > 3 car en python les listes vont de 0 à N-1 => -1 et les deux premières cases du tableau sont reservés => -2
                # on a alors positionCourante>3 
            #swap
            swap(positionCourante,positionCourante//2,tas) #on échange le noeud courrant avec le père
            positionCourante=positionCourante//2 #position courante pointe sur le père
        if(tas[positionOuInserer]==maxNone(tas[(positionOuInserer+2**(haut-1))//2],tas[positionOuInserer]) and positionCourante>3):
            #si le noeud où inserer est le maximum entre lui meme et le père de son vis à vis
            swap(positionOuInserer,(positionOuInserer+(2**(haut-1)))//2,tas) # on échange les noeuds
            positionCourante=(positionOuInserer+(2**(haut-1)))//2 #position courrante devient alors le dit-père
            while (tas[positionCourante]==maxNone(tas[positionCourante],tas[positionCourante//2])and positionCourante>3):#tant que le noeud courrant est plus grand que son fils
              #swap
              swap(positionCourante,positionCourante//2,tas)#on échange
              positionCourante=positionCourante//2 #le noeud courrant devient le fils
    else:
        while (tas[positionCourante]==maxNone(tas[positionCourante],tas[positionCourante//2]) and positionCourante>3):
            swap(positionCourante,positionCourante//2,tas)
            positionCourante=positionCourante//2
        if(tas[positionOuInserer]==minNone(tas[(positionOuInserer-2**(haut-1))],tas[positionOuInserer]) and positionCourante>3):
            swap(positionOuInserer,positionOuInserer-(2**(haut-1)),tas)
            positionCourante=positionOuInserer-(2**(haut-1))
            while (tas[positionCourante]==minNone(tas[positionCourante],tas[positionCourante//2])and positionCourante>3):
              #swap
              swap(positionCourante,positionCourante//2,tas)
              positionCourante=positionCourante//2
    tas[0]=tas[0]+1  #on incrémente alors la position où insérer         
    return tas
    

def main():
    tabElt=tabAndnbElt()
    print(tabElt)
    tas=initTree(tabElt)
    while(tabElt):
        insert(tas,tabElt.pop(0))
        print("---------------------------------------------")
        printArbre(tas,len(tas),1)
        print("---------------------------------------------")
    print(tas)
if __name__=='__main__':
    main()