import pandas as pd
REACTIONS = None
JOBS = None 
def load_all_csv():
    global REACTIONS, JOBS
    REACTIONS = pd.read_csv('./data/reactions.csv')
    JOBS = pd.read_csv('./data/jobs.csv')