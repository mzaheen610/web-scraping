Project requirements

Given a URL as command line arguments
1. Run a concurrent application , whose concurrency can be controlled
2. The application should take all the pages from that site. 
3. Use in-memory queue
4. From the HTML page received , create a document having URL , Title , H1 text , H2 text and size of HTML , response code and time to download
5. No URL from other domains should be added , it should take only the URL from that domain
6. Following should be configurable
    a. Concurrency
    b. Max number of pages
    c. Max timeout to download a page
    d. Number of retry

Coding guidelines
1. Only one class per file
2. Maximum 20 lines per function
3. Maximum 200 lines per file

