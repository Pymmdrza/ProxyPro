'''
ProxyPro - Create Fast Proxy List With Python
Programmer MMDRZA.Com
2022-2-24
==============================
 ____                      ____
|  _ \ _ __ _____  ___   _|  _ \ _ __ ___
| |_) | '__/ _ \ \/ / | | | |_) | '__/ _ \
|  __/| | | (_) >  <| |_| |  __/| | | (_) |
|_|   |_|  \___/_/\_\\__, |_|   |_|  \___/
                     |___/

==============================
w W w . M M D R Z A . C o M
'''
import random
import time
from colorama import Fore, Style



# ==================================[ M M D R Z A . C o M ]==================================

def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled: str = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled

# ==================================[ M M D R Z A . C o M ]==================================

z = 0
walletbtc = "16p9y6EstGYcnofGNvUJMEGKiAWhAr1uR8"
walletusdt = "TSb4w985WJ2zdDtTvex6jjFLejqZHGK5ez"
btc = str(walletbtc)
usdt = str(walletusdt)
# For Rec Many IP Needed On Clinet (int)
hwx = input('How Many Proxy IP Needed = ')
# ==================================[ M M D R Z A . C o M ]==================================
while True:
    # For Port Proxy
    sboter = random.randint(1000, 9999)
    # For IP proxy
    ixpro = spoofer()
    prox = str(ixpro) + ':' + str(sboter)
    z += 1
# ==================================[ M M D R Z A . C o M ]==================================
    print(Fore.WHITE, str(z), Fore.RED, ' IP =', Fore.GREEN, str(prox))
    # Save All Details On the Text File ProxyList.txt ( IPProxy+Port )
    f = open(u"ProxyList.txt", "a")
    f.write('\n' + prox)
    f.close()
    # Save Only IP Without Port
    f1 = open("ipList.txt", "a")
    f1.write('\n' + ixpro)
    f1.close()
# ==================================[ M M D R Z A . C o M ]==================================
    if z == int(hwx):
        time.sleep(4)
        print(Fore.YELLOW, "====================================")
        print(Fore.GREEN, 'End Create Proxy List')
        time.sleep(2)
        print(Fore.WHITE,'Donate (BTC)=', str(btc), '\nDonate (USDT-TRC20)=', str(usdt))
        time.sleep(1)
        print(Fore.WHITE, 'Programmer = M M D R Z A ')
        print(Fore.RED, 'Website = Mmdrza.Com ')
        print(Fore.RED, 'Email = x4@Mmdrza.Com')
        print(Fore.YELLOW, "====================================",Style.RESET_ALL)

        break
# For Donate ( Bitcoin Address ) : 16p9y6EstGYcnofGNvUJMEGKiAWhAr1uR8
