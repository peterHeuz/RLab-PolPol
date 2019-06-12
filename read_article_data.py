import xml.etree.ElementTree as ET
import pandas as pd
from datetime import datetime

xml_path = "data_semeval/articles-training-byarticle-20181122.xml"
# with open(xsd_path) as xsd_file
# 	xmlschema_doc = etree.parse(f)
# 	xmlschema = etree.XMLSchema(xmlschema_doc)

context = ET.parse(xml_path)
root = context.getroot()

df = pd.DataFrame(columns=["id", "title", "published", "text"])
for child in root :
	text = "".join(child.itertext())
	_id = int(child.attrib["id"])
	try:
		published = child.attrib["published-at"]
	except KeyError:
		published = None
	title = child.attrib["title"]
	if _id % 1000 == 0:
			print(datetime.now().time(), " - " ,
				str(_id), " articles processed")
	df.loc[len(df)] = [_id, title, published, text]

# converts published column to timestamps
df["published"] = df["published"].apply(lambda x: datetime.strptime(x, '%Y-%m-%d') if not pd.isnull(x) else None)
# removes leading /n s
df.loc[df['text'].str[:1] == "\n", 'text'] = df['text'].str[1:]

df.to_csv("data_semeval/articles-training-byarticle-20181122.csv")

