from django.shortcuts import redirect, render
import random
from datetime import datetime

# Create your views here.
def home(request):
    if "gold" not in request.session or 'log' not in request.session:
        request.session["gold"] = 0
        request.session["log"] = []
        request.session["log"].append("Welcome!!! " + "(" + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ")")
        request.session["count"] = 0
    return render(request, "index.html")

def reset(request):
    request.session.flush()
    return redirect("/")

def process_money(request):
    if request.method == "GET":
        return redirect("/")
    elif request.method == "POST":
        request.session["count"] += 1
        if request.POST["farming"] == "farm":
            gold = random.randint(10,20)
            request.session["log"].append("Earned " + str(gold) + " gold from the farm! " + "(" + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ")")
        if request.POST["farming"] == "cave":
            gold = random.randint(5,10)
            request.session["log"].append("Earned " + str(gold) + " golds from the cave! " + "(" + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ")")
        if request.POST["farming"] == "house":
            gold = random.randint(2,5)
            request.session["log"].append("Earned " + str(gold) + " golds from the house! " + "(" + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ")")
        if request.POST["farming"] == "casino":
            gold = random.randint(-50,50)
            if gold > 0:
                request.session["log"].append("Entered a casino and win " + str(gold) + " golds... Congrats!!!" + "(" + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ")")
            else:
                request.session["log"].append("Entered a casino and lost " + str(gold)[1:] + " golds... Ouch!!!!" + "(" + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ")")
        
        request.session["gold"] += gold

        if request.session["gold"] >= 100:
            return render(request, "win.html")

        if request.session["gold"] <= -20:
            return render(request, "lost.html")

        
        ## logeando en consola los datos del post
        #for key, value in request.POST.items():
        #    print(f'Key: %s' % (key) ) 
        #    print(f'Value %s' % (value) )
        
        return redirect("/")
    