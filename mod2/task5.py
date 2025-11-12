subdomains = input().split('.')
for i in range(len(subdomains) - 1, -1, -1):
    print(subdomains[i])
