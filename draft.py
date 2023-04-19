import pandas as pd
import numpy as np
import streamlit as st
import altair as alt

p_id = np.arange(1000)
p_treated = np.random.binomial(1, 0.5, 1000)
p_act = np.random.binomial(1, 0.5, 1000)

p_nd = np.random.binomial(1, 0.8, 1000)
p_nd = p_act & p_nd

p_con = np.random.binomial(1, 0.8, 1000)
p_con = p_nd & p_con


data = pd.DataFrame({
    "p_id": p_id,
    "p_treated": p_treated,
    "p_act": p_act,
    "p_nd": p_nd,
    "p_con": p_con
})

click = alt.selection_multi(encodings=["color"])

chart = alt.Chart(data).mark_bar(
    size=100
).encode(
    # y='count():Q',
    y=alt.Y('count():Q', scale=alt.Scale(domain=[0, 1000])),
    color='p_treated'
).properties(
    width=600
).add_selection(
    click
).transform_filter(
    click
)

chart_2 = alt.Chart(data).mark_bar(
    size=100
).encode(
    y=alt.Y('sum(p_act):Q', scale=alt.Scale(domain=[0, 500]))
    # color='p_treated'
).properties(
    width=150
).add_selection(
    click
).transform_filter(
    click
)

chart_3 = alt.Chart(data).mark_bar(
    size=100
).encode(
    y=alt.Y('sum(p_nd):Q', scale=alt.Scale(domain=[0, 500]))
    # color='p_treated'
).properties(
    width=150
).add_selection(
    click
).transform_filter(
    click
)

chart_4 = alt.Chart(data).mark_bar(
    size=100
).encode(
    y=alt.Y('sum(p_con):Q', scale=alt.Scale(domain=[0, 500]))
    # color='p_treated'
).properties(
    width=150
).add_selection(
    click
).transform_filter(
    click
)

chart_vert = alt.hconcat(chart_2, chart_3, chart_4)
# st.write("here is a sentence")
# text = alt.Chart().mark_text("this is a sentence")
chart_comb = alt.vconcat(chart, chart_vert)

st.altair_chart(chart_comb)