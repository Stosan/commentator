key="WggnOxa5VgqEAWlvXLDDaod0Eq4MUPnEqUCwhqhIze6AR5GbxndNTmL_QUJvJPCnlWbadA."
from bardapi import Bard

token = key
bard = Bard(token=token,timeout=30)
code = '''
what is goal
'''
print(bard.get_answer(f"{code}")['content'])