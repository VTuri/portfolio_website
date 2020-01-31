from django.shortcuts import render

# Create your views here.

data = [{"Date": "1.02.2020", "Event": "Webtalk Invite Day - Valletta - Malta", "Location": "Valletta",
         "Type": ["Blockchain & Tech"], "Venue": "Upper Barrakka..."},
        {"Date": "1.02.2020", "Event": "Cleaun up yacht charter by Holidays in Malta ltd", "Location": "Pieta",
         "Type": ["Special Events"], "Venue": "Marina di Valletta"},
        {"Date": "1.02.2020", "Event": "Valletta 300m Zipline", "Location": "Valletta", "Type": ["Sports"],
         "Venue": "Valletta"},
        {"Date": "1.02.2020", "Event": "\u017bigu\u017bajg Season: Kids Dig Science", "Location": "Valletta",
         "Type": ["Kids"], "Venue": "St. James Cavalier"},
        {"Date": "1.02.2020", "Event": "Diploma in Adult Education, Training & Development", "Location": "Msida",
         "Type": ["NONE"], "Venue": "University of Malta"},
        {"Date": "1.02.2020", "Event": "Surf & Turf at Fra Martino", "Location": "St Julians",
         "Type": ["Special Events"], "Venue": "Corinthia Hotel..."},
        {"Date": "1.02.2020", "Event": "The 20th Century Clarinet (Clarinet Recital)", "Location": "Valletta",
         "Type": ["Music"], "Venue": "Palazzo De La Salle"},
        {"Date": "31.01.2020", "Event": "The Importance of Being Earnest", "Location": "Valletta", "Type": ["Theatre"],
         "Venue": "Manoel Theatre"},
        {"Date": "2.02.2020", "Event": "Challenge walk around malta tail", "Location": "Mellieha", "Type": ["Sports"],
         "Venue": "St Agatha's..."},
        {"Date": "2.02.2020", "Event": "Sunday Buffet Lunch at Fra Martino", "Location": "St Julians",
         "Type": ["Special Events"], "Venue": "Corinthia Hotel..."},
        {"Date": "31.01.2020", "Event": "The Importance of Being Earnest", "Location": "Valletta", "Type": ["Theatre"],
         "Venue": "Manoel Theatre"},
        {"Date": "3.02.2020", "Event": "PRINCE2 - Foundation & Practitioner (Project Management)",
         "Location": "Ta' Xbiex", "Type": ["Learning"], "Venue": "People & Co...."},
        {"Date": "3.02.2020", "Event": "PRINCE2 - Foundation & Practitioner (Project Management)",
         "Location": "Ta' Xbiex", "Type": ["Learning"], "Venue": "People & Co...."},
        {"Date": "4.02.2020", "Event": "Human Resources Foundations", "Location": "Ta' Xbiex", "Type": ["Learning"],
         "Venue": "People & Co...."},
        {"Date": "3.02.2020", "Event": "PRINCE2 - Foundation & Practitioner (Project Management)",
         "Location": "Ta' Xbiex", "Type": ["Learning"], "Venue": "People & Co...."},
        {"Date": "5.02.2020", "Event": "Southern Depth and Northern Lights: Different Likeness", "Location": "Valletta",
         "Type": ["Arts", "Culture"], "Venue": "Malta Society of..."},
        {"Date": "5.02.2020", "Event": "Maltese Night at Fra Martino", "Location": "St Julians",
         "Type": ["Special Events"], "Venue": "Corinthia Hotel..."},
        {"Date": "5.02.2020", "Event": "Bellydance Classes", "Location": "Msida", "Type": ["Learning"],
         "Venue": "dance college..."},
        {"Date": "3.02.2020", "Event": "PRINCE2 - Foundation & Practitioner (Project Management)",
         "Location": "Ta' Xbiex", "Type": ["Learning"], "Venue": "People & Co...."},
        {"Date": "6.02.2020", "Event": "Movimento", "Location": "Valletta", "Type": ["Theatre"],
         "Venue": "MUZA - The Malta..."},
        {"Date": "30.01.2020", "Event": "English Cafe: Make friends & speak English", "Location": "St Julians",
         "Type": ["Special Events"], "Venue": "Me Lounge"},
        {"Date": "30.01.2020", "Event": "Jeudi Jazz", "Location": "Valletta", "Type": ["Music"],
         "Venue": "OffBeat Music Bar"},
        {"Date": "31.01.2020", "Event": "Train the Trainer - Vocational Training Qualification",
         "Location": "Ta' Xbiex", "Type": ["Learning"], "Venue": "People & Co...."},
        {"Date": "3.02.2020", "Event": "PRINCE2 - Foundation & Practitioner (Project Management)",
         "Location": "Ta' Xbiex", "Type": ["Learning"], "Venue": "People & Co...."},
        {"Date": "31.01.2020", "Event": "The Importance of Being Earnest", "Location": "Valletta", "Type": ["Theatre"],
         "Venue": "Manoel Theatre"},
        {"Date": "7.02.2020", "Event": "Kinky Boots", "Location": "St Julians", "Type": ["Theatre"],
         "Venue": "Eden Cinemas"},
        {"Date": "8.02.2020", "Event": "Strauss Composer and Conductor", "Location": "Valletta", "Type": ["Music"],
         "Venue": "Mediterranean..."},
        {"Date": "1.02.2020", "Event": "Surf & Turf at Fra Martino", "Location": "St Julians",
         "Type": ["Special Events"], "Venue": "Corinthia Hotel..."},
        {"Date": "31.01.2020", "Event": "The Importance of Being Earnest", "Location": "Valletta", "Type": ["Theatre"],
         "Venue": "Manoel Theatre"},
        {"Date": "2.02.2020", "Event": "Sunday Buffet Lunch at Fra Martino", "Location": "St Julians",
         "Type": ["Special Events"], "Venue": "Corinthia Hotel..."},
        {"Date": "7.02.2020", "Event": "Kinky Boots", "Location": "St Julians", "Type": ["Theatre"],
         "Venue": "Eden Cinemas"},
        {"Date": "31.01.2020", "Event": "The Importance of Being Earnest", "Location": "Valletta", "Type": ["Theatre"],
         "Venue": "Manoel Theatre"}]


#
# def whatson_scrape(request):
#
#     return JsonResponse(data, safe=False, )

def whatson_scrape(request):
    context = {
        "data": data,
    }
    return render(request, "whatson_scrape.html", context)
