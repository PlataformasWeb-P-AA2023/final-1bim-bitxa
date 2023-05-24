import pandas as pd
from connection import create_session, close_session
from schemes import *
file_path = 'data/Listado-Instituciones-Educativas.csv'


# Default value: null or None
session = locals().get('session', None)


def get_data():
    global data
    data = pd.read_csv(file_path)
    return data


def load_data_into_db():
    global session
    session = create_session()
    data = get_data()

    # For each row, it checks it already exists on db

    for index, row in data.iterrows():

        # COLLECTS PROVINCIA
        provincia = session.query(Provincia).filter_by(
            codigo=row['Código División Política Administrativa Provincia']).first()
        if not provincia:
            provincia = Provincia(
                codigo=row['Código División Política Administrativa Provincia'], nombre=row['Provincia'])
            session.add(provincia)

        # COLLECTS CANTON
        canton = session.query(Canton).filter_by(
            codigo=row['Código División Política Administrativa  Cantón']).first()
        if not canton:
            canton = Canton(codigo=row['Código División Política Administrativa  Cantón'], nombre=row['Cantón'],
                            provincia_codigo=row['Código División Política Administrativa Provincia'])
            session.add(canton)

        # COLLECTS PARROQUIA
        parroquia = session.query(Parroquia).filter_by(
            codigo=row['Código División Política Administrativa  Parroquia']).first()
        if not parroquia:
            parroquia = Parroquia(codigo=row['Código División Política Administrativa  Parroquia'], nombre=row['Parroquia'],
                                  canton_codigo=row['Código División Política Administrativa  Cantón'], provincia_codigo=row['Código División Política Administrativa Provincia'])
            session.add(parroquia)

        # COLLECTS DISTRITO
        distrito = session.query(Distrito).filter_by(
            codigo=row['Código de Distrito']).first()
        if not distrito:
            distrito = Distrito(codigo=row['Código de Distrito'])
            session.add(distrito)

        # COLLECTS ESTABLECIMIENTO
        establecimiento = session.query(Establecimiento).filter_by(
            codigo_amie=row['Código AMIE']).first()
        if not establecimiento:
            establecimiento = Establecimiento(
                codigo_amie=row['Código AMIE'],
                provincia_codigo=row['Código División Política Administrativa Provincia'],
                nombre=row['Nombre de la Institución Educativa'],
                canton_codigo=row['Código División Política Administrativa  Cantón'],
                parroquia_codigo=row['Código División Política Administrativa  Parroquia'],
                codigo_distrito=row['Código de Distrito'],
                sostenimiento=row['Sostenimiento'],
                tipo_educacion=row['Tipo de Educación'],
                modalidad=row['Modalidad'],
                jornada=row['Jornada'],
                acceso=row['Acceso (terrestre/ aéreo/fluvial)'],
                numero_estudiantes=row['Número de estudiantes'],
                numero_docentes=row['Número de docentes']
            )
            session.add(establecimiento)
    session.commit()


def terminate_session():
    close_session()


def get_running_session():
    return session
