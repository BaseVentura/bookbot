PATH_TO_FILE = 'books/frankenstein.txt'

def main():
  with open(PATH_TO_FILE) as f:
    file_contents = f.read()
    words = get_words(file_contents)
    sorted = create_char_list(count_characters(file_contents))
    sorted.sort(reverse=True, key=sort_on)
    print_report(PATH_TO_FILE, words, sorted)
    

def print_report(file: str, number_words: int, char_count: list[dict[str,int]])->None:
  print(f'===== start of report for {file} =====')
  print(f'{number_words} words found in document.')
  for entry in char_count: 
    print(f"The character '{entry['char']}' was used {entry['count']} times.")
  print(f'=========== end of report ============')


def sort_on(dict):
    return dict["count"] 

def get_words(text: str)-> int:
  return len(text.split())

def create_char_list(dict: dict[str, int]) -> list[dict[str,int]]:
  list = []
  for char in dict.keys():
    list.append({"char": char, 'count': dict[char]}) 
  return list


def count_characters(text: str) -> dict[str, int]:
  count_map = {}

  for character in text:
    lower = character.lower()
    if lower.isalpha():
      if lower in count_map:
        count_map[lower] += 1
      else: 
        count_map[lower] = 0

  return count_map
main()