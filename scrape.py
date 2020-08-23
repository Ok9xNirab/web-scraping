import requests
import pandas
from requests_html import HTML

url = "https://www.boxofficemojo.com/year/?ref_=bo_nb_hm_secondarytab"


def url_to_file(url):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        return html_text
    return


html_txt = url_to_file(url)
r_html = HTML(html=html_txt)
table_id = "#table"
r_table = r_html.find(table_id)

if len(r_table) == 1:
    parsed_table = r_table[0]
    rows = parsed_table.find("tr")
    header_row = rows[0]
    header_cols = header_row.find("th")
    header_names = [x.text for x in header_cols]
    table_data = []
    for row in rows[1:]:
        cols = row.find("td")
        row_data = []
        for i, col in enumerate(cols):
            row_data.append(col.text)
        table_data.append(row_data)
    df = pandas.DataFrame(table_data, columns=header_names)
    df.to_csv('movies.csv', index=False)
