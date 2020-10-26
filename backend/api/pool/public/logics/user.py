from backend.api.factory.base_logics import BaseLogic
from backend.databases.postgres import User


class UserLogic(BaseLogic):

    def get(self):
        users = self.session.query(User).all()
        for u in users:
            print(u.id)
        return {'message user logic was called': 1}

    def post(self, name):
        user = User()
        user.name = name
        self.session.add(user)
        self.session.commit()
        return {'user.id': user.id}
