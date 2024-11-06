# https://docs.python.org/zh-cn/3.10/library/socket.html#socket.socket.connect
# https://docs.python.org/zh-cn/3.10/library/sys.html#module-sys
# https://requests.readthedocs.io/projects/cn/zh-cn/latest/
# 功能太简单。。。
import socket
import sys
import requests

def GetIp():
    # 获取本地电脑的IP
    MyIp = requests.get("https://myip.ipip.net").text
    LocalIp = MyIp.split("：")[1].split(" ")[0]
    print("本地Ip:%s\n" % LocalIp)

def ScanIp(IP,port):
    # 扫描对应的IP
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0)
    # IP = sys.argv[1]
    # port = int(sys.argv[2])
    try:
        print("准备连接到%s:%d\n" % (IP, port))
        sock.connect((IP, port))
        print("成功连接到:%s:%d\n" % (IP,port))
    except TimeoutError:
        print("目标地址%s:%d连接超时\n" % (IP, port))
    except ConnectionRefusedError:
        print("由于目标计算机积极拒绝，无法连接\n")
    except Exception as Error:
        print("出现报错:%s\n" % Error)

def ScanDomain(domain):
    # 扫描对应的域名并获取对应的IP
    ports = [80,443]
    IpList = []
    try:
        for port in ports:
            print("准备扫描域名：%s\n" % domain)
            IpInfos = socket.getaddrinfo(domain,port)
            for IpInfo in IpInfos:
                Ip = IpInfo[4][0]
                Port = IpInfo[4][1]
                IpList.append([Ip,Port])
                ScanIp(Ip,Port)
        print("\n域名%sIp池中的Ip地址有：\n" % domain)
        for Ip in IpList:
            print("IP=%s, Port=%s" % (Ip[0],Ip[1]))
    except Exception as error:
        print("出现报错：" % error)

if __name__ == "__main__":
    ChosenNum = int(input("选择你要进行的操作：\n\t1.获取本地电脑ip;\n\t2.扫描IP;\n\t3.扫描域名;\n\t你要选择的操作:(用数字选择，如1):"))
    if (ChosenNum==1):
        GetIp()
    elif(ChosenNum==2):
        Ip = input("输入需要扫描的IP：")
        ScanIp(Ip)
    elif(ChosenNum==3):
        domain = input("输入需要扫描的域名:")
        ScanDomain(domain)

    sys.exit()
