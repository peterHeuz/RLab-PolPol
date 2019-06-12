import xml.etree.ElementTree as ET
import pandas as pd
import sys
from datetime import datetime

def main(file_path):
	xml_path = "data_semeval/" + file_path + ".xml"

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

	df.to_csv("data_semeval/" + file_path + ".csv")

if __name__ == '__main__':
	main(sys.argv[1])