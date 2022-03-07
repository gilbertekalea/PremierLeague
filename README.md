
## **Scraping Bot for English Premier League**
[English Premier League](https://www.premierleague.com/) 

The Premier League, also known exonymously as the English Premier League or the EPL, is the top level of the English football league system. Contested by 20 clubs, it operates on a system of promotion and relegation with the English Football League. Seasons run from August to May with each team playing 38 matches.

## **Description**
Premier League bot is a scraping bot built with *selenium* and *python*. The project is structure in two components.

## **Scraping component**
Contain methods that allow the bot crawl the premier league website and collects current/past season table data. Then, stores the data in a csv file. 

## **Data manipulation component**
Containt methods to perform retrieving data from the csv file and display it on the terminal, contain also methods for performing basic statistical analysis such as determining teams current win-draw-lose rate. 

## **Motivation**
The motivation behind this project was to improve my web scraping skills. I choose premier league because I love soccer and I am passionate about it. Also, the website is dynamic with lots of javascript which make it even harder to scrape it with standard libraries such as *BeautifulSoup*. By doing this project, it allow me to emphasis advanced technique of scraping modern websites. 

## **Technology Used**

    Technology used : Python
    Framework : Selenium 

## **Installation**
In order for this project to work in your computer; You need to have a selenium and python installed in your computer. 
I assume if you are interested in this project,you have already know the basics of python and you have python installed. 

For window users: Open windows terminal and open project directory, then.

    pip install selenium

## **Drivers**
Selenium requires a driver to interface with the chosen browser. Firefox, for example, requires geckodriver, which needs to be installed before the below examples can be run. Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin.

Read more about webdrivers here [Selenium Installation](https://pypi.org/project/selenium/) and [Selenium Official documentation](https://www.selenium.dev/documentation/webdriver/)


## **Downloading WebDriver**
This project uses chromedriver. I understand that you're using a different browser;

Here are download links for most popular browsers. 

[Chrome](https://chromedriver.chromium.org/downloads)

[Firefox](https://github.com/mozilla/geckodriver/releases)

[Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

[Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)

Once you download your prefered driver; You can either save the .exe file in your project folder or you can save it somewhere in the your computer and provide the path. I recommend you use save it in a different folder within the project folder or somewhere in your computer and use system path methods to access it. 

Here are the files you need to change; Go to *starting_point.py* in *premier_league* folder/module. Go to class *BotStartingPoint* and change the webdriver.chrome to web driver of your choice. Then change the driver_path paramenter equals to the path where your webdriver is stored. 

For example,mine is stored in folder called **SeleniumDrivers** 

Path **C:\Users\gilbe\Desktop\SeleniumDrivers**

Lastly, you can now change ChromeOptions() to equal to web driver of your choice. 

    class BotStartingPoint(webdriver.Firefox)
        def __init__(self, driver_path=r"C:\Users\gilbe\Desktop\SeleniumDrivers", teardown=True):
            self.driver_path = driver_path
            self.teardown = teardown
            os.environ["PATH"] += self.driver_path
            options = webdriver.ChromeOptions()


## **How to use**
You are now ready to explore and use the bot. Go to project directory and type python

    C:\Users\gilbe\Desktop\workstation\personal projects\python projects\webscraping\selenium\premierleaguebot> python


You will get an output like this;

    Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

The most import action to take here is to import run module

    >>> import run
Next, start the bot:

    >>> run.start_scraping()

The bot will wake up and print out the starting url. The it will automatically open a new browser window. Check your windows terminal; The bot will prompt you to enter which season you want to scrape data from: Basically the bot wants to know if you are interested to scrape past seasons table or current season. This is because the table structure for current and past seasons are quite different. So there are different methods to scrape the data. You can type C for current season or P for past seasons. 

**Note**
If you select C who the bot will automatically select the '2021/22' season. If you select P, you will be prompted to enter the season itself. Please refer to premier league season naming format: here is example, if you want to scrape data for 
2013 season, the format will be 2013/14, meaning that the season started on August 2013 and it goes through to may 2014. The 2014 seasons starts on August 2014 and ends on may 2015, the season format will be 2014/15. 

    >>> Current Season or Past? C | P : 

If you choose C  or P, you will be prompted to choose which type of data you would like to scrape;

Home - Only games played at home for each team

Away - Only matches played for away for each team.

All Matches - Scrapes all table data for both home and away. 

    >>> Enter Home | Away | All Matches: 

The bot will start now collecting data for you and saves this data in csv file.

## **Basic Stistical Analysis**

The next step is do some basic operations about the data you have collected.

To perform this operations  call view_premier(team_name) function.  This function receives a paramenter team_name which represents the name of the team you are interested in. Then it goes through csv file and creates instance of each team and returns object where the team_name matches. 

    >>> obj = run.view_premier('Manchester United')

Now you can do alot more operations

    >>> Obj.get_next_game()
        Manchester United next game fixture:

        +-------------------+----+-----------------+----------------------+-------+
        |    Current Team   |    |     Opponent    |         date         |  time |
        +-------------------+----+-----------------+----------------------+-------+
        | Manchester United | vs | Manchester City | Sunday 06 March 2022 | 16:30 |
        +-------------------+----+-----------------+----------------------+-------+

    >>> obj.get_wdl_rate()
        Manchester United win, draw and lose rate for all matches. 
        +-------------------+--------------+----------+-----------+------------+
        |        Club       | Games Played | Win rate | draw rate | Loose rate |
        +-------------------+--------------+----------+-----------+------------+
        | Manchester United |      27      |   0.48   |    0.3    |    0.22    |
        +-------------------+--------------+----------+-----------+------------+

    >>> obj.compare('Chelsea')
        MANCHESTER UNITED WIN, DRAW & LOOSE RATE AFTER 27 GAMES
        +-------------------+--------------+----------+-----------+------------+
        |        Club       | Games Played | Win rate | draw rate | Loose rate |
        +-------------------+--------------+----------+-----------+------------+
        | Manchester United |      27      |   0.48   |    0.3    |    0.22    |
        +-------------------+--------------+----------+-----------+------------+

        CHELSEA WIN, DRAW & LOOSE RATE AFTER 26 GAMES
        +---------+--------------+----------+-----------+------------+
        |   Club  | Games Played | Win rate | draw rate | Loose rate |
        +---------+--------------+----------+-----------+------------+
        | Chelsea |      26      |   0.58   |    0.31   |    0.12    |
        +---------+--------------+----------+-----------+------------+

## **Contribute**
Please feel free to contribute to this project. Anyone is allowed to contribute. 
