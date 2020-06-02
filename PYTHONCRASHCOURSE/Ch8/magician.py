def show_magicians(m):
    for magician in m:
        print(magician)

def great_magicians(m):
    for i in range(len(m)):
        m[i] = 'great ' + m[i]

magicians = ['joe', 'betty', 'bota']
great_magicians(magicians)
show_magicians(magicians)
