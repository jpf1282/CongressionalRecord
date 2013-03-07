from datetime import date
from dateutil.rrule import rrule, DAILY
import scraper
import parser

a = date(2013, 3, 4)
b = date(2013, 3, 5)

if __name__ == '__main__':
	for dt in rrule(DAILY, dtstart=a, until=b):
    		current_date = dt.strftime("%Y/%m/%d")
		print 'Scraping ' + current_date
		scraper.main(dt.strftime("%d/%m/%Y"))
		print 'Parsing ' + current_date
		parser.main(dt.strftime("%Y/%m/%d"))
