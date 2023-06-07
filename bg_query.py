from google.cloud import bigquery

client = bigquery.Client()

query = """
SELECT * FROM `analytics-388412.dbt.customers` LIMIT 10
"""

query_job = client.query(query)

print("Tulis data dari bigquery.")
for row in query_job:
    print(f"customer_id = {row['customer_id']},first_name =  {row['first_name']}")