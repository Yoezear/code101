def quick_sort(arr, low, high):
  if low < high:
    pi = partition(arr, low, high)
    quick_sort(arr, low, pi-1)
    quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
  pivot = arr[high]
  i = low - 1

  for j in range(low, high):
    if arr[j] <= pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  return i + 1

def main():
  numbers = list(map(int, input("Enter integers separated by spaces: ").split()))
  quick_sort(numbers, 0, len(numbers) - 1)

  print("Sorted array:", numbers)
  target = int(input("Enter a target element to search: "))
  replacement = int(input("Enter a replacement element: "))
  for i in range(len(numbers)):
    if numbers[i] == target:
      numbers[i] = replacement

  print("Modified array:", numbers)

if __name__ == "__main__":
  main()  
