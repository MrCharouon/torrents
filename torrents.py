 #!/usr/bin/python
import argparse
import webbrowser
import time
parser = argparse.ArgumentParser(description="""Documentation program""", usage="""
      For example:
    \t python main.py -S "House of the Dragon S01E02" """, epilog="and that's how you'd add and remove stocks on your watchlist")
parser.add_argument('-S', action='store', dest='your_input', help='your input in here')
args = parser.parse_args()

try:
    stock_input_add = (args.your_input)
    # print(f'\n{stock_input_add}\n')

    input_args= stock_input_add.replace(" ", "+")
    url1= (f"https://thepiratebay.org/search.php?q={input_args}")
    print(f"{url1}")
    webbrowser.open_new(url1)
    time.sleep(2)
    url2= (f'https://rarbg.to/torrents.php?search={input_args}&order=size&by=ASC')
    print(f"\n{url2}")
    webbrowser.open_new(url2)
    time.sleep(2)
    print('\ndone')

except:
    print("error")





