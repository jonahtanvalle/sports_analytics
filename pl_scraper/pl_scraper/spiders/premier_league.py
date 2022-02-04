import scrapy


class PremierLeague(scrapy.Spider):
    name = 'plspider'
    start_urls = ['https://www.premierleague.com/match/66520/']

    def parse(self, response, **kwargs):
        """Método indispensable"""
        # print(response.status, response.headers)

        # Defining Xpath.
        score_xpath = "//*/section/div[3]/div/div/div[1]/div[2]/div/div/text()"
        home_team_xpath = "//*/section/div[3]/div/div/div[1]/div[1]/a[2]/span[1]/text()"
        visitor_team_xpath = "//*/section/div[3]/div/div/div[1]/div[3]/a[2]/span[1]/text()"
        date_xpath = "/html/body/main/div/section[2]/div[2]/section/div[1]/div/div[1]/div[1]/text()"

        # Getting response from web
        score = response.xpath(score_xpath).getall()
        home_team = response.xpath(home_team_xpath).get()
        visitor_team = response.xpath(visitor_team_xpath).get()
        date = response.xpath(date_xpath).extract()

        yield {
            'home': home_team,
            'score': score,
            'visitor': visitor_team,
            'date': date
        }
