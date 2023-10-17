import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px 
import datetime, timedelta

st.set_page_config(page_title="Ritprofielen", page_icon="📈")

#st.sidebar.header("Ritprofielen")

st.title("Heavy Duty Elektrificatie tool")

ritdata = st.session_state["df_value"]

ritdata["KM"] = ritdata["Aantal kilometers"]

for z in range(len(ritdata["Aantal kilometers"])):
    if ritdata["Kan laden op einde rit"][z] != True:
        ritdata["KM"][z+1] = ritdata["KM"][z+1]+ ritdata["KM"][z]


rit1 =  ritdata["Aantal kilometers"].head(1)
if ritdata["Aantal kilometers"].shape[0]>1:
    andereritten = ritdata["KM"].tail(-1).max()/0.8
else:
    andereritten = rit1



ritdata["Starttime"] = pd.to_datetime('2023-01-01 ' + ritdata["Starttijd Rit"])
ritdata["Endtime"] = pd.to_datetime('2023-01-01 ' + ritdata["Eindtijd Rit"])
ritdata["difftime"] = ((ritdata["Starttime"].shift(-1) - ritdata["Endtime"]).dt.total_seconds()/3600)-0.16
ritdata["laadsnelheid"] =  ((ritdata["KM"] * st.session_state.voertuig)/  ritdata["difftime"])
ritdata["laadsnelheid"].fillna((ritdata["Aantal kilometers"].sum()* st.session_state.voertuig)/12, inplace=True)
#st.dataframe(ritdata)
                                    
    
kilometers = float(np.maximum(rit1, andereritten))

kilomterssom = ritdata["Aantal kilometers"].sum()

energieonderweg = int(kilometers/0.7 * st.session_state.voertuig)
energiedepot = int(kilomterssom/0.7 * st.session_state.voertuig)

oplaaddepot = int(np.round(ritdata["laadsnelheid"].tail(1)))


st.write("Op basis van uw input zijn dit drie trucks en laadstrategiëen")

col1, col2, col3, = st.columns(3)

with col1:
    st.header("Alleen depot laden")
    st.image("https://media.istockphoto.com/id/1306857153/nl/foto/het-laadstation-van-elektrische-voertuigen-op-een-achtergrond-van-een-vrachtwagen.jpg?s=612x612&w=0&k=20&c=kF5jroBqGmPsn_6zup2ahw1R2W6xNb6dNibQqlf-KGM=")
    st.write("Accu:", str(np.round(energiedepot)), "kWh")
    st.write("Range:", str(np.round(kilomterssom)), "km")
    st.write("Oplaadcapaciteit: ", str(oplaaddepot), "kW")
with col2:
    st.header("Frequent laden")
    st.image("https://media.istockphoto.com/id/1306857153/nl/foto/het-laadstation-van-elektrische-voertuigen-op-een-achtergrond-van-een-vrachtwagen.jpg?s=612x612&w=0&k=20&c=kF5jroBqGmPsn_6zup2ahw1R2W6xNb6dNibQqlf-KGM=")
    st.write("Accu:", str(np.round(energieonderweg)), "kWh")
    st.write("Range:", str(np.round(kilometers)),"km")
    st.write("Oplaadcapaciteit: ", str(int(np.round(ritdata["laadsnelheid"].max()))), "kW")


st.text("Gebruik deze input voor een verkenning van welke specifieke truck dit kan zijn in de ZETI tool:")
url = "https://globaldrivetozero.org/tools/zeti/"
st.write("Klik [hier](%s) voor de tool" % url)

truckinput = st.selectbox("Welke optie kiest u?", ("Alleen depot laden",  "Frequent laden"))

st.write("Afhankelijk van uw laadstrategie nemen we uw voertuigspecificaties mee. Wilt uw toch iets anders invullen dan kan dit hieronder")
with st.expander("Zie specificaties"):
    accu = st.number_input('Accu (kWh)', value= energiedepot)
    accu = st.number_input('Oplaadvermogen (kW)', value= oplaaddepot)
    