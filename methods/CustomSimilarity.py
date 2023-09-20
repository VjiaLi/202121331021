# 正则包
import re
# 自然语言处理包
import jieba
import jieba.analyse
# html 包
import html
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class CustomSimilarity(object):
    """
    Weighted similarity using Euclidean and Cosine distance
    """

    def __init__(self, content_x1, content_y2, alpha):
        self.s1 = content_x1
        self.s2 = content_y2
        self.alpha = alpha

    @staticmethod
    def extract_keyword(content):
        re_exp = re.compile(r'(<style>.*?</style>)|(<[^>]+>)', re.S)
        content = re_exp.sub(' ', content)
        content = html.unescape(content)
        seg = [i for i in jieba.cut(content, cut_all=True) if i != '']
        keywords = jieba.analyse.extract_tags("|".join(seg), topK=200, withWeight=False)
        return keywords

    @staticmethod
    def one_hot(word_dict, keywords):
        cut_code = [0] * len(word_dict)
        for word in keywords:
            cut_code[word_dict[word]] += 1
        return cut_code

    def euclidean_distance(self, vec1, vec2):
        return np.linalg.norm(np.array(vec1) - np.array(vec2))

    def main(self):
        jieba.analyse.set_stop_words('./files/stopwords.txt')
        keywords1 = self.extract_keyword(self.s1)
        keywords2 = self.extract_keyword(self.s2)
        union = set(keywords1).union(set(keywords2))
        word_dict = {word: i for i, word in enumerate(union)}
        s1_cut_code = self.one_hot(word_dict, keywords1)
        s2_cut_code = self.one_hot(word_dict, keywords2)

        # Calculate Euclidean distance
        euclidean_dist = self.euclidean_distance(s1_cut_code, s2_cut_code)

        # Calculate Cosine similarity
        sample = [s1_cut_code, s2_cut_code]
        cosine_sim = cosine_similarity(sample)[1][0]
        # Calculate weighted similarity
        weighted_similarity = (self.alpha * (1 / (euclidean_dist + 1)) + (1 - self.alpha) * cosine_sim)

        return weighted_similarity
