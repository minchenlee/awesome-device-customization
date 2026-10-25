# Awesome Device Customization [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[繁體中文](README.zh-TW.md)

> Community projects that customize consumer devices, organized by device model.

You own a device. Which open-source projects let you do more with it? This list answers that question by model, across brands and device types: open firmware, local control, add-on apps, configuration files, and compatible accessories.

## Contents

- [IKEA smart home](#ikea-smart-home)
- [Cameras](#cameras)
- [E-readers](#e-readers)
- [Android TV and Google TV](#android-tv-and-google-tv)
- [Routers](#routers)
- [Inclusion rules](#inclusion-rules)
- [Risk markers](#risk-markers)
- [Disclaimer](#disclaimer)
- [Further reading](#further-reading)
- [Contributing](#contributing)
- [License](#license)

## IKEA smart home

### IKEA OBEGRÄNSAD LED wall lamp

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [ikea-led-obegraensad](https://github.com/ph1p/ikea-led-obegraensad) | Replaces the lamp's controller with an ESP32 for custom animations, a web UI, and clock and weather screens. | 883 | 2026-10-19 | MIT | 🔧 🛡️ |
| [IKEA-Obegransad-Tetris](https://github.com/grandpasquarepants/IKEA-Obegransad-Tetris) | Turns the modded 16x16 LED panel into a playable Tetris game. | 46 | 2026-03-08 | Not detected | 🔧 🛡️ |
| [Home Assistant Obegransad](https://github.com/PiotrMachowski/Home-Assistant-custom-components-Obegransad) | Controls an OBEGRÄNSAD running the ESP32 firmware from Home Assistant. | 23 | 2026-03-05 | MIT |  |

### IKEA FREKVENS LED cube

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [Frekvens](https://github.com/VIPnytt/Frekvens) | ESP32 firmware for FREKVENS and OBEGRÄNSAD panels with effects, MQTT, and Home Assistant support. | 39 | 2026-10-24 | MIT | ⚡ 🔧 🛡️ |

### IKEA VINDRIKTNING air quality sensor

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [ESPHome-IKEA-VINDRIKTNING](https://github.com/DzurisHome/ESPHome-IKEA-VINDRIKTNING) | Adds an ESP module inside the sensor so PM2.5 readings reach Home Assistant through ESPHome. | 96 | 2026-05-12 | MIT | 🔧 🛡️ |
| [ESP-Vindriktning](https://github.com/LaskaKit/ESP-Vindriktning) | A drop-in ESP32 board that adds Wi-Fi, Bluetooth, and RGB LEDs, with optional CO2, temperature, and humidity modules. | 93 | 2025-10-07 | Not detected | 🔧 🛡️ |
| [VINDRIKTNING Zigbee](https://github.com/smartboxchannel/IKEA-VINDRIKTNING_ZIGBEE_I_II_III) | Zigbee boards that make the sensor report to a Zigbee hub instead of Wi-Fi. | 73 | 2025-03-29 | Not detected | 🔧 🛡️ |

### IKEA UPPÅTVIND air purifier

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [esphome-ikea-uppatvind](https://github.com/jonathonlui/esphome-ikea-uppatvind) | Wires an ESP8266 or ESP32 into the purifier so ESPHome can set fan speed and read its state. | 166 | 2024-01-14 | Not detected | 🔧 🛡️ |
| [esp8266-for-uppatvind](https://github.com/horvathgergo/esp8266-for-uppatvind) | A small replacement board that adds Wi-Fi control and an air quality sensor to the purifier. | 60 | 2026-02-20 | GPL-3.0 | 🔧 🛡️ |

### IKEA FYRTUR / KADRILJ blinds

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [fyrtur-esp](https://github.com/mjuhanne/fyrtur-esp) | Replaces the blind motor's Zigbee module with an ESP32 for MQTT and Home Assistant control. | 85 | 2024-08-01 | MIT | 🔧 🛡️ |

### IKEA IDÅSEN standing desk

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [idasen-control](https://github.com/mitsuhiko/idasen-control) | Command-line tool that moves the desk to saved heights over Bluetooth. | 440 | 2026-02-19 | MIT |  |
| [idasen](https://github.com/newAM/idasen) | Python library and CLI for reading and setting desk height over Bluetooth. | 157 | 2026-10-23 | MIT |  |
| [trayasen](https://github.com/golota60/trayasen) | Desktop tray app for switching between saved desk positions. | 30 | 2026-08-01 | MIT |  |

### IKEA TRÅDFRI gateway, bulbs, and remotes

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [pytradfri](https://github.com/home-assistant-libs/pytradfri) | Python library for local control of lights and blinds through the TRÅDFRI gateway. | 960 | 2026-10-23 | MIT |  |
| [node-tradfri-client](https://github.com/AlCalzone/node-tradfri-client) | Node.js library for local control of devices paired to the TRÅDFRI gateway. | 267 | 2024-08-29 | MIT |  |
| [TRADFRI-Hacking](https://github.com/basilfx/TRADFRI-Hacking) | Research notes and tools for flashing your own firmware onto TRÅDFRI hardware. | 741 | 2024-11-28 | CC-BY-4.0 | 🔧 🛡️ |

### IKEA DIRIGERA hub

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [dirigera](https://github.com/Leggin/dirigera) | Python library for local control of lights, outlets, blinds, and sensors on the hub. | 221 | 2026-10-23 | MIT |  |
| [dirigera_platform](https://github.com/sanjoyg/dirigera_platform) | Home Assistant integration that talks to the hub on the local network. | 226 | 2026-02-18 | MIT |  |
| [dirigera (TypeScript)](https://github.com/lpgera/dirigera) | TypeScript client for the hub's local API. | 94 | 2026-09-13 | MIT |  |
| [DirigeraClient](https://github.com/dvdgeisler/DirigeraClient) | Java client and MQTT bridge for the hub's local API. | 94 | 2023-12-27 | MIT |  |

### IKEA SYMFONISK speakers

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [opensymf](https://github.com/papadopouloskyriakos/opensymf) | Guide and scripts for rebuilding the speakers around a Raspberry Pi audio player. | 34 | 2026-02-18 | MIT | ⚡ 🔧 🛡️ |

## Cameras

### Canon EOS cameras (and some PowerShot)

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [Magic Lantern](https://github.com/reticulatedpines/magiclantern_simplified) | Add-on software that runs from the memory card and adds tools such as zebras, focus peaking, and intervalometers. | 559 | 2026-10-04 | GPL-2.0 | 🛡️ |

### Sony Alpha and Cyber-shot (PlayMemories app era)

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [Sony-PMCA-RE](https://github.com/ma1co/Sony-PMCA-RE) | Installs your own Android apps on cameras that supported PlayMemories Camera Apps. | 2,975 | 2024-07-27 | MIT | 🛡️ |
| [OpenMemories-Tweak](https://github.com/ma1co/OpenMemories-Tweak) | Camera app that changes hidden settings such as the video recording time limit and the language list. | 1,426 | 2024-01-21 | MIT | 🛡️ ⚠️ |
| [sony-pmca-ricoh-mod](https://github.com/bonyback1/sony-pmca-ricoh-mod) | Adds RICOH GR style color profiles to the Picture Effect app on supported Sony cameras. | 47 | 2026-10-17 | Apache-2.0 | 🛡️ |

### Fujifilm X and GFX

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [fudge](https://github.com/petabyt/fudge) | Open-source app that connects to Fujifilm cameras over Wi-Fi and USB to import photos and change settings. | 31 | 2026-10-23 | Not detected |  |
| [Filmcase](https://github.com/gosku/Filmcase) | Self-hosted app for saving film simulation recipes and browsing the JPEGs made with each one. | 74 | 2026-10-11 | Not detected |  |

### RICOH GR II, GR III, and GR IV

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [GRsync](https://github.com/clyang/GRsync) | Downloads photos from the camera over Wi-Fi without the official app. | 104 | 2026-02-11 | MIT |  |
| [ricoh-gr-bluetooth-api](https://github.com/dm-zharov/ricoh-gr-bluetooth-api) | Documents the camera's Bluetooth protocol so you can build your own remote. | 63 | 2024-11-14 | Unlicense |  |
| [grkit](https://github.com/ahonn/grkit) | Toolkit for browsing and downloading photos from the camera over Wi-Fi. | 89 | 2026-10-25 | MIT |  |
| [gr3-film-mods](https://github.com/idontknownihil/gr3-film-mods) | Firmware patches that add custom film looks to the GR III. | 35 | 2026-10-12 | MIT | 🛡️ |

### GoPro HERO and MAX

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [OpenGoPro](https://github.com/gopro/OpenGoPro) | GoPro's official open API and examples for controlling cameras over Bluetooth, Wi-Fi, and USB. | 992 | 2026-06-08 | Not detected |  |
| [GoPro Labs](https://github.com/gopro/labs) | GoPro's experimental firmware that adds QR-code commands and extra capture modes. | 733 | 2026-10-14 | Apache-2.0 |  |
| [gopro_as_webcam_on_linux](https://github.com/jschmid1/gopro_as_webcam_on_linux) | Uses a GoPro as a webcam on Linux. | 707 | 2026-03-04 | Apache-2.0 |  |

### Most USB cameras (PTP tethering)

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [libgphoto2](https://github.com/gphoto/libgphoto2) | Library that controls thousands of camera models over USB for tethered shooting and file transfer. | 1,396 | 2026-10-24 | LGPL-2.1 |  |
| [gphoto2](https://github.com/gphoto/gphoto2) | Command-line tool for tethered capture, live view, and downloads from supported cameras. | 906 | 2026-06-22 | GPL-2.0 |  |
| [python-gphoto2](https://github.com/jim-easterbrook/python-gphoto2) | Python bindings for scripting libgphoto2 camera control. | 429 | 2026-09-05 | LGPL-3.0 |  |

## E-readers

### Kindle, Kobo, PocketBook, and other e-readers (KOReader)

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [KOReader](https://github.com/koreader/koreader) | Alternative reading app with strong PDF and EPUB support, plugins, and sync. | 30,590 | 2026-10-25 | AGPL-3.0 |  |
| [koreader-sync-server](https://github.com/koreader/koreader-sync-server) | Self-hosted server that syncs reading progress between KOReader devices. | 794 | 2026-09-23 | AGPL-3.0 |  |
| [Project: Title](https://github.com/joshuacant/ProjectTitle) | KOReader plugin that replaces the file browser with a cover-based library view. | 1,138 | 2026-08-31 | AGPL-3.0 |  |

### Kobo e-readers

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [Plato](https://github.com/baskerville/plato) | Alternative document reader built for Kobo devices. | 1,725 | 2026-03-30 | Not detected |  |
| [NickelMenu](https://github.com/pgaskin/NickelMenu) | Adds custom menu items to the stock Kobo software to launch scripts and change settings. | 1,226 | 2026-06-12 | MIT |  |
| [kobopatch](https://github.com/pgaskin/kobopatch) | Applies community patches to the stock Kobo firmware to change its behavior. | 134 | 2026-03-17 | MIT | 🛡️ |
| [kepubify](https://github.com/pgaskin/kepubify) | Converts EPUB files to Kobo's KEPUB format for better reading features. | 898 | 2025-12-06 | MIT |  |
| [KoboCloud](https://github.com/fsantini/KoboCloud) | Syncs books from Dropbox, Google Drive, and other cloud folders to the device. | 1,313 | 2026-09-24 | Not detected |  |
| [Quill OS](https://github.com/Quill-OS/quill) | Alternative operating system for Kobo e-readers, installed on the internal SD card; no longer actively maintained. | 799 | 2026-08-14 | Not detected | 🔧 🛡️ |

### Kindle e-readers

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [KindleEar](https://github.com/cdhigh/KindleEar) | Self-hosted service that sends RSS and news digests to your Kindle. | 2,880 | 2026-10-24 | MIT |  |
| [FBInk](https://github.com/NiLuJe/FBInk) | Library and tool for drawing text and images directly on Kindle and Kobo screens. | 554 | 2026-08-06 | GPL-3.0 |  |
| [kindle-dash](https://github.com/pascalw/kindle-dash) | Turns an already unlocked Kindle into a low-power dashboard screen (tested on Kindle 4 NT). | 1,390 | 2024-03-04 | MIT | 🛡️ |
| [LanguageBreak](https://github.com/notmarek/LanguageBreak) | Unlocks your own Kindle (firmware 5.16.2.1.1 or lower) so you can install KOReader and other apps; it deletes all content. Project page only. | 1,215 | 2025-01-30 | Not detected | 🛡️ ⚠️ |

### reMarkable tablets

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [reStream](https://github.com/rien/reStream) | Streams the tablet screen to a computer for presentations. | 872 | 2026-06-10 | MIT |  |
| [rmview](https://github.com/bordaigorl/rmview) | Desktop viewer for live screen sharing from the tablet. | 826 | 2025-10-08 | GPL-3.0 |  |

### PocketBook e-readers

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [Pocketbook-Nextcloud-Client](https://github.com/JuanJakobo/Pocketbook-Nextcloud-Client) | Native app that downloads books from your Nextcloud. | 157 | 2025-08-25 | GPL-3.0 |  |
| [PocketPuzzles](https://github.com/SteffenBauer/PocketPuzzles) | Port of Simon Tatham's puzzle collection for PocketBook screens. | 104 | 2026-05-23 | Not detected |  |
| [Syncthing-for-PocketBook](https://github.com/mikedigriz/Syncthing-for-PocketBook) | Runs Syncthing on the device to sync book folders. | 58 | 2026-10-01 | Apache-2.0 |  |

## Android TV and Google TV

### Android TV and Google TV devices

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [AerialViews](https://github.com/theothernt/AerialViews) | Screensaver with Apple TV style aerial videos and your own media. | 1,119 | 2026-10-23 | Not detected |  |
| [Jellyfin for Android TV](https://github.com/jellyfin/jellyfin-androidtv) | TV client for your own Jellyfin media server. | 4,653 | 2026-10-24 | GPL-2.0 |  |
| [LtvLauncher](https://github.com/leanbitlab-org/LtvLauncher) | Open-source home screen launcher without ads. | 416 | 2026-10-25 | GPL-3.0 |  |
| [python-androidtv](https://github.com/JeffLIrion/python-androidtv) | Python library for controlling Android TV and Fire TV devices over ADB. | 196 | 2024-11-10 | MIT |  |

### Chromecast with Google TV

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [adb-auto-enable](https://github.com/mouldybread/adb-auto-enable) | Turns on wireless ADB at boot so home automation can reach the device; this opens full device access on your network. | 301 | 2026-10-18 | MIT |  |

### Amazon Fire TV

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [HA-Firemote](https://github.com/PRProd/HA-Firemote) | Home Assistant remote card for Fire TV, Chromecast, NVIDIA Shield, and other streamers. | 1,091 | 2026-03-08 | GPL-3.0 |  |

### NVIDIA Shield TV

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [shield-commander](https://github.com/siewers/shield-commander) | Desktop app for controlling a Shield TV over the local network. | 46 | 2026-10-24 | MIT |  |

## Routers

### Routers supported by OpenWrt

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [OpenWrt](https://github.com/openwrt/openwrt) | Open-source Linux firmware that replaces the stock router software. | 28,923 | 2026-10-25 | Not detected | 🛡️ |

### ASUS routers

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [Asuswrt-Merlin](https://github.com/RMerl/asuswrt-merlin.ng) | Third-party firmware based on the stock ASUS firmware with extra features and fixes. | 6,254 | 2026-10-25 | Not detected | 🛡️ |
| [Asuswrt-Merlin (gnuton)](https://github.com/gnuton/asuswrt-merlin.ng) | Ports Asuswrt-Merlin to ASUS models that the main project does not support. | 2,379 | 2026-09-17 | Not detected | 🛡️ |
| [amtm](https://github.com/decoderman/amtm) | Terminal menu for installing and managing Asuswrt-Merlin add-ons. | 237 | 2026-10-11 | GPL-3.0 |  |
| [IPSet_ASUS](https://github.com/Adamm00/IPSet_ASUS) | Firewall add-on that blocks known malicious IP addresses. | 439 | 2026-10-22 | Not detected |  |

### GL.iNet routers

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [glinet-tailscale-updater](https://github.com/admonstrator/glinet-tailscale-updater) | Updates the bundled Tailscale to a newer release. | 786 | 2026-10-21 | MIT |  |
| [ha-glinet4-integration](https://github.com/HarvsG/ha-glinet4-integration) | Home Assistant integration for routers on GL.iNet firmware 4. | 100 | 2026-10-24 | Apache-2.0 |  |
| [MT6000_cust_build](https://github.com/pesa1234/MT6000_cust_build) | Custom OpenWrt builds tuned for the GL-MT6000 (Flint 2). | 204 | 2026-08-29 | Not detected | 🛡️ |

### Broadcom-based routers (Netgear, Linksys, ASUS)

| Project | What it does | ★ | Last push | License | Markers |
|---|---|---:|---|---|---|
| [FreshTomato](https://github.com/FreshTomato-Project/freshtomato-arm) | Tomato-based open-source firmware for ARM Broadcom routers. | 197 | 2026-10-22 | GPL-3.0 | 🛡️ |

## Inclusion rules

Included: legal customization of a device you own. Examples are open-source firmware, local control without the vendor cloud, add-on apps, configuration and recipe files, and compatible accessories.

Not included: DRM removal, license key or paywall bypass, piracy, game ROMs, account sharing, and carrier unlock bypass. Projects that unlock your own device (for example an e-reader) are linked to their project page only, with the ⚠️ marker. This list gives no unlock steps and hosts no code, firmware, or files. If GitHub disables a linked repository, for example after a DMCA notice, the entry is removed. Project owners can ask for removal in an issue.

Projects with no push for more than 3 years are left out or marked 📦. Stars, last push dates, and licenses come from the GitHub API (`scripts/refresh.py`); the last refresh was on 2026-10-25.

## Risk markers

Each project shows the markers that apply to it.

| | |
|---|---|
| ⚡ | Mains voltage inside the device |
| 🔧 | Requires opening the device or soldering |
| 🛡️ | Likely voids the warranty |
| 📦 | Archived or not pushed for over 3 years |
| ⚠️ | Unlocks the device; read the project page and local law first |

## Disclaimer

You are responsible for your own device. Modifications can damage hardware, void the warranty, or break vendor terms. In some countries, anti-circumvention law can also restrict unlocking a device. Work on mains-powered devices (⚡) can kill you: unplug the device and let a qualified person do the work if you are not sure. Obey local law and your warranty terms. The projects belong to their authors; this list does not check their code.

## Further reading

- [awesome-home-assistant](https://github.com/frenck/awesome-home-assistant) - Home Assistant integrations and resources.
- [Awesome-Kindle](https://github.com/KindleTweaks/Awesome-Kindle) - Kindle tweaks and tools.
- [awesome-smart-tv](https://github.com/vitalets/awesome-smart-tv) - Smart TV app development.
- [Awesome-Android-TV-FOSS-Apps](https://github.com/Generator/Awesome-Android-TV-FOSS-Apps) - Free and open-source Android TV apps.
- [awesome-eink](https://github.com/asapelkin/awesome-eink) - E-ink devices and software.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before you open a pull request.

## License

[CC0-1.0](LICENSE). To the extent possible under law, the contributors waived all copyright to this list.
