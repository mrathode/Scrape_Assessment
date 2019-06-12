import requests
from threading import Thread
from time import sleep


class Scraper(object):

    def __init__(self, callback):
        self.pages = list()
        self.visited_pages = set()
        self.results = set()

        self.maxThreads = 5
        self.activeThreads = 0

        self.callback = callback

        print("Starting...")

	# Check if there is atleast 1 link to scrape
    def can_run(self):

        if len(self.pages) > 0:
            return True

        else:
            print("Please add pages to scrape")
            return False

    # Starting new threads
    def start_threads(self):
        if len(self.pages) == 0:
            self.threads_complete()

        elif self.activeThreads >= self.maxThreads:
            sleep(1)
            self.start_threads()

        else:
            self.activeThreads += 1
            _url = self.pages.pop()

            print("Thread created (" + str(len(self.pages)) + " pages left) for url: " + _url)
            sleep(1)
            thread = Thread(target=self.run_threads, args=(_url,))
            thread.start()

            if self.activeThreads < self.maxThreads:
                self.start_threads()

    # Run new started thread
    def run_threads(self, _url):
        try:
            headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
            page = requests.get(_url,headers=headers, timeout=5)
            sleep(1)
            self.__find__(_url, page)
            self.visited_pages.add(_url)

        except:
            self.add_ (_url)

        self.activeThreads -= 1
        self.start_threads()

    # Default run method for thread
    def run(self):

        if self.can_run():
            self.start_threads()


    # Finish scraper if no more URLs are left in the 'pages' list
    def threads_complete(self):
        if len(self.pages) == 0 and self.activeThreads <= 0:
            self.callback(self.results)

        else:
            print(str(self.activeThreads) + " threads waiting")


    # Add a single page
    def add_page(self, url):
        if url not in self.pages and url not in self.visited_pages:
            print("Adding url: " + url)
            self.pages.append(url)

    # Add a list of pages
    def add_page_list(self, _list):
        for url in _list:
            self.add_page(url)

    # Add result
    def add_result(self, url):
        self.results.add(url)