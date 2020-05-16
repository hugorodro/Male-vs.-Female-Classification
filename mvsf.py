
# Even though the title says Male vs Female, the battle is
# model vs. model vs. model.
from sklearn import tree


# each 'person' has a height, weight , shoe size
X = [[181, 72, 30], [134, 74, 46], [191, 98, 44],
     [171, 99, 28], [198, 110, 14], [197, 89, 54],
     [189, 59, 32], [145, 109, 45], [134, 59, 32],
     [141, 70, 26], [188, 79, 54], [123, 77, 23]]

Y = [['male'], ['female'], ['male'],
     ['male'], ['male'], ['male'],
     ['male'], ['female'], ['female'],
     ['female'], ['male'], ['female'], ]

#Using a decision tree...
treeCLF =  tree.DecisionTreeClassifier()
treeCLF = treeCLF.fit(X,Y)
prediction = treeCLF.predict([[176,45,45], [123, 65,34]])
print(prediction)

#Seems like height was the most import feature! Body fat doesn't discriminate!
