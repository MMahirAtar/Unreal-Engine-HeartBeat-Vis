#include <PulseSensorPlayground.h>

// Pulse Sensor ayarları
PulseSensorPlayground pulseSensor;
#define PULSE_PIN 36  // Pulse Sensor'un bağlı olduğu analog pin

// Değişkenler
int threshold = 550;  // Başlangıç eşik değeri
int BPM = 0;          // Beats per Minute
bool isBeat = false;

void setup() {
  Serial.begin(115200);
  delay(1000);

  // Pulse Sensor ayarları
  pulseSensor.analogInput(PULSE_PIN);
  pulseSensor.setThreshold(threshold);
  if (!pulseSensor.begin()) {
    Serial.println("Pulse Sensor başlatılamadı! Bağlantıları kontrol edin.");
    while (true) {
      delay(1000);
    }
  }
  Serial.println("Pulse Sensor başarıyla başlatıldı.");
}

void loop() {
  // Pulse Sensor'den okuma yap
  isBeat = pulseSensor.sawStartOfBeat();
  pulseSensor.getLatestSample();  // Bu satır, sensör verisinin güncel kalmasını sağlar.
  
  if (isBeat) {
    BPM = pulseSensor.getBeatsPerMinute();
    // BPM değerini seri porta yazdır
    //Serial.print("BPM: ");
    Serial.println(BPM);
  }
  delay(5);
}
