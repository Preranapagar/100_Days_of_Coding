#generating dataset at run time randomly and apply user defined k-means algorithm

import numpy as np
import pandas as pd
from copy import deepcopy
from matplotlib import pyplot as plt

def Kmean():
    print("-"*50)

    #set three centers, the model should predict similar results
    center_1 = np.array([1,1])
    print(center_1)
    print("-"*50)

    center_2 = np.array([5,5])
    print(center_2)
    print("-"*50)

    center_3 = np.array([8,1])
    print(center_3)
    print("-"*50)

    #Generate random data and center it to the three centers
    data_1 = np.random.randn(7,2) + center_1
    print("Element of first cluster with size "+str(len(data_1)))
    print(data_1)
    print("-"*50)

    data_2 = np.random.randn(7,2) + center_2
    print("Element of second cluster with size "+str(len(data_2)))
    print(data_2)
    print("-"*50)

    data_3 = np.random.randn(7,2) + center_3
    print("Element of third cluster with size "+str(len(data_3)))
    print(data_3)
    print("-"*50)

    data = np.concatenate((data_1,data_2,data_3),axis=0)
    print("Size of complete dataset "+str(len(data)))
    print(data)
    print("-"*50)

    plt.scatter(data[:,0],data[:,1],s=7)
    plt.title("Input Dataset")
    plt.show()
    print("-"*50)

    #number of clusters
    k = 3

    #number of training data
    n = data.shape[0]
    print("Total number of elements :", n)
    print("-"*50)

    #number of features in data
    c = data.shape[1]
    print("Total number of features :", c)
    print("-"*50)

    #generate random centers, here we use sigma and mean  to ensure it represent the whole data
    mean = np.mean(data,axis = 0)
    print("Value of Mean :", mean)
    print("-"*50)

    #calculate standard deviation
    std = np.std(data, axis = 0)
    print("Value of std :", std)
    print("-"*50)

    centers = np.random.randn(k,c)*std + mean
    print("Random points are :", centers)
    print("-"*50)

    #plot the data and the centers generated as random
    plt.scatter(data[:,0],data[:,1],c='r',s=7)
    plt.scatter(centers[:,0],centers[:,1],marker='*',c='g',s=150)
    plt.title("Input dataset with random centriod")
    plt.show()
    print("-"*50)

    center_old = np.zeros(centers.shape)
    center_new = deepcopy(centers)

    print("Values of old centroids")
    print(center_old)
    print("-"*50)

    print("Values of new centroids")
    print(center_new)
    print("-"*50)

    data.shape
    clusters = np.zeros(n)
    distances = np.zeros((n,k))

    print("Initial distances are")
    print(distances)
    print("-"*50)

    error = np.linalg.norm(center_new - center_old)
    print("Value of error is :", error)

    #when after an update, the estimate of that center stays the same, exit loop

    while error !=0:
        print("value of error is :", error)
        #measure distance to every center
        for i in range(k):
            print("Iteration number :", i)
            distances[:,i] = np.linalg.norm(data-centers[i], axis = 1)

        #assign all training points to closest center
        clusters = np.argmin(distances,axis=1)
        center_old = deepcopy(center_new)

        #calculate mean for every cluster and update center
        for i in range(k):
            center_new[i] = np.mean(data[clusters==i],axis=0)
        
        error = np.linalg.norm(center_new - center_old)

    #end of wile
    center_new

    #plot the data and the cluster generated as random
    plt.scatter(data[:,0],data[:,1],s=7)
    plt.scatter(center_new[:,0], center_new[:,1],marker ="*", c="g", s= 150)
    plt.title("Final data with centroids")
    plt.show()

def main():
    print("Unsupervised Machine Learning")
    print("Clustering using K-means")

    Kmean()

if __name__=="__main__":
    main()