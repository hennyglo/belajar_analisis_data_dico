# -*- coding: utf-8 -*-
"""bike_sharing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XrTUhYf6bUq-s-_PRH0TUFjg3-vLWIeu

# Proyek Analisis Data: Bike Sharing

- Nama: Henny Gloria Datubara
- Email: hennygloriadatubarag@mhs.unimed.ac.id
- Id Dicoding: <a href='https://www.dicoding.com/users/henny_4203/academies' target="_blank">henny_4203</a>
- Github: <a href='https://github.com/hennyglo/analisis_data_python' target="_blank">Bike Sharing</a>

# Menentukan Pertanyaan Bisnis

**Specifict:**
- 1. Berapa jumlah total sewa sepeda (cnt) untuk tahun 2012 selama musim gugur (musim 3)?

**Measurable:**
- 2. Berapa banyak sepeda sewaan yang digunakan pada hari libur (liburan = 1) selama musim panas (musim 2) pada tahun 2011?

**Action-oriented:**
- 3. Bagaimana cara meningkatkan jumlah rental sepeda yang digunakan oleh pengguna biasa (casual) pada hari kerja (hari kerja = 1)?

**Relevant:**
- 4. Apa hubungan suhu (temp) dengan jumlah pengguna yang terdaftar (registered)?
- 5. Apa pengaruh cuaca (weathersit) terhadap jumlah sewa sepeda (cnt) selama musim gugur (season 3)?

**Time-bound:**
- 6. Berapa distribusi per jam sewa sepeda (cnt) pada Hari Natal (hari libur = 1) pada tahun 2012 (tahun = 1)?

<!-- - **Specific**: What is the total count of rental bikes (cnt) for the year 2012 during the fall season (season 3)?
- **Measurable**: How many rental bikes were used on holidays (holiday = 1) during the summer season (season 2) in 2011?
- **Action-oriented**: How can we increase the number of rental bikes used by casual users (casual) on weekdays (workingday = 1)?
- **Relevant**:
    - What is the relationship between temperature (temp) and the number of registered users (registered)?
    - What effect does the weather (weathersit) have on the number of bicycle rentals (cnt) during autumn (season 3)?
- **Time-bound**: What was the hourly distribution of rental bikes (cnt) on Christmas Day (holiday = 1) in 2012 (yr = 1)? -->

::# Menyiapkan semua library yang dibutuhkan
"""

# Instal Plotly
!pip install plotly

# Impor Plotly
import plotly.express as px

# Contoh penggunaan Plotly Express
df = px.data.iris()
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')
fig.show()

"""# Data Wrangling

## Gathering Data
"""

import pandas as pd

df_day = pd.read_csv("/content/day.csv")
df_hour = pd.read_csv("/content/hour.csv")

df_day.head()

df_hour.head()

"""### > Data Type"""

print('Dataframe day:')
print(df_day.info())

print('\nDataframe hour:')
print(df_hour.info())

"""(!) Berdasarkan hasil observasi pada df_day, terdapat kesalahan dalam jenis data pada kolom dteday yang awalnya berupa objek, tetapi seharusnya berupa tipe data datetime.

### > Missing value
"""

print('Dataframe day:')
print(df_day.isna().sum())

print('\nDataframe hour:')
print(df_hour.isna().sum())

"""(✓) Dari hasil pemeriksaan pada dataset df_day dan df_hour, tidak ada nilai yang hilang atau kosong.

### > Duplicate Data
"""

print('Dataframe day:', df_day.duplicated().sum())
print("Dataframe hour:", df_hour.duplicated().sum())

"""(✓) Tidak ada data yang duplicate.

### > Descriptive statistics
"""

df_day.describe()

df_hour.describe()

"""**(⁜) Descriptive Analysis**

1. Dataset day
    - Jumlah data: 731 entri.
    - Musim paling umum: Musim panas (season 2).
    - Tahun yang dominan: 2012 (yr = 1).
    - Bulan yang paling sering muncul: Juli (mnth 7).
    - Hari libur hanya ada sekitar 2.87% dari total hari.
    - Hari kerja adalah mayoritas (sekitar 68.40%).
    - Cuaca rata-rata pada keadaan yang baik (weathersit 1).
    - Suhu rata-rata adalah sekitar 0.50 (41°C), dengan suhu perasaan rata-rata sekitar 0.47 (50°C).
    - Kelembaban rata-rata sekitar 0.47 (47%).
    - Kecepatan angin rata-rata adalah sekitar 0.63 (67% dari maksimal).
    - Jumlah pengguna casual rata-rata sekitar 848.
    - Jumlah pengguna terdaftar rata-rata sekitar 3656.
    - Total rental rata-rata sekitar 4504 per hari.


2. Dataset hour
    - Dataset terdiri dari 17,379 entri.
    - Rata-rata kolom-kolom utama adalah sekitar:
        - Musim (season) 2.50, menunjukkan musim rata-rata.
        - Tahun (yr) 0.50, mengindikasikan perbandingan antara tahun 2011 dan 2012.
        - Bulan (mnth) 6.54, menunjukkan bulan rata-rata dalam setahun.
        - Jam (hr) 11.55, mengindikasikan jam rata-rata dalam sehari.
        - Hari libur (holiday) 0.03, persentase hari libur.
        - Hari dalam seminggu (weekday) 3.00, hari rata-rata dalam seminggu.
        - Hari kerja (workingday) 0.68, persentase hari kerja.
        - Kondisi cuaca (weathersit) 1.43, kondisi cuaca rata-rata.
        - Suhu (temp) 0.50, suhu rata-rata yang normal.
        - Suhu perasaan (atemp) 0.48, suhu perasaan mendekati suhu sebenarnya.
        - Kelembaban (hum) 0.48, kelembaban rata-rata.
        - Kecepatan angin (windspeed) 0.63, kecepatan angin rata-rata.
        - Pengguna casual (casual) 35.68, rata-rata jumlah pengguna casual.
        - Pengguna terdaftar (registered) 153.79, rata-rata jumlah pengguna terdaftar.
        - Total rental sepeda (cnt) 189.46, rata-rata jumlah total rental sepeda.

## Cleaning Data

### > Fixed data type
"""

# df_day
df_day["dteday"] = pd.to_datetime(df_day["dteday"])
# df_hour
df_hour["dteday"] = pd.to_datetime(df_hour["dteday"])

# Check data type for df_day and df_hour
print('df_day["dteday"] : ', df_day["dteday"].dtypes)
print('df_hour["dteday"] : ', df_hour["dteday"].dtypes)

"""(✓) Fixed

# Exploratory Data Analysis (EDA)

**> Korelasi antara variabel numerik**
"""

import warnings
warnings.filterwarnings("ignore")

# df_day
correlation_matrix = df_day.corr()
fig = px.imshow(correlation_matrix)
fig.update_layout(title="Korelasi antara Variabel Numerik")
fig.show()

"""**> Distribusi variabel numerik**"""

numeric_cols = ['temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt']
for col in numeric_cols:
    fig = px.histogram(df_day, x=col, title=f'Distribusi {col}')
    fig.show()

"""**> Distribusi variabel kategorikal**"""

categorical_cols = ['season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit']
for col in categorical_cols:
    fig = px.bar(df_day[col].value_counts().reset_index(), x=df_day[col].value_counts().reset_index().index, y=col)
    fig.update_layout(title=f'Distribusi {col}')
    fig.show()

"""**> Hubungan antara musim (season) dan jumlah sewa (cnt)**"""

fig = px.box(df_day, x='season', y='cnt')
fig.update_layout(title='Hubungan antara Musim dan Jumlah Sewa')
fig.show()

"""**> Hubungan antara hari libur (holiday) dan jumlah sewa (cnt)**"""

fig = px.box(df_day, x='holiday', y='cnt')
fig.update_layout(title='Hubungan antara Hari Libur dan Jumlah Sewa')
fig.show()

"""**> Hubungan antara cuaca (weathersit) dan jumlah sewa (cnt)**"""

fig = px.box(df_day, x='weathersit', y='cnt')
fig.update_layout(title='Hubungan antara Cuaca dan Jumlah Sewa')
fig.show()

"""**> Scatter plot antara suhu (temp) dan jumlah sewa (cnt)**"""

fig = px.scatter(df_day, x='temp', y='cnt', title='Scatter Plot antara Suhu dan Jumlah Sewa')
fig.show()

"""# Visualization & Explanatory Analysis

**1. Berapa jumlah total sewa sepeda (cnt) untuk tahun 2012 selama musim gugur (musim 3)?**
"""

# Filter tahun 2012 dan musim gugur (season 3)
filtered_data = df_day[(df_day["yr"] == 1) & (df_day["season"] == 3)]

# Hitung jumlah total sewa sepeda (cnt)
total_sewa_sepeda = filtered_data["cnt"].sum()

print("Jumlah total sewa sepeda untuk tahun 2012 selama musim gugur (musim 3):", total_sewa_sepeda)

"""**2. Berapa banyak sepeda sewaan yang digunakan pada hari libur (liburan = 1) selama musim panas (musim 2) pada tahun 2011?**"""

# Filter tahun 2011, musim panas (season 2), dan hari libur (holiday = 1)
filtered_data = df_day[(df_day["yr"] == 0) & (df_day["season"] == 2) & (df_day["holiday"] == 1)]

# Hitung jumlah total sepeda sewaan
total_sepeda_sewaan = filtered_data["cnt"].sum()

print("Jumlah total sepeda sewaan yang digunakan pada hari libur selama musim panas tahun 2011:", total_sepeda_sewaan)

"""**3. Bagaimana cara meningkatkan jumlah rental sepeda yang digunakan oleh pengguna biasa (casual) pada hari kerja (hari kerja = 1)?**"""

# Filter pengguna casual (casual) pada hari kerja (workingday = 1)
filtered_data = df_day[(df_day["workingday"] == 1) & (df_day["casual"] > 0)]

# Visualisasikan jumlah sewa sepeda casual pada hari kerja
fig = px.bar(filtered_data, x="weekday", y="casual", title="Jumlah Sewa Sepeda Casual pada Hari Kerja")
fig.update_xaxes(title="Hari Kerja")
fig.update_yaxes(title="Jumlah Sewa Sepeda Casual")
fig.show()

"""**Strategi:**
- Promosi khusus untuk hari-hari tertentu yang memiliki grafik yang rendah seperti pada grafik (Monday & Wednesday), seperti diskon khusus atau penawaran khusus yang hanya berlaku pada hari kerja.
- Memastikan fasilitas penyewaan sepeda, seperti stasiun atau lokasi penyewaan, mudah diakses dan dalam kondisi baik selama hari kerja.
- Mempertimbangkan untuk menambah jumlah sepeda yang tersedia pada hari kerja untuk mengakomodasi permintaan yang lebih tinggi.
- Tingkatkan upaya pemasaran khusus untuk hari kerja, seperti iklan online yang menargetkan pengguna biasa pada hari kerja.
- Membuat program loyalitas atau diskon yang berkelanjutan untuk pengguna biasa yang sering menyewa sepeda pada hari kerja.

**4. Apa hubungan suhu (temp) dengan jumlah pengguna yang terdaftar?**
"""

# Buat scatter plot dengan Plotly untuk memvisualisasikan hubungan suhu (temp) dengan jumlah pengguna terdaftar (registered)
fig = px.scatter(df_day, x="temp", y="registered", title="Hubungan Suhu dengan Jumlah Pengguna Terdaftar")
fig.update_xaxes(title="Suhu (temp)")
fig.update_yaxes(title="Jumlah Pengguna Terdaftar")
fig.show()

"""**Insight:**

Pada grafik terlihat korelasi positif yang menunjukkan bahwa meningkatnya suhu (temp)  berpengaruh juga terhadap meningkatnya jumlah pengguna yang terdaftar.

**5. Apa pengaruh cuaca (weathersit) terhadap jumlah sewa sepeda (cnt) selama musim gugur (season 3)?**
"""

# Filter musim gugur (season 3)
filtered_data = df_day[df_day["season"] == 3]

# Buat plot dengan Plotly untuk menganalisis pengaruh cuaca terhadap jumlah sewa sepeda
fig = px.bar(filtered_data, x="weathersit", y="cnt", title="Pengaruh Cuaca terhadap Jumlah Sewa Sepeda (Musim Gugur)")
fig.update_xaxes(title="Cuaca (weathersit)")
fig.update_yaxes(title="Jumlah Sewa Sepeda (cnt)")

# Tampilkan plot
fig.show()

"""**(Info):**
- weathersit :
	- 1: Clear, Few clouds, Partly cloudy, Partly cloudy
	- 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
	- 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
	- 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog

**Insight:**

Dari hasil grafik yang telah dianalisis, kita dapat menyimpulkan bahwa faktor cuaca memiliki pengaruh yang signifikan terhadap jumlah sepeda yang disewa. Grafik tersebut menunjukkan bahwa perubahan kondisi cuaca memiliki dampak yang jelas terhadap perilaku pengguna sepeda. Lebih spesifiknya, kita dapat melihat bahwa pada kondisi cuaca tertentu, seperti cuaca yang cerah atau sebagian berawan (weathersit 1), jumlah sepeda yang disewa cenderung meningkat secara signifikan.

Analisis ini mengindikasikan bahwa faktor-faktor seperti kondisi cuaca dapat menjadi pertimbangan penting bagi penyedia layanan sewa sepeda, karena mereka dapat memengaruhi tingkat permintaan sepeda. Ini juga dapat memberikan wawasan yang berharga bagi pengambil keputusan dalam merencanakan stok sepeda, mengatur tarif, atau mengembangkan strategi pemasaran yang lebih efektif berdasarkan faktor cuaca yang berubah-ubah.

**6. Berapa distribusi per jam sewa sepeda (cnt) pada Hari Natal (hari libur = 1) pada tahun 2012 (tahun = 1)?**
"""

# Filter data tahun 2012 (yr = 1), Hari Natal (holiday = 1), dan musim panas (season 2)
filtered_data = df_hour[(df_hour["yr"] == 1) & (df_hour["holiday"] == 1) & (df_hour["season"] == 2)]

# Hitung distribusi per jam sewa sepeda (cnt)
distribusi_per_jam = filtered_data.groupby("hr")["cnt"].sum()

print("Distribusi per jam sewa sepeda pada Hari Natal tahun 2012:")
print(distribusi_per_jam)

"""**Insight:**

Distribusi ini menunjukkan bahwa pada pukul 17:00 (5:00 sore), terjadi lonjakan paling tinggi dalam jumlah sewa sepeda dengan 1.117 sewa, yang mungkin karena banyak orang menghabiskan waktu sore untuk bersepeda saat liburan Natal. Selain itu, aktivitas sewa sepeda mulai meningkat sejak pukul 6:00 pagi dan mencapai puncaknya antara pukul 17:00 dan 18:00. Setelah itu, jumlah sewa sepeda mulai turun secara perlahan hingga larut malam.

Ini menggambarkan pola penggunaan sepeda selama Hari Natal, yang mencerminkan kegiatan liburan dan rutinitas masyarakat pada tanggal tersebut.

# Conclusion

1. Faktor cuaca memiliki pengaruh signifikan terhadap jumlah sepeda yang disewa.
2. Sewa sepeda selama musim gugur 2012 mencapai 641.479, mengindikasikan potensi bisnis yang kuat. Cuaca, acara, dan promosi memengaruhi permintaan.
3. Jumlah sepeda sewaan yang digunakan selama liburan musim panas 2011 sebanyak 7224 mengindikasikan popularitas bersepeda saat liburan. Ini mencerminkan investasi infrastruktur dan meningkatnya minat bersepeda.
4. Sewa sepeda mencapai puncaknya pada hari Jumat, menunjukkan bahwa penggunaan sepeda secara signifikan meningkat menjelang akhir pekan.
5. Hubungan antara suhu dan jumlah pengguna terdaftar penyewaan sepeda menunjukkan bahwa cuaca memengaruhi minat bersepeda, dengan peningkatan suhu cenderung meningkatkan jumlah pengguna.
6. Pada Hari Natal tahun 2012, distribusi sewa sepeda menunjukkan puncak aktivitas antara jam 17:00 hingga 18:00, mencapai 1117 penyewaan, dengan peningkatan signifikan sejak pukul 8 pagi

# Mendapatkan file required.txt dari library yang digunakan
"""