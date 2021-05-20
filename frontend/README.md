# Frontend code

## STEP 1: Installing Dependencies
run `npm install` in your terminal to install package dependencies

## STEP 2: Start solr
navigate to the `solr-7.7.3` folder inside the `backend` folder and run solr by typing `./bin/solr start`

## STEP 3: Start the Frontend Server
run `npm start` in your terminal to start the server

## STEP 4: Using the Application
navigate to `localhost:3000` to access the application. The application is shown by the image below:

![Image of Application](https://github.com/tkhang1999/CZ4034-Team-11/blob/master/image1.png)

The application allows you to:
1. Enter a **search/query** term (search bar)
2. Filter your query by the **Country** the tweet originated from (dropdown)
3. Filter your query by the **Subjectivity** tag of the tweet (dropdown)
4. Filter your query by the **Toxicity** tag of the tweet (dropdown)

The application is equiped with a **MAP** as shown in the image below. The map view shows the origins of the tweets in the current page. It will show the location of the 100 tweets retrieved in one page

![Image of Map](https://github.com/tkhang1999/CZ4034-Team-11/blob/master/image3.png)

The application is also equiped with a **DOUGHNUT CHART** as shown in the image below. The donught chart visualises the tag proportion of the tweets retrieved in a page.

![Image of Chart](https://github.com/tkhang1999/CZ4034-Team-11/blob/master/image2.png)

The application also provides suggestions for spell-corrections when only a small number of results are returned from the query as shown in the image below

![Image of Spell Check](https://github.com/tkhang1999/CZ4034-Team-11/blob/master/image4.png)

You can also find more suggestions of spell-corrected words by clicking **more**

![Image of Spell Check 2](https://github.com/tkhang1999/CZ4034-Team-11/blob/master/image5.png)
