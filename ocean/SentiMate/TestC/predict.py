from django.conf import settings
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import backend as K
import pandas as pd
import numpy as np
import os


def model_predict(posts, length):
    model_path = os.path.join(settings.BASE_DIR, 'SentiMate/TestC/models/')
    ocean = [0, 0, 0, 0, 0]
    models = ['O', 'C', 'E', 'A', 'N']
    for i in tf.range(5):
        K.clear_session()
        model = keras.models.load_model(model_path+'{}Model'.format(models[i]), compile=False)
        x = model.predict(posts)
        x = np.argmax(x, axis = 1)
        ocean[i] = np.round(np.sum(x)/length,2)*100
    return ocean


def predict():
    csv_path = os.path.join(settings.BASE_DIR, 'SentiMate/TestC/file.csv')
    posts = pd.read_csv(csv_path)
    length = posts.shape[1]
    if length > 10:
        length = 10
        posts = posts.head(10)
    posts = posts[posts.columns[1]]
    ocean = model_predict(posts, length)
    return ocean
    