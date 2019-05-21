from lxml import etree
import pandas as pd
import pdb

xml_path = "../data_semeval/articles-validation-bypublisher-20181122.xml"
xsd_path = "../data_semeval/article.xsd"

# with open(xsd_path) as xsd_file
# 	xmlschema_doc = etree.parse(f)
# 	xmlschema = etree.XMLSchema(xmlschema_doc)

from bs4 import BeautifulSoup


# parser = etree.XMLParser(schema=etree.XMLSchema(file=xsd_path))
with open(xml_path, "br") as xml_file:
	xml_f = xml_file.read()
	soup = BeautifulSoup(xml_f)

df = pd.DataFrame(columns=["id", "title", "published", "text"])
for art in soup.articles:
	try:
		text = art.text
		attribs = art.attrs 
		print(attribs["id"])
		try:
			df.loc[len(df)] = [attribs["id"], attribs["title"], attribs["published-at"], text]
		except KeyError:
			df.loc[len(df)] = [attribs["id"], attribs["title"], None, text]
	except AttributeError:
		pass

df.to_csv("../data_semeval/articles-validation-bypublisher-20181122.csv")
	# 	xml_parsed = etree.XML(xml_f, parser)

# for art in xml_parsed:
# 	print(art.text)
# 	print("\n\n")
# pdb.set_trace()
# # xml = etree.XML(xml_path)


# # """
# <?xml version="1.0" encoding="UTF-8"?>
# <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
#   <xs:element name="ELEMENT">
#     <xs:complexType>
#       <xs:sequence>
#         <xs:element ref="element 1"/>
#         <xs:element ref="element 2"/>
#         <xs:element ref="element 3"/>
#       </xs:sequence>
#     </xs:complexType>
#   </xs:element>
# </xs:schema>
# """


# namespaces = {"xs": "http://www.w3.org/2001/XMLSchema"}

# names = xml.xpath("//xs:element/@ref", namespaces=namespaces)
# for article in xml.getroot():
# 	pdb.set_trace()
# 	print(article.text)
# 	print(article.attrib)
# 	print("\n \n")

# pdb.set_trace()