import seaborn as sns
import matplotlib.pyplot as plt

def scatter_plots(df, y_var, correlation_results):

    def group_color(group):
        if group.startswith('PD'):
            return 'blue'
        elif group.startswith('RBD'):
            return 'red'
        elif group.startswith('HC'):
            return 'green'
        else:
            return 'gray'  # unexpected vals
    
    columns_to_plot = [col for col in df.columns if col not in ['group', y_var]]
    
    plt.figure(figsize=(12, 12))
    plt.suptitle(f"Correlations for {y_var}", fontsize=20)
    for i, column in enumerate(columns_to_plot, 1):
        plt.subplot(5,5, i) # CHANGE
        stars_per_group = []
        for group in ['PD', 'RBD', 'HC']:
            p_value = correlation_results.loc[(correlation_results['Feature'] == column) & 
                                              (correlation_results['Group'] == group), 'P-value'].values[0]
            
            stars_per_group.append(f'{group} ({p_value})')

        title = ', '.join(stars_per_group)
        plt.title(title, fontsize=10)
        
        sns.scatterplot(
            data=df,
            x=column,
            y=y_var,
            hue=df['group'].map(group_color),
            palette=None,
            legend=None
        )
        
        plt.xlabel(column)
        plt.ylabel(y_var)
    
    plt.tight_layout()
    plt.show()