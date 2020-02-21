def getCarouselImageURL(n=2):
    url = []
    baseURL = "/static/Images/Carousel/"
    endURL = ".jpg"
    for i in range(1,n+1):
        url.append(baseURL + str(i) + endURL)
    return url
