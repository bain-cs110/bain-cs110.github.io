# zip everything:
python3 course-files/build/zip_it.py course-files/homeworks
python3 course-files/build/zip_it.py course-files/lectures
python3 course-files/build/zip_it.py course-files/tutorials

python3 course-files/build/zip_it.py ../bain-cs110/tutorial_solutions
python3 course-files/build/zip_it.py ../bain-cs110/exercise_solutions

pdoc --show-source course-files/projects/project01/project_utilities -o course-files/projects/project01/docs



# build indexes:
# python build_navigator.py ../.
