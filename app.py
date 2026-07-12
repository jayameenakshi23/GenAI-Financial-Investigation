import streamlit as st
import pandas as pd
import os

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

from services.ai_service import investigate_transaction
from utils.charts import show_risk_chart, show_amount_chart

st.set_page_config(
    page_title="GenAI Financial Investigation Assistant",
    page_icon="🏦",
    layout="wide"
)

# ---------------- Sidebar ---------------- #

st.sidebar.title("🏦 Bank Dashboard")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Upload Transactions",
        "AI Investigation",
        "Reports"
    ]
)

# ---------------- Main Page ---------------- #

st.title("🏦 GenAI Financial Investigation Assistant")

st.markdown("---")

# ---------------- Dashboard Metrics ---------------- #

default_file = "data/transaction.csv"

if os.path.exists(default_file):
    dashboard_df = pd.read_csv(default_file)

    total_transactions = len(dashboard_df)

    suspicious_transactions = len(
        dashboard_df[
            dashboard_df["Risk_Flag"].isin(["Medium", "High"])
        ]
    )

    high_risk_cases = len(
        dashboard_df[
            dashboard_df["Risk_Flag"] == "High"
        ]
    )

else:
    total_transactions = 0
    suspicious_transactions = 0
    high_risk_cases = 0

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Transactions", total_transactions)

with col2:
    st.metric("Suspicious Transactions", suspicious_transactions)

with col3:
    st.metric("High Risk Cases", high_risk_cases)

st.markdown("---")

# ---------------- Home ---------------- #

if menu == "Home":

    st.header("🏦 Welcome to the GenAI Financial Investigation Assistant")

    st.success("AI-powered fraud investigation system for banking transactions.")

    st.markdown("""
            ### Features

- 🤖 AI-powered fraud investigation using Llama 3.2
- 📂 Upload transaction datasets
- 📊 Interactive fraud analytics dashboard
- 📄 PDF investigation report generation
- 📥 CSV report download
- 🚨 Risk level analysis
""")
# ---------------- Upload Transactions ---------------- #

elif menu == "Upload Transactions":

    st.header("📂 Upload Transaction File")

    uploaded_file = st.file_uploader(
        "Choose a CSV file",
        type=["csv"]
    )

    default_file = "data/transaction.csv"

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

    elif os.path.exists(default_file):
        df = pd.read_csv(default_file)

    else:
        df = None

    if df is not None:

        st.success("✅ Transaction data loaded successfully!")

        st.subheader("Transaction Preview")

        st.dataframe(df, use_container_width=True)

# ---------------- AI Investigation ---------------- #

elif menu == "AI Investigation":

    st.header("🤖 AI Fraud Investigation")

    default_file = "data/transaction.csv"

    if os.path.exists(default_file):

        df = pd.read_csv(default_file)

        transaction = st.selectbox(
            "Select a Transaction",
            df["Transaction_ID"]
        )

        if st.button("Investigate"):

            selected = df[
                df["Transaction_ID"] == transaction
            ].iloc[0]

            with st.spinner("Analyzing Transaction..."):

                result = investigate_transaction(
                    selected.to_dict()
                )

            st.success("Investigation Completed")

            st.markdown("## 📝 AI Investigation Report")

            st.markdown(result)

    else:

        st.warning("No transaction file found.")

# ---------------- Reports ---------------- #


elif menu == "Reports":

    st.header("📄 Investigation Reports")

    if os.path.exists(default_file):

        report_df = pd.read_csv(default_file)
        search = st.text_input("🔍 Search Transaction ID")
        risk_filter = st.selectbox(
            "Filter by Risk Level",
             ["All", "Low", "Medium", "High"]
            )

        if risk_filter != "All":
             report_df = report_df[
                 report_df["Risk_Flag"] == risk_filter
             ]

        if search:
         report_df = report_df[
            report_df["Transaction_ID"].astype(str).str.contains(search, case=False)
    ]

        total = len(report_df)

        low = len(report_df[report_df["Risk_Flag"] == "Low"])
        medium = len(report_df[report_df["Risk_Flag"] == "Medium"])
        high = len(report_df[report_df["Risk_Flag"] == "High"])

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total", total)
        col2.metric("Low Risk", low)
        col3.metric("Medium Risk", medium)
        col4.metric("High Risk", high)

        st.markdown("---")

        st.subheader("📋 Recent Transactions")

        st.dataframe(report_df, use_container_width=True)

        st.markdown("---")

        show_risk_chart(report_df)

        st.markdown("---")

        show_amount_chart(report_df)

        st.markdown("---")

        # ---------------- CSV Download ---------------- #

        csv = report_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="⬇ Download CSV Report",
            data=csv,
            file_name="Investigation_Report.csv",
            mime="text/csv"
        )

        # ---------------- PDF Report ---------------- #

        os.makedirs("reports", exist_ok=True)

        styles = getSampleStyleSheet()

        pdf_file = "reports/Investigation_Report.pdf"

        doc = SimpleDocTemplate(pdf_file)

        elements = []

        elements.append(
            Paragraph(
                "<b>GenAI Financial Investigation Report</b>",
                styles["Title"]
            )
        )

        elements.append(Paragraph("<br/>", styles["Normal"]))

        elements.append(
            Paragraph(f"Total Transactions : {total}", styles["Normal"])
        )

        elements.append(
            Paragraph(f"Low Risk : {low}", styles["Normal"])
        )

        elements.append(
            Paragraph(f"Medium Risk : {medium}", styles["Normal"])
        )

        elements.append(
            Paragraph(f"High Risk : {high}", styles["Normal"])
        )

        elements.append(
            Paragraph("<br/>Recent Transactions", styles["Heading2"])
        )

        for _, row in report_df.iterrows():

            elements.append(

                Paragraph(

                    f"{row['Transaction_ID']} | "
                    f"{row['Customer_ID']} | "
                    f"₹{row['Amount']} | "
                    f"{row['Risk_Flag']}",

                    styles["Normal"]

                )

            )

        doc.build(elements)

        with open(pdf_file, "rb") as pdf:

            st.download_button(
                label="📄 Download PDF Report",
                data=pdf,
                file_name="Investigation_Report.pdf",
                mime="application/pdf"
            )

    else:

        st.warning("No transaction data available.")