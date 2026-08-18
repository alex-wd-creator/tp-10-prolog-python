progenitores = {
    "zeus": {"cronos", "rhea"},
    "poseidon": {"cronos", "rhea"},
    "kratos": {"zeus", "callisto"},
    "calliope": {"kratos", "lysandra"},
    "atreus": {"kratos", "laufey"},
}

hijos_de = {
    "cronos": {"zeus", "poseidon"},
    "rhea": {"zeus", "poseidon"},
    "zeus": {"kratos"},
    "callisto": {"kratos"},
    "kratos": {"calliope", "atreus"},
    "lysandra": {"calliope"},
    "laufey": {"atreus"},
}


def obtener_hermanos():
    diccionario_hermanos = {}

    for persona, padres in progenitores.items():
        posibles_hermanos = set()

        for padre in padres:
            posibles_hermanos.update(hijos_de.get(padre, set()))

        hermanos_reales = posibles_hermanos - {persona}

        diccionario_hermanos[persona] = hermanos_reales

    return diccionario_hermanos


def obtener_abuelos():
    diccionario_abuelos = {}

    for persona, padres in progenitores.items():
        conjunto_abuelos = set()

        for padre in padres:
            padres_del_padre = progenitores.get(padre, set())
            conjunto_abuelos.update(padres_del_padre)

        diccionario_abuelos[persona] = conjunto_abuelos

    return diccionario_abuelos


for persona, lista_hermanos in obtener_hermanos().items():
    print(f"Hermanos de {persona}: {lista_hermanos}")

for persona, lista_abuelos in obtener_abuelos().items():
    print(f"Abuelos de {persona}: {lista_abuelos}")
