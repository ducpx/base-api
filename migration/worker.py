from backend.common.constants import APP_ROOT_DIR


class MigrationWorker(object):

    def __init__(self, session):
        self.session = session
