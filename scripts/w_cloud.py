import requests

url = "https://textvis-word-cloud-v1.p.rapidapi.com/v1/textToCloud"

payload = {
	"text": "This is a test. I repeat, this is a test. We are only testing the functionality of this api, nothing else. End of test.",
	"scale": 0.5,
	"width": 400,
	"height": 400,
	"colors": ["#375E97", "#FB6542", "#FFBB00", "#3F681C"],
	"font": "Tahoma",
	"use_stopwords": True,
	"language": "en",
	"uppercase": False
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "textvis-word-cloud-v1.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())