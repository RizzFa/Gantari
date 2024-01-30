import http.client
import json
import time

print("=================================================")
print("🇬‌🇦‌🇳‌🇹‌🇦‌🇷‌🇮‌ 🇨‌🇴‌🇲‌🇲‌🇺‌🇳‌🇮‌🇹‌🇾‌‌")
print("=================================================")
author = "Faris#0064"
print("Author: " + author)
script = "Auto Post Discord"
print("Script: " + script)
discord = "dsc.gg/gantari"
print("Discord: " + discord)
print("===========================================\n")

time.sleep(1)

channel_id = input("masukkan channel ID: ")
waktu = int(input("Set Waktu Kirim Pesan: "))

time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

with open('./config.json') as f:
    config_data = json.load(f)
    token = config_data['Config'][0]['token']  # config.json
    message = config_data['Config'][0]['message']  # config.json

header_data = { 
    "Content-Type": "application/json", 
    "User-Agent": "DiscordBot", 
    "Authorization": token  
} 

def get_connection(): 
    return http.client.HTTPSConnection("discord.com", 443) 

def send_message(conn, channel_id, message_data): 
    try: 
        conn.request("POST", f"/api/v10/channels/{channel_id}/messages", message_data, header_data) 
        resp = conn.getresponse() 
         
        if 199 < resp.status < 300: 
            print(Fore.WHITE + "Pesan terkirim: ")
            print(Fore.YELLOW + payload["content"])
        else: 
            print(f"HTTP {resp.status}: {resp.reason}")
    except: 
        print("Error.") 

def main(): 
    message_data = { 
        "content": message + "== Gantari Community ==", 
        "tts": False
    } 

    send_message(get_connection(), channel_id, json.dumps(message_data)) 

if __name__ == '__main__': 
    while True:    
        main()      
        time.sleep(waktu)
