from django.shortcuts import render,HttpResponse,redirect
import newspaper
from newspaper import Article
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

            keywords = article.keywords
            print(type(keywords))
            summmary = article.summary
            print(summmary,keywords)
            author = article.authors
            if author==[]:
                author=" "


            return render(
                request,
                "data.html",
                {"summary":summmary,
                 "author":author[0],
                 "keyword":keywords},
            )

        except:
            return HttpResponse(f"{name}{article}please enter valid url")

    return render(request,
                  "newsscraper.html",
                  )

def handler404( request,
               exception
               ):

    return redirect("home")

def handler500(request,
               ):
    return redirect("home")
