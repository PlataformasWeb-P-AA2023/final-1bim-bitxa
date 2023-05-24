from sqlalchemy import desc
from schemes import Establecimiento, Provincia
from tabulate import tabulate


def run_queries(session):
    '''Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores.'''
    query1 = session.query(Establecimiento).filter(
        Establecimiento.numero_docentes > 100
    ).order_by(desc(Establecimiento.numero_estudiantes)).all()

    '''Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores.'''
    query2 = session.query(Establecimiento).filter(
        Establecimiento.numero_docentes > 100).order_by(desc(Establecimiento.numero_docentes)).all()

    print("Establecimientos con más de 100 profesores ordenados por número de estudiantes:")
    print(tabulate([(e.nombre, e.numero_estudiantes, e.provincia.nombre) for e in query1], headers=[
          "Establecimiento", "Número Estudiantes", "Provincia"]))

    print("\nEstablecimientos con más de 100 profesores ordenados por número de profesores:")
    print(tabulate([(e.nombre, e.numero_docentes, e.provincia.nombre) for e in query2], headers=[
          "Establecimiento", "Número Profesores", "Provincia"]))
