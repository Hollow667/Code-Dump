
import chilkat

spider = chilkat.CkSpider()

seenDomains = chilkat.CkStringArray()
seedUrls = chilkat.CkStringArray()

seenDomains.put_Unique(True)
seedUrls.put_Unique(True)

#  You will need to change the start URL to something else...
seedUrls.Append("http://something.whateverYouWant.com/")

#  Set outbound URL exclude patterns
#  URLs matching any of these patterns will not be added to the
#  collection of outbound links.
spider.AddAvoidOutboundLinkPattern("*?id=*")
spider.AddAvoidOutboundLinkPattern("*.mypages.*")
spider.AddAvoidOutboundLinkPattern("*.personal.*")
spider.AddAvoidOutboundLinkPattern("*.comcast.*")
spider.AddAvoidOutboundLinkPattern("*.aol.*")
spider.AddAvoidOutboundLinkPattern("*~*")

#  Use a cache so we don't have to re-fetch URLs previously fetched.
spider.put_CacheDir("c:/spiderCache/")
spider.put_FetchFromCache(True)
spider.put_UpdateCache(True)

while seedUrls.get_Count() > 0 :

    url = seedUrls.pop()
    spider.Initialize(url)

    #  Spider 5 URLs of this domain.
    #  but first, save the base domain in seenDomains
    domain = spider.getUrlDomain(url)
    seenDomains.Append(spider.getBaseDomain(domain))

    for i in range(0,5):
        success = spider.CrawlNext()
        if (success == True):

            #  Display the URL we just crawled.
            print(spider.lastUrl())

            #  If the last URL was retrieved from cache,
            #  we won't wait.  Otherwise we'll wait 1 second
            #  before fetching the next URL.
            if (spider.get_LastFromCache() != True):
                spider.SleepMs(1000)

        else:
            #  cause the loop to exit..
            i = 999

    #  Add the outbound links to seedUrls, except
    #  for the domains we've already seen.
    for i in range(0,spider.get_NumOutboundLinks()):

        url = spider.getOutboundLink(i)
        domain = spider.getUrlDomain(url)
        baseDomain = spider.getBaseDomain(domain)
        if (seenDomains.Contains(baseDomain) == False):
            #  Don't let our list of seedUrls grow too large.
            if (seedUrls.get_Count() < 1000):
                seedUrls.Append(url)
