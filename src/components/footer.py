import streamlit as st


def footer_home():

    logo_url = "https://www.mnnit.ac.in/rnc/nrnc/assets/images/MNNIT_LOGO.png"

    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center;">
        <p style="font-weight:bold; color:white;">Created with ❤️ for</p>

        <img src="{logo_url}" style="height:70px;" />
        </div>
    """, unsafe_allow_html=True)

def footer_dashboard():

    logo_url = "https://www.mnnit.ac.in/rnc/nrnc/assets/images/MNNIT_LOGO.png"

    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center;">
        <p style="font-weight:bold; color:black;">Created with ❤️ for</p>

        <img src="{logo_url}" style="height:70px;" />
        </div>
    """, unsafe_allow_html=True)