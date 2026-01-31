import asyncio

sem  = asyncio.Semaphore(5) #  5 requests at a time.

async def safe_fetch(url):
    async with sem:
        return await fetch(url)
    
async def main():
    tasks = [safe_fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)