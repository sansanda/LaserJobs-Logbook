import os

def main():
    path = 'E:\\repos\\LaserJobs-Manager\\persistence\\data\\laserJobs.xlsx'
    print(type(os.path.split(path)[1]))

main()