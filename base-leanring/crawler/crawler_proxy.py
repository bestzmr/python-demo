import requests
from lxml import etree
import time
"""爬取番茄代理IP"""


def parse_list(response):
    selector = etree.HTML(response)
    elements = selector.xpath('//div[@class="table-responsive mb-0"]/table/tbody/tr')
    if elements is None or len(elements) == 0:
        return None
    ip_list = []
    for element in elements:
        ip_dict = {'ip': element.xpath('./td[1]/div/text()')[0], 'port': element.xpath('./td[2]/div/text()')[0],
                   'address': element.xpath('./td[3]/div/text()')[0], 'ip_type': element.xpath('./td[4]/div/text()')[0]}
        ip_list.append(ip_dict)
    return ip_list


if __name__ == '__main__':
    start_time = time.time()
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "max-age=0",
        "Host": "www.fanqieip.com",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"

    }
    result = []
    for i in range(1, 5):
        http_response = requests.get('https://www.fanqieip.com/free/China/' + str(i), headers=headers)
        result_list = parse_list(http_response.text)
        if result_list is None:
            continue
        result.extend(result_list)
    end_time = time.time()
    print("总共消耗%.2f秒" % (end_time - start_time))
    print("总共%d条" % len(result))

    # for e in result:
    #     print(e['ip'], e['port'], e['address'], e['ip_type'])
