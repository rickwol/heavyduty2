import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px 
import datetime, timedelta

st.set_page_config(page_title="Ritprofielen", page_icon="📈")

#st.sidebar.header("Ritprofielen")

st.title("Heavy Duty Elektrificatie tool")


st.write("Vul hier het rittenpatroon in voor een gemiddelde dag")


Aantalritten =  st.number_input('Hoeveel ritten op 1 dag?', step = 1, min_value= 1) -1


df = pd.DataFrame(
    [
           {"Nummer rit": 1,"Starttijd Rit": "8:00", 'Eindtijd Rit ' : "9:45", "Aantal kilometers": 10, "Kan laden op einde rit" : True}
     
      
   ]
)  
if(Aantalritten > 0):
    for z in range(Aantalritten):
        df = df.append({"Nummer rit": z+2,"Starttijd Rit": "8:00", 'Eindtijd Rit ' : "9:45", "Aantal kilometers": 10, "Kan laden op einde rit" : True}, ignore_index=True)
        
    
    

edited_df = st.experimental_data_editor(df, num_rows="dynamic")
