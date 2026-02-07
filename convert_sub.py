import requests
import base64

# لینک‌های ساب سورس تو
sources = [
    "https://raw.githubusercontent.com/10ium/VpnClashFaCollector/main/sub/tested/speed_passed.txt",
    "https://raw.githubusercontent.com/10ium/VpnClashFaCollector/main/sub/tested/ping_passed.txt",
    "https://raw.githubusercontent.com/10ium/VpnClashFaCollector/main/sub/all/mixed.txt",
    "https://raw.githubusercontent.com/10ium/VpnClashFaCollector/main/sub/AR14N24B/mixed_base64.txt",
    "https://raw.githubusercontent.com/10ium/VpnClashFaCollector/main/sub/xsfilternet/mixed_base64.txt"
]

final_content = ""

for url in sources:
    r = requests.get(url)
    if r.status_code == 200:
        data = r.text.strip()
        # اگر Base64 بود کانورت کن
        if "base64" in url:
            try:
                data = base64.b64decode(data).decode()
            except:
                pass
        final_content += data + "\n"
    else:
        print(f"Failed to fetch: {url}")

# فایل خروجی برای Clash
with open("clash_sub.yaml", "w", encoding="utf-8") as f:
    f.write(final_content)
