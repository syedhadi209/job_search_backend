from app.db.get_db import get_database
from bson import ObjectId

async def fuzzy_search(query):
    db = await get_database()
    query_filter = {}
    
    # If query is provided, construct a regex filter for fuzzy search
    if query:
        query_filter["$or"] = [
            {"job_name": {"$regex": query, "$options": "i"}},  # Case insensitive fuzzy search on title
        ]
    
    # Execute the query and return results
    results = await db['jobs'].find(query_filter).to_list(length=None)

    # Convert ObjectId fields to strings
    for result in results:
        if '_id' in result and isinstance(result['_id'], ObjectId):
            result['_id'] = str(result['_id'])
    return results