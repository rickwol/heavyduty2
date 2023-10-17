import streamlit as st


from st_pages import Page, add_page_title, show_pages

"## Declaring the pages in your app:"

show_pages(
    [
        Page("Hello.py", "Home", "🏠"),
        # Can use :<icon-name>: or the actual icon
        Page("Pages/01_Voertuig_selectie.py", "Voertuig"), 
        Page("Pages/02_Ritprofielen_Gemiddeld.py", "Ritprofieel Gemiddeld"),
        Page("Pages/03_Voertuig_opties.py", "Voertuig keuze"),
        Page("Pages/04_Laadprofiel.py", "Laadprofiel"),
        Page("Pages/05_Netaansluiting.py", "Netaansluiting"),
        Page("Pages/06_Financieel.py", "Financieel overzicht"),

       
    ]
)


st.write("Welkom bij de Heavy Duty elektrificatie tool")

st.markdown(
    """
    De tool voor een geïntegreerd advies voor elektrische logistiek. Op basis van ritgegevens krijgt u een advies over de keuze voor elektrische trucks en de bijbehorende laadinfrastructuur. 
"""
)
