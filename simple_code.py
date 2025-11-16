# Creating a list of dictionaries to accommodate the details of each team member. Each dictionary represents the details of a single team member

team_aspartic = [
    {"Name": "Diksha Shetty", "Slack_username": "Diksha Shetty", "Country":"India", "Hobby": "Reading", "Affiliations": "Bioinformatics", "Favourite_gene": "MYC", "Sequence": "GGAGTTTATTCATAACGCGCTCTCCAAGTATACGTGGCAATGCGTT"},
    {"Name":"Akinjide", "Slack_username": "Akinjide Akinowose", "Country":"Nigeria", "Hobby": "Coding", "Affiliations": "Biomedical informatics", "Favourite_gene": "PTEN", "Sequence": "ATGACAGCCATCATCAAAGAG"},
    {"Name": "Fakhia Mubashir", "Slack_username": "Fakhia Mubashir", "Country":"Pakistan", "Hobby": "Reading", "Affiliations": "None", "Favourite_gene": "TRPV6", "Sequence": "ATCGTCGCCCGATACGATCCAGTA"},
    {"Name": "Funmilayo", "Slack_username": "Funmilayo Christianah Ligali", "Country":"Nigeria", "Hobby": "Cooking", "Affiliations": "Biochemistry", "Favourite_gene": "TP53", "Sequence": "ATGGAGGAGCCGCAGTCAGA"},
    {"Name": "Niraj Pun Magar", "Slack_username": "Niraj Pun Magar", "Country":"Nepal", "Hobby": "UX design", "Affiliations": "Bioinformatics", "Favourite_gene": "APOE", "Sequence": "ATGCATGCGCGCATGC"},
    {"Name": "Himanshu Pundir", "Slack_username": "HIMANSHU PUNDIR", "Country":"India", "Hobby": "Editing", "Affiliations": "Bioinformatics", "Favourite_gene": "SIR1", "Sequence": "ATGTCTATAAAAGGAAAT"},
    {"Name": "Sri Sathya Sandilya Garemilla", "Slack_username": "Garemilla Sandilya", "Country":"United States of America", "Hobby": "Coding", "Affiliations": "Bioinformatics and Molecular Biochemistry", "Favourite_gene": "AP1", "Sequence": "AACCGCATCTGCAGCGAGCATCTGAGAAGCCAAGACTGAGCCGGCGGCCGCGGCGCAGCGAACGAGCAGT"}
]

#Print to see if the list of dictionary is intact
print(team_aspartic)

#Indexing each team member and printing the details of the team members in such a way that each detail comes on a separate line.
#Creating a loop to iterate the command over each dictionary from the list (team_aspartic)
for index, member in enumerate(team_aspartic, start=1):
  print(f"\n ---Team Member {index} ---")
  print(f"Name: {member['Name']}")
  print(f"Slack_username: {member['Slack_username']}")
  print(f"Country: {member['Country']}")
  print(f"Hobby: {member['Hobby']}")
  print(f"Affiliations: {member['Affiliations']}")
  print(f"Favourite_gene: {member['Favourite_gene']}")
  print(f"Sequence: {member['Sequence']}")