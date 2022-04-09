from django.shortcuts import render,HttpResponse,redirect
import newspaper
from wordcloud import WordCloud,STOPWORDS
from newspaper import Article
import nltk
import os
from os import path

"""here model is downloaded"""
nltk.download('punkt')



def home(request,
         ):
    """ here the home page will be rendered"""
    return render(request,
                  "index.html",
                  )

def scraper(request,
            ):
    """post request will passed here"""
    if request.method == "POST":
        name = request.POST.get("page",
                                )
        keywords_number=request.POST.get("quantity")
        article = Article(name)


        try:
            """article will be downloaded here"""
            article.download()
            article.parse()
            article.nlp()

            #article
            text=article.text
            title=article.title

            #keyword willl be parsed here
            keywords = article.keywords

            #article will be coverted in summary here
            summmary = article.summary

            #here we will extracted aouthors from news article
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



            if author==[]:
                author=" "


            return render(
                    request,
                "data.html",
                {"title":title,
                 "summary":summmary,
                "text":text,
                 "author":author[0],
                 "keyword":keywords[0:int(keywords_number)],
                 "number":keywords_number,
                "publish_date":date,
                 "url":url,}
                )
        except:
            return HttpResponse("please enter valid url")


    return render(request,"newsscraper.html",
                  )

def handler404( request,
               exception
               ):

    return redirect("home")

def handler500(request,
               ):
    return redirect("home")

