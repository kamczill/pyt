import copy

di = {'one': [1], 'two': [2], 'three': [3], 'four': [4]}
diBackup = copy.deepcopy(di)

di['four'][0] = 'cztery'

print(di)
print(diBackup)