# SL Test Cricket Player Search Engine

<img src="https://github.com/prahack/sl-cricket-player-search-engine/blob/main/images/img.jpeg?raw=true">

## Example Search Queries
ෆර්විස් මහරුෆ්
* සනත් ජයසූරිය(`by name`)
* ලකුණු 5000 ට වැඩියෙන් රැස් කල ක්‍රීඩකයින්(`by runs`)
* කඩුලු 300 ට  වඩා වැඩිපුර දවා ගත් ක්‍රීඩකයින්(`by wickets`)
* කඩුලු 5 ට  වඩා අඩුවෙන් දවා ගත් ක්‍රීඩකයින්(`by wickets`)
* ලකුණු 10 ට අඩුවෙන් රැස් කල ක්‍රීඩකයින්(`by runs`)
* මාතර (`by description`)

## Quick Setup
* clone the project
* start `Elasticsearch` engine
* run `add_bulk.py` file to create and data to the index
* run `app.py` and open the search engine frontend
* run some search queries to see results :)

## Data
The data contains about all the players of the Sri Lanka mainly scraped from the [Wikipedia](https://en.wikipedia.org/) and [ESPN](https://www.espncricinfo.com/) sites.
### fields
* name
* birthday
* description
* career
* batting
* bowling
* matches 
* runs
* wickets
* top_score
* best_bowling

## Files for quick setup
corpus - `corpus/player_data.json` 

add data - `add_bulk.py`

flask backend - `app.py`