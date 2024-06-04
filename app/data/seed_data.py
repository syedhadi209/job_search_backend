import csv
import os
from app.db.get_db import get_database

required_columns = ['post_id','job_name','company_name']

csv_file_path = os.path.join(os.path.dirname(__file__), 'jobs_data.csv')

async def seed_data_to_db():
    db = await get_database()

    with open(csv_file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)

        jobs_data = {}

        for row in csv_reader:
            await db['jobs'].insert_one({
                "job_name":row[1]
            })

seed_data_to_db()
