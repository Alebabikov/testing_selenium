class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)


link = 'https://selenium-python.readthedocs.io/locating-elements.html'


