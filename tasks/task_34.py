import re


good_urls = (
    'http://www.amazon.com/exec/obidos/ASIN/B004NVUXH2/gasmencommon',
    'http://www.amazon.com/exec/obidos/ASIN/B004NVUXH2/gasmencommon-10',
    'http://www.amazon.com/exec/obidos/ASIN/B004NVUXH2/gasmencommon-2a',
)

bad_urls = (
    'http://www.amazon.com/exec/obidos/ASIN/B004NVUXH2/gasmencommon-20',
    'http://www.amazon.com/exec/obidos/ASIN/B004NVUXH2/gasmencommon-20-sdsdf',
    'http://www.amazon.com/exec/obidos/ASIN/B004N-20VUXH2/gasmencommon',
)


#reg = re.compile(r'^.*(gp/product|dp|ASIN)/(B[A-Za-z0-9]+)((?!\-2\d).)*$')
#reg = re.compile(r'^.*(gp\/product|dp|ASIN)/(?P<ext_id>B[A-Za-z0-9]+)((?!\-2\d).)*$')
reg = re.compile(r'^.*(gp\/product|dp|ASIN)\/(?P<ext_id>B[A-Za-z0-9]+)(?!.*\-(20|21).*$)')

def test_urls():
    for url in good_urls:
        match = reg.search(url)
        assert match
        print match.groups()[1]
        
    for url in bad_urls:
        assert not reg.search(url)


if __name__ == '__main__':
    test_urls()