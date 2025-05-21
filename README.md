# 📄 SEC Common Stock Filer — Streamlining Schedule 13D Analysis

![Deployed on Streamlit](https://img.shields.io/badge/Deployed-Streamlit-orange)
![Efficiency Boost](https://img.shields.io/badge/Productivity+Up-125%25-brightgreen)
![Powered by OpenAI](https://img.shields.io/badge/OpenAI-API-blue)

## 🔗 [Instructions & Demo Guide](https://www.canva.com/design/DAGb0qlASmU/TULDjcUx6GjvENKRvsaoeA/view?utm_content=DAGb0qlASmU&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h43ecb3e9d4)

---

## 📘 Project Overview

This tool was developed as part of an applied research assistantship under **Professor Carmen Payne-Mann** at the **University of Southern California**. It automates the extraction of **common stock transaction data** from SEC **Schedule 13D filings**, significantly reducing the time required for manual data entry.

> 🕒 Before: ~1 hour per 10 filings  
> ⚡ After: ~1 hour per 25 filings  
> **Result:** ~125% increase in efficiency

---

## 💡 How It Works

Using the **OpenAI GPT model** via API, the application parses raw `.txt` Schedule 13D files and extracts relevant common stock transactions. Users upload individual text files, and the tool returns a clean `.csv` with the following columns:

- 📅 Trade Date  
- 📈 Share Count  
- 💵 Buy/Sell Indicator  
- 💰 Transaction Price

**Note:** The tool omits secondary columns (e.g., footnotes, indirect ownership) to maximize parsing accuracy.

---

## 👤 Designed for Research Assistants

This app is **not designed for bulk scraping**. Instead, it is intended to **supplement human analysis** by speeding up routine entry tasks, especially when working with SEC filings manually downloaded from EDGAR.

- 🔍 **Upload files one at a time** for optimal accuracy.
- 🚫 Avoid uploading filings **without transaction details**, as these will still generate a CSV with no rows, which may be confusing.

---

## ⚙️ Deployment & Architecture

This is my **first end-to-end deployed application** using GitHub and Streamlit:

- ✅ Front-end built in **Streamlit**
- 🚀 Hosted via **Streamlit Cloud**
- 🧠 Integrated with **OpenAI GPT API** for natural language parsing
- 📂 Outputs downloadable CSVs for each file

Currently used by a team of **3 Research Assistants** at USC.

---

## 🧪 Challenges & Solutions

### 🔐 API Key Handling
**Challenge:**  
Allowing users to input and validate their own OpenAI API key securely.

**Solution:**  
Implemented `st.session_state` in Streamlit to persist the API key across user sessions. The "Validate" button runs a demo API call to check for authentication before storing the key in session.

---

### 📦 Efficient DataFrame Handling
**Challenge:**  
Passing the main transaction DataFrame across multiple parsing steps without unnecessary copies.

**Solution:**  
Optimized performance by passing references to the original DataFrame rather than creating new instances. Reduced memory overhead and latency.

---

### 🔗 Front-End ↔ Logic Integration
**Challenge:**  
Tying the upload/parse button functionality on Streamlit’s UI to the inner logic parsing layer.

**Solution:**  
Modularized parsing logic, used callbacks, and ensured that the uploaded file content flows directly into the transaction pipeline and outputs a downloadable file.

---

## 📂 Repository Structure

```bash
📁 __pycache__/                 # Compiled Python bytecode cache
📄 .gitignore                  # Standard Git ignore rules
📄 README.md                   # Project documentation
📄 requirements.txt            # Python dependencies

📄 frontend.py                 # Streamlit front-end (file uploader, UI)
📄 processor.py                # Core GPT API logic and parsing
📄 download_txt.py            # Handles download / return of final CSV
📄 text_file_pipeline.py      # End-to-end file parsing pipeline and date formatting
