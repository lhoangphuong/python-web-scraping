import pandas as pd
import os
import webbrowser

table_MN = pd.read_html('https://en.wikipedia.org/wiki/Minnesota')

df_list = pd.read_html('https://en.wikipedia.org/wiki/Minnesota', match='Election results from statewide races')
df_list[0].to_csv('Election_result.csv',index=False)

a = pd.read_csv("Election_result.csv")
html_file = a.to_html(index=False)

Html_file= open("test.html","w")
Html_file.write(html_file)
Html_file.close()

url = "file:///D:/test/test.html"
webbrowser.open(url,new=2)
