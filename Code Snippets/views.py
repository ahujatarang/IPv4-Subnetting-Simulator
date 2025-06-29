from django.shortcuts import render 
from django.http import HttpResponse 
import random
from .models import Addressing

# View to handle the simulation logic
def sim(request): 
    # Generate random Class A/B/C IP address components
    ip1=str(random.randint(120,223)) 
    ip2=str(random.randint(0,255)) 
    ip3=str(random.randint(0,255)) 
    ip4=str(random.randint(0,255)) 
    ip4x=str(random.randint(0,255))  # Second IP for comparison
    block= str(random.randint(24,30))  # Random subnet mask block

    # Format IPs
    ip=ip1 + "." + ip2 + "." + ip3 + "." + ip4 
    ipx=ip1 + "." + ip2 + "." + ip3 + "." + ip4x

    # Create Addressing object and extract subnetting details
    x =ip +"/"+block
    obj1=Addressing(ip,block,ip4x) 
    classs=obj1.className() 
    subnet=obj1.subnet() 
    host=obj1.host()
    mask = obj1.mask() 
    compare=obj1.IpCompare() 

    # Pass results to frontend template
    return render(request,'sim1.html', {
                   'title':"Simulation",
                   'ip':x,
                   'ipx':ipx,
                   'class':classs,
                   'subnet':s ubnet,
                   'host':host,
                   'mask':mask,
                   'compare':compare})

# View for main simulator page
def mainpage(request):
    return render(request,'mainpage.html',{'title':"IPv4 Subnetting"})

# View for first landing page
def firstpage(request):
    return render(request,'firstpage.html',{'title':"Virtual Labs"})
