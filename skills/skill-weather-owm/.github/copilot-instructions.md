# Copilot Instructions for skill-weather-owm

## Proje Mimari Özeti
- Bu proje, OpenWeatherMap API'sinden hava durumu bilgisini alan bir OVOS (Open Voice OS) Skill'dir.
- Ana bileşen: `OWMWeatherSkill` sınıfı (`__init__.py`), OVOSSkill'den türetilir ve API çağrısı ile hava durumu verisi döndürür.
- Intent dosyaları `locale/en-us/weather.intent` altında bulunur ve doğal dil sorgularını tanımlar.
- Skill, OVOS platformunda `ovos.plugin.skill` entry point'i ile yüklenir (`setup.py`).

## Geliştirici İş Akışları
- **Test:** `test_weather.py` dosyası, skill'in temel fonksiyonlarını terminalde test etmek için kullanılır. OVOS GUI ve `speak` fonksiyonları terminal çıktısına override edilmiştir.
- **Kurulum:**
  - Gerekli paketler: `requests` (API çağrısı için). Tüm bağımlılıklar `requirements.txt` ve `setup.py`'da listelenmiştir.
  - Skill'i yüklemek için: `pip install .` veya `python setup.py install`
- **Intent Tanımı:** Yeni intent eklemek için ilgili intent dosyasına (`locale/en-us/`) satır ekleyin ve handler fonksiyonunu `@intent_handler` ile tanımlayın.

## Proje Özgü Desenler ve Konvansiyonlar
- API anahtarı doğrudan `OWMWeatherSkill` içinde sabit olarak tanımlanmıştır (güvenlik için .env veya config dosyasına taşınabilir).
- Hata yönetimi: API'den dönen kod kontrol edilir, hata durumunda kullanıcıya açıklama döner.
- Yanıtlar İngilizce ve metin olarak döner, sesli çıktı override edilebilir.
- Skill, OVOS ekosistemine uygun olarak `ovos_workshop` paketini kullanır.

## Entegre Noktalar ve Bağımlılıklar
- **OpenWeatherMap API:** Dış hava durumu verisi için kullanılır.
- **OVOS Workshop:** Skill tabanı ve intent yönetimi için ana framework.
- **requests:** HTTP istekleri için ana bağımlılık.

## Önemli Dosyalar
- `__init__.py`: Ana skill ve intent handler'lar
- `test_weather.py`: Terminal tabanlı testler
- `setup.py`: Paketleme ve entry point
- `requirements.txt`: Bağımlılıklar
- `locale/en-us/weather.intent`: Intent tanımları

## Örnekler
- Yeni bir şehir için hava durumu almak: `skill.handle_weather_intent(Message("Istanbul"))`
- Yeni intent eklemek: `@intent_handler("Weather.intent")` ile fonksiyon tanımla, intent dosyasına satır ekle.

---
Bu doküman, AI kodlama ajanlarının projede hızlıca üretken olmasını sağlamak için hazırlanmıştır. Eksik veya belirsiz noktalar için lütfen geri bildirim verin.
