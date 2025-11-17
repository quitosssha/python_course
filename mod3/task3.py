domain_name = input()
reversed_domains = [x for x in reversed(domain_name.split('.'))]
[print(d) for d in reversed_domains]
