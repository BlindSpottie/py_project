# JBI010 Assignment 2026-2027

## Spotify Music Recommendation and Playlist Generation

This folder contains the starter files for the JBI010 programming assignment.

In this assignment, you will work with a cleaned Spotify tracks dataset. You will implement Python classes to represent tracks, load and validate data from a CSV file, analyze track similarity, generate playlists, and write tests for your implementation.

## Folder Structure

```text
Assignment/
│
├── data/
│   └── spotify_tracks.csv
│
├── tests/
│   ├── test_music_analyzer.py
│   ├── test_music_library.py
│   ├── test_playlist.py
│   └── test_track.py
│
├── dashboard.py
├── music_analyzer.py
├── music_library.py
├── playlist.py
└── track.py
```

## Files You Need to Edit

You should implement your solution in the following files:

```text
track.py
music_library.py
music_analyzer.py
playlist.py
dashboard.py
```

Do not rename these files. Do not move them to another folder. The automated tests depend on the file names and structure.

Your implementation must include the required parameters, type hints, meaningful docstrings, and code according to the assignment specification.

## Dataset

The dataset is located at:

```text
data/spotify_tracks.csv
```

Do not rename or move this file.

## Running the Tests

This assignment uses `pytest`.

Open a terminal in the assignment folder and run:

```bash
python -m pytest tests -q
```

To run a single test file:

```bash
python -m pytest tests/test_track.py -q
```

```bash
python -m pytest tests/test_music_library.py -q
```

```bash
python -m pytest tests/test_music_analyzer.py -q
```

```bash
python -m pytest tests/test_playlist.py -q
```

The provided tests are only example tests. They do not cover every situation. You are required to extend these test files by implementing your own pytests to check edge cases. Your final submission will also be evaluated using hidden staff test suite.

## Installing pytest

If `pytest` is not installed, run:

```bash
python -m pip install pytest
```

Then run the tests again:

```bash
python -m pytest tests -q
```
