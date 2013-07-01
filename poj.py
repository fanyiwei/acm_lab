import urllib

class poj:

    def __init__(self):
        self.url_head = 'http://poj.org/userstatus?user_id'
        
    def find(self, name=''):
        self.name = name
        url = '%s=%s' %(self.url_head, self.name)
        html_src = urllib.urlopen(url).read()
        s = '<a href=status?result=0&user_id=%s>' % self.name
        i = html_src.find(s)
        if i == -1:
            return '0'
        temp = html_src[i:i+123]
        i = temp.find('>')
        j = temp.find('</')
        return temp[i+1:j]

