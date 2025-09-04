import asyncio
from bleak import BleakClient

# 把你要连接的设备地址填进去（示例地址，替换为你自己的）
ADDRESS = "307C6CA0-4107-CF22-3359-7A0D17A54266"

async def list_services():
    async with BleakClient(ADDRESS) as client:
        # 确保连接成功
        if client.is_connected:
            print(f"Connected to {ADDRESS}")
            # get_services() 在 v1.0.1 是 coroutine，需要 await
            services = await client.get_services()
            for service in services:
                print(f"Service: {service}")
                for char in service.characteristics:
                    print(f"  Characteristic: {char} - {char.properties}")

if __name__ == "__main__":
    asyncio.run(list_services())
