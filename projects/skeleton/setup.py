try:
 
    from setuptools import setup
 
except ImportError:
 
    from distutils.core import setup
 
 
config = {
 
    'description': 'Competitive Programming',
    
    'author': 'SolverBot',
    
    'url': 'https://dmoj.ca/user/solverbot',
    
    'download_url': 'https://github.com/Kamalabot/HowCompetitive',
    
    'author_email': 'noname@mymail.com',
    
    'version': ' _._ ',
    
    'install_requires': ['nose'],
    
    'packages': ['NAME'],
    
    'scripts': [],
    
    'name': 'projectname'
    
    }
  
  
setup(**config)