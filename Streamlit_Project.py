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

st.subheader("Pola Peminjaman Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x=filtered_day_df["season"], y=filtered_day_df["cnt"], hue=filtered_day_df["season"], palette="Set2", ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Peminjaman")
ax.set_title("Pola Peminjaman Berdasarkan Musim")
ax.grid(axis='y')
st.pyplot(fig)

st.subheader("Pola Peminjaman Berdasarkan Cuaca")
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x=filtered_day_df["weathersit"], y=filtered_day_df["cnt"], hue=filtered_day_df["weathersit"], palette="Set3", ax=ax)
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Jumlah Peminjaman")
ax.set_title("Pola Peminjaman Berdasarkan Cuaca ☀️")
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

st.subheader("👥 Perbandingan Pengguna Casual vs. Registered")
sns.set_theme(style="whitegrid")
avg_hourly_usage = filtered_hour_df.groupby("hr")[["casual", "registered"]].mean()
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(avg_hourly_usage.index, avg_hourly_usage["casual"], label="Casual Users", color="tomato", linestyle="--", linewidth=2.5, marker="o", markersize=8)
ax.plot(avg_hourly_usage.index, avg_hourly_usage["registered"], label="Registered Users", color="dodgerblue", linestyle="-", linewidth=2.5, marker="s", markersize=8)

ax.set_xlabel("Jam dalam Sehari", fontsize=12)
ax.set_ylabel("Rata-rata Jumlah Peminjaman", fontsize=12)
ax.set_title("Perbandingan Pola Peminjaman: Casual vs. Registered Users", fontsize=14, pad=20)
ax.set_xticks(range(0, 24))
ax.legend(loc="upper left", fontsize=10)
ax.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()
st.pyplot(fig)

st.markdown("**Sumber Data:** Bike Sharing Dataset")
