import sys

table = [l.strip().split() for l in sys.stdin]
pars = [int(pars) for pars in table[0]]
index = [int(index) for index in table[1]]
players = table[2:]

scores_for_player = {}
lname = 0

for player in players:
    name = " ".join(player[:-19])
    hcap = int(player[-19])
    scores = player[-18:]

    if len(name) > lname:
        lname = len(name)

    scores_for_player[name] = 0

    for variable, score in enumerate(scores):
        try:
            score = int(score)
            current = index[variable]
            free = (hcap % 18 >= current) + hcap // 18
            net = score - free
            curr_par = pars[variable]
            score_on_par = net - curr_par
            points = (score_on_par * -1) + 2

        except:
            continue
        if points < 0:
            points = 0

        scores_for_player[name] += points

scores_for_player = sorted(scores_for_player.items(), key = lambda variable: -variable[1])
for name, score in scores_for_player:
    print("{:>{}} : {:2}".format(name, lname, score))
