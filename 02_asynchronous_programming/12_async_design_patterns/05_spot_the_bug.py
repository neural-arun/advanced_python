async def main():
    sem = asyncio.Semaphore(5)
    for url in urls:
        async with sem:
            await fetch(url)


# above code is so wrong.
# below structure is fine.

sem = asyncio.Semaphore(5)

async def safe_fetch(url):
    async with sem:
        return await fetch(url)  # many tasks is been created which will be sent to event loop to be executed.

tasks = [safe_fetch(url) for url in urls]
async def main():
    results = await asyncio.gather(*tasks)
