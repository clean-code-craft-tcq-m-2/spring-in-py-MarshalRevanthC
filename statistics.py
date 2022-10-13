def calculateStats(numbers):
  if len(numbers) == 0 :
      return float("None")
  else:
      avg = sum(numbers)/len(numbers)
      max = max(numbers)
      min = min(numbers)
      return avg, max, min
