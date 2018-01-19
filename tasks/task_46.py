def parse_url_string(url):
    params = url.split('?')[1].split('&')
    car = {}
    for param in params:
        car[param.split('=')[0]] = param.split('=')[1]
    return car
    
model_x = parse_url_string('domain.com?model=x&color=black&package=signature&interior=brown&wheels=alloy')

print model_x
print 'Model: %s' % model_x['model']
print 'Color: %s' %model_x['color']
print 'Package: %s' %model_x['package']
print 'Interior: %s' %model_x['interior']
print 'Wheels: %s' %model_x['wheels']
