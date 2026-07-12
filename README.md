# 🏦 GenAI Financial Investigation Assistant

An AI-powered financial investigation application that helps bank fraud analysts investigate suspicious transactions using **Generative AI**. The system leverages **Llama 3.2** running locally through **Ollama** to generate intelligent investigation reports with risk assessment, evidence, and actionable recommendations.

---

## 📌 Overview

Financial institutions process millions of transactions every day, making manual fraud investigation time-consuming and inefficient.

The **GenAI Financial Investigation Assistant** automates the investigation process by allowing analysts to upload transaction data, analyze suspicious transactions, and generate AI-powered investigation reports through a simple and interactive dashboard.

---

## ✨ Features

- 🤖 AI-powered transaction investigation using **Llama 3.2**
- 📂 Upload and analyze transaction datasets
- 📊 Interactive fraud analytics dashboard
- 📈 Risk distribution visualization
- 💰 Transaction amount analysis
- 🔍 Search transactions by Transaction ID
- 🚨 Filter transactions by Risk Level
- 📄 Export investigation reports as PDF
- 📥 Download transaction data as CSV
- 🖥️ Fully local AI execution using Ollama (No cloud API required)

---

## 🛠️ Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Frontend | Streamlit |
| Large Language Model | Llama 3.2 |
| LLM Runtime | Ollama |
| Data Processing | Pandas |
| Data Visualization | Plotly |
| PDF Generation | ReportLab |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

```text
GenAI-Financial-Investigation/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── transaction.csv
│
├── reports/
│
├── services/
│   └── ai_service.py
│
├── utils/
│   └── charts.py
│
└── generate_dataset.py
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/jayameenakshi23/GenAI-Financial-Investigation.git
```

### 2. Navigate to the project

```bash
cd GenAI-Financial-Investigation
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Install Ollama

Download and install Ollama from:

https://ollama.com

Pull the Llama model:

```bash
ollama pull llama3.2
```

Verify installation:

```bash
ollama list
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📊 Dashboard Features

The application provides:

- Total Transactions
- Suspicious Transactions
- High Risk Cases
- Risk Distribution Pie Chart
- Transaction Amount Analysis
- Search Transactions
- Risk Level Filtering

---

## 🤖 AI Investigation Workflow

```
Transaction Dataset
        │
        ▼
Upload CSV File
        │
        ▼
Select Transaction
        │
        ▼
Llama 3.2 Analysis
        │
        ▼
AI Investigation Report
        │
        ▼
Risk Assessment
Reasons
Recommendations
        │
        ▼
Export PDF / CSV
```

---

## 📄 Sample AI Output

The AI generates an investigation report containing:

- Risk Level
- Executive Summary
- Investigation Reasons
- Supporting Evidence
- Recommendations

---

## 🎯 Business Benefits

- Reduces manual fraud investigation effort
- Speeds up decision-making
- Assists fraud analysts with AI-generated insights
- Provides downloadable investigation reports
- Improves operational efficiency

---

## 🚀 Future Enhancements

- User Authentication
- Database Integration
- Investigation History
- Email Notifications
- Real-time Transaction Monitoring
- Multi-LLM Support
- Cloud Deployment

---

## 👩‍💻 Author

**Jaya Meenakshi N**

Electronics and Communication Engineering

Interested in:
- Data Analytics
- Generative AI
- Machine Learning
- Python Development

GitHub:
https://github.com/jayameenakshi23

---

## ⭐ Project Status

✅ Completed

Built as a portfolio project to demonstrate practical applications of **Generative AI**, **Python**, and **Data Analytics** in financial fraud investigation.