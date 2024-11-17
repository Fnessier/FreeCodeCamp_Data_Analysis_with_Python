import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['overweight'] = ((df['weight']/(df['height']/100)**2)>25).astype(int)
#3
df[['gluc','cholesterol']]= (df[['gluc','cholesterol']]>1).astype(int)
# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])


    # 6
    df_cat_count = df_cat.value_counts()
    #df_cat_count.rename(columns = {'': 'count'}, inplace=True)
    print(df_cat_count)

    # 7


    # 8
    fig = sns.catplot(data = df_cat, kind='count',  x='variable', hue='value', col='cardio').set(ylabel = 'total').fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi'])&
    (df['height'] >= df['height'].quantile(0.025))&
    (df['height'] >= df['height'].quantile(0.975))&
    (df['weight'] >= df['weight'].quantile(0.025))&
    (df['weight'] >= df['weight'].quantile(0.025))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(corr)

    # 14
    fig, ax = plt.subplots()

    # 15
    ax = sns.heatmap(corr, mask= mask, annot=True, square=True, fmt='0.1f')

    # 16
    fig.savefig('heatmap.png')
    return fig
