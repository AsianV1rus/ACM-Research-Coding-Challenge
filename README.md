# ACM Research Coding Challenge (Fall 2020)

## No Collaboration Policy

**You may not collaborate with anyone on this challenge.** You _are_ allowed to use Internet documentation. If you _do_ use existing code (either from Github, Stack Overflow, or other sources), **please cite your sources in the README**.

## Submission Procedure

Please follow the below instructions on how to submit your answers.

1. Create a **public** fork of this repo and name it `ACM-Research-Coding-Challenge`. To fork this repo, click the button on the top right and click the "Fork" button.
2. Clone the fork of the repo to your computer using . `git clone [the URL of your clone]`. You may need to install Git for this (Google it).
3. Complete the Challenge based on the instructions below.
4. Email the link of your repo to research@acmutd.co with the same email you used to submit your application. Be sure to include your name in the email.

## Question One

![Image of Cluster Plot](ClusterPlot.png)
<br/>
Given the following dataset in `ClusterPlot.csv`, determine the number of clusters by using any clustering algorithm. **You're allowed to use any Python library you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file.

INTERNET DOCUMENTATION
To read the CVS file
https://realpython.com/python-csv/#parsing-csv-files-with-the-pandas-library

To convert my DataFrame to the nmd array
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_numpy.html

To actaully do the Clustering and the ploting
https://pythonprogramming.net/hierarchical-clustering-mean-shift-machine-learning-tutorial/


EXPLAINATION
Being not very familiar with Python, I first had to try to learn it to first attempt this problem. I was only familiar with C++ because of college course I am currently taking
and Java, something I was very familar with as I used it all throughout high school. Luckly when I looked up clustering algorithm I came across Hierarchical Clustering, 
exactly what I needed.

First read in the csv file and stored it into a nmd Array.
Then I used the Mean Shift library 'fit' function to read in the data from the csv and to find the center of the data of each cluster
ms.label then gives us the cluster array
and the unqiue len gives us the number of clusters in label

From my basic understanding, mean shift sets every point in the data as a center and records all of the value within a certain radius? With that, it takes
the mean or the avg of the location and reiterates itself as a center till the mean doesnt change. I think?