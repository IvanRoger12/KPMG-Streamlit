
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="KPMG Data Analyst Dashboard", layout="wide")

# Titre de l'application
st.title("📊 Dashboard de Suivi des Risques et Performance")

st.markdown("Ce tableau de bord a été conçu pour illustrer ma capacité à transformer les données en insights exploitables, dans un contexte proche des missions proposées chez KPMG.")

# Simuler un jeu de données
data = pd.DataFrame({
    "Période": ["T1", "T2", "T3", "T4"],
    "Nombre de contrôles": [120, 150, 130, 160],
    "Incidents détectés": [12, 18, 10, 14],
    "Taux de conformité (%)": [90, 88, 92, 91]
})

# Affichage des données
st.subheader("📋 Données internes de contrôle")
st.dataframe(data)

# Graphique : Nombre de contrôles vs incidents
fig1 = px.bar(data, x="Période", y=["Nombre de contrôles", "Incidents détectés"],
              barmode="group", title="Contrôles réalisés vs Incidents détectés")
st.plotly_chart(fig1, use_container_width=True)

# Graphique : Taux de conformité
fig2 = px.line(data, x="Période", y="Taux de conformité (%)", markers=True,
               title="Évolution du taux de conformité")
st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")
st.markdown("👨‍💻 Réalisé par Ivan Nfinda – Candidat Consultant Junior Data Analyst – Avril 2025")
