import requests
from lxml import etree


def parse_detail_html():
    html = requests.get(
        'https://www.healthcareglobal.com/press-release/fda-approves-biotroniks-ultrathin-orsiro-stent-treatment'
        '-coronary-artery-disease').text
    selector = etree.HTML(html)
    tags = ['press-release']
    author = str(
        selector.xpath('//div[@class="flex__SQ2u alignCenter__1AJm wrapInfoItem__1CQU"][1]/a/strong/text()')[
            0]).split(",")[0]
    content = ""
    elements = selector.xpath('//div[@class="xn-content"]/*')
    for element in elements:
        if isinstance(element, str):

            content += '\n' + element.strip() + "\n"
        elif element.tag in ["p", "h4", "h2", "h1", "h3"]:
            content_text = element.xpath('string(.)').strip()
            content += '\n' + content_text + "\n"
            if element.tail:
                content += '\n' + element.tail + "\n"
        elif element.tag in ["a", "em", "span"]:
            content_text = element.xpath('string(.)').strip()
            content += content_text
            if element.tail:
                content += element.tail
        elif element.tag == "ul":
            temp_texts = element.xpath(".//text()")
            for temp_text in temp_texts:
                content += '\n' + temp_text + "\n"
    return {'tags': tags, 'content': content, "authors": author}
    # return self.generate_json_data(self.uri, title=None, content=content, tags=tags, author=author)
    # 调用generate_json_data方法生成json,生成的json语句若某属性没有值，则显示为null


if __name__ == '__main__':
    parse_detail_html()
