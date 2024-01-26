from setuptools import setup

setup(name='assistant_bot',
      version='1.0.0',
      description='Saves contacts - phones and names',
      url='https://github.com/Yuliia-Vogel/bot_helper',
      author='Yuliia Melnychenko',
      author_email='arwen.vogel@gmail.com',
      license='MIT',
      packages=['assistant_bot'],
      install_requires=[],
      entry_points={'console_scripts': ['bot-assistant = assistant_bot.main:main']})