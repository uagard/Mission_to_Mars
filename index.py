<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Mission to Mars</title>
    <link
      rel="stylesheet"
      href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
    />
  </head>
  <body>
    <div class="container">
      <!-- Add Jumbotron to Header -->
      <div class="jumbotron text-center">
        <h1>Mission to Mars</h1>
        <!-- Add a button to activate scraping script -->
        <p><a class="btn btn-primary btn-lg" href="/scrape" role="button">Scrape New Data</a></p>
      </div>
      <!-- Add section for Mars News -->
      <div class="row" id="mars-news">
        <div class="col-md-12">
          <div class="media">
            <div class="media-body">
              <h2>Latest Mars News</h2>
              <h4 class="media-heading">{{ mars.news_title }}</h4>
              <p>{{ mars.news_paragraph }}</p>
            </div>
          </div>
        </div>
      </div>
      <!-- Section for Featured Image and Facts table -->
      <div class="row" id="mars-featured-image">
        <div class="col-md-8">
          <h2>Featured Mars Image</h2>
          <img
            src="{{mars.featured_image }}"
            class="img-responsive"
            alt="Responsive image"
          />
        </div>
        <div class="col-md-4">
          <!-- Mars Facts -->
          <div class="row" id="mars-facts">
            <h4>Mars Facts</h4>
            {{ mars.facts | safe }}
          </div>
        </div>
      </div>
    </div>
  </body>
</html>