import asyncio

async def one_second() -> None:
    count = 0
    while True:
        await asyncio.sleep(1)
        count += 1
        print(f"прошло {count} секунд")


async def five_second() -> None:
    while True:
        await asyncio.sleep(5)
        print(f"прошло еще 5 секнуд")


async def main() -> None:
    function1 = asyncio.create_task(one_second())
    function2 = asyncio.create_task(five_second())

    await function1
    await function2