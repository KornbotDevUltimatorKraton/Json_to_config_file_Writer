import configparser # Using the configparser to generate config file from the json 
import json 
import threading # Getting the threading function 
config = configparser.ConfigParser() 
component = {'Speech_recognition':{'initial_lang':"'th'",'destination_lang':"'en'",'ip':"'127.0.0.1'",'speed':"'1.04'",'Loudness':100,'Buffers':65536,'port':5080}}
for r in list(component):
      config.add_section(r)
      for t in list(component.get(r)):
             config.set(str(r),str(t),str(component.get(r).get(t)))
             configfile = open("Autogenerate_File.cfg",'w')
             config.write(configfile)      




