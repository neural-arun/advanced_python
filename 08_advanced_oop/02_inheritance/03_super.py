class Scraper:
    def fetch(self):
        print("Fetching data from website.")

class PhysicsScraper(Scraper):
    def parse(self):
        print("Parsing physics question.")
    def fetch(self):
        super().fetch()
        print("Fetching physics questions.")

s = PhysicsScraper()
s.fetch()
# Fetching data from website.
# Fetching physics questions.  
# ab ye dono aayenge.