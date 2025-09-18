import requests
from ovos_workshop.skills import OVOSSkill
from ovos_workshop.decorators import intent_handler
from datetime import datetime  # <<< bunu ekle

class OWMWeatherSkill(OVOSSkill):
    def __init__(self):
        super().__init__(name="OWMWeatherSkill")
        self.api_key = "b66ffc385d7c20dfd73045bf3a5cec83"   # API 
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        """API'den hava durumu alır ve metin olarak döner"""
        url = f"{self.base_url}?q={city}&appid={self.api_key}&units=metric"
        try:
            response = requests.get(url, timeout=5)
            data = response.json()

            # Hata kontrolü
            if data.get("cod") != 200:
                return f"Sorry, I could not find weather data for {city}."

            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"].capitalize()
            feels_like = data["main"]["feels_like"]

            return (
                f"The current weather in {city} is {desc}, "
                f"with a temperature of {temp}°C, feels like {feels_like}°C."
            )
        except Exception as e:
            return f"Error fetching weather data: {e}"

    @intent_handler("Weather.intent")
    def handle_weather_intent(self, message):
        city = message.data.get("city") or "London"
        result = self.get_weather(city)

        # Sesli çıktı yok, sadece text/log
        if hasattr(self, "gui") and self.gui:
            self.gui.show_text(result)
        self.log.info(result)

    # <<< Saat intent fonksiyonu eklendi
    @intent_handler("Time.intent")
    def handle_time_intent(self, message):
        now = datetime.now()
        result = f"The current time is {now.strftime('%H:%M:%S')}."
        if hasattr(self, "gui") and self.gui:
            self.gui.show_text(result)
        self.log.info(result)
