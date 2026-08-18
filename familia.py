padres = {
    "zeus": "cronos",  
    "kratos": "zeus", 
    "atreus": "kratos",
     
    "poseidon": "cronos",
    }

madres = {
    "zeus": "rhea", 
    "kratos": "callisto", 
    "calliope": "lysandra", 
    "atreus": "laufey",
    }

def hermanos():
    hermanos = {}
    for hijo in padres:
        padre = padres[hijo]
        madre = madres.get(hijo)
        if padre and madre:

            hermanos[hijo] = [h for h in padres if padres[h] == padre or madres.get(h) == madre and h != hijo]
            for h in hermanos[hijo]:
                if h == hijo:
                    hermanos[hijo].remove(h)
            print(f"Hermanos de {hijo}: {hermanos[hijo]}")
    return hermanos

# abuelos: cronos y zeus
# orden: cronos-zeus-kratos-atreus (por ejemplo)
# primero deberia obtener los hijos e ir escalando para conseguir el padre del padre

def abuelos():
    abuelos = {}
    
    for hijo in padres:
        abuelo = padres.get("zeus")
        padre = padres[hijo]
        nieto = hijo

        abuelos[nieto] = [abuelo]
        print(abuelos)
    return abuelos

            
abuelos()
