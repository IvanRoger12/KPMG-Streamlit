
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="KPMG - Tableau de bord Data Analyst", layout="wide")

# Bannière
st.markdown("<h1 style='text-align: center; color: #002060;'>📊 Candidature – Consultant Junior Data Analyst chez KPMG</h1>", unsafe_allow_html=True)

# Historique KPMG
st.markdown("### 🏢 À propos de KPMG")
st.markdown("""
KPMG est un leader mondial de l’audit, du conseil et des services fiscaux et juridiques. 
En France, le cabinet accompagne les entreprises de toutes tailles dans leur transformation numérique, leur performance et leur conformité réglementaire.
Présent dans 143 pays, KPMG regroupe plus de 265 000 collaborateurs à travers le monde.
""")

# Section Compétences
st.markdown("### 🧠 Compétences Clés")
st.markdown("""
- Leadership en data & analytics, collaboration transverse  
- Power BI (DAX, Langage M), SQL, Python, Alteryx  
- Analyse avancée, modélisation, automatisation de workflows  
- Gestion de projets BI (recette, spécifications, dashboards)  
- Suite Microsoft 365 : Teams, SharePoint, OneDrive  
""")

# Simulation de données
data = pd.DataFrame({
    "Trimestre": ["T1", "T2", "T3", "T4"],
    "Contrôles réalisés": [120, 150, 130, 160],
    "Incidents détectés": [12, 18, 10, 14],
    "Taux de conformité (%)": [90, 88, 92, 91]
})

# Affichage des données avec mise en forme
st.markdown("### 📋 Données de contrôle interne (exemple)")
styled_data = data.style.set_properties(**{'background-color': '#f9f9f9', 'color': '#333'}).format({"Taux de conformité (%)": "{:.0f}%"})
st.dataframe(styled_data, use_container_width=True)

# Graphique 1 : Barres comparatives
fig1 = px.bar(data, x="Trimestre", y=["Contrôles réalisés", "Incidents détectés"],
              barmode="group", title="📊 Contrôles vs Incidents",
              color_discrete_sequence=["#002060", "#70ad47"])
st.plotly_chart(fig1, use_container_width=True)

# Graphique 2 : Taux de conformité
fig2 = px.line(data, x="Trimestre", y="Taux de conformité (%)", markers=True,
               title="📈 Évolution du taux de conformité",
               line_shape="linear", markersize=10,
               color_discrete_sequence=["#4472c4"])
st.plotly_chart(fig2, use_container_width=True)

# Pied de page
st.markdown("---")
st.markdown("<p style='text-align: center;'>👨‍💻 Réalisé par Ivan Nfinda – Candidat Consultant Junior Data Analyst – Avril 2025</p>", unsafe_allow_html=True)
