# Import Library
import csv
import matplotlib.pyplot as plt
# Read CSV

data_dict = []
with open('insurance.csv', 'r', newline='') as insurance_csv:
    insurance_cost = csv.DictReader(insurance_csv)

    for row in insurance_cost:
        row['charges'] = float(row['charges'])
        row['age'] = int(row['age'])
        data_dict.append(row)
    
# print(data_dict)

# Calculate average cost
def calculate_average_cost(data_dict):
    total_cost = 0
    
    for record in data_dict:
        total_cost += record['charges']
        
    average_cost = round(total_cost / len(data_dict), 2)
    
    return {
        'total': total_cost,
        'average': average_cost
    }
    
cost = calculate_average_cost(data_dict)
  
print(f"The total amount people paid for insurance: ${cost['total']:.2f}")
print(f"Average Insurance Costs: ${cost['average']:.2f}")

# Percentage for each cost range
def calculate_cost_percentages(data_dict):
    total_patients = len(data_dict)
    
    # Initialize counter variables for each cost interval
    low_cost_count = 0
    medium_cost_count = 0
    high_cost_count = 0
    
    # Cost classification
    for record in data_dict:
        if record['charges'] < 6000:
            low_cost_count += 1
        elif record['charges'] <= 30000:
            medium_cost_count += 1
        else:
            high_cost_count += 1
    
    # Calculate the percentage for each group
    low_cost_percent = (low_cost_count / total_patients) * 100
    medium_cost_percent = (medium_cost_count / total_patients) * 100
    high_cost_percent = (high_cost_count/ total_patients) * 100
    
    # Returns the results as a dictionary
    return {
        'low_cost_percent': low_cost_percent,
        'medium_cost_percent': medium_cost_percent,
        'high_cost_percent': high_cost_percent
    }

percentages = calculate_cost_percentages(data_dict)
print(f"Percentage of patients with costs less than 6000 USD: {percentages['low_cost_percent']:.2f}%")
print(f"Percentage of patients with costs from 6000 USD to 30000 USD: {percentages['medium_cost_percent']:.2f}%")
print(f"Percentage of patients with costs over 30,000 USD: {percentages['high_cost_percent']:.2f}%")


# Calculate average insurance costs by gender
def cost_by_gender(data_dict):
    total_male = 0
    total_male_cost = 0
    total_female = 0
    total_female_cost = 0
    for record in data_dict:
        if record['sex'] == 'male':
            total_male += 1
            total_male_cost += record['charges']
        elif record['sex'] == 'female':
            total_female += 1
            total_female_cost += record['charges']
            
    average_male_cost = total_male_cost / total_male 
    average_female_cost = total_female_cost/ total_female
    return {
        'average male cost': average_male_cost,
        'average female cost': average_female_cost
    }

average_by_gender = cost_by_gender(data_dict)
print(f"The average insurance cost for men is: ${average_by_gender['average male cost']:.2f}")
print(f"The average insurance cost for women is: ${average_by_gender['average female cost']:.2f}")
    
genders = ['Male', 'Female']
average_costs = [average_by_gender['average male cost'], average_by_gender['average female cost']]

# Draw a chart
plt.bar(genders, average_costs, color=['blue', 'pink'])
plt.title('Average Insurance Cost by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Cost (USD)')
plt.show()

# Classify costs by age and gender
def cost_by_age_and_gender(data_dict):
    age_groups = {
        '18-25': {'male': {'total_cost': 0, 'count': 0}, 'female': {'total_cost': 0, 'count': 0}},
        '26-35': {'male': {'total_cost': 0, 'count': 0}, 'female': {'total_cost': 0, 'count': 0}},
        '36-45': {'male': {'total_cost': 0, 'count': 0}, 'female': {'total_cost': 0, 'count': 0}},
        '46-55': {'male': {'total_cost': 0, 'count': 0}, 'female': {'total_cost': 0, 'count': 0}},
        '56-65': {'male': {'total_cost': 0, 'count': 0}, 'female': {'total_cost': 0, 'count': 0}}
    }
    
    # Classify data into groups
    for record in data_dict:
        age = record['age']
        sex = record['sex']
        cost = record['charges']
    
        if age >= 18 and age <= 25:
            age_groups['18-25'][sex]['total_cost'] += cost
            age_groups['18-25'][sex]['count'] += 1
        elif age >= 26 and age <= 35:
            age_groups['26-35'][sex]['total_cost'] += cost
            age_groups['26-35'][sex]['count'] += 1
        elif age >= 36 and age <= 45:
            age_groups['36-45'][sex]['total_cost'] += cost
            age_groups['36-45'][sex]['count'] += 1
        elif age >= 46 and age <= 55:
            age_groups['46-55'][sex]['total_cost'] += cost
            age_groups['46-55'][sex]['count'] += 1
        elif age >= 56 and age <= 65:
            age_groups['56-65'][sex]['total_cost'] += cost
            age_groups['56-65'][sex]['count'] += 1
        else:
            continue
    
    for group, data in age_groups.items():
        for sex, value in data.items():
            count = value['count']
            value['average_cost'] = round(value['total_cost'] / count, 2)
    
    return age_groups

age_gender_data = cost_by_age_and_gender(data_dict)
# print(age_gender_data)

age_labels = list(age_gender_data.keys())
male_costs = [age_gender_data[age]['male']['average_cost'] for age in age_labels]
female_costs = [age_gender_data[age]['female']['average_cost'] for age in age_labels]

# Draw a chart
plt.figure(figsize=(15, 8))
plt.plot(age_labels, male_costs, label='Male', marker='o', color='blue')
plt.plot(age_labels, female_costs, label='Female', marker='o', color='pink')
plt.title("Average Insurance Cost by Age and Gender")
plt.xlabel('Age Group')
plt.ylabel('Average Cost (USD)')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Analyze factors that affect insurance costs
def calculate_average_cost_by_smoking_status(data_dict):
    smoker_cost = 0
    non_smoker_cost = 0
    smoker_count = 0
    non_smoker_count = 0
    for record in data_dict:
        if record['smoker'] == 'yes':
            smoker_cost += record['charges']
            smoker_count += 1
        elif record['smoker'] == 'no':
            non_smoker_cost += record['charges']
            non_smoker_count += 1
    
    avg_smoker_cost = smoker_cost / smoker_count
    avg_non_smoker_cost = non_smoker_cost / non_smoker_count
    return avg_smoker_cost, avg_non_smoker_cost, smoker_count, non_smoker_count

# Function to draw a chart
def plot_comparison(avg_smoker_cost, avg_non_smoker_cost, smoker_count, non_smoker_count):
    labels = ['Smoker', 'Non-Smoker']
    costs = [avg_smoker_cost, avg_non_smoker_cost]
    counts = [smoker_count, non_smoker_count]
    
    # Draw a chart
    plt.figure(figsize=(15, 8))
    plt.bar(labels, costs, color=['blue', 'green'], alpha=0.8)
    plt.twinx()
    plt.bar(labels, counts, color=['blue', 'green'], alpha=0.3, width=0.4)
    plt.title('Comparison of Insurance Cost: Smoker vs Non-Smoker')
    plt.xlabel('Group')
    plt.ylabel('Average Insurance Cost (USD)', color='black')
    plt.ylabel('Count of Individuals', color='grey')
    plt.show()

# Function to calculate average cost by number of children
def calculate_average_cost_by_children(data_dict):
    children_cost = {}
    children_count = {}
    
    for record in data_dict:
        num_children = record['children']
        cost = float(record['charges'])
        
        if num_children in children_cost:
            children_cost[num_children] += cost
            children_count[num_children] += 1
        else:
            children_cost[num_children] = cost
            children_count[num_children] = 1
    
    average_cost_by_children = {}
    for num_children in children_cost:
        average_cost_by_children[num_children] = children_cost[num_children] / children_count[num_children]
        
    return average_cost_by_children

# Function to draw a chart
def plot_comparison_children(average_costs_by_children):
    num_childrens = list(average_costs_by_children.keys())
    avg_costs = list(average_costs_by_children.values())

    plt.figure(figsize=(10, 6))
    plt.bar(num_childrens, avg_costs, color='skyblue')
    plt.title('Average Insurance Cost by Number of Children')
    plt.xlabel('Number of Children')
    plt.ylabel('Average Insurance Cost (USD)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


if __name__ == "__main__":

    # Average Cost by Smoker
    avg_smoker_cost, avg_non_smoker_cost, smoker_count, non_smoker_count = calculate_average_cost_by_smoking_status(data_dict)
    print(f"Average cost for smokers: ${avg_smoker_cost:.2f}")
    print(f"Average cost for non-smokers: ${avg_non_smoker_cost:.2f}")
    
    # Average Cost by Children
    average_costs_by_children = calculate_average_cost_by_children(data_dict)
    for num_children, avg_cost in average_costs_by_children.items():
        print(f"Average cost for {num_children} children: ${avg_cost:.2f}")
    
    # Draw a comparison chart
    plot_comparison(avg_smoker_cost, avg_non_smoker_cost, smoker_count, non_smoker_count)
    plot_comparison_children(average_costs_by_children)
    

    
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            





