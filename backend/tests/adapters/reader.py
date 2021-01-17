# import pandas as pd



# root = 'api'
# filename = 'get_category_rankings_'
# platform = 'android' or 'iOS'
# date = '20201227'

# define function that will read json file (root, filename, date)
#   split each list into free, paid, grossing = 0,1,2
#   list of top 100 games
#       insert into db




# df = pd.read_json('get_category_rankings_android_20201227.json')
# df.to_dict('records')
# game = df[0][0]

# games table
# game['name']
# game['platform']
# game['publisher']
# rawg {'search' : game['name']}, temp[0]['released'], enter NULL 
# game['categories'] = ['game_action','game']
# igdb ig.find_game_engine('Among Us')

# earnings table
# game_id
# game['price'] = 0.0
# game['in_app_purchases'] = True/False
# game['humanized_worldwide_last_month_revenue']['revenue']
# game['humanized_worldwide_last_month_downloads']['downloads']

# ratings table
# game_id
# rawg {'search' : game['name']}, temp[0]['metacritic']
# game['rating']
# 'FREE' rank_type
# game['rank']
# '20201227' date_of_file

# # seeding games
# amongus = db.save(models.Game(name = 'Among Us', platform = 'android', publisher = 'Innersloth LLC', release_date = '2018-07-25', genre = 'action', game_engine = 'Unity'), test_conn, cursor)
# roblox = db.save(models.Game(name = 'Roblox', platform = 'android', publisher = 'Roblox Corporation', release_date = '2019-12-31', genre = 'building', game_engine = 'Something Else'), test_conn, cursor)
# candy = db.save(models.Game(name = 'Candy Crush Saga', platform = 'android', publisher = 'King', release_date = '2015-1-1', genre = 'casual', game_engine = 'Candy Factory'), test_conn, cursor)
# amongus_ios = db.save(models.Game(name = 'Among Us', platform = 'iOS', publisher = 'Innersloth LLC', release_date = '2018-11-2', genre = 'action', game_engine = 'Unity'), test_conn, cursor)
# # seeding ratings
# amongus_r = db.save(models.Rating(game_id = amongus.id, metacritic = 84, TS_rating = 4.465, rank_type = 'top free', ranking = 1, date_created = '2020-12-01'), test_conn, cursor)
# roblox_r = db.save(models.Rating(game_id = roblox.id, metacritic = 90, TS_rating = 4.48, rank_type = 'top free', ranking = 2, date_created = '2020-12-02'), test_conn, cursor)
# candy_r = db.save(models.Rating(game_id = candy.id, metacritic = 75, TS_rating = 4.1, rank_type = 'top grossing', ranking = 3, date_created = '2020-12-03'), test_conn, cursor)
# amongus_ios_r = db.save(models.Rating(game_id = amongus_ios.id, metacritic = 84, TS_rating = 4.465, rank_type = 'top free', ranking = 1, date_created = '2020-12-01'), test_conn, cursor)
# # seeding earnings
# amongus_e = db.save(models.Earnings(game_id = amongus.id, price = 0.00, inapp = True, revenue = 35000000, downloads = 100000), test_conn, cursor)
# roblox_e = db.save(models.Earnings(game_id = roblox.id, price = 0.01, inapp = False, revenue = 50000000, downloads = 200000), test_conn, cursor)
# candy_e = db.save(models.Earnings(game_id = candy.id, price = 0.50, inapp = True, revenue = 100000000, downloads = 300000), test_conn, cursor)
# amongus_ios_e = db.save(models.Earnings(game_id = amongus_ios.id, price = 1.00, inapp = False, revenue = 2000000, downloads = 75000), test_conn, cursor)




mobilegaming_development=# SELECT g.name, r.rank_type, r.ranking, COUNT(r.ranking) FROM ratings AS r JOIN games AS g ON g.id = r.game_id GROUP BY g.name, r.rank_type, r.ranking ORDER BY g.name, r.ranking;
                            name                             |  rank_type   | ranking | count 
-------------------------------------------------------------+--------------+---------+-------
 60 Parsecs!                                                 | top paid     |      84 |     1
 60 Seconds! Atomic Adventure                                | top paid     |      16 |     1
 8 Ball Pool                                                 | top grossing |      74 |     1
 8 Ball Pool                                                 | top free     |      77 |     1
 AFK Arena                                                   | top grossing |      26 |     1
 Acrylic Nails!                                              | top free     |      16 |     1
 Alien: Blackout                                             | top paid     |      82 |     1
 Among Us                                                    | top free     |       1 |     2
 Among Us                                                    | top grossing |      99 |     1
 Among Us!                                                   | top free     |       1 |     1



 mobilegaming_development=# SELECT g.name, r.rank_type, r.ranking, COUNT(r.ranking) FROM ratings AS r JOIN games AS g ON g.id = r.game_id GROUP BY g.name, r.rank_type, r.ranking ORDER BY r.ranking, g.name;
                            name                             |  rank_type   | ranking | count 
-------------------------------------------------------------+--------------+---------+-------
 Among Us                                                    | top free     |       1 |     2
 Among Us!                                                   | top free     |       1 |     1
 Minecraft                                                   | top paid     |       1 |     3
 Roblox                                                      | top grossing |       1 |     3
 Bloons TD 6                                                 | top paid     |       2 |     2
 Clash of Clans                                              | top grossing |       2 |     1
 Coin Master                                                 | top grossing |       2 |     2
 Heads Up!                                                   | top paid     |       2 |     1
 Project Makeover                                            | top free     |       2 |     1
 Sushi Roll 3D                                               | top free     |       2 |     2
 Bloons TD 6                                                 | top paid     |       3 |     1
 Candy Crush Saga                                            | top grossing |       3 |     2
 DRAGON BALL Z DOKKAN BATTLE                                 | top grossing |       3 |     1
 Hit Master 3D                                               | top free     |       3 |     2
 Monopoly - Board game classic about real-estate!            | top paid     |       3 |     2
 Oh God!                                                     | top free     |       3 |     1
 Garena Free Fire-New Beginning                              | top grossing |       4 |     1
 Stacky Dash                                                 | top free     |       4 |     1
 Stardew Valley                                              | top paid     |       4 |     1
 DOP 2: Delete One Part                                      | top free     |       5 |     1
 Incredibox                                                  | top paid     |       5 |     1
 Pokemon GO                                                  | top grossing |       5 |     1


 mobilegaming_development=# SELECT g.name, g.genre, r.rank_type, r.ranking, COUNT(r.ranking) FROM ratings AS r JOIN games AS g ON g.id = r.game_id GROUP BY g.name, g.genre, r.rank_type, r.ranking ORDER BY r.ranking, g.name;
                            name                             |          genre           |  rank_type   | ranking | count 
-------------------------------------------------------------+--------------------------+--------------+---------+-------
 Among Us                                                    | action                   | top free     |       1 |     3
 Among Us!                                                   | action                   | top free     |       1 |     1
 Coin Master                                                 | casual                   | top grossing |       1 |     3
 Minecraft                                                   | arcade                   | top paid     |       1 |    10
 Project Makeover                                            | casual                   | top free     |       1 |     4
 Roblox                                                      | adventure                | top grossing |       1 |     7
 Sushi Roll 3D                                               | simulation               | top free     |       1 |     2
 Among Us                                                    | action                   | top free     |       2 |     1
 Among Us!                                                   | action                   | top free     |       2 |     2
 Bloons TD 6                                                 | strategy                 | top paid     |       2 |     5
 Candy Crush Saga                                            | casual                   | top grossing |       2 |     3
 Clash of Clans                                              | strategy                 | top grossing |       2 |     2
 Coin Master                                                 | casual                   | top grossing |       2 |     2
 Heads Up!                                                   | [6014, 6016, 7019, 7005] | top paid     |       2 |     3
 Monopoly                                                    | board                    | top paid     |       2 |     2
 Project Makeover                                            | casual                   | top free     |       2 |     1
 Red Imposter                                                | action                   | top free     |       2 |     1
 Roblox                                                      | adventure                | top grossing |       2 |     3
 Sushi Roll 3D                                               | simulation               | top free     |       2 |     3
 WidgetPet!                                                  | [6014, 7015, 6016, 7014] | top free     |       2 |     2
 Among Us!                                                   | action                   | top free     |       3 |     2
 Bloons TD 6                                                 | strategy                 | top paid     |       3 |     3
 Candy Crush Saga                                            | casual                   | top grossing |       3 |     5
 DRAGON BALL Z DOKKAN BATTLE                                 | action                   | top grossing |       3 |     1
 Heads Up!                                                   | [6014, 6016, 7019, 7005] | top paid     |       3 |     1
 Hit Master 3D                                               | action                   | top free     |       3 |     2
 Monopoly                                                    | board                    | top paid     |       3 |     1
 Monopoly - Board game classic about real-estate!            | board                    | top paid     |       3 |     5
 Oh God!                                                     | [6014, 7015, 7003]       | top free     |       3 |     2
 Pokemon GO                                                  | adventure                | top grossing |       3 |     4


 mobilegaming_development=# SELECT g.name, e.revenue, r.rank_type, r.ranking, COUNT(r.ranking) FROM ratings AS r JOIN games AS g ON g.id = r.game_id JOIN earnings AS e ON g.id = e.game_id WHERE r.rank_type = 'top grossing' GROUP BY g.name, e.revenue, r.rank_type, r.ranking ORDER BY r.ranking, g.name;
                            name                             | revenue  |  rank_type   | ranking | count 
-------------------------------------------------------------+----------+--------------+---------+-------
 Coin Master                                                 | 55000000 | top grossing |       1 |     3
 Roblox                                                      | 37000000 | top grossing |       1 |     2
 Roblox                                                      | 60000000 | top grossing |       1 |     5
 Candy Crush Saga                                            | 34000000 | top grossing |       2 |     3
 Clash of Clans                                              | 31000000 | top grossing |       2 |     2
 Coin Master                                                 | 55000000 | top grossing |       2 |     2
 Roblox                                                      | 37000000 | top grossing |       2 |     3
 Candy Crush Saga                                            | 26000000 | top grossing |       3 |     5
 DRAGON BALL Z DOKKAN BATTLE                                 | 11000000 | top grossing |       3 |     1
 Pokemon GO                                                  | 51000000 | top grossing |       3 |     4
 Candy Crush Saga                                            | 34000000 | top grossing |       4 |     1
 Coin Master                                                 | 27000000 | top grossing |       4 |     2
 Garena Free Fire-New Beginning                              | 43000000 | top grossing |       4 |     3
 Homescapes                                                  | 36000000 | top grossing |       4 |     1
 Pokemon GO                                                  | 61000000 | top grossing |       4 |     1
 Clash of Clans                                              | 31000000 | top grossing |       5 |     1
 DRAGON BALL Z DOKKAN BATTLE                                 | 11000000 | top grossing |       5 |     1
 Garena Free Fire-New Beginning                              | 18000000 | top grossing |       5 |     1
 Garena Free Fire-New Beginning                              | 43000000 | top grossing |       5 |     1
 Pokemon GO                                                  | 61000000 | top grossing |       5 |     3
 Project Makeover                                            | 12000000 | top grossing |       5 |     1


mobilegaming_development=# SELECT g.name, e.revenue, r.rank_type, r.ranking, COUNT(r.ranking) FROM ratings AS r JOIN games AS g ON g.id = r.game_id JOIN earnings AS e ON g.id = e.game_id WHERE r.rank_type = 'top free' GROUP BY g.name, e.revenue, r.rank_type, r.ranking ORDER BY r.ranking, g.name;
                        name                        | revenue  | rank_type | ranking | count 
----------------------------------------------------+----------+-----------+---------+-------
 Among Us                                           |  2000000 | top free  |       1 |     3
 Among Us!                                          |  6000000 | top free  |       1 |     1
 Project Makeover                                   | 12000000 | top free  |       1 |     4
 Sushi Roll 3D                                      |     1000 | top free  |       1 |     2
 Among Us                                           |  2000000 | top free  |       2 |     1
 Among Us!                                          |  6000000 | top free  |       2 |     2
 Project Makeover                                   | 12000000 | top free  |       2 |     1
 Red Imposter                                       |     1000 | top free  |       2 |     1
 Sushi Roll 3D                                      |     1000 | top free  |       2 |     3
 WidgetPet!                                         |    20000 | top free  |       2 |     2
 Among Us!                                          |  6000000 | top free  |       3 |     2
 Hit Master 3D                                      |     1000 | top free  |       3 |     2
 Oh God!                                            |     1000 | top free  |       3 |     2
 Project Makeover                                   |  7000000 | top free  |       3 |     1
 Stacky Dash                                        |     1000 | top free  |       3 |     2
 WidgetPet!                                         |    20000 | top free  |       3 |     1
 Among Us                                           |  2000000 | top free  |       4 |     1
 Hit Master 3D                                      |     1000 | top free  |       4 |     1
 Oh God!                                            |     1000 | top free  |       4 |     1
 Project Makeover                                   |  7000000 | top free  |       4 |     1
 Roof Rails                                         |    20000 | top free  |       4 |     1
 Stacky Dash                                        |     1000 | top free  |       4 |     1
 Sushi Roll 3D                                      |     1000 | top free  |       4 |     2
 DOP 2: Delete One Part                             |     1000 | top free  |       5 |     1
 Jump Dunk 3D                                       |     1000 | top free  |       5 |     1
 Red Imposter                                       |     1000 | top free  |       5 |     1
 Roblox                                             | 60000000 | top free  |       5 |     1
 Roof Rails                                         |    20000 | top free  |       5 |     1
 Stacky Dash                                        |     1000 | top free  |       5 |     1
 Sushi Roll 3D                                      |     1000 | top free  |       5 |     2


mobilegaming_development=# SELECT g.name, e.revenue, r.rank_type, r.ranking, COUNT(r.ranking) FROM ratings AS r JOIN games AS g ON g.id = r.game_id JOIN earnings AS e ON g.id = e.game_id WHERE r.rank_type = 'top paid' GROUP BY g.name, e.revenue, r.rank_type, r.ranking ORDER BY r.ranking, g.name;
                       name                       | revenue  | rank_type | ranking | count 
--------------------------------------------------+----------+-----------+---------+-------
 Minecraft                                        |  4000000 | top paid  |       1 |     5
 Minecraft                                        | 10000000 | top paid  |       1 |     5
 Bloons TD 6                                      |   600000 | top paid  |       2 |     5
 Heads Up!                                        |   800000 | top paid  |       2 |     3
 Monopoly                                         |   700000 | top paid  |       2 |     2
 Bloons TD 6                                      |  1000000 | top paid  |       3 |     3
 Heads Up!                                        |   800000 | top paid  |       3 |     1
 Monopoly                                         |   700000 | top paid  |       3 |     1
 Monopoly - Board game classic about real-estate! |   300000 | top paid  |       3 |     5
 Bloons TD 6                                      |  1000000 | top paid  |       4 |     2
 Heads Up!                                        |   800000 | top paid  |       4 |     1
 Monopoly                                         |   700000 | top paid  |       4 |     1
 Stardew Valley                                   |   200000 | top paid  |       4 |     1
 THE GAME OF LIFE 2                               |    90000 | top paid  |       4 |     3
 Incredibox                                       |    50000 | top paid  |       5 |     1
 Incredibox                                       |   300000 | top paid  |       5 |     1
 Plague                                           |   300000 | top paid  |       5 |     3
 Stardew Valley                                   |   200000 | top paid  |       5 |     3


mobilegaming_development=# SELECT g.name, g.platform, e.revenue, e.downloads, r.rank_type, r.ranking, 
                            COUNT(r.ranking) FROM ratings AS r JOIN games AS g ON g.id = r.game_id JOIN earnings AS e ON g.id = e.game_id 
                            WHERE r.rank_type = 'top free' GROUP BY g.name, g.platform, e.revenue, e.downloads, r.rank_type, r.ranking 
                            ORDER BY r.ranking, g.name;
          name          | platform | revenue  | downloads | rank_type | ranking | count 
------------------------+----------+----------+-----------+-----------+---------+-------
 Among Us               | android  |  2000000 |  29000000 | top free  |       1 |     3
 Among Us!              | iOS      |  6000000 |  12000000 | top free  |       1 |     1
 Project Makeover       | iOS      | 12000000 |   7000000 | top free  |       1 |     2
 Among Us!              | iOS      |  6000000 |  12000000 | top free  |       2 |     2
 Project Makeover       | iOS      | 12000000 |   7000000 | top free  |       2 |     1
 Sushi Roll 3D          | android  |     1000 |  21000000 | top free  |       2 |     3
 Hit Master 3D          | android  |     1000 |   4000000 | top free  |       3 |     2
 Oh God!                | iOS      |     1000 |   3000000 | top free  |       3 |     2
 Stacky Dash            | android  |     1000 |   2000000 | top free  |       3 |     1
 WidgetPet!             | iOS      |    20000 |    300000 | top free  |       3 |     1
 Hit Master 3D          | android  |     1000 |   4000000 | top free  |       4 |     1
 Oh God!                | iOS      |     1000 |   3000000 | top free  |       4 |     1
 Roblox                 | iOS      | 60000000 |   4000000 | top free  |       4 |     1
 Stacky Dash            | android  |     1000 |   2000000 | top free  |       4 |     2
 Sushi Roll 3D          | iOS      |     1000 |   5000000 | top free  |       4 |     1
 DOP 2: Delete One Part | android  |     1000 |   9000000 | top free  |       5 |     2
 Jump Dunk 3D           | android  |     1000 |   5000000 | top free  |       5 |     1
 Jump Dunk 3D           | iOS      |     1000 |   1000000 | top free  |       5 |     1
 Roblox                 | iOS      | 60000000 |   4000000 | top free  |       5 |     1
 Sushi Roll 3D          | iOS      |     1000 |   5000000 | top free  |       5 |     1

import datetime

temp = datetime.date(day=10)

 {"app_id":1153461915,"canonical_country":"US","name":"Idle Heroes - Idle Games","publisher_name":"DHGames Limited","publisher_id":463987809,"humanized_name":"Idle Heroes","icon_url":"https://is4-ssl.mzstatic.com/image/thumb/Purple114/v4/ea/bc/b9/eabcb9d2-c08f-7ca6-5111-478cb7de0082/AppIcon-0-0-1x_U007emarketing-0-0-0-10-85-220.png/150x150bb.png","os":"ios","id":1153461915,"appId":1153461915,"icon":"https://is4-ssl.mzstatic.com/image/thumb/Purple114/v4/ea/bc/b9/eabcb9d2-c08f-7ca6-5111-478cb7de0082/AppIcon-0-0-1x_U007emarketing-0-0-0-10-85-220.png/150x150bb.png","iconUrl":"https://is4-ssl.mzstatic.com/image/thumb/Purple114/v4/ea/bc/b9/eabcb9d2-c08f-7ca6-5111-478cb7de0082/AppIcon-0-0-1x_U007emarketing-0-0-0-10-85-220.png/150x150bb.png","url":"https://apps.apple.com/US/app/id1153461915?l=en","categories":[6014,7017,7014],"valid_countries":["US","AU","CA","CN","FR","DE","GB","IT","JP","KR","RU","DZ","AO","AR","AT","AZ","BB","BY","BE","BM","BR","BG","CL","CO","CR","HR","CZ","DK","DO","EC","EG","SV","FI","GH","GR","GT","HK","HU","IN","ID","IE","IL","KZ","KE","KW","LB","LT","LU","MO","MG","MY","MX","NL","NZ","NG","NO","OM","PK","PA","PE","PH","PL","PT","QA","RO","SA","SG","SK","SI","ZA","ES","LK","SE","CH","TW","TH","TN","TR","UA","AE","UY","UZ","VE","VN","BO","KH","EE","LV","NI","PY","AF","GE","IQ","LY","MA","MZ","MM","YE"],"app_view_url":"/ios/us/dhgames-limited/app/idle-heroes-idle-games/1153461915/","publisher_profile_url":"/ios/publisher/dhgames-limited/463987809","release_date":"2016-11-09T12:09:51Z","updated_date":"2021-01-13T00:00:00Z","in_app_purchases":true,"shows_ads":true,"buys_ads":true,"rating":4.75867,"price":0.0,"global_rating_count":309973,"rating_count":83547,"rating_count_for_current_version":83547,"rating_for_current_version":4.75867,"version":"1.31.3","apple_watch_enabled":null,"apple_watch_icon":null,"imessage_enabled":null,"imessage_icon":null,"humanized_worldwide_last_month_downloads":{"downloads":100000,"downloads_rounded":100,"prefix":null,"string":"100k","units":"k"},"humanized_worldwide_last_month_revenue":{"prefix":"$","revenue":4000000,"revenue_rounded":4,"string":"$4m","units":"m"},"bundle_id":"com.droidhang.ad","support_url":"https://www.facebook.com/IdleHeroes","website_url":null,"privacy_policy_url":"http://www.droidhang.com/privacy.html","eula_url":null,"publisher_email":null,"publisher_address":null,"publisher_country":"China","feature_graphic":null,"short_description":null,"advisories":["Infrequent/Mild Cartoon or Fantasy Violence"],"content_rating":"9+","rank":55,"delta":38,"downloads_revenue_date":"2021-01-01T00:00:00Z"}

"""
RESTful

rating/<game_id>
    grab list of game id, name -> ask user for name 

earnings/all (data including game : name/platform/ranktype)
earnings/ranktype_platform ()

game/search (use request.args params) display information on a game/platform user requests
    does it need to search by id?

"""

