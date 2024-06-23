from setuptools import setup
setup(
   name = 'summarize',
   version = '1.0.11',
   author = 'aroun coumar',
   description = 'summarize the text',
   packages = ['summarize'],
   install_requires = ['docopt','requests','pandas'],
   entry_points = {
      'console_scripts': [
         'summarize=summarize:main'
      ]
   }
)