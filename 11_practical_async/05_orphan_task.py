# orphan task happens when you

"""
❌ asyncio.create_task() but no reference
❌ No cancellation on shutdown
❌ Infinite background tasks
❌ Fire-and-forget everywhere
"""

# Bad task example:

# async def handler():
#     asyncio.create_task(long_job())
#     return "ok"

# good task example:
import asyncio
tasks = set()   # Stores references to running background tasks


async def long_job():
    await asyncio.sleep(5)


async def handler():
    task = asyncio.create_task(long_job())
    tasks.add(task)                         # If no reference exists → Python may destroy the task
    task.add_done_callback(tasks.discard)

"""
When the task finishes

Call tasks.discard(task)

Remove it from the set

Free memory automatically
"""

"""
Task tracked ✔

Cleanup automatic ✔

No orphan ✔
"""