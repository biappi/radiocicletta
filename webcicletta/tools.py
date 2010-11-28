from BeautifulSoup import BeautifulSoup, Comment
def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

def clean(value):
        valid_tags = 'p i strong b u a h1 h2 h3 pre br img'.split()
        valid_attrs = 'href src'.split()
        soup = BeautifulSoup(value)
        for comment in soup.findAll(
            text=lambda text: isinstance(text, Comment)):
            comment.extract()
        for tag in soup.findAll(True):
            if tag.name not in self.valid_tags:
                tag.hidden = True
            tag.attrs = [(attr, val) for attr, val in tag.attrs
                         if attr in self.valid_attrs]
        return soup.renderContents().decode('utf8')


def purifica_html(s): #prende la descriz e purifica seriamente l'html, ci mette ' in cima e in fondo e codifica in html i caratteri spaccajson
		      #infine taglia la descr al primo spazio (o punto, o ...) utile dopo _MAXLEN
	_MAXLEN=120
	try:
		s=clean(s)
	except:
		pass
	if s[0]=='"':
		s[0]="'"
	if s[0]!="'":
		s="'"+s
	if s[-1]!="'":
		s=s+"'"
	purazza={"'":"&#39;", "'":"\\'",":":"&#58;",";":"&#59;",".":"&#46;","[":"&#91;","]":"&#93;","{":"&#123;","}":"&#125;","#":"&#35;","$":"&#36;"}
	s=replace_all(s[1:-1],purazza)
	if len(s)>_MAXLEN:
		while s[_MAXLEN] not in [" ","!","."]:
			_MAXLEN=_MAXLEN+1
		s=s[:_MAXLEN]+" [...]"
	s.replace('\n',"<br>")
	return s
