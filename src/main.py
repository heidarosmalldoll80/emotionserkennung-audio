import sys
import sounddevice as sd
import numpy as np
import tensorflow as tf
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

class EmotionRecognitionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.model = self.load_model()

    def initUI(self):
        self.setWindowTitle('Emotionserkennung in Audio')
        self.layout = QVBoxLayout()
        self.label = QLabel('Drücke auf die Schaltfläche, um eine Audioaufnahme zu machen')
        self.record_button = QPushButton('Aufnehmen')
        self.record_button.clicked.connect(self.record_audio)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.record_button)
        self.setLayout(self.layout)

    def load_model(self):
        return tf.keras.models.load_model('emotion_model.h5')

    def record_audio(self):
        self.label.setText('Aufnahme läuft...')
        duration = 5  # in Sekunden
        fs = 44100  # Sample rate
        audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()
        audio_data = audio_data.flatten()
        emotion = self.predict_emotion(audio_data)
        self.label.setText(f'Erkannte Emotion: {emotion}')

    def predict_emotion(self, audio_data):
        # Hier sollte die Vorverarbeitung und Vorhersage implementiert werden
        # Beispiel: return 'Freude'
        return 'Emotion Placeholder'  # Ersetze dies durch die eigentliche Vorhersage

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EmotionRecognitionApp()
    ex.show()
    sys.exit(app.exec_())