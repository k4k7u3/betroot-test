import asyncio
import random


async def fibo(name, number):
    prew = cur = 1
    print(f"Start function {name}")
    for i in range(number-2):
        prew, cur = cur, prew + cur
        await asyncio.sleep(0.8)
    print(f"End function {name}")
    return cur


async def fact(name, number):
    factor = 1
    print(f"Start function {name}")
    for i in range(2, number+1):
        factor *= i
        await asyncio.sleep(0.8)
    print(f"End function {name}")
    return factor


async def squares(name, number, exp):
    print(f"Start function {name}")
    await asyncio.sleep(0.8)
    number *= exp
    print(f"End function {name}")
    return number


async def main():
    number = random.randint(10, 20)
    print(f"Number = {number}")
    a= await asyncio.gather(
        fibo("Fibonacci", number),
        fact("Factorial", number),
        squares("Square", number, random.randint(10, 20)),
        )
    print(a)
    print(f"Fibonacci({number}) = {a[0]}, Factorial({number}) = {a[1]}, Square({number}) = {a[2]}")

asyncio.run(main())
