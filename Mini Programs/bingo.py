import random
import pandas as pd

def generate_bingo_card():
    
    return {'B': [random.randint(1, 15) for x in range(0,5)], 'I': [random.randint(16, 30) for x in range(0,5)],
            'N': [random.randint(31, 45) if x != 2 else "" for x in range(0,5)],"G": [random.randint(46, 60) for x in range(0,5)], 
            "O":[random.randint(61, 75) for x in range(0,5)]}

df = pd.DataFrame(generate_bingo_card())

print(df)