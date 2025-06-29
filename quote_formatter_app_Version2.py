import streamlit as st
import pandas as pd
import pdfplumber
import io
import re

# Function to extract text from uploaded PDF or text files
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text


# Function to parse quote lines from extracted text
def parse_quote_lines(text):
    lines = text.splitlines()
    data = []
    for line in lines:
        # Basic pattern to match lines with item info
        match = re.search(r"(\d+)\s+([A-Z0-9\-]+)\s+(.+?)\s+(\d+\.\d{2})\s+\$(\d+(?:,\d{3})*(?:\.\d{2})?)", line)
        if match:
            qty = int(match.group(1))
            cat_no = match.group(2)
            description = match.group(3).strip()
            unit_cost = float(match.group(4))
            line_cost = float(match.group(5).replace(",", ""))
            data.append({
                "QTY": qty,
                "CAT NO": cat_no,
                "Description": description,
                "COST PER UNIT": unit_cost,
                "LINE COST": line_cost
            })
    return data

# Function to apply margin and calculate selling prices
def apply_margin(data, margin_percent):
    for item in data:
        margin = margin_percent / 100
        unit_sell = item["COST PER UNIT"] * (1 + margin)
        total_sell = unit_sell * item["QTY"]
        gst = total_sell * 0.10
        item["MARGIN"] = f"{margin_percent:.2f}%"
        item["UNIT SELL EX GST"] = round(unit_sell, 2)
        item["TOTAL SELL EX GST"] = round(total_sell, 2)
        item["GST"] = round(gst, 2)
        item["TOTAL INC GST"] = round(total_sell + gst, 2)
    return data

# Streamlit UI
st.title("📦 Supplier Quote Formatter")
st.write("Upload supplier quote PDFs or text files, apply margin, and export formatted table.")

uploaded_files = st.file_uploader("Upload PDF or TXT files", type=["pdf", "txt"], accept_multiple_files=True)
margin = st.slider("Select Margin (%)", min_value=0, max_value=100, value=9)

if uploaded_files:
    all_data = []
    for uploaded_file in uploaded_files:
        text = extract_text_from_file(uploaded_file)
        parsed_data = parse_quote_lines(text)
        all_data.extend(parsed_data)

    if all_data:
        formatted_data = apply_margin(all_data, margin)
        df = pd.DataFrame(formatted_data)
        st.dataframe(df)

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download CSV", data=csv, file_name="formatted_supplier_quotes.csv", mime="text/csv")
    else:
        st.warning("No valid quote lines found in the uploaded files.")
else:
    st.info("Please upload one or more supplier quote files to begin.")
