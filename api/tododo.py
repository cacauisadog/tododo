from app import create_app, db

api = create_app()


@api.shell_context_processor
def make_shell_context():
    return {'db': db}


if __name__ == '__main__':
    api.run(debug=True, use_debugger=False, use_reloader=True, passthrough_errors=True)
