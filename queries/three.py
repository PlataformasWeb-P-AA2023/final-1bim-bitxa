from schemes import Establecimiento, Canton, Parroquia
from tabulate import tabulate
from sqlalchemy import or_, text
from sqlalchemy import func


def run_queries(session):
    try:
        session.execute(
            text("SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''))"))
    except:
        print("ONLY_FULL_GROUP_BY could not be set.")

    '''Los cantones que tienen establecimientos con 0 número de profesores, 5 profesores, 11 profesores:'''
    teacher_numbers = [0, 5, 11]
    query1 = session.query(Canton, Establecimiento).select_from(Canton).join(
        Canton.parroquias).join(
        Parroquia.establecimientos).filter(
        Establecimiento.numero_docentes.in_(teacher_numbers)).group_by(Canton).distinct(Canton.codigo)
    result1 = query1.all()

    '''Los establecimientos que pertenecen a la parroquia Pindal con estudiantes mayores o iguales a 21:'''
    query2 = session.query(Establecimiento).select_from(Establecimiento).join(Parroquia,
                                                                              Establecimiento.parroquia_codigo == Parroquia.codigo).filter(
        Parroquia.nombre == "PINDAL", Establecimiento.numero_estudiantes >= 21)
    result2 = query2.all()

    print("Cantones que tienen establecimientos con 0 número de profesores, 5 profesores, 11 profesores:")
    print(tabulate([(c.codigo, c.nombre, e.numero_docentes) for c, e in result1],
                   headers=["Código Cantón", "Nombre Cantón", "Número Docentes"]))

    print("\nEstablecimientos de la parroquia Pindal con estudiantes mayores o iguales a 21:")
    print(tabulate([(e.codigo_amie, e.nombre, e.numero_estudiantes)
          for e in result2], headers=["Código AMIE", "Nombre", "Número estudiantes"]))
