from rest_framework import generics
from .models import ShrtTrmCh
from .serializer import SendShrtTrmSerializer, ReceivedShrtTrmSerializer

# Create your views here.
class AllSentChallenges(generics.ListAPIView):
    queryset = ShrtTrmCh.objects.all()
    serializer_class = SendShrtTrmSerializer

all_sent_challenges = AllSentChallenges.as_view()

class CreateChallenge(generics.CreateAPIView):
    queryset = ShrtTrmCh.objects.all()
    serializer_class = SendShrtTrmSerializer

create_challenge = CreateChallenge.as_view()

class AllReceivedChallenges(generics.ListAPIView):
    queryset = ShrtTrmCh.objects.all()
    serializer_class = ReceivedShrtTrmSerializer

all_received_challenges = AllReceivedChallenges.as_view()

class DetailReceivedChallenges(generics.RetrieveAPIView):
    queryset = ShrtTrmCh.objects.all()
    serializer_class = ReceivedShrtTrmSerializer
    lookup_field = "to_user"
    lookup_url_kwarg = "to_user"

detail_received_challenges = DetailReceivedChallenges.as_view()