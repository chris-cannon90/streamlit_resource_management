import streamlit as st
import pandas as pd
import snowflake.connector
import plotly.express as px
from streamlit_extras.app_logo import add_logo
from streamlit_extras.switch_page_button import switch_page
import base64
import time
from backend.functions import *


####################################################################################################
# Formatting
####################################################################################################




####################################################################################################
# Connect to Snowflake
####################################################################################################
status_obj = st.status("Connecting to Snowflake...")
with status_obj:
    st.write("Initiating connection...")
    st.write("Hello world!")
    conn = st.connection(name="personal_snowflake"
                         , type="snowflake"
                         , password=st.secrets["snowflake_password"])
    df = conn.query("SELECT * FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF100.CUSTOMER LIMIT 1000")
    if df is not None:
        status_obj.update(state="complete")
        status_obj.success("Connected to Snowflake and saved the dataframe to session state!")
    else:
        status_obj.update(state="error")
        status_obj.error("Error connecting to Snowflake and creating the dataframe")