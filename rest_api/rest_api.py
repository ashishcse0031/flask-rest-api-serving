from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/print_filename", methods=['POST','PUT'])
def print_filename():
    file = request.files['file']
    filename=secure_filename(file.filename)   
    return filename



@app.route("/get_transcript", methods=['POST','PUT'])
def get_transcript():
    file = request.files['file']
    filename=secure_filename(file.filename)   

    #cmd = 'python recognize.py --file  file'
    print(type(file))
    return 'hellpo'


@app.route('/asr', methods=['GET', 'POST'])
def asr():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save('./files/' + filename)
            file.save(filename)
            file.save(filename + filename)
            print('saved sucessfully!')
            #python recognize.py --file asset/data/LibriSpeech/test-clean/1089/134686/1089-134686-0000.flac

            os.system('rm  ' + filename)

    return 'done!'


if __name__=="__main__":
    app.run(port=6969, debug=True)


