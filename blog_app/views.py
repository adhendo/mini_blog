import requests
from requests.compat import quote_plus
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from . import models
from .models import TwitterHeadline, RedditHeadline, YoutubeHeadline

BASE_URL = 'https://www.instagram.com/{}'
url = 'https://www.instagram.com/explore/locations/US/united-states/'

# Create your views here.


def profile_search(request):
    return render(request, 'blog_app/profile_search.html')

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
          new_headline.save(force_insert=False)

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

          new_headline.save(force_insert=False)


      news = soup.find_all('div', {"class": "MomentCapsuleSummary"})
      print (news)

      for article in news:
        main = article.find_all('a')[1]
        link = main['href']

        image_src = set(img['src'] for img in article.find_all('img', {"class": "MomentMediaItem-entity--image"}) if img.has_attr('src'))
        image = [elem.strip("{''}") for elem in image_src]
        final_image = ' '.join(map(str, image))

        tag = set(span.text for span in article.find_all('span', {"class":"MomentCapsuleSubtitle-category"}))
        tagtag = [elem.strip("{''}").strip() for elem in tag]
        final_tag = ' '.join(map(str, tagtag))

        time = set(span.text for span in article.find_all('span', {"class":"MomentCapsuleSubtitle-context"}))
        timetime = [elem.strip("{''}").strip() for elem in time]
        final_time = ' '.join(map(str, timetime))

        title = main['title']

        new_headline = TwitterHeadline()
        new_headline.title = title
        new_headline.url = link
        new_headline.image = final_image
        new_headline.tag = final_tag
        new_headline.time = final_time
        new_headline.save(force_insert=False,)
  return redirect("../")

def news_list(request):
    headlines_twitter = TwitterHeadline.objects.all()[::-1][:10]
    headlines_reddit = RedditHeadline.objects.all()[::-1][:10]
    headlines_youtube = YoutubeHeadline.objects.all()[::-1][:10]
    context = {
        'twitter_list': headlines_twitter,
        'reddit_list': headlines_reddit,
        'youtube_list': headlines_youtube
    }
    return render(request, "base.html", context)

def location_getter(request):
    response = requests.get(url)
    data = response.text
    soup = BSoup(data, features='html.parser')

    location_listings = soup.find_all('li', {'class': 'kiTXG'})


    for location in location_listings:
        location_title = location.find(class_='aMwHK').text
        location_url = location.find('a').get('href')

        final_locations = (location_title, location_url)

    print(final_locations)

    stuff_for_frontend = {
        'final_locations': final_locations
    }

    return render(request, 'blog_app/locations.html', stuff_for_frontend)

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