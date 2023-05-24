from schemes import Establecimiento, Parroquia, Distrito
from tabulate import tabulate


def run_queries(session):
    '''Los establecimientos ordenados por nombre de parroquia que tengan más de 40 profesores
    y la cadena "Educación regular" en tipo de educación.'''
    query1 = session.query(Establecimiento).join(Parroquia).filter(
        Establecimiento.numero_docentes > 40,
        Establecimiento.tipo_educacion.like('%Educación regular%')
    ).order_by(Parroquia.nombre).all()

    '''Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D04:'''
    query2 = session.query(Establecimiento).join(Distrito).filter(
        Distrito.codigo == '11D04'
    ).order_by(Establecimiento.sostenimiento).all()

    print('Establecimientos ordenados por nombre de parroquia que tengan más de 40 profesores y la cadena "Educación regular" en tipo de educación:')
    print(tabulate([(e.nombre, e.numero_docentes, e.parroquia.nombre)
          for e in query1], headers=["Nombre establecimiento", "N° docentes", "Parroquia"]))

    print("\nEstablecimientos con código de distrito 11D04 ordenados por sostenimiento:")
    print(tabulate([(e.sostenimiento, e.nombre) for e in query2], headers=[
          "Sostenimiento", "Establecimiento"]))
