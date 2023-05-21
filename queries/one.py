from schemes import Establecimiento, Parroquia, Provincia, Canton
from tabulate import tabulate


def run_queries(session):
    '''Todos los establecimientos que pertenecen al Código División Política Administrativa 
    Parroquia con valor 110553:'''
    parroquia = session.query(Establecimiento).join(Parroquia).filter(
        Parroquia.codigo == '110553').all()

    '''Todos los establecimientos de la provincia del Oro:'''
    establecimientos_oro = session.query(Establecimiento).join(
        Provincia).filter(Provincia.nombre == 'El Oro').all()

    '''Todos los establecimientos del cantón de Portovelo:'''
    portovelo_establecimientos = session.query(Establecimiento).join(
        Canton).filter(Canton.nombre == 'Portovelo').all()

    '''Todos los establecimientos del cantón de Zamora:'''
    establecimientos_zamora = session.query(Establecimiento).join(
        Canton).filter(Canton.nombre == 'Zamora').all()

    print("Establecimientos que pertenecen al Código División Política Administrativa Parroquia con valor 110553:")
    print(tabulate([(e.codigo_amie, e.nombre)
          for e in parroquia], headers=["Código AMIE", "Nombre"]))

    print("\nEstablecimientos de la provincia del Oro:")
    print(tabulate([(e.codigo_amie, e.nombre)
          for e in establecimientos_oro], headers=["Código AMIE", "Nombre"]))

    print("\nEstablecimientos del cantón de Portovelo:")
    print(tabulate([(e.codigo_amie, e.nombre)
          for e in portovelo_establecimientos], headers=["Código AMIE", "Nombre"]))

    print("\nEstablecimientos del cantón de Zamora:")
    print(tabulate([(e.codigo_amie, e.nombre)
          for e in establecimientos_zamora], headers=["Código AMIE", "Nombre"]))
