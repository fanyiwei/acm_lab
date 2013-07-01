import urllib

class hdoj:

    def __init__(self):
        self.url_head = 'http://acm.hdu.edu.cn/userstatus.php?user'
        
    def find(self, name=''):
        self.name = name
        url = '%s=%s' %(self.url_head, self.name)
        html_src = urllib.urlopen(url).read()
        #print html_src
        s = '<tr><td>Problems Solved</td><td align=center>'
        i = html_src.find(s)
        if i == -1:
            return '0'
        temp = html_src[i:i+123]
        i = temp.find('center>')
        j = temp.find('</td></tr>')
        return temp[i+7:j]

