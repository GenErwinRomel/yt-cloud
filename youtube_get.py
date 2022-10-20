import youtube_dl
import os
bad_words = ['-->','</c>'] 

video_id = '0YP4n9G0qtQ'

def get_sub(video_id: str = '0YP4n9G0qtQ'):
    ydl_opts = {
        #'proxy': 'socks5://localhost:5008',
        'writeautomaticsub': True,
        'writesubtitles': True,
        'skip_download': True,
        'outtmpl': "tmp/%(id)s/%(id)s",
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        status = ydl.download([f'https://www.youtube.com/watch?v={video_id}'])

    with open(f'tmp/{video_id}/{video_id}.en.vtt') as oldfile, open(f'tmp/{video_id}/{video_id}.txt', 'w') as newfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in bad_words):
                newfile.write(line)
    try:
        os.remove(f'tmp/{video_id}/{video_id}.en.vtt')
    except:
        print(f'Cannot remove tmp/{video_id}/{video_id}.en.vtt')
    return {
        'status': True, 'where': f'tmp/{video_id}/{video_id}.txt', 'video_id': video_id,
    }
