import os

"Disclaimer"
"This Script is only for Education and Knowledge Purposes"

def makeCommits (days : int):

    if days < 1:

        os.system('git push')

    else:

        dates = f"{days} days ago"

        with open('Demo.txt', 'a') as file:

            file.write(f'{dates} <- Commit Listed in a Day!\n')
        
        os.system('git add demo.txt')

        os.system('git commit --date="'+ dates +'" -m "Commit Listed in a Day"')

        return days * makeCommits(days - 1)

makeCommits(200)