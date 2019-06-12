
import csv
import getopt
import os, os.path
import sys


from LinkScraper import LinkScraper


# Application handling class
class MainApp:

    def __init__(self):
        self.scraper = LinkScraper(self)

        self.urls = list()

        self.fileUpdated = False

    def main(self):

        # Selecting options (help) with u
        try:
            opts, args = getopt.getopt(
                sys.argv[1:],
                "hf:u:l",
                ["help", "url=","link"]
            )
        except getopt.GetoptError as err:
            # print help information and exit:
            print(err)  # prints "option -a not recognized" if any error
            self.usage()
            sys.exit(2)

        # Process args
        for o, a in opts:
            if o in ("-h", "--help"):
                self.usage()
                sys.exit()

            elif o in ("-u", "--url"):
                self.urls.append(a)
                self.scraper = LinkScraper(callback=self.write_csv)

        # Run
        self.scraper.add_page_list(self.urls)
        self.scraper.run()

    # Display help message
    def usage(self):
        print("Options:")
        print("help: -h, --help")
        print("scrape a url: -u, --url <your URL here>")
        pass

    # Write output into file
    def write_csv(self, _results):
        if not self.fileUpdated:
            self.fileUpdated = True

            fh = open("Results.csv", "w")
            fh.write('\n'.join(sorted(_results)) + '\n')
            fh.close()

            print("Result written!")

            os.startfile("Results.csv")

# Run application from self

if __name__ == '__main__':
    _app = MainApp()
    _app.main()
