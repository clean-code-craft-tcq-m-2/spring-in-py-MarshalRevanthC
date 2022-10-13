def calculateStats(numbers):
  if len(numbers) == 0 :
      x = float('nan')
      return x
  else:
      avg = sum(numbers)/len(numbers)
      max = max(numbers)
      min = min(numbers)
      return avg , max , min
