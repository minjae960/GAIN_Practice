'''Main function for UCI letter and spam datasets.
'''

# Necessary packages
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import numpy as np
from scipy import stats

from data_loader import data_loader
from gain import gain
from utils import rmse_loss
from utils import knn

def main (args):
  '''Main function for UCI letter and spam datasets.
  
  Args:
    - data_name: letter or spam
    - miss_rate: probability of missing components
    - batch:size: batch size
    - hint_rate: hint rate
    - alpha: hyperparameter
    - iterations: iterations
    
  Returns:
    - imputed_data_x: imputed data
    - rmse: Root Mean Squared Error
  '''
  
  data_name = args.data_name
  miss_rate = args.miss_rate
  data_type = args.data_type
  
  gain_parameters = {'batch_size': args.batch_size,
                     'hint_rate': args.hint_rate,
                     'alpha': args.alpha,
                     'iterations': args.iterations}
  
  # Load data and introduce missingness
  ori_data_x, miss_data_x, data_m = data_loader(data_name, miss_rate, data_type)
  
  # Impute missing data(GAIN)
  imputed_data_x = gain(miss_data_x, gain_parameters, data_type)

  # Impute missing data(KNN)
  min_vector = np.nanmin(miss_data_x, axis=0)
  max_vector = np.nanmax(miss_data_x, axis=0)

  knn_norm_x = (miss_data_x - min_vector) / (max_vector - min_vector)
  knn_data_x = knn(knn_norm_x, 3)
  knn_data_x = knn_data_x * (max_vector - min_vector) + min_vector
  
  # Report the RMSE performance
  rmse = rmse_loss(ori_data_x, imputed_data_x, data_m)
  rmse_knn = rmse_loss(ori_data_x, knn_data_x, data_m)

  print()
  print('GAIN RMSE Performance: ' + str(np.round(rmse, 4)))
  print('KNN RMSE Performance: ' + str(np.round(rmse_knn, 4)))

  # r-square values of GAIN and KNN
  REAL = ori_data_x[data_m == 0]
  GAIN_imputed = imputed_data_x[data_m == 0]
  KNN_imputed = knn_data_x[data_m == 0]

  slope_GAIN, intercept_GAIN, r_value_GAIN, p_value_GAIN, std_err_GAIN = stats.linregress(REAL, GAIN_imputed)
  slope_KNN, intercept_KNN, r_value_KNN, p_value_KNN, std_err_KNN = stats.linregress(REAL, KNN_imputed)

  print()
  print('GAIN r-square value is', round(r_value_GAIN ** 2, 4))
  print('KNN r-square value is', round(r_value_KNN ** 2, 4))

  return ori_data_x, miss_data_x, data_m, imputed_data_x, knn_data_x, REAL, GAIN_imputed, KNN_imputed

if __name__ == '__main__':  
  
  # Inputs for the main function
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '--data_name',
      choices=['letter','spam', 'pm', 'pm_wthr'],
      default='pm',
      type=str)
  parser.add_argument(
      '--miss_rate',
      help='missing data probability',
      default=0.2,
      type=float)
  parser.add_argument(
      '--data_type',
      help='data type',
      choices=['ocec', 'ele', 'ion', 'ocec+ele', 'ocec+ion', 'ele+ion', 'all'],
      default='ocec',
      type=str)
  parser.add_argument(
      '--batch_size',
      help='the number of samples in mini-batch',
      default=1000,
      type=int)
  parser.add_argument(
      '--hint_rate',
      help='hint probability',
      default=0.9,
      type=float)
  parser.add_argument(
      '--alpha',
      help='hyperparameter',
      default=100,
      type=float)
  parser.add_argument(
      '--iterations',
      help='number of training interations',
      default=10000,
      type=int)
  
  args = parser.parse_args() 
  
  # Calls main function  
  ori_data_x, miss_data_x, data_m, imputed_data_x, knn_data_x, REAL, GAIN, KNN = main(args)