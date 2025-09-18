import httpx
from base import get_metabase_client
import asyncio




async def metabase_get_task_list():
    client = get_metabase_client()

    headers = {
        "Content-Type": "application/json",
        "X-Metabase-Session": client['auth_token']
    }
    async with httpx.AsyncClient(base_url=client['url']) as client:
        resp = await client.get("/api/task", headers=headers)
        print(resp.status_code, resp.text)


if __name__ == "__main__":
    asyncio.run(metabase_get_task_list())