import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
from datetime import datetime, timedelta

# Mengatur gaya plot seaborn
sns.set(style='whitegrid')

day_df = pd.read_csv("day.csv")

# Mendapatkan tanggal sekarang
current_date = datetime.now().date()

# Mendefinisikan rentang waktu, misalnya dari 1 Januari 2011 hingga 31 Desember 2012
start_date = datetime(2011, 1, 1).date()
end_date = datetime(2012, 12, 31).date()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/gloryindahs/bike-sharing/raw/main/bike.png")
    
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
    fig, ax = plt.subplots(figsize=(10, 6))
    season_mapping = {1: 'Springer', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    day_df['season_name'] = day_df['season'].map(season_mapping)
    sns.barplot(x='season_name', y='cnt', data=day_df, palette="pastel")
    ax.set_title('Rata-rata Jumlah Sewa Sepeda Berdasarkan Musim')
    ax.set_xlabel('season')
    ax.set_ylabel('Rata-rata Jumlah Sepeda')
    st.pyplot(fig)

# Scatter plot untuk Kondisi Cuaca
with col2:
    fig, ax = plt.subplots(figsize=(10, 6))
    weathersit_mapping = {1: 'Few clouds', 2: 'Mist', 3: 'Light Snow', 4: 'Snow + Fog'}
    day_df['weathersit_name'] = day_df['weathersit'].map(weathersit_mapping)
    sns.barplot(x='weathersit_name', y='cnt', data=day_df, palette="pastel")  
    ax.set_title('Rata-rata Jumlah Sewa Sepeda Berdasarkan Kondisi Cuaca')
    ax.set_xlabel('weathersit')
    ax.set_ylabel('Rata-rata Jumlah Sepeda')
    st.pyplot(fig)

# Membagi layar menjadi dua kolom untuk suhu dan suhu terasa
col1, col2 = st.columns(2)

# Scatter plot untuk Suhu
with col1:
    sample_df = day_df.sample(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='temp', y='cnt', data=sample_df, palette="pastel")
    ax.set_title('Rata-rata Jumlah Sewa Sepeda Berdasarkan Suhu')
    ax.set_xlabel('temp')
    ax.set_ylabel('Rata-rata Jumlah Sepeda')
    st.pyplot(fig)

# Scatter plot untuk Suhu Terasa
with col2:
    sample_df = day_df.sample(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='atemp', y='cnt', data=sample_df, palette="pastel")
    ax.set_title('Rata-rata Jumlah Sewa Sepeda Berdasarkan Suhu Terasa')
    ax.set_xlabel('atemp')
    ax.set_ylabel('Rata-rata Jumlah Sepeda')
    st.pyplot(fig)



st.markdown('### Korelasi antara Jumlah Sepeda Sewaan dengan Suhu, Kelembaban, dan Kecepatan Angin')
# Membagi layar menjadi dua kolom untuk msuhu dan kelembaban
col1, col2, = st.columns(2)

# Scatter plot untuk Korelasi Suhu vs Jumlah Sewa Sepeda
with col1:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='temp', y='cnt', data=day_df, palette="pastel")
    ax.set_title('Korelasi Suhu vs Jumlah Sewa Sepeda')
    ax.set_xlabel('temp')
    ax.set_ylabel('Jumlah Sepeda')
    st.pyplot(fig)

# Scatter plot untuk Korelasi Kelembaban vs Jumlah Sewa Sepeda
with col2:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='hum', y='cnt', data=day_df, palette="pastel")
    ax.set_title('Korelasi Kelembaban vs Jumlah Sewa Sepeda')
    ax.set_xlabel('hum')
    ax.set_ylabel('Jumlah Sepeda')
    st.pyplot(fig)

# Scatter plot untuk Korelasi Kecepatan Angin vs Jumlah Sewa Sepeda
col1, = st.columns(1)
with col1:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='windspeed', y='cnt', data=day_df, palette="pastel")
    ax.set_title('Korelasi Kecepatan Angin vs Jumlah Sewa Sepeda')
    ax.set_xlabel('windspeed')
    ax.set_ylabel('Jumlah Sepeda')
    st.pyplot(fig)

st.markdown('### Jumlah Sewa Sepeda Selama Dua Tahun Terakhir')
# Membagi layar menjadi dua kolom untuk hari dan bulan
col1, col2, = st.columns(2)

# Scatter plot untuk Jumlah Sewa Sepeda Berdasarkan hari dan bulan
with col1:
    fig, ax = plt.subplots(figsize=(10, 6))
    weekday_mapping = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
    day_df['weekday_name'] = day_df['weekday'].map(weekday_mapping)
    sns.barplot(x='weekday_name', y='cnt', data=day_df, palette="pastel")  
    ax.set_title('Rata-rata Jumlah Sewa Sepeda Setiap Harinya')
    ax.set_xlabel('weekday')
    ax.set_ylabel('Rata-rata Jumlah Sepeda')
    st.pyplot(fig)

with col2:
    fig, ax = plt
