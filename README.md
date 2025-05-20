# Coworking Map Streamlit - Projet Python S2

Bienvenue sur mon projet de fin d’année en Python. Il s'agit d'une application interactive développée avec Python et Streamlit, permettant de visualiser sur une carte les espaces de coworking en Île-de-France, avec des options de recherche, de filtrage, et un graphique d’analyse.

## Objectif

Créer une application simple, visuelle et utile, basée sur des données extraites d’un annuaire en ligne, enrichies automatiquement par géolocalisation (latitude/longitude), et affichées via une interface Streamlit ergonomique.

---

## Doc générale

La première étape du projet était de récupérer automatiquement les données à partir du site web "leportagesalarial.com" qui propose un annuaire des espaces de coworking. Pour cela, j'ai utilisé la bibliothèque PyQuery, qui permet de manipuler le HTML à la manière de jQuery. J'ai repéré la structure HTML du site et ciblé les balises contenant les noms, adresses, sites web, et autres informations des espaces de coworking. Une fois les URLs récupérées, j'ai lancé une boucle pour scraper chaque page individuelle d’espace.
J’'ai ajouté une étape de géolocalisation en utilisant le service Nominatim via la bibliothèque geopy. Cela m'a permis d'obtenir les coordonnées GPS : latitude et longitude de chaque adresse, pour l'affichage sur la carte. Pour ne pas surcharger le service et éviter le blocage de mes requêtes, j'ai introduit un délai de 1,2 seconde entre chaque appel.
Après le scraping et la géolocalisation, j'ai procédé à une vérification de la qualité des données. J'ai supprimé les doublons en me basant sur la combinaison du nom et de l'adresse. J'ai ensuite sauvegardé les données sous forme de fichier JSON dans mon Google Drive depuis Colab, en prévision de leur utilisation ultérieure dans l'application Streamlit déployée en local. Ce fichier contient toutes les informations collectées.
Pour la partie visualisation, j'ai utilisé PyCharm avec Streamlit. L'application charge le fichier JSON et le convertit en DataFrame Pandas. Une carte Folium est ensuite générée, centrée sur Paris, avec des marqueurs roses qui montrent chaque espace de coworking. Un système de filtrage dynamique a été intégré dans la barre latérale : l'utilisateur peut filtrer les résultats par code postal ou rechercher un espace précis par nom. Les espaces filtrés sont affichés à la fois sur la carte et sous forme de liste dans l'application.
Pour améliorer l’expérience utilisateur, j’ai ajouté une présentation en haut de page via un encart dédié avec st.markdown(), et un graphique avec matplotlib qui affcihe la répartition des espaces par arrondissement ou par ville. J'ai aussi réorganisé l'affichage des résultats en trois colonnes avec st.columns() afin de limiter le scroll vertical et de rendre l'interface plus lisible. Le fond de la carte a été changé en plus clair avec le style CartoDB positron.


## Fonctionnalités

- Scraping automatique des données à partir du site [leportagesalarial.com](https://www.leportagesalarial.com/coworking/)
- Géocodage des adresses via OpenStreetMap (Nominatim)
- Nettoyage et dédoublonnage des données avec pandas
- Carte interactive avec Folium (affichage des marqueurs personnalisés)
- Recherche par nom (barre latérale)
- Filtre par code postal
- Affichage en colonnes des résultats
- Graphique dynamique de répartition par arrondissement ou ville

---

## Éléments

- `app.py` : Code principal de l'application Streamlit
- `coworking_idf.json` : Données JSON enrichies (scraping + géolocalisation)
- `requirements.txt` : Dépendances nécessaires pour exécuter l'application
- `README.md` : Documentation du projet (ce fichier)

---

## Lancer l'application localement

1. **Cloner ce dépôt** :
   ```bash
   git clone https://github.com/Noraa4/Coworking-Map-Streamlit-PythonS2.git
   cd Coworking-Map-Streamlit-PythonS2
