import pandas as pd
import os
import webbrowser

# df = data frame
url = str(
    input('Enter website url: ')
    or 'https://en.wikipedia.org/wiki/Minnesota')

dfs = pd.read_html(url)
print(f'There are {len(dfs)} tables in this website')

match = str(
    input('Enter an matching string of the table: ')
    or 'Election results from statewide races')

df_list = pd.read_html('https://en.wikipedia.org/wiki/Minnesota', match=f'{match}')
df_list[0].to_csv('result.csv',index=False)

a = pd.read_csv("result.csv")
html_file = a.to_html(index=False)

Html_file= open("result.html","w")
Html_file.write(html_file)
Html_file.close()

webbrowser.open('file://' + os.path.realpath("result.html"), new=2)
