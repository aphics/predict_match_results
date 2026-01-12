import os


def get_leagues():
    files = os.listdir("db")
    leagues = []
    for l in files:
        if "final" in l:
            league = l.split("_")[0]
            if league not in leagues:
                leagues.append(league)
    return leagues


if __name__ == "__main__":
    get_leagues()
