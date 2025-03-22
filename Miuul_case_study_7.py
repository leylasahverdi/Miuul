import scipy.stats as st
import numpy as np
import pandas as pd
import math
from sklearn.preprocessing import MinMaxScaler
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.expand_frame_repr', False)

df = pd.read_csv('DATA/amazon_review.csv')
df.info()
df['overall'].mean()
#4.58
df.loc[df['day_diff'] < 30, 'overall'].mean()
df.loc[(df['day_diff'] >= 30) & (df['day_diff'] < 60), 'overall'].mean()
df.loc[(df['day_diff'] >= 60) & (df['day_diff'] < 90), 'overall'].mean()
df.loc[(df['day_diff'] >= 90) & (df['day_diff'] < 120), 'overall'].mean()

def time_based_wa(df, var, t1 = 30 ,t2 = 60 ,t3 = 90, t4 = 120, p1 = 0.30, p2 = 0.40, p3 = 0.30, p4 = 0.20, p5 = 0.10):
    a = df.loc[df[var] < t1, var].mean()
    b = df.loc[(df[var] >= t1) & (df[var] < t2), var].mean()
    c = df.loc[(df[var] >= t2) & (df[var] < t3), var].mean()
    d = df.loc[(df[var] >= t3) & (df[var] < t4), var].mean()
    e = df.loc[df[var] >= t4, var].mean()
    return (a * p1) + (b * p2) + (c * p3) + (d * p4) + (e * p5)

def helpful_no(df, total_vote, helpful_yes, helpful_no):
    df[helpful_no] = df[total_vote] - df[helpful_yes]


helpful_no(df, 'total_vote', 'helpful_yes', 'helpful_no')


def wilson_lower_bound(up, down, confidence=0.95):
    """
    Wilson Lower Bound Score hesapla

    - Bernoulli parametresi p için hesaplanacak güven aralığının alt sınırı WLB skoru olarak kabul edilir.
    - Hesaplanacak skor ürün sıralaması için kullanılır.
    - Not:
    Eğer skorlar 1-5 arasıdaysa 1-3 negatif, 4-5 pozitif olarak işaretlenir ve bernoulli'ye uygun hale getirilebilir.
    Bu beraberinde bazı problemleri de getirir. Bu sebeple bayesian average rating yapmak gerekir.

    Parameters
    ----------
    up: int
        up count
    down: int
        down count
    confidence: float
        confidence

    Returns
    -------
    wilson score: float

    """
    n = up + down
    if n == 0:
        return 0
    z = st.norm.ppf(1 - (1 - confidence) / 2)
    phat = 1.0 * up / n
    return (phat + z * z / (2 * n) - z * math.sqrt((phat * (1 - phat) + z * z / (4 * n)) / n)) / (1 + z * z / n)

def score_pos_neg_diff(df):
    df['score_pos_neg_diff'] = df['helpful_yes']- df['helpful_no']
score_pos_neg_diff(df)
def score_average_rating(df):
    df['score_average_rating'] = df['helpful_yes']/df['total_vote']


df['wilson_score'] = df.apply(lambda row: wilson_lower_bound(row['helpful_yes'], row['helpful_no']), axis=1)