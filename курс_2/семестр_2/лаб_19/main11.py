import z31

def main():

  list_a = [1, 5, 3, 8, 2, 8, 4]

  max_element = z31.find_max_element(list_a)
  count_max = z31.count_max_elements(list_a)

  print(f"Максимальный элемент в списке {list_a}: {max_element}")
  print(f"Количество максимальных элементов в списке: {count_max}")

if __name__ == "__main__":
  main()
