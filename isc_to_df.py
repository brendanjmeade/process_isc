import glob
import pdb
import time
import pandas as pd


def file_to_df(file_name):
    '''Read single .csv file and convert to a dataframe'''
    keep_column_index = [0, 1, 2, 3, 4, 10, 11, 12]
    df = pd.read_csv(file_name, header=None, usecols=keep_column_index)
    df.columns = ['source', 'date_time_string', 'latitude', 'longitude',
                  'depth', 'magnitude_author', 'magnitude', 'magnitude_type']
    df['datetime'] = pd.to_datetime(df.date_time_string)
    return df


def main():
    '''Read all .csv files in dir_name, convert to dataframe, and save'''
    dir_name = 'COMPCATCSV'
    df_file_name = 'isc_comp'
    file_names = glob.glob(dir_name + '/*.csv')
    file_names.sort()
    for i in range(0, len(file_names)):
        print 'Converting ' + file_names[i]
        df_current = file_to_df(file_names[i])
        if i == 0:
            df = df_current
        if i > 0:
            df = pd.concat([df, df_current])

    df = df.drop('date_time_string', axis=1)
    df.to_csv(df_file_name + '.csv')
    df.to_pickle(df_file_name + '.pkl')

    t0 = time.time()
    df = pd.read_pickle(df_file_name + '.pkl')
    t1 = time.time()
    print t1 - t0


if __name__ == '__main__':
    main()
