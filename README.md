<img width="1302" height="932" alt="image" src="https://github.com/user-attachments/assets/b7796261-31cd-4431-a7c8-4c39066614e9" />


## SimpleFOCStudio 汉化版中文自述

SimpleFOCStudio 是基于 PyQt5 的图形化工具，用于通过串口或无线（TCP）连接对基于 SimpleFOC 库的 BLDC/步进电机控制器进行实时调参、监控与代码生成。

### 主要功能
- 即插即用（针对 SimpleFOC v2.1）
- 电机参数实时整定（PID/LPF、限幅、扭矩/控制模式等）
- 实时曲线监控（角度、速度、电压/电流等）
- 一键生成 Arduino 参数代码，便于将整定结果迁移到固件
- 集成串口终端与自定义命令面板

### 环境要求
- Python 3.9（建议）
- 依赖：见 `requirements.txt`

### 安装步骤
1) 安装 Python（或使用 Anaconda 创建环境）：
```sh
conda create -n simplefoc python=3.9.0
conda activate simplefoc
```
2) 安装依赖：
```sh
pip install -r requirements.txt
```

### 启动程序
```sh
python simpleFOCStudio.py
```
（使用 Anaconda 时，先 `conda activate simplefoc` 再运行上面命令。）

### 快速上手
1) 打开程序后，点击工具栏中的“添加电机”按钮（小电机图标），选择“树形视图”或“表单视图”。
2) 配置连接：
   - 串口：选择端口、波特率等参数，点击“连接”。
   - 无线：在“配置连接”对话框选择“无线”，填写 IP 和端口后连接。
3) 连接成功后可在界面中：
   - 修改控制模式（力矩/速度/角度/开环等）与 PID/LPF 参数；
   - 设置限幅（速度/电压/电流），传感器零点/电气零偏；
   - 在“图形”页查看实时曲线；
   - 使用“点动控制”面板进行简单目标控制；
   - 打开“命令行”窗口查看/发送 Commander 指令。

### 代码生成（Arduino）
当参数整定完成后，在工具栏点击“生成代码”，选择需要生成的参数组，系统会在新标签页中生成对应的 Arduino 片段，将其复制到固件 `setup()` 初始化附近（`motor.init()` 之前）即可。

### 自定义命令
若在固件中扩展了 Commander 接口（如 `command.add('M', doMotor, "motor")`），可在“自定义命令”树中添加命令并执行，用于修改寄存器、触发动作等。

### 集成串口终端
命令行窗口会显示设备的原始输出，也可直接发送 Commander 指令。

提示：如下消息为下位机（固件）输出，非上位机生成：
- `D-BOT ESP32S3 SimpleFOC Device`
- `FOC READY`
- `Wireless Tuning Server Ready`

### 常见问题（FAQ）
- 无法连接串口？
  - 确认端口号与波特率，检查占用情况与驱动。
- 无法连接无线？
  - 核对 IP/端口，确保固件侧开启了 TCP 服务器，并处于同一网络。
- 曲线无数据？
  - 在“图形”页点击“开始”，确认固件侧 `motor.monitor()` 与监控变量配置正确。

### 打包（可选）
可使用 PyInstaller 本地打包：
```sh
pyinstaller -F -w simpleFOCStudio.py
```

### 目录结构简述
- `src/gui/`：界面代码（工具栏、主窗口、各配置面板、资源）
- `src/simpleFOCConnector.py`：上位机与设备通信与数据解析
- `DOC/`：示例动图与截图

### 许可证
详见仓库中的 `LICENSE` 文件。


### 版权声明
- 本项目的著作权及其相关权利归原作者/原仓库所有。
- 本人仅对界面与文档进行中文本地化（汉化）等轻量改动，不涉及核心功能逻辑的原创性变更。
- 本项目的使用、复制、修改与分发，均应严格遵循原仓库的许可协议（LICENSE）；如与本文档描述存在差异，以原许可文件为准。
- 若原作者或版权方对此有进一步要求，请以其公告为准，并可联系我进行相应调整或移除。





