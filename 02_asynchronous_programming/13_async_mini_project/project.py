# This project shows that async is faster than sync.

import time
import asyncio

def sync_fetch(url):
    time.sleep(1)
    return f"data from {url}"

async def async_fetch(url):
    await asyncio.sleep(1)
    return f"data from {url}"

def sync_main(urls):
    start = time.time()
    results = []

    for url in urls:
        results.append(sync_fetch(url))

    print("Sync time:", time.time() - start)
    return results


async def async_main(urls):
    start = time.time()

    tasks = [async_fetch(url) for url in urls]
    results = await asyncio.gather(*tasks)

    print("Async time:", time.time() - start)
    return results


urls = [f"url{i}" for i in range(10)]

sync_main(urls)
asyncio.run(async_main(urls))
