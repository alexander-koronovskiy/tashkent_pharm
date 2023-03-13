class MixinMarkChanges:
    created_at = Column(Datetime, server_default=func.now()) # ref
    updaded_at = Column(Datetime, server_default=func.now(), onupdate=func.now()) # ref
    # created_by
    # updated_by
    is_deleted = Column(Boolean, default=False)
