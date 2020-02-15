
use_cols = [
    'loan_amnt', 'int_rate', 'annual_inc', 'open_acc', 'loan_status',
    'open_il_12m'
]

data = pd.read_csv(
    'loan.csv', usecols=use_cols).sample(
        10000, random_state=44)  # set a seed for reproducibility
