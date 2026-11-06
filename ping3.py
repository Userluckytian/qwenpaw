# -*- coding: utf-8 -*-
"""最简版：访问三个保活地址，必须 HTTP 200 才算过"""
import sys
import urllib.request

URLS = [
    "https://url-fetch-proxy.app.workbuddy.host/?sharecode=URA34JXSBU",
    "https://aa6fdf0bbd8ec5018.app.workbuddy.host/?sharecode=2YGOCFSQFH",
    "https://npc-tunnel-client.app.workbuddy.host/?sharecode=EREAFNURUR",
    "https://npc-tunnel-client-39357.app.workbuddy.host/api/status?sharecode=ZL546S6MK2",
]

ok = True
for u in URLS:
    try:
        with urllib.request.urlopen(u, timeout=30) as r:
            status = r.status
    except Exception as e:
        status = str(e)
    passed = status == 200
    print(("PASS" if passed else "FAIL"), status, u)
    ok = ok and passed

sys.exit(0 if ok else 1)
