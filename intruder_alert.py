import serial #to include python
import smtplib #to send email
import csv #to save data of intrusion detection 
from datetime import datetime #to help give real time alerts
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

# 🚀 Set up Serial Communication with Arduino
try:
    ser = serial.Serial('COM7', 9600, timeout=1)  # port num
    print("🔄 Waiting for Arduino data...")
    time.sleep(2)  # Give time for Arduino to reset
except serial.SerialException as e:
    print(f"❌ Error: {e}")
    exit()

# 📧 Email Configuration
SMTP_SERVER = "smtp.gmail.com" 
SMTP_PORT = 587
EMAIL_SENDER = "sender_email"
EMAIL_PASSWORD = "your_paasword"
EMAIL_RECEIVER = "receiver_email"

# 📂 Function to Log Intrusion Events
def log_intrusion():
    with open("intrusion_log.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Intruder Detected"])
    print("📂 Intrusion logged successfully.")

# ✉️ Function to Send an Email Alert
def send_email():
    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg["Subject"] = "🚨 **INTRUDER ALERT - IMMEDIATE ACTION REQUIRED** 🚨"

    # 📌 Email Body with Steps & Safety Precautions
    body = f"""
    <html>
    <body>
        <h2 style='color: red;'>⚠️ SECURITY ALERT! An intruder has been detected. ⚠️</h2>
        <p><b>🕒 Time of Detection:</b> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        <p><b>📍 Location:</b> Your Secured Area</p>

        <h3>🚀 Next Steps to Follow:</h3>
        <ol>
            <li>🔍 <b>Check Surveillance Cameras</b> to verify the intrusion.</li>
            <li>📞 <b>Contact Security or Law Enforcement</b> if necessary.</li>
            <li>🚪 <b>Ensure all Entry Points are Secured</b> (Doors, Windows, Gates).</li>
            <li>🚨 <b>Activate Emergency Response Plan</b> if required.</li>
        </ol>

        <h3>🔒 Important Safety Precautions:</h3>
        <ul>
            <li>🔦 <b>Do not engage the intruder alone.</b> Call for help.</li>
            <li>📢 <b>Make your presence known</b> by turning on lights or alarms.</li>
            <li>📡 <b>Stay in a safe, locked room</b> until help arrives.</li>
        </ul>

        <p style='color: red;'><b>⏳ Take Action Immediately! Every second counts.</b></p>

        <hr>
        <p>This is an automated message from your <b>Laser Security System</b>. Stay Safe! 🛡️</p>
    </body>
    </html>
    """

    msg.attach(MIMEText(body, "html"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ ERROR: {e}")
        print("⚠️ Failed to send email. Check your credentials or connection.")

# 🔄 Main Loop - Reads Arduino Data & Responds
try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            print(f"📡 Received from Arduino: {line}")

            if "INTRUDER DETECTED" in line:
                print("🚨 Intruder detected! Logging and sending alert...")
                log_intrusion()
                send_email()
except serial.SerialException:
    print("❌ Serial port error! Closing connection...")
finally:
    ser.close()
    print("🔌 Serial connection closed.")
