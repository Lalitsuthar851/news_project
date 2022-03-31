from django.shortcuts import render,HttpResponse,redirect
import newspaper
from wordcloud import WordCloud,STOPWORDS
from newspaper import Article
import nltk
import shutil
import os
from os import path
nltk.download('punkt')
# Create your views here.

def home(request,
         ):
    return render(request,
                  "index.html",
                  )

def scraper(request,
            ):
    if request.method == "POST":
        name = request.POST.get("page")
        print(name)
        article = Article(name)

        try:
            article.download()
            article.parse()
            article.nlp()
            text=article.text
            title=article.title
            keywords = article.keywords
            print(type(keywords))
            summmary = article.summary
            print(summmary,keywords)
            author = article.authors

            date=article.publish_date
            url=article.url



            stopwords=STOPWORDS

            wc=WordCloud(background_color="white",stopwords=stopwords,height=400,width=400)
            wc.generate(' '.join(keywords))

            wc2 = WordCloud(background_color="gray", stopwords=stopwords, height=400, width=400)
            wc2.generate(' '.join(keywords))
            file=wc.to_file(os.path.join('./news/static/img/wordcloud.png'))
            file__=wc.to_file(os.path.join('./staticfiles/img/wordcloud.png'))
            file2=wc2.to_file(os.path.join('./news/static/img/wordcloud2.png'))
            file_2 = wc2.to_file(os.path.join('./staticfiles/img/wordcloud2.png'))





            if author==[]:
                    author=" "


            return render(
                    request,
                "slider/dist/index.html",
                {"title":title,"summary":summmary,
                 "text":text,
                 "author":author[0],
                 "keyword":keywords,
                "publish_date":date,"url":url}
            )
        except:
            return HttpResponse("plz enter valid url")


    return render(request,"newsscraper.html",
                  )

def handler404( request,
               exception
               ):

    return redirect("home")

def handler500(request,
               ):
    return redirect("home")
