from sqlalchemy import Column, BigInteger, Integer, String, Boolean, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(50))
    email = Column(String(120), unique=True)
    contraseña = Column(String(120))
    rol = Column(String(30))
    estado = Column(Boolean)
    ventas = relationship("Venta")

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

class Producto(Base):
    __tablename__ = 'productos'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(50))
    cantidad = Column(Integer)
    preciounit = Column(Numeric(10, 2))
    imagen = Column(String(1000))
    estado = Column(Boolean)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class Venta(Base):
    __tablename__ = 'ventas'
    id = Column(BigInteger, primary_key=True)
    usuario_id = Column(ForeignKey('usuarios.id'))
    fecha = Column(DateTime)
    valortotal = Column(Numeric(10, 2))
    estado = Column(Boolean)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)