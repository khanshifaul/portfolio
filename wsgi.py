from app import create_app
from app.models import Message

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'Message': message}