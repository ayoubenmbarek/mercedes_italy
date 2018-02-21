import scrapy
from mercedes.items import MercedesItem
from scrapy import Request
from scrapy.http import FormRequest
import json
from scrapy_splash import SplashRequest
import requests
import ast
import re


class mercedesSpider(scrapy.Spider):
    name =  "mercedes_italy24-01-2" #"mercedes_italy_deatil_page26-01"#mercedes_italy25-01-firstcache(old)
    #allowed_domains = ["usato.firsthand.it/"]
   #start_urls = ["http://usato.firsthand.it/"]
    start_urls = [l.strip() for l in open('/home/databiz41/scrapy_projects/mercedes/mercedes/links_only_dealers.csv').readlines()] #old links2.csv
    download_delay = 0
    page_incr = 1
    pagination_url = 'http://usato.firsthand.it/xhr/request-parser.php' 
    #preload jquery
    #def script(n):
    script = """
            function main(splash, args)
                assert(splash:autoload("https://code.jquery.com/jquery-2.1.3.min.js"))
                assert(splash:go(splash.args.url))
                local version = splash:evaljs("$.fn.jquery")
                return 'JQuery version: ' .. version
            end
        """
     #   return _script


    script_title = """
        function main(splash)
            assert(splash:go(splash.args.url))
            splash:wait(0.5)
            local title = splash:evaljs("document.title")
            return {title=title}
        end

    """

#    def start_requests(self):
 #       headers = {#'Origin':'http://usato.firsthand.it',
  #                  'Accept-Encoding':'gzip, deflate',
   #                 'Accept-Language':'fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4',
    #                'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
     ##               'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
          #          'Accept':'application/json, text/javascript, */*; q=0.01',
       #             'Referer':'http://usato.firsthand.it/',
        #            'X-Requested-With':'XMLHttpRequest',
         #           'Connection':'keep-alive',
                #    'CooKie':'cookie_got_it=true; query_data_url=http%3A%2F%2Fusato.firsthand.it%2Fricerca%2Fconcessionario%3Atutti%2Fmodello%3Atutti%2Fanni%3Atutti%2Falimentazione%3Atutte%2Fcambio%3Atutti%2Fcolori%3Atutti%2Fchilometri%3Atutti%2Fprezzo%3Atutti%2Fgaranzia%3Atutte%2Foptional%3Atutti%2Fordina-per%3Aprezzo%2Fdistanza%3Acap%2Bmax%2F; _back_from_search=null; _ga=GA1.2.269070102.1516786361; _gid=GA1.2.1846954450.1516786361; query_data=%7B%22action%22%3A%22getPage%22%2C%22brand%22%3A%22MERCEDES%22%2C%22dealer%22%3A%22all%22%2C%22carline%22%3A%22all%22%2C%22warranty%22%3A%22all%22%2C%22priceStart%22%3A100%2C%22priceEnd%22%3A15400000%2C%22kmStart%22%3A%220%22%2C%22kmEnd%22%3A%22159867%22%2C%22yearStart%22%3A%222012%22%2C%22yearEnd%22%3A%222017%22%2C%22fuel%22%3A%22all%22%2C%22optionals%22%3A%22all%22%2C%22gearbox%22%3A%22all%22%2C%22color%22%3A%22all%22%2C%22cap%22%3A%22%22%2C%22lat%22%3A%22%22%2C%22lon%22%3A%22%22%2C%22distance%22%3A%22-1%22%2C%22isFiera%22%3A%22false%22%2C%22specialOffer%22%3A%22false%22%2C%22specials24Offer%22%3A%22false%22%2C%22page%22%3A%2213%22%2C%22sortBy%22%3A%22price%22%2C%22carsPerPage%22%3A%226%22%2C%22special_query%22%3A%22%22%7D',
                 #   '--data':'action=getPage&brand=MERCEDES&dealer=all&carline=all&warranty=all&priceStart=100&priceEnd=15400000&kmStart=0&kmEnd=159867&yearStart=2012&yearEnd=2017&fuel=all&optionals=all&gearbox=all&color=all&cap=&lat=&lon=&distance=-1&isFiera=false&specialOffer=false&specials24Offer=false&page=2&sortBy=price&carsPerPage=6&special_query=',
                  #  '--compressed':'',
                    #'':'',
                    #'':'',
                   # 'Host':'usato.firsthand.it',
            #        'Content-Length':'326',
           #         }
        #for i in range(4,6):#try with splashRequest and autoload jquery
        #post_urls = ['http://usato.firsthand.it/wp-content/themes/firsthand/js/search.js?ver=4.8.5', 'http://usato.firsthand.it/wp-includes/js/jquery/jquery.js?ver=1.12.4']
        #for u in post_urls:
        #    responsee = responsee = requests.post(u)
        #self.page_incr +=1
        #for i in range(1,230):

         #   formdata = {'action':'getPage','brand':'MERCEDES','dealer':'all','carline':'all',
          #          'warranty':'all','priceStart':'100','priceEnd':'15400000','kmStart':'0',
           #         'kmEnd':'159867','yearStart':'2012','yearEnd':'2017','fuel':'all',
            #        'optionals':'all','gearbox':'all','color':'all','cap':'',
             #       'lat':'','lon':'','distance':'-1','isFiera':'false','specialOffer':'false','specials24Offer':'false', 'page':str(i),
              #      'sortBy':'price','carsPerPage':'6','special_query':'all'
               # }
           # formdata = {'page':str(i), 'action':'getPage','brand':'MERCEDES','dealer':'all','carline':'all','warranty':'all','priceStart':'100','priceEnd':'15400000','kmStart':'0','kmEnd':'159867','yearStart':'2012','yearEnd':'2017','fuel':'all','optionals':'all','gearbox':'all','color':'all',}
        #    url2 = "http://usato.firsthand.it/xhr/request-parser.php"
           # url1 = "http://usato.firsthand.it"
            #url = 'https://code.jquery.com/jquery-1.5.1.min.js'
        #url = "http://usato.firsthand.it/wp-content/themes/firsthand/js/search.js?ver=4.8.5"
        #responsee = requests.post(url)#, data=formdata)#, headers=request_headers)
           # yield FormRequest(url=self.pagination_url, formdata= formdata #{'Content-Type':'application/json'}
            #                     , callback=self.parse)#, meta={
        #    yield SplashRequest(url1, self.parse_phone,
         #                        endpoint="execute",
          #                      # 'lua_source':self.script_title
           #                      #endpoint='render.html',
            #                     args={#'js_source': 'document.title="My Title";',
             #                          'lua_source':self.script_title,
              #                         'autoload':"https://code.jquery.com/jquery-2.1.3.min.js" }
#
 #                           #     args={"lua_source": self.script}
  #                          )
               # 'dont_merge_cookies': True,
               # 'splash': {
                    
                #    'autoload': 'https://code.jquery.com/jquery-1.5.1.min.js',}
                    #})
    def start_requests(self):

        for url in self.start_urls:
            urls = url.split("'")
            links = urls[0]
            yield scrapy.Request(links, callback=self.parse)



    def parse(self, response):
                #data = json.loads(response.body)
                #data  = json.loads('/home/databiz41/scrapy_projects/mercedes/mercedes/save_all_cars_info.json')
           # for info in data.get('results',[]).get('list',[]).get('paged',[]).get('cars',[]):#get url from json first
            #for i in range(1,1369):

           # for info in data.get('results').get('list').get('paged').get('cars'):

                myItem = MercedesItem()
                myItem['ANNONCE_LINK'] = response.url#data.get('ANNONCE_LINK') DEALER_URL to annonce_link
                cc = response.xpath('//div[@class="col-content"]/p[2]/text()').extract_first()
                bb = cc.split(':')
                myItem['TELEPHONE'] = bb[-1]  # dealer_phone to TELEPHONE
               # myItem['ADRESSE'] =  response.xpath('//div[@class="col-content"]/p[1]/text()').extract_first()# old
                myItem['ADRESSE'] =  re.search(r'streetAddress": "(.*?)"', response.body ).group(1)
                #myItem['DEPARTEMENT'] = re.search(r'addressRegion": "(.*?)"', response.body ).group(1) #was prvince_changed09-20
                myItem['PROVINCE'] = " "#  re.search(r'addressRegion": "(.*?)"', response.body ).group(1)
                myItem['VILLE'] =  re.search(r'"addressLocality": "(.*?)"', response.body ).group(1)#was VILLE changed09-20 
                #myItem['DEPARTEMENT'] = locality +' '+ '('+myItem['PROVINCE']+')'
                myItem['DEPARTEMENT'] = re.search(r'addressRegion": "(.*?)"', response.body ).group(1)
                ville = myItem['ADRESSE'].split(',')
                #myItem['VILLE'] = ville[0] #clean ville after crawling
                myItem['PUISSANCE'] = response.xpath('//ul[@class="last"]/li[1]/span/text()').extract_first() 
                myItem['GARAGE_NAME'] = response.xpath('//div[@class="col-full feedback map"]/div/h1/text()').extract() #change dealer_name to garage_name
                #href_dealer = myItem['DEALER_URL']
                #half_url = href_dealer.split('auto/')
                #vv = half_url[-1]
                #hh = vv.split('/')
                #myItem['DEALER_ID']= hh[0]
                myItem['FROM_SITE'] = 'http://usato.firsthand.it'
                myItem['LONGITUDE'] = re.search(r'var lon = (.*?);', response.body).group(1)
                myItem['LATITUDE'] = re.search(r'var lat = (.*?);', response.body).group(1)
                myItem['EMAIL'] = response.xpath('//input[@id="dealer_email"]/@value').extract() #from/auto change DEALER_EMAIL to email
                myItem['GARAGE_ID'] = response.xpath('//input[@id="dealer_code"]/@value').extract()    #from/auto #change dealer_id to GARAGE_ID
                #myItem['NUMBER_OF_CARS'] = response.xpath('//span[@class="brandTotal"]/text()').extract() #from concessionare page
                page_detail = response.xpath('//a[@class="link right"]/@href').extract_first()
                #myItem['ANNONCE_LINK'] = page_detail 


                myItem['CARROSSERIE']  = response.xpath('//ul[@class="first"]/li[4]/span/text()').extract_first()
                immatriculazione =  response.xpath('//ul[@class="first"]/li[1]/span/text()').extract_first()
                mm = response.xpath('//*[@class="flexslider"]/ul/li').extract()
                myItem['PHOTO'] = len(mm)
                immatriculazione1 = immatriculazione.split('/')
                myItem['ANNEE'] = immatriculazione1[-1]
                myItem['MOIS'] = immatriculazione1[0]
                myItem['MINISITE'] = response.xpath('//a[@class="link right"]/@href').extract()
                myItem['NOM'] = response.xpath('//div[@class="col-lg-8"]/h1/text()').extract()
                myItem['OPTIONS'] = response.xpath('//meta[@property="og:description"]/@content').extract()
                url = response.url
                url2 = url.split('/')
                myItem['ID_CLIENT'] = url2[4]
                myItem['CARBURANT'] = response.xpath('//li[@class="last"]/span/text()').extract_first()
                myItem['CYLINDRE'] = response.xpath('//ul[@class="first"]/li[3]/span/text()').extract_first()
                myItem['KM'] = response.xpath('//div[@class="col-lg-12 col-md-12 col-sm-6 col-xs-6"]/li[2]/p/span/text()').extract()
                myItem['PRIX'] = response.xpath('//li[@id="bloccoPrezzo"]/p/span/text()').extract_first()
                myItem['COULEUR'] = response.xpath('//ul[@class="last"]/li[2]/span/text()').extract_first()
                myItem['BOITE'] = response.xpath('//ul[@class="last"]/li[4]/span/text()').extract_first()
                #myItem['DATE_ENREGISTREMENT']


                
                #request = scrapy.Request(url=page_detail)#, callback=self.parse_phone) #try it to get number of cars
                #request.meta["myItem"] = myItem
                yield myItem

                #myItem['ANNONCE_LINK'] = data.get('results',{}).get('list',{}).get('paged',{}).get('cars')#.get('brand')#.get('name')#.get('id')#[i]#.get('cars')[i]
               # myItem['ANNONCE_LINK'] = data
                #myItem['DEALER_URL'] =  info['dealer_link']
                #cc = info.get('list').get('paged').get('cars')
                #bb = ast.literal_eval(cc)
                #myItem['ANNONCE_LINK'] = info
                # myItem['DEALER_ID'] =  info.get('id')
                ##myItem['DEALER_ID'] =  info.get('dealer')
                ##myItem['DEALER_NAME'] =  info.get('dealer_name')
               # myItem['SLUG'] =  info.get('slug')
               # myItem['LATITUDE'] =  info.get('lat')
               # myItem['LONGITUDE'] =  info.get('lon')
               # myItem['ADRESSE'] =  info.get('address')
              #  myItem['NUMBER_OF_CARS'] =  info.get('cars_count')
               # myItem['FROM_SITE'] = 'http://usato.firsthand.it'
                #request = scrapy.Request(url=myItem['ANNONCE_LINK'], callback=self.parse_phone)
                #request = scrapy.Request(myItem['DEALER_URL'], callback=self.parse_phone)
                #request.meta["myItem"] = myItem
                #yield myItem

    def parse_phone(self, response):
        myItem = response.meta['myItem']
        myItem['NUMBER_OF_CARS'] = response.xpath('//span[@class="brandTotal"]/text()').extract() #from concessionare page




        yield myItem

