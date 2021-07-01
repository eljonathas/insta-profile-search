import instaloader
import json

def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    if iteration == total:
        print()


# VARIAVEIS DE LOGIN (É BOM QUE NÃO TENHA AUTENTICAÇÃO DE DOIS FATORES NA TUA CONTA)
login_username = "YOUR USERNAME"
login_password = "YOUR PASSWORD"

# PERFIL ALVO DA BUSCA
profile_target_username = "PROFILE TARGET"

loader = instaloader.Instaloader()
loader.login(login_username, login_password)

profile = instaloader.Profile.from_username(
    loader.context, profile_target_username)

max_followers = 1000
possible_profiles = []
counter = 0

print('Getting followers list...')
printProgressBar(0, max_followers, prefix='Progress:',
                 suffix='Complete', length=50)

for followee in profile.get_followers():
    # Update Progress Bar
    printProgressBar(counter + 1, max_followers, prefix='Progress:',
                     suffix='Complete', length=50)

    if(followee.full_name):
        full_name_list = followee.full_name.lower().split()
        target_name = input("Informe o primeiro nome do alvo").lower()

        if(full_name_list[0] == target_name):
            possible_profiles.append({
                "full_name": followee.full_name,
                "username": followee.username,
                "userid": followee.userid
            })

    # add a new value
    counter = counter + 1

    if(counter == max_followers):
        break

print('Generating JSON file with all filtered content')

with open('results.txt', 'w') as f:
    json.dump(possible_profiles, f)

loader.close()

print('Done ✅')