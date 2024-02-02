"""
This module defines the database models using SQLAlchemy.

It includes model classes for different types of real estate,
specifically rental apartments. The module uses SQLAlchemy's
ORM capabilities to map Python classes to database tables.
The structure and fields of the RentApartments class are configured
to match the corresponding database for rental apartments.
"""

from sqlalchemy import INTEGER, REAL, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from config import db_settings


class Base(DeclarativeBase):
    """Base class for SQLAlchemy models."""

    pass  # noqa: WPS420, WPS604


class RentApartments(Base):
    """
    SQLAlchemy model class for rental apartments.

    Attributes:
        address (str): The address of the apartment, primary key.
        area (float): The area of the apartment in square meters.
        constraction_year (int): The year the apartment was constructed.
        rooms (int): The number of rooms in the apartment.
        bedrooms (int): The number of bedrooms in the apartment.
        bathrooms (int): The number of bathrooms in the apartment.
        balcony (str): Information about the balcony.
        storage (str): Information about storage space.
        parking (str): Information about parking availability.
        furnished (str): Indicates if the apartment is furnished.
        garage (str): Information about the garage.
        garden (str): Information about the garden.
        energy (str): Energy efficiency rating.
        facilities (str): Other facilities available.
        zip (str): ZIP code of the apartment's location.
        neighborhood (str): Neighborhood where the apartment is located.
        rent (int): Monthly rent price.
    """

    __tablename__ = db_settings.rent_apart_table_name

    address: Mapped[str] = mapped_column(VARCHAR(), primary_key=True)
    area: Mapped[float] = mapped_column(REAL())
    constraction_year: Mapped[int] = mapped_column(INTEGER())
    rooms: Mapped[int] = mapped_column(INTEGER())
    bedrooms: Mapped[int] = mapped_column(INTEGER())
    bathrooms: Mapped[int] = mapped_column(INTEGER())
    balcony: Mapped[str] = mapped_column(VARCHAR())
    storage: Mapped[str] = mapped_column(VARCHAR())
    parking: Mapped[str] = mapped_column(VARCHAR())
    furnished: Mapped[str] = mapped_column(VARCHAR())
    garage: Mapped[str] = mapped_column(VARCHAR())
    garden: Mapped[str] = mapped_column(VARCHAR())
    energy: Mapped[str] = mapped_column(VARCHAR())
    facilities: Mapped[str] = mapped_column(VARCHAR())
    zip: Mapped[str] = mapped_column(VARCHAR())
    neighborhood: Mapped[str] = mapped_column(VARCHAR())
    rent: Mapped[int] = mapped_column(INTEGER())
