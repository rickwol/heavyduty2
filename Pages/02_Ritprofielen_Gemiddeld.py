import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px 
import datetime, timedelta

st.set_page_config(page_title="Ritprofielen", page_icon="📈")

#st.sidebar.header("Ritprofielen")

st.title("Heavy Duty Elektrificatie tool")


st.write("Vul hier het rittenpatroon in voor een gemiddelde dag")


Aantalritten =  st.number_input('Hoeveel ritten op 1 dag?', step = 1, min_value= 3) -1

###Standaard Dataframe
df = pd.DataFrame(
    [
           {"Nummer rit": 1,"Starttijd Rit": "8:00", 'Eindtijd Rit' : "9:45", "Aantal kilometers": 10, "Kan laden op einde rit" : True, "Locatie einde rit: (Depot of Anders)" : "Depot"},
        {"Nummer rit": 2,"Starttijd Rit": "10:00", 'Eindtijd Rit' : "10:45", "Aantal kilometers": 75, "Kan laden op einde rit" : False, "Locatie einde rit: (Depot of Anders)" : "Depot"},
        {"Nummer rit": 3,"Starttijd Rit": "12:00", 'Eindtijd Rit' : "13:45", "Aantal kilometers": 175, "Kan laden op einde rit" : True, "Locatie einde rit: (Depot of Anders)" : "Depot"}
     
      
   ]
)  


###Store dataframe in session state
if "df_value" not in st.session_state:
    st.session_state.df_value = df


###Bepaal aantal ritten
if(Aantalritten > 0):
    for z in range(Aantalritten):
        df = df.append({"Nummer rit": z+2,"Starttijd Rit": "8:00", 'Eindtijd Rit' : "9:45", "Aantal kilometers": 10, "Kan laden op einde rit" : True, "Locatie einde rit: (Depot of Anders)" : "Depot"}, ignore_index=True)

        
###update df functie
def update(edited_df):
    for row_1, row_2, row_3, row_4, row_5, row_6 in zip(
        edited_df["Nummer rit"], edited_df["Starttijd Rit"], edited_df['Eindtijd Rit'], edited_df["Aantal kilometers"], edited_df["Kan laden op einde rit"], edited_df["Locatie einde rit: (Depot of Anders)"] 
    ):
        st.write(
            ""
        )
        
###Edit ritten
if df.equals(st.session_state["df_value"]): 
    edited_df = st.data_editor(df,key="editor",  num_rows="dynamic")
    
else:
    edited_df = st.data_editor(st.session_state["df_value"],key="editor",  num_rows="dynamic")

###Controleer of df zelfde als edited_Df ander supdate session state

                
                                        

if edited_df is not None and not edited_df.equals(st.session_state["df_value"]):
    # This will only run if
    # 1. Some widget has been changed (including the dataframe editor), triggering a
    # script rerun, and
    # 2. The new dataframe value is different from the old value
    update(edited_df)
    st.session_state["df_value"] = edited_df



