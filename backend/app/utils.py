import pandas as pd
from .database import get_db

def fetch_containers_from_db():
    db = get_db()
    query = "SELECT id, latitude, longitude, status FROM containers"
    df = pd.read_sql(query, db)
    return df.to_dict(orient='records')
