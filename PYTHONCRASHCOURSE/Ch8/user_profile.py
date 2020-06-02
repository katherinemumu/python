def user_profile(first, last, **stuff):
    info = {}
    info['first'] = first
    info['last'] = last
    for k, v in stuff.items():
        info[k] = v
    return info

profile = user_profile('kat', 'key', age=25, car='ford')
print(profile)

