from django.http import HttpResponse, JsonResponse
from .serializer import MeetingsSerializer, RegistrationSerializer, RequestsSerializer, TimeWindowSerializer
from .models import Babysitter, Meetings, Requests, TimeWindow
from .serializer import BabysitterSerializer
from .models import Parents
from .serializer import ParentsSerializer
from .models import Kids
from .serializer import KidsSerializer
from .models import Reviews
from .serializer import ReviewsSerializer
from .models import Availability
from .serializer import AvailabilitySerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import permissions , viewsets , generics




def index(req):
    return HttpResponse("hello world")


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


#i’m protected
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def about(req): 
 return HttpResponse("about")



@api_view(['POST'])
def register(request):
    # Create the user
    user_serializer = RegistrationSerializer(data=request.data)
    if not user_serializer.is_valid():
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializers_map = {
        'Babysitter': BabysitterSerializer,
        'Parent': ParentsSerializer,    
    }
    user_type = request.data.get('user_type', None)
    profile_serializer_class = serializers_map.get(user_type)
    if profile_serializer_class is None:
        return Response({"error" : "invalid user type"} , status=status.HTTP_400_BAD_REQUEST)

    profile_serializer = profile_serializer_class(data = request.data)
    if not profile_serializer.is_valid():
        return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    user = user_serializer.save()
    profile_serializer.save(user = user)
    return Response({"message" : f"{user_type} User created successfuly"} , status=status.HTTP_201_CREATED)



# Babysitter crud 

# get requests - if admin show all babysitters
class BabysitterViewSet(viewsets.ModelViewSet):
    serializer_class = BabysitterSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admin users can access

    def get_queryset(self):
        # Admin users see all Parents records; non-admin users see nothing
        return Babysitter.objects.all()
    
    def update(self, request, *args, **kwargs):
        # Handle updates for admin users
        try:
            partial = kwargs.pop('partial', False)
            babysitter = self.get_object()
            serializer = self.get_serializer(babysitter, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        print("hi")
        return Response({"error": str()}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Get the ID from the URL
            babysitter_id = kwargs.get('pk')
            babysitter = Babysitter.objects.get(id=babysitter_id)  # Retrieve by ID

            # Mark as inactive
            babysitter.is_active = False
            babysitter.save()

            return Response(
                {"message": f"Babysitter with ID {babysitter_id} deleted successfully."},
                status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
# get requests - show info for the logged in babysitter 
class BabysitterProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = BabysitterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        Babysitter.objects.get(user = self.request.user)




# Parents crud
def TheParents(req):
    all_products = ParentsSerializer(Parents.objects.all(), many=True).data
    return JsonResponse(all_products, safe=False)

# get requests - if admin show all babysitters
class BabysitterViewSet(viewsets.ModelViewSet):
    serializer_class = BabysitterSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admin users can access

    def get_queryset(self):
        # Admin users see all Parents records; non-admin users see nothing
        return Babysitter.objects.all()
    
# get requests - show info for the logged in babysitter 
class BabysitterProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = BabysitterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        Babysitter.objects.get(user = self.request.user)











# create+read+update+delete
# Kids crud
def TheKids(req):
    all_products = KidsSerializer(Kids.objects.all(), many=True).data
    return JsonResponse(all_products, safe=False)

# create+read
# Info crud
def TheMeetings(req):
    all_products = MeetingsSerializer(Meetings.objects.all(), many=True).data
    return JsonResponse(all_products, safe=False)

# create+read
# Reviews crud
def TheReviews(req):
    all_products = ReviewsSerializer(Reviews.objects.all(), many=True).data
    return JsonResponse(all_products, safe=False)

# create+read+update+delete
# Availability crud
def TheAvailability(req):
    all_products = AvailabilitySerializer(Availability.objects.all(), many=True).data
    return JsonResponse(all_products, safe=False)

# create+read
# Message crud
def TheRequests(req):
    all_products = RequestsSerializer(Requests.objects.all(), many=True).data
    return JsonResponse(all_products, safe=False)

# create +read+update
# Time window crud
def TheTimeWindow(req):
    all_products = TimeWindowSerializer(TimeWindow.objects.all(), many=True).data
    return JsonResponse(all_products, safe=False)