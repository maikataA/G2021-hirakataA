import os
import librosa
import numpy as np
from numpy import random
import pickle
import sys


class Noise_detection_AI(object):

    def __init__(self):
        # 学習結果読み込み
        self.base_path = os.path.dirname(__file__)
        self.open_path = os.path.join(self.base_path, 'save_AI/model_main.pickle')
        with open(self.open_path, mode='rb') as f:
            self.model = pickle.load(f)


    def jdg_start(self, data):

        data = np.array(data)
        data = data / data.max()

        start = random.randint(0, len(data) -  22144 - 1)
        data = data[start:start +  22144]

        tmp = []
        melspec = librosa.feature.melspectrogram(data, 44100)
        melspec = librosa.amplitude_to_db(melspec).flatten()
        melspec = data.astype(np.float16)
        mean = np.sqrt(np.mean(data**2))
        zc = np.sum(librosa.zero_crossings(data))
        test_feature = [np.append(np.append(np.append(tmp, mean), zc), melspec) for _ in range(1)]

        pred = self.model(test_feature)
        return pred
