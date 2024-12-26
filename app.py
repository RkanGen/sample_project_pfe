
from fastapi import FastAPI
import numpy as np
import csv
from fastapi.responses import JSONResponse, StreamingResponse

app = FastAPI()

# Sample S-matrix data (simulate CST data)
S_MATRIX = [[0.2, 0.1], [0.3, 0.15], [0.5, 0.2]]  # Example values

@app.get("/get_s_matrix/")
def get_s_matrix(format: str = "json"):
    """
    Get S-matrix data in JSON or CSV format.
    """
    if format == "json":
        return {"s_matrix": S_MATRIX}
    elif format == "csv":
        # Stream CSV response
        def iter_csv():
            yield "S11,S12\n"
            for row in S_MATRIX:
                yield ",".join(map(str, row)) + "\n"

        return StreamingResponse(iter_csv(), media_type="text/csv", headers={"Content-Disposition": "attachment; filename=s_matrix.csv"})
    else:
        return {"error": "Invalid format. Use 'json' or 'csv'."}

@app.post("/process_s_matrix/")
def process_s_matrix(s_matrix: list[list[float]]): 
    frequencies = np.linspace(1e9, 10e9, len(s_matrix))
    rlc_values = []
    for idx, s_coeff in enumerate(s_matrix):
        f = frequencies[idx]
        z_in = compute_impedance(s_coeff)
        r = z_in.real
        l = z_in.imag / (2 * np.pi * f)
        c = -1 / (z_in.imag * 2 * np.pi * f) if z_in.imag != 0 else 0
        rlc_values.append({"frequency": f, "R": r, "L": l, "C": c})

    return {"rlc_values": rlc_values}

def compute_impedance(s_coeff):
    s11 = s_coeff[0]  # Assuming s_coeff is a list of S11, S12, etc.
    z0 = 50  # Characteristic impedance
    z_in = z0 * (1 + s11) / (1 - s11) if (1 - s11) != 0 else complex(z0, 0)
    return z_in
