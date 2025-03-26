from stats import count_word_report
import sys

try:
  count_word_report("./"+sys.argv[1])
    
except:
  print("Usage: python3 main.py <path_to_book>")
  sys.exit(main())

#print(count_word_report("./books/frankenstein.txt"));