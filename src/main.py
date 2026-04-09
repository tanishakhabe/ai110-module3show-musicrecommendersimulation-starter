"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example taste profile with target values for every feature
    # the recommender can compare against.
    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "tempo_bpm": 120,
        "valence": 0.85,
        "danceability": 0.8,
        "acousticness": 0.2,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 64)
    print("TOP RECOMMENDATIONS")
    print("=" * 64)

    for idx, rec in enumerate(recommendations, start=1):
        # Returned format: (song_dict, score, explanation_string)
        song, score, explanation = rec
        reasons = [reason.strip() for reason in explanation.split(";") if reason.strip()]

        print(f"\n[{idx}] {song['title']}")
        print(f"Final Score : {score:.2f}")
        print("Reasons:")
        for reason in reasons:
            print(f"  - {reason}")
        print("-" * 64)


if __name__ == "__main__":
    main()
