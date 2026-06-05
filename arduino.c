#define LDR_PIN 6     // LDR Digital Output connected to pin 6
#define BUZZER_PIN 11
#define LED_PIN 9

bool alarmActive = false;

void setup() {
  pinMode(LDR_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);  // 🔗 Required for Python connection
}

void loop() {
  int ldrState = digitalRead(LDR_PIN);  // 1 = light blocked, 0 = light present

  if (ldrState == HIGH && !alarmActive) {
    // Light is blocked (Intruder)
    Serial.println("INTRUDER DETECTED");  // 🚨 Python will catch this!
    alarmActive = true;

    digitalWrite(BUZZER_PIN, HIGH);
    digitalWrite(LED_PIN, HIGH);
  }
  else if (ldrState == LOW && alarmActive) {
    // Light restored (no intrusion)
    Serial.println("Laser Detected - System Monitoring");
    alarmActive = false;

    digitalWrite(BUZZER_PIN, LOW);
    digitalWrite(LED_PIN, LOW);
  }

  delay(100); // stability
}
