from sqlalchemy import Integer, String, MetaData, \
    TIMESTAMP, Column, Table

metadata = MetaData()

operation = Table(
    "operation",
    metadata,
    Column("id", Integer, primary_key=True),
)