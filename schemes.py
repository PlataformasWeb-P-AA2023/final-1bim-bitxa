from sqlalchemy import Column, Integer, String, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from connection import engine

Base = declarative_base()


class Provincia(Base):
    __tablename__ = 'provincia'

    codigo = Column('codigo_division_politica_provincia',
                    String(10), primary_key=True)
    nombre = Column('nombre', String(50))

    cantones = relationship("Canton", back_populates="provincia")

    establecimientos = relationship(
        "Establecimiento", back_populates="provincia")


class Canton(Base):
    __tablename__ = 'canton'

    codigo = Column('codigo_division_politica_canton',
                    String(10), primary_key=True)
    nombre = Column('nombre', String(250))
    provincia_codigo = Column('codigo_division_politica_provincia', String(
        10), ForeignKey('provincia.codigo_division_politica_provincia'))

    provincia = relationship("Provincia", back_populates="cantones")
    parroquias = relationship("Parroquia", back_populates="canton")

    establecimientos = relationship(
        "Establecimiento", back_populates="canton")


class Parroquia(Base):
    __tablename__ = 'parroquia'

    codigo = Column('codigo_division_politica_parroquia',
                    String(10), primary_key=True)
    nombre = Column('nombre', String(250))
    canton_codigo = Column('codigo_division_politica_canton', String(
        10), ForeignKey('canton.codigo_division_politica_canton'))
    provincia_codigo = Column('codigo_division_politica_provincia', String(
        10), ForeignKey('provincia.codigo_division_politica_provincia'))

    canton = relationship("Canton", back_populates="parroquias")

    establecimientos = relationship(
        "Establecimiento", back_populates="parroquia")


class Distrito(Base):
    __tablename__ = 'distrito'
    codigo = Column('codigo_distrito', String(10), primary_key=True)
    establecimientos = relationship(
        "Establecimiento", back_populates="distrito")


class Establecimiento(Base):
    __tablename__ = 'establecimiento'

    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo_amie = Column('codigo_amie', String(10))
    nombre = Column('nombre', String(250))
    provincia_codigo = Column('codigo_division_politica_provincia', String(
        10), ForeignKey('provincia.codigo_division_politica_provincia'))
    canton_codigo = Column('codigo_division_politica_canton', String(
        10), ForeignKey('canton.codigo_division_politica_canton'))
    parroquia_codigo = Column('codigo_division_politica_parroquia', String(
        10), ForeignKey('parroquia.codigo_division_politica_parroquia'))
    codigo_distrito = Column('codigo_distrito', String(
        10), ForeignKey('distrito.codigo_distrito'))
    sostenimiento = Column('sostenimiento', String(50))
    tipo_educacion = Column('tipo_educacion', String(50))
    modalidad = Column('modalidad', String(50))
    jornada = Column('jornada', String(50))
    acceso = Column('acceso', String(50))
    numero_estudiantes = Column('numero_estudiantes', Integer)
    numero_docentes = Column('numero_docentes', Integer)

    provincia = relationship("Provincia", back_populates="establecimientos")
    canton = relationship("Canton", back_populates="establecimientos")
    parroquia = relationship("Parroquia", back_populates="establecimientos")
    distrito = relationship("Distrito", back_populates="establecimientos")


def create_schemes():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
