import os

BASE_DIR = os.path.dirname(__file__)

DATASET_DIR = os.path.join(os.path.join(BASE_DIR, 'data'), '2021MCMProblemC_DataSet.xlsx')
IMAGES_BY_GLOBALID_DIR = os.path.join(os.path.join(BASE_DIR, 'data'), '2021MCM_ProblemC_ Images_by_GlobalID.xlsx')

RESOURCE_DIR = os.path.join(BASE_DIR, 'resource')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

MY_STOP_WORDS = [
            'I', 'It', "'s", 'long', 'picture', 'saw', 'one', 'get',
            'like', 'hornet', "'", 'sure', 'seen', '.', ',', '’',
            'we', '2', "n't", 'found', 'looked', 'flew', 'around',
            'asian', 'suspect', 'back', 'area', 'ski', 'sent', 'leavenworth',
            'today', 'specimen', 'live', 'nearby', 'wa', 'big', '!', '！',
            'thanks', 'wood', 'great', 'golden'
        ]
