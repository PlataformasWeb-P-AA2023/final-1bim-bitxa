from schemes import Establecimiento, Parroquia, Distrito
from tabulate import tabulate


def run_queries(session):
    '''Los establecimientos ordenados por nombre de parroquia que tengan más de 40 profesores y la cadena "Educación regular" en tipo de educación.'''
    establecimientos_profesores = session.query(Establecimiento, Parroquia).join(Parroquia).filter(
        Establecimiento.numero_docentes > 40,
        Establecimiento.tipo_educacion.like('%Educación regular%')
    ).order_by(Parroquia.nombre).all()

    print("Establecimientos con más de 40 profesores y tipo de educación 'Educación regular':")
    print(tabulate([(e.nombre, e.numero_docentes, p.nombre)
          for e, p in establecimientos_profesores], headers=["Nombre establecimiento", "N° docentes", "Parroquia"]))

    '''Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D04:'''
    establecimientos_sostenimiento = session.query(Establecimiento).join(Distrito).filter(
        Distrito.codigo == '11D04'
    ).order_by(Establecimiento.sostenimiento).all()

    print("\nEstablecimientos con código de distrito 11D04 ordenados por sostenimiento:")
    print(tabulate([(e.sostenimiento, e.nombre) for e in establecimientos_sostenimiento], headers=[
          "Sostenimiento", "Establecimiento"]))
