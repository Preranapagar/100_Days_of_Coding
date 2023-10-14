from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def ClaculateAccuracyDesicionTree():
    iris = load_iris()

    data = iris.data
    target = iris.target

    train_data, test_data, train_target, test_target = train_test_split(data,target,test_size = 0.5)

    classifier = tree.DecisionTreeClassifier()
    classifier.fit(train_data,train_target)

    predictions = classifier.predict(test_data)
    Accuracy = accuracy_score(test_target,predictions)

    return Accuracy

def ClaculateAccuracyKNN():
    iris = load_iris()

    data = iris.data
    target = iris.target

    train_data, test_data, train_target, test_target = train_test_split(data,target, test_size =0.5)

    classifier = KNeighborsClassifier()
    classifier.fit(train_data,train_target)

    prediction = classifier.predict(test_data)
    Accuracy = accuracy_score(test_target, prediction)

    return Accuracy

def main():
    Accuracy = ClaculateAccuracyDesicionTree()
    print("Accuracy of Decision Tree algorithm is :", Accuracy*100,"%")

    Accuracy = ClaculateAccuracyKNN()
    print("Accuracy of K Nearest Neighbors algorithm is :", Accuracy*100,"%")

if __name__=="__main__":
    main()
