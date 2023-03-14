class ManagesBase:
    def __init__(self, session):
        self.session = session

    def execute(self, query):
        self.session.execute(query)

    def create(self, instance):
        self.session.add(instance)

    def update(self, instance):
        self.session.add(instance)

    def delete(self, instance):
        self.session.delete(instance)
