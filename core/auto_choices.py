from .models import Opcion

tipo_linkert = [
    {
        "etiqueta": "Totalmente de Acuerdo",
        "ponderado": 5,
    },
    {
        "etiqueta": "De Acuerdo",
        "ponderado": 4,
    },
    {
        "etiqueta": "Ni de Acuerdo, Ni en Desacuerdo",
        "ponderado": 3,
    },
    {
        "etiqueta": "En Desacuerdo",
        "ponderado": 2,
    },
    {
        "etiqueta": "Totalmente en Desacuerdo",
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

tipo_abierta = [
    {
        'etiqueta': 'abierta',
        'ponderado': 1
    }
]
def addChoices(pregunta_instance):
    if str(pregunta_instance.tpregunta).strip() == 'linkert':
        auto_create_choices(tipo_linkert, pregunta_instance)
    if str(pregunta_instance.tpregunta).strip() == 'Si No':
        auto_create_choices(tipo_si_no, pregunta_instance)
    if str(pregunta_instance.tpregunta).strip() == 'interes':
        auto_create_choices(tipo_interes, pregunta_instance)
    if str(pregunta_instance.tpregunta).strip() == 'abierta':
        auto_create_choices(tipo_abierta, pregunta_instance)

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
