# Child parent ke method ko override kar sakta hai.

class Scraper:
    def fetch(self):
        print("Fetching data from website.")

class PhysicsScraper(Scraper):
    def parse(self):
        print("Parsing physics question.")
    def fetch(self):
        print("Fetching physics questions.")

s = PhysicsScraper()
s.fetch()   # PhysicsScraper wala method chalega parent ka nhi.
# Fetching physics questions.