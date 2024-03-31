"""
Simple Flask server to serve STL files for stellated icosahedra.
"""
from flask import Flask, send_file
from models import Icosahedron

app = Flask(__name__)

@app.route('/<icosahedron_id>')
def serve_icosahedron_stl(icosahedron_id):
    """
    Serve STL file for stellated icosahedron with given id.
    """
    file_path = Icosahedron.find(icosahedron_id)
    if file_path is None:
        return "Icosahedron not found", 404
    return send_file(file_path, mimetype='model/stl')

@app.route('/random')
def serve_random_icosahedron_stl():
    """
    Serve STL file for a random stellated icosahedron.
    """
    file_path = Icosahedron.random()
    return send_file(file_path, mimetype='model/stl')

if __name__ == '__main__':
    app.run(debug=True)
