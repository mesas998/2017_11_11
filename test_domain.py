from urlparse import urlparse
parsed_uri = urlparse( 'http://stackoverflow.com/questions/1234567/blah-blah-blah-blah' )
domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
print domain

# gives 'http://stackoverflow.com/'

