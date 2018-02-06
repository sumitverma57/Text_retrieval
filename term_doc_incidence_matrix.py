import graph
matrix=graph.Graph()#making graph object
matrix.add_edge('Aaron','Titus Andronicus',1)#making graph with edge weight 1
matrix.add_edge("Abbott of Westminster","Richard ii",1)
matrix.add_edge("Lord Abergavenny","Henry viii",1)
matrix.add_edge("Abhorson","Measure of Measure",1)
matrix.add_edge("Abraham Slender","The Merry wives of Windsor",1)
matrix.add_edge("Abraham","Richard ii",1)
matrix.add_edge("Archilles","Troilus and Cressida",1)
matrix.add_edge("Adam","As you like it",1)
matrix.add_edge("Adrian","Coriolanus",1)
matrix.add_edge("Adriana","The comedy of Errors",1)
matrix.add_edge("Aediles","Coriolanus",1)
matrix.add_edge("Aemelia","The comedy of Errors",1)
matrix.add_edge("Aemilius","Titus Andronicus",1)
matrix.add_edge("Aeneas","Troilus and Cressida",1)
matrix.add_edge("Agamemnon","Troilus and Cressida",1)
matrix.add_edge("Agrippa","Antony and Cleopatra",1)
matrix.add_edge("Agamemnon","Troilus and Cressida",1)
matrix.add_edge("Ajax","Troilus and Cressida",1)
matrix.add_edge("Alarbus","Titus Andronicus",1)
matrix.add_edge("The Mayor of St. Albans","Henry vi",1)
matrix.add_edge("Alcibiades","Timon of Athens",1)
matrix.add_edge("Alexander","Troilus and Cressida",1)
matrix.add_edge("Alexas","Antony and Cleopatra",1)
matrix.add_edge("Alonso","The tempest",1)
matrix.add_edge("Amiens","As you like it",1)
matrix.add_edge("Andromache","Troilus and Cressida",1)
matrix.add_edge("Angelica","Romeo and Juliet",1)
matrix.add_edge("Angelo","Measure for Measure",1)
matrix.add_edge("Angus","Macbeth",1)
matrix.add_edge("Anne Page","The Merry wives of Windsor",1)
matrix.add_edge("Antenor","Troilus and Cressida",1)
matrix.add_edge("Antigonus","The Winter's tale",1)
matrix.add_edge("Antonio","Much Ado about Nothing",1)
matrix.add_edge("Alexander","Troilus and Cressida",1)
matrix.add_edge("Alexander","Troilus and Cressida",1)
matrix.add_edge("Antony","Julius and Ceaser",1)
matrix.add_edge("Antony","Antony and Cleopatra",1)
matrix.add_edge("Octavius","Julius and Caesar",1)
matrix.add_edge("Octavius","Antony and Cleopatra",1)
matrix.add_edge("Brutus","Julius and Caesar",1)
matrix.add_edge("Cleopatra","Antony and Cleopatra",1)
matrix.add_edge("Julius","Julius and Caesar",1)

l1_1=matrix.get_adjacent("Octavius")#getting all the nodes to which edge is connected to Octavius
print "Octavius found in", l1_1
l2_1=matrix.get_adjacent("Antony")
print "Antony found in",l2_1
lnet1_1=l1_1 and l2_1
l3_1=matrix.get_adjacent("Cleopatra")
print "Cleopatra found in",l3_1
if len(l3_1)>len(lnet1_1):#if length of l3_1 is greater then we compare each element with the smaller list
    for val1 in lnet1_1:
        for i in range(len(l3_1)):
            if l3_1[i]!=val1:
                lnet2_1=l3_1[i]
                break
            else:
                continue
else:
    for val1 in l3_1:
        for i in range(len(lnet1_1)):
            if lnet1_1!=val1:
                lnet2_1=lnet1_1[i]
                break
            else:
                continue
print "The first query 'Antony and Octavius and not Cleopatra returned",lnet2_1
l1_2=matrix.get_adjacent("Brutus")
print "Brutus forund in",l1_2
l2_2=matrix.get_adjacent("Julius")
print "Julius found in",l2_2
l3_2=matrix.get_adjacent("Octavius")
print "Octavius found in",l3_2
lnet1_2=(l1_2 or l2_2)
if len(l3_2)>len(lnet1_2):
    for val1 in lnet1_2:
        if l3_2[0]==val1:
            lnet2_2=l3_2[0]
        else:
            lnet2_2=l3_2[1]
else:
    for val1 in l3_2:
        if lnet1_2[0]==val1:
            lnet2_2=l3_2[0]
        else:
            lnet2_2=l3_2[1]
print "The second query 'Brutus or Julius and Octavius' returned",lnet2_2
