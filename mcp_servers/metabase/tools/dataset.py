import httpx
from base import get_metabase_client
import asyncio




async def metabase_get_dataset_list(
        database_id: int,
        table_id: int
):
    client = get_metabase_client()

    headers = {
        "Content-Type": "application/json",
        "X-Metabase-Session": client["auth_token"]
    }

    payload = {
        "type": "query",
        "database": database_id,
        "query": {
            "source-table": table_id
        }
    }

    async with httpx.AsyncClient(base_url=client["url"]) as session:
        resp = await session.post("/api/dataset", headers=headers, json=payload)
        print(resp.status_code, resp.text)

if __name__ == "__main__":
    asyncio.run(metabase_get_dataset_list(1,1))