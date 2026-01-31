class Scraper:
    def fetch(self):
        print("Fetching generic data.")
    
class PhysicsScraper(Scraper):
    def fetch(self):
        print("Fetching Physics data.")
    
class BioScraper(Scraper):
    def fetch(self):
        print("Fetching Biology data.")

class ChemScraper(Scraper):
    def fetch(self):
        print("Fetching Chemistry data.")


scrapers = [PhysicsScraper() , BioScraper(), ChemScraper()]

for s in scrapers:
    s.fetch()

"""
loop same 
method name same
behaviour different
"""