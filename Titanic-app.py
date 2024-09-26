# %%
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 显示标题
st.markdown('<h1 style="font-size:24px; font-weight:bold;">Titanic App by JIN YAN</h1>', unsafe_allow_html=True)

# 读取Titanic数据集
df = pd.read_csv('train.csv')

# 显示数据集
st.write(df)

# 创建三个子图的图形
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 绘制不同等级的箱图
for i, pclass in enumerate([1, 2, 3]):
    sns.boxplot(x='Pclass', y='Fare', data=df[df['Pclass'] == pclass], ax=axes[i], width=0.2)
    axes[i].set_xlabel(f'PClass={pclass}')
    axes[i].set_ylabel('')
    axes[i].set_xticks([0])
    axes[i].set_xticklabels(['Fare'])
    axes[i].grid(True)

# 调整布局
plt.tight_layout()

# 在Streamlit中显示图形
st.pyplot(fig)




