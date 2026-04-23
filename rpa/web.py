import requests
import datetime
#测试sshfyuf
URLS = [
    "https://fourddecision-backend.onrender.com/api/hello",
    
]

def check_health(url):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"[{now}] ✅ 正常 - {url} - 状态码: {response.status_code}, 响应时间: {response.elapsed.total_seconds():.2f}s")
        else:
            print(f"[{now}] ⚠️ 异常 - {url} - 状态码: {response.status_code}")
    except requests.exceptions.Timeout:
        print(f"[{now}] ❌ 超时 - {url}")
    except requests.exceptions.ConnectionError:
        print(f"[{now}] ❌ 连接失败 - {url}")
    except Exception as e:
        print(f"[{now}] ❌ 未知错误 - {url} - {e}")

if __name__ == "__main__":
    for url in URLS:
        check_health(url)


