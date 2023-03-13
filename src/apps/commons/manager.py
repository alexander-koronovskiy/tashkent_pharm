class ManagesBase:
    def __init__(self, session):
        self.session = session

    def execute(self, query):
        self.session.execute(query)

    def create(self, ):
        pass

    def update(self, ):
        pass

    def delete(self, ):
        pass
