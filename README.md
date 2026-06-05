# 🛡️ Laser Security System

A comprehensive real-time intrusion detection system that combines hardware sensors with intelligent software alerting. This project uses a laser-based LDR (Light Dependent Resistor) sensor connected to an Arduino microcontroller, which communicates with a Python application to detect intruders and send immediate email alerts.

## 📋 Overview

The Laser Security System is designed to provide reliable perimeter security by detecting when a laser beam is blocked by an intruder. The system operates on three levels:

1. **Hardware Level**: Arduino-based laser detection and immediate physical alerts (buzzer & LED)
2. **Communication Layer**: Serial connection between Arduino and Python application
3. **Alert Layer**: Real-time email notifications with safety guidance

## 🎯 Key Features

- ✅ **Real-time Laser Detection**: LDR sensor detects laser beam interruption with 100ms response time
- ✅ **Immediate Physical Alerts**: Buzzer and LED activate instantly upon detection
- ✅ **Email Notifications**: Automated email alerts sent to configured recipients
- ✅ **Event Logging**: CSV-based intrusion logging with timestamps for audit trails
- ✅ **Safety Guidance**: Email alerts include emergency response instructions
- ✅ **Continuous Monitoring**: 24/7 monitoring with persistent data logging
- ✅ **Easy Integration**: Serial communication protocol for simple system expansion

## 🔧 Hardware Requirements

### Components
- **Arduino Microcontroller** (Arduino Uno, Nano, or compatible)
- **LDR (Light Dependent Resistor)** - Laser light detector
- **Laser Pointer/Module** - IR or visible laser (non-damaging)
- **Buzzer** - Audio alarm (active buzzer recommended)
- **LED** - Visual indicator (red recommended)
- **USB Cable** - Arduino programming and power
- **Resistors**: 10kΩ (for LDR), 220Ω (for LED)
- **Power Supply**: 5V USB or external power

### Pin Configuration
```
LDR Digital Output  → Arduino Pin 6
Buzzer             → Arduino Pin 11
LED                → Arduino Pin 9
```

## 💻 Software Requirements

### Python Application
- Python 3.7+
- Required Libraries:
  - `pyserial` - Serial communication with Arduino
  - `smtplib` - Email sending (built-in)
  - `email` - Email formatting (built-in)
  - `csv` - Data logging (built-in)
  - `datetime` - Timestamp generation (built-in)

### Arduino
- Arduino IDE or compatible compiler
- Board: Arduino AVR (or compatible)

## 📦 Installation

### 1. Hardware Setup

1. **Connect Components to Arduino**:
   - LDR sensor data output → Pin 6
   - Buzzer positive → Pin 11 (through 220Ω resistor if needed)
   - LED positive → Pin 9 (through 220Ω resistor)
   - Laser pointer → Power source (position to hit LDR continuously)

2. **Install Arduino Firmware**:
   - Open Arduino IDE
   - Load `arduino.c` sketch
   - Select your board type and COM port
   - Upload to Arduino

### 2. Python Application Setup

1. **Install Dependencies**:
   ```bash
   pip install pyserial
   ```

2. **Configure Email Settings** (Edit `intruder_alert.py`):
   ```python
   SMTP_SERVER = "smtp.gmail.com"      # Gmail SMTP server
   SMTP_PORT = 587                      # Gmail TLS port
   EMAIL_SENDER = "your-email@gmail.com"
   EMAIL_PASSWORD = "your-app-password" # Use Gmail App Password
   EMAIL_RECEIVER = "alert@example.com" # Recipient email
   ```

3. **Configure Serial Port** (Edit `intruder_alert.py`):
   ```python
   ser = serial.Serial('COM7', 9600, timeout=1)  # Change COM7 to your Arduino port
   ```

   To find your Arduino port:
   - Windows: Device Manager → COM & LPT Ports
   - Linux/Mac: `ls /dev/tty*` or `dmesg | grep ttyUSB`

### 3. Run the System

```bash
python intruder_alert.py
```

Expected output:
```
🔄 Waiting for Arduino data...
📡 Received from Arduino: Laser Detected - System Monitoring
```

## 🔐 Security Configuration

### Gmail Setup (Recommended)
1. Enable 2-Factor Authentication in Google Account
2. Generate an **App Password**: https://myaccount.google.com/apppasswords
3. Use the 16-character app password in the code
4. **Never commit credentials to version control**

### Environment Variables (Recommended)
Instead of hardcoding credentials, use environment variables:
```python
import os
EMAIL_SENDER = os.getenv("ALERT_EMAIL")
EMAIL_PASSWORD = os.getenv("ALERT_PASSWORD")
```

## 📊 How It Works

### Detection Flow
```
Laser Beam Intact → LDR Reads Light → Arduino Monitors
                         ↓
                    No Action
                    
Intruder Blocks Laser → LDR Reads Darkness → Arduino Detects HIGH
                         ↓
                    Buzzer & LED Activate (Instant)
                         ↓
                    Serial: "INTRUDER DETECTED"
                         ↓
                    Python Receives Signal
                         ↓
                    Log Event to CSV
                    Send Email Alert
```

### Arduino Logic
- **LDR Pin State**: HIGH = darkness (laser blocked), LOW = light present
- **Detection Sensitivity**: 100ms response time with delay stabilization
- **Alert Duration**: Continues until laser is restored

### Python Logic
- Continuously reads Arduino serial output
- Parses "INTRUDER DETECTED" message
- Triggers CSV logging with timestamp
- Sends formatted HTML email with instructions
- Graceful error handling for serial/network failures

## 📝 Output Files

### intrusion_log.csv
Automatically created and updated with intrusion events:
```
Timestamp,Event
2026-06-05 14:23:45,Intruder Detected
2026-06-05 14:25:12,Intruder Detected
```

## 🚀 Usage Examples

### Basic Monitoring
```bash
python intruder_alert.py
```

### Logging with Timestamp Monitoring
```bash
python intruder_alert.py  # Check intrusion_log.csv for history
```

### Testing Email Alerts
1. Temporarily block the laser manually
2. Verify Arduino detects interruption (buzzer/LED activate)
3. Confirm email alert is received within seconds

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| **"Serial port not found"** | Check COM port in Device Manager, update code with correct port |
| **"Arduino data not received"** | Verify USB cable, check Arduino upload, confirm baud rate (9600) |
| **"Email not sending"** | Verify Gmail credentials, enable "Less secure apps" or use App Password |
| **"LDR not detecting"** | Check wiring, test with multimeter, ensure laser is aligned to LDR |
| **"False positives"** | Adjust delay timing in Arduino (line 34), check sensor placement |

## 🔄 System Expansion Ideas

- 🌐 **Remote Dashboard**: Web interface to monitor system status
- 📱 **Mobile Notifications**: Push notifications via mobile app
- 🎥 **Camera Integration**: Capture images on intrusion detection
- 🗺️ **Multi-Zone**: Multiple sensors with zone mapping
- 💾 **Cloud Storage**: Store logs in cloud database
- 📊 **Analytics**: Heatmaps of intrusion patterns

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This is an educational and experimental security system. For production security:
- Consult professional security integrators
- Ensure compliance with local security regulations
- Implement redundant systems
- Test thoroughly in your environment
- Do not rely solely on this system for critical security

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Multi-sensor support
- Web dashboard
- Configuration file support
- Unit testing
- Docker containerization

## 📞 Support

For issues or questions:
1. Check the Troubleshooting section
2. Verify hardware connections
3. Review Arduino and Python logs
4. Test components individually

## 🙏 Acknowledgments

Built with Arduino and Python. Special thanks to the open-source community for serial and email libraries.

---

**Last Updated**: June 2026  
**Status**: Active Development  
**Stability**: Experimental
