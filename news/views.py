from django.shortcuts import render,HttpResponse,redirect
import newspaper
from wordcloud import WordCloud,STOPWORDS
from newspaper import Article
import nltk
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
        keywords_number=request.POST.get("quantity")
        print(name,keywords_number)
        article = Article(name)

        if True:
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
            nouns=[]


            nlp = spacy.load("en_core_web_sm")
            doc = nlp(summmary)


        #
        # for np in doc.noun_chunks:
        #     nouns.append(np.text)







            if author==[]:
                author=" "


            return render(
                    request,
                "New folder/index2.html",
                {"title":title,"summary":summmary,
                "text":text,
                 "author":author[0],
                 "keyword":keywords[0:int(keywords_number)],"number":keywords_number,
                "publish_date":date,"url":url,"nouns":nouns}
                )
        # except:
        #     return HttpResponse("plz enter valid url")


    return render(request,"newsscraper.html",
                  )

def handler404( request,
               exception
               ):

    return redirect("home")

def handler500(request,
               ):
    return redirect("home")

def demo(request,link):
    return redirect(link)