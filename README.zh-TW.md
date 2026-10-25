# Awesome Device Customization（裝置客製化清單）[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[English](README.md)

> 按裝置型號整理的社群客製化專案。

你有一台裝置。社群做了哪些開源專案，讓它做更多事？這份清單按型號回答，跨品牌、跨類別：開源韌體、本機控制、外掛 app、設定檔與相容配件。

## 目錄

- [IKEA 智慧家居](#ikea-智慧家居)
- [相機](#相機)
- [電子書閱讀器](#電子書閱讀器)
- [Android TV 與 Google TV](#android-tv-與-google-tv)
- [路由器](#路由器)
- [收錄規則](#收錄規則)
- [風險標記](#風險標記)
- [免責聲明](#免責聲明)
- [延伸閱讀](#延伸閱讀)
- [貢獻方式](#貢獻方式)
- [授權](#授權)

## IKEA 智慧家居

### IKEA OBEGRÄNSAD LED wall lamp

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [ikea-led-obegraensad](https://github.com/ph1p/ikea-led-obegraensad) | 把燈的控制器換成 ESP32，可自訂動畫、網頁介面，以及時鐘與天氣畫面。 | 883 | 2026-10-19 | MIT | 🔧 🛡️ |
| [IKEA-Obegransad-Tetris](https://github.com/grandpasquarepants/IKEA-Obegransad-Tetris) | 把改裝過的 16x16 LED 面板變成可玩的俄羅斯方塊遊戲。 | 46 | 2026-03-08 | 未偵測到 | 🔧 🛡️ |
| [Home Assistant Obegransad](https://github.com/PiotrMachowski/Home-Assistant-custom-components-Obegransad) | 從 Home Assistant 控制執行 ESP32 韌體的 OBEGRÄNSAD。 | 23 | 2026-03-05 | MIT |  |

### IKEA FREKVENS LED cube

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [Frekvens](https://github.com/VIPnytt/Frekvens) | 給 FREKVENS 與 OBEGRÄNSAD 面板用的 ESP32 韌體，支援燈效、MQTT 與 Home Assistant。 | 39 | 2026-10-24 | MIT | ⚡ 🔧 🛡️ |

### IKEA VINDRIKTNING air quality sensor

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [ESPHome-IKEA-VINDRIKTNING](https://github.com/DzurisHome/ESPHome-IKEA-VINDRIKTNING) | 在感測器內加裝 ESP 模組，讓 PM2.5 讀值透過 ESPHome 送到 Home Assistant。 | 96 | 2026-05-12 | MIT | 🔧 🛡️ |
| [ESP-Vindriktning](https://github.com/LaskaKit/ESP-Vindriktning) | 可直接替換的 ESP32 板子，加上 Wi-Fi、藍牙與 RGB LED，並可選配 CO2、溫度與濕度模組。 | 93 | 2025-10-07 | 未偵測到 | 🔧 🛡️ |
| [VINDRIKTNING Zigbee](https://github.com/smartboxchannel/IKEA-VINDRIKTNING_ZIGBEE_I_II_III) | Zigbee 板子，讓感測器改為回報給 Zigbee 中樞，而不是走 Wi-Fi。 | 73 | 2025-03-29 | 未偵測到 | 🔧 🛡️ |

### IKEA UPPÅTVIND air purifier

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [esphome-ikea-uppatvind](https://github.com/jonathonlui/esphome-ikea-uppatvind) | 把 ESP8266 或 ESP32 接進清淨機，讓 ESPHome 能設定風速並讀取狀態。 | 166 | 2024-01-14 | 未偵測到 | 🔧 🛡️ |
| [esp8266-for-uppatvind](https://github.com/horvathgergo/esp8266-for-uppatvind) | 小型替換板，為清淨機加上 Wi-Fi 控制與空氣品質感測器。 | 60 | 2026-02-20 | GPL-3.0 | 🔧 🛡️ |

### IKEA FYRTUR / KADRILJ blinds

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [fyrtur-esp](https://github.com/mjuhanne/fyrtur-esp) | 把窗簾馬達的 Zigbee 模組換成 ESP32，以便用 MQTT 和 Home Assistant 控制。 | 85 | 2024-08-01 | MIT | 🔧 🛡️ |

### IKEA IDÅSEN standing desk

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [idasen-control](https://github.com/mitsuhiko/idasen-control) | 透過藍牙把書桌移動到已儲存高度的命令列工具。 | 440 | 2026-02-19 | MIT |  |
| [idasen](https://github.com/newAM/idasen) | 透過藍牙讀取與設定桌面高度的 Python 程式庫與 CLI。 | 157 | 2026-10-23 | MIT |  |
| [trayasen](https://github.com/golota60/trayasen) | 桌面常駐程式，用來切換已儲存的桌面位置。 | 30 | 2026-08-01 | MIT |  |

### IKEA TRÅDFRI gateway, bulbs, and remotes

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [pytradfri](https://github.com/home-assistant-libs/pytradfri) | 透過 TRÅDFRI 閘道器在本機控制燈具與窗簾的 Python 程式庫。 | 960 | 2026-10-23 | MIT |  |
| [node-tradfri-client](https://github.com/AlCalzone/node-tradfri-client) | 以 Node.js 程式庫在本機控制配對到 TRÅDFRI 閘道器的裝置。 | 267 | 2024-08-29 | MIT |  |
| [TRADFRI-Hacking](https://github.com/basilfx/TRADFRI-Hacking) | 在 TRÅDFRI 硬體上刷入自製韌體的研究筆記與工具。 | 741 | 2024-11-28 | CC-BY-4.0 | 🔧 🛡️ |

### IKEA DIRIGERA hub

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [dirigera](https://github.com/Leggin/dirigera) | 在本機控制中樞上燈具、插座、窗簾與感測器的 Python 程式庫。 | 221 | 2026-10-23 | MIT |  |
| [dirigera_platform](https://github.com/sanjoyg/dirigera_platform) | 在區域網路內與中樞通訊的 Home Assistant 整合。 | 226 | 2026-02-18 | MIT |  |
| [dirigera (TypeScript)](https://github.com/lpgera/dirigera) | 中樞本機 API 的 TypeScript 用戶端。 | 94 | 2026-09-13 | MIT |  |
| [DirigeraClient](https://github.com/dvdgeisler/DirigeraClient) | 中樞本機 API 的 Java 用戶端與 MQTT 橋接。 | 94 | 2023-12-27 | MIT |  |

### IKEA SYMFONISK speakers

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [opensymf](https://github.com/papadopouloskyriakos/opensymf) | 以 Raspberry Pi 播放器重建喇叭的指南與腳本。 | 34 | 2026-02-18 | MIT | ⚡ 🔧 🛡️ |

## 相機

### Canon EOS cameras (and some PowerShot)

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [Magic Lantern](https://github.com/reticulatedpines/magiclantern_simplified) | 從記憶卡執行的附加軟體，加入斑馬紋、對焦峰值與縮時攝影等工具。 | 559 | 2026-10-04 | GPL-2.0 | 🛡️ |

### Sony Alpha and Cyber-shot (PlayMemories app era)

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [Sony-PMCA-RE](https://github.com/ma1co/Sony-PMCA-RE) | 在支援 PlayMemories Camera Apps 的相機上安裝自己的 Android 應用程式。 | 2,975 | 2024-07-27 | MIT | 🛡️ |
| [OpenMemories-Tweak](https://github.com/ma1co/OpenMemories-Tweak) | 相機應用程式，可更改錄影時間上限、語言清單等隱藏設定。 | 1,426 | 2024-01-21 | MIT | 🛡️ ⚠️ |
| [sony-pmca-ricoh-mod](https://github.com/bonyback1/sony-pmca-ricoh-mod) | 在支援的 Sony 相機上，為 Picture Effect 應用程式加入 RICOH GR 風格色彩設定。 | 47 | 2026-10-17 | Apache-2.0 | 🛡️ |

### Fujifilm X and GFX

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [fudge](https://github.com/petabyt/fudge) | 開源應用程式，透過 Wi-Fi 與 USB 連線 Fujifilm 相機，匯入照片並更改設定。 | 31 | 2026-10-23 | 未偵測到 |  |
| [Filmcase](https://github.com/gosku/Filmcase) | 自架應用程式，用來保存底片模擬配方，並瀏覽各配方拍出的 JPEG。 | 74 | 2026-10-11 | 未偵測到 |  |

### RICOH GR II, GR III, and GR IV

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [GRsync](https://github.com/clyang/GRsync) | 不用官方 App，透過 Wi-Fi 從相機下載照片。 | 104 | 2026-02-11 | MIT |  |
| [ricoh-gr-bluetooth-api](https://github.com/dm-zharov/ricoh-gr-bluetooth-api) | 記錄相機的藍牙通訊協定，方便自行打造遙控器。 | 63 | 2024-11-14 | Unlicense |  |
| [grkit](https://github.com/ahonn/grkit) | 透過 Wi-Fi 瀏覽與下載相機照片的工具組。 | 89 | 2026-10-25 | MIT |  |
| [gr3-film-mods](https://github.com/idontknownihil/gr3-film-mods) | 韌體修補，為 GR III 加入自訂的底片風格。 | 35 | 2026-10-12 | MIT | 🛡️ |

### GoPro HERO and MAX

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [OpenGoPro](https://github.com/gopro/OpenGoPro) | GoPro 官方的開放 API 與範例，可透過藍牙、Wi-Fi 與 USB 控制相機。 | 992 | 2026-06-08 | 未偵測到 |  |
| [GoPro Labs](https://github.com/gopro/labs) | GoPro 的實驗性韌體，加入 QR 碼指令與額外拍攝模式。 | 733 | 2026-10-14 | Apache-2.0 |  |
| [gopro_as_webcam_on_linux](https://github.com/jschmid1/gopro_as_webcam_on_linux) | 在 Linux 上把 GoPro 當成網路攝影機使用。 | 707 | 2026-03-04 | Apache-2.0 |  |

### Most USB cameras (PTP tethering)

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [libgphoto2](https://github.com/gphoto/libgphoto2) | 透過 USB 控制數千種相機機型的程式庫，可連線拍攝與傳輸檔案。 | 1,396 | 2026-10-24 | LGPL-2.1 |  |
| [gphoto2](https://github.com/gphoto/gphoto2) | 對支援的相機進行連線拍攝、即時預覽與下載的命令列工具。 | 906 | 2026-06-22 | GPL-2.0 |  |
| [python-gphoto2](https://github.com/jim-easterbrook/python-gphoto2) | 用 Python 腳本控制 libgphoto2 的繫結。 | 429 | 2026-09-05 | LGPL-3.0 |  |

## 電子書閱讀器

### Kindle, Kobo, PocketBook, and other e-readers (KOReader)

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [KOReader](https://github.com/koreader/koreader) | 替代閱讀應用程式，PDF 與 EPUB 支援強，有外掛與同步功能。 | 30,590 | 2026-10-25 | AGPL-3.0 |  |
| [koreader-sync-server](https://github.com/koreader/koreader-sync-server) | 自架伺服器，在 KOReader 裝置之間同步閱讀進度。 | 794 | 2026-09-23 | AGPL-3.0 |  |
| [Project: Title](https://github.com/joshuacant/ProjectTitle) | KOReader 外掛，把檔案瀏覽器換成以封面為主的書庫檢視。 | 1,138 | 2026-08-31 | AGPL-3.0 |  |

### Kobo e-readers

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [Plato](https://github.com/baskerville/plato) | 為 Kobo 裝置打造的另一套文件閱讀器。 | 1,725 | 2026-03-30 | 未偵測到 |  |
| [NickelMenu](https://github.com/pgaskin/NickelMenu) | 在 Kobo 原廠軟體加入自訂選單項目，用來執行腳本與更改設定。 | 1,226 | 2026-06-12 | MIT |  |
| [kobopatch](https://github.com/pgaskin/kobopatch) | 對 Kobo 原廠韌體套用社群修補，改變其行為。 | 134 | 2026-03-17 | MIT | 🛡️ |
| [kepubify](https://github.com/pgaskin/kepubify) | 把 EPUB 檔案轉成 Kobo 的 KEPUB 格式，以獲得更好的閱讀功能。 | 898 | 2025-12-06 | MIT |  |
| [KoboCloud](https://github.com/fsantini/KoboCloud) | 把 Dropbox、Google Drive 等雲端資料夾的書同步到裝置。 | 1,313 | 2026-09-24 | 未偵測到 |  |
| [Quill OS](https://github.com/Quill-OS/quill) | Kobo 電子書閱讀器的另一套作業系統，裝在內部 SD 卡上；已不再積極維護。 | 799 | 2026-08-14 | 未偵測到 | 🔧 🛡️ |

### Kindle e-readers

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [KindleEar](https://github.com/cdhigh/KindleEar) | 自架服務，把 RSS 與新聞摘要送到你的 Kindle。 | 2,880 | 2026-10-24 | MIT |  |
| [FBInk](https://github.com/NiLuJe/FBInk) | 直接在 Kindle 與 Kobo 螢幕上繪製文字與圖像的程式庫與工具。 | 554 | 2026-08-06 | GPL-3.0 |  |
| [kindle-dash](https://github.com/pascalw/kindle-dash) | 把已解鎖的 Kindle 變成低耗電的儀表板螢幕（只在 Kindle 4 NT 測試過）。 | 1,390 | 2024-03-04 | MIT | 🛡️ |
| [LanguageBreak](https://github.com/notmarek/LanguageBreak) | 解鎖自己的 Kindle（韌體 5.16.2.1.1 以下），以安裝 KOReader 等 app；會刪除所有內容。只連專案頁。 | 1,215 | 2025-01-30 | 未偵測到 | 🛡️ ⚠️ |

### reMarkable tablets

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [reStream](https://github.com/rien/reStream) | 把平板螢幕串流到電腦，方便簡報。 | 872 | 2026-06-10 | MIT |  |
| [rmview](https://github.com/bordaigorl/rmview) | 桌面檢視器，可即時接收平板的螢幕分享。 | 826 | 2025-10-08 | GPL-3.0 |  |

### PocketBook e-readers

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [Pocketbook-Nextcloud-Client](https://github.com/JuanJakobo/Pocketbook-Nextcloud-Client) | 從你的 Nextcloud 下載書籍的原生應用程式。 | 157 | 2025-08-25 | GPL-3.0 |  |
| [PocketPuzzles](https://github.com/SteffenBauer/PocketPuzzles) | 把 Simon Tatham 的益智遊戲集移植到 PocketBook 螢幕。 | 104 | 2026-05-23 | 未偵測到 |  |
| [Syncthing-for-PocketBook](https://github.com/mikedigriz/Syncthing-for-PocketBook) | 在裝置上執行 Syncthing，同步書籍資料夾。 | 58 | 2026-10-01 | Apache-2.0 |  |

## Android TV 與 Google TV

### Android TV and Google TV devices

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [AerialViews](https://github.com/theothernt/AerialViews) | 螢幕保護程式，播放 Apple TV 風格的空拍影片與自己的媒體。 | 1,119 | 2026-10-23 | 未偵測到 |  |
| [Jellyfin for Android TV](https://github.com/jellyfin/jellyfin-androidtv) | 連線到自己 Jellyfin 媒體伺服器的電視用戶端。 | 4,653 | 2026-10-24 | GPL-2.0 |  |
| [LtvLauncher](https://github.com/leanbitlab-org/LtvLauncher) | 沒有廣告的開源主畫面啟動器。 | 416 | 2026-10-25 | GPL-3.0 |  |
| [python-androidtv](https://github.com/JeffLIrion/python-androidtv) | 透過 ADB 控制 Android TV 與 Fire TV 裝置的 Python 程式庫。 | 196 | 2024-11-10 | MIT |  |

### Chromecast with Google TV

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [adb-auto-enable](https://github.com/mouldybread/adb-auto-enable) | 開機時自動開啟無線 ADB，讓家庭自動化能連上裝置；這會在區域網路上開放完整的裝置權限。 | 301 | 2026-10-18 | MIT |  |

### Amazon Fire TV

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [HA-Firemote](https://github.com/PRProd/HA-Firemote) | Home Assistant 遙控卡片，支援 Fire TV、Chromecast、NVIDIA Shield 等串流裝置。 | 1,091 | 2026-03-08 | GPL-3.0 |  |

### NVIDIA Shield TV

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [shield-commander](https://github.com/siewers/shield-commander) | 透過區域網路控制 Shield TV 的桌面應用程式。 | 46 | 2026-10-24 | MIT |  |

## 路由器

### Routers supported by OpenWrt

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [OpenWrt](https://github.com/openwrt/openwrt) | 開源 Linux 韌體，可取代路由器原廠軟體。 | 28,923 | 2026-10-25 | 未偵測到 | 🛡️ |

### ASUS routers

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [Asuswrt-Merlin](https://github.com/RMerl/asuswrt-merlin.ng) | 以 ASUS 原廠韌體為基礎的第三方韌體，加入額外功能與修正。 | 6,254 | 2026-10-25 | 未偵測到 | 🛡️ |
| [Asuswrt-Merlin (gnuton)](https://github.com/gnuton/asuswrt-merlin.ng) | 把 Asuswrt-Merlin 移植到主要專案未支援的 ASUS 機型。 | 2,379 | 2026-09-17 | 未偵測到 | 🛡️ |
| [amtm](https://github.com/decoderman/amtm) | 用來安裝與管理 Asuswrt-Merlin 附加套件的終端機選單。 | 237 | 2026-10-11 | GPL-3.0 |  |
| [IPSet_ASUS](https://github.com/Adamm00/IPSet_ASUS) | 防火牆附加元件，可封鎖已知的惡意 IP 位址。 | 439 | 2026-10-22 | 未偵測到 |  |

### GL.iNet routers

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [glinet-tailscale-updater](https://github.com/admonstrator/glinet-tailscale-updater) | 把內建的 Tailscale 更新到較新的版本。 | 786 | 2026-10-21 | MIT |  |
| [ha-glinet4-integration](https://github.com/HarvsG/ha-glinet4-integration) | 給執行 GL.iNet 韌體 4 的路由器用的 Home Assistant 整合。 | 100 | 2026-10-24 | Apache-2.0 |  |
| [MT6000_cust_build](https://github.com/pesa1234/MT6000_cust_build) | 為 GL-MT6000（Flint 2）調校的自訂 OpenWrt 版本。 | 204 | 2026-08-29 | 未偵測到 | 🛡️ |

### Broadcom-based routers (Netgear, Linksys, ASUS)

| 專案 | 用途 | ★ | 最後更新 | 授權 | 標記 |
|---|---|---:|---|---|---|
| [FreshTomato](https://github.com/FreshTomato-Project/freshtomato-arm) | 以 Tomato 為基礎、給 ARM Broadcom 路由器用的開源韌體。 | 197 | 2026-10-22 | GPL-3.0 | 🛡️ |

## 收錄規則

收錄：對自己的裝置做合法的客製化。例如開源韌體、不經原廠雲端的本機控制、外掛 app、設定檔與配方檔、相容配件。

不收錄：破解 DRM、繞過授權金鑰或付費機制、盜版、遊戲 ROM、帳號共享、繞過電信鎖。解鎖自己裝置的專案（例如電子書閱讀器）只連到專案頁，並加上 ⚠️ 標記。本清單不提供解鎖步驟，也不存放任何程式碼、韌體或檔案。連結的 repo 若被 GitHub 停用（例如收到 DMCA 通知），就會移除該筆。專案作者可以開 issue 要求移除。

超過 3 年沒有更新的專案不收，或標為 📦。星數、最後更新日期與授權來自 GitHub API（`scripts/refresh.py`），最近一次更新在 2026-10-25。

## 風險標記

每個專案會顯示適用的標記。

| | |
|---|---|
| ⚡ | 裝置內有市電 |
| 🔧 | 需要拆機或焊接 |
| 🛡️ | 可能失去保固 |
| 📦 | 已封存或超過 3 年未更新 |
| ⚠️ | 會解鎖裝置；請先讀專案頁並確認當地法律 |

## 免責聲明

自己的裝置自己負責。改裝可能損壞硬體、失去保固或違反原廠條款。在部分國家，解鎖裝置也可能受反規避法規限制。改裝接市電的裝置（⚡）可能致命：先拔插頭；沒有把握就交給合格的人做。請遵守當地法律與保固條款。專案屬於各自的作者，本清單不檢查它們的程式碼。

## 延伸閱讀

- [awesome-home-assistant](https://github.com/frenck/awesome-home-assistant) - Home Assistant 整合與資源。
- [Awesome-Kindle](https://github.com/KindleTweaks/Awesome-Kindle) - Kindle 調校與工具。
- [awesome-smart-tv](https://github.com/vitalets/awesome-smart-tv) - 智慧電視 app 開發。
- [Awesome-Android-TV-FOSS-Apps](https://github.com/Generator/Awesome-Android-TV-FOSS-Apps) - 自由開源的 Android TV app。
- [awesome-eink](https://github.com/asapelkin/awesome-eink) - 電子紙裝置與軟體。

## 貢獻方式

開 pull request 前，請先讀 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 授權

[CC0-1.0](LICENSE)。在法律允許的範圍內，貢獻者放棄本清單的所有著作權。
