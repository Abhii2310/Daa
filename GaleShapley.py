man = {
    "A": ["V", "W", "X"],
    "B": ["W", "V", "X"],
    "C": ["V", "W", "X"]
}

women = {
    "V": ["A", "B", "C"],
    "W": ["B", "C", "A"],
    "X": ["C", "A", "B"]
}

free =[x for x in man.keys()]
prop={x:[] for x in man.keys()}
eng={x:0 for x in women.keys()}

def match(man, women):
    while free:
        m = free.pop()  # Get the first free man
        mp = man[m]     # Get his preference list

        for w in mp:
            if w not in prop[m]:  # If he hasn't proposed to this woman
                prop[m].append(w) # Mark that he has now proposed to her

                if not eng[w]:    # If the woman is not yet engaged
                    eng[w] = m    # Engage her to this man
                    break
                else:
                    cp = eng[w]   # Current partner of the woman
                    wp = women[w] # Woman's preference list

                    if wp.index(cp) > wp.index(m):  # If she prefers new man
                        eng[w] = m  # Engage her to the new man
                        free.append(cp)  # The current partner becomes free
                        break

    print(eng)  # Print the final engagements

match(man,women)