# OVOS Custom Project

**OVOS Custom Project**, OpenVoiceOS (OVOS) tabanlı bir **hava durumu ve saat bilgisi skill'i** içerir. Proje, Docker ve Docker Compose kullanılarak çalışacak şekilde yapılandırılmıştır.

## 📂 Proje Yapısı

```
ovos-custom-project/
│
├─ skills/skill-weather-owm/    # Skill kodları
├─ config/                     # Dil, API key ve diğer ayarlar
├─ docker-compose.yml          # Container'ları başlatmak için
├─ run_weather.sh              # Hava durumu scripti
└─ run_time.sh                 # Saat scripti
```

## ⚙️ Gereksinimler

- Docker
- Docker Compose
- Git

> Linux, macOS ve Windows (WSL2) ile uyumludur.

## 🚀 Kurulum ve Çalıştırma

### 1️⃣ Repo'yu Klonla

```bash
git clone https://github.com/yasindabak/ovos-custom-project.git
cd ovos-custom-project
```

### 2️⃣ Container'ları Başlat

```bash
docker compose up -d
```

## 🌤 Hava Durumu Skill'i

### Hızlı çalıştırma:

```bash
./run_weather.sh Istanbul
```

İstediğiniz şehri belirterek çalıştırabilirsiniz:

```bash
./run_weather.sh Paris
```

### Manuel test:

```bash
docker exec -it ovos_cli bash
source ~/.venv/bin/activate
cd /home/ovos/skills/skill-weather-owm
python3 test_weather.py Istanbul
```

## ⏰ Saat Skill'i

### Hızlı çalıştırma:

```bash
./run_time.sh
```

### Manuel test:

```bash
docker exec -it ovos_cli bash
source ~/.venv/bin/activate
cd /home/ovos/skills/skill-weather-owm
python3 test_time.py
```

## 🔧 Ayarlar

- **Dil:** `config/mycroft.conf` dosyasında `"lang": "en-us"`
- **API Key:** `config/mycroft.conf` veya ilgili skill dosyasında ayarlanmıştır

## 📌 Notlar

- Hava durumu için OpenWeatherMap API kullanılmaktadır
- Skill İngilizce olarak yanıt verir
- Docker konteyneri üzerinden test etmek, bağımlılıkları ve OVOS ortamını doğru şekilde kullanmanızı sağlar
