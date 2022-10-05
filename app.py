'''
    This bullshit creates YouTube videos wordcloud for free
'''

from flask import *
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    return '/'

@app.route('/yt', methods=['GET'])
def free_this_article():
    try:
        wanted_url = request.args.to_dict()['id']
    except:
        return redirect('/', code=302)
    return wanted_url


if __name__ == '__main__':
    import random, hashlib, validators, urllib.parse, requests
    # app.run(port=8000)
    app.run(port=5001, debug=True)