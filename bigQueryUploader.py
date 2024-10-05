from google.cloud import bigquery
import os
from datetime import datetime

credentials_path = 'keys/big-query-service-account-key.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

table_id = 'united-triode-437113-j0.gcp_bigquery_task.get-item-logs'
envName = os.getenv('ServiceName')

def logDataToBigQuery(executionTime: str, value: float) -> None:

    client = bigquery.Client()
    rows_to_insert = [
        {u'executionTime':executionTime, u'value':value, u'timestamp': f'{datetime.now()}', u'serviceName':envName},
    ]
    client.insert_rows_json(table_id, rows_to_insert)

