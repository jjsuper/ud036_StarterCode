import media

# Create instances of movie
dunkirk = media.Movie("Dunkirk",
                      "http://t3.gstatic.com/images?q=tbn:ANd9GcSi8V"
                      "mNoMYm77iHAsAdsZhABzm_idRwgsU-r3njA4F6HY3-xceC",
                      "https://www.youtube.com/watch?v=T7O7BtBnsG4")

spider_man = media.Movie("Spider-Man: Homecoming",
                         "http://t0.gstatic.com/images?q=tbn:ANd9GcT8W"
                         "3Fe7DD101g0M7OCalJN9u675sQAJFslGCjvs74PTOfEKt_t",
                         "https://www.youtube.com/watch?v=OiyeBWwlvsY")

emoji = media.Movie("The Emoji Movie",
                    "http://t0.gstatic.com/images?q=tbn:ANd9GcRQc0"
                    "pj8eAuiJa5K_DX1MeTSWwQCX5mDaBWz8auP38FeUX7NX5V",
                    "https://www.youtube.com/watch?v=wc_dT5-chuc")

# Create a list of these movie objects
movies = [dunkirk, spider_man, emoji]
