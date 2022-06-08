import pandas as pd
import collections
import loader


def task2():
    loader.load_all_csv()
    reactions = loader.REACTIONS
    companies = loader.JOBS
    companies_db = reactions.merge(companies, how='inner', on='job_id')

    company_graph = collections.defaultdict(list)
    dataset = companies_db.loc[companies_db.direction == True]

    dataset = dataset.drop_duplicates(
        subset=['user_id', 'job_id', 'company_id'])

    for c in dataset.company_id:
        users = dataset.user_id.loc[dataset.company_id == c].tolist()
        company_graph[c] = users

    company1 = 0
    company2 = 0
    max_sim = 0
    for i in company_graph:
        for j in company_graph:
            if i == j:
                continue
            common = list(set(company_graph[i]).intersection(company_graph[j]))
            if len(common) > max_sim:
                max_sim = len(common)
                company1 = i
                company2 = j
    print(
        f'Similarity between company1: {company1} and company2: {company2} is {max_sim}')


if __name__ == '__main__':
    task2()
