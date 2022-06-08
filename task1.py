import pandas as pd
import collections
import loader

def task1():
    loader.load_all_csv()
    reactions = loader.REACTIONS
    userGraph = collections.defaultdict(list)
    dataset = reactions.loc[reactions.direction == True]
    dataset = dataset.drop_duplicates(subset=['user_id', 'job_id'])

    for user in dataset.user_id:
        jobs = dataset.job_id.loc[dataset.user_id == user].tolist()
        userGraph[user] = jobs

    user1 = 0
    user2 = 0
    max_sim = 0
    for i in userGraph:
        for j in userGraph:
            if i == j:
                continue
            common = list(set(userGraph[i]).intersection(userGraph[j]))
            # print(common)
            if len(common) > max_sim:
                max_sim = len(common)
                user1 = i
                user2 = j
    print(f'Similarity between user1: {user1} and user2: {user2} is {max_sim}')


if __name__ == '__main__':
    task1()
