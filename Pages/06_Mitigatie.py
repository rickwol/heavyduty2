import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px 
import datetime, timedelta

congestiedatabase = pd.read_csv("data2/netcongestie.csv")
#st.sidebar.header("Ritprofielen")

st.title("Heavy Duty Elektrificatie tool")


st.write("Welke maatregelen kunt u nemen bij netcongestie")


         

