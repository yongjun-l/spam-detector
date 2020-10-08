import os
import numpy as np
import pandas as pd

base_dir = os.path.abspath("")
csv_dataset = os.path.join(base_dir, "dataset.csv")

dataset = pd.read_csv(csv_dataset, names=['text', 'label'])
print(dataset.shape)

#divide up dataset to training set and testing set
train = dataset.loc[:30000,['text']]
train_label = dataset.loc[:30000,['label']]
test = dataset.loc[30000:,['text']]
test_label = dataset.loc[30000:,['label']]



