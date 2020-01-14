import random as rd 

def set_list(nb_in_list):
    my_list = []
    while(len(my_list)<nb_in_list):
        n = rd.randint(1,nb_in_list*2)
        if(n not in my_list):
            my_list.append(n)
    return my_list

def research(my_list,element):
    for i in range(len(my_list)):
        if(my_list[i] == element):
            return("the number is in the list and the index of it is " + str(i))

def recherche_dichotomique(element,my_list):
    if(element not in my_list):
        return(str(element)  + " is not in the list")
    m = len(my_list)//2
    if(my_list[m]== element):
        print("the index of you number is ")
        return m
    elif(my_list[m] > element):
        return recherche_dichotomique(element,my_list[:m])
    else:
        return m+recherche_dichotomique(element,my_list[m:])

def partition(liste,debut,fin):
    pivot = liste[fin]
    i = debut
    j = debut
    while j < fin:
        if liste[j] <= pivot:
            liste[i],liste[j] = liste[j],liste[i]
            i += 1
        j += 1
    liste[fin],liste[i] = liste[i],liste[fin]
    return i

def tri_partition_recursif(liste,debut,fin):
    if debut < fin:
        i = partition(liste,debut,fin)
        tri_partition_recursif(liste,debut,i-1)
        tri_partition_recursif(liste,i+1,fin)
    return liste

def exo2():
    my_list = set_list(50)  
    print(my_list)
    print(research(my_list,50))                            
    my_list = tri_partition_recursif(my_list,0,len(my_list)-1)
    print(my_list)
    print(recherche_dichotomique(50,my_list))

if __name__ == "__main__":
    exo2()
    input("Appuyer sur une touche pour quitter...")
    