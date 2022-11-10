import os

import View

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'secret.json'
def main():
    View.View()

if __name__ == '__main__':
    main()
