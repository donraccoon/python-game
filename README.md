Hier zijn de instructies om pong.py te draaien in een folder genaamd pong_pygame, inclusief hoe je Python installeert en pygame installeert op zowel Windows als Linux.

Stap 1: Installeer Python
Windows
Download de nieuwste versie van Python van de officiële website:
 https://www.python.org/downloads/
Open het installatiebestand.
BELANGRIJK: Vink de optie "Add Python to PATH" aan voordat je op "Install Now" klikt.
Wacht tot de installatie is voltooid en klik op "Close".
Linux (Debian/Ubuntu):
Open een terminal en voer de volgende opdrachten uit:
sudo apt update
sudo apt install python3 python3-pip -y

Voor andere Linux-distributies, gebruik het pakketbeheersysteem van je distributie (bijvoorbeeld dnf voor Fedora of pacman voor Arch Linux).

Stap 2: Controleer of Python correct is geïnstalleerd
Open een terminal of de Opdrachtprompt (cmd) en typ:
python --version

of (indien nodig op sommige systemen):
python3 --version

Dit zou een versie moeten tonen, bijvoorbeeld:
Python 3.11.2

Als je een foutmelding krijgt, start je computer opnieuw op en probeer het opnieuw.

Stap 3: Pygame installeren
Windows
Open de Opdrachtprompt en voer uit:
pip install pygame

Linux
Open een terminal en voer uit:
pip3 install pygame

Controleer de installatie met:
python -m pygame --version

Stap 4: Pong.py uitvoeren
Maak een map genaamd pong_pygame en plaats het bestand pong.py daarin.

Navigeer naar de map in de terminal of opdrachtprompt:

 Windows (cmd of PowerShell):

 cd path\naar\pong_pygame
 Bijvoorbeeld, als de map in je documenten staat:
 cd C:\Users\JouwNaam\Documents\pong_pygame
 
Linux:
 cd ~/pong_pygame

Voer het spel uit:

 Windows:
 python pong.py
 Linux:
 python3 pong.py

Als alles correct is geïnstalleerd, zou het Pong-spel moeten starten! 🚀
