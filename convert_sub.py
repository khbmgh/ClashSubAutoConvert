import requests
import base64
import yaml

# لینک‌های ساب شما
urls = [
    "https://raw.githubusercontent.com/10ium/VpnClashFaCollector/main/sub/tested/speed_passed.txt",
    "https://raw.githubusercontent.com/10ium/VpnClashFaCollector/main/sub/tested/ping_passed.txt",
    "https://raw.githubusercontent.com/10ium/VpnClashFaCollector/main/sub/all/mixed.txt",
    "https://raw.githubusercontent.com/10ium/VpnClashFaCollector/main/sub/AR14N24B/mixed_base64.txt",
    "https://raw.githubusercontent.com/10ium/VpnClashFaCollector/main/sub/xsfilternet/mixed_base64.txt"
]

all_subs = []

for url in urls:
    r = requests.get(url)
    if r.status_code == 200:
        text = r.text.strip()
        if "base64" in url:  # اگر Base64 بود، decode کن
            try:
                text = base64.b64decode(text).decode("utf-8")
            except Exception as e:
                print(f"Base64 decode error for {url}: {e}")
        lines = text.splitlines()
        all_subs.extend(lines)
    else:
        print(f"Failed to fetch {url}, status {r.status_code}")

# حذف تکراری‌ها
all_subs = list(dict.fromkeys(all_subs))

# ساختار خروجی Clash
clash_yaml = {
    "proxies": all_subs,
    "proxy-groups": [
        {
            "name": "Auto",
            "type": "select",
            "proxies": all_subs
        }
    ],
    "rules": ["MATCH,Auto"]
}

# ذخیره به فایل
with open("clash_sub.yaml", "w", encoding="utf-8") as f:
    yaml.dump(clash_yaml, f, allow_unicode=True)

print("✅ Clash sub updated successfully!")
