import os
import sys

# Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from __init__ import OWMWeatherSkill


class TestWeatherSkill(OWMWeatherSkill):
    def __init__(self):
        super().__init__()
        self.gui = self  # gui.show_text yerine print kullanacağız

    def show_text(self, text):
        print(text)

    def speak(self, utterance, expect_response=False):
        print(utterance)

skill = TestWeatherSkill()
skill.initialize()

# Test mesajı için şehir adı
if len(sys.argv) > 1:
    city = sys.argv[1]
else:
    city = input("Enter city name: ")

class Message:
    def __init__(self, city):
        self.data = {"city": city}

message = Message(city)
skill.handle_weather_intent(message)
