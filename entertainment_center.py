import fresh_tomatoes
import media
# add movie information here
forest_gump = media.Movie("Forest Gump",
	"Slow-witted Forrest Gump (Tom Hanks) has never \
	thought of himself as disadvantaged, and thanks \
	to his supportive mother (Sally Field), he leads \
	anything but a restricted life. Whether dominating \
	on the gridiron as a college football star, \
	fighting in Vietnam or captaining a shrimp boat, \
	Forrest inspires people with his childlike optimism. \
	But one person Forrest cares about most may be the \
	most difficult to save -- his childhood love, the \
	sweet but troubled Jenny (Robin Wright).",
	"http://t3.gstatic.com/images?q=tbn:\
	ANd9GcQCFOcMb5_zkdZg4B4JvIGLlTQTvLdtLjiS5axJJDqP1FaI8Yyx",
	"https://www.youtube.com/watch?v=uPIEn0M8su0")
duckweed = media.Movie("Duckweed",
	"When a son attempts to reconcile with his father, \
	some fateful events allow him to experience his \
	father's life in the past.",
	"http://t1.gstatic.com/images?q=tbn:ANd9GcSLHo\
	jDUMoCl7e_ZKzoFsn74fEEiQYCHAuAFwMJ81YR9HX7hGCb",
	"https://www.youtube.com/watch?v=L1sXeKT5ARM"
	)

kungfu_yoga = media.Movie("Kung Fu Yoga",
	"Jack (Jackie Chan), a world-renowned archaeology \
	professor, and his team are on a grand quest to \
	locate a lost ancient Indian treasure when they \
	are ambushed by a team of mercenaries and left for \
	dead. Using his vast knowledge of history and kung \
	fu, Jack leads his team on a race around the world \
	to beat the mercenaries to the treasure and save an ancient culture.",
	"http://t1.gstatic.com/images?q=tbn:ANd9GcSTH4JAX\
	X6MleUJZNeew9pLomm0Y0Xa6WjJMTz-jgFCgu3z9tQj",
	"https://www.youtube.com/watch?v=5KcwjfPdFC0"
	)
journey_to_the_west = media.Movie("Journey to the West: \
	The Demons Strike Back",
	"A monk (Kris Wu) and his disciples encounter a \
	spider demon and other fantastic creatures on their travels.",
	"http://t2.gstatic.com/images?q=tbn:ANd9GcSZKI\
	9yppcEYchk4D8oBShYkD3ltmfjO6XEmb7UMlcloowdGtL0",
	"https://www.youtube.com/watch?v=PuDEs9_Jsz0")

the_angry_birds = media.Movie("The Angry Birds Movie",
	"Flightless birds lead a mostly happy existence,\
	 except for Red (Jason Sudeikis), who just can't get\
	 past the daily annoyances of life. His temperament\
	 leads him to anger management class, where he meets\
	 fellow misfits Chuck (Josh Gad) and Bomb. \
	 Red becomes even more agitated when his \
	 feathered brethren welcome green pigs to \
	 their island paradise. As the swine begin \
	 to get under his skin, Red joins forces \
	 with Chuck and Bomb to investigate the real \
	 reason behind their mysterious arrival.",
	"http://t3.gstatic.com/images?q=tbn:\
	ANd9GcTL4cM7wCCXjCEoxmzvs_vmiQtNqrpMQ80rgdjABG2_N-IEE-tp",
	"https://www.youtube.com/watch?v=1U2DKKqxHgE"
	)
transformers4 = media.Movie("Transformers: Age of Extinction",
	"After an epic battle, a great city lies in ruins, \
	but the Earth itself is saved. As humanity begins \
	to pick up the pieces, a shadowy group emerges to \
	try to take control of history. Meanwhile, an ancient \
	and powerful new menace sets its sights on Earth. \
	A new group of humans, led by Cade Yeager (Mark Wahlberg), \
	helps Optimus Prime (Peter Cullen) and the Autobots rise \
	up to meet their most fearsome challenge yet: a worldwide \
	war of good versus evil.",
	"http://t0.gstatic.com/images?q=tbn:ANd9GcQiog19jyNY\
	J3uTY5pPNBCaWcS-mfJ8HLBLd58sGwB-1FObtFYX",
	"https://www.youtube.com/watch?v=r8HPIH5JCak")

# add movieNames in the following list
movies = [forest_gump, duckweed, kungfu_yoga, journey_to_the_west, the_angry_birds, transformers4]
fresh_tomatoes.open_movies_page(movies)