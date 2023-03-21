from datetime import datetime


class MixinMarkChanges:
    created_at: datetime
    updated_at: datetime
    is_deleted: bool
    created_by: int
    updated_by: int
