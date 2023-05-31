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


def get_provincia_for_canton(row):
    existing_provincia = session.query(Provincia).filter_by(
        codigo=row['Código División Política Administrativa Provincia']).first()

    if not existing_provincia:
        existing_provincia = Provincia(
            codigo=row['Código División Política Administrativa Provincia'], nombre=row['Provincia'])
        session.add(existing_provincia)
        session.flush()  # Flush the session to generate primary key before accessing it

    return existing_provincia


def get_canton_for_parroquia(row):
    existing_canton = session.query(Canton).filter_by(
        codigo=row['Código División Política Administrativa  Cantón']).first()

    if not existing_canton:
        existing_canton = Canton(codigo=row['Código División Política Administrativa  Cantón'], nombre=row['Cantón'],
                                 provincia=get_provincia_for_canton(row))
        session.add(existing_canton)
        session.flush()  # Flush the session to generate primary key before accessing it

    return existing_canton


def load_data_into_db():
    global session
    session = create_session()
    data = get_data()

    # For each row, it checks if it already exists in the db
    for index, row in data.iterrows():
        # COLLECTS PARROQUIA
        parroquia = session.query(Parroquia).filter_by(
            codigo=row['Código División Política Administrativa  Parroquia']).first()

        if not parroquia:
            canton = get_canton_for_parroquia(row)

            parroquia = Parroquia(codigo=row['Código División Política Administrativa  Parroquia'],
                                  nombre=row['Parroquia'],
                                  canton=canton)

            session.add(parroquia)
            session.flush()  # Flush the session to generate primary key before accessing it

        # COLLECTS DISTRITO
        distrito = session.query(Distrito).filter_by(
            codigo=row['Código de Distrito']).first()

        if not distrito:
            distrito = Distrito(codigo=row['Código de Distrito'])
            session.add(distrito)
            session.flush()  # Flush the session to generate primary key before accessing it

        # COLLECTS ESTABLECIMIENTO
        establecimiento = session.query(Establecimiento).filter_by(
            codigo_amie=row['Código AMIE']).first()

        if not establecimiento:
            establecimiento = Establecimiento(
                codigo_amie=row['Código AMIE'],
                nombre=row['Nombre de la Institución Educativa'],
                parroquia=parroquia,
                distrito=distrito,
                sostenimiento=row['Sostenimiento'],
                tipo_educacion=row['Tipo de Educación'],
                modalidad=row['Modalidad'],
                jornada=row['Jornada'],
                acceso=row['Acceso (terrestre/ aéreo/fluvial)'],
                numero_estudiantes=row['Número de estudiantes'],
                numero_docentes=row['Número de docentes']
            )

            session.add(establecimiento)
            session.flush()  # Flush the session to generate primary key before accessing it

    session.commit()


def terminate_session():
    close_session()


def get_running_session():
    return session
