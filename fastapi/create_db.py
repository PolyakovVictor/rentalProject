from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from dependencies import Base, engine


class User(Base):
    __tablename__ = 'User'
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    contact_data = relationship("UserContactData", back_populates="user")
    apartments = relationship("Apartment", back_populates="user")


class UserContactData(Base):
    __tablename__ = 'UserContactData'
    user_contact_data_id = Column(Integer, primary_key=True)
    email = Column(String(70), nullable=False)
    phone_number = Column(String(50), nullable=False)
    id_user = Column(Integer, ForeignKey("User.user_id"))
    user = relationship("User", back_populates="contact_data")


class Apartment(Base):
    __tablename__ = 'Apartment'
    apartment_id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    price = Column(String(50), nullable=False)
    description = Column(String(300), nullable=False)
    id_user = Column(Integer, ForeignKey("User.user_id"))
    user = relationship("User", back_populates="apartments")
    address = relationship("ApartmentAddress", back_populates="apartment")
    images = relationship("ApartmentImage", back_populates="apartment")


class ApartmentAddress(Base):
    __tablename__ = 'ApartmentAddress'
    apartment_address_id = Column(Integer, primary_key=True)
    country = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    address = Column(String(100), nullable=False)
    zip_code = Column(String(20), nullable=False)
    id_apartment = Column(Integer, ForeignKey("Apartment.apartment_id"))
    apartment = relationship("Apartment", back_populates="address")


class ApartmentImage(Base):
    __tablename__ = 'ApartmentImage'
    apartment_image_id = Column(Integer, primary_key=True)
    path = Column(String(250), nullable=False)
    id_apartment = Column(Integer, ForeignKey("Apartment.apartment_id"))
    apartment = relationship("Apartment", back_populates="images")


class RentalGroup(Base):
    __tablename__ = 'RentalGroup'
    rental_group_id = Column(Integer, primary_key=True)
    users = relationship("RentalGroupUser", back_populates="group")


class RentalGroupUser(Base):
    __tablename__ = 'RentalGroupUser'
    id_rental_group = Column(
        Integer, ForeignKey("RentalGroup.rental_group_id"), primary_key=True)
    id_user = Column(Integer, ForeignKey("User.user_id"), primary_key=True)
    group = relationship("RentalGroup", back_populates="users")
    user = relationship("User", back_populates="rental_groups")


Base.metadata.create_all(engine)
