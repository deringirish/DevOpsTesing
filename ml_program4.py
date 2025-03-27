import pandas as pd


def find_s_algorithm(file_path):
    data = pd.read_csv(file_path)
    print("Training Data:\n", data)
    attributes = data.columns[:-1]
    class_label = data.columns[-1]
    positive_instances = data[data[class_label] == 'Yes']
    hypothesis = list(positive_instances.iloc[0][attributes])
    for _, row in positive_instances.iterrows():
        for i, value in enumerate(row[attributes]):
            if hypothesis[i] != value:
                hypothesis[i] = "?"
    return hypothesis


filepath = "Program4\\training_data.csv"
hypothesis = find_s_algorithm(filepath)
print("\nThe final hypothesis si:", hypothesis)
