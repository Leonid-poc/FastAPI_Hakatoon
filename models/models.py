from datetime import datetime
from sqlalchemy import MetaData, Integer, String, ForeignKey, TIMESTAMP, Table, Column, VARCHAR, JSON

metadata = MetaData()


roles = Table(
    'roles',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', VARCHAR(255), nullable=False),
    Column('permissions', JSON),
)

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', VARCHAR(255), nullable=False),
    Column('email', VARCHAR(255), nullable=False),
    Column('phone', VARCHAR(50), nullable=True),
    Column('password', String, nullable=False),
    Column('registered_at', TIMESTAMP, default=datetime.utcnow),
    Column('role_id', Integer, ForeignKey('roles.id'))
)