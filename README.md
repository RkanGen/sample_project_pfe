![image](https://github.com/user-attachments/assets/32a734f6-9b2c-4797-9a30-852e9d0420bf)

# sample_project_pfe
![image](https://github.com/user-attachments/assets/2b76ab6e-700e-4657-a319-23013c335e74)

![image](https://github.com/user-attachments/assets/2840ab30-b269-4a1b-ac21-afc8bea04ff2)

![image](https://github.com/user-attachments/assets/8caf8103-0069-4d4b-83bd-a829ded87915)

---

 # S-Matrix to RLC Converter

This project provides an interactive interface to process S-matrix data, extract  values from endpoint CST Studio Suite, and visualize the results. It includes a FastAPI backend and a Streamlit frontend.

Features

1. FastAPI Backend:

Fetch S-matrix data in JSON or CSV format.

Process S-matrix to calculate  values.

2. Streamlit Frontend:

Fetch S-matrix data from the backend.

Process data to extract  values.

Display results in a table and graph.

Download or copy the results for further use.

---

### Getting Started

Prerequisites

Python (in case)

Required libraries:
```
fastapi

uvicorn

numpy

pandas

requests

streamlit

```

Install dependencies:
```
pip install fastapi uvicorn numpy pandas requests streamlit
```

---

Running the Project

Step 1: Start the FastAPI Backend

Run the FastAPI app:
```
uvicorn app:app --reload
```
The backend will be available at http://127.0.0.1:8000.

Step 2: Start the Streamlit Frontend

Run the Streamlit app:

streamlit run streamlit_app.py

The frontend will be available at http://localhost:8501.


---

### Usage

1. Fetch S-Matrix Data

Click "Fetch as JSON" or "Fetch as CSV" to retrieve S-matrix data.

If fetching as JSON, the data will be displayed in a table.

If fetching as CSV, the file will be downloaded.


2. Process S-Matrix Data

After fetching the data, click "Calculate RLC" to process the data.

The results will be displayed in a table and as a graph.


3. Copy or Download Results

Copy the results as plain text or download them as a CSV file.



---

API Endpoints

GET /get_s_matrix/

Fetch S-matrix data.

Parameters:

format: Output format (json or csv).


Example:

GET http://127.0.0.1:8000/get_s_matrix/?format=json

POST /process_s_matrix/

Process S-matrix data to calculate .

Request Body:

{
  "s_matrix": [[0.2, 0.1], [0.3, 0.15], [0.5, 0.2]]
}

Example:

POST http://127.0.0.1:8000/process_s_matrix/


---

# Project Structure
```
.
├── app.py              # FastAPI backend
├── streamlit_app.py    # Streamlit frontend
├── requirements.txt    # Python dependencies
└── README.md           # Documentation

```
---
### N.B Check the format of output of S-matrix from CST Studio Suite whether Json or csv 
