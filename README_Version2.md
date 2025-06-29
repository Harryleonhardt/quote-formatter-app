# Supplier Quote Formatter

A simple Streamlit web app to upload supplier quote PDF or text files, parse and reformat their content, apply a margin, and export the results as a CSV.

## Features

- Upload multiple PDF or TXT files.
- Extracts and parses quote lines (quantity, catalog number, description, unit cost, line cost).
- Apply a markup margin to costs.
- Outputs a formatted table with GST calculation.
- Download the processed data as a CSV.

## Demo

![demo screenshot](demo_screenshot.png) <!-- Optional: add screenshot when available -->

## How to Use (Cloud Only)

### 1. Deploy on Streamlit Community Cloud (Recommended & Free)

1. [Create a GitHub account](https://github.com/) if you don't have one.
2. [Create a new repository](https://github.com/new) (e.g., `quote-formatter-app`) and upload these files:
    - `quote_formatter_app.py`
    - `requirements.txt`
    - `README.md`
3. Go to [Streamlit Cloud](https://share.streamlit.io/) and sign in with GitHub.
4. Click "New app" and select your repo and `quote_formatter_app.py` as the main file.
5. Click "Deploy". Your app will be live in the browser!

### 2. (Optional) Run in GitHub Codespaces or Replit

- Codespaces and Replit let you run Python apps in the cloud directly from your GitHub repo. Just import the repo and run!

---

## Dependencies

- streamlit
- pandas
- PyMuPDF

(Automatically installed on Streamlit Cloud.)

---

## Security & Privacy

- Your uploaded files are processed in-memory and not stored.

---

## Troubleshooting

- If you see errors about missing packages, check that `requirements.txt` is present and matches the file above.
