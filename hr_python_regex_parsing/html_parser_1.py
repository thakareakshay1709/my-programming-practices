from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def _handler_factory(msg):
        msg = msg.ljust(6) + ':'
        def handler(self, tag, attrs=[]):
            print(msg, tag)
            for a in attrs:
                print("-> %s > %s" % a)
        return handler

    locals().update(zip(
        map("handle_{}tag".format, ("start", "end", "startend")),
        map(_handler_factory, ("Start", "End", "Empty"))
    ))

MyHTMLParser().feed(' '.join(input() for _ in range(int(input()))))