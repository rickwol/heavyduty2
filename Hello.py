import streamlit as st
from st_pages import Page, add_page_title, show_pages

show_pages(
    [
        Page("Hello.py", "Home", "🏠"),
        # Can use :<icon-name>: or the actual icon
        Page("pages/01_Ritprofielen_Gemiddeld.py", "Ritprofieel Gemiddeld"),
        Page("pages/02_Ritprofielen_Maximaal.py", "Ritprofieel Gemiddeld"),
        Page("pages/03_Voertuig_opties.py", "Ritprofieel Gemiddeld"),
        Page("pages/04_Laadprofiel.py", "Ritprofieel Gemiddeld"),

       
    ]
)

st.write("Welkom bij de Heavy Duty elektrificatie tool")

st.markdown(
    """
    De tool voor een geïntegreerd advies voor elektrische logistiek
"""
)
