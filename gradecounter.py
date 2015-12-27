import pickle

MENU = '''add a course
            grade points
          select a course
            add assignment category
                category weight
                num assignments
            view course
          list courses'''

class Course:
    def __init__(self, grade_points):
        self.total_points = grade_points
        self.categories = {} #eg: { 'Homework':{'weight':30, 'scores':[0,0,0,0,0,0]}, 'Midterms':{'weight':30, 'scores':[0,0]}, 'Final':{'weight':40, 'scores':[0]} }
        
    def add_cat(self, category, weight, num):
        if category in self.categories:
            if input('Category already exists! Reset? (y/n) ').lower() != 'y':
                return            
        scores = [0 for i in range(num)]
        self.categories[category] = {'weight':weight, 'scores':scores}
        
    def edit_score(self, category, num, score):
        try:
            self.categories[category]['scores'][num] = score
        except KeyError:
            if input('Score out of range! Would you like to append it? (y/n) ').lower() == 'y':
                self.categories[category]['scores'].append(score)
                    
    def average(self):
        avg = 0
        for cat in self.categories:
            catAvg = sum(self.categories[cat]['scores']) / len(self.categories[cat]['scores'])
            avg += self.categories[cat]['weight'] * catAvg
        return round(avg, 3)
    
    def grade_points(self):
        return round((self.average() * self.total_points), 4)
    
    
def test():
    semester1 = []
    OS = Course(3.0)
    OS.add_cat('Exams', .40, 2)
    OS.add_cat('Project1', .05, 1)
    OS.add_cat('Project2', .1, 1)
    OS.add_cat('Project3', .1, 1)
    OS.add_cat('Project4', .15, 1)
    OS.add_cat('Quizzes', .1, 4)
    OS.add_cat('Participation', .1, 1)
    
    print('Average at beginning: ' + str(OS.average()))
    print(repr(OS.categories))
    
    print('Project1')
    OS.edit_score('Project1', 0, .90)
    print('Quiz1')
    OS.edit_score('Quizzes', 0, .90)
    
    print('Average after project1, quiz 1: ' + str(OS.average()))
    
    OS.edit_score('Exams', 0, .85)
    OS.edit_score('Project2', 0, 1)
    OS.edit_score('Participation', 0, .2)
    
    print('Average after more: ' + str(OS.average()))
    
    OS.edit_score('Participation', 0, .75)
    
    print('After more participation: ' + str(OS.average()))
    
test()
    
    
    
