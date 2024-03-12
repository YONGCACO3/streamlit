import streamlit as st
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import altair as alt

# Sample Hist Plot
rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

# Line Chart
df = pd.DataFrame(np.random.randn(10, 2),    columns=['x', 'y'])
st.line_chart(df)

# Bar Chart
df = pd.DataFrame(np.random.randn(10, 2),    columns=['x', 'y'])
st.bar_chart(df)

# Area Chart
df = pd.DataFrame(np.random.randn(10, 2),    columns=['x', 'y'])
st.area_chart(df)

# Altair Chart
df = pd.DataFrame(np.random.randn(500, 3),   columns=['x', 'y', 'z'])
c = alt.Chart(df).mark_circle().encode(
    x='x', y='y', size='z', color='z', tooltip=['x', 'y', 'z'])
st.altair_chart(c, use_container_width=True)

# Display Map
df = pd.DataFrame(np.random.randn(500, 2) /
                  [50, 50] + [49.28, -123.12], columns=['lat', 'lon'])
st.map(df)
