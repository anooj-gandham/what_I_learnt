import pandas as pd
import numpy as np

def subheading(h):
    return '<h3>'+h+'</h3>'

def li(folder,file,desc,date):
    desc = desc.replace('-',',')
    return '<li><a href="./'+folder+'/'+file+'">'+desc+'</a> '+date+'</li>'




all = pd.read_csv('all.csv')

folders,file_count = np.unique(all.folder_name,return_counts=True)

body = '<body><h1>What I learnt till now</h1>'
for i in range(len(folders)):
    sub_h = subheading(folders[i])
    rows = all[all.folder_name==folders[i]]
    listitems = ''
    for j in (rows.index.values):
        listitems = listitems + li(rows.loc[j].folder_name,rows.loc[j].file_name,rows.loc[j].description,rows.loc[j].dates)
    body = body + sub_h+'<ul>'+listitems+'</ul>'

body = body + '</body>'

head = '<html><head><link rel="stylesheet" href="style.css"/><title>What I Learnt.</title></head>' + body + '</html>'

html = open('index.html','w')

html.write(head)
html.close()