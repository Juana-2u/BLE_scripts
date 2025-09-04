import asyncio
from bleak import BleakClient

DEVICE_ADDRESS = "307C6CA0-4107-CF22-3359-7A0D17A54266"
CHAR_UUID = "ac7bc836-6b69-74b6-d64c-451cc52b476e"
TURN_ON_COMMAND = bytes.fromhex("0e000000000000000000000416020181")

async def main():
    async with BleakClient(DEVICE_ADDRESS) as client:
        print(f"🔌 已连接: {DEVICE_ADDRESS}")
        await client.write_gatt_char(CHAR_UUID, TURN_ON_COMMAND, response=True)
        print("💡 开灯指令已发送")

asyncio.run(main())
