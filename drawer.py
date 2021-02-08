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

    def _draw_word_cloud(self, frequecy, filename):
        self.word_cloud_drawer.fit_words(frequecy)
        self.word_cloud_drawer.to_file(os.path.join(self.save_path, filename))

    def draw_positive(self):
        self._draw_word_cloud(self.reader.get_freq_dist(self.reader.get_all_positive_id_notes_words()),
                              'positive_id_notes_words_cloud.jpg')
        self._draw_word_cloud(self.reader.get_freq_dist(self.reader.get_all_positive_id_comments_words()),
                              'positive_id_comments_words_cloud.jpg')

    def draw_negative(self):
        self._draw_word_cloud(self.reader.get_freq_dist(self.reader.get_all_negative_id_notes_words()),
                              'negative_id_notes_words_cloud.jpg')
        self._draw_word_cloud(self.reader.get_freq_dist(self.reader.get_all_negative_id_comments_words()),
                              'negative_id_comments_words_cloud.jpg')

    def draw_unprocessed(self):
        self._draw_word_cloud(self.reader.get_freq_dist(self.reader.get_all_unprocesssed_notes_words()),
                              'unprocessed_notes_words_cloud.jpg')

    def draw_unverified(self):
        self._draw_word_cloud(self.reader.get_freq_dist(self.reader.get_all_unverified_notes_words()),
                              'unverified_notes_words_cloud.jpg')
        self._draw_word_cloud(self.reader.get_freq_dist(self.reader.get_all_unverified_comments_words()),
                              'unverified_comments_words_cloud.jpg')

    def draw_all(self):
        self._draw_word_cloud(self.reader.get_freq_dist(self.reader.get_all_users_notes_words()),
                              'all_notes_words_cloud.jpg')
        self._draw_word_cloud(self.reader.get_freq_dist(self.reader.get_all_users_comments_words()),
                              'all_comments_words_cloud.jpg')


class WordFrequencyDrawer(BaseDrawer):
    reader = DrawWordsReader()
    task = 'word_frequecy'


    def _draw_words_frequency_bar(self, frequency_dict, filename):
        top10 = frequency_dict.most_common(10)
        x = [ele[0] for ele in top10]
        y = [ele[1] for ele in top10]
        _, ax = plt.subplots()
        ax.bar(x, y, width=0.4)
        plt.xticks(rotation=20)
        ax.set_title(filename.split('.')[0].replace('_', ' '))

        plt.savefig(os.path.join(self.save_path, filename))


    def draw_positive(self):
        self._draw_words_frequency_bar(
            self.reader.get_freq_dist(self.reader.get_all_positive_id_notes_words()),
            'positive_id_notes_words_frequency_histogram.jpg')
        self._draw_words_frequency_bar(
            self.reader.get_freq_dist(self.reader.get_all_positive_id_comments_words()),
            'positive_id_comments_words_frequency_histogram.jpg')

    def draw_negative(self):
        self._draw_words_frequency_bar(
            self.reader.get_freq_dist(self.reader.get_all_negative_id_notes_words()),
            'negative_id_notes_words_frequency_histogram.jpg')
        self._draw_words_frequency_bar(
            self.reader.get_freq_dist(self.reader.get_all_negative_id_comments_words()),
            'negative_id_comments_words_frequency_histogram.jpg')

    def draw_unprocessed(self):
        self._draw_words_frequency_bar(
            self.reader.get_freq_dist(self.reader.get_all_unprocesssed_notes_words()),
            'unprocessed_notes_words_frequency_histogram.jpg')

    def draw_unverified(self):
        self._draw_words_frequency_bar(
            self.reader.get_freq_dist(self.reader.get_all_unverified_notes_words()),
            'unverified_notes_words_frequency_histogram.jpg')
        self._draw_words_frequency_bar(
            self.reader.get_freq_dist(self.reader.get_all_unverified_comments_words()),
            'unverified_comments_words_frequency_histogram.jpg')

    def draw_all(self):
        self._draw_words_frequency_bar(
            self.reader.get_freq_dist(self.reader.get_all_users_notes_words()),
            'all_notes_words_frequency_histogram.jpg')
        self._draw_words_frequency_bar(
            self.reader.get_freq_dist(self.reader.get_all_users_comments_words()),
            'all_comments_words_frequency_histogram.jpg')
