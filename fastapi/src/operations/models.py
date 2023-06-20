from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, ForeignKey, MetaData


metadata = MetaData()

group = Table(
    "group",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
)

apartment = Table(
    "apartment",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, nullable=False),
    Column("title", String, nullable=False),
    Column("price", String, default=datetime.utcnow),
    Column("description", String, nullable=False),
    Column("group_id", Integer, ForeignKey(group.c.id)),
)


address = Table(
    "address",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("country", String, nullable=False),
    Column("city", String, nullable=False),
    Column("address", String, nullable=False),
    Column("zip_code", String, nullable=False),
    Column("apartment_id", Integer, ForeignKey(apartment.c.id)),
)

groupUser = Table(
    "groupUser",
    metadata,
    Column("group_id", Integer, ForeignKey(group.c.id)),
    Column("user_id", Integer, nullable=False),
)
