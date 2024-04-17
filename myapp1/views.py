from django.shortcuts import render
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed')
    html = """
    <html>
        <head>
        <title>Internet Shop</title>
            <style>
                .column {
                    width: 33.33%;
                    float: left;
                    padding: 10px;
                    box-sizing: border-box;
                }
                .clear {
                    clear: both;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to our Internet Shop!</h1>
                <p>Explore our wide range of products.</p>
                <p><img width="50%" height="50%" src="https://eurobyte.ru/img/articles/plyusy-i-minusy-internet-magazina/image1.png" alt="Shop"></p>          
            <div class="column">
                <h2>Clothes</h2>
                    <p>Clothing and shoes from the best distributors.</p>
            </div>
            <div class="column">
                <h2>Products</h2>
                    <p>Fresh products and fast delivery.</p>
            </div>
            <div class="column">
                <h2>Electronics</h2>
                    <p>Original goods at low prices.</p>
            </div>
            <div class="clear"></div>
            <button><a href="/about">Learn more</a></button>
        </body>
    </html>
    """
    return HttpResponse(html)

def about(request):
    logger.info('About page accessed')
    html = """
    <html>
        <head>
            <title>About Us</title>
        </head>
        <body>
            <h1>About Us</h1>
            <p>Internet Shop founded in 2024.</p>
            <p>Our mission.</p>
            <h4>Make life easier</h4>
        </body>
    </html>
    """
    return HttpResponse(html)