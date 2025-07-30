import streamlit as st
import json
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from urllib.parse import quote_plus

st.set_page_config(layout="wide")
st.title("Atlanta Neighborhood Property Map")

@st.cache_data(show_spinner=False)
def load_geojson():
    with open('./data/atlanta_official.geojson', 'r') as f:
        return json.load(f)

@st.cache_data(show_spinner=False)
def load_data(year):
    datafile = f'./data/atlanta_{year}.csv'
    df = pd.read_csv(datafile)
    return df
    
def plot_map(data, year):
    geojson = load_geojson()
    token = '' # You must generate a token 
    #center_lon = -84.390035
    #center_lat = 33.744042
    center_lon = -84.41
    center_lat = 33.765

    custom_columns = data[['nbhd_name','parcels','avgprice','medianprice','nbhd_atl_id']].to_numpy()
    data['log_medianprice'] = np.log10(data['medianprice'].clip(lower=50000, upper=2600000))

    fig = go.Figure(go.Choroplethmapbox(
        geojson=geojson,
        locations=data['nbhd_atl_id'],
        z=data['log_medianprice'],
        featureidkey='properties.OBJECTID',
        colorscale='jet',
        customdata=custom_columns,
        hovertemplate=(
            'Neighborhood: %{customdata[0]}<br>' +
            'Parcels: %{customdata[1]:,}<br>' +
            'Avg Sale Price: $%{customdata[2]:,}<br>' +
            'Median Sale Price: $%{customdata[3]:,}<extra></extra>'
        ),
        colorbar=dict(
            title="Median Sale Price ($)",
            tickvals=[4.7, 5, 5.3, 5.6, 5.9, 6.2, 6.41],
            ticktext=["50K", "100K", "200K", "400K", "800K", "1.6M", "2.6M"]
        ),
        marker_opacity=0.6,
        marker_line_color='black',
        marker_line_width=0.5,
        zmin=4.7,
        zmid=5.6,
        zmax=6.41
    ))

    fig.update_layout(
        mapbox=dict(
            accesstoken=token,
            style='streets',
            center=dict(lat=center_lat, lon=center_lon),
            zoom=10.3
        ),
        title_text=f'Homes by Neighborhood in Atlanta ({year})',
        width=750,
        height=600,
        margin={"r":0,"t":50,"l":0,"b":0}
    )
    return fig

# --- UI and Rendering ---
with st.container():
    year = st.slider("Select Year", min_value=2016, max_value=2024, value=2024, step=1)

with st.spinner(f"Loading data for {year}..."):
    data = load_data(year)

if data is not None and not data.empty:
    fig = plot_map(data, year)
    st.plotly_chart(fig, use_container_width=True)
