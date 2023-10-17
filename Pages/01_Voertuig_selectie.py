import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px 
import datetime, timedelta

st.set_page_config(page_title="Voertuigen", page_icon="📈")

#st.sidebar.header("Ritprofielen")

st.title("Heavy Duty Elektrificatie tool")


st.write("Kies hier het type voertuig dat u wilt elektrificeren")

###Keuze voertuig
voertuig = st.selectbox(
    '',
    ('Medium bakwagen lvm 12 - 18 ton', 'Grote bakwagen lvm > 18 ton', 'Lichte trekker z/opl gvm < 40 ton', "Zware trekker z/opl gvm > 40 ton"))


optiesvoertuig =  st.selectbox("Welke andere energievebruikers heeft uw voertuig?",
                                        ("Geen", "Koeling", "Lift: Vuilnis", "Lift Anders"))
                                         

st.write("De keuzes voor uw voertuig en opties hangen samen met het energieverbruik")
st.write("Wilt u deze inzien en aanpassen, dan kan dit hieronder")
with st.expander("Zie specificaties"):
    st.write(voertuig)
    if voertuig == 'Medium bakwagen lvm 12 - 18 ton':
        tempverbruikvoertuig = 1.2
    elif voertuig =='Grote bakwagen lvm > 18 ton': 
        tempverbruikvoertuig = 1.1
    elif voertuig =='Lichte trekker z/opl gvm < 40 ton':
        tempverbruikvoertuig = 1
    else:
        tempverbruikvoertuig = 0.8
    
    
    verbruikvoertuig = st.number_input('Energieverbruik voertuig kWh/km', value= tempverbruikvoertuig)
    st.write(optiesvoertuig)
    if optiesvoertuig == "Koeling":
        verbruikopties  = st.number_input('Energieverbruik opties kWh/uur', value=0.8)
    elif optiesvoertuig == "Geen":
        verbruikopties  = st.number_input('Energieverbruik opties kWh/uur', value=0)       
    else: 
        verbruikopties = st.number_input('Energieverbruik opties kWh/keer', value=0.05)

###Store inputs in session state
if "voertuig" not in st.session_state:
    st.session_state.voertuig = verbruikvoertuig
if "opties" not in st.session_state:
    st.session_state.opties = verbruikopties   
    