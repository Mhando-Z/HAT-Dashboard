from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from .models import *
from . seriallizer import *

# HERO SECTION


@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def HeroSect(request):
    if request.method == 'GET':
        herosection = HeroSection.objects.all()
        serializers = HeroSectionSerial(herosection, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializer = HeroSectionSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def heroSection_details(request, pk):
    try:
        heroSection = HeroSection.objects.get(pk=pk)
    except HeroSection.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HeroSectionSerial(heroSection)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HeroSectionSerial(
            heroSection, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        heroSection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# PRESIDENT SPEECH SECTION


@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def PresidentSect(request):
    if request.method == 'GET':
        presidentspeech = PresidentSpeech.objects.all()
        serializers = PresidentSerial(presidentspeech, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = PresidentSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def President_details(request, pk):
    try:
        presidentSpeech = PresidentSpeech.objects.get(pk=pk)
    except PresidentSpeech.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PresidentSerial(presidentSpeech)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PresidentSerial(
            presidentSpeech, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        presidentSpeech.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ABOUT US SECTION


@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def AboutUsSect(request):
    if request.method == 'GET':
        aboutus = AboutUs.objects.all()
        serializers = AboutSerial(aboutus, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = AboutSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def AboutUs_details(request, pk):
    try:
        aboutUs = AboutUs.objects.get(pk=pk)
    except AboutUs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AboutSerial(aboutUs)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AboutSerial(aboutUs, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        aboutUs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# CONTACT SECTION


@api_view(['GET', 'POST'])
def ContactSect(request):
    if request.method == 'GET':
        contacts = Contacts.objects.all()
        serializers = ContactSerial(contacts, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = ContactSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def Contacts_details(request, pk):
    try:
        contacts = Contacts.objects.get(pk=pk)
    except Contacts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContactSerial(contacts)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContactSerial(contacts, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        contacts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# TERMS OF SERVICES SECTION


@api_view(['GET', 'POST'])
def TermsSect(request):
    if request.method == 'GET':
        terms = TermsofService.objects.all()
        serializers = TermsSerial(terms, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = TermsSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def Terms_details(request, pk):
    try:
        terms = TermsofService.objects.get(pk=pk)
    except TermsofService.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TermsSerial(terms)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TermsSerial(terms, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        terms.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# POLICIES SECTION


@api_view(['GET', 'POST'])
def PoliciesSect(request):
    if request.method == 'GET':
        policies = Policies.objects.all()
        serializers = PoliciesSerial(policies, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = PoliciesSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def Policies_details(request, pk):
    try:
        policies = Policies.objects.get(pk=pk)
    except Policies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PoliciesSerial(policies)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PoliciesSerial(policies, data=request.data, partial=True)
        print(policies)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        policies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# STAFF SECTION


@api_view(['GET', 'POST'])
def StaffsSect(request):
    if request.method == 'GET':
        staffs = Staffs.objects.all()
        serializers = StaffsSerial(staffs, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = StaffsSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def Staffs_details(request, pk):
    try:
        staffs = Staffs.objects.get(pk=pk)
    except Staffs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StaffsSerial(staffs)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StaffsSerial(staffs, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        staffs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# CONFERENCE SECTION


@api_view(['GET', 'POST'])
def ConferenceSect(request):
    if request.method == 'GET':
        conference = Conference.objects.all()
        serializers = ConferenceSerial(conference, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = ConferenceSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def Conference_details(request, pk):
    try:
        conference = Conference.objects.get(pk=pk)
    except Conference.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ConferenceSerial(conference)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ConferenceSerial(
            conference, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        conference.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# GALLERY SECTION


@api_view(['GET', 'POST'])
def GallerySect(request):
    if request.method == 'GET':
        gallery = Gallery.objects.all()
        serializers = GallerySerial(gallery, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = GallerySerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def Gallery_details(request, pk):
    try:
        gallery = Gallery.objects.get(pk=pk)
    except Gallery.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GallerySerial(gallery)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GallerySerial(gallery, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        gallery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# RESOURCE AND PUBLICATION SECTION


@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def ResourceSectt(request):
    if request.method == 'GET':
        resources = Resource.objects.all()
        serializers = ResourceSerializer(resources, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        serializer = ResourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def resource_detail(request, pk):
    try:
        resource = Resource.objects.get(pk=pk)
    except Resource.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ResourceSerializer(resource)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ResourceSerializer(
            resource, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        resource.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# COMPANIES SECTION


@api_view(['GET', 'POST'])
def PartnersSect(request):
    if request.method == 'GET':
        companies = Companies.objects.all()
        serializers = CompanySerial(companies, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = CompanySerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def Partners_details(request, pk):
    try:
        company = Companies.objects.get(pk=pk)
    except Companies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CompanySerial(company)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CompanySerial(company, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ANNOUNCEMENTS SECTION


@api_view(['GET', 'POST'])
def AnnounceSect(request):
    if request.method == 'GET':
        announce = Announce.objects.all()
        serializers = AnnounceSerial(announce, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = AnnounceSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def Announce_details(request, pk):
    try:
        announce = Announce.objects.get(pk=pk)
    except Announce.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AnnounceSerial(announce)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AnnounceSerial(announce, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        announce.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# FOOTER SECTION


@api_view(['GET', 'POST'])
def FooterSect(request):
    if request.method == 'GET':
        footer = Footer.objects.all()
        serializers = FooterSerial(footer, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = FooterSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def Footer_details(request, pk):
    try:
        footer = Footer.objects.get(pk=pk)
    except Footer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FooterSerial(footer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FooterSerial(footer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        footer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
