
# API Data Pipeline with Python and Databases

This project demonstrates a pipeline to extract weather data from the OpenWeatherMap API, process it using Python, save the data locally as a CSV file, and load it into Oracle, MySQL, and PostgreSQL databases.

---

## **Features**

1. **API Data Extraction**: Extract weather data for multiple cities using the OpenWeatherMap API.
2. **Data Processing**: Organize the extracted data into a structured DataFrame using Pandas.
3. **Data Storage**:
   - Save the data locally as a CSV file.
   - Load the data into Oracle, MySQL, and PostgreSQL databases using Python libraries.

---

## **Technologies Used**

- **Python Libraries**:
  - `requests`: To interact with the API.
  - `pandas`: For data processing and manipulation.
  - `sqlalchemy`: To manage database connections.
  - `cx_Oracle`, `mysql-connector-python`, `psycopg2`: Database-specific libraries.

- **Databases**:
  - Oracle
  - MySQL
  - PostgreSQL

- **Tools**:
  - DBeaver: For database management.

---

## **Setup Instructions**

### **1. Prerequisites**

- Python 3.7+
- DBeaver installed ([Download here](https://dbeaver.io/)).
- Oracle, MySQL, and PostgreSQL databases set up and accessible.
- OpenWeatherMap API key ([Get it here](https://openweathermap.org/)).

### **2. Install Required Python Libraries**

Run the following command to install the required libraries:

```bash
pip install pandas sqlalchemy cx_oracle mysql-connector-python psycopg2 requests
```

### **3. Configure the OpenWeatherMap API Key**

Replace `api_key` in the Python code with your actual API key.

### **4. Set Up Databases**

- Create Oracle, MySQL, and PostgreSQL databases.
- Note the connection details (host, port, user, password, database name) for each.

### **5. Execute the Python Script**

#### **Extract Data from API**
Run the following script to fetch weather data and create a DataFrame:

```python
import requests
import pandas as pd

API_KEY = "api_key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
CITIES = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Paris", "New York"]

data = []
for city in CITIES:
    response = requests.get(BASE_URL, params={"q": city, "appid": API_KEY, "units": "metric"})
    if response.status_code == 200:
        weather_data = response.json()
        data.append({
            "City": city,
            "Temperature (°C)": weather_data["main"]["temp"],
            "Humidity (%)": weather_data["main"]["humidity"],
            "Weather": weather_data["weather"][0]["description"]
        })
    else:
        print(f"Error fetching data for {city}: {response.status_code}")

# Create DataFrame
df = pd.DataFrame(data)
```

#### **Save Data Locally as CSV**

```python
import os

output_dir = "output_data"
os.makedirs(output_dir, exist_ok=True)

csv_file = os.path.join(output_dir, "weather_data.csv")
df.to_csv(csv_file, index=False)

print(f"CSV file saved at: {csv_file}")
```

#### **Load Data into Databases**

Replace the connection strings with the appropriate details for your Oracle, MySQL, and PostgreSQL databases, and run the following script:

```python
from sqlalchemy import create_engine

def save_to_db(df, connection_string, table_name):
    engine = create_engine(connection_string)
    with engine.connect() as conn:
        df.to_sql(table_name, conn, if_exists="replace", index=False)

# Database connection strings
oracle_conn = "oracle+cx_oracle://user:password@host:port/service_name"
mysql_conn = "mysql+mysqlconnector://user:password@host:port/database_name"
postgresql_conn = "postgresql+psycopg2://user:password@host:port/database_name"

# Load data into databases
save_to_db(df, oracle_conn, "weather_data")
save_to_db(df, mysql_conn, "weather_data")
save_to_db(df, postgresql_conn, "weather_data")

print("Data loaded into databases!")
```

---

## **Expected Outputs**

1. A CSV file named `weather_data.csv` saved in the `output_data` folder.
2. Weather data loaded into the `weather_data` table in Oracle, MySQL, and PostgreSQL databases.

---

## **Future Enhancements**

- Add error handling for database connections.
- Schedule regular API calls to update the database with the latest weather data.
- Implement a web interface to display the data from the databases.

---

## **Acknowledgments**

- [OpenWeatherMap API](https://openweathermap.org/) for the weather data.
- [DBeaver](https://dbeaver.io/) for database management.
