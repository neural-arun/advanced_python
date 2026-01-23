import asyncio

async def job():
    print("job start")
    await asyncio.sleep(5)
    print("job end")

async def main():
    task = asyncio.create_task(job())
    await asyncio.sleep(1)
    task.cancel()

asyncio.run(main())

# job end nahi aayega
# Task was CANCELLED while WAITING