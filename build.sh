# zip everything:
python3 course-files/build/zip_it.py course-files/homeworks
python3 course-files/build/zip_it.py course-files/lectures
python3 course-files/build/zip_it.py course-files/tutorials

python3 course-files/build/zip_it.py ../bain-cs110/tutorial_solutions
python3 course-files/build/zip_it.py ../bain-cs110/exercise_solutions

# T3/HW3 Docs
pdoc --show-source --logo "https://bain-cs110.github.io/assets/images/cs110.png" course-files/tutorials/tutorial3/cs110_t3_shapes -o course-files/tutorials/tutorial3/docs/
pdoc --show-source --logo "https://bain-cs110.github.io/assets/images/cs110.png" course-files/homeworks/hw3/cs110_hw3_shapes -o course-files/homeworks/hw3/docs/

# T4/HW 5 Docs
pdoc --show-source --logo "https://bain-cs110.github.io/assets/images/cs110.png" course-files/tutorials/tutorial4/cs110_t4 -o course-files/tutorials/tutorial4/docs
pdoc --show-source --logo "https://bain-cs110.github.io/assets/images/cs110.png" course-files/homeworks/hw5/cs110_hw5 -o course-files/homeworks/hw5/docs

# P1 Docs
pdoc -t course-files/build/ --show-source --logo "https://bain-cs110.github.io/assets/images/cs110.png" course-files/projects/project1/p1_utilities -o course-files/projects/project1/docs

# HW 7 Docs
# Only run this every once in a while...it has a problem with file paths
#pdoc --show-source --logo "https://bain-cs110.github.io/assets/images/cs110.png" course-files/homeworks/hw7/wordle.py -o course-files/homeworks/hw7/docs
#pdoc --show-source --logo "https://bain-cs110.github.io/assets/images/cs110.png" course-files/homeworks/hw7/cs110_hw7.py -o course-files/homeworks/hw7/docs

# P2 Docs
pdoc --show-source --logo "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Yelp_Logo.svg/800px-Yelp_Logo.svg.png" course-files/projects/project2/apis/yelp -o course-files/projects/project2/docs
pdoc --show-source --logo "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Twilio-logo-red.svg/2560px-Twilio-logo-red.svg.png" course-files/projects/project2/apis/twilio -o course-files/projects/project2/docs
pdoc --show-source --logo "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Spotify_logo_with_text.svg/1024px-Spotify_logo_with_text.svg.png" course-files/projects/project2/apis/spotify -o course-files/projects/project2/docs
pdoc --show-source --logo "https://bain-cs110.github.io/assets/images/cs110.png" course-files/projects/project2/apis/gui -o course-files/projects/project2/docs

python3 course-files/build/zip_it.py course-files/projects

# build indexes:
# python build_navigator.py ../.
