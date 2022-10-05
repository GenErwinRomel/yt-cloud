import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np
import base64


def gen_wc(video_id: str):
    with open(f'tmp/{video_id}/{video_id}.txt') as seed:
        lines = seed.readlines()
    seed = "".join(lines).replace('\n', ' ')
    word_cloud =  WordCloud(
        # background_color='#C3352E', collocations=False, random_state=3,
        # width=500, height=500, 
        # contour_color='steelblue',
        # contour_width=3, contour_color='steelblue',
        background_color='white',
        max_words=80,
        normalize_plurals=True,
        stopwords=STOPWORDS , mask=np.array(Image.open('masks/ghalb.jpg'))
    ).generate(seed)
    res = word_cloud.to_file(f'tmp/{video_id}/wc.png')

    return f'tmp/{video_id}/wc.png'
    #return word_cloud.to_array()