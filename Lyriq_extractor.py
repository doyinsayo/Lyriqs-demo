from lyrics_extractor import SongLyrics 

# using genius api

api_key = 'AIzaSyDM2uJ-CweOkPkZ3xLiyelKDprN8iarBDM'
engine_ID = 'f93d78b2384fc85e2'

extract_lyriq = SongLyrics(api_key, engine_ID)
lyriqs = extract_lyriq.get_lyrics("Sungba")
print(lyriqs)
print(lyriqs['title'])
