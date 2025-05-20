import streamlit as st
import json
import pandas as pd
import folium
from folium.plugins import Search
from streamlit_folium import st_folium
import matplotlib.pyplot as plt

# === Chargement des données JSON ===
with open("coworking_idf.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# === Prépa des données ===
df = pd.DataFrame(data)
df = df[df['latitude'].notnull() & df['longitude'].notnull()]
df['lat'] = df['latitude']
df['lon'] = df['longitude']
df['code_postal'] = df['adresse'].str.extract(r'(\d{5})')

# Extraction ville + arrondissement
def extraire_ville(row):
    if isinstance(row['code_postal'], str) and row['code_postal'].startswith("75"):
        arr = row['code_postal'][-2:]
        return f"Paris {arr}"
    else:
        parts = row['adresse'].split(',')
        return parts[-1].strip().title() if len(parts) > 1 else "Autre"

df['ville'] = df.apply(extraire_ville, axis=1)

# === Présentation du site ===
with st.container():
    st.title("👋 Bienvenue sur la plateforme des espaces de coworking")
    st.info("Découvrez les espaces de coworking en Île-de-France. Vous pouvez filtrer par ville, code postal ou rechercher par nom.")

# === filtres ===
search_input = st.sidebar.text_input("🔎 Rechercher un espace de coworking par nom")
code_postaux = sorted(df['code_postal'].dropna().unique())
code_selection = st.sidebar.selectbox("📍 Filtrer par code postal :", ["Tous"] + code_postaux)

# === Filtres +++ ===
filtered_df = df.copy()
if code_selection != "Tous":
    filtered_df = filtered_df[filtered_df['code_postal'] == code_selection]
if search_input:
    filtered_df = filtered_df[filtered_df['nom'].str.contains(search_input, case=False, na=False)]

# === Affichage colonnes ===
st.markdown("### 🏢 Liste des espaces de coworking")
cols = st.columns(3)
for i, (_, row) in enumerate(filtered_df.iterrows()):
    with cols[i % 3]:
        st.markdown(
            f"""
            <div style='font-size: 14px'>
            <b>{row['nom']}</b><br>
            {row['adresse']}<br>
            📞 {row.get('téléphone', 'Non renseigné')}<br>
            🌐 <a href="{row.get('Site', '#')}" target="_blank">Site web</a>
            </div>
            <hr>
            """, unsafe_allow_html=True
        )

# === Carte Folium ===
st.markdown("### 🗺️ Carte interactive des espaces de coworking")
m = folium.Map(location=[48.8566, 2.3522], zoom_start=11, tiles="cartodbpositron")

for _, row in filtered_df.iterrows():
    popup = folium.Popup(f"<b>{row['nom']}</b><br>{row['adresse']}", max_width=300)
    folium.Marker(
        location=[row['lat'], row['lon']],
        popup=popup,
        icon=folium.Icon(color='pink', icon='briefcase', prefix='fa')
    ).add_to(m)

st_folium(m, width=700, height=500)

# === Graphique Paris/Villes ===
st.markdown("### 📊 Répartition par arrondissement ou ville")
ville_counts = filtered_df['ville'].value_counts().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(10, 4))
ville_counts.plot(kind='bar', ax=ax, color="#f48fb1")
ax.set_ylabel("Nombre d'espaces")
ax.set_xlabel("Ville / Arrondissement")
ax.set_title("Nombre d'espaces de coworking par zone")
st.pyplot(fig)
