##————————————————————————————————————————————##    
#说明：本程序用于从https://github.com/Alvin9999/new-pac/wiki下载goflyway\ss\ssr\v2ray的配置文件。
#程序运行格式：
#    python downloadcon.py
#存储路径：D:\works\software\VPN\dongtaiwang\
##————————————————————————————————————————————##

import requests
from bs4 import BeautifulSoup

def get_con(url,proxcon,filepath):
    print(url)
    print(filepath)
    # 发送HTTP请求
    response = requests.get(url)

    # 检查请求是否成功
    if response.status_code == 200:
        # 解析网页内容
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 查找包含特定文本的元素
        pre_tags = soup.find_all('pre')  # 在网页中，vmess链接通常会在 <pre> 标签内
        
        # 打开文件用于写入
        with open(filepath, 'w') as file:
            for pre in pre_tags:
                #if 'vmess://' in pre.get_text():
                #print(pre.get_text())
                if proxcon in pre.get_text():
                    link = pre.get_text().strip()
                    # 写入文件
                    file.write(link + '\n')
                    print('Found and wrote link:\n', link)         
    else:
        print('请求失败，状态码：', response.status_code)
    
def mergefile(file1,file2,output_file):
    # 定义要合并的文件名
    # file1 = 'file1.txt'
    # file2 = 'file2.txt'
    # output_file = 'merged_file.txt'

    # 打开第一个文件并读取内容
    with open(file1, 'r', encoding='utf-8') as f1:
        content1 = f1.read()

    # 打开第二个文件并读取内容
    with open(file2, 'r', encoding='utf-8') as f2:
        content2 = f2.read()

    # 将两个文件的内容写入到一个新文件中
    with open(output_file, 'w', encoding='utf-8') as f_out:
        f_out.write(content1 + '\n' + content2)

    print(f"文件 {file1} 和 {file2} 已合并为 {output_file}")       
                
if __name__ == "__main__":
    print("注意，可能需要vpn，可运行vpn工具后开启系统代理！")
    ##获取v-ray配置
    prox1 = 'v2ray'  
    prox1_1 = 'v2ray_1'
    prox1_2 = 'v2ray_2'
    proxcon1_1 = 'vmess://' 
    proxcon1_2 = 'vless://'
    url1 = 'https://github.com/Alvin9999/new-pac/wiki/v2ray%E5%85%8D%E8%B4%B9%E8%B4%A6%E5%8F%B7'     
    filepath1_1 = 'D:\\software\\vpn软件客户端\\dongtaiwang\\'+ prox1_1+'.txt'  
    filepath1_2 = 'D:\\software\\vpn软件客户端\\dongtaiwang\\'+ prox1_2+'.txt'
    filepath1 = 'D:\\software\\vpn软件客户端\\dongtaiwang\\'+ prox1+'.txt'
    get_con(url1,proxcon1_1,filepath1_1)
    get_con(url1,proxcon1_2,filepath1_2)
    mergefile(filepath1_1,filepath1_2,filepath1)
    
    # ##获取goflyway配置
    prox2 = 'goflyway'
    proxcon2 = 'goflyway' 
    url2 = 'https://github.com/Alvin9999/new-pac/wiki/Goflyway%E5%85%8D%E8%B4%B9%E8%B4%A6%E5%8F%B7'    
    filepath2 = 'D:\\software\\vpn软件客户端\\dongtaiwang\\'+ prox2+'.txt'
    get_con(url2,proxcon2,filepath2)
    
    # ##获取ss配置
    prox3 = 'ss'
    proxcon3 = 'ss:'  
    url3 = 'https://github.com/Alvin9999/new-pac/wiki/ss%E5%85%8D%E8%B4%B9%E8%B4%A6%E5%8F%B7'    
    filepath3 = 'D:\\software\\vpn软件客户端\\dongtaiwang\\'+ prox3+'.txt'
    get_con(url3,proxcon3,filepath3)
    
    # ##获取ssr配置
    prox4 = 'ssr'
    proxcon4 = 'ssr:'     
    filepath4 = 'D:\\software\\vpn软件客户端\\dongtaiwang\\'+ prox4+'.txt'
    get_con(url3,proxcon4,filepath4)
