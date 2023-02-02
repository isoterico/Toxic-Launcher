#!/usr/bin/python3
import time
import os
import subprocess
from os import system
from subprocess import call

def msfinstall():
  call(["sh", "-c", "sudo snap install metasploit-framework"])
  subprocess.run(["clear"])
  print("[*]-[Install]-[*]: Installazione di MsfConsole.")
  time.sleep(0.5)
  subprocess.run(["clear"])
  print("[*]\[Install]/[*]: Installazione di MsfConsole..")
  time.sleep(0.5)
  subprocess.run(["clear"])
  print("[*]|[Install]|[*]: Installazione di MsfConsole...")
  time.sleep(0.5)
  subprocess.run(["clear"])
  print("[*]-[Info]-[*]: Installazione di MsfConsole completata con successo!")

msfinstall()
