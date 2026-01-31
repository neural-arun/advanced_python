# class Parent:
#     pass

# class Child(Parent):
#     pass


# another example:

class Scraper:
    def fetch(self):
        print("Fetching data from website.")

class PhysicsScraper(Scraper):
    def parse(self):
        print("Parsing physics question.")
    

s = PhysicsScraper()
s.fetch()       # Parent ka
s.parse()       # child ka