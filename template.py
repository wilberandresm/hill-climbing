import string, math
def distancesFromCoords():
    f = open('berlin52.tsp') 
    data = [line.replace("\n","").split(" ")[1:] for line in f.readlines()[6:58]]# lee el data set y lo guard aen data
    coords =  list(map(lambda x: [float(x[0]),float(x[1])], data)) #crea una lista del mapeado del data, obteniendo las coordenadas
    distances = []#lista para almacenar las distancias
    for i in range(len(coords)):
        row = [] 
        for j in range(len(coords)):
            row.append(math.sqrt((coords[i][0]-coords[j][0])**2 + (coords[i][1]-coords[j][1])**2))#raid de la distancia anterior con la siguiente
        distances.append(row) 
    return distances

