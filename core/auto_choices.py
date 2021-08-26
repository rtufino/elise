from .models import Opcion


def addChoices(pregunta_instance):
    if str(pregunta_instance.tpregunta).strip() == 'linkert':
        linkert(pregunta_instance)
    if str(pregunta_instance.tpregunta).strip() == 'Si No':
        si_no(pregunta_instance)


tipo_linkert = [
    {
        "etiqueta": "Totalmente deacuerdo",
        "ponderado": 5,
    },
    {
        "etiqueta": "Deacuerdo",
        "ponderado": 4,
    },
    {
        "etiqueta": "Ni deacuerdo, ni desacuerdo",
        "ponderado": 3,
    },
    {
        "etiqueta": "Desacuerdo",
        "ponderado": 2,
    },
    {
        "etiqueta": "Totalmente desacuerdo",
        "ponderado": 1,
    }
]

tipo_si_no = [
    {
        'etiqueta': 'Si',
        'ponderado': 1
    },
    {
        'etiqueta': 'No',
        'ponderado': 0
    }
]


def linkert(pregunta_instance):
    i = 1
    opcion_list = list()
    for opcion in tipo_linkert:
        opcion_list.append(
            Opcion(
                pregunta=pregunta_instance,
                numero=i,
                ponderado=opcion["ponderado"],
                etiqueta=opcion["etiqueta"]
            )
        )
        i += 1
    Opcion.objects.bulk_create(opcion_list)


def si_no(pregunta_instance):
    i = 1
    opcion_list = list()
    for opcion in tipo_si_no:
        opcion_list.append(
            Opcion(
                pregunta=pregunta_instance,
                numero=i,
                ponderado=opcion["ponderado"],
                etiqueta=opcion["etiqueta"]
            )
        )
        i+=1
    Opcion.objects.bulk_create(opcion_list)
