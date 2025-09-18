import httpx
from base import get_metabase_client
import asyncio




async def metabase_get_database_list():
    client = get_metabase_client()

    headers = {
        "Content-Type": "application/json",
        "X-Metabase-Session": client['auth_token']
    }
    async with httpx.AsyncClient(base_url=client['url']) as client:
        resp = await client.get("/api/database", headers=headers)
        print(resp.status_code, resp.text)


async def metabase_get_database_by_id(id: int):


    client = get_metabase_client()

    headers = {
        "Content-Type": "application/json",
        "X-Metabase-Session": client['auth_token']
    }
    async with httpx.AsyncClient(base_url=client['url']) as client:
        resp = await client.get(f"/api/database/{id}", headers=headers)
        print(resp.status_code, resp.text)

if __name__ == "__main__":
    asyncio.run(metabase_get_database_list())
    asyncio.run(metabase_get_database_by_id(1))