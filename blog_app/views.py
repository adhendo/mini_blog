import requests
from selenium import webdriver
import time
from pytrends.request import TrendReq
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from . import models
from .models import TwitterHeadline, RedditHeadline, YoutubeHeadline, GoogleTrends
from django.views.generic import TemplateView

# Create your views here.
BASE_URL = ''
pytrends = TrendReq(hl='en-US', tz=360)

def scrapeGoogle(request):
    df = pytrends.trending_searches(pn='united_states')
    results = df.to_string(index=False)

    df_2 = pytrends.today_searches(pn='US')
    results_2 = df_2.to_string(index=False)

    for result in results, results_2:
        new_headline = GoogleTrends()
        new_headline.trends = results
        new_headline.realtimetrends = results_2
        new_headline.save(force_insert=False, force_update=False)
    return redirect("../")

    #print(results)





class HomePageView(TemplateView):
    template_name = 'blog_app/news.html'

def like_post(request):
    post = get_objet_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False
    if post.like.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(post.get_absolute_url())

def profile_search(request):
    return render(request, 'blog_app/profile_search.html')

def news_list(request):
    is_liked = False
    headlines_twitter = TwitterHeadline.objects.all()[::-1][:15]
    headlines_reddit = RedditHeadline.objects.all()[::-1][:15]
    headlines_youtube = YoutubeHeadline.objects.all()[::-1][:15]
    trends_google = GoogleTrends.objects.all()[::-1][:1]
    #if headlines_youtube.likes.filter(id=request.user.id).exists(): is_liked = True
    context = {
        'twitter_list': headlines_twitter,
        'reddit_list': headlines_reddit,
        'youtube_list': headlines_youtube,
        'trends_google': trends_google,
        'is_liked': is_liked,
    }
    return render(request, "blog_app/news.html", context)

def scrapeYoutube(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://www.youtube.com/feed/trending?bp=4gIuCggvbS8wNWpoZxIiUEwzWlE1Q3BOdWxRbUtPUDNJekdsYWN0V1c4dklYX0hFUA%3D%3D"
    content = session.get(url, verify=True).content
    soup = BSoup(content, "html.parser")

    youtubefeed = soup.find_all('a', {"class": "yt-uix-tile-link"})
    thumbnail = soup.find_all('a', {"class": "ytd-thumbnail"})
    # youtubechannel = soup.find_all('a',{"class":"yt-uix-sessionlink"})
    youtubemeta = soup.find_all('ul',{"class":"yt-lockup-meta-info"})

    # print(soup)

    for item in youtubemeta:
        metadataInfo = set(li.text for li in item.find_all('li'))
        # print(metadataInfo)
        info = [elem.strip("{''}") for elem in metadataInfo]
        final_meta = ' '.join(map(str, info))
        print(final_meta)
        new_headline = YoutubeHeadline()
        new_headline.youtube_metadata = final_meta

    for item in thumbnail:
        link = item['href']
        new_headline = YoutubeHeadline()
        new_headline.youtube_thumbnailUrl = link

    for thing in youtubefeed:
        link = thing['href']
        title = thing['title']
        final_link = str("https://youtube.com" + link)
        # info =  thing.find_all('ul', {"class": "yt-lockup-meta-info"})
        new_headline = YoutubeHeadline()
        new_headline.youtube_title = title
        new_headline.youtube_url = final_link
        # new_headline.youtube_info = info
        new_headline.save(force_insert=False, force_update=False)
    return redirect("../")

def scrapeReddit(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = "https://old.reddit.com/user/Adhendo/m/news/"
    content = session.get(url, verify=True).content
    soup = BSoup(content, "html.parser")

    redditfeed = soup.find_all('div', {"class": "top-matter"})
    thumbnail = soup.find_all('div', {"class": "thing"})

    for item in thumbnail:
        main = item.find_all('a', {"class": "thumbnail"})[0]
        link = main['href']
        new_headline = RedditHeadline()
        new_headline.reddit_thumbnailUrl = link

    for item in redditfeed:
        main = item.find_all('a')[0]
        link = main['href']
        title = set(p.text for p in item.find_all('p', {"class": "title"}))
        titletitle = [elem.strip("{''}") for elem in title]
        final_title = ' '.join(map(str, titletitle))

        tagline = set(time.text for time in item.find_all('time', {"class": "live-timestamp"}))
        tagtag = [elem.strip("{''}") for elem in tagline]
        final_tag = ' '.join(map(str, tagtag))

        new_headline = RedditHeadline()
        new_headline.reddit_title = final_title
        new_headline.reddit_url = link
        new_headline.reddit_tag = final_tag

        new_headline.save(force_insert=False, force_update=False)
    return redirect("../")

def scrapeTwitter(request):
    session = requests.Session()
    session.headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15"}
    url = "https://twitter.com/explore"
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(30)
    results = driver.find_elements_by_xpath()
    data = []

    for result in results:
        new_headline = TwitterHeadline()
        new_headline.title = title
        new_headline.url = link
        new_headline.image = final_image
        new_headline.tag = final_tag
        new_headline.time = final_time
        new_headline.save(force_insert=False, force_update=False)
    return redirect("../")


def scrape(request):
  session = requests.Session()
  session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
  urls = ["https://twitter.com/explore", "https://old.reddit.com/user/Adhendo/m/news/", "https://www.youtube.com/feed/trending?bp=4gIuCggvbS8wNWpoZxIiUEwzWlE1Q3BOdWxRbUtPUDNJekdsYWN0V1c4dklYX0hFUA%3D%3D"]
  for url in urls:
      content = session.get(url, verify=True).content
      soup = BSoup(content, "html.parser")

      youtubefeed = soup.find_all('a',  {"class": "yt-uix-tile-link"})

      for thing in youtubefeed:
          link = thing['href']
          title = thing['title']
          final_link = str("https://youtube.com" + link)

          # info =  thing.find_all('ul', {"class": "yt-lockup-meta-info"})


          new_headline = YoutubeHeadline()
          new_headline.youtube_title = title
          new_headline.youtube_url = final_link
          # new_headline.youtube_info = info
          new_headline.save(force_insert=False, force_update=False)

      redditfeed = soup.find_all('div', {"class": "top-matter"})

      for item in redditfeed:
          main = item.find_all('a')[0]
          link = main['href']
          title = set(p.text for p in item.find_all('p', {"class": "title"}))
          titletitle = [elem.strip("{''}") for elem in title]
          final_title = ' '.join(map(str, titletitle))

          tagline = set(time.text for time in item.find_all('time', {"class": "live-timestamp"}))
          tagtag = [elem.strip("{''}") for elem in tagline]
          final_tag = ' '.join(map(str, tagtag))

          new_headline = RedditHeadline()
          new_headline.reddit_title = final_title
          new_headline.reddit_url = link
          new_headline.reddit_tag = final_tag

          new_headline.save(force_insert=False, force_update=False)


      news = soup.find_all('div', {"class": "MomentCapsuleSummary"})
      # print (news)

      for article in news:
        main = article.find_all('a')[0]
        link = main['href']

        main2 = article.find_all('a')[1]

        image_src = set(img['src'] for img in article.find_all('img', {"class": "MomentMediaItem-entity"}) if img.has_attr('src'))
        image = [elem.strip("{''}") for elem in image_src]
        final_image = ' '.join(map(str, image))

        tag = set(span.text for span in article.find_all('span', {"class":"MomentCapsuleSubtitle-category"}))
        tagtag = [elem.strip("{''}").strip() for elem in tag]
        final_tag = ' '.join(map(str, tagtag))

        time = set(span.text for span in article.find_all('span', {"class":"MomentCapsuleSubtitle-context"}))
        timetime = [elem.strip("{''}").strip() for elem in time]
        final_time = ' '.join(map(str, timetime))

        title = main2['title']

        new_headline = TwitterHeadline()
        new_headline.title = title
        new_headline.url = link
        new_headline.image = final_image
        new_headline.tag = final_tag
        new_headline.time = final_time

        new_headline.save(force_insert=False, force_update=False)

  return redirect("../")

def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    # print(quote_plus(search))
    final_url = BASE_URL.format(search)

    response = requests.get(final_url)
    data = response.text

    soup = BSoup(data, features='html.parser')

    analytics = soup.select_one("meta[property='og:description']")

    name = analytics.find_previous_sibling().get("content").split("•")[0]
    followers = analytics.get("content").split(", ")[0]
    following = analytics.get("content").split(", ")[1]
    #posts = for thousands in posts : analytics.get("content").split(",")[3]

    avatar = soup.findAll('img', {'class': 'be6sR'})
    for image in avatar:
        print(image['src'])

    #number_of_posts = analytics.text[0]

    #number_of_followers = analytics.text[1]

    #number_following = analytics.text[2]

    # post_img = post_listings.()

    print(analytics, f'{name}\n{followers}\n{following}\n{avatar}')

    # print(data)
    stuff_for_frontend = {
        'search': search,
        'name': name,
        'followers': followers,
        'following': following,
        #'posts': posts,
        'final_url': final_url,
        'avatar': avatar
    }
    return render(request, 'blog_app/new_search.html', stuff_for_frontend)