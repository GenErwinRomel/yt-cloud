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
    vid = request.args['id']
    selected_mask = request.args['mask']
    # selected_mask = 'ghalb'
    print(selected_mask)
    res = get_sub(video_id=vid)
    if (res['status']):
        return send_file(gen_wc(video_id=vid, mask_name=selected_mask), mimetype='image/png')
    return redirect('/yt/create')

@app.route('/yt', methods=['GET'])
def free_this_article():
    '''
    vid = request.args['id']
    selected_mask = request.args['mask']
    print(selected_mask)
    res = get_sub(video_id=vid)
    if (res['status']):
        return send_file(gen_wc(video_id=vid, mask_name=selected_mask), mimetype='image/png')
    '''
    try:
        vid = request.args['id']
        selected_mask = request.args['mask']
        print(selected_mask)
        res = get_sub(video_id=vid)
        if (res['status']):
            return send_file(gen_wc(video_id=vid, mask_name=selected_mask), mimetype='image/png')
    except:
        return 'wtf'
        #return redirect('/yt/create')
        
@app.route('/yt/create')
def yt_mask():
    maks = fetch_masks()
    # return render_template()
    return render_template('mask.html', masks= maks)

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