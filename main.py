import pandas as pd

# Load the data with 'latin1' encoding
df = pd.read_csv('gowtham.csv', encoding='latin1')
df = df.drop('subtypeDescription', axis=1)

for i in range(0,len(df['publicationName'].unique())):
    print(f'''<owl:NamedIndividual rdf:about="http://www.amrita.org/terms#{df["publicationName"][i]}">
            <rdf:type rdf:resource="http://xmlns.com/foaf/0.1/Organization"/>
        </owl:NamedIndividual>''')

for i in range(0, len(df)):
    print('<owl:NamedIndividual rdf:about="http://www.amrita.org/terms#Doc' + str(i) + '">')
    print('<rdf:type rdf:resource="http://purl.org/ontology/bibo/AcademicArticle"/>')
    if df.iloc[i,2] == 'Conference':
        print('<rdf:type rdf:resource="http://purl.org/ontology/bibo/Conference"/>')
    elif df.iloc[i,2] == 'Journal':
        print('<rdf:type rdf:resource="http://purl.org/ontology/bibo/Journal"/>')
    elif df.iloc[i,2] == 'Book':
        print('<rdf:type rdf:resource="http://purl.org/ontology/bibo/Book"/>')
    print(f'<dc:publisher rdf:resource="http://www.amrita.org/terms#{df["publicationName"][i]}"/>')
    if pd.isna(df['volume'][i]) == False:
        print(f'<basic:volume rdf:datatype="http://www.w3.org/2001/XMLSchema#decimal">{df["volume"][i]}</basic:volume>')
    print(f'<dc:issued rdf:datatype="http://www.w3.org/2000/01/rdf-schema#Literal">{df["PublishedDate"][i]}</dc:issued>')
    if pd.isna(df['Pages'][i]) == False:
        print(f'<pages rdf:datatype="http://www.w3.org/2000/01/rdf-schema#Literal">{df["Pages"][i]}</pages>')
    print(f'<dc:description>{df["description"][i]}</dc:description>')
    print(f'<dc:title>{df["title"][i]}</dc:title>')
    # print(f'<amrita:authors rdf:datatype="http://www.w3.org/2000/01/rdf-schema#Literal">{}</amrita:authors>')
    print(f'<amrita:totalCitations rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">{df["citedby_count"][i]}</amrita:totalCitations>')