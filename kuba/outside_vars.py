import numpy as np
from scipy.stats import shapiro, normaltest
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr

def fill_hc_nan_values(df):
    # UPDRS III range guess (Can't find anything more precise than to just guess upper bound for now)
    UPDRS_HC_RANGE = (0, 5)
    UPDRS_HC_MEAN = np.mean(UPDRS_HC_RANGE)
    UPDRS_HC_STD = (UPDRS_HC_RANGE[1] - UPDRS_HC_RANGE[0]) / 4 # Approx 95% within range
    
    # MoCA mean and variance for healthy controls to replace NaN values in data
    # from: https://mocacognition.com/moca-clinic-data/
    # NO IDEA ABOUT SAMPLE SIZE FOR THESE ESTIMATES
    # (maybe it's there, but I doubt it's critical)
    MOCA_HC_MEAN = 27.4
    MOCA_HC_STD = 2.2
    MOCA_HC_CUTOFF = 26 # >= 26 means healthy
    MOCA_HC_RANGE = (25.2, 30)    # using 30 upper bound, no idea why the website states 29.6
    
    def generate_clamped_data(mean, std, value_range, size):
        data = np.random.normal(mean, std, size)
        return np.clip(data, value_range[0], value_range[1]) # constrain bounds of values

    hc_rows = df['group'].str.startswith('HC')
    
    # Generate MoCA values for HC
    moca_nan_indices = df.loc[hc_rows, 'MoCA'].index[df.loc[hc_rows, 'MoCA'].isna()]
    df.loc[moca_nan_indices, 'MoCA'] = generate_clamped_data(
        MOCA_HC_MEAN, MOCA_HC_STD, MOCA_HC_RANGE, len(moca_nan_indices)
    )
    
    # Generate UPDRS III values for HC
    updrs_nan_indices = df.loc[hc_rows, 'UPDRS_III'].index[df.loc[hc_rows, 'UPDRS_III'].isna()]
    df.loc[updrs_nan_indices, 'UPDRS_III'] = generate_clamped_data(
        UPDRS_HC_MEAN, UPDRS_HC_STD, UPDRS_HC_RANGE, len(updrs_nan_indices)
    )
    
    return df

column_map = {
    'group': 'Patient Group',
    'age': 'Age (years)',
    'MoCA': 'MoCA',
    'UPDRS_III': 'UPDRS III',
    'ha_rt': 'Horizontal Antisaccade Reaction Time',
    'ha_err': 'Horizontal Antisaccade Error',
    'va_rt': 'Vertical Antisaccade Reaction Time',
    'va_err': 'Vertical Antisaccade Error',
    'hpr_rt': 'Horizontal Prosaccade Right Reaction Time',
    'hpr_avgv': 'Horizontal Prosaccade Right Average Speed',
    'hpr_maxv': 'Horizontal Prosaccade Right Max Speed',
    'hpr_gain': 'Horizontal Prosaccade Right Gain',
    'hpl_rt': 'Horizontal Prosaccade Left Reaction Time',
    'hpl_avgv': 'Horizontal Prosaccade Left Average Speed',
    'hpl_maxv': 'Horizontal Prosaccade Left Max Speed',
    'hpl_gain': 'Horizontal Prosaccade Left Gain',
    'vpu_rt': 'Vertical Prosaccade Up Reaction Time',
    'vpu_avgv': 'Vertical Prosaccade Up Average Speed',
    'vpu_maxv': 'Vertical Prosaccade Up Max Speed',
    'vpu_gain': 'Vertical Prosaccade Up Gain',
    'vpd_rt': 'Vertical Prosaccade Down Reaction Time',
    'vpd_avgv': 'Vertical Prosaccade Down Average Speed',
    'vpd_maxv': 'Vertical Prosaccade Down Max Speed',
    'vpd_gain': 'Vertical Prosaccade Down Gain'
}


def mass_sw_test(df):
    groups = df['group'].unique()
    numeric_data = df.drop(columns=['group'])

    results_df = pd.DataFrame(index=groups, columns=numeric_data.columns)

    for group in groups:
        group_data = df[df['group'] == group]

        for column in numeric_data.columns:
            stat, p_value = shapiro(group_data[column].dropna())  # drop NaNs
            normal = "Normal" if p_value > 0.05 else "Not Normal"
            results_df.loc[group, column] = normal

    return results_df


def compute_correlations(df, y_var, normality_df):
    results = []
    groups = df['group'].unique()
    
    
    for group in groups:
        group_data = df[df['group'].str.startswith(group)]
        numeric_data = group_data.drop(columns=['group'])
        for column in numeric_data.columns:
            if column == y_var:  # skip dependent variable
                continue

            if column not in normality_df.columns:
                continue  # skip if the column isn't in the normality test results

            x = group_data[column].dropna()
            y = group_data[y_var].dropna()

            aligned_data = pd.concat([x, y], axis=1).dropna()
            x = aligned_data[column]
            y = aligned_data[y_var]

 
            normal_x = normality_df.loc[group, column]
            normal_y = normality_df.loc[group, y_var]


            if normal_x == 'Normal' and normal_y == 'Normal':
                method = 'Pearson'
                corr, p_value = pearsonr(x, y)
            else:
                method = 'Spearman'
                corr, p_value = spearmanr(x, y)

            if p_value < 0.005:
                stars = '***'
            elif p_value < 0.01:
                stars = '**'
            elif p_value < 0.05:
                stars = '*'
            else:
                stars = 'ns'

            results.append({
                'Group': group,
                'Feature': column,
                'Correlation Coefficient': corr,
                'P-value': stars,
                #'Method': method
            })
    
    return pd.DataFrame(results)


