# GSS Interactive Dashboard: Gender, Work, and Attitudes

An interactive web dashboard built with Python, Dash, and Plotly to explore relationships between gender, income, job prestige, and societal attitudes using data from the 2018 General Social Survey (GSS).

## 🚀 Live Demo

**View the live, deployed dashboard here: [https://mieraci.pythonanywhere.com/](https://mieraci.pythonanywhere.com/)** 

![Dashboard Screenshot](screenshot.png)


## Features

* **Interactive Controls:** Users can select different survey questions and demographic groups to generate custom bar plots on the fly.
* **Data Visualization:** Leverages Plotly to create a variety of interactive charts.
* **Fully Deployed:** The entire application is deployed on PythonAnywhere, making it publicly accessible.

## How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/mieraci22/gss-interactive-dashboard.git](https://github.com/mieraci22/gss-interactive-dashboard.git)
    cd your-repo-name
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the app:**
    ```bash
    python app.py
    ```
    The dashboard will be available at `http://127.0.0.1:8050/`.

## Technologies Used

* Python
* Dash & Plotly
* Pandas
* PythonAnywhere