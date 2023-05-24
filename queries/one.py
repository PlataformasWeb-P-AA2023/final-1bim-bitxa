from schemes import Establecimiento, Parroquia, Provincia, Canton
from tabulate import tabulate


def run_queries(session):
    '''Todos los establecimientos que pertenecen al Código División Política Administrativa 
    Parroquia con valor 110553:'''
    query1 = session.query(Establecimiento).join(Parroquia).filter(
        Parroquia.codigo == '110553').all()

    '''Todos los establecimientos de la provincia del Oro:'''
    query2 = session.query(Establecimiento).join(
        Provincia).filter(Provincia.nombre == 'El Oro').all()

    '''Todos los establecimientos del cantón de Portovelo:'''
    query3 = session.query(Establecimiento).join(
        Canton).filter(Canton.nombre == 'Portovelo').all()

    '''Todos los establecimientos del cantón de Zamora:'''
    query4 = session.query(Establecimiento).join(
        Canton).filter(Canton.nombre == 'Zamora').all()

    print("Establecimientos que pertenecen al Código División Política Administrativa Parroquia con valor 110553:")
    print(tabulate([(e.codigo_amie, e.nombre)
          for e in query1], headers=["Código AMIE", "Nombre"]))

    print("\nEstablecimientos de la provincia del Oro:")
    print(tabulate([(e.codigo_amie, e.nombre)
          for e in query2], headers=["Código AMIE", "Nombre"]))

    print("\nEstablecimientos del cantón de Portovelo:")
    print(tabulate([(e.codigo_amie, e.nombre)
          for e in query3], headers=["Código AMIE", "Nombre"]))

    print("\nEstablecimientos del cantón de Zamora:")
    print(tabulate([(e.codigo_amie, e.nombre)
          for e in query4], headers=["Código AMIE", "Nombre"]))
