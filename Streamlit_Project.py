import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Sidebar filter
st.sidebar.header("Filter Data")
selected_month = st.sidebar.slider("Pilih Bulan", min_value=1, max_value=12, value=(1, 12))
selected_hour = st.sidebar.slider("Pilih Jam", min_value=0, max_value=23, value=(0, 23))

filtered_day_df = day_df[(day_df['dteday'].dt.month >= selected_month[0]) & (day_df['dteday'].dt.month <= selected_month[1])]
filtered_hour_df = hour_df[(hour_df['hr'] >= selected_hour[0]) & (hour_df['hr'] <= selected_hour[1])]

# Dashboard 
st.title("Bike Sharing Dashboard")
st.markdown("Dashboard menganalisis data peminjaman sepeda.")


season_mapping = {
    1: "Musim Semi",
    2: "Musim Panas",
    3: "Musim Gugur",
    4: "Musim Dingin"
}
filtered_day_df["season_label"] = filtered_day_df["season"].map(season_mapping)

st.subheader("Pola Peminjaman Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x=filtered_day_df["season_label"], y=filtered_day_df["cnt"], hue=filtered_day_df["season_label"], palette="Set2", ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Peminjaman")
ax.set_title("Pola Peminjaman Berdasarkan Musim")
ax.grid(axis='y')
st.pyplot(fig)


st.subheader("Pola Peminjaman Berdasarkan Jam dalam Sehari")
fig, ax = plt.subplots(figsize=(8, 4))
sns.lineplot(x=filtered_hour_df["hr"], y=filtered_hour_df["cnt"], color="b", marker="o", ax=ax)
ax.set_xlabel("Jam dalam Sehari")
ax.set_ylabel("Rata-rata Jumlah Peminjaman")
ax.set_title("Pola Peminjaman Berdasarkan Jam dalam Sehari")
ax.grid(axis='y')
ax.set_xticks(range(0, 24))
st.pyplot(fig)

st.subheader("Proporsi Total Penyewaan Sepeda Tahun 2011 dan 2012")
yearly_counts = day_df.groupby("yr")["cnt"].sum()
labels = ["2011", "2012"]
fig, ax = plt.subplots(figsize=(7, 7))
ax.pie(yearly_counts, labels=labels, autopct='%1.1f%%', colors=['tab:blue', 'tab:orange'], startangle=90)
ax.set_title("Distribusi Jumlah Peminjaman Sepeda Tahun 2011-2012")
st.pyplot(fig)

st.subheader("Grafik Penyewaan Sepeda Tahun 2011-2012")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(day_df['dteday'], day_df['cnt'], label='Total Peminjaman', color='tab:green', alpha=0.8)
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Peminjaman")
ax.set_title("Peminjaman Sepeda Harian")
ax.legend()
ax.grid(True)
st.pyplot(fig)


st.markdown("**Sumber Data:** Bike Sharing Dataset")
