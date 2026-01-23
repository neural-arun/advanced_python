import asyncio
async def fetch(url):
    await asyncio.sleep(1)   # pretend network
    return f"data from {url}"

async def main():
    urls = ["a", "b", "c", "d"]

    tasks = [fetch(u) for u in urls]
    results = await asyncio.gather(*tasks)

    print(results)

asyncio.run(main())
