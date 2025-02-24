import os
from app import app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    print(f"Starting server at http://{host}:{port}")
    app.run(host=host, port=port)