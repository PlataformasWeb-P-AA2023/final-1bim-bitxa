from sqlalchemy import desc
from schemes import Establecimiento, Provincia, Canton, Parroquia
from tabulate import tabulate


def run_queries(session):
    # Establecimientos con más de 100 profesores ordenados por número de estudiantes.
    query1 = session.query(Establecimiento, Provincia).select_from(Parroquia).join(Parroquia.establecimientos).join(Canton).join(Provincia).filter(
        Establecimiento.numero_docentes > 100).order_by(desc(Establecimiento.numero_estudiantes)).all()

    # Establecimientos con más de 100 profesores ordenados por número de profesores.
    query2 = session.query(Establecimiento, Provincia).select_from(Parroquia).join(Parroquia.establecimientos).join(Canton).join(Provincia).filter(
        Establecimiento.numero_docentes > 100).order_by(desc(Establecimiento.numero_docentes)).all()

    print("Establecimientos con más de 100 profesores ordenados por número de estudiantes:")
    print(tabulate([(e.nombre, e.numero_estudiantes, p.nombre) for e, p in query1], headers=[
          "Establecimiento", "Número Estudiantes", "Provincia"]))

    print("\nEstablecimientos con más de 100 profesores ordenados por número de profesores:")
    print(tabulate([(e.nombre, e.numero_docentes, p.nombre) for e, p in query2], headers=[
          "Establecimiento", "Número Profesores", "Provincia"]))
