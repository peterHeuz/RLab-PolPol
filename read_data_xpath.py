from lxml import etree
import pandas as pd
import pdb
from datetime import datetime

xml_path = "data_semeval/articles-training-byarticle-20181122.xml"

# with open(xsd_path) as xsd_file
# 	xmlschema_doc = etree.parse(f)
# 	xmlschema = etree.XMLSchema(xmlschema_doc)

context = etree.iterparse(xml_path, tag='article' )

df = pd.DataFrame(columns=["id", "title", "published", "text"])
for event, elem in context :
	text = elem.text
	if text == None:
		pdb.set_trace()
	if len(elem.xpath("@title")) == 1:
		title = elem.xpath("@title")[0] 
	else:
		title = None
	if len(elem.xpath("@published-at")) == 1:
		published = elem.xpath("@published-at")[0] 
	else:
		published = None 
	if len(elem.xpath("@id")) == 1:
		_id = int(elem.xpath("@id")[0])
	else:
		_id = None
	if _id % 1000 == 0:
			print(datetime.now().time(), " - " ,
				str(_id), " articles processed")
	df.loc[len(df)] = [_id, title, published, text]

pdb.set_trace()

del context



from bs4 import BeautifulSoup


# parser = etree.XMLParser(schema=etree.XMLSchema(file=xsd_path))
# soup = BeautifulSoup(open(xml_path))
with open(xml_path) as xml_file:
	# xml_f = xml_file.read()
	soup = BeautifulSoup(xml_file, "xml")

pdb.set_trace()
df = pd.DataFrame(columns=["id", "title", "published", "text"])
for art in soup.articles:
	try:
		text = art.text
		attribs = art.attrs 
		if int(attribs["id"]) % 1000 == 0:
			print(datetime.now().time(), " - " ,
				str(attribs["id"]), " articles processed")
		try:
			df.loc[len(df)] = [attribs["id"], attribs["title"], attribs["published-at"], text]
		except KeyError:
			df.loc[len(df)] = [attribs["id"], attribs["title"], None, text]
	except AttributeError:
		pass

df.to_csv("data_semeval/articles-validation-bypublisher-20181122.csv")
	# 	xml_parsed = etree.XML(xml_f, parser)

