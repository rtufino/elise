import csv

from django.core.management.base import BaseCommand, CommandError

from core.models import Alumno, User, Carrera, Periodo


# from registro.models import Periodo, Carrera, Usuario, Estudiante, Materia, Distributivo, Alumno


class Command(BaseCommand):
    help = '''Carga los datos de estudiantes y materias a partir de datos 
    proporcionados por el departamento de informática de la UPS-Q'''

    def get_version(self):
        return '0.1'

    def add_arguments(self, parser):
        parser.add_argument(
            'periodo',
            help='Número de periodo para el cual se cargara la información'
        )

        parser.add_argument(
            'archivo',
            help='Path del archivo csv con la información para cargar al sistema'
        )

    def handle(self, *args, **options):
        periodo = options['periodo']
        archivo = options['archivo']
        periodo = Periodo(
            nombre=periodo
        )
        periodo.save()
        registros = []
        with open(archivo, encoding="utf8") as csvfile:
            read_csv = csv.reader(csvfile, delimiter=',')
            next(read_csv)
            for row in read_csv:
                registros.append(row)

        self.stdout.write("[*] Creando Estudiantes ...")
        for row in registros:
            self.crear_estudiante(row)

    @staticmethod
    def crear_estudiante(estudiante):
        correo = estudiante[9]
        data = User.objects.filter(email=correo)
        if len(data) > 0:
            return data[0]
        # Crear el usuario
        usuario = User(
            email=correo,
            is_active=True,
            is_staff=False,
            is_superuser=False,
        )
        usuario.set_password(str(estudiante[1]))
        # Guardar en BDD
        usuario.save()
        carrera = Carrera.objects.filter(nombre=estudiante[0]).first()
        alumno = Alumno(
            usuario=usuario,
            cedula=str(estudiante[1]),
            nombres=estudiante[2],
            apellidos=estudiante[3],
            genero=estudiante[4],
            ciudad=estudiante[5],
            colegio=estudiante[6],
            edad=estudiante[7],
            estado=estudiante[8],
            carrera_postular=carrera
        )
        alumno.save()
        print("[+] Creando ", usuario.pk, "-", usuario)
        return alumno
