import urllib

class cf:

    def __init__(self):
        self.url_head = 'http://codeforces.com/profile'
        
    def find(self, name=''):
        self.name = name
        url = '%s/%s' %(self.url_head, self.name)
        html_src = urllib.urlopen(url).read()
        s = '<span style="font-weight:bold;"'
        i = html_src.find(s)
        if i == -1:
            return '0'
        temp = html_src[i:i+123]
        i = temp.find('>')
        j = temp.find('</')
        return temp[i+1:j]

