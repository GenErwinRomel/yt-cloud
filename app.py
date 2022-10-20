'''
    This bullshit creates YouTube videos wordcloud for free
'''

from flask import *
app = Flask(__name__)

from word_cloud_gen import gen_wc
from youtube_get import get_sub
from masks import fetch_masks

@app.route('/', methods=['GET'])
def home_page():
    return redirect('/yt/create')

@app.route('/yt', methods=['GET'])
def rout_yt():
    try:
        vid = request.args['id']
        selected_mask = request.args['mask']
        stopwords = request.args['stopwords']
        if (get_sub(video_id=vid)['status']):
            return send_file(gen_wc(video_id=vid, mask_name=selected_mask, stopwords=stopwords), mimetype='image/png')
    except Exception as err:
        return f'wtf<br/>{err}'
        
@app.route('/yt/create')
def yt_create():
    return render_template('mask.html', masks = fetch_masks())

@app.route('/yt/test', methods=['GET'])
def home_page_test():
    # Test Video: 'https://www.youtube.com/watch?v=ubV-8EYzTyc'
    vid = 'ubV-8EYzTyc'
    res = get_sub(video_id=vid)
    if (res['status']):
        return send_file(gen_wc(video_id=vid), mimetype='image/png')
    
if __name__ == '__main__':
    app.run(port=8000)
