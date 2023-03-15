from sqlalchemy import Column, DateTime, Boolean, Integer, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import declared_attr


class MixinMarkChanges:
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    is_deleted = Column(Boolean, default=False)

    @declared_attr
    def created_by(cls):
        return Column(Integer, ForeignKey('users.id'), nullable=False)

    @declared_attr
    def updated_by(cls):
        return Column(Integer, ForeignKey('users.id'), nullable=False)
