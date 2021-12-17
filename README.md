# hostsscan
host碰撞小工具，用于寻找未设置dns的隐藏域名,自动以域名和时间戳保存扫描结果。<br>
-ip 参数指定目标服务器ip地址 <br>
-domain 参数想要扫描的主域名 <br>
-dict 指定子域名字典文件，默认使用subdomain.txt <br>


用法示例 <br>
python3 hostsscan.py -ip 193.168.1.78 -domain webhack123.com <br>
![image](https://user-images.githubusercontent.com/57749670/146505189-4879c3b1-1194-4605-b03f-a98baef19191.png)

