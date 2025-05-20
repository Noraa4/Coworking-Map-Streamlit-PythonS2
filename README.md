# 🗺️ Coworking Map Streamlit - Projet Python S2

Bienvenue sur mon projet de fin d’année en Python. Il s'agit d'une application interactive développée avec Python et Streamlit, permettant de **visualiser sur une carte les espaces de coworking en Île-de-France**, avec des options de recherche, de filtrage, et un graphique d’analyse.

## 🎯 Objectif

Créer une application simple, visuelle et utile, basée sur des données extraites d’un annuaire en ligne, enrichies automatiquement par géolocalisation (latitude/longitude), et affichées via une interface Streamlit ergonomique.

---

## 🛠️ Fonctionnalités

- **Scraping** automatique des données à partir du site [leportagesalarial.com](https://www.leportagesalarial.com/coworking/)
- **Géocodage** des adresses via OpenStreetMap (Nominatim)
- **Nettoyage et dédoublonnage** des données avec pandas
- **Carte interactive** avec Folium (affichage des marqueurs personnalisés)
- **Recherche par nom** (barre latérale)
- **Filtre par code postal**
- **Affichage en colonnes des résultats**
- **Graphique dynamique** de répartition par arrondissement ou ville

---

## 📁 Structure du projet

- `app.py` : Code principal de l'application Streamlit
- `coworking_idf.json` : Données JSON enrichies (scraping + géolocalisation)
- `requirements.txt` : Dépendances nécessaires pour exécuter l'application
- `README.md` : Documentation du projet (ce fichier)

---

## ▶️ Lancer l'application localement

1. **Cloner ce dépôt** :
   ```bash
   git clone https://github.com/Noraa4/Coworking-Map-Streamlit-PythonS2.git
   cd Coworking-Map-Streamlit-PythonS2
