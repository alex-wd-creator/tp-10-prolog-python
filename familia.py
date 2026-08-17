padres = {
    "zeus": "cronos", 
    "poseidon": "cronos", 
    "kratos": "zeus", 
    "calliope": "kratos", 
    "atreus": "kratos",
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

