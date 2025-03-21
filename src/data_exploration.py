import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\S580381\Documents\GitHub\marketing_camp_rev_pred\data\fb_ad_camps.csv')

#make age a numerical value
#make age the mean of the two values
#make interest cat as each number means a specific interest
#make gender cat

df['age_start'], df['age_end'] = zip(*df['age'].apply(lambda x: map(int, x.split('-'))))
df['age_start'] = df['age_start'].astype(int)
df['age_end'] = df['age_end'].astype(int)
df['age'] = ((df['age_start'] + df['age_end']) / 2).astype(int)

df['interest'] = df['interest'].astype('category')
df['gender'] = df['gender'].astype('category')

df.drop(columns=['age_start', 'age_end'], inplace=True)

#rename columns to be more readable
df.rename(columns={'ad_id': 'Ad_ID', 'xyz_campaign_id': 'Company_Campaign_ID', 'fb_campaign_id': 'FB_campaign_ID', 'age': 'Age', 'spent': 'Spent', 'impressions': 'Impressions', 'clicks': 'Clicks', 'gender': 'Gender'}, inplace=True)   

#clikc-through rate col
df['Ctr'] = df.apply(lambda x: x['Clicks'] / x['Impressions'] if x['Impressions'] != 0 else 0, axis=1) 

#cost per click col
df['Cpc'] = df.apply(lambda x: x['Spent'] / x['Clicks'] if x['Clicks'] != 0 else 0, axis=1)

#conversion rate col
df['Conversion_Rate'] = df.apply(lambda x: x['Total_Conversion'] / x['Clicks'] if x['Clicks'] != 0 else 0, axis=1) 

#cost per conversion col
df['Cpa'] = df.apply(lambda x: x['Spent'] / x['Total_Conversion'] if x['Total_Conversion'] != 0 else 0, axis=1)

print(df.head())
