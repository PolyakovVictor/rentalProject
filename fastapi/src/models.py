from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Group(Base):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True, autoincrement=True)
    apartment_id = Column(Integer, ForeignKey('apartment.id'), nullable=True)
    start_of_lease = Column(Date, nullable=True)
    end_of_lease = Column(Date, nullable=True)
    settlers_limit = Column(Integer, nullable=False)
    description = Column(String, nullable=True)
    title = Column(String, nullable=False)


class GroupUser(Base):
    __tablename__ = "groupUser"

    group_id = Column(Integer, ForeignKey("group.id"), primary_key=True)
    user_id = Column(Integer, nullable=False)

    group = relationship("Group", lazy="select")


class Apartment(Base):
    __tablename__ = "apartment"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    price = Column(String, default=0)
    description = Column(String, nullable=False)
    type = Column(String, nullable=False)
    room_count = Column(Integer, nullable=False)

    groups = relationship("Group", lazy="select")


class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String, nullable=False)
    city = Column(String, nullable=False)
    address = Column(String, nullable=False)
    zip_code = Column(String, nullable=False)
    apartment_id = Column(Integer, ForeignKey("apartment.id"))

    apartment = relationship("Apartment", lazy="select")
