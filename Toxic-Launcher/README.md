# ToxicSecTools - Sample Launcher
### { *Un semplice e veloce Hacking Launcher* }
 

Nel tool sono presenti solo 4 tool tra cui 3 attualmente funzionanti,
Il tool verrà aggiornato, pertanto rimanete sintonizzati al repository.

# Prossime Novità:

- Osint Tool
- Auto-Update
- ✨!Work In Progress!✨

## Features

- ### *Phishing:*
      Il phishing è un tipo di truffa effettuata su Internet attraverso la quale
      un malintenzionato cerca di ingannare la vittima convincendola a fornire 
      informazioni personali, dati finanziari o codici di accesso, 
      fingendosi un ente affidabile in una comunicazione digitale (Pagina Di Accesso).

- ### *Payload / Reverse Shell:*
      È una tecnica per eseguire comandi sulla macchina della vittima; 
      la particolarità di questo attacco è che la connessione si origina 
      dal sistema infetto verso l'attaccante, 
      al quale viene dato poi accesso alla shell dei comandi.

- ### *DDoS:*
      Nel campo della sicurezza informatica, un attacco denial-of-service o 
      attacco DoS (lett. "attacco di negazione del servizio") indica un malfunzionamento 
      dovuto a un attacco informatico in cui si fanno esaurire deliberatamente le risorse
      di un sistema informatico che fornisce un servizio ai client, ad esempio un sito
      web su un server web, fino a renderlo non più in grado di erogare il servizio ai client
      richiedenti.

- ### *Osint:*
      La Open Source INTelligence, acronimo OSINT (in italiano: "Intelligence su fonti aperte"[2]),
      è quella disciplina dell'intelligence che si occupa della ricerca, 
      raccolta ed analisi di dati e di notizie d'interesse pubblico tratte da fonti aperte.
      OSINT è stata introdotta durante la seconda guerra mondiale 
      dalle agenzie di sicurezza di alcune nazioni.

# Metodi DDoS List:
### *Layer 7*

| Metodo | Descrizione |
| ------ | ----------- |
| > GET |  *GET Flood* |
| > POST | *POST Flood* |
| > OVH | *Bypass OVH* |
| > RHEX | *Random HEX* |
| > STOMP | *Bypass chk_captcha* |
| > STRESS | *Send HTTP Packet With High Byte* |
| > DYN | *A New Method With Random SubDomain* |
| > DOWNLOADER | *A New Method of Reading data slowly* |
| > SLOW | *Slowloris Old Method of DDoS* |
| > HEAD | *https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD* |
| > NULL | *Null UserAgent and ...* |
| > COOKIE | *Random Cookie PHP 'if (isset($_COOKIE))'* |
| > PPS | *Only 'GET / HTTP/1.1\r\n\r\n'* |
| > EVEN | *GET Method with more header* |
| > GSB | *Google Project Shield Bypass* |
| > DGB | *DDoS Guard Bypass* |
| > AVB | *Arvan Cloud Bypass* |
| > BOT | *Like Google bot* |
| > APACHE | *Apache Expliot* |
| > XMLRPC | *WP XMLRPC expliot (add /xmlrpc.php)* |
| > CFB | *CloudFlare Bypass* |
| > CFBUAM | *CloudFlare Under Attack Mode Bypass* |
| > BYPASS | *Bypass Normal AntiDDoS* |
| > BOMB | *Bypass with codesenberg/bombardier* |
| > KILLER | *run many threads to kill a target* |
| > TOR | *Bypass onion website* |

### *Layer 4*
| Metodo | Descrizione|
| ------ | ---------- |
| > TCP | *TCP Flood Bypass* |
| > UDP | *UDP Flood Bypass* |
| > SYN | *SYN Flood* |
| > CPS | *Open and close connections with proxy* |
| > ICMP | *Icmp echo request flood (Layer3)* |
| > CONNECTION | *Open connection alive with proxy*
| > VSE | *Send Valve Source Engine Protocol*
| > TS3 | *Send Teamspeak 3 Status Ping Protocol* |
| > FIVEM | *Send Fivem Status Ping Protocol* |
| > MEM | *Memcached Amplification* |
| > NTP | *NTP Amplification* |
| > MCBOT | *Minecraft Bot Attack* |
| > MINECRAFT | *Minecraft Status Ping Protocol* |
| > MCPE | *Minecraft PE Status Ping Protocol* |
| > DNS | *DNS Amplification* |
| > CHAR | *Chargen Amplification* |
| > CLDAP | *Cldap Amplification* |
| > ARD | *Apple Remote Desktop Amplification* |
| > RDP | *Remote Desktop Protocol Amplification* |


## INSTALLAZIONE

##### *Python 3 Required.*

Istruzioni per scaricare ed installare il Tool.

```sh
git clone https://github.com/isoterico/ToxicSecTools
cd ToxicSecTools
sudo apt install < requirements.txt
python3 install.py
```
Il Tool si avvierà in completa autonomia successivamente all'installazione...
#### Avvio manuale:
```sh
python3 ToxicSec.py
```

## Plugins

*Qui puoi trovare i repository degli strumenti lanciati dal launcher.
(Se hai dubbi sul funzionamento di uno di loro... Li trovi qui sotto!)*

| Plugin | README |
| ------ | ------ |
| Phishing | [*https://github.com/KasRoudra/PyPhisher*] |
| Payload | [*https://github.com/r00t-3xp10it/venom*] |
| DDoS | [*https://github.com/MatrixTM/MHDDoS*] |
| Osint | *!-Work In Progress-!* |


## *Ringraziamenti*
| Developer |
| --------- |
| Isoterico |

| Ringraziamenti |
| -------------- |
| PyPhisher      |
| Venom          |
| MHDDoS         |
