import xml.etree.ElementTree as ET
import pandas as pd
import sys

def main(file_path):
	xml_path = "data_semeval/" + file_path + ".xml"

	context = ET.parse(xml_path)
	root = context.getroot()

	context = ET.parse(xml_path)
	root = context.getroot()

	df = pd.DataFrame(columns=["id", "hyperpartisan", "labeled_by", "URL"])
	for child in root :
		_id = int(child.attrib["id"])
		hyperpartisan = child.attrib["hyperpartisan"]
		labeled_by = child.attrib["labeled-by"]
		URL = by = child.attrib["url"]
		df.loc[len(df)] = [_id, hyperpartisan, labeled_by, URL]

	df.to_csv("data_semeval/" + file_path + ".csv")

if __name__ == "__main__":
   main(sys.argv[1])