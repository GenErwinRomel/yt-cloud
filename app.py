'''
    This bullshit creates YouTube videos wordcloud for free
'''

from flask import *
app = Flask(__name__)

from word_cloud_gen import gen_wc
from youtube_get import get_sub

'https://www.youtube.com/watch?v=ubV-8EYzTyc'

@app.route('/', methods=['GET'])
def home_page():
    vid = 'ubV-8EYzTyc'
    my_html = f'''
    <h2>Home page at / </h2><br/>
    <a href="yt"><h2>Click for /yt</h2></a><br/>
    <a href="yt?id=1234"><h2>Click for 1234</h2></a><br/>
    <a href="yt?id=lXPF1i39AjM"><h2>Click for lXPF1i39AjM</h2></a><br/>
    '''
    res = get_sub(video_id=vid)
    if (res['status']):
        return send_file(gen_wc(video_id=vid), mimetype='image/png')

@app.route('/yt', methods=['GET'])
def free_this_article():
    try:
        wanted_url = request.args.to_dict()['id']
    except:
        return '/yt'
    return wanted_url

if __name__ == '__main__':
    # app.run(port=8000)
    app.run(port=5001, debug=True)