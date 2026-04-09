import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into a list of dictionaries."""
    songs: List[Dict] = []

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Compute a weighted score and reasons for one song vs user preferences."""
    score = 0.0
    reasons: List[str] = []

    def add_points(points: float, reason: str) -> None:
        """Add weighted points and record the matching reason."""
        nonlocal score
        score += points
        reasons.append(reason)

    preferred_genre = user_prefs.get("genre")
    if preferred_genre and song.get("genre") == preferred_genre:
        add_points(1.5, f"genre matches {preferred_genre}")

    preferred_mood = user_prefs.get("mood")
    if preferred_mood and song.get("mood") == preferred_mood:
        add_points(2.0, f"mood matches {preferred_mood}")

    target_energy = user_prefs.get("energy")
    if target_energy is not None:
        energy_diff = abs(float(song.get("energy", 0.0)) - float(target_energy))
        if energy_diff <= 0.1:
            add_points(4.0, "energy is very close to the target")
        elif energy_diff <= 0.2:
            add_points(2.0, "energy is reasonably close to the target")
        else:
            add_points(-2.0, "energy is far from the target")

    target_tempo = user_prefs.get("tempo_bpm")
    if target_tempo is not None:
        tempo_diff = abs(float(song.get("tempo_bpm", 0.0)) - float(target_tempo))
        if tempo_diff <= 10:
            add_points(1.5, "tempo is very close to the target")
        elif tempo_diff <= 25:
            add_points(0.5, "tempo is somewhat close to the target")
        else:
            add_points(-1.0, "tempo is far from the target")

    target_valence = user_prefs.get("valence")
    if target_valence is not None:
        valence_diff = abs(float(song.get("valence", 0.0)) - float(target_valence))
        if valence_diff <= 0.1:
            add_points(1.0, "valence is very close to the target")
        elif valence_diff <= 0.25:
            add_points(0.5, "valence is somewhat close to the target")
        else:
            add_points(-0.5, "valence is far from the target")

    target_danceability = user_prefs.get("danceability")
    if target_danceability is not None:
        danceability_diff = abs(float(song.get("danceability", 0.0)) - float(target_danceability))
        if danceability_diff <= 0.1:
            add_points(1.0, "danceability is very close to the target")
        elif danceability_diff <= 0.25:
            add_points(0.5, "danceability is somewhat close to the target")
        else:
            add_points(-0.5, "danceability is far from the target")

    target_acousticness = user_prefs.get("acousticness")
    if target_acousticness is None and "likes_acoustic" in user_prefs:
        target_acousticness = 0.8 if user_prefs.get("likes_acoustic") else 0.2

    if target_acousticness is not None:
        acousticness_diff = abs(float(song.get("acousticness", 0.0)) - float(target_acousticness))
        if acousticness_diff <= 0.1:
            add_points(1.0, "acousticness matches the target")
        elif acousticness_diff <= 0.25:
            add_points(0.5, "acousticness is somewhat close to the target")
        else:
            add_points(-0.5, "acousticness is far from the target")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top-k ranked songs with score and explanation text."""


    ranked_songs: List[Tuple[Dict, float, str]] = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons) if reasons else "No strong matches, but included in the ranking"
        ranked_songs.append((song, score, explanation))

    ranked_songs.sort(key=lambda item: (-item[1], item[0]["title"]))
    return ranked_songs[:k]
