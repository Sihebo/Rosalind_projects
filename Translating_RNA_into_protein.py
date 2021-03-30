dict = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"", "UAG":"",
    "UGU":"C", "UGC":"C", "UGA":"", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

#print(dict)


s = "AUGAGGUCUCCUGCUUUGUCGGACCUGACCUACAGGCAUGCGGCAAUCUAUGAGAUCAAGAUAGGUACGUCUGGCAGAGAUCGGAUCGCAUUAUGCAGUGACGGAAGUUUCACCGCCCCAACAGUAAUAGGGUCGAUUCAGAAAGCCCCGGUAGCUCCAGACUCCGAAAUCCGAUUCUCACACUCCAAGACUUUGAAUUGGCGCCAUUUGUCUGUAUAUUCCCUAAAUACUUGUUUAACAAAGCCUCCCGUGGUAGCAUCCAGGCGCCCAUGUGUAGAGUCAAUUAUAUUUGAUGAUGGAAAGCUCACAGGCUUGAAGGCGCACGCAGAAAUCAAACGCAGCUGGGCUAGAACCCCUGAUGCACUACACGCGGUCCCUUUUCUGAUCGCAGCGCCGAGUACGCAAGCGAAUAAGCACUGUCUUGUAGCCUUUCUGGAUCGAGACCUACAGAUACUACCUGAUUGGGAAUACCUCCCCUCGAAUUCGAACCCGAACGAUAAUAUUUUGCAUCGGCUGGCGCCCCCGCUAGCUCGACCCCCGGGCUUUUAUAGGUACGUUGCUACCCACCUGAACCCUGUUCUAUCCCGUUCUUUUGUAGUUAUUUCUGCCCGUAGCAGGCACACGCCUAAACUCCUCUGCGUCGGUUCAUCAGUAGCAACUAGCAUCCUAAUGAAGGUAUGUGACGCGAUCUUGCCAUCCAUACUGAGAAGGAGGCAACUGGACUACCGUCGGAGGUACAAGCCAUCGUUGCUGACGUUAAGUUCAGGUGGAGAGCUGGUCAAUGGACGUGCACAACCAAUGCUAGUGGUUGAGCUGUUCGCACGCACCUACGACUGCAGAUCUAAGGCUCCACCUCCAGUCCCCUUAUCUUUAUUCAAGUGCACUUUAACCUCCACAUGGAAGUGCACUUCAGUACUAUGUGGGCAACUUUCCGGUCUUCCAUGUCGAGAGAUUGUUGUGAUCACGCUUAACAAUGCAUGUCGCGUAGUAGGGCAUUGUGCGGGCCGCUGCUACGCUGGUGGUCUCUUAGGUCUUAAGGCCCCGGACUCCGUUCCUGUACGGUCAGUGAGGGGAGUCGCAGCGCUCUACGACGCUAUAGGUCCCCGUUCCCCAACUGCCGAAUAUGGCGCAGGCAUUGGUCAACUAAAUGAACUUAGGGCGGUUGCUAACCCGGGGGGCACCAGUUAUCAAUCUCGUAUUCGUGCUCACUCAAUUCACGCACUCGAAGCCCAGAGAGAAUUCGGGUUCCCUCUGCCCAGCGCGCAGCUACGUAAACUUCCCCAUCUCUUGAUGUGUAUGCUGGUCCUACCGUUACCGGGCGCGAUUGACCCAAGAUUGUGGCGAGAAGCGCGGAUCAGUAGCAGCGGAGAAUCGCAGUCCGUCUACACAAAUUUUUGUAAGCGACAAUCCCAGUCUCAAGUUCCGCACCUUAACUCUUUUCGCCCCAGAUGGCUCGCUACUGGGCAGCGUACGCAACGACAAGCAAACACCCAAACUGUUUAUUUUGAGACUCAACAGAGUGGACGUGCGGGGUCAAAGCCCCGACCGACGAGCCUCUACGGGCUUCCCGGUCUGAAGGUUACCUCCUGUAAAGUCCAGUUGUUCGUUGUAACGAUGGUUUCAAAGUUCUAUUGGGCAUGUGCUCUGCUGAUCUGGAACACUGUGAAUCGCAUUAAAGCCUUUUGGGGGUUAAGGAAGAACUGGACUCACCUUUGCCAAAACGUAUUCUCGAGGCGACACCAGCUUUAUAGGUACAAUGGCACGUCUCAGUCACUACGCGCAAUGAUACACCCAUGUGCAUGCGCGGACUCUUUCGACAUAUGGACGAUCCUUGAAAACUUACUGAUACCAAAAGUGCUACUAAGACAGAUUAGUGGACACCGCGAUGUCCCCCUCAGUCCGACUAACCACAAGCUACACGCAGUGAUGACACCCUUGAACUAUCACCGUUUCACGGGAAAAGGCUCACAUCCUAGAGUACCGAGAUACCCCCCGAUGUUAAGGCUUAAUGAGAACCCUGGCUAUUAUCUAGAAUGGCUCCCCCGUUGUAAUGAUCUGAUGUUCGAACAACGGGGUUCCCGGUUACCUUCGAACAACACGGGGCCAACCCACAGGGCGGUCAAGGCCGCAAAUGUAUAUAGUUUAAGGACCCUUCGGAACACAGGAUCUCCGCUGUCCCUACCGGUAAGUUGUGUGAGACGCUUAGGAGACAAAAUUUGCGAACACCCUCGCUUAGCCUGCAUCUCGGGCUGCUACAACUUGCACAGACCGGCCCACACGAGCGACUCCACAAGUCCCUUGAGAGGAGAUUAUUGUGUAGUCCUAUGCUAUGGCCGUUGUAAACGACGGUGCUAUAUAUCAAAUGUGUGUCGACUAAGGGACGUCCCGCAGGAAAUGAGACUCACCAGGCCCAUGCGUGAAAAAUGGUGGUACUUGCACAUAAAUUCAGGAAAAGUUUUUUACCAGCUGGACGCAGCCGUAGGAGCGAAGCUUGCGGCCUAUCCCUGCCGGAGCACCCUAGACAAGCUCUUAGGUGUUCAUUGCGUGUUCUCAGUUUCGCUGUCCAUGUCGAUACAUAGCGAUGUAUGUAUGCCCAUAGAGCAACGGUUAAGAAACAAAAACGGAUCCGGGCCCGGGAUUAGAGCACAUACUGUAACGAUCCUUCCGGGCGAGCAGCUUCGAUUAAAGUGGGGUAUGCCUCAACAUGCUGUUGUUGCGAAAACAAGCGCCUCCAACCCGGUUGCUGGCGAAAUUCCGCGGGCAUCUCCGCACUAUAUACCUAUACCACAUACUUUGAUGCUUGUAUGCACUGUUGUUGGGGUGUUUUCAUUCCUACGAUCGGCAGUUACCAGCGAGGCAAGGGGGUUCCGUUAUGAAACUUACUGGCGGCAUCCUGACAUGCGCCUUCGCUGUAGCAUCCUUGUUACCUCGCCAUCUACCGCAGUAAGAGUCGGUUUUAUUCUAGUACCGCCGCGGUUUGUAAGGUUGUGUUUCUGGACUAUCAAGUCUCGCCUUAGCGCAUAUCGGUUCAACCCUCGGAAUUCAAUGGGCCCGAGUAAACUUAACAGCGGGCCAUGCAGGUCAAUCCUCCAUAAAAUUGCCCGCCAAAACCCCGAUUUACUGGCUGCUCUGAGUAAUUGGAAGACGUCGGUACAGGCUAGAGCAACUUUGGAAGCCGGAAUACGUCCUGUAUUCGCCGAGAAUCGCUCUGACCGACCAAAAUUAUCAGGACCUGGGAAUUCCACUAUCCAGAAAAAACAGCGCCAAGGCAGUCGCGGGAAAGUAAUUAAACCAAUCGUUAUUAGACCUCCCCGUGAUAUGAAGAAUAUUACACCGCUUUUGAAGGGAGGGUGUGGGGGAUCUCUUCCGGUUAAUAGAGAGGUACUGAAUAUUAUUAAAUGGAGUCCGAGGUUGGUAUCAGAACGACGGCAGUUAAUGAUUCAACAAUGGAGACUGUGUUCGUUGGCUCACGGAGAGCGGAAAGUUUCAACCUCGCCACUACACAGAGCACUGACUUUAGUACAACAAUACUGUCACAGGUCGAAUCAACUUGGGAUUAUUACUCGCAGAAGGACUGUUCUAUUAUGUAGUGUCGCGAGUAGGGUCAGGACGGCGCACAAUCCCCCAUCAAGGUGCAAUUAUAUGGAGCCCCAGGCAUCAAGGCCCCGGUCUUCCAAACCCCAUGAACAGUUCCAUCCCCUCACGUUUUGUGCGGAUGGCCCGCAUCUGACCAUAUUCCGAUAUGCGGGCCGGCGGAGAAGUCCCAACGGAGACUGUACGUCGACAGAUUGCAGUACAAAUAGGAAUAAUCCCGCAUAUCUAUUGCGUCGUAGUAUUUGGUGGCCGUGUGCUAGAGAUGUUUGGGGAUGUCAUAGUCUCCGUCAUAUUCGCGGUGGUGGUUUCCAUUGGCACCUAUCCUGGGGCCCGCAAUACCGAUGGGUUGCAUACUCUAGAUAUAUGCCCUUAUAUUACAGGGCCCGAAUGCUUGAGAAAAGGGAGCUUUGCUUGACCCUAUCGCCGAUGAACCGUGUAAGUUCAAAGGAGACUAUGAACCAUCUUCUGACCGCAGAGGUUGAGUGGGGUAUCUUAUCCCCGCUCUCAUACAGACAUUAUCAGCCAUUGGGCCCGACCGAGCAUAAAAAGCAUGGAAGUAAGUUCUACACAGCUACCAGUCUGCGUCGCGAAUGCUGUACUGUUUUGGAUAACGUGUCGACAGUGAGUACUUGGCGAGGUAAGGGUAGCCCAACUAGGAGUUCCCGUUACUCGCCGUCAUCCAGACGCCAGCUGGACUAUUGCGAACCUACGGGCCCUCGCGGGGUUUCCUCGUGCUGUGGGGGUUCGUUGACCCUAUACGCCACGGGUUUAGCAAGAUUCCUGACGUAUAGCUUGCAUCGCCGCUCUAAUGAGAAGGCUGGUUGGCUAGGAUGGUACCGGCGUGGGGCGAAGACCUCGAACAACAUGGCUAUUACGGAACCAACGCCGUUGGUCACGGCGGUCUCUCAAGCGCUUGCAGCUUGCAGCCGUACGCAGAUUUGGCGCCAGGUAUCCGGAGCGCAAAUGGCCAGUCACUCCUUUCGUUGUCCUACAAUGGUAUCUUCACGAAGGCUCCAUUACAUAGUGCGAAAUCUCGGCGCAACGUCGAACCUACAAACCUACAUAGGGAGCCAAACCAGAAUCAAACUAAGCAGAUCAUACGAUUCGGUUUUAUCCACGCUUCGACAAGUUGAGCGGAAUUUGGCGUUAGCUGUGAGGCCGGCGAGCGAAUGCGAUAUGCCAGCGCGGCUGAGAAAGGUGAAUGCGGUAUGCACCCUUGCCUCAUUAAAGAUGUGUUGUCAUUUUUAUGCAGCAACAGCAUCAAUCCGCUUGCUAAUUCCUUUCUUAGGUAGUACUAGUGCAUUAUUGACCGAGUCUCCCCCCCUAUUUACAACGGACCGCGUAAACAAUCUCAGCUCAAACAUUAUACGUCACAUCCUUAACAUGAUUUAUAUAUCGAUAAGGAGCUCUUUGGUAGCACUCAUCAAAAGGUAUGUCUACGCGCUCCUUUGGUUCCAUGUAGCGGGCUGGCUAUCGGGAAUUCCAUUAGUCGGUGCCCUGUCAAACUAUAGAGUUGUACCAACCACUGUGGUAGGCAACCUACAAGUCGACUACGUUCGACUAAGAUUUUCGCCGGUCACCCGAAUAUCAACGCCUGACUUUCUACGCAGGCUCCAGGUAUCAGAGAUCUCAACAUCCAGAUGCGACGCCUGUUAUUCUGAUACCGUAACGGCCGGAUACUUAAAAGGAUUUGACACAGGGCCGGGGUUUAUUCAGGGGGCUGAGGAUGGUCUACCGGGGGGUGCGAAGACGAACAUAGUCACUAAUACUUUAACAGGUCUUGGGUAUCGACUGAACAUCAAGGGGUUAGACAUCUGCAACAACAAGCGUCUGAGGAAGCUAGAUGCGCUAAAAGGCUGUCUUCUGGGUACUAAGUCCACAACUCUAUUGCUUGUGACGUGUCAGAGUCUGUUCAAUCAGCACGCCACGCUUCCGCUUAACACAUGGGAAGGGUGCCCUCAGAGCUGGAGAAAUAACAACACACUCCAAUCGCGUCACGUUAGUACACCGGCGUCUCGAAGUUGGCUUGACUUUCUCUUAUUGCCAGGCAUGGUAUGGAGCCACCUUUUGUCAGACAGACCAAGGCAACCAGCACCCGUGGUCGCUCCGAUCUUCACGUCGAGUACGAGUUUACGGGGCUUUUGGGGGACAGGCAGCUAUGCCGAGAUAACCAUACCAUUACUUGUAGGGCUUUUCCAAUACCCUUUCCACCAUCAGGUCCUAUUCGCAUGGACUGGACGCCAAAUUUUCGUGCCCUCAGCCUUGUAUGGAAGUGGCACACGAGUUGCCCCACUACGGGAAGAACACCUGGCAGGAUCAUUGCCCAAGGAUGGCCUGACUUGUUUAUUUUGGCUGAGGGUCAUACUGCCGGCGGUCACCUACUUAACUGUGUUAGCUCAUCCCUACCGCGGAACGUUGGUACCCAAUCUGAAAUACCCAGUUGCCAUCGGUCAUCCCAACGUCAGGAUGACCGUAGGAAUAGUAGCCGUAAAAUGUACAGGCGGAAUUCAGCACAUGCGCCAGGAACUGAAUCCGUCAGAUAGCAACCAACAUCCGAGACCGGACAUCGCCGGGGGGAUGCGAGAGACUACUAGACCAGCCGUCCGUGGGGGAGGUUUUUGUAUAAUGGAACUGGGGCAGUUGUGGCAGAAAGGGCACACACCUACGGGGGGAGUUAUGGUUACCUCUCCUUACAAAACGCGUCGGAUCCCUCUUCAAUACAGAUAUACCGGGCCGAAUAUACACAAACUCGUCUUUGAGGGGACUUUAAGCCACCUCCUUAGCUCAUGGGACUCCAGAUUCGGAUGGGCGCUACACACAAGGAGAUGGAUUUGCCAUCGGUCUCAUUCCCCAGCUUGUGACUACGAGUUAGCGGUUAUGCCGCAAGGCACACUCUGCAGGGUCGACAAGCUUAGUGAGUUAGAUCUAAUUAUUGACCAGCGGAUGCAGGCUCAAUCACUCAUCAGCGCACUCUUAGACCAUAGAAAAGUCACCGCGAGCUCUGUGACCCUCAAGAAUUAUAGUGUGCAUCCGAUACGCGCACUGUACCAAGCUGAUAUCGUGCUCCCCAGAGCUGUCAUAUGUACCGGAUGCACGCACGGCCGUACUUCUGAACGUUACAUUUGCCCGACUGAGAACCUCCUCGGAUUUAGGAGUUCUCGUUUCGAUGGCCGUGUUAGUAAACGUACUACCAAUGCGCACGCCAGUAAAGUCGAGCCUAGAUCGCUUACACACGAUAUCGCUGAGUGGUUCCGCGCUUAUUGCGGGAAAGUCAUCAGUGUCUUAUUGAUUGUCGAGGCUAGAGAAGCCCAGUACUCCAAUACAGACUUGUCCCUAUCAUCACGGGGGGUUGGCCAUGUCCGGAUAGGUAGUAGUGGUACAUUGGUCGCCCGACACUCUUUUUCAAGCCAGAUUAGUCGGCUGGUUAACUGUCCACUACUCAGCCGGUUAAACGCUGGUGGGUCUUGCCUAAUCUACCAGGCAAUUCUUACGGCGCCUCUUUUAUUCAAAAGAGGCUCUCAUCAUAGAGACCCACAUCUCGGUGCAGCUGACUCAGUGUACGAUCUCCCUCCUGAUGACUUUGCCCUAUGUAGUGUAGGAACGAAUACACAGCGCAUCUACCUGCACGGCUCCAUAAACAACCGUAUGGAAUCAGGGACAGCAUUUGUGGCCAAGGAGUUUUUAGCAGUUUAUGGCUUAGCCCCGAAAUCGGUCGGGAAACACGAGUCAAAUCCGGGAGCCACCUGGUUUAAUAGUAUUGGGUCCUGUUGGAUGUUCCAAUACCGUUUCUUCCCACGGUGCCCGUAUUGCUCUUGCCCAUCGUUAUCCAACAAAAAUGCACCUCUUUUCGAGACCGUGGUCCUACUAAACUUUUGUUUGUCGGCGGCCAGGUUACGAGUACCAAGGCGUUCAUGUCGCACUGCGAGUGGGGCGAAUCCAUUGCUCAGUUCAUCCCAUCCUGAGAUUGUGGCAAAGGAAAACCGUCGACGGGUCAUAGAGACAACACAUCGACCAACCUUUAGAGGCAAGCUGCGGGUUGUCAUAUCAGGGGAACCCGGGGUCAUGACGGUACCCGGGACAUACACCGACUUUCCGCUAUCUAUCCAGAAGACCUCAAACAGACCAGUUCCACCAGCUGUCAUACAGUUGUACAGCUUAUUCCUGAGGGGUAAUGUCAUCAUGCUGUCGGACGUAAAGAGAAUCAUCUUACCUUACAAUAACGACCUAGAGGGAGUCCCAAAACGCUCCUUGGUCCCAUCUUCGGUUCCGUGGAGUUUCUAUGAGACAAAUUCAAAUAAUGCCUUCAGUUUUAAGAACUGCCUAUUCGUGGGAGCAUGGCUUGUUAAGAUUAGUUAUCUGUUCGCCUUGGAUACACCUGCGGGAUCGUCGGGGACUUCCACCUGUGUAUCGUCUCCGAUACAACAGUGUGCCCCUCGAACGCAUAGCGACAUACUACUCUCCCCUGUACUUGAAUCGCAUACGCUUAAUUCUAGAGGACUACGACCGGUCUACCCAGCGAUGGGCAACGAGCUCUGGUAUGAUCACGACCGACACGUGGGUCGCAUUUCGGACGGACAAUCGUCCGUCUCUUUAAGCAGGAAAAUUCACCAUACAGCUCCUUGCAUGCUGAUUCCAAACGAGACACGAAACGGGAUAGCUGUUAUGCGCAUAGUGGGGUCACUAGACCCUUCUACUUCUAGUACAUUAGAUGCGAGAAUGUCAUCAUUUGACGCCCCUCCACUUACCGUUAAUGUAGCUAAUCUCAGACCGGACCACCGGGGUCUAGUUGAAUGCUCCCAACGCUAUAGACCGGCAGACUUACGGAAACGCCUUUUUGUCACCUCUUUUAGGGACGCAACUCAAUUUCAUGCCUCCCUUCUCCCCACUAUCCUUGGUCUUGUACUACAAUCGUCAUACCAUUCGCUUACGGUCCCGCAGGACAAGAGAGGAGGGAAGCGAUUCAGACGCGUGGCAUUCGGUGCCAGCUCUUACUAUGCCUCUGGAGGUCGCUCUAUUAGAAACUACGUGGCAGUCGAGAGGUACCGUUUCAAGGUGAUACACCUUAGGAGUAGAACAACCGAACGCGAUUUGUGGCGGGCAACCUUGAGUAUUUGCUUAUGCAUGUUACUGACUUACGAGCCCAUGCACAUUGUCUUUAAAGCCACAUUAAUGGCGACCGUGAGGAUGUCGCCAUUGGACGCUUUCGUGACCAUAGGCGAAUUGGCGAAUCACCUUACGAAAAAGACCGAAUCAAGCUACGUUAGAGGACUUGCGGACGAAUAA"

list = []

def tripletlist(rna):
    n = len(rna)
    for i in range(0, n, 3):
        #print(i)
        list.append(rna[i:i+3])
    return list

tripletlist(s)


proteinstring = ""

for i in list:
    if i in dict.keys():
        #print(dict.get(i))
        proteinstring += dict.get(i)

proteinstring = proteinstring.upper()

print(proteinstring)
        
        
    
        
        
        
    
    
    


    
