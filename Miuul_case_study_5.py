#Customer segmentation with RFM analysis
import pandas as pd
import numpy as np
import datetime as dt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
pd.set_option('display.float_format', '{:,.2f}'.format)
pd.set_option('display.expand_frame_repr', True)
df = pd.read_csv('flo_data_20k.csv')
df.head()
df_copy = df.copy()
df.head(10)
df.columns  #df.info()
df.describe().T
df.isnull().sum()
df.info()
df['Total_order'] = df['order_num_total_ever_online'] + df['order_num_total_ever_offline']
df['Total_customer_value'] = df['customer_value_total_ever_offline'] + df['customer_value_total_ever_online']
df['first_order_date'] = pd.to_datetime(df['first_order_date'])
df['last_order_date'] = pd.to_datetime(df['last_order_date'])
df_order_channel = df.groupby('order_channel').agg({'master_id': lambda master_id: master_id.count(),
                                                    'Total_order': lambda Total_order: Total_order.sum(),
                                                    'Total_customer_value': lambda Total_customer_value : Total_customer_value.sum()})
df_order_channel.describe().T
df['Total_customer_value'].sort_values(ascending=False).head(10)
df.sort_values("Total_customer_value", ascending=False)[:10]
df.sort_values('Total_order', ascending=False)[:10]


def data_preparation(df):
    df['Total_order'] = df['order_num_total_ever_online'] + df['order_num_total_ever_offline']
    df['Total_customer_value'] = df['customer_value_total_ever_offline'] + df['customer_value_total_ever_online']
    df['first_order_date'] = pd.to_datetime(df['first_order_date'])
    df['last_order_date'] = pd.to_datetime(df['last_order_date'])
    return df.head(10)


import datetime as dt

today = dt.datetime(2021, 6, 1)
df['Recency'] = (today - df['last_order_date']).dt.days
df['Frequency'] = df['Total_order']
df['Monetary'] = df['Total_customer_value']
df['Recency_metrics'] = pd.qcut(df['Recency'].rank(method='first'), 5, labels=['5', '4', '3', '2', '1'])
df['Frequency_metrics'] = pd.qcut(df['Frequency'].rank(method='first'), 5, labels=['1', '2', '3', '4', '5'])
df['Monetary_metrics'] = pd.qcut(df['Monetary'].rank(method='first'), 5, labels=['1', '2', '3', '4', '5'])
df['RFM_score'] = df['Recency_metrics'].astype(str) + df['Frequency_metrics'].astype(str) + df[
    'Monetary_metrics'].astype(str)
a = ['Recency_metrics', 'Frequency_metrics', 'Monetary_metrics', 'RFM_score']
rfm = df.loc[:,
      ['Recency', 'Frequency', 'Monetary', 'Recency_metrics', 'Frequency_metrics', 'Monetary_metrics', 'RFM_score']]
seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_Risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalists',
    r'5[4-5]': 'champions'
}
df["RF_SCORE"] = (df['Recency_metrics'].astype(str) + df['Frequency_metrics'].astype(str))
df['segment'] = df['RF_SCORE'].replace(seg_map, regex=True)
rfm_1 = df.loc[(df['segment'].isin(['champions', 'loyal_customers'])) & (df['interested_in_categories_12'].str.contains('KADIN', na=False)), 'master_id']
rfm_1.to_csv('indirim_uygulanacak_kadın_şampiyon_ve_sadık', index=False)
var = df.loc[(df['segment'].isin(['hibernating', 'new_customers', 'cant_loose'])) & ((df["interested_in_categories_12"].str.contains('ERKEK')) & (df['interested_in_categories_12'].str.contains('COCUK'))), "master_id"]
var.to_csv('erkek_ve_çocuk_ürünleri', index=False)