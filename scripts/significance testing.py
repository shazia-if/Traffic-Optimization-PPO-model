from scipy.stats import ttest_ind, pearsonr, spearmanr
import pandas as pd

# Load the dataset
file_path = "Results/Low Traffic Nonbiased data/without_RL_low_traffic_no_bias_low_traffic.csv"  #  file path
df = pd.read_csv(file_path)

# two groups for comparison (first vs. second half of the dataset)
midpoint = len(df) // 2
group1 = df.loc[:midpoint, 'system_mean_waiting_time']
group2 = df.loc[midpoint:, 'system_mean_waiting_time']

#  t-test
t_stat, p_value_ttest = ttest_ind(group1, group2, equal_var=False)
print(f"T-test results: t-statistic = {t_stat:.4f}, p-value = {p_value_ttest:.4f}")

#  Pearson correlation between speed and waiting time
pearson_corr, p_value_pearson = pearsonr(df['system_mean_speed'], df['system_mean_waiting_time'])
print(f"Pearson correlation: {pearson_corr:.4f}, p-value = {p_value_pearson:.4f}")

#  Spearman correlation (for non-linear relationships)
spearman_corr, p_value_spearman = spearmanr(df['system_mean_speed'], df['system_mean_waiting_time'])
print(f"Spearman correlation: {spearman_corr:.4f}, p-value = {p_value_spearman:.4f}")