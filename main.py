import instaloader
import datetime

insta = instaloader.Instaloader()
now = datetime.datetime.now()
try:
    insta.login("", "")
    insta.test_login()
    print("logged")
except:
    print("log error")
    exit()

while True:
    target = input("Inserisci il nome utente del target oppure 0 per uscire: ")

    try:
        if target=="0":
            exit()
        print("Trovato")
        profile = instaloader.Profile.from_username(insta.context, target)
        followers = profile.get_followers()
    except:
        print("User non trovato oppure 0")
        exit()

    names = []
    i = 0
    print("Registro i dati...")
    for follower in followers:
        names.insert(i,follower.username+" "+str(follower.userid))
        i += 1
    names.sort()
    print("...finito")
    print("Inserisci 1 per scrivere nel file i followers, 2 per confrontare, 3 quit")
    switch = input("Inserisci un numero: ")

    if switch=="1":
        f = open(profile.username+".txt", "w+")
        f.write('Profile {} has {} followers {}-{}-{}:\n'.format(profile.username, profile.followers,now.day,now.month,now.year))

        for name in names:
            f.write("{} {}\n".format(name.strip().split()[0],name.strip().split()[1]))
        f.close()

    if switch=="2":
        a=0
        try:
            f = open(input("Inserisci nome file da confrontare: ")+".txt", "r")
            f1 = open("unfollow.txt", 'w')
        except:
            print("File non trovato")
            exit()
        count = f.readline().split()[3]
        print("Da {} followers a {}".format(count, profile.followers))
        f1.write("Da {} followers a {}\n".format(count, profile.followers))
        lines = f.readlines()
        for line in lines:
            for name in names:
                if line.strip().split()[1]==name.strip().split()[1]:
                    a += 1
            if a == 0:
                print("Persona che unfollowa: "+line.split()[0])
                f1.write("{}\n".format(line.split()[0]))
            a=0
        f.close()
        f1.close()

    if switch=="3":
        exit()
    print("-----------------------------------\n\n")
