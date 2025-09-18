import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from __init__ import OWMWeatherSkill

class TestTimeSkill(OWMWeatherSkill):
    def __init__(self):
        super().__init__()
        self.gui = self
    def show_text(self, text):
        print(text)
    def speak(self, utterance, expect_response=False):
        print(utterance)

skill = TestTimeSkill()
skill.initialize()

class Message:
    def __init__(self):
        self.data = {}

message = Message()
skill.handle_time_intent(message)
