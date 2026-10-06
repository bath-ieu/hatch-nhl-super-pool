import json
import urllib.request

# Configuration des participants et leurs choix
PARTICIPANTS = [
    {
        "name": "Jean-Philip Tremblay",
        "skaters": [8480069, 8484801, 8480839, 8480018, 8481540, 8484144, 8485366, 8477493, 8478483, 8478427, 8483445, 8484153, 8478397, 8484984, 8483515, 8484387, 8478013, 8481533, 8483495, 8478010, 8476468, 8481618],
        "goalies": [8476883, 8479406, 8480045],
        "teams": [8, 7, 1, 52]
    },
    {
        "name": "Nicolas St-Pierre",
        "skaters": [8480069, 8480800, 8477956, 8479318, 8477939, 8482740, 8485366, 8477493, 8478483, 8477960, 8475786, 8484153, 8477946, 8486067, 8483515, 8480893, 8478013, 8481581, 8485406, 8475168, 8482702, 8482775],
        "goalies": [8476945, 8480280, 8482661],
        "teams": [25, 14, 2, 28]
    },
    {
        "name": "Alondra Rima",
        "skaters": [8478402, 8484801, 8480027, 8480018, 8481557, 8478550, 8485366, 8477493, 8476973, 8478427, 8482699, 8483431, 8471215, 8484984, 8477500, 8479987, 8475754, 8481581, 8483495, 8476454, 8482702, 8481618],
        "goalies": [8479979, 8479406, 8482487],
        "teams": [25, 22, 2, 28]
    },
    {
        "name": "Aya el Khazen",
        "skaters": [8476453, 8483457, 8477956, 8480018, 8481540, 8471675, 8485366, 8481605, 8474590, 8482093, 8479343, 8473419, 8478397, 8484984, 8480830, 8481524, 8474564, 8481581, 8485391, 8476875, 8484145, 8481618],
        "goalies": [8475683, 8480313, 8482487],
        "teams": [8, 14, 29, 3]
    },
    {
        "name": "Alain Roy",
        "skaters": [8480069, 8483457, 8477956, 8480018, 8481540, 8471675, 8485366, 8477493, 8479420, 8478427, 8479314, 8480208, 8475166, 8484984, 8483515, 8484387, 8476462, 8481533, 8483495, 8478010, 8480002, 8482775],
        "goalies": [8476883, 8480313, 8482487],
        "teams": [21, 22, 4, 28]
    },
    {
        "name": "Mathieu Huot",
        "skaters": [8480803, 8477934, 8480839, 8480039, 8479345, 8477504, 8485366, 8481605, 8474590, 8477933, 8479343, 8476887, 8477946, 8484762, 8482078, 8481604, 8475754, 8479407, 8485406, 8482730, 8480002, 8481618],
        "goalies": [8476883, 8480313, 8482661],
        "teams": [21, 14, 1, 28]
    },
    {
        "name": "Olivier Jubelin",
        "skaters": [8480069, 8477934, 8478864, 8479325, 8478398, 8478550, 8485366, 8477404, 8476973, 8477933, 8479343, 8476887, 8477946, 8484227, 8477951, 8480893, 8480014, 8479407, 8483516, 8478010, 8480002, 8482775],
        "goalies": [8476883, 8480313, 8474593],
        "teams": [12, 7, 5, 18]
    },
    {
        "name": "Yanick Tremblay",
        "skaters": [8477492, 8483457, 8477956, 8479325, 8481540, 8480036, 8478420, 8481605, 8478483, 8480865, 8479314, 8483431, 8478397, 8484873, 8483515, 8482720, 8474564, 8477955, 8482809, 8476875, 8481598, 8481618],
        "goalies": [8476945, 8480313, 8482487],
        "teams": [8, 22, 26, 20]
    },
    {
        "name": "Alexandre Neal",
        "skaters": [8478402, 8483457, 8477956, 8480018, 8477939, 8471675, 8478420, 8481605, 8479420, 8480865, 8479314, 8480208, 8478038, 8484873, 8477500, 8481524, 8471214, 8478445, 8482809, 8475168, 8477346, 8478133],
        "goalies": [8475683, 8479406, 8482487],
        "teams": [8, 6, 26, 52]
    },
    {
        "name": "Antoine Duguay",
        "skaters": [8478402, 8480800, 8480027, 8480018, 8481540, 8482740, 8478403, 8477493, 8479420, 8480865, 8479314, 8476887, 8475166, 8484984, 8483515, 8481604, 8474564, 8477955, 8482809, 8475168, 8482702, 8481618],
        "goalies": [8475683, 8478048, 8482487],
        "teams": [21, 7, 26, 28]
    },
    {
        "name": "Hak Jun Oh",
        "skaters": [8477492, 8484801, 8480839, 8483456, 8481540, 8478550, 8478420, 8477404, 8480801, 8476459, 8479314, 8476887, 8478397, 8486067, 8480830, 8480893, 8476462, 8481581, 8483495, 8478010, 8477346, 8482737],
        "goalies": [8476883, 8475809, 8474593],
        "teams": [13, 22, 1, 28]
    }
]

def fetch_json(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Erreur lors du téléchargement de {url}: {e}")
        return {}

def main():
    # 1. Récupérer les classements des équipes
    standings_data = fetch_json("https://api-web.nhle.com/v1/standings/now")
    teams_stats = {}
    for team in standings_data.get('standings', []):
        t_id = team.get('teamAbbrev', {}).get('default')
        # On calcule les points de l'équipe selon le règlement
        reg_wins = team.get('regulationWins', 0)
        ot_wins = team.get('wins', 0) - reg_wins
        ot_losses = team.get('otLosses', 0)
        
        # 3 pts reg win, 2 pts ot win, 1 pt ot loss
        total_pts = (reg_wins * 3) + (ot_wins * 2) + (ot_losses * 1)
        teams_stats[team.get('teamId', {}).get('default')] = {
            "name": team.get('teamName', {}).get('french', team.get('teamName', {}).get('default')),
            "abbrev": t_id,
            "reg_wins": reg_wins,
            "ot_wins": ot_wins,
            "ot_losses": ot_losses,
            "points": total_pts
        }

    # 2. Récupérer les stats des joueurs
    all_player_ids = set()
    for p in PARTICIPANTS:
        all_player_ids.update(p['skaters'])
        all_player_ids.update(p['goalies'])

    players_stats = {}
    for pid in all_player_ids:
        p_data = fetch_json(f"https://api-web.nhle.com/v1/player/{pid}/landing")
        if not p_data:
            continue
            
        pos = p_data.get('position', 'F')
        first_name = p_data.get('firstName', {}).get('default', '')
        last_name = p_data.get('lastName', {}).get('default', '')
        full_name = f"{first_name} {last_name}"
        
        featured = p_data.get('featuredStats', {}).get('regularSeason', {}).get('subSeason', {})
        
        if pos == 'G':
            wins = featured.get('wins', 0)
            shutouts = featured.get('shutouts', 0)
            ot_losses = featured.get('otLosses', 0)
            # 4 pts victoire, 5 pts blanchissage, 1 pt défaite OT/SO
            pts = (wins * 4) + (shutouts * 5) + (ot_losses * 1)
            players_stats[pid] = {
                "name": full_name,
                "position": "G",
                "wins": wins,
                "shutouts": shutouts,
                "otLosses": ot_losses,
                "points": pts
            }
        else:
            goals = featured.get('goals', 0)
            assists = featured.get('assists', 0)
            # D: 3 pts but, 2 pts passe | A: 2 pts but, 1 pt passe
            if pos == 'D':
                pts = (goals * 3) + (assists * 2)
            else: # Attaquant
                pts = (goals * 2) + (assists * 1)
                
            players_stats[pid] = {
                "name": full_name,
                "position": pos,
                "goals": goals,
                "assists": assists,
                "points": pts
            }

    # 3. Calculer les points par participant
    leaderboard = []
    for p in PARTICIPANTS:
        total_score = 0
        skater_details = []
        goalie_details = []
        team_details = []

        for pid in p['skaters']:
            st = players_stats.get(pid, {"name": f"ID {pid}", "points": 0, "goals": 0, "assists": 0, "position": "F"})
            total_score += st['points']
            skater_details.append(st)

        for pid in p['goalies']:
            st = players_stats.get(pid, {"name": f"ID {pid}", "points": 0, "wins": 0, "shutouts": 0, "otLosses": 0, "position": "G"})
            total_score += st['points']
            goalie_details.append(st)

        for tid in p['teams']:
            st = teams_stats.get(tid, {"name": f"Équipe {tid}", "points": 0, "reg_wins": 0, "ot_wins": 0, "ot_losses": 0})
            total_score += st['points']
            team_details.append(st)

        leaderboard.append({
            "name": p['name'],
            "total_points": total_score,
            "skaters": skater_details,
            "goalies": goalie_details,
            "teams": team_details
        })

    # Trier par rang
    leaderboard.sort(key=lambda x: x['total_points'], reverse=True)

    # Sauvegarder dans data.json
    output = {
        "updated_at": standings_data.get("season", "20262027"),
        "leaderboard": leaderboard
    }
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
