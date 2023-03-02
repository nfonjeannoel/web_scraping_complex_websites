import json

import scrapy


class WalmartSpider(scrapy.Spider):
    name = "walmart"
    allowed_domains = ["walmart.ca"]
    start_urls = ["https://www.walmart.ca/browse/grocery/10019"]

    custom_settings = {
        "CONCURRENT_REQUESTS": 1,
        "DOWNLOAD_DELAY": 20,
    }

    headers = {
        'authority': 'www.walmart.ca',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': '_schn=_9lq9eo; deliveryCatchment=1061; walmart.nearestPostalCode=L5V2N6; walmart.shippingPostalCode=L5V2N6; defaultNearestStoreId=1061; headerType=grocery; vtc=fBheWwgHqVOQtJSWo1RKnE; walmart.nearestLatLng="43.60822,-79.69387"; userSegment=50-percent; pxcts=ecf900db-b470-11ed-96c9-4279576f5a51; _pxvid=ecf8f30f-b470-11ed-96c9-4279576f5a51; walmart.id=a27658af-d6a8-4e47-82a8-ce2a3170bc79; _cs_c=1; _gcl_au=1.1.1041739892.1677263263; __gads=ID=ad5d174027cceea2:T=1677263265:S=ALNI_MaJsG3zTwlnng97wqTt4xipmhg-8A; __gpi=UID=000009bc91e91e64:T=1677263265:RT=1677263265:S=ALNI_MZ-Jh1fL8UVkPCMo8nfRu3DnC1j7A; AMCVS_C4C6370453309C960A490D44%40AdobeOrg=1; cookiePolicy=true; _ga=GA1.2.1617201769.1677263264; _gid=GA1.2.1982486749.1677263265; s_ecid=MCMID%7C39737451839915523161183874674407954160; s_cc=true; kndctr_C4C6370453309C960A490D44_AdobeOrg_identity=CiYzOTczNzQ1MTgzOTkxNTUyMzE2MTE4Mzg3NDY3NDQwNzk1NDE2MFIPCNHFuaXoMBgBKgRJUkwx8AHRxbml6DA=; _4c_=%7B%22_4c_mc_%22%3A%22315ae22f-b8ef-477f-ba25-cae9065e0048%22%7D; _fbp=fb.1.1677263270524.162197248; _scid=cb1b7f2d-10b0-47b6-b7c7-6fc82cd16338; _pin_unauth=dWlkPU9UVXdaV1F5TkRJdFlXUTJZeTAwTlRjMkxUbGtOakl0TVRBd05UZG1PR1V3TURWaQ; _sctr=1|1677193200000; wmt.c=0; _uetsid=f47fd480b47011edbf441fdebf285653; _uetvid=f47fe810b47011ed91c4e5b582263f50; ENV=ak-eus-t1-prod; bstc=carZl4I6sj1dsYo5D6RsXQ; xpa=5sfML|9oiCx|CEJ49|HfmFY|KX9zf|MlWYt|OCh7V|OCyta|Qligk|RxMsL|S2NR7|Sek64|TKAa5|VKpZ3|ZIhUr|_r70T|hcJIR|ik-KQ|jE0bf|jxo4u|k1wRM|mVv6K|zKxNl; exp-ck=5sfML19oiCx2HfmFY1MlWYt1OCh7V1Qligk1RxMsL1S2NR72Sek642ZIhUr1_r70T1jxo4u1k1wRM1zKxNl1; xpm=1%2B1677270149%2BfBheWwgHqVOQtJSWo1RKnE~%2B0; kndctr_C4C6370453309C960A490D44_AdobeOrg_cluster=irl1; _cs_cvars=%7B%221%22%3A%5B%22appName%22%2C%22product-page%22%5D%7D; s_visit=1; localStoreInfo=eyJwb3N0YWxDb2RlIjoiTDVWMk42IiwibG9jYWxTdG9yZUlkIjoiMTA2MSIsInNlbGVjdGVkU3RvcmVJZCI6IjEwNjEiLCJjaXR5IjoiTWlzc2lzc2F1Z2EiLCJzZWxlY3RlZFN0b3JlTmFtZSI6IkhFQVJUTEFORCwgTUlTU0lTU0FVR0EsT04iLCJmdWxmaWxsbWVudFN0b3JlSWQiOiIxMDYxIiwiZnVsZmlsbG1lbnRUeXBlIjoiSU5TVE9SRV9QSUNLVVAifQ==; salsify_session_id=e99ef87b-53f3-4725-b257-6872e04385e9; BVBRANDID=0a312b3a-6372-4b39-949a-d84d0b0c1418; BVImplmain_site=2036; ak_bmsc=83BF6E38C99E3F1F95862078A9AA38C0~000000000000000000000000000000~YAAQR8ITAp1/WTKGAQAAI6EmhRLgXtRwNkAHbfjpcgBe3gYgxS7nd2t9IkSty5op8is0lWiMYWwtJLdnMRSnYQzgMow4q/sWAkgvYX18R+MAqYu0KDTHlvCNP6KOCGSyDiVkg4yzWoRI8veEDA1P6cEsSRlxKpsHdQA3GHBq+7B56dvW9OC5c8sWqW3yNxyHzn2GTdHPE08Y4crVKpNnIj81msDOPh8VXeHq4JREcV4z0WxczAdIaA7YGA6gmjoDQN8nA+R/azAhcw+BCGrJWu6P5mKPMDH879lvj4pZHikxUTTqaf7AfL0F24pD9f4g/lo2/kLFYNLnWg1hnUZCtxYy2FBtww4bpM1RLvYeyv72Qr/axTSHVJyhXS3gfNpCz7YzdczMAY65wEM=; s_sq=%5B%5BB%5D%5D; _cs_id=b2736357-e23e-aa63-c3f6-c4ad638df344.1677263262.4.1677271801.1677269377.1.1711427262840; _cs_s=5.0.0.1677273601621; cto_bundle=u_b9-180aXZraUQyOW0zbTJwM1lUYUJoQkU1MlNRemp6MFE3YlAlMkZwV0VrTm5pelVKamxzZXFFMWV2RU56TkYxVWFEeUo0cjRGUVliS0ZSSnJLZTdwdkpSSzdkNFpQZ1ZjSnA4ZTlBTGtRJTJCVlpxYTR4T1JCZU1vTHhBMVppdUU4aUxCSEE2WkJMUVpEbW0lMkZ6TzBkRVFBdzN2YmclM0QlM0Q; s_gnr=1677271802982-Repeat; gpv_Page=Product%3AOnion%2C%20Yellow%2C%20Your%20Fresh%20Market; AMCV_C4C6370453309C960A490D44%40AdobeOrg=-1124106680%7CMCIDTS%7C19413%7CMCMID%7C39737451839915523161183874674407954160%7CMCAAMLH-1677876604%7C6%7CMCAAMB-1677876604%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1677279004s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.2.0; bm_sv=E0EE905EFACDB73543192BFBE7C50D9A~YAAQR8ITAq+UWTKGAQAAOLowhRLjOBXGm24MK4lWZqGsIpdlnHghfdYbxQyZbLRYYle0oYAk8cdm7QMPbFvCjKQcGQp48bz5EiswtaI/4irhjF6DnDblZm0V67rheet2TPCErrEXag6E6XvbqKwOTeeVbo3s8vOeGpRHeeCgZ5EjGXDzW1mlAbbdaWFnhqv+8no5/vjLtlS2DPlhl1CHHH8ejlFC9sc9IxjuXUoFOBNpjiMaQKWmAzmzm+mtkVLn~1; seqnum=31; TS0196c61b=01cb3df500c326d97e014bddb349284e23afb49604548c2e49de9f16cb9807a75c4065286a1ca185992e0d8df471586f90905afeb8; TS017d5bf6=01cb3df500c326d97e014bddb349284e23afb49604548c2e49de9f16cb9807a75c4065286a1ca185992e0d8df471586f90905afeb8; TS01170c9f=01cb3df500c326d97e014bddb349284e23afb49604548c2e49de9f16cb9807a75c4065286a1ca185992e0d8df471586f90905afeb8; _pxde=b112cd618a7d07c21dfe2eeeda4eb02716b7445ed4b3716b88cc294da2402c49:eyJ0aW1lc3RhbXAiOjE2NzcyNzIzNTg5OTV9',
        'pragma': 'no-cache',
        # 'referer': 'https://www.google.com/',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    headers2 = {
        'authority': 'www.walmart.ca',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': 'localStoreInfo=eyJwb3N0YWxDb2RlIjoiTDVWMk42IiwibG9jYWxTdG9yZUlkIjoiMTA2MSIsInNlbGVjdGVkU3RvcmVJZCI6IjEwNjEiLCJzZWxlY3RlZFN0b3JlTmFtZSI6IkhlYXJ0bGFuZCBTdXBlcmNlbnRyZSIsImZ1bGZpbGxtZW50U3RvcmVJZCI6IjEwNjEiLCJmdWxmaWxsbWVudFR5cGUiOiJJTlNUT1JFX1BJQ0tVUCIsImFzc2lnbmVkRmFsbGJhY2siOnRydWV9; deliveryCatchment=1061; walmart.nearestPostalCode=L5V2N6; walmart.shippingPostalCode=L5V2N6; defaultNearestStoreId=1061; headerType=grocery; vtc=Udp3p-Bh-iY8r3q586STkg; walmart.nearestLatLng="43.60822,-79.69387"; TS017d5bf6=01538efd7ca77173d6f57a33fe8401f0b96e227acd0d7130a62c8c2ca401dc07c7cb3924dbcd018f6087ff3b80a4083c97f5b92816; userSegment=40-percent; walmart.id=a06420cb-3b27-4837-8de0-5f29519faa90; DYN_USER_ID=7012f18e-ba29-4757-8839-68f0d97d59b8; WM_SEC.AUTH_TOKEN=MTAyOTYyMDE44TburFcIAaUIm80Q8rLWh1FD3wd1QYDtSFH/kgrBfOHT4Dm0OD2OYMhhAcVLntAmOl1Qo7NA5Gjyhqpvv/nKnf5GoO11RLjPWXDxxeq5eaNEN6y5yOVjuY86cMq9PkNRj8OFN4dileb20bpDLeCIlSFd/Hsc7bnSe4+TLU2zbj1VARrYyKc6EDZWgDNpPDntGCGzasLrTjDWuCho6CFa5TrnXVtFH1RcVEtwWee4aETb/SoGFgAYL9DGZ8K45WCXDCcb9mgycy9jtT1uIyOBHWD+jrJmimQkL94oxm+ogG9+WowhAkgBnOt7xXIf+4f1nkA9m/JlJ+LUiNqPD3Z4AuH1TCzUfAWLpL5zZkw/4yfifM+FSzTmodU691L008kYc/CTQ09n8n4/EymoYgdtzEr1eX9YGQ0laieVMoEr348=; LT=1677257808682; DYN_USER_ID.ro=7012f18e-ba29-4757-8839-68f0d97d59b8; NEXT_GEN.ENABLED=1; cartId=b4413b5e-f3d8-42fa-aaa1-72fe1b64f9aa; _gcl_au=1.1.260208977.1677257811; pxcts=3bd87a59-b464-11ed-bab1-445474776f4e; _pxvid=3bd86d26-b464-11ed-bab1-445474776f4e; s_ecid=MCMID%7C31356660122460010071158502235397407282; AMCVS_C4C6370453309C960A490D44%40AdobeOrg=1; s_cc=true; _ga=GA1.2.1858048017.1677257814; _gid=GA1.2.1087270790.1677257814; kndctr_C4C6370453309C960A490D44_AdobeOrg_identity=CiYzMTM1NjY2MDEyMjQ2MDAxMDA3MTE1ODUwMjIzNTM5NzQwNzI4MlIQCJ7p7KLoMBABGAEqA09SMvABnunsougw; _cs_c=1; __gads=ID=614ff87a5c62773c:T=1677257816:S=ALNI_Mav53MAOpYhjqMtwRbr9GUbwJYebQ; __gpi=UID=000009502a27a226:T=1677257816:RT=1677257816:S=ALNI_MZy9kOBywEPgsXCXoN0ptSxzDzhtA; _fbp=fb.1.1677257824132.371702569; cookiePolicy=true; enableHTTPS=1; ak_bmsc=4B7A0F29F0C8829AC06B6C1EEBDB20E1~000000000000000000000000000000~YAAQkvzaF6p153CGAQAAy2buhBKBympy7dlXBDF0neVplL/fBj3DaGtWdJDsUZGZV+9Syvm5h+HTarP6wQpe5qWJYxr3e1r0OEcp8PdG0ELJsUdUsD+viYha+5yrdJ6H8wMcLj8ofc7zmahwL+I3Hh7Vbcg9EbIf5P+c0mhA1nFxGmL1jc6b8fLH4zx450hRTwTFo8WaU/RSuXVD3ev2p+aavOjQNdlJU7I+JcNFUupQECBVPa/DTN1jVLmJBKUU7/fBNTTQCeOVLJ5303bxoIj2fQWWOpMxwe/VDuWgVgrVabcq0l/cG/KdwmnlJs2HNOiSGwWLZLLX+YjOFbZ78t1wZT4F97RDn352d/AQQFqXuMnasmCqJUQJ+Y4Hvr5Vgut6KwMjvuJjTA==; TS01170c9f=01538efd7c07da1a2bd1558a58fc333fe4ff6ce1196c6ecc4ce42599076c91487089be6667d17895b0f1294390e048d920b189d570; wmt.c=0; authDuration={"lat":"1677267524963000","lt":"1677267524963000"}; _scid=c8387fc8-036f-4e24-93df-426dcbc6ad91; _uetsid=d9c469c0b47a11eda1372f9a4f1d8c5a; _uetvid=d9c48f60b47a11ed8d238b61c204b777; cto_bundle=g6kHUl9jS21qRzBkN1I5YnE2bWlyb2o5blJtNERWNnM3RnNDTU0wbTNNZEJVMXVuRDJqN1NGd2RlazVYNCUyQmlvUkxxeVpzRjJzamZvdThDcGZ3YWs2ckJWMzRLMkRQVzdZdnZxJTJGT2ZBSWlTNEtKdWdGb2VScDZGUTVyUzFNTEtFd0s1bE8; s_gnr=1677267526965-Repeat; s_sq=%5B%5BB%5D%5D; _cs_cvars=%7B%221%22%3A%5B%22appName%22%2C%22browse-search-page%22%5D%7D; _pin_unauth=dWlkPU9EVm1aalkyWXpJdE1EYzVaaTAwWXpkaUxXSm1ZbVF0TTJGaE16azFaVGt4WWpabQ; AMCV_C4C6370453309C960A490D44%40AdobeOrg=-1124106680%7CMCIDTS%7C19413%7CMCMID%7C31356660122460010071158502235397407282%7CMCAID%7CNONE%7CMCOPTOUT-1677274728s%7CNONE%7CMCAAMLH-1677872328%7C6%7CMCAAMB-1677872328%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19420%7CvVersion%7C5.2.0; ENV=ak-scus-t1-prod; xpa=0bwws|5sfML|CEJ49|KX9zf|NkdDh|OCyta|Qligk|RxMsL|S2NR7|Sd2S2|Sek64|SrVxB|TKAa5|VKpZ3|ZIhUr|ZZ-I8|hcJIR|ik-KQ|jE0bf|jxo4u|mVv6K|uo8Lz; exp-ck=5sfML1NkdDh1Qligk1RxMsL1S2NR72Sd2S21Sek642ZIhUr1jxo4u1uo8Lz1; bstc=Z-dIEg3WBR10pqjFxW7GE0; xpm=1%2B1677269417%2BUdp3p-Bh-iY8r3q586STkg~%2B0; TS0196c61b=01538efd7c59dfa238b610c3ec5ee806b7eafdb02217a7290a35079f5317765900a0ecae5b422a154e331bc8c1e995e8bc61d72978; seqnum=16; bm_sv=42A1B71CD978598DC59C41E602224D20~YAAQR8ITAvtpWTKGAQAAq4IdhRJxD7ISyypMTWYt5OAc2fbh+I/123W9RXW3dt2q1QD31yBKD3Bc5QgnMhBmZfQk7JlFyilBo4w4NMNABWVYpOK25C/tUgaLQUa3RLv3hpRS89nRe5KKbADNoWBCo9AGnnrso6T1Ik7/hfeiQZSIRn2mUYqCM2iqnyYaYbKibBpL8d+uKQbp1nsxTvQMo/xhNXpdw8egRyfBx83qp2o2y7M+51y3PtS1JGQHpc+xew==~1; _pxde=78ad74981f6d8d2f5fb107e3d41850d7bbca08a3972e381b99845a6a187e7757:eyJ0aW1lc3RhbXAiOjE2NzcyNzExMjY4MzV9; _cs_id=b79b6952-e23e-a27b-ba87-a6473ae96c3a.1677257815.5.1677271311.1677271311.1.1711421815737; _cs_s=1.0.0.1677273111078',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], headers=self.headers, callback=self.parse)

    def parse(self, response):
        data = response.xpath("//script[text()[contains(., 'window.__PRELOADED_STATE__=')]] //text()").re_first(
            r'window.__PRELOADED_STATE__=(.*);$')
        data = json.loads(data)

        products = data.get("results").get("entities", {}).get("products", {})

        for product in products.values():
            prod_id = product.get("id")
            prod_name = product.get("name")
            description = product.get("description", "")
            url = "https://www.walmart.ca/en/ip/{}/{}".format(prod_name.lower().replace(" ", "-"), prod_id)

            brand = "Walmart"
            base = {
                "prod_id": prod_id,
                "prod_name": prod_name,
                "url": url,
                "brand": brand,
                "description": description
            }

            yield scrapy.Request(url, callback=self.parse_product, headers=self.headers2,
                                 meta={"base": base, "prod_id": prod_id})

        # or
        # products = response.css("#product-results [data-automation='grocery-product'] >a ::attr(href)").extract()
        # for product in products:
        #     yield scrapy.Request(product, callback=self.parse_product, headers=self.headers2)


    def parse_product(self, response):
        data = response.xpath("//script[text()[contains(., 'window.__PRELOADED_STATE__=')]] //text()").re_first(
            r'window.__PRELOADED_STATE__=(.*);$')

        data = json.loads(data)

        active_sku = data['product']['activeSkuId']
        cats = data['product']['item']['primaryCategories'][0]['hierarchy']
        category = [cat['displayName']['en'] for cat in cats][::-1]

        images = data['entities']['skus'][active_sku]['images']
        image_urls = [image['thumbnail']['url'] for image in images]

        base = response.meta.get("base")
        base.update({
            "category": category,
            "image_urls": image_urls
        })

        price_api = "https://www.walmart.ca/api/bsp/v2/price-offer"

        payload = {
            "fsa": "L5V",
            "lang": "en",
            "pricingStoreId": "1061",
            "fulfillmentStoreId": "1061",
            "experience": "grocery"
        }

        prod_id = response.meta.get("prod_id")

        products = [
            {
                "productId": prod_id,
                "skuIds": [
                    active_sku
                ]
            }
        ]

        payload.update({"products": products})

        yield scrapy.Request(price_api, method="POST", body=json.dumps(payload), headers=self.headers,
                             callback=self.parse_price, meta={"base": base, "sku": active_sku})

    def parse_price(self, response):
        data = json.loads(response.body)

        base = response.meta.get("base")
        sku = response.meta.get("sku")

        # prod_id = base.get("prod_id")
        price = data['offers'][sku]['currentPrice']
        brand = data['offers'][sku]['sellerInfo']['en']

        base.update({
            "price": price,
            "brand": brand
        })
        yield base
