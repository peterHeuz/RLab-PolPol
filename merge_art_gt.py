import pandas as pd
import sys

def main(art_path, gt_path):
	art = pd.read_csv("data_semeval/" + art_path)
	art.drop("Unnamed: 0", axis=1)
	gt = pd.read_csv("data_semeval/" + gt_path)
	gt.drop("Unnamed: 0", axis=1)
	df = art.merge(gt,on="id")
	df.to_csv("data_semeval/articles-" + gt_path)

if __name__ == '__main__':
	main(sys.argv[1], sys.argv[2])