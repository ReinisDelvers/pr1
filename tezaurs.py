# ''' Scraper.
# '''

# import re
# from urllib.parse import urljoin, urlsplit, SplitResult
# import requests
# from bs4 import BeautifulSoup


# class RecursiveScraper:
#     ''' Scrape URLs in a recursive manner. '''
#     def __init__(self, url, output_file="tezaurslinks.txt"):
#         ''' Constructor to initialize domain name, main URL, and output file.'''
#         self.domain = urlsplit(url).netloc
#         self.mainurl = url
#         self.urls = set()
#         self.output_file = output_file  # Set the output file
#         self.counter = 1  # Initialize counter for printing

#     def preprocess_url(self, referrer, url):
#         ''' Clean and filter URLs before scraping.'''
#         if not url:
#             return None

#         fields = urlsplit(urljoin(referrer, url))._asdict()  # Convert to absolute URLs and split
#         fields['path'] = re.sub(r'/$', '', fields['path'])  # Remove trailing /
#         fields['fragment'] = ''  # Remove targets within a page
#         fields = SplitResult(**fields)
#         if fields.netloc == self.domain:
#             # Scrape pages of current domain only
#             if fields.scheme == 'http':
#                 httpurl = cleanurl = fields.geturl()
#                 httpsurl = httpurl.replace('http:', 'https:', 1)
#             else:
#                 httpsurl = cleanurl = fields.geturl()
#                 httpurl = httpsurl.replace('https:', 'http:', 1)
#             if httpurl not in self.urls and httpsurl not in self.urls:
#                 # Return URL only if it's not already in list
#                 return cleanurl

#         return None

#     def scrape(self, url=None):
#         ''' Scrape the URL and its outward links in a depth-first order.
#             If URL argument is None, start from main page.
#         '''
#         if url is None:
#             url = self.mainurl

#         self.urls.add(url)
#         response = requests.get(url)
        
#         # Ensure proper encoding for Latvian characters
#         response.encoding = 'utf-8'  # Explicitly set encoding
        
#         soup = BeautifulSoup(response.content, 'lxml')
#         for link in soup.findAll("a"):
#             childurl = self.preprocess_url(url, link.get("href"))
#             if childurl:
#                 print(f"{self.counter}. {childurl}")  # Print the counter and URL
#                 self.counter += 1  # Increment the counter
#                 self.scrape(childurl)

#         # Save all found URLs to the output file after scraping
#         self.save_urls()

#     def save_urls(self):
#         ''' Save all collected URLs into the output file.'''
#         with open(self.output_file, 'w', encoding='utf-8') as file:
#             for url in self.urls:
#                 file.write(url + '\n')  # Write each URL on a new line


# if __name__ == '__main__':
#     rscraper = RecursiveScraper("https://tezaurs.lv/")
#     rscraper.scrape()






''' Scraper.
'''

import re
from urllib.parse import urljoin, urlsplit, SplitResult
import requests
from bs4 import BeautifulSoup


class RecursiveScraper:
    ''' Scrape URLs in a recursive manner.
    '''
    def __init__(self, url):
        ''' Constructor to initialize domain name and main URL.
        '''
        self.domain = urlsplit(url).netloc
        self.mainurl = url
        self.urls = set()

    def preprocess_url(self, referrer, url):
        ''' Clean and filter URLs before scraping.
        '''
        if not url:
            return None

        fields = urlsplit(urljoin(referrer, url))._asdict() # convert to absolute URLs and split
        fields['path'] = re.sub(r'/$', '', fields['path']) # remove trailing /
        fields['fragment'] = '' # remove targets within a page
        fields = SplitResult(**fields)
        if fields.netloc == self.domain:
            # Scrape pages of current domain only
            if fields.scheme == 'http':
                httpurl = cleanurl = fields.geturl()
                httpsurl = httpurl.replace('http:', 'https:', 1)
            else:
                httpsurl = cleanurl = fields.geturl()
                httpurl = httpsurl.replace('https:', 'http:', 1)
            if httpurl not in self.urls and httpsurl not in self.urls:
                # Return URL only if it's not already in list
                return cleanurl

        return None

    def scrape(self, url=None):
        ''' Scrape the URL and its outward links in a depth-first order.
            If URL argument is None, start from main page.
        '''
        if url is None:
            url = self.mainurl

        print("Scraping {:s} ...".format(url))
        self.urls.add(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')
        for link in soup.findAll("a"):
            childurl = self.preprocess_url(url, link.get("href"))
            if childurl:
                self.scrape(childurl)


if __name__ == '__main__':
    rscraper = RecursiveScraper("http://bbc.com")
    rscraper.scrape()
    print(rscraper.urls)