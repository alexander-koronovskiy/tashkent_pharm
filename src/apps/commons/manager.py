class ManagesBase:
    def __init__(self, session):
        self.session = session

    def execute(self, query):
        self.session.execute(query)

    def create(self, instance):
        self.session.add(instance)
        self.session.commit()
        return instance

    def update(self, instance, data_update: dict):
        for field in data_update.keys():
            setattr(instance, field, data_update.get(field))
        self.session.add(instance)
        self.session.commit()
        return instance

    def delete(self, instance):
        self.session.delete(instance)
        self.session.commit()
        return instance
