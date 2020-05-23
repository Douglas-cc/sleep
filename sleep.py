import numpy as np
import pandas as pd
import altair as alt
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt

@st.cache(suppress_st_warning=True)
def criar_histograma(coluna, df):
    chart = alt.Chart(df, width=600).mark_bar().encode(
        alt.X(coluna, bin=True),
        y = 'count()', tooltip=[coluna, 'count()']
    ).interactive()
    return chart

@st.cache(suppress_st_warning=True)
def criar_barras(coluna_num, coluna_cat, df):
    bars = alt.Chart(df, width = 600).mark_bar().encode(
        x = alt.X(coluna_num, stack='zero'),
        y = alt.Y(coluna_cat),
        tooltip = [coluna_cat, coluna_num]
    ).interactive()
    return bars

@st.cache(suppress_st_warning=True)
def criar_scatterplot(x, y, color, df):
    scatter = alt.Chart(df, width=800, height=400).mark_circle().encode(
        alt.X(x),
        alt.Y(y),
        color = color,
        tooltip = [x, y]
    ).interactive()
    return scatter

def calcula_corr(col_x, col_y, df):
    resposta = df[col_x].corr(df[col_y])
    return round(resposta,2)

def main():
    st.image('sono.jpg', width = 695)
    st.title('Analyze Data')
    st.subheader('Data Base')    
    df = pd.read_csv('tratado.csv')
    df = df.drop(columns=['Unnamed: 0'])
    st.dataframe(df)
    if df is not None:
        st.subheader('Univariate descriptive statistics')
        aux = pd.DataFrame({"columns": df.columns, 'types': df.dtypes})
        colunas_numericas = list(aux[aux['types'] != 'object']['columns'])
        colunas_object = list(aux[aux['types'] == 'object']['columns'])
        colunas = list(df.columns)
        col = st.selectbox('Select the column: ', colunas_numericas)
        if col is not None:
            st.markdown('Select what you want to analyze:')
            
            mean = st.checkbox('Mean')
            if mean:
                st.markdown(df[col].mean())
            
            median = st.checkbox('Median')
            if median:
                st.markdown(df[col].median())
            
            desvio_pad = st.checkbox('Standard deviation')
            if desvio_pad:
                st.markdown(df[col].std())
            
            kurtosis = st.checkbox('Kurtosis')
            if kurtosis:
                st.markdown(df[col].kurtosis())
            
            skewness = st.checkbox('Skewness')
            if skewness:
                st.markdown(df[col].skew())
            
            describe = st.checkbox('Describe')
            if describe:
                st.table(df[colunas_numericas].describe().transpose())
       
        st.subheader('Data visualization')
        st.image('https://media.giphy.com/media/Rkoat5KMaw2aOHDduz/giphy.gif', width=200)
        st.markdown('Select the view')
       
        histograma = st.checkbox('Histogram')
        if histograma:
            col_num = st.selectbox('Select the numeric column: ', colunas_numericas,key = 'unique')
            st.markdown('Spine histogram : ' + str(col_num))
            st.write(criar_histograma(col_num, df))
       
        barras = st.checkbox('Bar chart')
        if barras:
            col_num_barras = st.selectbox('Select the numeric column: ', colunas_numericas, key = 'unique')
            col_cat_barras = st.selectbox('Select the categorical column ', colunas_object, key = 'unique')
            st.markdown('Column bar chart' + str(col_cat_barras) + ' by the column ' + col_num_barras)
            st.write(criar_barras(col_num_barras, col_cat_barras, df))
       
        scatter = st.checkbox('Scatterplot')
        if scatter:
            col_num_x = st.selectbox('Select the value of x', colunas_numericas, key = 'unique')
            col_num_y = st.selectbox('Select the value of y ', colunas_numericas, key = 'unique')
            col_color = st.selectbox('Select column for color', colunas)
            st.markdown('Select the x and y values')
            st.write(criar_scatterplot(col_num_x, col_num_y, col_color, df))
       
        correlacao = st.checkbox('Correlation')
        if correlacao:
            st.markdown('HeatMap')
            fig,ax = plt.subplots(figsize = (35,35))
            mask = np.zeros_like(df.corr(), dtype = np.bool)
            mask[np.triu_indices_from(mask)]=True
            sns.heatmap(df.corr().round(2),mask=mask ,annot= True, ax=ax)
            st.pyplot()

        corre_duple = st.checkbox('Calculate the correlation between two Variables')
        if corre_duple:
            col_x = st.selectbox('Select a column ', colunas_numericas, key = 'unique')
            col_y = st.selectbox('Select another column ', colunas_numericas, key = 'unique')
            st.markdown('Correlation between the selected variables')
            st.write(calcula_corr(col_x, col_y, df))

if __name__ == '__main__':
    main()