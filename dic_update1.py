key=['ten','twenty','thirty']
value=[10,20,30]
rec=dict()
# rec={} # also use angular parenthics for making dictrionay
for i in range(len(key)):
    rec.update({key[i] : value[i]})
print(rec)