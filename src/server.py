import time
import markdown
import json
import jsonpickle
import markdown.extensions.fenced_code
import markdown.extensions.codehilite
from pygments.formatters import HtmlFormatter   
import os
from flask import Flask, request, jsonify, send_file, Response

app = Flask(__name__)
port = int(os.environ.get('PORT', 5000))

def answer(content, status):
    if(status != 200):
        content = { 'error': content }
    return jsonify(content), status

@app.route('/', methods=['GET'])
def info():
    readme_file = open('README.md', 'r')
    md_template_string = markdown.markdown(readme_file.read(), extensions=['fenced_code','codehilite'])
    formatter = HtmlFormatter(style='emacs', full=True, cssclass='codehilite')
    css_string = formatter.get_style_defs()
    md_css_string = '<style>' + css_string + '</style>'
    md_template = md_css_string + md_template_string
    return md_template

@app.route('/resource', methods=['POST'])
def post():
    if (not request.data):
        return answer('No request contents', 400)
    if (not request.is_json):
        return answer('Request content not in JSON format', 400)
    try:
        json_object = jsonpickle.decode(request.data)
    except ValueError as e:
        return answer('Request format not in valid JSON: ' + e, 400)
    content = request.get_json();
    return answer('You make a new resource creation request: ' + json.dumps(content), 200)

@app.route('/resource/<id>', methods=['GET'])
def get(id):
    return answer('You make a new resource reading request: ' + id, 200)

@app.route('/resource/<id>', methods=['DELETE'])
def delete(id):
    return answer('You make a new resource delete request: ' + id, 200)

@app.route('/resource/<id>', methods=['PUT'])
def put(id):
    if (not request.data):
        return answer('No request contents', 400)
    if (not request.is_json):
        return answer('Request content not in JSON format', 400)
    try:
        json_object = jsonpickle.decode(request.data)
    except ValueError as e:
        return answer('Request format not in valid JSON: ' + e, 400)
    content = request.get_json();
    return answer('You make a new resource modify request: ' + id + ' - ' + json.dumps(content), 200)

@app.errorhandler(404)
def notfound(error):
    return answer('Route not found', 404)  

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)