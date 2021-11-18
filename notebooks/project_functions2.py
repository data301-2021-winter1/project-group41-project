import pandas as pd

def load_and_process(url_or_path_to_csv_file):
    
    nintiesRecData = pd.read_csv(url_or_path_to_csv_file)
    
    nintiesRecData['avg_across_gen'] = (nintiesRecData['mean_millennial_recognition']*nintiesRecData['mean_gen_z_recognition'])/2 
    
    Mill = (
        nintiesRecData.sort_values(by=['mean_millennial_recognition'])
        .drop('mean_gen_z_recognition',1)
        .drop('avg_across_gen',1)
        .reset_index(drop=True)
    )

    
    GenZ = (nintiesRecData.sort_values(by=['mean_gen_z_recognition'])
    .drop('mean_millennial_recognition',1)
    .drop('avg_across_gen', 1)
    .reset_index(drop=True)
    )
    
    
    Avg = (nintiesRecData.sort_values(by=['avg_across_gen'])
    .drop('mean_gen_z_recognition', 1)
    .drop('mean_millennial_recognition', 1)
    .reset_index(drop=True)
    )
                                
    
    return (Mill, GenZ, Avg) 
    