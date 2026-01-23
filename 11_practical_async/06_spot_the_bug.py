import asyncio

async def ping():        # ye ek infinite background task hai.
    while True:
        await asyncio.sleep(5)
        print("ping")

async def main():
    for _ in range(100):
        asyncio.create_task(ping())
    await asyncio.sleep(1)
    """
    100 separate ping tasks create ho gaye Sab event loop ke paas register ho gaye
    Sab forever chalne ke liye bane hain. na track karne ka rasta hai na cancel karne ka.
    """

asyncio.run(main())

"""
1️⃣ Bug:

infinite tasks created

no tracking

no cancellation

2️⃣ Dangerous kyun:

long-running app mein RAM leak

zombie background tasks

3️⃣ Fix (concept):

task reference rakho

cancel on shutdown

avoid fire-and-forget blindly
"""