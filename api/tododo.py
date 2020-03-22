from app import api, db


@api.shell_context_processor
def make_shell_context():
    return {'db': db}
