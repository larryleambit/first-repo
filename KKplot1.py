import streamlit as st
import altair as alt
from vega_datasets import data
from plotly import express as px
import pandas as pd

st.set_page_config(layout="wide")

source = data.seattle_weather()
source1 = source.iloc[:760, :]

# generate random data for sample slides
Treated_patients = ["KKUS"]*2014

# print(source.shape)

chart = alt.Chart(source, title="Treated Patients (on Crysvita)").mark_bar(
    # size=10, #we can use this parameter to adjust bar size
    cornerRadiusTopLeft=1,
    cornerRadiusTopRight=3,
    align="center"
).encode(
    x='month(date):O',
    y='count():Q',
    color='weather:N'
)

chart2 = alt.Chart(source1, title="Diagnosed Patients (Not on Crysvita)").mark_bar(
    cornerRadiusTopLeft=1,
    cornerRadiusTopRight=3,
    align="center"
).encode(
    x='month(date):O',
    y='count():Q',
    color='weather:N'
)

chart3 = alt.Chart(source1, title="Number of Diagnosed Patients Addressed by Reps").mark_bar(
    cornerRadiusTopLeft=1,
    cornerRadiusTopRight=3
).encode(
    x='count():Q',
    y='month(date):O',
    # color='weather:N'
    # color=alt.Color("weather", scale=alt.Scale(domain=domain, range=range_))
).properties(
    width=550
)

chart_2 = alt.hconcat(chart, chart2)

# chart_final = alt.vconcat(chart_2, chart3).configure_title(align="center")

# Here we plot our main visulizations

# title = st.title("Sales Reps: Diagnosed Patients")

tab1, tab2 = st.tabs(["Patient Polulation", "Sales Reps - Diagnosed Patients"])

with tab1:

    age = st.slider("Patient Age", 0, 80, 80)

    with st.container():
        col1, col2, col3, col4 = st.columns(4)

        with col3:
            show = st.write("""
                    <div style="border-radius: 25px;
                        background: #F0F8FF;
                        padding: 25px">
                        <p style="font-weight: bold; text-align: center; font-size: 20px"> 14,008 </p>
                        <p style="text-align: center; font-size: 15px"> Prevalence (# Total Patients) </p>
                    </div>
                """,
                unsafe_allow_html=True)
    
    for i in range(2):
        st.text("")
    
    st.write("""
            <div style="position: relative; left: 62.5%;">
                <vl style="border: 2px solid blue; border-color: #FFA07A; height: 100px" />
            </ div>
            """, unsafe_allow_html=True)


    st.write("""
                <div align="right">
                    <hr width="75%" style="margin: 0px, padding: 0px; border: 2px solid; border-color: #FFA07A" />
                </ div>
            """, unsafe_allow_html=True)

    with st.container():
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            pass

        with col2:
            show = st.write("""
                    <div style="border-radius: 25px;
                        background: #F0F8FF;
                        padding: 25px">
                        <p style="font-weight: bold; text-align: center; font-size: 20px"> 7,908 </p>
                        <p style="text-align: center; font-size: 15px"> # Diagnosed Patients </p>
                    </div>
                """,
                unsafe_allow_html=True)
        
        with col3:
            source = pd.DataFrame({"category": [1, 2, 3, 4, 5, 6], "value": [4, 6, 10, 3, 7, 8]})

            chart = alt.Chart(source).mark_arc().encode(
                theta=alt.Theta(field="value", type="quantitative"),
                color=alt.Color(field="category", type="nominal"),
            ).configure_legend(
                orient="bottom",
                labelFontSize=10,
                labelAlign="center",
                title=None
            ).properties(
                width=200,
                height=200
            )

            st.altair_chart(chart, theme="streamlit", use_container_width=True)

        with col4:
            show = st.write("""
                    <div style="border-radius: 25px;
                        background: #F0F8FF;
                        padding: 25px">
                        <p style="font-weight: bold; text-align: center; font-size: 20px"> 6,100 </p>
                        <p style="text-align: center; font-size: 15px"> # Undiagnosed Patients </p>
                    </div>
                """,
                unsafe_allow_html=True)
    
    st.markdown("""
            <div style="position: relative; left: 37.5%;">
                <vl style="border: 2px solid #FFA07A; height: 100px" />
            </ div>
            """, unsafe_allow_html=True)

    st.markdown("""
                <div align="left">
                    <hr width="75%" style="border: 2px solid #FFA07A;" />
                </ div>
                """, unsafe_allow_html=True)

    with st.container():
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            show = st.write("""
                    <div style="border-radius: 25px;
                        background: #F0F8FF;
                        padding: 25px">
                        <p style="font-weight: bold; text-align: center; font-size: 20px"> 2,203 </p>
                        <p style="text-align: center; font-size: 15px"> On Crysvita </p>
                    </div>
                """,
                unsafe_allow_html=True)
        
        with col2:
            source = pd.DataFrame({"category": [1, 2, 3, 4, 5, 6], "value": [4, 6, 10, 3, 7, 8]})

            chart = alt.Chart(source).mark_arc().encode(
                theta=alt.Theta(field="value", type="quantitative"),
                color=alt.Color(field="category", type="nominal"),
            ).configure_legend(
                orient="bottom",
                labelFontSize=10,
                labelAlign="center",
                title=None
            ).properties(
                width=200,
                height=200
            )

            st.altair_chart(chart, theme="streamlit", use_container_width=True)
        
        with col3:
            show = st.write("""
                    <div style="border-radius: 25px;
                        background: #F0F8FF;
                        padding: 25px">
                        <p style="font-weight: bold; text-align: center; font-size: 20px"> 5,705 </p>
                        <p style="text-align: center; font-size: 15px"> Not On Crysvita </p>
                    </div>
                """,
                unsafe_allow_html=True)
        
        with col4:
            pass
    
    st.markdown("""
            <div style="position: relative; left: 62.5%;">
                <vl style="border: 2px solid #FFA07A; height: 100px" />
            </ div>
            """, unsafe_allow_html=True)

    st.markdown("""
                <div align="right">
                    <hr width="75%" style="border: 2px solid #FFA07A;" />
                </ div>
                """, unsafe_allow_html=True)

    with st.container():
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            pass

        with col2:
            show = st.write("""
                    <div style="border-radius: 25px;
                        background: #F0F8FF;
                        padding: 25px">
                        <p style="font-weight: bold; text-align: center; font-size: 20px"> 533 </p>
                        <p style="text-align: center; font-size: 15px"> Other Market Basket </p>
                    </div>
                """,
                unsafe_allow_html=True)
        
        with col3:
            source = pd.DataFrame({"category": [1, 2, 3, 4, 5, 6], "value": [4, 6, 10, 3, 7, 8]})

            chart = alt.Chart(source).mark_arc().encode(
                theta=alt.Theta(field="value", type="quantitative"),
                color=alt.Color(field="category", type="nominal"),
            ).configure_legend(
                orient="bottom",
                labelFontSize=10,
                labelAlign="center",
                title=None
            ).properties(
                width=200,
                height=200
            )

            st.altair_chart(chart, theme="streamlit", use_container_width=True)

        with col4:
            show = st.write("""
                    <div style="border-radius: 25px;
                        background: #F0F8FF;
                        padding: 25px">
                        <p style="font-weight: bold; text-align: center; font-size: 20px"> 5,172 </p>
                        <p style="text-align: center; font-size: 15px"> Not On Any Therapy </p>
                    </div>
                """,
                unsafe_allow_html=True)


with tab2:

# Here we plot our sidebar visulizations using "with" notation
    with st.sidebar:
        textbox = st.markdown("""
            <div style="border-radius: 25px;
                background: #BEBEBE;
                padding: 25px;">
            <h3> Preset Parameters </h3>
            <b> Number of Reps </b>
            <p>
                KKUS: 26 <br />
                UCL & PDL: 42
            </p>
            <b> Capacity Per Rep </b>
            <p> 55 physicians </p>
            <b> Access </b>
            <p> 80% of physicians targeted are reached </p>
            </div>
        """,
        unsafe_allow_html=True)
        
        st.text("")

        textbox_1 = st.markdown("""
            <div style="
                border-radius: 25px;
                padding: 15px;
                background: #F0F8FF">
            
            <p>
                <b> Logic: </b> <br/>
                <ul>
                    <li style="font-size: 15px"> KKUS reps are always assigned the highest priority physicians </li>
                    <li style="font-size: 15px"> When new KKUS reps are added, they will be assigned to the available 
                        high priority physicians including physicians assigned to UCLs </li>
                    <li style="font-size: 15px"> Once physicians assigned to UCLs are reassigned to new KKUS reps, 
                        the UCLs too will be reassigned to remaining high priority physicians </li>
                </ul>
            </p>
            </div>
        """,
        unsafe_allow_html=True)

        # <a href="https://google.com" class="button">Go to Google</a>
        # <button> this is a button! </button>


        text = st.markdown("""
            <p> * Ctr + click the info icon for the definition of terms. </p>
        """,
        unsafe_allow_html=True)

    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            textbox_main_1 = st.write("""
                    <div style="border-radius: 25px;
                        background: #F0F8FF;
                        padding: 25px">
                        <p style="font-weight: bold"> A Targets </p>
                        <p style="text-align: left"> Total number: <b> 1316 </b> </p>
                        <p style="text-align: left"> Percent Assigned: <b> 100% </b> </p>
                    </div>
                """,
                unsafe_allow_html=True)
            # info_1 = st.info("""A Targets <br/>
            #                     Total Number: 1316
            #                     Percent Assigned: 100%
            #                 """)

        with col2:
            textbox_main_2 = st.write("""
                    <div style="border-radius: 25px;
                        background: #F0F8FF;
                        padding: 25px;">
                        <p style="font-weight: bold"> B Targets </p>
                        <p style="text-align: left"> Total number: <b> 1316 </b> </p>
                        <p style="text-align: left"> Percent Assigned: <b> 100% </b> </p>
                    </div>
                """,
                unsafe_allow_html=True)
            # info_2 = st.info("55 physicians")

        with col3:
            textbox_main_3 = st.write("""
                    <div style="border-radius: 25px;
                        background: #F0F8FF;
                        padding: 25px;">
                        <p style="font-weight: bold"> Prime Targets </p>
                        <p style="text-align: left"> Total number: <b> 1316 </b> </p>
                        <p style="text-align: left"> Percent Assigned: <b> 100% </b> </p>
                    </div>
                """,
                unsafe_allow_html=True)
            # info_3 = st.info("55 physicians")

    # st.write("")
    # st.selectbox(
    # 'Which company?',
    # ('KKUS', 'UCL&PDL', 'Unseen'))

    # Add some blank space to the main canvas
    for i in range(3):
        st.text("")


    st.altair_chart(chart_2, theme="streamlit")

    data = dict(
        number=[39, 27.4, 20.6, 11, 2],
        stage=["Website visit", "Downloads", "Potential customers", "Requested price", "invoice sent"])
    fig = px.funnel(data, x='number', y='stage')

    st.plotly_chart(fig, theme="streamlit")
