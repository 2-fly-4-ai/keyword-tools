import pandas as pd
import os
import datetime 
from jinja2 import Template
import gzip
 
# Import List of URLs
list_of_urls = pd.read_csv('2023-02-15-product_tag-01c44a33-3af2-0a24-67bd-d944c3cf7205.csv')
list_of_urls
 
# Set-Up Maximum Number of URLs (recommended max 50,000)
n = 25000
 
# Create New Empty Row to Store the Splitted File Number
list_of_urls.loc[:,'name'] = ''
 
# Split the file with the maximum number of rows specified
new_df = [list_of_urls[i:i+n] for i in range(0,list_of_urls.shape[0],n)]
 
# For Each File Created, add a file number to a new column of the dataframe
for i,v in enumerate(new_df):
    v.loc[:,'name'] = str(v.iloc[0,1])+'_'+str(i)
    print(v)
             
# Create a Sitemap Template to Populate
 
sitemap_template='''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    {% for page in pages %}
    <url>
        <loc>{{page[1]|safe}}</loc>
        <lastmod>{{page[3]}}</lastmod>
        <changefreq>{{page[4]}}</changefreq>
        <priority>{{page[5]}}</priority>        
    </url>
    {% endfor %}
</urlset>'''
 
template = Template(sitemap_template)
 
# Get Today's Date to add as Lastmod
lastmod_date = datetime.datetime.now().strftime('%Y-%m-%d')
 
# Fill the Sitemap Template and Write File
for i in new_df:                           # For each URL in the list of URLs ...                                                          
    i.loc[:,'lastmod'] = lastmod_date      # ... add Lastmod date
    i.loc[:,'changefreq'] = 'daily'        # ... add changefreq
    i.loc[:,'priority'] = '1.0'            # ... add priority 
 
    # Render each row / column in the sitemap
    sitemap_output = template.render(pages = i.itertuples()) 
     
    # Create a filename for each sitemap like: sitemap_0.xml.gz, sitemap_1.xml.gz, etc.
    filename = 'product_tag-sitemap' + str(i.iloc[0,1]) + '.xml.gz'
 
    # Write the File to Your Working Folder
    with open(filename, 'wt') as f:   
        f.write(sitemap_output)