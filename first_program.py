from google.cloud import bigquery

if __name__ == "__main__":
    client = bigquery.Client()
    query = ("""
        SELECT
         * EXCEPT(is_typed)
        FROM
        `admin.INFORMATION_SCHEMA.TABLES`
    """)

    query_job = client.query(query, location="EU")

    # for row in query_job:
    #     print(row)

    print(type(query_job.result()))
    for l in list(query_job.result()):
        print(dict(l).get('table_name'))

    # for s in client.schemas():
    #     print(s)
