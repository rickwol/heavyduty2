import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px 
import datetime, timedelta

st.set_page_config(page_title="Financieel overzicht", page_icon="📈")

#st.sidebar.header("Ritprofielen")

st.title("Heavy Duty Elektrificatie tool")


st.write("Financieel overzicht")
st.write("De input voor deze gegevens komen uit de keuzes en de input van de ritprofielen. De tool biedt wel de mogelijkheid om aanpassingen te maken in het financiële overzicht")

col1, col2 = st.columns(2)

with col1:
   st.header("Elektrisch")
   st.write("Aanschafkosten")
   aanschafe = st.number_input("Aanschafkosten", value=300000)
   afschrijfe = st.number_input("Afschrijftermijn in jaren", value=7)
   st.write("Jaarlijkse kosten: €", float(np.round(aanschafe/afschrijfe, 0)))

   st.write("Verbruikskosten")
   kile = st.number_input("Kilometrage per jaar", value=75000)
   kwhe = st.number_input("Prijs per kWh", value=0.2)
   effe = st.number_input("Efficiënctie km/kWh", value=1)
   st.write("Jaarlijkse kosten: €", float(np.round((kile*kwhe)/effe, 0)))
    
   st.write("Laadinfrastructuur") 
   laadpaal = st.number_input("Aanschaf laadpaal", value=25000)
   netaan = st.number_input("Uitbreiding netaansluiting", value=25000)
   afschrijflaadpaal = st.number_input("Afschrijftermijn in jaren", value=10)
   perioned = st.number_input("Periodieke netaanslutingskosten", value=20000)
   st.write("Jaarlijkse kosten: €", float(np.round(((laadpaal + netaan)/afschrijflaadpaal) + perioned, 0)))

   st.write("Totale jaarlijkste kosten: €",  float(np.round(aanschafe/afschrijfe, 0)) + float(np.round((kile*kwhe)/effe, 0)+ float(np.round((laadpaal + netaan)/afschrijflaadpaal + perioned, 0))))

with col2:
   st.header("Diesel")
   st.write("Aanschafkosten")
   aanschafd = st.number_input("Aanschafkosten", value=125000)
   afschrijfd= st.number_input("Afschrijftermijn in jaren Diesel", value=7)
   st.write("Jaarlijkse kosten: €", float(np.round(aanschafd/afschrijfd, 0)))

   st.write("Verbruikskosten")
   kild = st.number_input("Kilometrage per jaar Diesel", value=kile)
   kwhd = st.number_input("liter", value=0.2)
   effd = st.number_input("km/liter", value=1)
   st.write("Jaarlijkse kosten: €", float(np.round((kild*kwhd)/effd, 0)))
    
   st.write("Laadinfrastructuur") 
   st.write("") 
   st.write("") 
   st.write("") 
   st.write("") 
   st.write("") 
   st.write("") 
   st.write("") 
   st.write("") 
   st.write("") 
   st.write("") 
   st.write("") 
   st.write("") 
   st.write("") 
   st.write("") 
   st.write("") 
   st.write("") 
   st.write("") 
   st.write("") 
   st.write("") 
   st.write("") 
   st.write("") 
   st.write("") 
   st.write("") 
   st.write("") 
   st.write("") 
    
   st.write("Totale jaarlijkste kosten: €",  float(np.round(aanschafd/afschrijfd, 0)) + float(np.round((kild*kwhd)/effd, 0)))

        


