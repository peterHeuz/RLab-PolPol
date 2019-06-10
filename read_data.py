from lxml import etree
import pandas as pd
import pdb
from datetime import datetime

xml_path = "data_semeval/articles-validation-bypublisher-20181122.xml"
xsd_path = "data_semeval/article.xsd"

# with open(xsd_path) as xsd_file
# 	xmlschema_doc = etree.parse(f)
# 	xmlschema = etree.XMLSchema(xmlschema_doc)

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

