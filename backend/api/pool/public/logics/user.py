from backend.api.factory.base_logics import BaseLogic


class UserLogic(BaseLogic):

    # def get(self, machine_id):
    #
    #     return {'message': machine_id}

    def post(self, machine_id, id):
        print('Create directory in machine_id:', machine_id)
        return {'message': id}
