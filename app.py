'''
    This bullshit creates YouTube videos wordcloud for free
'''

from flask import *
app = Flask(__name__)

from word_cloud_gen import gen_wc
from youtube_get import get_sub

@app.route('/', methods=['GET'])
def home_page():
    return redirect('/yt/create')

@app.route('/yt', methods=['GET'])
def free_this_article():
    try:
        vid = request.args.to_dict()['id']
        res = get_sub(video_id=vid)
        if (res['status']):
            return send_file(gen_wc(video_id=vid), mimetype='image/png')
    except:
        return redirect('/yt/create')
        
@app.route('/yt/create')
def yt_mask():
    return render_template('mask.html')

@app.route('/yt/test', methods=['GET'])
def home_page_test():
    # Test Video: 'https://www.youtube.com/watch?v=ubV-8EYzTyc'
    vid = 'ubV-8EYzTyc'
    res = get_sub(video_id=vid)
    if (res['status']):
        return send_file(gen_wc(video_id=vid), mimetype='image/png')
    
if __name__ == '__main__':
    # app.run(port=8000)
    app.run(port=5001, debug=True)