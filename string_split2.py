authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"
author_names = authors.split(",")
print(author_names)
author_names_split = []
author_last_names = []
for i in author_names:
    author_names_split.append(i.split())
for i in author_names_split:
    author_last_names.append(i[1])
print(author_last_names)
