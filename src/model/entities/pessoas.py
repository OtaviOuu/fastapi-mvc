from src.model.settings.db_metadata import metadata
from sqlalchemy import Column, Integer, String, Table

Pessoas = Table(
    "pessoas",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("nome", String),
)
