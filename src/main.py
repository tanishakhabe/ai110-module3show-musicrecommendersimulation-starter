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

    # Profile 1: High-Energy Pop
    high_energy_pop = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.9,
        "tempo_bpm": 130,
        "valence": 0.85,
        "danceability": 0.9,
        "acousticness": 0.1,
    }

    # Profile 2: Chill Lofi
    # Compared to High-Energy Pop, this should shift the top results toward lofi and away from high-energy pop,
    # because the genre and mood preferences change and the target energy drops sharply.
    chill_lofi = {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.35,
        "tempo_bpm": 75,
        "valence": 0.6,
        "danceability": 0.55,
        "acousticness": 0.85,
    }

    # Profile 3: Deep Intense Rock
    # Compared to Chill Lofi, this should favor louder, faster songs and penalize calm acoustic tracks,
    # which makes sense because the desired genre, mood, and tempo all move in the opposite direction.
    deep_intense_rock = {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.92,
        "tempo_bpm": 150,
        "valence": 0.45,
        "danceability": 0.62,
        "acousticness": 0.12,
    }

    # Profile 4: Hype Sad
    # Compared to Deep Intense Rock, this keeps the energy high but changes the mood and genre,
    # so the output should still lean energetic while shifting away from rock-specific matches.
    hype_sad = {
        "genre": "hip-hop",
        "mood": "sad",
        "energy": 0.85,
        "tempo_bpm": 110,
        "valence": 0.3,
        "danceability": 0.8,
        "acousticness": 0.2,
    }

    # Profile 5: Intense Pop with Chill Preferences
    # Compared to Hype Sad, this creates a conflict: the genre prefers pop and intense tracks,
    # but the energy, valence, and acousticness preferences point toward a much calmer sound.
    # That should produce mixed recommendations because the score has to balance competing signals.
    intense_pop_chill = {
        "genre": "pop",
        "mood": "intense",
        "energy": 0.2,
        "tempo_bpm": 60,
        "valence": 0.2,
        "danceability": 0.2,
        "acousticness": 0.95
        }
    

    # Profile 6: Missing Features
    # Compared to Intense Pop with Chill Preferences, this is much less specific,
    # so the output should rely mostly on genre and produce tighter ties among lofi songs.
    missing_features = {
        "genre": "lofi"}

    # Pick which profile to run.
    user_prefs = hype_sad
    profile_name = f"{user_prefs}"
    

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 64)
    print(f"USER PROFILE: {profile_name}")
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
