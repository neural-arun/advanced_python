import asyncio
import aiohttp

async def main():
    session = aiohttp.ClientSession()
    print(session)
    await session.close()

asyncio.run(main())