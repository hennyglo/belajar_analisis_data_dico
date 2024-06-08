import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
from datetime import datetime, timedelta

sns.set(style='dark')

day_df = pd.read_csv("day.csv")

# Mendapatkan tanggal sekarang
current_date = datetime.now().date()

# Mendefinisikan rentang waktu, misalnya dari 1 Januari 2011 hingga 31 Desember 2012
start_date = datetime(2011, 1, 1).date()
end_date = datetime(2012, 12, 31).date()
    
    # Mengambil start_date & end_date dari date_input
    selected_dates = st.date_input(
        label='Rentang Waktu',
        min_value=start_date,
        max_value=end_date,
        value=[start_date, end_date]
    )
    
st.header('Bike Share Dashboard :sparkles:')

st.markdown('### Jumlah Sewa Sepeda Berdasarkan Musim, Cuaca, Suhu, dan Suhu Terasa')
# Membagi layar menjadi dua kolom untuk musim dan cuaca
col1, col2 = st.columns(2)

# Scatter plot untuk Musim
with col1:
    season_mapping = {1: 'Springer', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    day_df['season_name'] = day_df['season'].map(season_mapping)
    fig = px.bar(day_df, x='season_name', y='cnt', title='Rata-rata Jumlah Sewa Sepeda Berdasarkan Musim')
    st.plotly_chart(fig)

# Scatter plot untuk Kondisi Cuaca
with col2:
    weathersit_mapping = {1: 'Few clouds', 2: 'Mist', 3: 'Light Snow', 4: 'Snow + Fog'}
    day_df['weathersit_name'] = day_df['weathersit'].map(weathersit_mapping)
    fig = px.bar(day_df, x='weathersit_name', y='cnt', title='Rata-rata Jumlah Sewa Sepeda Berdasarkan Kondisi Cuaca')
    st.plotly_chart(fig)

# Membagi layar menjadi dua kolom untuk suhu dan suhu terasa
col1, col2 = st.columns(2)

# Scatter plot untuk Suhu
with col1:
    sample_df = day_df.sample(10)
    fig = px.bar(sample_df, x='temp', y='cnt', title='Rata-rata Jumlah Sewa Sepeda Berdasarkan Suhu')
    st.plotly_chart(fig)

# Scatter plot untuk Suhu Terasa
with col2:
    sample_df = day_df.sample(10)
    fig = px.bar(sample_df, x='atemp', y='cnt', title='Rata-rata Jumlah Sewa Sepeda Berdasarkan Suhu Terasa')
    st.plotly_chart(fig)

st.markdown('### Korelasi antara Jumlah Sepeda Sewaan dengan Suhu, Kelembaban, dan Kecepatan Angin')
# Membagi layar menjadi dua kolom untuk suhu dan kelembaban
col1, col2 = st.columns(2)

# Scatter plot untuk Korelasi Suhu vs Jumlah Sewa Sepeda
with col1:
    fig = px.scatter(day_df, x='temp', y='cnt', title='Korelasi Suhu vs Jumlah Sewa Sepeda')
    st.plotly_chart(fig)

# Scatter plot untuk Korelasi Kelembaban vs Jumlah Sewa Sepeda
with col2:
    fig = px.scatter(day_df, x='hum', y='cnt', title='Korelasi Kelembaban vs Jumlah Sewa Sepeda')
    st.plotly_chart(fig)

# Scatter plot untuk Korelasi Kecepatan Angin vs Jumlah Sewa Sepeda
col1, = st.columns(1)
with col1:
    fig = px.scatter(day_df, x='windspeed', y='cnt', title='Korelasi Kecepatan Angin vs Jumlah Sewa Sepeda')
    st.plotly_chart(fig)

st.markdown('### Jumlah Sewa Sepeda Selama Dua Tahun Terakhir')
# Membagi layar menjadi dua kolom untuk hari dan bulan
col1, col2 = st.columns(2)

# Scatter plot untuk Jumlah Sewa Sepeda Berdasarkan hari dan bulan
with col1:
    weekday_mapping = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
    day_df['weekday_name'] = day_df['weekday'].map(weekday_mapping)
    fig = px.bar(day_df, x='weekday_name', y='cnt', title='Rata-rata Jumlah Sewa Sepeda Setiap Harinya')
    st.plotly_chart(fig)

with col2:
    month_mapping = {
        1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
        7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'
    }
    day_df['month_name'] = day_df['mnth'].map(month_mapping)
    fig = px.bar(day_df, x='month_name', y='cnt', title='Rata-rata Jumlah Sewa Sepeda Setiap Bulan')
    st.plotly_chart(fig)

# Scatter plot untuk Jumlah Sewa Sepeda pada setiap Bulan dalam Dua Tahun Terakhir
col1, = st.columns(1)
with col1:
    fig = px.line(day_df, x='mnth', y='cnt', color='yr', title='Jumlah Sewa Sepeda Tiap Bulan dalam 2 Tahun Terakhir')
    fig.update_layout(xaxis_title='Month', yaxis_title='Jumlah Sewa Sepeda', legend_title='Year')
    st.plotly_chart(fig)
