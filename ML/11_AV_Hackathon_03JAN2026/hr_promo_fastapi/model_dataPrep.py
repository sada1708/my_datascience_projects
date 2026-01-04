def data_prep(df):
    import pandas as pd
    trainX = pd.read_csv('trainx.csv')
    rules = {
        'edu_mode' : trainX['education'].mode()[0],
        'dept_count': trainX['department'].value_counts().to_dict(),
        'region_count': trainX['region'].value_counts().to_dict()

    }
    data = df.copy()

    data['education'] = data['education'].fillna(rules['edu_mode'])
    data['previous_year_rating'] = data['previous_year_rating'].fillna(0)

    data['total_score'] = data['no_of_trainings'] * data['avg_training_score']
    data['is_high_performer'] = ((data['KPIs_met >80%'] == 1) & (data['awards_won?'] == 1)).astype(int)

    data['education'] = data['education'].map({"Below Secondary": 1, "Bachelor's": 2, "Master's & above": 3})
    data['gender'] = data['gender'].map({'f': 0, 'm': 1})

    data['dept_size'] = data['department'].map(rules['dept_count']).fillna(0)
    data['region_size'] = data['region'].map(rules['region_count']).fillna(0)

    return data.drop(columns=['department', 'region', 'recruitment_channel'])