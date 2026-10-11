from sqlalchemy import Column, Integer, String, Boolean, JSON, DateTime, ForeignKey, Enum
from sqlalchemy.sql import func
from .database import Base
import enum

class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    status = Column(String, default="active")
    settings = Column(JSON, default={})
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Environment(Base):
    __tablename__ = "environments"

    id = Column(Integer, primary_key=True, index=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    name = Column(String, nullable=False)
    environment_type = Column(String, nullable=False)
    provider = Column(String)
    resource_scope = Column(String)
    execution_mode = Column(String, default="Observe")
    policy_set_id = Column(String)
