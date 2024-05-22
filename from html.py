from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    #def handle_starttag(self, tag, attrs):
        #print("Encountered a start tag:", tag)

    #def handle_endtag(self, tag):
        #print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print( data)


#parser = MyHTMLParser()
#parser.feed(r.text)




#print(r.status_code)
#print(r.headers)
#print(r.content)  # bytes
#print(r.text)     # r.content as str