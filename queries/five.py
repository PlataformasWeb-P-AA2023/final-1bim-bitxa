from sqlalchemy import asc
from schemes import Establecimiento
from tabulate import tabulate


def run_queries(session):
    '''Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores.'''
    establecimientos_by_estudiantes = session.query(Establecimiento).filter(
        Establecimiento.numero_docentes > 100).order_by(asc(Establecimiento.numero_estudiantes)).all()
    '''Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores.'''
    establecimientos_by_profesores = session.query(Establecimiento).filter(
        Establecimiento.numero_docentes > 100).order_by(asc(Establecimiento.numero_docentes)).all()

    print("Establecimientos con más de 100 profesores ordenados por número de estudiantes:")
    print(tabulate([(e.nombre, e.numero_estudiantes) for e in establecimientos_by_estudiantes], headers=[
          "Establecimiento", "Número Estudiantes"]))

    print("\nEstablecimientos con más de 100 profesores ordenados por número de profesores:")
    print(tabulate([(e.nombre, e.numero_docentes) for e in establecimientos_by_profesores], headers=[
          "Establecimiento", "Número Profesores"]))
