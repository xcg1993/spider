from lxml import etree
def parse_xml():
    xml_parse=etree.parse('ips.xml')
    ips=xml_parse.xpath('//ip')

    for ip_selector in ips:
        # port= ip_selector.xpath('./@port')
        # ip=ip_selector.xpath('./text()')[0]
        port = ip_selector.get('port')
        ip = ip_selector.text
        print(ip,port)
if __name__ == '__main__':
    parse_xml()