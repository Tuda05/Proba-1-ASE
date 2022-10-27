# Deschidem fisierul
lista_produse = open("produse.txt", "r")

# Creez un nested list in care bag informatiile fiecarui produs
array_mare = []
for row in lista_produse.readlines():
    array_lista_produse = []
    row = row.strip() # Scoate elementele nevrute din lista
    for elm in row.split(", "):
        array_lista_produse.append(elm)
    array_mare.append(array_lista_produse)

# Sortez prin magie ceva, criteriile sunt in dreapta
array_mare = sorted(array_mare, key = lambda x: (x[1], -float(x[3]), (x[2])))

# Deschid celalalt fisier
lista_produse = open("produse_ordonate.txt", "w")

# Scriu in fisier
for i in array_mare:
    for j in range(len(i) - 1):
        lista_produse.write(str(i[j]) + ", ")
    lista_produse.write(str(i[j + 1]) + "\n")

'''

    Asa nu! Gasesti pe net mai multe lol :)))

# Sortez alfabetic dupa categorie
for a in range(len(array_mare)):
    n = len(array_mare)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if array_mare[j][1] > array_mare[j + 1][1]:
                array_mare[j], array_mare[j + 1] = array_mare[j + 1], array_mare[j]

# Sortez descrescator dupa rating
for a in range(len(array_mare)):
    n = len(array_mare)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if array_mare[j][1] == array_mare[j + 1][1]:
                if array_mare[j][3] < array_mare[j + 1][3]:
                    array_mare[j], array_mare[j + 1] = array_mare[j + 1], array_mare[j]

# Sortez crescator dupa pret
for a in range(len(array_mare)):
    n = len(array_mare)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if array_mare[j][3] == array_mare[j + 1][3]:
                if array_mare[j][2] > array_mare[j + 1][2]:
                    array_mare[j], array_mare[j + 1] = array_mare[j + 1], array_mare[j]

print(array_name)
'''
