"""Schema for Apartment."""

from pydantic import BaseModel


class Apartment(BaseModel):
    """
    Apartment schema.

    area - Apartment area
    constraction_year - Apartment constraction year
    bedrooms - Count of apartment bedrooms
    garden_area - Apartment garden area
    balcony_present - Apartment balcony presence
    parking_present - Apartment parking present
    furnished - Apartment furnished status
    garage_present - Apartment garage present
    storage_present - Apartment storage present
    """

    area: int
    constraction_year: int
    bedrooms: int
    garden_area: int
    balcony_present: int
    parking_present: int
    furnished: int
    garage_present: int
    storage_present: int
