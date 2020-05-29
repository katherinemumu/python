names = ['bob', 'joe', 'chris', 'jen', 'jason']

languages = {
    'bob': 'C',
    'bobby': 'Python',
    'yeah': 'Java',
    'jason': 'Java',
}

for i in languages.keys():
    if i in names:
        print("Thanks for filling out the survey", i )
    else:
        print("Please fill out the survey", i)