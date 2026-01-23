import asyncio

async def job():
    print("job start")
    while True:
        pass   # busy loop
        await asyncio.sleep(2)  # this is the correction.

async def main():
    task = asyncio.create_task(job())
    await asyncio.sleep(1)
    task.cancel()

asyncio.run(main())
