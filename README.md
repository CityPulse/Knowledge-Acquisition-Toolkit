# KAT
KAT - Knowledge Acquisition Toolkit

To run KAT go to view folder and run KATView.py

KAT follows a simple processing approach. We use a general workflow that has been extracted by observing several different solutions for information abstraction. The existing solutions either follow the steps shown in the figure below or implement some parts of it. We identified the following main steps: Pre-processing to bring the data into shape for further processing, Dimensionality Reduction to either compress the data or reduce its feature vectors, Feature Extraction to find low-level Abstractions in local sensor data, Abstraction from raw data to higher-level Abstractions and finally semantic representations to make the abstracted data available for the end-user and/or machines that interpret the data.

![alt tag](http://kat.ee.surrey.ac.uk/graph/flow.png)

(Source: Frieder Ganz, Daniel Puschmann, Payam Barnaghi, Francois Carrez, "A Practical Evaluation of Information Processing and Abstraction Techniques for the Internet of Things", IEEE Internet of Things Journal, 2015.)

# Pre-Processing
The raw sensory data is pre-processed stage to prepare the data for information acquisition. Pre-processing can be done on sensor nodes to reduce transmission cost or filter unwanted data and can include mathematical/statistical methods to smooth the data by applying moving average windows, or methods from signal processing such as band-, low-, high pass filtering to focus on a certain frequency spectrum.

Transmission cost can be reduced by only sending aggregated information or a selection of data to a base-station or a gateway; e.g. sending minimum and/or maximum values or the mean value of the current window. The pre-processing is not only limited to a single sensor node; some solutions use in-network processing to aggregate the data before further processing it by finding the minimum, mean or maximum value in a set of sensor nodes and before transmitting the data to a base station. In addition to data aggregation, in-network techniques can also be used to improve the accuracy of the data by calculating correlation with data from neighbouring nodes.

# Dimensionality Reduction
To handle the large amount of data that has to be processed and stored. Dimensionality reduction can decrease the size and length of samples by applying different methods on the data while preserving the important features and patterns.

This section presents a simple example based on a dataset gathered in an office environment consisting of several hundred thousand sensor readings. The sensor was deployed near an office desk and measured light level, PIR, sound, and energy consumption of an office workstation. The dataset can be downloaded here: http://kat.ee.surrey.ac.uk/download.html


# Data Import
The first step is the data import. KAT currently supports CSV and MS Excel formats. To import data click on the Load Data button and select a comma separated file or an MS Excel file. You can download the sample dataset (http://kat.ee.surrey.ac.uk/download.html), save it as a csv file and import it to KAT.

![alt tag](http://kat.ee.surrey.ac.uk/graph/KAT_sc1.PNG)


Once the data is imported, the labels will appear on the screen. Select "light" check box from the data labels to show the data in a diagram (as shown below). In case that the data is not shown, select check box and left click on empty diagram.

![alt tag](http://kat.ee.surrey.ac.uk/graph/KAT_sc2.PNG)


# Data Pre-Processing
To highlight features of the data set, a mean filter is used in this example. The mean filter divides the data into windows and replaces the window with the mean value. This filter can highlight outliers and reduces the noise.

![alt tag](http://kat.ee.surrey.ac.uk/graph/KAT_sc3.PNG)

# Dimension Reduction
To create a symbolic representation of the data, we use a technique called SAX. 

![alt tag](http://kat.ee.surrey.ac.uk/graph/KAT_sc4.PNG)

# Feature Extraction
To find interesting patterns that are likely to represent an event, phenomena or interesting observations a k-means clustering algorithm is used. In this example, the k-means algorithm is run with a group size of three. The algorithm clusters periods of low activity (low power), medium activity, and peaks (high power usage) into the groups labelling them from 0 to 2.

![alt tag](http://kat.ee.surrey.ac.uk/graph/KAT_sc5.PNG)

# Abstraction
To find relationships between different groups produced in the previous section, a Markov based statistical model is applied to the data. The model returns the likelihood of the temporal presence of the different groups.

![alt tag](http://kat.ee.surrey.ac.uk/graph/KAT_sc6.PNG)
