from random import sample
import pandas as pd 
import sys

if __name__ == '__main__':
	dataset_path = sys.argv[1]
	k = int(sys.argv[2])

	df = pd.read_csv(dataset_path)
	df_sub = df.iloc[sample(range(len(df)),k)]

	df_sub.to_csv(dataset_path[:-4] 
		+ "_" + str(k) + ".csv")