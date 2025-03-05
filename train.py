import musdb

mus = musdb.DB(download=True)
train_tracks = mus.load_mus_tracks(subsets="train")

for track in train_tracks:
    print(f"Track: {track.name}")
    print("Mix:", track.audio.shape)
    print("Vocals:", track.targets['vocals'].audio.shape)
