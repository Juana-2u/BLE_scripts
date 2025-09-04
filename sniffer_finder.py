def find_sniffer(write_data=False):
    # 暂时用手动路径测试
    port = '/dev/tty.usbserial-58BB0045651'  # 替换为你的串口路径
    rate = 1000000
    try:
        # 测试串口可用性
        reader = Packet.PacketReader(portnum=port, baudrate=rate)
        reader.doExit()
        return [port]  #返回字符串类型
    except Exception as e:
        print("Error opening serial port:", e)
        return []
