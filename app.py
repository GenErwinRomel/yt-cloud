'''
    This bullshit creates YouTube videos wordcloud for free
'''

from flask import *
app = Flask(__name__)

from word_cloud_gen import gen_wc
from youtube_get import get_sub

@app.route('/', methods=['GET'])
def home_page():
    # Test Video: 'https://www.youtube.com/watch?v=ubV-8EYzTyc'
    vid = 'ubV-8EYzTyc'
    res = get_sub(video_id=vid)
    if (res['status']):
        return send_file(gen_wc(video_id=vid), mimetype='image/png')

@app.route('/yt', methods=['GET'])
def free_this_article():
    try:
        vid = request.args.to_dict()['id']
    except:
        return '/yt'
    
    res = get_sub(video_id=vid)
    if (res['status']):
        return send_file(gen_wc(video_id=vid), mimetype='image/png')

if __name__ == '__main__':
    # app.run(port=8000)
    app.run(port=5001, debug=True)