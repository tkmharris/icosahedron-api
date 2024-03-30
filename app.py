"""
Simple Flask server to serve STL files for stellated icosahedra.
"""
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/<icosahedron_id>')
def serve_stl(icosahedron_id):
    """
    Serve STL file for stellated icosahedron with given id.
    """
    file_path = f"stl/icosahedra/{icosahedron_id}.stl"
    return send_file(file_path, mimetype='model/stl')

if __name__ == '__main__':
    app.run(debug=True)
