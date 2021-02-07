import os

import wordcloud
import matplotlib.pyplot as plt

import configs
from reader import DrawWordsReader


class BaseDrawer:
    reader = None
    task = None

    @property
    def save_path(self):
        if not self.task:
            return

        save_path = os.path.join(os.path.join(
            os.path.join(configs.OUTPUT_DIR, 'text_processing'),
            self.task))
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        return save_path


class WordCloudDrawer(BaseDrawer):
    reader = DrawWordsReader()
    task = 'word_cloud'

    def __init__(self):
        self.word_cloud_drawer = wordcloud.WordCloud(width=600, height=600,
                                                     max_words=2000,  max_font_size=40,
                                                     random_state=42, relative_scaling=0)

    def draw_positive(self):
        self.word_cloud_drawer.fit_words(
            self.reader.get_freq_dist(self.reader.get_all_positive_id_words()))
        plt.imshow(self.word_cloud_drawer)
        plt.show()
        self.word_cloud_drawer.to_file(os.path.join(self.save_path, 'positive_id_words_cloud.jpg'))

    def draw_negative(self):
        self.word_cloud_drawer.fit_words(
            self.reader.get_freq_dist(self.reader.get_all_negative_id_words()))
        plt.imshow(self.word_cloud_drawer)
        plt.show()
        self.word_cloud_drawer.to_file(os.path.join(self.save_path, 'negative_id_words_cloud.jpg'))

    def draw_unprocessed(self):
        self.word_cloud_drawer.fit_words(
            self.reader.get_freq_dist(self.reader.get_all_unprocesssed_words()))
        plt.imshow(self.word_cloud_drawer)
        plt.show()
        self.word_cloud_drawer.to_file(os.path.join(self.save_path, 'unprocessed_words_cloud.jpg'))

    def draw_unverified(self):
        self.word_cloud_drawer.fit_words(
            self.reader.get_freq_dist(self.reader.get_all_unverified_words()))
        plt.imshow(self.word_cloud_drawer)
        plt.show()
        self.word_cloud_drawer.to_file(os.path.join(self.save_path, 'unverified_words_cloud.jpg'))

    def draw_all(self):
        self.word_cloud_drawer.fit_words(
            self.reader.get_freq_dist(self.reader.get_all_users_words()))
        plt.imshow(self.word_cloud_drawer)
        plt.show()
        self.word_cloud_drawer.to_file(os.path.join(self.save_path, 'all_words_cloud.jpg'))


class WordFrequencyDrawer(BaseDrawer):
    reader = DrawWordsReader()
    task = 'word_frequecy'

    def __init__(self):
        pass




