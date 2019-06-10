from lxml import etree
import xml.etree.ElementTree as ET
import pandas as pd
import pdb
from datetime import datetime

xml_path = "ground-truth-training-byarticle-20181122.xml"

context = ET.parse(xml_path)
root = context.getroot()

context = ET.parse(xml_path)
root = context.getroot()

df = pd.DataFrame(columns=["id", "hyperpartisan", "labled_by", "URL"])
for child in root :
	_id = int(child.attrib["id"])
	hyperpartisan = child.attrib["hyperpartisan"]
	labled_by = child.attrib["labeled-by"]
	URL = by = child.attrib["url"]
	df.loc[len(df)] = [_id, hyperpartisan, labled_by, URL]

df.to_csv("ground-truth-training-byarticle-20181122.csv")