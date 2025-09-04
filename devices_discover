import asyncio
from bleak import BleakScanner

async def scan():
    devices = await BleakScanner.discover(timeout=5.0)
    for d in devices:
        print(f"Name: {d.name}, Address: {d.address}")

asyncio.run(scan())
