import asyncio

async def job():
    print("job start")
    await asyncio.sleep(1)
    print("job end")

async def main():
    asyncio.create_task(job())
    await asyncio.sleep(0.1)

asyncio.run(main())


#yaha par main function shuts down before job() function completes. task gets cancelled before finishing.