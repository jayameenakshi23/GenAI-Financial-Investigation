import streamlit as st
import plotly.express as px


def show_risk_chart(df):

    risk_counts = df["Risk_Flag"].value_counts().reset_index()

    risk_counts.columns = ["Risk Level", "Count"]

    fig = px.pie(
        risk_counts,
        names="Risk Level",
        values="Count",
        title="Risk Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)


def show_amount_chart(df):

    fig = px.bar(
        df,
        x="Transaction_ID",
        y="Amount",
        color="Risk_Flag",
        title="Transaction Amount Analysis"
    )

    st.plotly_chart(fig, use_container_width=True)