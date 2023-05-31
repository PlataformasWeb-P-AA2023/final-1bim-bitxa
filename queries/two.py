from schemes import Establecimiento, Canton, Parroquia
from tabulate import tabulate


def run_queries(session):
    '''Las parroquias que tienen establecimientos únicamente en la jornada "Matutina y Vespertina"'''
    query1 = session.query(Parroquia).select_from(Parroquia).join(
        Parroquia.establecimientos).filter(
        Establecimiento.jornada == 'Matutina y Vespertina').distinct()

    '''Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459'''
    student_numbers = [448, 450, 451, 454, 458, 459]
    query2 = session.query(Canton).select_from(Canton).join(
        Canton.parroquias).join(
        Parroquia.establecimientos).filter(
        Establecimiento.numero_estudiantes.in_(student_numbers)).distinct()

    print("Parroquias con establecimientos únicamente en la jornada 'Matutina y Vespertina':")
    result1 = query1.all()
    print(tabulate([(p.codigo, p.nombre) for p in result1],
          headers=["Código Parroquia", "Nombre"]))

    result2 = query2.all()
    print("\nCantones con establecimientos y números de estudiantes específicos:")
    print(tabulate([(c.codigo, c.nombre, student_numbers[index])
                    for index, c in enumerate(result2)], headers=["Código Cantón", "Nombre", "Número Estudiantes"]))
