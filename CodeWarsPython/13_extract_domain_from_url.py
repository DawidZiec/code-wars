'''
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
'''

def domain_name(url):
    if url[0:4]=='http' or url[0:3]=='www':
        if 'https://www.' in url:
            name_first = url[12:]
            storage = []
            storage.append(name_first.split('.'))
            return (storage[0][0])
        elif 'http://www.' in url:
            name_first = url[11:]
            storage = []
            storage.append(name_first.split('.'))
            return (storage[0][0])
        elif 'https://' in url:
            name_first = url[8:]
            storage = []
            storage.append(name_first.split('.'))
            return(storage[0][0])
        elif 'http://' in url:
            name_first = url[7:]
            storage = []
            storage.append(name_first.split('.'))
            return (storage[0][0])
        elif 'www' in url:
            name_first = url[4:]
            storage = []
            storage.append(name_first.split('.'))
            return (storage[0][0])
    else:
        storage = []
        storage.append(url.split('.'))
        return (storage[0][0])


print(domain_name('https://gry-online.pl/sdjhf.lasdj.askdfj'))