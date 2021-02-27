from fake_useragent import UserAgent
headers = UserAgent(verify_ssl=False).random
print(headers)