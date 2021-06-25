import os, time , sys, requests
from colorama import Fore
from colored import fg


R = Fore.RESET
b = Fore.LIGHTBLACK_EX
p = fg('#8A2BE2	')
f = fg('#9370DB')

clear = lambda: os.system('cls') if os.name == 'nt' else os.system('clear')

token = "your token"

os.system('title [Krii$ 4L Tool]')

def kriis():
  print(f'''
                                  
      {R}██╗  ██╗██████╗ ██╗██╗███████╗
      ██║ ██╔╝██╔══██╗██║██║██╔════╝
      {b}█████╔╝ ██████╔╝██║██║███████╗
      ██╔═██╗ ██╔══██╗██║██║╚════██║
      {f}██║  ██╗██║  ██║██║██║███████║
      {p}╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝╚══════╝
                              

  {R}''')

kriis()

def kriisK(cID):
  z = 0
  payload = {'content': "the msg to send here"}
  header = {'authorization': token}
  time.sleep(420)
  r = requests.post(f"https://discord.com/api/v8/channels/{cID}/messages", data=payload, headers=header)
  if r.status_code == 429:
    print(f"[{f}~ {p}STATUS {f}~{R}] Â· {p}Error Couldn't Send{R}")
  if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
    z += 1
    print(f"[{f}~ {p}STATUS {f}~{R}] Â· {p}Sent Payload in {R}[{p}{cID}{R}] | {p}Time{R}: {p}420 {R}ms")
    os.system('title [Krii$ 4L Tool] â”‚ Watching: [{cid}] â”‚ Payloads Sent: [{z}]')



def start():
  while True:
    kk = input(f'[ {p}~ {R}] Â· {p}Want To Start Watcher y:{R}/{p}n{R}:{p} ')
    if "yes" in kk.content.lower():
      clear()
      kriis()
      cID = input(f"[~ STATUS ~] Â· Channel ID:  ")
      clear()
      kriis()
      kriisK(cID)
    elif "y" in kk.content.lower():
      clear()
      kriis()
      cID = input(f"[~ STATUS ~] Â· Channel ID:  ")
      clear()
      kriis()
      kriisK(cID)
    elif "n" in kk.content.lower():
      print("Then why the fuck did u open it you dumb piece of shit")
      time.sleep(50)
    elif "no" in kk.content.lower():
      print("Then why the fuck did u open it you dumb piece of shit")
      time.sleep(50)
    
      

if __name__ == '__main__':
  start()
