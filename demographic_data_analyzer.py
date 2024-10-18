import pandas as pd


def calculate_demographic_data(print_data=True):
df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    men=df[df['sex']=='Male']
    average_age_men =men['age'].mean()
    average_age_men=round(average_age_men,1)

    # What is the percentage of people who have a Bachelor's degree?
    bacheor=df[df['education']=='Bachelors'].shape[0]
    total=df.shape[0]
    percentage_bachelors = (bacheor/total) * 100
    percentage_bachelors=round(percentage_bachelors,1)


    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[(df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate')]
    lower_education = df[~((df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate'))]
    

    # percentage with salary >50K
    high=higher_education[higher_education['salary'] == '>50K'].shape[0]
    low=lower_education[lower_education['salary'] == '>50K'].shape[0]
    higher_education_rich = (high/higher_education.shape[0]) * 100
    lower_education_rich = (low/lower_education.shape[0]) *100
    higher_education_rich=round(higher_education_rich,1)
    lower_education_rich=round(lower_education_rich,1)


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers= df[(df['hours-per-week']== min_work_hours) & (df['salary'] == '>50K')].shape[0]
    total_sal=df[df['hours-per-week']==min_work_hours].shape[0]
    
    rich_percentage = (min_workers/total_sal)*100
    rich_percentage=round(rich_percentage,1)


    # What country has the highest percentage of people that earn >50K?
    high_earn= df[df['salary']=='>50K']
    countt= high_earn['native-country'].value_counts()
    count_total = df['native-country'].value_counts()
    percentage_high_earn = (countt / count_total) * 100
    highest_earning_country = percentage_high_earn.idxmax()
    highest_earning_country_percentage = percentage_high_earn.max()
    highest_earning_country_percentage=round(highest_earning_country_percentage,1)


    # Identify the most popular occupation for those who earn >50K in India.
    pop=df[(df['native-country']=='India') & (df['salary']=='>50K')]
    count_pop= pop['occupation'].value_counts()
    top_IN_occupation = count_pop.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }