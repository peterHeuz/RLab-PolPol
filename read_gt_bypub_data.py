from lxml import etree
import xml.etree.ElementTree as ET
import pandas as pd
from datetime import datetime

xml_path = "data_semeval/ground-truth-validation-bypublisher-20181122.xml"
# with open(xsd_path) as xsd_file
# 	xmlschema_doc = etree.parse(f)
# 	xmlschema = etree.XMLSchema(xmlschema_doc)

context = ET.parse(xml_path)
root = context.getroot()

df = pd.DataFrame(columns=["id", "hyperpartisan", "bias", "URL", "labeled_by"])
for child in root :
	_id = int(child.attrib["id"])
	bias = child.attrib["bias"]		
	hyper = child.attrib["hyperpartisan"]
	lbl = child.attrib["labeled-by"]
	url = child.attrib["url"]
	if _id % 1000 == 0:
			print(datetime.now().time(), " - " ,
				str(_id), " articles processed")
	df.loc[len(df)] = [_id, hyper, bias, url, lbl]

df.to_csv("data_semeval/ground-truth-validation-bypublisher-20181122.csv")
