import json
import os
import urllib.request

SEASON_ID = "20262027"

PARTICIPANTS = [
    {
        "name": "Jean-Philip Tremblay",
        "skaters": [8480069, 8484801, 8480839, 8480018, 8481540, 8484144, 8485366, 8477493, 8478483, 8478427, 8483445, 8484153, 8478397, 8484984, 8483515, 8484387, 8478013, 8481533, 8483495, 8478010, 8476468, 8481618],
        "goalies": [8476883, 8479406, 8480045],
        "teams": [8, 7, 1, 52] # MTL, BUF, NJD, WPG
    },
    {
        "name": "Nicolas St-Pierre",
        "skaters": [8480069, 8480800, 8477956, 8479318, 8477939, 8482740, 8485366, 8477493, 8478483, 8477960, 8475786, 8484153, 8477946, 8486067, 8483515, 8480893, 8478013, 8481581, 8485406, 8475168, 8482702, 8482775],
        "goalies": [8476945, 8480280, 8482661],
        "teams": [25, 14, 2, 28] # DAL, TBL, NYI, SJS
    },
    {
        "name": "Alondra Rima",
        "skaters": [8478402, 8484801, 8480027, 8480018, 8481557, 8478550, 8485366, 8477493, 8476973, 8478427, 8482699, 8483431, 8471215, 8484984, 8477500, 8479987, 8475754, 8481581, 8483495, 8476454, 8482702, 8481618],
        "goalies": [8479979, 8479406, 8482487],
        "teams": [25, 22, 2, 28] # DAL, EDM, NYI, SJS
    },
    {
        "name": "Aya el Khazen",
        "skaters": [8476453, 8483457, 8477956, 8480018, 8481540, 8471675, 8485366, 8481605, 8474590, 8482093, 8479343, 8473419, 8478397, 8484984, 8480830, 8481524, 8474564, 8481581, 8485391, 8476875, 8484145, 8481618],
        "goalies": [8475683, 8480313, 8482487],
        "teams": [8, 14, 29, 3] # MTL, TBL, CBJ, NYR
    },
    {
        "name": "Alain Roy",
        "skaters": [8480069, 8483457, 8477956, 8480018, 8481540, 8471675, 8485366, 8477493, 8479420, 8478427, 8479314, 8480208, 8475166, 8484984, 8483515, 8484387, 8476462, 8481533, 8483495, 8478010, 8480002, 8482775],
        "goalies": [8476883, 8480313, 8482487],
        "teams": [21, 22, 4, 28] # COL, EDM, PHI, SJS
    },
    {
        "name": "Mathieu Huot",
        "skaters": [8480803, 8477934, 8480839, 8480039, 8479345, 8477504, 8485366, 8481605, 8474590, 8477933, 8479343, 8476887, 8477946, 8484762, 8482078, 8481604, 8475754, 8479407, 8485406, 8482730, 8480002, 8481618],
        "goalies": [8476883, 8480313, 8482661],
        "teams": [21, 14, 1, 28] # COL, TBL, NJD, SJS
    },
    {
        "name": "Olivier Jubelin",
        "skaters": [8480069, 8477934, 8478864, 8479325, 8478398, 8478550, 8485366, 8477404, 8476973, 8477933, 8479343, 8476887, 8477946, 8484227, 8477951, 8480893, 8480014, 8479407, 8483516, 8478010, 8480002, 8482775],
        "goalies": [8476883, 8480313, 8474593],
        "teams": [12, 7, 5, 18] # CAR, BUF, PIT, NSH
    },
    {
        "name": "Yanick Tremblay",
        "skaters": [8477492, 8483457, 8477956, 8479325, 8481540, 8480036, 8478420, 8481605, 8478483, 8480865, 8479314, 8483431, 8478397, 8484873, 8483515, 8482720, 8474564, 8477955, 8482809, 8476875, 8481598, 8481618],
        "goalies": [8476945, 8480313, 8482487],
        "teams": [8, 22, 26, 20] # MTL, EDM, LAK, CGY
    },
    {
        "name": "Alexandre Neal",
        "skaters": [8478402, 8483457, 8477956, 8480018, 8477939, 8471675, 8478420, 8481605, 8479420, 8480865, 8479314, 8480208, 8478038, 8484873, 8477500, 8481524, 8471214, 8478445, 8482809, 8475168, 8477346, 8478133],
        "goalies": [8475683, 8479406, 8482487],
        "teams": [8, 6, 26, 52] # MTL, BOS, LAK, WPG
    },
    {
        "name": "Antoine Duguay",
        "skaters": [8478402, 8480800, 8480027, 8480018, 8481540, 8482740, 8478403, 8477493, 8479420, 8480865, 8479314, 8476887, 8475166, 8484984, 8483515, 8481604, 8474564, 8477955, 8482809, 8475168, 8482702, 8481618],
        "goalies": [8475683, 8478048, 8482487],
        "teams": [21, 7, 26, 28] # COL, BUF, LAK, SJS
    },
    {
        "name": "Hak Jun Oh",
        "skaters": [8477492, 8484801, 8480839, 8483456, 8481540, 8478550, 8478420, 8477404, 8480801, 8476459, 8479314, 8476887, 8478397, 8486067, 8480830, 8480893, 8476462, 8481581, 8483495, 8478010, 8477346, 8482737],
        "goalies": [8476883, 8475809, 8474593],
        "teams": [13, 22, 1, 28] # FLA, EDM, NJD, SJS
    }
]

TEAM_INFO = {
    8: {"name": "Canadiens de Montréal", "abbrev": "MTL"},
    25: {"name": "Stars de Dallas", "abbrev": "DAL"},
    12: {"name": "Hurricanes de la Caroline", "abbrev": "CAR"},
    21: {"name": "Avalanche du Colorado", "abbrev": "COL"},
    13: {"name": "Panthers de la Floride", "abbrev": "FLA"},
    7: {"name": "Sabres de Buffalo", "abbrev": "BUF"},
    14: {"name": "Lightning de Tampa Bay", "abbrev": "TBL"},
    22: {"name": "Oilers d'Edmonton", "abbrev": "EDM"},
    6: {"name": "Bruins de Boston", "abbrev": "BOS"},
    1: {"name": "Devils du New Jersey", "abbrev": "NJD"},
    2: {"name": "Islanders de New York", "abbrev": "NYI"},
    29: {"name": "Blue Jackets de Columbus", "abbrev": "CBJ"},
    4: {"name": "Flyers de Philadelphie", "abbrev": "PHI"},
    5: {"name": "Penguins de Pittsburgh", "abbrev": "PIT"},
    26: {"name": "Kings de Los Angeles", "abbrev": "LAK"},
    52: {"name": "Jets de Winnipeg", "abbrev": "WPG"},
    28: {"name": "Sharks de San Jose", "abbrev": "SJS"},
    3: {"name": "Rangers de New York", "abbrev": "NYR"},
    18: {"name": "Predators de Nashville", "abbrev": "NSH"},
    20: {"name": "Flames de Calgary", "abbrev": "CGY"}
}

def fetch_json(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Erreur téléchargement {url}: {e}")
        return {}

def main():
    # Récupérer l'ancien classement pour calculer la tendance (montée/descente)
    previous_ranks = {}
    if os.path.exists("data.json"):
        try:
            with open("data.json", "r", encoding="utf-8") as f:
                old_data = json.load(f)
                for rank, item in enumerate(old_data.get("leaderboard", []), start=1):
                    previous_ranks[item["name"]] = rank
        except Exception as e:
            print(f"Impossible de lire data.json existant: {e}")

    # 1. Classement Équipes
    standings_data = fetch_json("https://api-web.nhle.com/v1/standings/now")
    teams_stats = {}
    for tid, info in TEAM_INFO.items():
        teams_stats[tid] = {
            "name": info["name"], "abbrev": info["abbrev"],
            "reg_wins": 0, "ot_wins": 0, "ot_losses": 0, "points": 0
        }

    abbrev_to_id = {info["abbrev"]: tid for tid, info in TEAM_INFO.items()}

    for team in standings_data.get('standings', []):
        raw_tid = team.get('teamId')
        tid = raw_tid.get('default') if isinstance(raw_tid, dict) else raw_tid

        if not tid or tid not in teams_stats:
            raw_abbrev = team.get('teamAbbrev', {})
            abbrev_str = raw_abbrev.get('default') if isinstance(raw_abbrev, dict) else raw_abbrev
            if isinstance(abbrev_str, str) and abbrev_str in abbrev_to_id:
                tid = abbrev_to_id[abbrev_str]

        if tid and tid in teams_stats:
            reg_wins = team.get('regulationWins', 0)
            wins = team.get('wins', 0)
            ot_wins = max(0, wins - reg_wins)
            ot_losses = team.get('otLosses', 0)
            total_pts = (reg_wins * 3) + (ot_wins * 2) + (ot_losses * 1)
            
            teams_stats[tid]['reg_wins'] = reg_wins
            teams_stats[tid]['ot_wins'] = ot_wins
            teams_stats[tid]['ot_losses'] = ot_losses
            teams_stats[tid]['points'] = total_pts

    # 2. Stats Joueurs
    all_player_ids = set()
    for p in PARTICIPANTS:
        all_player_ids.update(p['skaters'])
        all_player_ids.update(p['goalies'])

    players_stats = {}
    for pid in all_player_ids:
        p_data = fetch_json(f"https://api-web.nhle.com/v1/player/{pid}/landing")
        if not p_data:
            continue
            
        raw_pos = p_data.get('position', 'F')
        pos = "G" if raw_pos == 'G' else ("D" if raw_pos == 'D' else "A")
        
        first_name = p_data.get('firstName', {}).get('default', '')
        last_name = p_data.get('lastName', {}).get('default', '')
        full_name = f"{first_name} {last_name}".strip()
        
        stats_dict = {}
        for sub in p_data.get('seasonTotals', []):
            if str(sub.get('season')) == SEASON_ID and sub.get('gameTypeCode') == 2:
                stats_dict = sub
                break
        
        if not stats_dict:
            featured = p_data.get('featuredStats', {}).get('regularSeason', {}).get('subSeason', {})
            if str(p_data.get('featuredStats', {}).get('season', '')) == SEASON_ID:
                stats_dict = featured

        if pos == 'G':
            wins = stats_dict.get('wins', 0)
            shutouts = stats_dict.get('shutouts', 0)
            ot_losses = stats_dict.get('otLosses', 0)
            pts = (wins * 4) + (shutouts * 5) + (ot_losses * 1)
            players_stats[pid] = {
                "name": full_name, "position": "G",
                "wins": wins, "shutouts": shutouts, "otLosses": ot_losses, "points": pts
            }
        else:
            goals = stats_dict.get('goals', 0)
            assists = stats_dict.get('assists', 0)
            pts = (goals * 3) + (assists * 2) if pos == 'D' else (goals * 2) + (assists * 1)
            players_stats[pid] = {
                "name": full_name, "position": pos,
                "goals": goals, "assists": assists, "points": pts
            }

    # 3. Cumul par participant
    leaderboard = []
    for p in PARTICIPANTS:
        att_pts, def_pts, goalie_pts, team_pts = 0, 0, 0, 0
        skater_details, goalie_details, team_details = [], [], []

        for pid in p['skaters']:
            st = players_stats.get(pid, {"name": f"ID {pid}", "points": 0, "goals": 0, "assists": 0, "position": "A"})
            if st.get('position') == 'D':
                def_pts += st.get('points', 0)
            else:
                att_pts += st.get('points', 0)
            skater_details.append(st)

        for pid in p['goalies']:
            st = players_stats.get(pid, {"name": f"ID {pid}", "points": 0, "wins": 0, "shutouts": 0, "otLosses": 0, "position": "G"})
            goalie_pts += st.get('points', 0)
            goalie_details.append(st)

        for tid in p['teams']:
            st = teams_stats.get(tid, {"name": f"Équipe {tid}", "points": 0, "reg_wins": 0, "ot_wins": 0, "ot_losses": 0})
            team_pts += st.get('points', 0)
            team_details.append(st)

        total_points = att_pts + def_pts + goalie_pts + team_pts

        leaderboard.append({
            "name": p['name'],
            "total_points": total_points,
            "att_pts": att_pts,
            "def_pts": def_pts,
            "goalie_pts": goalie_pts,
            "team_pts": team_pts,
            "skaters": skater_details,
            "goalies": goalie_details,
            "teams": team_details
        })

    leaderboard.sort(key=lambda x: x['total_points'], reverse=True)

    # Calcul des tendances
    for new_rank, p in enumerate(leaderboard, start=1):
        old_rank = previous_ranks.get(p["name"])
        if old_rank is None or old_rank == new_rank:
            p["trend"] = "same"
        elif new_rank < old_rank:
            # Nouveau rang plus petit = le participant a monté
            p["trend"] = "up"
        else:
            # Nouveau rang plus grand = le participant a descendu
            p["trend"] = "down"

    output = {
        "season": SEASON_ID,
        "leaderboard": leaderboard
    }
    
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
