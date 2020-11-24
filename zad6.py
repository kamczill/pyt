di = {'one': [1], 'two': [2], 'three': [3], 'four': [4]}
diBackup = di.copy()

di['four'] = 'cztery'

print(di)
print(diBackup)