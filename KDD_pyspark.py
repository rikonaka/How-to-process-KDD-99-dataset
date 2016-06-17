#
# 
# Copyright 2016 isinstance <super_big_hero@sina.com>/*
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301, USA.
# 
# 
#

#!/usr/bin/env python

# dataset: http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html

import sys
import os


# Path for spark source folder
os.environ['SPARK_HOME']="/path/to/spark"

# Append pyspark  to Python Path
sys.path.append("/path/to/spark/python")

try:
    from pyspark import SparkContext, SparkConf
    from pyspark.mllib.clustering import KMeans
    from pyspark.mllib.feature import StandardScaler
    print ("Successfully imported Spark Modules")
except ImportError as e:
    print ("Can not import Spark Modules", e)
    sys.exit(1)

from numpy import array
from math import sqrt

def parse_interaction(line):
    """
    Parses a network data interaction.
    """
    line_split = line.split(",")
    clean_line_split = line_split[0:-1]
    return (line_split[-1], array([float(x) for x in clean_line_split]))


def distance(a, b):
    """
    Calculates the euclidean distance between two numeric RDDs
    """
    return sqrt(a.zip(b).map(lambda x: (x[0]-x[1])).map(lambda x: x*x).reduce(lambda a,b: a+b))


def dist_to_centroid(datum, clusters):
    """
    Determines the distance of a point to its cluster centroid
    """
    cluster = clusters.predict(datum)
    centroid = clusters.centers[cluster]
    return sqrt(sum([x**2 for x in (centroid - datum)]))


def clustering_score(data, k):
    clusters = KMeans.train(data, k, maxIterations=10, runs=5, initializationMode="random")
    result = (k, clusters, data.map(lambda datum: dist_to_centroid(datum, clusters)).mean())
    #result = (k, clusters, data.map(lambda datum: dist_to_centroid(datum, clusters)))
    print "Clustering score for k=%(k)d is %(score)f" % {"k": k, "score": result[2]}
    return result



if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print "Usage: /home/spark-1.6.1-bin-hadoop2.4/bin/spark-submit --driver-memory 2g " + \
          "KDD_spark.py max_k corrected"
        sys.exit(1)

    # set up environment
    max_k = int(sys.argv[1])
    data_file = sys.argv[2]
    conf = SparkConf().setAppName("kdd-cup-99") \
    sc = SparkContext(conf=conf)

    # load raw data
    print "Loading RAW data..."
    raw_data = sc.textFile(data_file)

    labels = raw_data.map(lambda line: line.strip().split(",")[-1])

    # Prepare data for clustering input
    # the data contains non-numeric features, we want to exclude them since
    # k-means works with numeric features. These are the first three and the last
    # column in each data row
    print "Parsing dataset..."
    parsed_data = raw_data.map(parse_interaction)
    parsed_data_values = parsed_data.values().cache()

    # Standardize data
    print "Standardizing data..."
    standardizer = StandardScaler(True, True)
    standardizer_model = standardizer.fit(parsed_data_values)
    standardized_data_values = standardizer_model.transform(parsed_data_values)
	
    # Evaluate values of k from 5 to 40
    print "Calculating total in within cluster distance for different k values (10 to %(max_k)d):" % {"max_k": max_k}
    scores = map(lambda k: clustering_score(standardized_data_values, k), range(10, max_k+1, 10))

    # Obtain min score k
    min_k = min(scores, key=lambda x: x[2])[0]
    print "Best k value is %(best_k)d" % {"best_k": min_k}

    # Use the best model to assign a cluster to each datum
    # We use here standardized data - it is more appropriate for exploratory purposes
    print "Obtaining clustering result sample for k=%(min_k)d..." % {"min_k": min_k}
    best_model = min(scores, key=lambda x: x[2])[1]
    
    cluster_assignments_sample = standardized_data_values.map(lambda datum: str(best_model.predict(datum))+","+",".join(map(str,datum)))
    
    # Save assignment sample to file
    print "Saving sample to file..."
    cluster_assignments_sample.saveAsTextFile("sample_standardized")
    labels.saveAsTextFile("labels")
    print "DONE!"
