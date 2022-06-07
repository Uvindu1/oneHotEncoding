import pandas as pd
from sklearn.preprocessing import LabelEncoder # samanya paridi encode karanne meken
from sklearn.preprocessing import LabelBinarizer # meken thamai one hot encoding kirima
data = pd.read_csv("Iris.csv")
print(data["Species"])

result_category = data["Species"]

# samanya paridi encode kirima
obj1 = LabelEncoder()
result1 = obj1.fit_transform(result_category)
print(result1)

# one hot encoding kirima
obj2 = LabelBinarizer()
result2 = obj2.fit_transform(result_category)
print(result2)

# one hot encoding kiyana ekee class tika
object_class = obj2.classes_
print(object_class)
























