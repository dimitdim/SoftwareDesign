#import pattern
#import pattern.web
#
#url=pattern.web.URL('http://animalsadda.com/wp-content/uploads/2013/07/Albatross.jpg')
#print url.mimetype
#f=open('test'+pattern.web.extension(url.page),'wb')
#f.write(url.download())
#f.close()

from patter.web import Facebook
f=Facebook()

