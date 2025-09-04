# BLE_scripts
基于 **Python** 的脚本，用于在 **Wireshark 配置完成** 的情况下，对 **BLE (Bluetooth Low Energy)** 数据包进行抓取和简单的重放测试。  

其中部分功能依赖 macOS 自带的 BLE 模块，重放逻辑基于 [bleak](https://github.com/hbldh/bleak) 框架实现。  

⚠️ 本项目仅供学习与研究 BLE 协议使用，禁止用于非法用途。

在Wireshark配置完成的情况下，使用macOS自带的BLE模块进行重放攻击脚本

使用顺序
1. sniffer_finder.py - 测试sniffer模块的串口
2. devices_discover.py - 获取蓝牙设备的设备地址
3. device_status.py - 测试指定 BLE 设备是否可用
4. command_script.py - 基于 Wireshark 抓取的数据，进行 BLE 指令的重放实验

## 依赖环境
- macOS (测试环境)
- Python 3.8+
- 依赖库：
  ```bash
  pip install bleak pyserial
  ```
