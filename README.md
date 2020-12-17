# Multilingual Online Translator
Command-Line project that translates words in 13 languages via web scraping context.reverso.net
 
## This project makes use of the following libraries:
* bs4
* argparse

## Application Features
* Usage: python translator.py [origin language] [target language] [word]
* Scrapes context.reverso.net for top 5 translated word results
* Scrapes context.reverso.net for a single sentence in original and translated language
* Prints data to the terminal and stores it into a file named [word].txt
* You can also select "all" as the target language and get your word translated in 12 other languages!
* Languages supported: "arabic", "german", "english", "spanish", "french", "hebrew", "japanese",
             "dutch", "polish", "portuguese", "romanian", "russian", "turkish"
--------------------
This project is part of the <b>JetBrains Academy Python Developer Plan</b>
