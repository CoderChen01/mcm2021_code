import nltk
from nltk.corpus import stopwords
import pandas as pd

import configs


class BaseDataReader:
    @property
    def dataset(self):
        dataset = pd.read_excel(configs.DATASET_DIR)  # read dataset from xlsx

        # convert null to '#'
        dataset.fillna('#')
        dataset.loc[dataset[dataset['Notes'] == ' '].index, 'Notes'] = '#'
        dataset.loc[dataset[dataset['Lab Comments'] == ' '].index, 'Lab Comments'] = '#'

        return dataset

    @property
    def images_by_globalid(self):
        images_by_globalid = pd.read_excel(configs.IMAGES_BY_GLOBALID_DIR)
        return images_by_globalid

    @property
    def positive_data(self):
        return self.dataset[self.dataset['Lab Status'] == 'Positive ID']

    @property
    def negative_data(self):
        return self.dataset[self.dataset['Lab Status'] == 'Negative ID']

    @property
    def unprocessed_data(self):
        return self.dataset[self.dataset['Lab Status'] == 'Unprocessed']

    @property
    def unverified_data(self):
        return self.dataset[self.dataset['Lab Status'] == 'Unverified']

    def get_column_data(self, column_name):
        """
        get any columen data in dataset
        :param column_name: column name
        :return: DataFrame
        """
        column_names = ('GlobalID', 'Detection Date', 'Notes', 'Lab Status', 'Lab Comments',
           'Submission Date', 'Latitude', 'Longitude')

        if column_name not in column_names:
            return

        return self.dataset[column_name]

    def get_image_file_info(self, globalid):
        """
        get image file info from images by global id file
        :param globalid: global id column in dataset
        :return: DataFrame
        """
        return self.images_by_globalid[self.images_by_globalid['GlobalID'] == globalid]


class DrawWordsReader(BaseDataReader):
    def __init__(self):
        self.stopwords = stopwords.words('english')
        mystopwords = [
            'I', 'It', "'s", 'long', 'picture', 'saw', 'one', 'get',
            'like', 'hornet', "'", 'sure', 'seen', '.', ',', '’',
            'we', '2', "n't", 'found', 'looked', 'flew', 'around',
            'asian', 'suspect', 'back', 'area', 'ski', 'sent', 'leavenworth',
            'today', 'specimen', 'live', 'nearby', 'wa', 'big'
        ]
        for w in mystopwords:
            self.stopwords.append(w)

    def _get_words(self, dataframe):
        words = []
        notes = dataframe['Notes']

        for note in notes:
            if note == '#':
                continue
            sents = nltk.sent_tokenize(str(note))
            for sent in sents:
                words.extend(nltk.word_tokenize(sent.lower()))

        return [word for word in words if word not in self.stopwords]

    def get_all_positive_id_words(self):
        return self._get_words(self.positive_data)

    def get_all_negative_id_words(self):
        return self._get_words(self.negative_data)

    def get_all_unprocesssed_words(self):
        return self._get_words(self.unprocessed_data)

    def get_all_unverified_words(self):
        return self._get_words(self.unverified_data)

    def get_all_users_words(self):
        return self._get_words(self.dataset)

    @staticmethod
    def get_freq_dist(words):
        return nltk.FreqDist(words)
