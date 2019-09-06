from django.shortcuts import render, HttpResponse

htmlBase = """

    <h1> Personal Portfolio </h1>
    <ul>
        <li><a href="/">Homepage</a></li>
        <li><a href="/about-me">About me</a></li>
        <li><a href="/portfolio">Portfolio</a></li>
        <li><a href="/contact">Contact me</a></li>
    </ul>

"""

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    text = "<h2> About me </h2>"
    return HttpResponse(htmlBase + text)

def portfolio(request):
    text = """
        <h2> Portfolio </h2>
        <ul>
            <li><a href="#">My first project</a></li>
            <li><a href="#">My second project</a></li>
        </ul>
        """
    return HttpResponse(htmlBase + text)

def contact(request):
    text = """
        <h2> Contact me </h2>
        <ul>
            <li><a href="https://github.com/QiqeMtz" target="_blank">This is my Github</a></li>
        </ul>
        """
    return HttpResponse(htmlBase + text)