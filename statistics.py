import math
def calculateStats(numbers):
  if len(numbers) == 0:
      x = float('nan')
      return x
  else:
     return {"avg":sum(numbers)/len(numbers),"max":max(numbers),"min":min(numbers)}
