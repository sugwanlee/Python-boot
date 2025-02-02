def solution(babbling):
    for i in range(len(babbling)):
        while babbling[i] != "":
            if babbling[i].startswith("aya"):
                babbling[i] = babbling[i].replace("aya","")
            elif babbling[i].startswith("ye"):
                babbling[i] = babbling[i].replace("ye","")
            elif babbling[i].startswith("woo"):
                babbling[i] = babbling[i].replace("woo","")
            elif babbling[i].startswith("ma"):
                babbling[i] = babbling[i].replace("ma","")
            else:
                break
    return babbling.count("")