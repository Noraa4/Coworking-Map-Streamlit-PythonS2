{\rtf1\ansi\ansicpg1252\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 ArialMT;\f1\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28600\viewh16380\viewkind0
\deftab720
\pard\pardeftab720\qj\partightenfactor0

\f0\fs29\fsmilli14667 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 \
\pard\pardeftab720\sa320\qj\partightenfactor0
\cf0 La premi\'e8re \'e9tape du projet \'e9tait de r\'e9cup\'e9rer automatiquement les donn\'e9es \'e0 partir du site web "leportagesalarial.com" qui propose un annuaire des espaces de coworking. Pour cela, j'ai utilis\'e9 la biblioth\'e8que PyQuery, qui permet de manipuler le HTML \'e0 la mani\'e8re de jQuery. J'ai rep\'e9r\'e9 la structure HTML du site et cibl\'e9 les balises contenant les noms, adresses, sites web, et autres informations des espaces de coworking. Une fois les URLs r\'e9cup\'e9r\'e9es, j'ai lanc\'e9 une boucle pour scraper chaque page individuelle d\'92espace.
\f1\fs24 \

\f0\fs29\fsmilli14667 J\'92'ai ajout\'e9 une \'e9tape de g\'e9olocalisation en utilisant le service Nominatim via la biblioth\'e8que geopy. Cela m'a permis d'obtenir les coordonn\'e9es GPS : latitude et longitude de chaque adresse, pour l'affichage sur la carte. Pour ne pas surcharger le service et \'e9viter le blocage de mes requ\'eates, j'ai introduit un d\'e9lai de 1,2 seconde entre chaque appel.
\f1\fs24 \

\f0\fs29\fsmilli14667 Apr\'e8s le scraping et la g\'e9olocalisation, j'ai proc\'e9d\'e9 \'e0 une v\'e9rification de la qualit\'e9 des donn\'e9es. J'ai supprim\'e9 les doublons en me basant sur la combinaison du nom et de l'adresse. J'ai ensuite sauvegard\'e9 les donn\'e9es sous forme de fichier JSON dans mon Google Drive depuis Colab, en pr\'e9vision de leur utilisation ult\'e9rieure dans l'application Streamlit d\'e9ploy\'e9e en local. Ce fichier contient toutes les informations collect\'e9es.
\f1\fs24 \

\f0\fs29\fsmilli14667 Pour la partie visualisation, j'ai utilis\'e9 PyCharm avec Streamlit. L'application charge le fichier JSON et le convertit en DataFrame Pandas. Une carte Folium est ensuite g\'e9n\'e9r\'e9e, centr\'e9e sur Paris, avec des marqueurs roses qui montrent chaque espace de coworking. Un syst\'e8me de filtrage dynamique a \'e9t\'e9 int\'e9gr\'e9 dans la barre lat\'e9rale : l'utilisateur peut filtrer les r\'e9sultats par code postal ou rechercher un espace pr\'e9cis par nom. Les espaces filtr\'e9s sont affich\'e9s \'e0 la fois sur la carte et sous forme de liste dans l'application.
\f1\fs24 \

\f0\fs29\fsmilli14667 Pour am\'e9liorer l\'92exp\'e9rience utilisateur, j\'92ai ajout\'e9 une pr\'e9sentation en haut de page via un encart d\'e9di\'e9 avec st.markdown(), et un graphique avec matplotlib qui affcihe la r\'e9partition des espaces par arrondissement ou par ville. J'ai aussi r\'e9organis\'e9 l'affichage des r\'e9sultats en trois colonnes avec st.columns() afin de limiter le scroll vertical et de rendre l'interface plus lisible. Le fond de la carte a \'e9t\'e9 chang\'e9 en plus clair avec le style CartoDB positron.
\f1\fs24 \
\pard\pardeftab720\partightenfactor0
\cf0 \
}