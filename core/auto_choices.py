from .models import Opcion

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

tipo_interes = [
    {
        'etiqueta': 'Si me interesa',
        'ponderado': 1
    },
    {
        'etiqueta': 'No me interesa',
        'ponderado': '0'
    }
]


def addChoices(pregunta_instance):
    if str(pregunta_instance.tpregunta).strip() == 'linkert':
        auto_create_choices(tipo_linkert, pregunta_instance)
    if str(pregunta_instance.tpregunta).strip() == 'Si No':
        auto_create_choices(tipo_si_no, pregunta_instance)
    if str(pregunta_instance.tpregunta).strip() == 'interes':
        auto_create_choices(tipo_interes, pregunta_instance)

def auto_create_choices(tipo_pregunta, pregunta_instance):
    i = 1
    opcion_list = list()
    for opcion in tipo_pregunta:
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
