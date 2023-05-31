from sqlalchemy.orm import sessionmaker
from connection import engine
from tabulate import tabulate
from schemes import Establecimiento, Parroquia, Provincia, Canton

# Create a session
Session = sessionmaker(bind=engine)
session = Session()


def run_queries(session):

    # Query 1: Todos los establecimientos que pertenecen al Código División Política Administrativa Parroquia con valor 110553
    query1 = session.query(Establecimiento).join(
        Parroquia).filter(Parroquia.codigo == '110553')

    # Query 2: Todos los establecimientos de la provincia del Oro
    query2 = session.query(Establecimiento).select_from(Establecimiento).join(
        Parroquia, Establecimiento.parroquia).join(
        Canton, Parroquia.canton).join(
        Provincia, Canton.provincia).filter(
        Provincia.nombre == 'EL ORO')

    # Query 3: Todos los establecimientos del cantón de Portovelo
    query3 = session.query(Establecimiento).select_from(Establecimiento).join(
        Parroquia, Establecimiento.parroquia).join(
        Canton, Parroquia.canton).filter(
        Canton.nombre == 'PORTOVELO')

    # Query 4: Todos los establecimientos del cantón de Zamora
    query4 = session.query(Establecimiento).select_from(Establecimiento).join(
        Parroquia, Establecimiento.parroquia).join(
        Canton, Parroquia.canton).filter(
        Canton.nombre == 'ZAMORA')

    print("Establecimientos que pertenecen al Código División Política Administrativa Parroquia con valor 110553:")
    result1 = query1.all()
    print(tabulate([(e.codigo_amie, e.nombre)
          for e in result1], headers=["Código AMIE", "Nombre"]))

    print("\nEstablecimientos de la provincia del Oro:")
    result2 = query2.all()
    print(tabulate([(e.codigo_amie, e.nombre)
          for e in result2], headers=["Código AMIE", "Nombre"]))

    print("\nEstablecimientos del cantón de Portovelo:")
    result3 = query3.all()
    print(tabulate([(e.codigo_amie, e.nombre)
          for e in result3], headers=["Código AMIE", "Nombre"]))

    print("\nEstablecimientos del cantón de Zamora:")
    result4 = query4.all()
    print(tabulate([(e.codigo_amie, e.nombre)
          for e in result4], headers=["Código AMIE", "Nombre"]))
