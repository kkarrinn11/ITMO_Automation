from re import search


class Input:

    def __init__(self, loc):
        self.loc = loc


search = Input ('input#search')

print (search.loc)

