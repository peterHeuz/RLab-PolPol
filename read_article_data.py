import xml.etree.ElementTree as ET
import pandas as pd
from datetime import datetime
import sys 

import pdb

def main(file_path):
	xml_path = "data_semeval/" + file_path + ".xml"

	context = ET.iterparse(xml_path, events=("start", "end"))
	# turn it into an iterator
	context = iter(context)

	# get the root element
	event, root = context.__next__()


	df = pd.DataFrame(columns=["id", "title", "published", "text"])
	for event, elem in context:
		if event == "end" and elem.tag == "article":
			text = "".join(elem.itertext())
			_id = int(elem.attrib["id"])
			try:
				published = elem.attrib["published-at"]
			except KeyError:
				published = None
			title = elem.attrib["title"]
			if _id % 1000 == 0:
					print(datetime.now().time(), " - " ,
						str(_id), " articles processed")
			df.loc[len(df)] = [_id, title, published, text]
			root.clear()

	# converts published column to timestamps
	df["published"] = df["published"].apply(lambda x: datetime.strptime(x, '%Y-%m-%d') if not pd.isnull(x) else None)
	# removes all line breaks
	df["text"] = df["text"].apply(lambda x: x.replace("\n", " "))

	df.to_csv("data_semeval/" + file_path + ".csv")


if __name__ == "__main__":
   main(sys.argv[1])
