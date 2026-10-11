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

class Integration(Base):
    __tablename__ = "integrations"

    id = Column(Integer, primary_key=True, index=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    environment_id = Column(Integer, ForeignKey("environments.id"), nullable=False)
    integration_type = Column(String, nullable=False)
    configuration = Column(JSON, default={})
    credential_reference = Column(String)
    health_status = Column(String)
    last_successful_sync = Column(DateTime(timezone=True))

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    environment_id = Column(Integer, ForeignKey("environments.id"), nullable=False)
    source = Column(String, nullable=False)
    source_event_id = Column(String)
    fingerprint = Column(String, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    severity = Column(String)
    status = Column(String, default="New")
    affected_resources = Column(JSON, default=[])
    opened_at = Column(DateTime(timezone=True), server_default=func.now())
    resolved_at = Column(DateTime(timezone=True))
    correlation_id = Column(String, index=True)

class Evidence(Base):
    __tablename__ = "evidence"

    id = Column(Integer, primary_key=True, index=True)
    incident_id = Column(Integer, ForeignKey("incidents.id"), nullable=False)
    source_integration_id = Column(Integer, ForeignKey("integrations.id"))
    evidence_type = Column(String, nullable=False)
    resource_reference = Column(String)
    observed_at = Column(DateTime(timezone=True))
    collected_at = Column(DateTime(timezone=True), server_default=func.now())
    content_reference = Column(String)
    content_hash = Column(String)
    redaction_status = Column(String)
