from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def Home(request):
    list_of_num = [i * 7 for i in range(100)]
    careers={
        'Web Developer':['back-end web development technologies such as Node.js or Django','web hosting and deployment technologies such as AWS, Heroku, or Docker','Proficiency in HTML, CSS, and JavaScript','problem solving','web development framework (e.g., React, Angular, Vue)'],
        'Software Developer':['problem solving','programming language (e.g., Python, Java, C++) ','software testing and debugging techniques','software development tools such as IDEs, source control'],
        'Mobile App Developer':['problem solving','mobile development platform (e.g., Android, iOS)','mobile app development tools and frameworks such as Android Studio or Xcode','back-end mobile development technologies such as Firebase or AWS Mobile'],
        'Software Engineer':['Software Developer','Web Developer','Database management','Database design','Data structure and algo'],

        'Data Analyst':['Data cleaning and manipulation','Data visualization','Statistical analysis','Knowledge programming languages such as Python and R','Knowledge of statistical software such as SAS and SPSS'] ,
        'Data Scientist':['Data science','Statistical analysis','Data visualization','Knowledge of programming languages such as Python and R','Knowledge of machine learning libraries such as scikit-learn, TensorFlow, and PyTorch','Knowledge of deep learning and neural networks','Experience with big data technologies such as Hadoop and Spark'],
        'Machine Learning Engineer':['Machine learning algorithms and techniques','Software engineering','Data infrastructure','Knowledge of programming languages such as Python and R','Knowledge of machine learning libraries such as scikit-learn, TensorFlow, and PyTorch','Knowledge of deep learning and neural networks','Experience with big data technologies such as Hadoop and Spark'],
        'Big Data Engineer':['Distributed computing','Big data technologies such as Hadoop and Spark','SQL and NoSQL databases','Software engineering','Knowledge of programming languages such as Python and R'],
        'Data Architect:':['Data modeling','Database design','SQL and NoSQL databases','Knowledge of big data technologies such as Hadoop and Spark'],
        
        'Network Administrator':['Knowledge of networking protocols such as TCP/IP','Network security','Network troubleshooting and problem-solving','Knowledge of network hardware such as routers and switches','Knowledge of scripting and programming languages such as Python and PowerShell','Knowledge of operating systems such as Windows and Linux'],
        'Network Engineer':['Knowledge of network design and implementation','Knowledge of routing and switching protocols','Network security','Network troubleshooting and problem-solving','Knowledge of network hardware such as routers and switches','Knowledge of scripting and programming languages such as Python and PowerShell','Knowledge of operating systems such as Windows and Linux'],
        'Network Architect':['Network Engineer','Knowledge of network protocols and standards','Experience with network security and network performance optimization'],
        'Network Architect':['Network Administrator','Knowledge of network design and implementation','Experience with network security and network performance optimization'],

    }
    domains={
    'Development':{0: 'Experience with big data technologies such as Hadoop and Spark', 1: 'Knowledge of statistical software such as SAS and SPSS', 2: 'Knowledge of Excel, SQL, and programming languages such as Python and R', 3: 'back-end mobile development technologies such as Firebase or AWS Mobile', 4: 'mobile app development tools and frameworks such as Android Studio or Xcode', 5: 'mobile development platform (e.g., Android, iOS)', 6: 'programming language (e.g., Python, Java, C++)', 7: 'back-end web development technologies such as Node.js or Django', 8: 'software development tools such as IDEs, source control', 9: 'software testing and debugging techniques', 10: 'web hosting and deployment technologies such as AWS, Heroku, or Docker', 11: 'Proficiency in HTML, CSS, and JavaScript', 12: 'web development framework (e.g., React, Angular, Vue)'},
    'Math':{13: 'problem solving', 14: 'Data structure and algo', 15: 'Statistical analysis'},
    'Career':{16: 'Software Developer', 17: 'Web Developer', 18: 'Software engineering'},
    'DataBase':{19: 'Database management', 20: 'Database design', 21: 'SQL and NoSQL databases', 22: 'Data infrastructure'},
    'Data':{23: 'Data cleaning and manipulation', 24: 'Data visualization', 25: 'Data science', 26: 'Data modeling'},
    'Network':{27: 'Distributed computing', 28: 'Knowledge of networking protocols such as TCP/IP', 29: 'Network security', 30: 'Network troubleshooting and problem-solving', 31: 'Knowledge of network hardware such as routers and switches', 32: 'Knowledge of scripting and programming languages such as Python and PowerShell', 33: 'Knowledge of operating systems such as Windows and Linux', 34: 'Knowledge of network design and implementation', 35: 'Knowledge of routing and switching protocols', 36: 'Network Engineer', 37: 'Knowledge of network protocols and standards', 38: 'Experience with network security and network performance optimization', 39: 'Network Administrator'},
    'AI':{40: 'Knowledge of machine learning libraries such as scikit-learn, TensorFlow, and PyTorch', 41: 'Knowledge of deep learning and neural networks', 42: 'Machine learning algorithms and techniques'},
    }
        
    allskils={0: 'Experience with big data technologies such as Hadoop and Spark', 1: 'Knowledge of statistical software such as SAS and SPSS', 2: 'Knowledge of Excel, SQL, and programming languages such as Python and R', 3: 'back-end mobile development technologies such as Firebase or AWS Mobile', 4: 'mobile app development tools and frameworks such as Android Studio or Xcode', 5: 'mobile development platform (e.g., Android, iOS)', 6: 'programming language (e.g., Python, Java, C++)', 7: 'back-end web development technologies such as Node.js or Django', 8: 'software development tools such as IDEs, source control', 9: 'software testing and debugging techniques', 10: 'web hosting and deployment technologies such as AWS, Heroku, or Docker', 11: 'Proficiency in HTML, CSS, and JavaScript', 12: 'web development framework (e.g., React, Angular, Vue)', 13: 'problem solving', 14: 'Data structure and algo', 15: 'Statistical analysis', 16: 'Software Developer', 17: 'Web Developer', 18: 'Software engineering', 19: 'Database management', 20: 'Database design', 21: 'SQL and NoSQL databases', 22: 'Data infrastructure', 23: 'Data cleaning and manipulation', 24: 'Data visualization', 25: 'Data science', 26: 'Data modeling', 27: 'Distributed computing', 28: 'Knowledge of networking protocols such as TCP/IP', 29: 'Network security', 30: 'Network troubleshooting and problem-solving', 31: 'Knowledge of network hardware such as routers and switches', 32: 'Knowledge of scripting and programming languages such as Python and PowerShell', 33: 'Knowledge of operating systems such as Windows and Linux', 34: 'Knowledge of network design and implementation', 35: 'Knowledge of routing and switching protocols', 36: 'Network Engineer', 
              37: 'Knowledge of network protocols and standards', 38: 'Experience with network security and network performance optimization', 39: 'Network Administrator', 40: 'Knowledge of machine learning libraries such as scikit-learn, TensorFlow, and PyTorch', 41: 'Knowledge of deep learning and neural networks', 42: 'Machine learning algorithms and techniques'}


  
    
    userskills = []
    Skills=[]
    skillsDict={}
    bestCareer=[]
    careersDict={}
    if request.method == 'POST':
        userskills = request.POST.getlist('userskills[]')
        print(userskills)
    
    for n in userskills:
        Skills.append(allskils[int(n)])
    print(Skills)
    
    for c,s in careers.items():
        if set(s).issubset(set(Skills)):
            bestCareer.append(c)
    print("best",bestCareer)
    for c,s in careers.items():
        score=0
        for skill in s:
            if skill in Skills :
                score=score+1
        if (score != 0):
            careersDict.update({c:score/len(s)*100})
    careerDict=sorted(careersDict.items(),key=lambda x:x[1],reverse=True)
    print(careerDict)
        
    context = {
            
            'data': allskils,
            'domains':domains
            }
    return render(request,"Home.html", context=context)


 