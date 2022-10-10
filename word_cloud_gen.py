import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np
import base64


def gen_wc(video_id: str, mask_name: str = 'none', stopwords: str = ''):
    with open(f'tmp/{video_id}/{video_id}.txt') as seed:
        lines = seed.readlines()
    seed = "".join(lines).replace('\n', ' ')
    stopwords = set(stopwords.split(','))
    stopwords.update(STOPWORDS)
    word_cloud =  WordCloud(
        width=500, height=500, 
        background_color='white',
        max_words=80,
        normalize_plurals=True,
        stopwords=stopwords,
        mask=np.array(Image.open(f'masks/{mask_name}.jpg'))
    ).generate(seed)
    res = word_cloud.to_file(f'tmp/{video_id}/wc.png')

    return f'tmp/{video_id}/wc.png'