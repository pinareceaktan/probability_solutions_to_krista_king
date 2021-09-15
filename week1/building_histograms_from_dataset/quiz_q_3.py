#! /Users/aktan/opt/anaconda3/envs/env-prob/bin/python3.7
import visualization


data_points = [85, 91, 94, 74, 88, 98, 83, 73, 86, 89, 93, 80, 77, 79, 95]
hist = visualization.create_histograms(data_points, lower_bound=70, upper_bound=99, n_bins=4)
