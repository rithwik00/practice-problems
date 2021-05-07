def count_balloon():
    
    for i in strr:
        if i in balloon:
            balloon[i] += 1

    balloon['L'] = balloon['L'] // 2
    balloon['O'] = balloon['O'] // 2
   
    return min(balloon.values())


balloon = {'B':0, 'A':0, 'L':0, 'O':0, 'N':0}
strr = 'baloonballoonnbbaallaollllnOlnONLnoLNLnolNOLnolNOLnlNLONLoloanlonloalnonaoonlaonlaonlaonlaonlnlanoaoaonolnlnaon'
strr = strr.upper()

print(count_balloon())
print(balloon)
