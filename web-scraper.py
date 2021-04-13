import pandas as pd
import os
import webbrowser

# df = data frame
# get data frame from website and print total number of data frame
dfs = None
while dfs is None:
    try:
      url = str(
        input('Enter website url: ')
        or 'https://en.wikipedia.org/wiki/Minnesota')
      dfs = pd.read_html(url,flavor='bs4')
    except:
      print("No table here!")
      continue
print(f'There are {len(dfs)} tables in this website')

# Filter and display data frame
match = str(
    input('Enter an related string of the table: '))

if match != '':
    df_list = pd.read_html(url, match=f'{match}')

elif match == '':
    table_index = str(
        input(f"You didn't an matching string of the table, enter table index then (from 0 to {len(dfs)-1}): "))
    df_list = pd.read_html(url)

df_list[int(table_index)].to_csv('result.csv',index=False)

a = pd.read_csv("result.csv")
a.to_html("result.html", index=False)

#Html_file= open("result.html","w")
#Html_file.write(html_file)
#Html_file.close()

webbrowser.open('file://' + os.path.realpath("result.html"), new=2)
