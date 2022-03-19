# zip everything:
python3 course-files/build/zip_it.py course-files/homework
python3 course-files/build/zip_it.py course-files/lectures
python3 course-files/build/zip_it.py course-files/tutorials

# Build the Project 2 docs
pdoc course-files/projects/project02/apis/yelp.py -o course-files/projects/project02/docs --html --force
pdoc course-files/projects/project02/apis/spotify.py -o course-files/projects/project02/docs --html --force
pdoc course-files/projects/project02/apis/twilio.py -o course-files/projects/project02/docs --html --force
pdoc course-files/projects/project02/apis/authentication.py -o course-files/projects/project02/docs --html --force

python3 course-files/build/zip_it.py course-files/projects

# build indexes:
# python build_navigator.py ../.
