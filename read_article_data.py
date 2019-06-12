import xml.etree.ElementTree as ET
import pandas as pd
from datetime import datetime
import sys 

def main(file_path):
	xml_path = "data_semeval/" + file_path + ".xml"

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
	# removes all line breaks
	df["text"] = df["text"].apply(lambda x: x.replace("\n", " "))

	df.to_csv("data_semeval/" + file_path + ".csv")


if __name__ == "__main__":
   main(sys.argv[1])
