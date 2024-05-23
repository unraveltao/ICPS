import streamlit as st
import pandas as pd

from pygwalker.api.streamlit import StreamlitRenderer


uploaded_file = st.file_uploader("your csv data", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    pyg_app = StreamlitRenderer(data)
    pyg_app.explorer()