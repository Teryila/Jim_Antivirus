from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        # Add your file processing logic here
        return 'File successfully uploaded and scanned'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

