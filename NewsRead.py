import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    api_dict = {"business" : "https://www.livemint.com/market/stock-market-news/stocks-to-watch-tata-consumer-itc-tata-steel-ioc-torrent-power-titagarh-rail-granules-india-11722395292631.html",
            "entertainment" : "https://www.123telugu.com/mnews/mahesh-babu-wins-the-hearts-of-tamil-audience.html",
            "health" : "https://www.moneycontrol.com/health-and-fitness/health-benefits-of-cinnamon-cinnamon-isnt-just-for-baking-heres-how-this-spice-can-actually-boost-your-health-article-12783162.html",
            "science" :"https://www.news18.com/education-career/neet-pg-2024-nbems-to-release-exam-city-allotment-slip-today-check-details-8985094.html",
            "sports" :"https://sports.ndtv.com/",
            "technology" :"https://www.cnbctv18.com/market/earnings/dixon-tech-share-price-mobile-manufacturing-growth-smartphones-it-hardware-and-components-brokerages-view-fy25-19452136.htm"
}

    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = input("Type field news that you want: ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break
        
    speak("thats all")
