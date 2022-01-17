import sys

def main():
  print('From docker container running python3 in dev branch')
  print('Hello world')

if __name__ == '__main__':
  print('Argument: ', sys.argv[1])
  main()

