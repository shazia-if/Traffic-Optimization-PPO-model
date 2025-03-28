import pandas as pd

def calculate_optimization_score(csv_path, output_path):
    # Load the CSV file
    df = pd .read_csv(csv_path)
    
    # Calculate max values for normalization
    max_speed_limit = df['system_mean_speed'].max()
    max_vehicles = df['system_total_stopped'].max()
    max_waiting_time = df['system_total_waiting_time'].max()
    max_mean_wait = df['system_mean_waiting_time'].max()
    
    # optimization score
    df['optimization_score'] = (
        (df['system_mean_speed'] / max_speed_limit) * 0.6 -
        (df['system_total_stopped'] / max_vehicles) * 0.2 -
        (df['system_total_waiting_time'] / max_waiting_time) * 0.1 -
        (df['system_mean_waiting_time'] / max_mean_wait) * 0.1
    )
    
    # Categorizing optimization levels
    def categorize(score):
        if score > 0.6:
            return 'Excellent'
        elif 0.3 <= score <= 0.6:
            return 'Good'
        elif 0 <= score < 0.3:
            return 'Moderate'
        elif -0.3 <= score < 0:
            return 'Poor'
        else:
            return 'Critical'
    
    df['optimization'] = df['optimization_score'].apply(categorize)
    
    # Save modified DataFrame
    df.to_csv(output_path, index=False)
    
    # Count occurrences of each category
    category_counts = df['optimization'].value_counts()
    total_rows = len(df)
    category_percentages = (category_counts / total_rows) * 100
    
    # Print category statistics
    for category, count in category_counts.items():
        percentage = category_percentages[category]
        print(f"{category}: {count} rows ({percentage:.2f}%)")
    
    # Determine overall optimization
    most_frequent_category = category_percentages.idxmax()
    if category_percentages.max() >= 75:
        print(f"Overall Optimization: {most_frequent_category}")
    else:
        print("Overall Optimization: Mixed Performance")

list_of_results= ['Results/Extra HeavyTraffic biased data/ppo_testing_Against_extra_heavy_traffic_biased.csv', 
                  'Results/Extra HeavyTraffic biased data/without_RL_on_extra_heavy_traffic_bias_data.csv',
                  'Results/Extra HeavyTraffic Nonbiased data/ppo_testing_Against_extra_heavy_traffic.csv',
                  'Results/Extra HeavyTraffic Nonbiased data/without_RL_extra_heavy_traffic_no_bias_fixed_policy.csv',
                  'Results/Heavy traffic Biased data/with ppo_heavy traffic_biased_data.csv',
                  'Results/Heavy traffic Biased data/without_RL_on_heavy_traffic_bias_data.csv',
                  'Results/Heavy Traffic Nonbiased data (Training data)/ppo_testing_Against_training_data_heavy_biased.csv',
                  'Results/Heavy Traffic Nonbiased data (Training data)/without_RL_ON_Training_data_heavy_biased.csv',
                  'Results/Low traffic Biased data/ppo_testing_Against_low_traffic_biased.csv',
                  'Results/Low traffic Biased data/without_RL_on_low_traffic_bias_data.csv',
                  'Results/Low Traffic Nonbiased data/ppo_testing_Against_low_traffic_no_bias_data.csv',
                  'Results/Low Traffic Nonbiased data/without_RL_low_traffic_no_bias_low_traffic.csv'
                  ]

# Example usage
#input_file = "/mnt/data/ppo_testing_Against_extra_heavy_traffic_biased_conn1_ep1.csv"
#output_file = "/mnt/data/optimized_output.csv"
#calculate_optimization_score(input_file, output_file)


for i in range(12):
    input_file = list_of_results[i]
    output_file= f"{list_of_results[i]}_optimization_data.csv"
    print("logging for:", input_file, "saving in", output_file)
    calculate_optimization_score(input_file, output_file)


