#!/usr/bin/python3
import time
import os
import subprocess
from os import system
from subprocess import call


def update():
  call(["sh", "-c", "sudo rm -r ToxicSecTools"])
  dir = 'ToxicSecTools'
  if not os.path.exists(dir): # if the directory does not exist
      call(["sh", "-c", "git clone https://github.com/isoterico/ToxicSecTools.git"]) # make the directory
  else: # the directory exists
      #remove a folder
      call(["sh", "-c", "sudo rm -r ToxicSecTools"])
      call(["sh", "-c", "git clone https://github.com/isoterico/ToxicSecTools.git"]) # make the directory
      print("[*]-[Info]-[*]: Aggiornamento completato con successo!.")
      time.sleep(1)
      print("[*]-[Info]-[*]: Avvio del Tool in corso...")
      time.sleep(2)
      call(["sh", "-c", "cd ToxicSecTools"])
      call(["sh", "-c", "python3 install.py"])
update()
