from schemes import Establecimiento, Canton, Parroquia
from tabulate import tabulate


def run_queries(session):
    '''Las parroquias que tienen establecimientos únicamente en la jornada "Matutina y Vespertina"'''
    query1 = session.query(Parroquia).join(Establecimiento).filter(
        Establecimiento.jornada == 'Matutina y Vespertina').all()

    '''Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459'''
    student_numbers = [448, 450, 451, 454, 458, 459]
    query2 = session.query(Canton).join(Establecimiento).filter(
        Establecimiento.numero_estudiantes.in_(student_numbers)).distinct().all()

    print("Parroquias con establecimientos únicamente en la jornada 'Matutina y Vespertina':")
    print(tabulate([(p.codigo, p.nombre) for p in query1],
          headers=["Código Parroquia", "Nombre"]))

    print("\nCantones con establecimientos y números de estudiantes específicos:")
    print(tabulate([(c.codigo, c.nombre, student_numbers[index])
                    for index, c in enumerate(query2)], headers=["Código Cantón", "Nombre", "Número Estudiantes"]))
