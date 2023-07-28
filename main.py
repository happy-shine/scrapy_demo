import hashlib
import json


def l(t):
    result = ""
    for key in sorted(t.keys()):
        value = t[key]
        if value is not None:
            if isinstance(value, (dict, list)):
                value = json.dumps(value)
            result += key + str(value)
    return result


def portal_sign(t):
    r_a = "B3978D054A72A7002063637CCDF6B2E5"  # 这是你提供的r["a"]值
    t = {k: v for k, v in t.items() if v is not None and v != ""}
    n = r_a + l(t)
    return hashlib.md5(n.encode()).hexdigest().lower()  # 假设s函数是md5哈希


print(portal_sign({
    'IS_IMPORT': 1,
    'pageSize': 3,
    "ts": '1690532174221',
    'type': "12"
}))
