from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import requests
import json
import os 

date = datetime.datetime.now()
formatted_date_time = date.strftime("%Y-%m-%dT%H:%M:%S%z")
formatted_date_time += "+02:00"


url="https://httpbin/post"


with open("test.json") as f:
    data = json.load(f)

data["signedOn"]  = formatted_date_time

# print(data)
header = {
    "Host": "app.sowesign.com",
    "Content-Length": "16489",
    "Sec-Ch-Ua": '"Chromium";v="117", "Not;A=Brand";v="8"',
    "Accept-Language": "fr",
    "Sec-Ch-Ua-Mobile": "?0",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoicmVjb3ZlcnkiLCJjbGllbnQiOnsiaWQiOjEwMTIsIm5hbWUiOiJMZSBDYW1wdXMgTnVtw6lyaXF1ZSBpbiB0aGUgQWxwcyIsInR5cGUiOiJzdGFuZGFyZCIsImNvcnBvcmF0ZUNvbm5lY3RvciI6bnVsbCwidG9rZW4iOiJSRSJ9LCJpYXQiOjE2OTYyNTc2NjUsImVudGl0eSI6eyJpZCI6OTA2NTYsInR5cGUiOiJyZWNvdmVyeSJ9LCJleHAiOjE2OTYyNzIwNjUsImF1ZCI6Imh0dHBzOi8vYXBwLnNvd2VzaWduLmNvbSIsImlzcyI6Imh0dHBzOi8vYXBwLnNvd2VzaWduLmNvbSJ9.dEzgdrHV7We0l3SwHLkpZmZqj67c7xJ3vl273Od0ZSw",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36",
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Origin": "https://app.sowesign.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://app.sowesign.com/sign/signature/recovery/1012/4c914dc3-0c09-431d-8c68-26437d51cc36",
    "Accept-Encoding": "gzip, deflate, br",
}


# requests.post(url,data=data, headers=header)

