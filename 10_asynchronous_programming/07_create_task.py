import asyncio

async def worker():
    print("Worker start")
    await asyncio.sleep(2)
    print("worker end")

async def main():
    asyncio.create_task(worker())  # worker background mein register ho gya hai jab event loop free hoga tab isko chala dega.
    print("main continues")
    await asyncio.sleep(3)

asyncio.run(main())