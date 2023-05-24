from schemes import Establecimiento, Canton, Parroquia
from tabulate import tabulate
from sqlalchemy import text


def run_queries(session):
    session.execute(
        text("SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''))"))

    '''Los cantones que tienen establecimientos con 0 número de profesores, 5 profesores, 11 profesores:'''
    teacher_numbers = [0, 5, 11]
    query1 = session.query(Canton, Establecimiento).join(Establecimiento).filter(
        Establecimiento.numero_docentes.in_(teacher_numbers)
    ).group_by(Canton).distinct().all()

    '''Los establecimientos que pertenecen a la parroquia Pindal con estudiantes mayores o iguales a 21:'''
    query2 = session.query(Establecimiento).join(Parroquia).filter(
        Parroquia.nombre == "Pindal", Establecimiento.numero_estudiantes >= 21).all()

    print("Cantones con establecimientos y números de docentes específicos:")
    print(tabulate([(c.codigo, c.nombre, e.numero_docentes) for c, e in query1],
                   headers=["Código Cantón", "Nombre Cantón", "Número Docentes"]))

    print("\nEstablecimientos de la parroquia Pindal con estudiantes mayores o iguales a 21:")
    print(tabulate([(e.codigo_amie, e.nombre, e.numero_estudiantes)
          for e in query2], headers=["Código AMIE", "Nombre", "Número estudiantes"]))
