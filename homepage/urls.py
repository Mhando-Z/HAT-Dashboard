from django.urls import path
from . import views

urlpatterns = [
    # Section Endpoints
    path("heroSect/", views.HeroSect, name="HeroSection"),
    path("President/", views.PresidentSect, name="President"),
    path("AboutUs/", views.AboutUsSect, name="AboutUs"),
    path("Footer/", views.FooterSect, name="Footer"),
    path("Contact/", views.ContactSect, name="Contact"),
    path("TermsofServices/", views.TermsSect, name="Terms"),
    path("Policies/", views.PoliciesSect, name="Policies"),
    path("Conference/", views.ConferenceSect, name="Conference"),
    path("Staffs/", views.StaffsSect, name="Staffs"),
    path("Announce/", views.AnnounceSect, name="Announce"),
    path("Gallery/", views.GallerySect, name="Gallery"),
    path("Companies/", views.PartnersSect, name="Companies"),
    path('Resources/', views.ResourceSectt, name='resources'),

    # Detail Endpoints
    path('Resources_Details/<str:pk>/',
         views.resource_detail, name='resource_detail'),
    path("Companies_Details/<str:pk>/",
         views.Partners_details, name="CompaniesDetails"),
    path("Announce_Details/<str:pk>/",
         views.Announce_details, name="AnnounceDetails"),
    path("Gallery_Details/<str:pk>/",
         views.Gallery_details, name="GalleryDetails"),
    path("Contact_Details/<str:pk>/",
         views.Contacts_details, name="ContactDetails"),
    path("Conference_Details/<str:pk>/",
         views.Conference_details, name="ConferenceDetails"),
    path("Hero_Details/<str:pk>/", views.heroSection_details, name="HeroDetails"),
    path("About_Details/<str:pk>/", views.AboutUs_details, name="AboutDetails"),
    path("Terms_Details/<str:pk>/", views.Terms_details, name="TermsDetails"),
    path("Policies_Details/<str:pk>/",
         views.Policies_details, name="PoliciesDetails"),
    path("President_Details/<str:pk>/",
         views.President_details, name="PresidentDetails"),
    path("Staffs_Details/<str:pk>/", views.Staffs_details, name="StaffsDetails"),
]
